import argparse
import base64
import io
import json
import os
import pathlib
import urllib.request
from PIL import Image, ImageEnhance

ROOT = pathlib.Path(__file__).parent.parent.resolve()
MD_FILE = ROOT / "Murder/game/images/locations/_locations.md"
CHOICES_DIR = ROOT / "Images/locations_new/flux_2_final_choices"

API_URL = "http://127.0.0.1:7860"
IMG2IMG = "/sdapi/v1/img2img"

PROMPT_TEMPLATES = {
    "interior_night": (
        "A high-quality semi-realistic digital painting of a 1920s Scottish manor "
        "{description} at night. The only light is the warm golden glow of oil lamps "
        "and candlelight, strong cosy amber lighting filling the room, warm pools of "
        "light, deep warm shadows in the corners. The windows are dark and unlit with "
        "no light coming from outside. Warm candlelit nocturnal interior, wide shot, "
        "empty room, rich textures. No daylight, no blue light."
    ),
    "interior_day": (
        "A high-quality semi-realistic digital painting of a 1920s Scottish manor "
        "{description} by day. Soft muted daylight filtering through the windows, "
        "overcast grey light, subdued and dim, gentle soft shadows, quiet mysterious "
        "atmosphere, wide shot, empty room, rich textures, detailed."
    ),
    "outdoor_night": (
        "A high-quality semi-realistic digital painting of a {description} at night. "
        "Very dark, dark overcast cloudy night sky, cool blue ambient light, long "
        "shadows, cold nocturnal atmosphere, deep shadows, wide shot, rich textures. "
        "No sun, no sunlight."
    ),
    "outdoor_day": (
        "A high-quality semi-realistic digital painting of a {description} by day. "
        "Bright natural daylight, clear sunny atmosphere, wide shot, rich textures."
    ),
}

NEGATIVE_PROMPT = (
    "people, person, human, figure, crowd, text, signature, watermark, "
    "blurry, low quality, deformed, cartoon, anime"
)

# Extra negatives only applied when the target lighting is night, to push out the
# leftover daylight that img2img tends to keep from a bright day source.
NIGHT_NEGATIVE_EXTRA = (
    "daylight, sunlight, sunbeams, god rays, golden hour, sunset, sunrise, "
    "bright sky, blue sky, bright daylight, glowing windows, overexposed, warm sunlight, "
    "moon, stars, starry sky"
)

# Extra negatives for interior daytime, to keep the manor's mystery: a soft, dim,
# overcast room instead of a bright cheerful sunny one.
INTERIOR_DAY_NEGATIVE_EXTRA = (
    "bright sunlight, harsh sunlight, direct sunbeams, sunny, cheerful, "
    "blown highlights, overexposed, hdr, washed out"
)

# _locations.md files some genuinely interior rooms under its "Outdoor locations"
# heading (e.g. broken_flat, a pauper apartment interior). Force them onto the interior
# lighting path so day -> night gets the warm-lamp treatment, not the cold outdoor grade.
FORCE_INTERIOR = {"broken_flat"}

def parse_locations():
    rows = {}
    template_type = "interior"
    for raw in MD_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("#"):
            low = line.lower()
            if any(k in low for k in ("outdoor", "outside", "exterior")):
                template_type = "outdoor"
            elif "interior" in low:
                template_type = "interior"
            continue
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        rid, desc = cells[0], cells[1]
        if rid.lower() == "id" or set(rid) <= set("-: "):
            continue
        rid = rid.strip("`").strip()
        if rid and desc:
            rows[rid] = {"desc": desc, "type": template_type}
    return rows

def post_json(path, payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        API_URL + path, data=data, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=600) as resp:
        return json.loads(resp.read().decode("utf-8"))

