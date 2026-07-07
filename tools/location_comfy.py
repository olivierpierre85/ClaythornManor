"""
Generate Claythorn Manor location backgrounds with the local ComfyUI
Flux 2 Dev server (native API at http://127.0.0.1:8188).

This is the ComfyUI / Flux 2 Dev counterpart of tools/generate_location_images.py
(which drives the Forge Neo Klein server at :7860). It reads the same source file:

    Murder/game/images/locations/_locations.md   (Markdown tables)

Each description is wrapped in a prompt template chosen by its section
(interior / attic / outdoor) and the --variant (night / day), then queued as an
API-format graph on ComfyUI. Flux 2 Dev has no negative prompt in this graph
(single-conditioning BasicGuider), so the anti-cues (no people, no text) are
baked into the positive templates.

Optionally, --ref <image> feeds a reference image through ReferenceLatent so the
new render keeps the composition/style of an existing approved image (e.g. the
Klein-generated final choice) while the prompt re-describes it.

Usage (from the repo root):
    python tools/location_comfy.py entrance_hall                 # 1 night image
    python tools/location_comfy.py entrance_hall -n 3            # 3 seeds
    python tools/location_comfy.py entrance_hall --variant day
    python tools/location_comfy.py entrance_hall --ref Images/locations_new/flux_2_final_choices/entrance_hall_night.png
    python tools/location_comfy.py --list
"""
import argparse
import json
import pathlib
import random
import sys
import time
import urllib.parse

import requests

ROOT = pathlib.Path(__file__).parent.parent.resolve()
MD_FILE = ROOT / "Murder/game/images/locations/_locations.md"
DEFAULT_OUT = ROOT / "Images/locations_new/flux2dev"
SERVER = "http://127.0.0.1:8188"

# ---- Flux 2 Dev model files (as installed on this box) ----------------------
UNET_NAME = "flux2-dev-nvfp4.safetensors"
CLIP_NAME = "mistral_3_small_flux2_fp4_mixed.safetensors"
VAE_NAME = "flux2-vae.safetensors"

# Dev-tuned templates + per-room prop details live in their own module so the
# Klein wording (generate_location_images.py / toggle_location_lighting.py) is
# never touched.
from location_prompts_flux2dev import PROMPT_TEMPLATES, ROOM_DETAILS


def parse_locations(md_path):
    """Return [(id, description, section), ...] from the Markdown tables."""
    rows = []
    section = "interior"
    for raw in md_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("#"):
            low = line.lower()
            if any(k in low for k in ("outdoor", "outside", "exterior")):
                section = "outdoor"
            elif "attic" in low:
                section = "attic"
            elif "interior" in low:
                section = "interior"
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
            rows.append((rid, desc, section))
    return rows


# ---- ComfyUI client ---------------------------------------------------------


def upload_image(path, server):
    """Upload a local image into ComfyUI's input folder; return its server name."""
    with open(path, "rb") as f:
        r = requests.post(
            f"{server}/upload/image",
            files={"image": (pathlib.Path(path).name, f, "image/png")},
            data={"overwrite": "true"},
            timeout=60,
        )
    r.raise_for_status()
    j = r.json()
    name = j["name"]
    return f"{j['subfolder']}/{name}" if j.get("subfolder") else name


def queue_prompt(graph, server):
    r = requests.post(f"{server}/prompt", json={"prompt": graph}, timeout=60)
    if r.status_code != 200:
        raise RuntimeError(f"/prompt HTTP {r.status_code}: {r.text[:500]}")
    j = r.json()
    if j.get("node_errors"):
        raise RuntimeError(f"node_errors: {json.dumps(j['node_errors'])[:500]}")
    return j["prompt_id"]


def wait_for_images(prompt_id, server, timeout):
    """Poll /history until the prompt finishes; return the list of output images."""
    t0 = time.time()
    while time.time() - t0 < timeout:
        r = requests.get(f"{server}/history/{prompt_id}", timeout=30)
        if r.status_code == 200 and r.json():
            entry = r.json()[prompt_id]
            status = entry.get("status", {})
            if status.get("status_str") == "error":
                raise RuntimeError(f"generation error: {json.dumps(status)[:500]}")
            images = []
            for node in entry.get("outputs", {}).values():
                images.extend(node.get("images", []))
            if images:
                return images
        time.sleep(2)
    raise TimeoutError(f"timed out after {timeout}s waiting for {prompt_id}")


def download_image(img, out_path, server):
    params = urllib.parse.urlencode(
        {
            "filename": img["filename"],
            "subfolder": img.get("subfolder", ""),
            "type": img.get("type", "output"),
        }
    )
    r = requests.get(f"{server}/view?{params}", timeout=120)
    r.raise_for_status()
    out_path.write_bytes(r.content)


def next_available_path(out_dir, stem):
    """Return <stem>.png, or <stem>_1.png, _2.png ... if earlier ones exist."""
    candidate = out_dir / f"{stem}.png"
    if not candidate.exists():
        return candidate
    n = 1
    while (out_dir / f"{stem}_{n}.png").exists():
        n += 1
    return out_dir / f"{stem}_{n}.png"


# ---- Graph ------------------------------------------------------------------


