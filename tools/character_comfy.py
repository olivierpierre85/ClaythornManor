"""
Character art harness for the local ComfyUI Flux 2 Dev server
(native API at http://127.0.0.1:8188).

This is the ComfyUI / Flux 2 Dev counterpart of tools/character_flux.py (which
drives the Forge Neo Klein server). It follows the proven pipeline recorded in the
`comfyui-flux2-character` memory. There are TWO stages:

    base <char>   Head-shot  ->  a darker, subtly-stylised 3/4-body FRONTAL figure.
                  The likeness comes from the head-shot (fed through ReferenceLatent);
                  the outfit and everything else come from the character description.

    turn <char>   Take the APPROVED frontal base and turn the figure a little into a
                  moderate three-quarter view. The reference is now the front image,
                  which already carries the outfit, so the uniform/clothes stay
                  identical across the turn -- only the pose changes.

WORKFLOW
--------
1.  python tools/character_comfy.py base captain            # a few frontal candidates
2.  pick the best one and copy it to the approved front slot:
        Images/characters_new/captain/base/captain_flux2dev_front.png
3.  python tools/character_comfy.py turn captain            # 3/4 turns of that front

Each character has an entry in CHARACTERS (head-shot path + description). Only the
captain's description is written; add the others (see the TODO stubs) as you go.
Outputs are numbered (never overwritten) under Images/characters_new/<char>/base/.

EXAMPLES
--------
  python tools/character_comfy.py base captain --count 3
  python tools/character_comfy.py base captain --seed 1924 --count 1
  python tools/character_comfy.py turn captain --count 3
  python tools/character_comfy.py turn captain --direction right --count 2
"""
import argparse
import json
import random
import sys
import time
import urllib.parse
from pathlib import Path

import requests

ROOT = Path(__file__).parent.parent.resolve()
OUT_ROOT = ROOT / "Images" / "characters_new"
SERVER = "http://127.0.0.1:8188"

# ---- Flux 2 Dev model files (as installed on this box) ----------------------
UNET_NAME = "flux2-dev-nvfp4.safetensors"
CLIP_NAME = "mistral_3_small_flux2_fp4_mixed.safetensors"
VAE_NAME = "flux2-vae.safetensors"

# ---- Per-character registry -------------------------------------------------
# head_shot: source portrait for the `base` stage (relative to repo root).
# description: the full subject sentence injected into the prompts -- spell out
#   face AND clothing/uniform, or the likeness and outfit will drift. Set to None
#   until written; the tool refuses to run a character whose description is None.


class Character:
    def __init__(self, head_shot, description):
        self.head_shot = head_shot
        self.description = description