def b64_encode(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def encode_image(img):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("utf-8")

def process_toggle(image_path):
    image_path = pathlib.Path(image_path).resolve()
    if not image_path.exists():
        raise FileNotFoundError(f"Input file not found: {image_path}")

    filename = image_path.name
    stem = image_path.stem  # e.g., bedroom_doctor_day
    
    # 1. Determine base room ID and target lighting
    if stem.endswith("_day"):
        rid = stem[:-4]
        target_time = "night"
        target_stem = f"{rid}_night"
    elif stem.endswith("_night"):
        rid = stem[:-6]
        target_time = "day"
        target_stem = f"{rid}_day"
    else:
        rid = stem
        target_time = "day"
        target_stem = f"{rid}_day"
        
    target_path = image_path.parent / f"{target_stem}.png"
    
    # 2. Get description and type
    locations = parse_locations()
    if rid not in locations:
        # Fallback if the filename is not in _locations.md
        print(f"Warning: Room ID '{rid}' not found in _locations.md. Using a generic prompt.")
        desc = rid.replace("_", " ")
        loc_type = "interior"
    else:
        desc = locations[rid]["desc"]
        loc_type = locations[rid]["type"]

    if rid in FORCE_INTERIOR:
        loc_type = "interior"
        
    print(f"Source file: {filename}")
    print(f"Detected room ID: {rid}")
    print(f"Target lighting: {target_time}")
    print(f"Target file will be: {target_path.name}")
    
    # 3. Generate the image using img2img
    print(f"Encoding source image...")
    src_img = Image.open(image_path).convert("RGB")
    if target_time == "night" and loc_type == "interior":
        # Pre-darken the day source so the bright daylit window stops anchoring the
        # relight; the warm lamp prompt then fills the dark room with golden light
        # instead of the model applying a flat cold night grade with the lamps off.
        src_img = ImageEnhance.Brightness(src_img).enhance(0.35)
        src_img = ImageEnhance.Color(src_img).enhance(0.7)
    init_b64 = encode_image(src_img)
    
    prompt_key = f"{loc_type}_{target_time}"
    prompt = PROMPT_TEMPLATES[prompt_key].format(description=desc)

    # Day -> night is the hard direction: the bright day source bleeds through as a
    # luminance anchor, so push the denoise harder and fight daylight in the negative.
    if target_time == "night":
        negative_prompt = f"{NEGATIVE_PROMPT}, {NIGHT_NEGATIVE_EXTRA}"
        distilled_cfg_scale = 4.0
        if loc_type == "interior":
            # The window-killing denoise works, but the model's night grade turns the
            # room cold and snuffs the lamps. Keep the denoise and force warmth: fight
            # the cool grade in the negative so the warm lamp glow survives.
            negative_prompt += ", cold blue light, cool tones, blue cast, desaturated, dark gloomy room"
            denoising_strength = 0.72
        else:
            denoising_strength = 0.88
    else:
        denoising_strength = 0.75
        distilled_cfg_scale = 3.5
        if loc_type == "interior":
            # Keep interior manor rooms moody by day rather than bright and cheerful.
            negative_prompt = f"{NEGATIVE_PROMPT}, {INTERIOR_DAY_NEGATIVE_EXTRA}"
        else:
            negative_prompt = NEGATIVE_PROMPT

    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "init_images": [init_b64],
        "denoising_strength": denoising_strength,
        "width": 1920,
        "height": 1088,
        "steps": 20,
        "cfg_scale": 1.0,
        "distilled_cfg_scale": distilled_cfg_scale,
        "sampler_name": "Euler a",
        "scheduler": "Beta",
        "seed": 1924,
        "send_images": True,
        "save_images": False,
    }
    
    print(f"Sending img2img request to FLUX.2 server...")
    res = post_json(IMG2IMG, payload)
    img_b64 = res["images"][0]
    
    target_path.write_bytes(base64.b64decode(img_b64))
    print(f"Successfully saved new toggled image to: {target_path}")

def main():
    ap = argparse.ArgumentParser(description="Toggle image between day and night automatically.")
    ap.add_argument("image_path", help="Path to the source image file")
    args = ap.parse_args()
    
    try:
        process_toggle(args.image_path)
    except Exception as e:
        print(f"Error: {e}")
        raise SystemExit(1)

if __name__ == "__main__":
    main()
