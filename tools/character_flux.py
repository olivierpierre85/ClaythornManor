"""
Character art experimentation harness for the local FLUX.2 Klein server
(Forge Neo, A1111-compatible API at http://127.0.0.1:7860).

This is a *tinkering* tool. It exposes the FLUX dials as CLI args and always
writes numbered outputs into a staging tree so no iteration is ever overwritten:

    Images/characters_new/<char>/
        base/         mode=base   -> <char>_base[_N].png
        expressions/  mode=expr   -> <char>_<expr>[_N].png
        scenes/       mode=scene  -> <char>_<room>[_N].png

It reuses the proven payload shape from _flux_oneoff.py: img2img +
multi-reference via the "ImageStitch Integrated" alwayson script, with
cfg_scale=1.0 and distilled_cfg_scale as the real guidance dial (Klein is
guidance-distilled).

--------------------------------------------------------------------------
THREE MODES
--------------------------------------------------------------------------
base   Turn a head-and-shoulders portrait into a 3/4-length body in a new
       style. The body is invented and the canvas is taller than the square
       source, so the source can't be a same-size init. Methods:
         --method ref    (default) neutral grey init at the target size, high
                         denoise (~0.95), source carried as an ImageStitch
                         reference -> a fresh tall figure anchored to the face.
         --method pad    paste the head near the top of a tall canvas, fill
                         below with the source's background tone, moderate
                         denoise (~0.8) + ImageStitch ref. More controllable
                         framing.
         --method txt2img  pure txt2img + ImageStitch (experimental; only if
                         this Forge build honours the alwayson script on
                         txt2img).

expr   Derive an expression variant from an APPROVED base. img2img on the base
       at low denoise (~0.4) so pose / uniform / style are preserved, base
       carried as an ImageStitch ref, prompt changes only the face.

scene  AI-bake the character into a location. img2img with init = the location
       image and the approved base carried as an ImageStitch reference.

--------------------------------------------------------------------------
EXAMPLES
--------------------------------------------------------------------------
  # 4 base variants, default captain prompt, default ref method
  python tools/character_flux.py base --count 4

  # tinker: stronger guidance, more change, fixed seed
  python tools/character_flux.py base --distilled-cfg 3.5 --denoise 0.97 --seed 1924

  # padded-canvas method instead
  python tools/character_flux.py base --method pad --denoise 0.8

  # an angry expression from an approved base
  python tools/character_flux.py expr angry --base Images/characters_new/captain/base/captain_base_2.png

  # bake the base into the captain's bedroom
  python tools/character_flux.py scene \
      --base Images/characters_new/captain/base/captain_base_2.png \
      --location "Murder/game/images/locations/version2/bedroom_captain_version2.webp"
"""
import argparse
import base64
import io
import pathlib
import sys
import time

import requests
from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).parent.parent.resolve()
API_URL = "http://127.0.0.1:7860"
TXT2IMG = "/sdapi/v1/txt2img"
IMG2IMG = "/sdapi/v1/img2img"

DEFAULT_SOURCE = ROOT / "Images/Archive/16_05_ARCHIVE/characters/artflowcharacters/captain.png"
OUT_ROOT = ROOT / "Images/characters_new"

# ---- Default prompts (override with --prompt / --prompt-file) ---------------

# {char_desc} lets the same template serve other characters later. Spell out the
# face so the restyle keeps the original likeness instead of inventing a generic one.
CAPTAIN_DESC = (
    "a gaunt older Indian Army officer of South Asian descent, around sixty, "
    "short silver-grey hair receding at the temples, dark tanned brown skin, "
    "deep-set tired eyes, hollow cheeks, prominent cheekbones, lined weathered face, "
    "clean-shaven, thin stern mouth, smooth unscarred skin, "
    "wearing a 1920s khaki military dress uniform"
)

# Head-only restyle (pad pre-pass): turns the photographic source head into the
# same painterly medium as the generated body, so the two merge seamlessly.
HEAD_PROMPT = (
    "A refined semi-realistic digital painting of the head and shoulders of "
    "{char_desc}, calm stern expression, subtle painterly stylisation, soft "
    "naturalistic brushwork, realistic facial structure, gentle soft shading, "
    "matte illustration, plain neutral background."
)