CHARACTERS = {
    # --- written ---
    "captain": Character(
        head_shot="Images/Archive/16_05_ARCHIVE/characters/artflowcharacters/captain.png",
        description=(
            "a gaunt older Indian Army officer of South Asian descent, around sixty, "
            "short silver-grey hair receding at the temples, dark tanned brown skin, "
            "deep-set tired eyes, hollow cheeks, prominent cheekbones, lined weathered "
            "face, clean-shaven, thin stern mouth, wearing a dark olive-drab and deep "
            "brown 1920s military dress uniform in muted low-key tones with a brown "
            "leather Sam Browne belt and diagonal shoulder strap"
        ),
    ),
    "lad": Character(
        head_shot="Images/characters_original_and_archive/side/side lad.png",
        description=(
            "a young man of about twenty-two, fair skin with a faint ruddy flush, tousled "
            "light blond hair swept across the forehead, clear green eyes, clean-shaven with "
            "soft youthful features and a full mouth, a wary watchful expression, wearing a "
            "light brown 1920s three-piece lounge suit with a waistcoat and a loosened "
            "collar, the suit clean but a little cheap and ill-fitting, only subtly worn with "
            "no visible dirt or stains, the clothes of a working man trying to pass in gentry "
            "company"
        ),
    ),
    "psychic": Character(
        head_shot="Images/characters_original_and_archive/side/side psychic.png",
        description=(
            "a gaunt woman in her early sixties, a deeply lined careworn face with hollow "
            "cheeks, pale skin and calm pale hazel eyes with an ordinary, steady gaze, thin "
            "lips touched with dark red, greying hair wrapped in a soft draped grey headscarf "
            "or cloche, small drop earrings, wearing a layered dark 1920s dress with a fringed "
            "shawl and long strings of beads, the theatrical look of a spiritualist medium"
        ),
    ),
    "doctor": Character(
        head_shot="Images/characters_original_and_archive/side/side doctor.png",
        description=(
            "a gaunt middle-aged man of about fifty, greying dark hair combed back from a "
            "high forehead, round wire-rimmed spectacles, sunken tired eyes with dark shadows "
            "beneath, pale sallow skin and hollow lined cheeks, clean-shaven, a weary faintly "
            "furtive expression, wearing a respectable bottle-green 1920s three-piece tweed "
            "suit with a waistcoat and a warm brown tie, tidy and well-kept, the proper "
            "middle-class look of a charity-hospital doctor with a quiet morphine habit"
        ),
    ),
    "nurse": Character(
        head_shot="Images/characters_original_and_archive/side/side nurse.png",
        description=(
            "a plain woman in her early fifties, dark brown hair lightly greying, parted in "
            "the centre and drawn loosely back, pale lined skin, cool blue-grey eyes, an "
            "unadorned ageing face with a reserved, faintly severe and disapproving "
            "expression, wearing a plain high-collared dark 1920s dress with a pale collar and "
            "a small brooch, austere, spinsterish and respectable"
        ),
    ),
    "drunk": Character(
        head_shot="Images/characters_original_and_archive/side/side drunk.png",
        description=(
            "a grizzled older man of about sixty, unkempt greying hair and a grey stubbled "
            "beard, ruddy weathered and deeply lined skin, bleary bloodshot eyes and a loose "
            "wry half-smile, wearing a rumpled grey 1920s three-piece suit with a crooked "
            "loosened tie and an unbuttoned waistcoat, the suit clean but well-worn and "
            "creased, only subtly shabby with no visible dirt or stains, a once-respectable "
            "barrister gone to drink"
        ),
    ),
    "broken": Character(
        # Masked -- his in-game identity (the side portrait is masked too). For the
        # disfigured face instead, point at the maskless portrait and describe the scarring.
        head_shot="Images/characters_original_and_archive/side/side broken.png",
        description=(
            "a lean man of about forty wearing a carved painted wooden half-mask (a mask of "
            "pale carved wood in muted browns, with a visible wood grain) that covers the "
            "disfigured nose and upper face, weary watchful eyes visible through it, a soft "
            "flat cloth cap over short hair, wearing a plain working-class 1920s outfit of "
            "collarless pale shirt, waistcoat and jacket in muted tones, a disfigured war "
            "veteran hiding behind the mask"
        ),
    ),
    "host": Character(
        head_shot="Images/characters_original_and_archive/side/side host.png",
        description=(
            "an elegant woman of about forty-five, softly waved silver-grey hair set in a "
            "1920s finger-wave bob, arched brows, striking green eyes, pale powdered skin and "
            "dark red lips, a poised composed and faintly theatrical expression, wearing a "
            "refined pale 1920s gown with a beaded lace collar and ropes of pearls, an "
            "out-of-work actress playing the part of a grand lady"
        ),
    ),
}

# ---- Prompt templates -------------------------------------------------------
# Shared house style. Character specifics live in {desc}; keep this generic.
STYLE = (
    "a refined semi-realistic digital illustration with a gentle, very subtle touch "
    "of cartoon stylisation, muted low-key colour palette"
)

