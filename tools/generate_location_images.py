"""
Generate Claythorn Manor location backgrounds (interior + outdoor) with the
local FLUX.2 Klein server (Forge Neo, A1111-compatible API at
http://127.0.0.1:7860).

Reads room ids + descriptions from:
    Murder/game/images/locations/_locations.md   (Markdown tables)

The file has an "Interior locations" and an "Outdoor locations" section; rows
under each use the matching prompt template (see PROMPT_TEMPLATES below).

Each description is wrapped in its prompt template and POSTed to
/sdapi/v1/txt2img. The returned PNG is saved as <id>_<variant>.png (the variant
defaults to "night") in the output folder (default:
Images/locations_new/generated/), ready to be reviewed and promoted into
Murder/game/images/locations/ once approved.

Usage (from the repo root):
    python tools/generate_location_images.py                  # all rooms -> a new timestamped subfolder
    python tools/generate_location_images.py library kitchen  # only these ids; keeps existing files and
                                                              #   writes <id>_night_1.png, ... on collision
    python tools/generate_location_images.py library -n 4     # 4 variants of one room, each with a different seed
    python tools/generate_location_images.py --variant day    # write <id>_day.png instead of <id>_night.png
    python tools/generate_location_images.py --force          # overwrite <id>_night.png in place instead of numbering
    python tools/generate_location_images.py --list           # list parsed rooms and exit
    python tools/generate_location_images.py --out some/dir --seed 1234
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
TXT2IMG = "/sdapi/v1/txt2img"

# One template per section in _locations.md. parse_locations() tags each row
# with the key of the section it sits under.
PROMPT_TEMPLATES = {
    "interior": (
        "A high-quality semi-realistic digital painting of a 1920s Scottish manor "
        "{description} at night. Warm amber light, touches of colorful objects. "
        "Deep soft shadows, mysterious atmosphere, wide shot, empty room, rich textures."
    ),
    "outdoor": (
        "A high-quality semi-realistic digital painting of a {description}. "
        "Warm amber light. Deep soft shadows, mysterious atmosphere, wide shot, "
        "rich textures."
    ),
}

NEGATIVE_PROMPT = (
    "people, person, human, figure, crowd, text, signature, watermark, "
    "blurry, low quality, deformed, cartoon, anime"
)

# Mirrors the Forge Neo UI settings. FLUX.2 Klein is guidance-distilled, so
# cfg_scale stays at 1.0 and the real guidance dial is distilled_cfg_scale.
GEN_DEFAULTS = {
    "steps": 8,
    "cfg_scale": 1.0,
    "distilled_cfg_scale": 1.0,
    "sampler_name": "Euler a",
    "scheduler": "Beta",
    "width": 1920,
    "height": 1088,
}


def parse_locations(md_path):
    """Return [(id, description, template), ...] from the Markdown tables.

    Rows under an "Outdoor"/"Outside"/"Exterior" heading use the outdoor
    template; everything else defaults to the interior template.
    """
    rows = []
    template = "interior"
    for raw in md_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("#"):  # markdown heading -> pick the active template
            low = line.lower()
            if any(k in low for k in ("outdoor", "outside", "exterior")):
                template = "outdoor"
            elif "interior" in low:
                template = "interior"
            continue
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        rid, desc = cells[0], cells[1]
        # Skip the header row and the |---|---| separator.
        if rid.lower() == "id" or set(rid) <= set("-: "):
            continue
        rid = rid.strip("`").strip()
        if rid and desc:
            rows.append((rid, desc, template))
    return rows


def post_json(path, payload, timeout):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        API_URL + path, data=data, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def next_available_path(out_dir, stem):
    """Return <stem>.png, or <stem>_1.png, <stem>_2.png, ... if earlier ones exist."""
    out_path = out_dir / f"{stem}.png"
    if not out_path.exists():
        return out_path
    n = 1
    while True:
        candidate = out_dir / f"{stem}_{n}.png"
        if not candidate.exists():
            return candidate
        n += 1


def generate_one(rid, desc, template, out_path, args, seed):
    payload = dict(GEN_DEFAULTS)
    payload.update(
        prompt=PROMPT_TEMPLATES[template].format(description=desc),
        negative_prompt=NEGATIVE_PROMPT,
        seed=seed,
        batch_size=1,
        n_iter=1,
        save_images=False,
        send_images=True,
    )
    if args.width:
        payload["width"] = args.width
    if args.height:
        payload["height"] = args.height
    if args.steps:
        payload["steps"] = args.steps
    if args.distilled_cfg is not None:
        payload["distilled_cfg_scale"] = args.distilled_cfg
    if args.model:
        payload["override_settings"] = {"sd_model_checkpoint": args.model}
        payload["override_settings_restore_after_request"] = False

    result = post_json(TXT2IMG, payload, timeout=args.timeout)
    images = result.get("images") or []
    if not images:
        raise RuntimeError(f"server returned no image (info: {result.get('info')!r})")
    b64 = images[0]
    if "," in b64[:64]:  # strip a possible data: URI prefix
        b64 = b64.split(",", 1)[1]
    out_path.write_bytes(base64.b64decode(b64))
    return out_path


def main():
    ap = argparse.ArgumentParser(
        description="Generate manor location images via the local FLUX.2 Klein server."
    )
    ap.add_argument("ids", nargs="*", help="Only generate these room ids (default: all).")
    ap.add_argument("--md", default=str(MD_FILE), help="Markdown source file.")
    ap.add_argument("--out", default=str(DEFAULT_OUT), help="Output folder.")
    ap.add_argument("--variant", default="night", help="Time-of-day variant appended to filenames: output is <id>_<variant>.png (default: night). Use '' for no suffix.")
    ap.add_argument("--force", action="store_true", help="Overwrite <id>_<variant>.png in place instead of writing a numbered copy (one-by-one mode).")
    ap.add_argument("--list", action="store_true", help="List parsed rooms and exit.")
    ap.add_argument("--seed", type=int, default=-1, help="Seed (-1 = random). With --count, fixed seeds are incremented per image.")
    ap.add_argument("--count", "-n", type=int, default=1, help="How many images to generate per room, each with a different seed.")
    ap.add_argument("--width", type=int, default=None)
    ap.add_argument("--height", type=int, default=None)
    ap.add_argument("--steps", type=int, default=None)
    ap.add_argument("--distilled-cfg", type=float, default=None, dest="distilled_cfg")
    ap.add_argument("--model", default=None, help="Override sd_model_checkpoint for the request.")
    ap.add_argument("--timeout", type=int, default=600, help="Per-image request timeout (s).")
    args = ap.parse_args()

    md_path = pathlib.Path(args.md)
    if not md_path.exists():
        sys.exit(f"Markdown source not found: {md_path}")

    rooms = parse_locations(md_path)
    if args.ids:
        wanted = set(args.ids)
        unknown = wanted - {r for r, _, _ in rooms}
        if unknown:
            sys.exit(f"Unknown room id(s): {', '.join(sorted(unknown))}")
        rooms = [(r, d, t) for r, d, t in rooms if r in wanted]

    if args.list:
        for rid, desc, template in rooms:
            print(f"{rid:22} [{template:8}] {desc}")
        print(f"\n{len(rooms)} room(s).")
        return

    out_dir = pathlib.Path(args.out)
    # Generating all rooms (no explicit ids) drops everything into a fresh
    # timestamped subfolder so each full run is kept separate.
    generating_all = not args.ids
    if generating_all:
        out_dir = out_dir / time.strftime("%Y%m%d_%H%M%S")
    out_dir.mkdir(parents=True, exist_ok=True)

    count = max(1, args.count)
    total = len(rooms)
    generated = failed = 0
    aborted = False
    for i, (rid, desc, template) in enumerate(rooms, 1):
        stem = f"{rid}_{args.variant}" if args.variant else rid
        for k in range(count):
            if (generating_all or args.force) and k == 0:
                # Fresh timestamped folder, or explicit overwrite request.
                out_path = out_dir / f"{stem}.png"
            else:
                # Keep existing files and number new ones.
                out_path = next_available_path(out_dir, stem)
            # Random seed (-1) stays random each time; a fixed seed is bumped
            # per image so the variants actually differ.
            seed = args.seed if args.seed < 0 else args.seed + k
            label = f"{rid} ({k + 1}/{count})" if count > 1 else rid
            print(f"[{i}/{total}] gen    {label} -> {out_path.name} ...", end="", flush=True)
            t0 = time.time()
            try:
                generate_one(rid, desc, template, out_path, args, seed)
            except urllib.error.HTTPError as e:
                print(f" FAILED (HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:200]}).")
                failed += 1
                continue
            except urllib.error.URLError as e:
                print(f" FAILED ({e.reason}).")
                print(f"  Is the FLUX.2 Klein server running at {API_URL} ?")
                failed += 1
                aborted = True
                break  # connection errors will repeat for every image
            except Exception as e:  # noqa: BLE001 - report and move on
                print(f" FAILED ({e}).")
                failed += 1
                continue
            print(f" ok ({time.time() - t0:.0f}s) -> {out_path.name}")
            generated += 1
        if aborted:
            break

    print(f"\nDone — {generated} generated, {failed} failed. Output: {out_dir}")


if __name__ == "__main__":
    main()