# Subtle painterly look (NOT clean cartoon). The anti-cartoon markers live in the
# negative; keep this positive about soft realism.
BASE_PROMPT = (
    "A refined semi-realistic digital painting of {char_desc}, calm stern expression, "
    "standing portrait cropped at the thighs, facing directly forward toward the viewer, "
    "body squared to the camera, shoulders straight and level, symmetrical frontal pose, "
    "the head small within the frame with the full torso and waist clearly visible, "
    "natural head-to-body proportions, wearing a brown leather Sam Browne belt at the "
    "waist, hands resting at his sides, soft naturalistic brushwork, subtle painterly "
    "stylisation, realistic facial structure and lifelike proportions, gentle soft "
    "shading, matte illustration, soft even studio lighting, plain neutral background."
)

EXPR_PROMPT = (
    "A semi-cartoon illustration of the same character, {expr} expression, "
    "identical pose, identical 1920s military dress uniform, identical art style, "
    "three-quarter length standing portrait, plain neutral background."
)

# Scene baking only places the figure if the prompt explicitly demands a
# foreground full figure AND denoise is high enough (~0.8+) to re-paint space
# for it. At low denoise the room init fills the frame and the figure is skipped.
SCENE_PROMPT = (
    "A semi-cartoon illustration of the same officer character standing "
    "prominently in the foreground of {room_desc}, full figure clearly visible, "
    "same face and uniform as the character reference, integrated naturally into "
    "the scene with consistent lighting and perspective."
)

BASE_NEGATIVE = (
    "scar, facial scar, double head, two heads, extra head, two faces, ghost head, "
    "turned body, twisted torso, body at an angle, three-quarter view, side view, "
    "profile, looking away, head turned, contrapposto, "
    "cartoon, anime, comic book, cel shaded, flat colors, thick black outlines, "
    "bold linework, caricature, exaggerated features, photograph, photo, ornate frame, "
    "picture frame, border, text, watermark, signature, deformed hands, mangled hands, "
    "extra fingers, extra limbs, missing limbs, blurry, low quality, cropped head."
)


# ---- Server / IO helpers (mirror the existing FLUX tools) -------------------

def b64_file(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def encode_pil(img):
    buf = io.BytesIO()
    img.convert("RGB").save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()


def _mask_b64(mask):
    buf = io.BytesIO()
    mask.convert("L").save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()


def snap16(n):
    """FLUX needs each side divisible by 16 (latent patchify); round to nearest."""
    return max(16, int(round(n / 16)) * 16)


def post_json(path, payload, timeout):
    r = requests.post(API_URL + path, json=payload, timeout=timeout)
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:600]}")
    return r.json()


def next_available_path(out_dir, stem):
    """Return <stem>.png, or <stem>_1.png, _2.png ... if earlier ones exist."""
    out_path = out_dir / f"{stem}.png"
    if not out_path.exists():
        return out_path
    n = 1
    while True:
        candidate = out_dir / f"{stem}_{n}.png"
        if not candidate.exists():
            return candidate
        n += 1


def decode_to_file(b64, out_path):
    if "," in b64[:64]:  # strip a possible data: URI prefix
        b64 = b64.split(",", 1)[1]
    out_path.write_bytes(base64.b64decode(b64))


def stitch_script(refs_b64, max_side):
    """The multi-reference alwayson script: [enabled, refs_list, max_side]."""
    return {"ImageStitch Integrated": {"args": [True, refs_b64, max_side]}}


def read_text_arg(value, file_path):
    """--prompt wins; else --prompt-file contents; else None."""
    if value:
        return value
    if file_path:
        return pathlib.Path(file_path).read_text(encoding="utf-8").strip()
    return None


# ---- Payload assembly -------------------------------------------------------

def base_payload(args, init_b64, refs_b64, prompt, negative, seed, endpoint, mask_b64=None):
    payload = {
        "prompt": prompt,
        "negative_prompt": negative,
        "width": args.width,
        "height": args.height,
        "steps": args.steps,
        "cfg_scale": 1.0,
        "distilled_cfg_scale": args.distilled_cfg,
        "sampler_name": args.sampler,
        "scheduler": args.scheduler,
        "seed": seed,
        "send_images": True,
        "save_images": False,
    }
    if endpoint == IMG2IMG:
        payload["init_images"] = [init_b64]
        payload["denoising_strength"] = args.denoise
    if mask_b64:
        # White region is regenerated (the body); the black-masked face is composited
        # back, so the real likeness survives even at high denoise.
        payload["mask"] = mask_b64
        payload["inpainting_fill"] = 2          # latent noise -> generate fresh body
        payload["inpaint_full_res"] = False     # whole-canvas context so body fits figure
        payload["inpainting_mask_invert"] = 0   # white = inpaint
        payload["mask_blur"] = args.mask_blur
    if refs_b64:
        payload["alwayson_scripts"] = stitch_script(refs_b64, args.max_side)
    if args.model:
        payload["override_settings"] = {"sd_model_checkpoint": args.model}
        payload["override_settings_restore_after_request"] = True
    return payload