# Stage 1: head-shot -> frontal 3/4-body figure.
BASE_PROMPT = (
    "{style}, of {desc}. Depict them as a full standing portrait cropped at the "
    "thighs, facing directly forward toward the viewer, body squared to the camera, "
    "shoulders straight and level, the head small within the frame with the full "
    "torso and waist visible, natural head-to-body proportions, hands resting at "
    "their sides. Soft naturalistic brushwork with slightly cleaner, gently stylised "
    "shading, realistic facial structure and lifelike proportions, matte illustration, "
    "soft even studio lighting, plain neutral warm-grey background."
)

# Stage 2: turn the approved front a little. No "still facing viewer / not a profile"
# hedges -- those collapse it back to frontal (see memory). Plain moderate-turn wording.
TURN_PROMPT = (
    "Show the exact same character from the reference image, {desc}. Keep the outfit, "
    "face, hair and colours identical to the reference, only change the pose: they "
    "stand in a relaxed three-quarter view, their body rotated about twenty degrees "
    "to their {direction} so the {shoulder} shoulder comes gently forward and the "
    "other side turns slightly away. A natural standing three-quarter pose. Full "
    "standing portrait cropped at the thighs, hands resting at their sides, {style}, "
    "matte illustration, soft even studio lighting, plain neutral warm-grey background."
)

# ---- ComfyUI client ---------------------------------------------------------


def upload_image(path, server):
    """Upload a local image into ComfyUI's input folder; return its server name."""
    with open(path, "rb") as f:
        r = requests.post(
            f"{server}/upload/image",
            files={"image": (Path(path).name, f, "image/png")},
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


def build_graph(ref_name, prompt, seed, guidance, width, height, steps, prefix):
    """The Flux 2 Dev reference/pose graph (single reference image via ReferenceLatent)."""
    return {
        "10": {"class_type": "UNETLoader", "inputs": {"unet_name": UNET_NAME, "weight_dtype": "default"}},
        "11": {"class_type": "CLIPLoader", "inputs": {"clip_name": CLIP_NAME, "type": "flux2"}},
        "12": {"class_type": "VAELoader", "inputs": {"vae_name": VAE_NAME}},
        "20": {"class_type": "LoadImage", "inputs": {"image": ref_name}},
        "21": {"class_type": "FluxKontextImageScale", "inputs": {"image": ["20", 0]}},
        "22": {"class_type": "VAEEncode", "inputs": {"pixels": ["21", 0], "vae": ["12", 0]}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["11", 0], "text": prompt}},
        "23": {"class_type": "ReferenceLatent", "inputs": {"conditioning": ["6", 0], "latent": ["22", 0]}},
        "13": {"class_type": "FluxGuidance", "inputs": {"conditioning": ["23", 0], "guidance": guidance}},
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


def run_batch(args, ref_path, prompt, guidance, stem):
    """Upload the reference, then generate args.count images (incrementing/rolling seeds)."""
    out_dir = OUT_ROOT / args.char / "base"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"       reference = {Path(ref_path).name}  guidance = {guidance}  size = {args.width}x{args.height}")
    ref_name = upload_image(ref_path, args.server)

    made = []
    for k in range(max(1, args.count)):
        seed = random.randint(0, 2**31 - 1) if args.seed < 0 else args.seed + k
        graph = build_graph(ref_name, prompt, seed, guidance, args.width, args.height, args.steps, stem)
        out_path = next_available_path(out_dir, stem)
        label = f"{k + 1}/{args.count}" if args.count > 1 else "1/1"
        print(f"  gen {label} seed={seed} -> {out_path.name} ...", end="", flush=True)
        t0 = time.time()
        try:
            prompt_id = queue_prompt(graph, args.server)
            images = wait_for_images(prompt_id, args.server, args.timeout)
        except requests.exceptions.ConnectionError:
            print(" FAILED.")
            sys.exit(f"  Is ComfyUI running at {args.server} ?")
        download_image(images[0], out_path, args.server)
        print(f" ok ({time.time() - t0:.0f}s)")
        made.append(out_path)
    return made, out_dir


# ---- Stages -----------------------------------------------------------------