def build_graph(prompt, seed, guidance, width, height, steps, prefix, ref_name=None):
    """Flux 2 Dev txt2img graph; with ref_name, the prompt conditions on the
    reference image via ReferenceLatent (composition/style transfer)."""
    graph = {
        "10": {"class_type": "UNETLoader", "inputs": {"unet_name": UNET_NAME, "weight_dtype": "default"}},
        "11": {"class_type": "CLIPLoader", "inputs": {"clip_name": CLIP_NAME, "type": "flux2"}},
        "12": {"class_type": "VAELoader", "inputs": {"vae_name": VAE_NAME}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["11", 0], "text": prompt}},
        "13": {"class_type": "FluxGuidance", "inputs": {"conditioning": ["6", 0], "guidance": guidance}},
        "14": {"class_type": "BasicGuider", "inputs": {"model": ["10", 0], "conditioning": ["13", 0]}},
        "5": {"class_type": "EmptyFlux2LatentImage", "inputs": {"width": width, "height": height, "batch_size": 1}},
        "15": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "euler"}},
        "16": {"class_type": "Flux2Scheduler", "inputs": {"steps": steps, "width": width, "height": height}},
        "17": {"class_type": "RandomNoise", "inputs": {"noise_seed": seed}},
        "18": {
            "class_type": "SamplerCustomAdvanced",
            "inputs": {"noise": ["17", 0], "guider": ["14", 0], "sampler": ["15", 0], "sigmas": ["16", 0], "latent_image": ["5", 0]},
        },
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["18", 0], "vae": ["12", 0]}},
        "9": {"class_type": "SaveImage", "inputs": {"images": ["8", 0], "filename_prefix": prefix}},
    }
    if ref_name:
        graph["20"] = {"class_type": "LoadImage", "inputs": {"image": ref_name}}
        graph["21"] = {"class_type": "FluxKontextImageScale", "inputs": {"image": ["20", 0]}}
        graph["22"] = {"class_type": "VAEEncode", "inputs": {"pixels": ["21", 0], "vae": ["12", 0]}}
        graph["23"] = {"class_type": "ReferenceLatent", "inputs": {"conditioning": ["6", 0], "latent": ["22", 0]}}
        graph["13"]["inputs"]["conditioning"] = ["23", 0]
    return graph


# ---- Main -------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(
        description="Generate manor location images via the local ComfyUI Flux 2 Dev server."
    )
    ap.add_argument("ids", nargs="*", help="Only generate these room ids (default: all).")
    ap.add_argument("--md", default=str(MD_FILE), help="Markdown source file.")
    ap.add_argument("--out", default=str(DEFAULT_OUT), help="Output folder.")
    ap.add_argument("--variant", default="night", choices=["night", "day"],
                    help="Lighting variant; output is <id>_<variant>.png (default: night).")
    ap.add_argument("--list", action="store_true", help="List parsed rooms and exit.")
    ap.add_argument("--seed", type=int, default=-1, help="-1 = random per image; a fixed value increments per --count.")
    ap.add_argument("--count", "-n", type=int, default=1, help="How many images per room, each with a different seed.")
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--height", type=int, default=1088)
    ap.add_argument("--steps", type=int, default=24)
    ap.add_argument("--guidance", type=float, default=3.5, help="FluxGuidance value.")
    ap.add_argument("--ref", default=None, help="Reference image fed through ReferenceLatent (composition/style match).")
    ap.add_argument("--prompt", default=None, help="Override the ENTIRE prompt for this run.")
    ap.add_argument("--server", default=SERVER)
    ap.add_argument("--timeout", type=int, default=900, help="Per-image wait timeout (s).")
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
        rooms = [(r, d, s) for r, d, s in rooms if r in wanted]

    if args.list:
        for rid, desc, section in rooms:
            print(f"{rid:22} [{section:8}] {desc}")
        print(f"\n{len(rooms)} room(s).")
        return

    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    ref_name = None
    if args.ref:
        ref_path = pathlib.Path(args.ref)
        if not ref_path.is_absolute():
            ref_path = ROOT / ref_path
        if not ref_path.exists():
            sys.exit(f"Reference image not found: {ref_path}")
        ref_name = upload_image(ref_path, args.server)
        print(f"reference = {ref_path.name}")

    count = max(1, args.count)
    total = len(rooms)
    generated = failed = 0
    for i, (rid, desc, section) in enumerate(rooms, 1):
        if rid in ROOM_DETAILS:
            desc = f"{desc}, {ROOM_DETAILS[rid]}"
        prompt = args.prompt or PROMPT_TEMPLATES[(section, args.variant)].format(description=desc)
        stem = f"{rid}_{args.variant}"
        for k in range(count):
            seed = random.randint(0, 2**31 - 1) if args.seed < 0 else args.seed + k
            out_path = next_available_path(out_dir, stem)
            label = f"{rid} ({k + 1}/{count})" if count > 1 else rid
            print(f"[{i}/{total}] gen    {label} seed={seed} -> {out_path.name} ...", end="", flush=True)
            t0 = time.time()
            try:
                graph = build_graph(prompt, seed, args.guidance, args.width, args.height,
                                    args.steps, f"loc_{stem}", ref_name=ref_name)
                prompt_id = queue_prompt(graph, args.server)
                images = wait_for_images(prompt_id, args.server, args.timeout)
                download_image(images[0], out_path, args.server)
            except requests.exceptions.ConnectionError:
                print(" FAILED.")
                sys.exit(f"  Is ComfyUI running at {args.server} ?")
            except Exception as e:  # noqa: BLE001 - report and move on
                print(f" FAILED ({e}).")
                failed += 1
                continue
            print(f" ok ({time.time() - t0:.0f}s)")
            generated += 1

    print(f"\nDone -- {generated} generated, {failed} failed. Output: {out_dir}")


if __name__ == "__main__":
    main()