def run_batch(args, out_dir, stem, init_b64, refs_b64, prompt, negative, endpoint, mask_b64=None):
    """Generate args.count images, each with an incremented seed, numbered output."""
    out_dir.mkdir(parents=True, exist_ok=True)
    base_seed = args.seed
    made = []
    for k in range(max(1, args.count)):
        seed = base_seed if base_seed < 0 else base_seed + k
        payload = base_payload(args, init_b64, refs_b64, prompt, negative, seed, endpoint, mask_b64)
        out_path = next_available_path(out_dir, stem)
        label = f"{stem} ({k + 1}/{args.count})" if args.count > 1 else stem
        print(f"  gen {label} seed={seed} -> {out_path.name} ...", end="", flush=True)
        t0 = time.time()
        try:
            res = post_json(endpoint, payload, args.timeout)
        except requests.exceptions.ConnectionError:
            print(" FAILED.")
            print(f"  Is the FLUX.2 Klein server running at {API_URL} ?")
            sys.exit(1)
        images = res.get("images") or []
        if not images:
            print(f" FAILED (no image; info={res.get('info')!r}).")
            continue
        decode_to_file(images[0], out_path)
        print(f" ok ({time.time() - t0:.0f}s)")
        made.append(out_path)
    return made


# ---- Modes ------------------------------------------------------------------

def restyle_head(args, source_path, negative):
    """Pre-pass: repaint the photographic source head into the painterly medium so
    it merges with the generated body. Returns a PIL image. denoise = args.restyle_head."""
    src = Image.open(source_path).convert("RGB").resize((768, 768))
    # Fix the head seed independently of the body seed so a chosen head can be
    # reused while only the body/pose varies across --count variants.
    rseed = args.restyle_seed if getattr(args, "restyle_seed", None) is not None else args.seed
    payload = {
        "prompt": HEAD_PROMPT.format(char_desc=args.char_desc),
        "negative_prompt": negative,
        "init_images": [encode_pil(src)],
        "denoising_strength": args.restyle_head,
        "width": 768, "height": 768, "steps": args.steps,
        "cfg_scale": 1.0, "distilled_cfg_scale": args.distilled_cfg,
        "sampler_name": args.sampler, "scheduler": args.scheduler,
        "seed": rseed, "send_images": True, "save_images": False,
        "alwayson_scripts": stitch_script([b64_file(source_path)], args.max_side),
    }
    print(f"       restyling head (denoise={args.restyle_head}) ...", end="", flush=True)
    res = post_json(IMG2IMG, payload, args.timeout)
    b64 = res["images"][0]
    if "," in b64[:64]:
        b64 = b64.split(",", 1)[1]
    print(" ok")
    return Image.open(io.BytesIO(base64.b64decode(b64))).convert("RGB")


