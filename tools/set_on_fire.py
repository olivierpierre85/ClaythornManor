"""Set an existing Claythorn Manor location image on fire.

An img2img pass on the local FLUX.2 Klein server (Forge Neo, A1111-compatible API
at http://127.0.0.1:7860), same server as tools/toggle_location_lighting.py. The
source image is kept as the composition anchor, so the burning version shows the
*same* room or building rather than a new one.

The room description and the interior/outdoor template are read from
    Murder/game/images/locations/_locations.md
using the id parsed off the filename (billiard_room_day.png -> billiard_room).

Denoising strength is the dial between "the same picture, now alight" and "a
picture of a fire": 0.55 keeps the source almost intact and was the value chosen
for manor_on_fire; 0.65-0.75 give progressively bigger blazes and progressively
more drift from the original.

Usage (from the repo root):
    python tools/set_on_fire.py Murder/game/images/locations/billiard_room_day.png
    python tools/set_on_fire.py <image> -n 4                # 4 seeds
    python tools/set_on_fire.py <image> --denoise 0.65      # bigger blaze
    python tools/set_on_fire.py <image> --denoise 0.55 0.65 # one image per value
    python tools/set_on_fire.py <image> --out some/dir
"""
import argparse
import base64
import json
import pathlib
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).parent.parent
MD_FILE = ROOT / "Murder/game/images/locations/_locations.md"
DEFAULT_OUT = ROOT / "Images/locations_new/generated"

API_URL = "http://127.0.0.1:7860"
IMG2IMG = "/sdapi/v1/img2img"

# The fire wording is deliberately concrete about where the flames are: Klein
# otherwise re-lights the whole frame orange without ever drawing a flame.
PROMPT_TEMPLATES = {
    "interior": (
        "A high-quality semi-realistic digital painting of a 1920s Scottish manor "
        "{description}, the room on fire: tall orange flames climbing the walls and "
        "curtains, the furniture alight and burning, fire spreading across the floor, "
        "thick black smoke rolling along the ceiling, burning embers in the air, "
        "everything lit by the harsh orange glow of the flames, deep shadows behind. "
        "Dramatic, mysterious atmosphere, wide shot, empty room, rich textures."
    ),
    "outdoor": (
        "A high-quality semi-realistic digital painting of a {description}, the building "
        "on fire: tall orange flames bursting from the upper windows and the roof, fire "
        "glowing behind the windows, thick black smoke billowing into the sky, burning "
        "embers drifting on the air, the facade and the surrounding trees lit orange by "
        "the blaze, the ground washed in firelight. Dramatic, mysterious atmosphere, "
        "wide shot, rich textures."
    ),
}

NEGATIVE_PROMPT = (
    "people, person, human, figure, crowd, firefighter, fire engine, text, signature, "
    "watermark, blurry, low quality, deformed, cartoon, anime, intact undamaged room, "
    "no fire, blue sky, sunny"
)

# Mirrors toggle_location_lighting.py. Klein is guidance-distilled: cfg_scale stays
# at 1.0 and distilled_cfg_scale is the real guidance dial.
GEN_DEFAULTS = {
    "width": 1920,
    "height": 1088,
    "steps": 20,
    "cfg_scale": 1.0,
    "distilled_cfg_scale": 3.5,
    "sampler_name": "Euler a",
    "scheduler": "Beta",
}

FORCE_INTERIOR = {"broken_flat"}  # interior scenes filed under "Outdoor locations"


def parse_locations():
    """Return {id: {"desc": ..., "type": "interior"|"outdoor"}} from _locations.md."""
    rows = {}
    template = "interior"
    for raw in MD_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("#"):
            low = line.lower()
            if any(k in low for k in ("outdoor", "outside", "exterior")):
                template = "outdoor"
            elif "interior" in low or "attic" in low:
                template = "interior"
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
            rows[rid] = {"desc": desc, "type": template}
    return rows


def split_stem(stem):
    """billiard_room_night -> ("billiard_room", "night"); no suffix -> (stem, "")."""
    for suffix in ("_day", "_night", "_neutral"):
        if stem.endswith(suffix):
            return stem[: -len(suffix)], suffix[1:]
    return stem, ""


def post_json(path, payload, timeout):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        API_URL + path, data=data, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    ap = argparse.ArgumentParser(description="Set a location image on fire (img2img).")
    ap.add_argument("image_path", help="Source image, e.g. .../billiard_room_day.png")
    ap.add_argument("--out", default=None, help="Output folder (default: Images/locations_new/generated/<id>_on_fire).")
    ap.add_argument("--denoise", type=float, nargs="+", default=[0.55], help="One or more denoising strengths (default: 0.55).")
    ap.add_argument("--count", "-n", type=int, default=1, help="Seeds per denoise value.")
    ap.add_argument("--seed", type=int, default=1924, help="First seed (incremented per image).")
    ap.add_argument("--guidance", type=float, default=None, help="Override distilled_cfg_scale.")
    ap.add_argument("--prompt", default=None, help="Replace the fire prompt entirely.")
    ap.add_argument("--timeout", type=int, default=900, help="Per-image request timeout (s).")
    args = ap.parse_args()

    src = pathlib.Path(args.image_path).resolve()
    if not src.exists():
        sys.exit(f"Source image not found: {src}")

    rid, variant = split_stem(src.stem)
    locations = parse_locations()
    if rid in locations:
        desc, loc_type = locations[rid]["desc"], locations[rid]["type"]
    else:
        print(f"Warning: '{rid}' is not in _locations.md — using a generic description.")
        desc, loc_type = rid.replace("_", " "), "interior"
    if rid in FORCE_INTERIOR:
        loc_type = "interior"

    prompt = args.prompt or PROMPT_TEMPLATES[loc_type].format(description=desc)
    out_dir = pathlib.Path(args.out) if args.out else DEFAULT_OUT / f"{rid}_on_fire"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Source : {src.name}  (id: {rid}, {loc_type})")
    print(f"Output : {out_dir}")

    init_b64 = base64.b64encode(src.read_bytes()).decode("utf-8")
    generated = failed = 0
    for denoise in args.denoise:
        for k in range(max(1, args.count)):
            seed = args.seed + k
            # The source variant is part of the name: a day run and a night run of the
            # same room must not overwrite each other.
            prefix = f"{rid}_on_fire_{variant}" if variant else f"{rid}_on_fire"
            stem = f"{prefix}_d{int(denoise * 100)}_s{seed}"
            payload = dict(GEN_DEFAULTS)
            payload.update(
                prompt=prompt,
                negative_prompt=NEGATIVE_PROMPT,
                init_images=[init_b64],
                denoising_strength=denoise,
                seed=seed,
                send_images=True,
                save_images=False,
            )
            if args.guidance is not None:
                payload["distilled_cfg_scale"] = args.guidance

            print(f"gen {stem} ...", end="", flush=True)
            t0 = time.time()
            try:
                res = post_json(IMG2IMG, payload, timeout=args.timeout)
            except urllib.error.URLError as e:
                print(f" FAILED ({e.reason}).")
                print(f"  Is the FLUX.2 Klein server running at {API_URL} ?")
                failed += 1
                break
            except Exception as e:  # noqa: BLE001 - report and move on
                print(f" FAILED ({e}).")
                failed += 1
                continue
            (out_dir / f"{stem}.png").write_bytes(base64.b64decode(res["images"][0]))
            print(f" ok ({time.time() - t0:.0f}s)")
            generated += 1

    print(f"\nDone — {generated} generated, {failed} failed. Output: {out_dir}")


if __name__ == "__main__":
    main()
