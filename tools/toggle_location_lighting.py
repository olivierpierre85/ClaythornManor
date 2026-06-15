import argparse
import base64
import json
import os
import pathlib
import urllib.request
from PIL import Image

ROOT = pathlib.Path(__file__).parent.parent.resolve()
MD_FILE = ROOT / "Murder/game/images/locations/_locations.md"
CHOICES_DIR = ROOT / "Images/locations_new/flux_2_final_choices"

API_URL = "http://127.0.0.1:7860"
IMG2IMG = "/sdapi/v1/img2img"

PROMPT_TEMPLATES = {
    "interior_night": (
        "A high-quality semi-realistic digital painting of a 1920s Scottish manor "
        "{description} at night. Warm amber light, touches of colorful objects. "
        "Deep soft shadows, mysterious atmosphere, wide shot, empty room, rich textures."
    ),
    "interior_day": (
        "A high-quality semi-realistic digital painting of a 1920s Scottish manor "
        "{description} by day. Bright natural daylight streaming in, clear sunny atmosphere. "
        "Wide shot, empty room, rich textures, detailed."
    ),
    "outdoor_night": (
        "A high-quality semi-realistic digital painting of a {description} at night."
        "Deep soft shadows, mysterious atmosphere, wide shot, "
        "rich textures."
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
        
    print(f"Source file: {filename}")
    print(f"Detected room ID: {rid}")
    print(f"Target lighting: {target_time}")
    print(f"Target file will be: {target_path.name}")
    
    # 3. Generate the image using img2img
    print(f"Encoding source image...")
    init_b64 = b64_encode(image_path)
    
    prompt_key = f"{loc_type}_{target_time}"
    prompt = PROMPT_TEMPLATES[prompt_key].format(description=desc)
    
    payload = {
        "prompt": prompt,
        "negative_prompt": NEGATIVE_PROMPT,
        "init_images": [init_b64],
        "denoising_strength": 0.75,
        "width": 1920,
        "height": 1088,
        "steps": 20,
        "cfg_scale": 1.0,
        "distilled_cfg_scale": 3.5,
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