def resolve_character(args):
    if args.char not in CHARACTERS:
        sys.exit(f"Unknown character '{args.char}'. Known: {', '.join(CHARACTERS)}")
    ch = CHARACTERS[args.char]
    desc = args.desc or ch.description
    if not desc:
        sys.exit(
            f"No description for '{args.char}' yet. Write it in CHARACTERS "
            f"(tools/character_comfy.py) or pass --desc \"...\"."
        )
    return ch, desc


def mode_base(args):
    ch, desc = resolve_character(args)
    head = Path(args.head_shot) if args.head_shot else (ROOT / ch.head_shot) if ch.head_shot else None
    if not head or not head.exists():
        sys.exit(f"Head-shot not found for '{args.char}'. Set it in CHARACTERS or pass --head-shot.")

    prompt = args.prompt or BASE_PROMPT.format(style=STYLE, desc=desc)
    guidance = args.guidance if args.guidance is not None else 3.5
    print(f"[base] char={args.char}  (head-shot -> frontal 3/4 figure)")
    made, out_dir = run_batch(args, str(head), prompt, guidance, f"{args.char}_flux2dev_base")
    print(f"[base] {len(made)} image(s) -> {out_dir}")
    print(f"       promote your pick to: {out_dir / (args.char + '_flux2dev_front.png')}")


def mode_turn(args):
    ch, desc = resolve_character(args)
    front = Path(args.front) if args.front else OUT_ROOT / args.char / "base" / f"{args.char}_flux2dev_front.png"
    if not front.exists():
        sys.exit(
            f"Approved front not found: {front}\n"
            f"Run `base {args.char}` first, then copy your chosen candidate to that path."
        )

    direction = args.direction
    shoulder = "right" if direction == "left" else "left"
    prompt = args.prompt or TURN_PROMPT.format(style=STYLE, desc=desc, direction=direction, shoulder=shoulder)
    guidance = args.guidance if args.guidance is not None else 3.0
    print(f"[turn] char={args.char}  (front -> moderate 3/4 turn to their {direction})")
    made, out_dir = run_batch(args, str(front), prompt, guidance, f"{args.char}_flux2dev_turn")
    print(f"[turn] {len(made)} image(s) -> {out_dir}")


# ---- CLI --------------------------------------------------------------------


def add_common(p):
    p.add_argument("char", help="Character id (e.g. captain). See CHARACTERS.")
    p.add_argument("--count", "-n", type=int, default=3, help="How many images (each a different seed).")
    p.add_argument("--seed", type=int, default=-1, help="-1 = random per image; a fixed value increments per --count.")
    p.add_argument("--guidance", type=float, default=None, help="FluxGuidance (default: base 3.5, turn 3.0).")
    p.add_argument("--steps", type=int, default=24)
    p.add_argument("--width", type=int, default=832)
    p.add_argument("--height", type=int, default=1216)
    p.add_argument("--desc", default=None, help="Override the character description for this run.")
    p.add_argument("--prompt", default=None, help="Override the ENTIRE prompt for this run.")
    p.add_argument("--server", default=SERVER)
    p.add_argument("--timeout", type=int, default=600)


def main():
    ap = argparse.ArgumentParser(description="ComfyUI Flux 2 Dev character art harness.")
    sub = ap.add_subparsers(dest="mode", required=True)

    pb = sub.add_parser("base", help="Head-shot -> frontal 3/4-body figure.")
    add_common(pb)
    pb.add_argument("--head-shot", default=None, dest="head_shot", help="Override the source head-shot path.")
    pb.set_defaults(func=mode_base)

    pt = sub.add_parser("turn", help="Turn the approved front into a moderate 3/4 view.")
    add_common(pt)
    pt.add_argument("--front", default=None, help="Override the approved front reference path.")
    pt.add_argument("--direction", choices=["left", "right"], default="left", help="Which way the figure turns.")
    pt.set_defaults(func=mode_turn)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