def build_init_for_base(args, source_path, negative):
    """Return (init_b64, endpoint, mask_b64) for the chosen base method.

    mask_b64 is None except for `pad`, which masks the body region so it is
    regenerated while the pasted head (face) is preserved.
    """
    if args.method == "txt2img":
        return None, TXT2IMG, None
    if args.method == "pad":
        # Optionally restyle the head into the painterly medium first (so it merges
        # with the painted body), then paste it; everything below the jaw is masked
        # white and inpainted into a body under the kept face.
        if args.restyle_head and args.restyle_head > 0:
            src = restyle_head(args, source_path, negative)
        else:
            src = Image.open(source_path).convert("RGB")
        bg = src.getpixel((2, 2))
        canvas = Image.new("RGB", (args.width, args.height), bg)
        head_w = int(args.width * args.head_scale)
        head_h = int(head_w * src.height / src.width)
        head = src.resize((head_w, head_h))
        top = int(args.height * args.head_y)
        cx = args.width // 2
        canvas.paste(head, (cx - head_w // 2, top))
        # Keep ONLY an ellipse around the face/hair (black); regenerate everything
        # else (white) so the background is repainted uniformly and a body grows in
        # under the chin -- avoids the seam left by the source head's own backdrop.
        mask = Image.new("L", (args.width, args.height), 255)
        ell_w = head_w * args.keep_w
        ell_top = top + head_h * 0.04
        ell_bottom = top + head_h * args.keep_ratio
        ImageDraw.Draw(mask).ellipse(
            [cx - ell_w / 2, ell_top, cx + ell_w / 2, ell_bottom], fill=0)
        return encode_pil(canvas), IMG2IMG, _mask_b64(mask)
    # method == "ref": neutral grey init, high denoise -> fresh figure, face from ref.
    grey = Image.new("RGB", (args.width, args.height), (128, 128, 128))
    return encode_pil(grey), IMG2IMG, None


def mode_base(args):
    source_path = pathlib.Path(args.source) if args.source else DEFAULT_SOURCE
    if not source_path.exists():
        sys.exit(f"Source not found: {source_path}")

    refs = [b64_file(source_path)]
    for extra in args.refs or []:
        refs.append(b64_file(extra))

    prompt = read_text_arg(args.prompt, args.prompt_file) or \
        BASE_PROMPT.format(char_desc=args.char_desc)
    negative = read_text_arg(args.neg, args.neg_file) or BASE_NEGATIVE

    init_b64, endpoint, mask_b64 = build_init_for_base(args, source_path, negative)
    out_dir = OUT_ROOT / args.char / "base"
    print(f"[base] char={args.char} method={args.method} endpoint={endpoint} "
          f"denoise={args.denoise} dcfg={args.distilled_cfg} size={args.width}x{args.height}"
          f"{' inpaint-body' if mask_b64 else ''}")
    print(f"       source={source_path.name} refs={len(refs)}")
    made = run_batch(args, out_dir, f"{args.char}_base", init_b64, refs, prompt, negative,
                     endpoint, mask_b64)
    print(f"[base] {len(made)} image(s) -> {out_dir}")


def mode_expr(args):
    base_path = pathlib.Path(args.base)
    if not base_path.exists():
        sys.exit(f"Base image not found: {base_path}")
    base_b64 = b64_file(base_path)

    prompt = read_text_arg(args.prompt, args.prompt_file) or \
        EXPR_PROMPT.format(expr=args.expr)
    negative = read_text_arg(args.neg, args.neg_file) or BASE_NEGATIVE

    out_dir = OUT_ROOT / args.char / "expressions"
    print(f"[expr] char={args.char} expr={args.expr} denoise={args.denoise} "
          f"base={base_path.name}")
    made = run_batch(args, out_dir, f"{args.char}_{args.expr}", base_b64, [base_b64],
                     prompt, negative, IMG2IMG)
    print(f"[expr] {len(made)} image(s) -> {out_dir}")


def mode_scene(args):
    base_path = pathlib.Path(args.base)
    location_path = pathlib.Path(args.location)
    for p in (base_path, location_path):
        if not p.exists():
            sys.exit(f"Not found: {p}")

    base_b64 = b64_file(base_path)
    loc_img = Image.open(location_path).convert("RGB")
    # Match the canvas to the location, snapped to /16 for FLUX's latent patchify.
    args.width, args.height = snap16(loc_img.width), snap16(loc_img.height)
    if (args.width, args.height) != loc_img.size:
        loc_img = loc_img.resize((args.width, args.height))
    init_b64 = encode_pil(loc_img)

    room_desc = args.room_desc or location_path.stem.replace("_version2", "").replace("_", " ")
    prompt = read_text_arg(args.prompt, args.prompt_file) or \
        SCENE_PROMPT.format(room_desc=room_desc)
    negative = read_text_arg(args.neg, args.neg_file) or \
        "text, watermark, signature, deformed hands, extra limbs, blurry, low quality"

    out_dir = OUT_ROOT / args.char / "scenes"
    stem = f"{args.char}_{location_path.stem.replace('_version2', '')}"
    print(f"[scene] char={args.char} room='{room_desc}' denoise={args.denoise} "
          f"size={args.width}x{args.height}")
    print(f"        base={base_path.name} location={location_path.name}")
    made = run_batch(args, out_dir, stem, init_b64, [base_b64], prompt, negative, IMG2IMG)
    print(f"[scene] {len(made)} image(s) -> {out_dir}")


# ---- CLI --------------------------------------------------------------------

def add_common(p, denoise_default):
    p.add_argument("--char", default="captain", help="Character id (output folder + filename prefix).")
    p.add_argument("--denoise", type=float, default=denoise_default, dest="denoise")
    p.add_argument("--distilled-cfg", type=float, default=3.0, dest="distilled_cfg")
    p.add_argument("--steps", type=int, default=24)
    p.add_argument("--seed", type=int, default=-1, help="-1=random; fixed seeds increment per --count image.")
    p.add_argument("--count", "-n", type=int, default=1)
    p.add_argument("--width", type=int, default=832)
    p.add_argument("--height", type=int, default=1216)
    p.add_argument("--sampler", default="Euler")
    p.add_argument("--scheduler", default="simple")
    p.add_argument("--max-side", type=int, default=1024, dest="max_side", help="ImageStitch reference max side length.")
    p.add_argument("--prompt", default=None)
    p.add_argument("--prompt-file", default=None, dest="prompt_file")
    p.add_argument("--neg", default=None)
    p.add_argument("--neg-file", default=None, dest="neg_file")
    p.add_argument("--model", default=None, help="Override sd_model_checkpoint for the request.")
    p.add_argument("--timeout", type=int, default=600)


def main():
    ap = argparse.ArgumentParser(description="FLUX.2 Klein character art harness.")
    sub = ap.add_subparsers(dest="mode", required=True)

    pb = sub.add_parser("base", help="Head-shot -> 3/4-body restyled figure.")
    add_common(pb, denoise_default=0.95)
    pb.add_argument("--method", choices=["ref", "pad", "txt2img"], default="ref")
    pb.add_argument("--restyle-head", type=float, default=0.0, dest="restyle_head",
                    help="pad method: if >0, repaint the source head into the painterly medium at this denoise "
                         "(~0.8 matches base_8) before pasting, so face and body share one style.")
    pb.add_argument("--restyle-seed", type=int, default=None, dest="restyle_seed",
                    help="pad method: fix the head-restyle seed (default: follow --seed). Set this to reuse a "
                         "chosen head while --seed/--count vary only the body/pose.")
    pb.add_argument("--head-scale", type=float, default=0.40, dest="head_scale",
                    help="pad method: pasted head width as fraction of canvas width (smaller = smaller head).")
    pb.add_argument("--head-y", type=float, default=0.04, dest="head_y",
                    help="pad method: pasted head top offset as fraction of canvas height.")
    pb.add_argument("--keep-ratio", type=float, default=0.82, dest="keep_ratio",
                    help="pad method: vertical extent of the kept face ellipse (fraction of head height; bottom edge near the chin).")
    pb.add_argument("--keep-w", type=float, default=0.66, dest="keep_w",
                    help="pad method: width of the kept face ellipse as a fraction of the pasted head width.")
    pb.add_argument("--mask-blur", type=int, default=24, dest="mask_blur",
                    help="pad method: feather (px) at the face/body inpaint boundary.")
    pb.add_argument("--source", default=None, help=f"Source head-shot (default: {DEFAULT_SOURCE.name}).")
    pb.add_argument("--refs", nargs="*", default=None, help="Extra ImageStitch reference image paths.")
    pb.add_argument("--char-desc", default=CAPTAIN_DESC, dest="char_desc",
                    help="Subject description injected into the default base prompt.")
    pb.set_defaults(func=mode_base)

    pe = sub.add_parser("expr", help="Expression variant from an approved base.")
    add_common(pe, denoise_default=0.4)
    pe.add_argument("expr", help="Expression word(s), e.g. angry / surprised / sad.")
    pe.add_argument("--base", required=True, help="Approved base image path.")
    pe.add_argument("--method", choices=["reprompt"], default="reprompt")
    pe.set_defaults(func=mode_expr)

    ps = sub.add_parser("scene", help="Bake the character into a location.")
    add_common(ps, denoise_default=0.82)
    ps.add_argument("--base", required=True, help="Approved base image path.")
    ps.add_argument("--location", required=True, help="Location background image path.")
    ps.add_argument("--room-desc", default=None, dest="room_desc",
                    help="Room description for the prompt (default: derived from filename).")
    ps.set_defaults(func=mode_scene)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
