"""
Bake approved character figures into an approved location background as a single
group scene, using the local ComfyUI Flux 2 Dev server (native API at
http://127.0.0.1:8188).

This is the third tool in the Flux 2 Dev family:

    tools/character_comfy.py   head-shot   -> standing character figure
    tools/location_comfy.py    description -> empty room background
    tools/scene_comfy.py       room + figures -> one picture with people in it

TWO MODES
---------
insert  (default choice) One pass per character. Each pass crops the patch of the
        frame where that person will stand, re-renders just that patch with TWO
        references -- the patch and the character -- and blends it back through a
        feathered, colour-matched edge. Only one character reference is ever in
        play, so figures cannot fuse; everything outside the patch is untouched,
        so nobody already placed can drift; and the render is a quarter of the
        area, so it is quicker as well. The patch boxes live in
        scene_prompts_flux2dev.REGIONS -- check them with --show-regions, which
        draws them on the room and costs no GPU time.

group   One pass for the whole picture, with the room and every character chained
        as ReferenceLatent references and the prompt pointing at each by ordinal.
        Composes the three figures together most naturally, but with several
        same-sex references Flux will fuse or drop people, and the room is
        re-rendered so it drifts from the source background.

Either way the output is a NEW scene image (like boxer_neutral.png), not a
replacement for the background it was built from.

MODELS
------
--model dev (default) is Flux 2 Dev: the best likeness, but at 19.6 GB against a
12.8 GB card it streams weights from system RAM and a full frame takes ~7 min.
--model klein9b is Flux 2 Klein 9B (5.4 GB): it fits in VRAM and is step-distilled,
so it is far quicker. If Klein ignores --guidance (it has no guidance embedding),
use --cfg 2.5 instead, which switches the graph to a real CFG guider.

Character descriptions come from tools/character_comfy.py (CHARACTERS) and the
room description from Murder/game/images/locations/_locations.md, so nothing is
re-typed here. The prompt wording lives in tools/scene_prompts_flux2dev.py.

Outputs are numbered (never overwritten) under Images/scenes_new/flux2dev/.
Nothing is written into Murder/game/ -- promote a picture by hand once approved.

EXAMPLES
--------
  python tools/scene_comfy.py insert entrance_hall --chars captain host broken --show-regions
  python tools/scene_comfy.py insert entrance_hall --chars captain host broken
  python tools/scene_comfy.py insert entrance_hall --chars broken --model klein9b
  python tools/scene_comfy.py insert entrance_hall --chars host --region 752,320,416,688
  python tools/scene_comfy.py group  entrance_hall --chars captain host broken -n 3
"""
import argparse
import pathlib
import random
import sys
import time

import numpy as np
import requests
from PIL import Image, ImageDraw, ImageFilter

from character_comfy import CHARACTERS
from comfy_client import (SERVER, download_image, next_available_path,
                          queue_prompt, upload_image, wait_for_images)
from location_comfy import parse_locations
from location_prompts_flux2dev import ROOM_DETAILS
from scene_prompts_flux2dev import (DEFAULT_PLACEMENT, NUMBER_WORDS, ORDINALS,
                                    PLACEMENTS, REGION_PROMPTS, REGIONS,
                                    SCENE_PROMPTS, STYLE_LEAD)

ROOT = pathlib.Path(__file__).parent.parent.resolve()
MD_FILE = ROOT / "Murder/game/images/locations/_locations.md"
LOCATIONS_DIR = ROOT / "Murder/game/images/locations"
CHAR_DIR = ROOT / "Images/characters_new"
DEFAULT_OUT = ROOT / "Images/scenes_new/flux2dev"

# ---- VAE (shared by every model below: all three take a 128-wide patch input) --
VAE_NAME = "flux2-vae.safetensors"


class Model:
    """A diffusion model plus the text encoder and dials it needs.

    kind "unet" loads through UNETLoader (models/diffusion_models), kind "ckpt"
    through CheckpointLoaderSimple (models/checkpoints) taking ONLY its MODEL
    output -- all three files are transformer-only, so the text encoder and the
    VAE are always loaded separately.

    The text encoder is NOT interchangeable. Each model's txt_in layer fixes the
    width of the conditioning it can accept -- read straight off the weights:
        flux2 dev  txt_in [6144, 15360]  = 5120 x 3  -> Mistral 3 Small
        klein 9b   txt_in [4096, 12288]  = 4096 x 3  -> Qwen 3 8B
        klein 4b   txt_in [3072,  7680]  = 2560 x 3  -> Qwen 3 4B (not installed)
    Pairing the wrong one fails in the sampler with "mat1 and mat2 shapes cannot
    be multiplied".
    """

    def __init__(self, kind, file, clip, clip_type, steps, guidance, note):
        self.kind = kind
        self.file = file
        self.clip = clip
        self.clip_type = clip_type
        self.steps = steps
        self.guidance = guidance
        self.note = note


# Sizes matter here: the GPU has 12.8 GB, so Flux 2 Dev (19.6 GB) streams its
# weights from system RAM every render -- that offload, not compute, is why a
# 1920x1088 frame takes ~7 minutes. Both Klein models fit in VRAM outright and
# are step-distilled on top, so they are the fast options.
MODELS = {
    "dev": Model("unet", "flux2-dev-nvfp4.safetensors",
                 "mistral_3_small_flux2_fp4_mixed.safetensors", "flux2", 24, 3.0,
                 "Flux 2 Dev, 19.6 GB -- best likeness, offloads to RAM, slow"),
    "klein9b": Model("ckpt", "flux-2-klein-9b-nvfp4.safetensors",
                     "qwen_3_8b.safetensors", "flux2", 8, 3.0,
                     "Flux 2 Klein 9B, 5.4 GB -- fits in VRAM, distilled, fast"),
    "klein4b": Model("ckpt", "fluxKleinFP8_flux2Klein4bFp8.safetensors",
                     None, "flux2", 8, 3.0,
                     "Flux 2 Klein 4B FP8, 3.6 GB -- needs a Qwen 3 4B encoder, not installed"),
}

# How a figure is pointed at when the character references are stitched into one
# sheet and the ordinals no longer identify a single person.
SHEET_POSITIONS = {
    1: ["the figure"],
    2: ["the left-hand figure", "the right-hand figure"],
    3: ["the left-hand figure", "the middle figure", "the right-hand figure"],
    4: ["the first figure from the left", "the second figure from the left",
        "the third figure from the left", "the fourth figure from the left"],
}


# ---- Inputs -----------------------------------------------------------------


def room_description(room_id):
    """The room's _locations.md description plus its ROOM_DETAILS props."""
    rows = {rid: desc for rid, desc, _section in parse_locations(MD_FILE)}
    if room_id not in rows:
        sys.exit(f"Unknown room id '{room_id}'. Try: python tools/location_comfy.py --list")
    desc = rows[room_id]
    if room_id in ROOM_DETAILS:
        desc = f"{desc}, {ROOM_DETAILS[room_id]}"
    return desc


def character_image(char_id, override=None):
    """The approved figure for a character: the turned 3/4 if one exists, else the base."""
    if override:
        p = pathlib.Path(override)
        if not p.is_absolute():
            p = ROOT / p
        if not p.exists():
            sys.exit(f"Character image not found: {p}")
        return p
    if char_id not in CHARACTERS:
        sys.exit(f"Unknown character '{char_id}'. Known: {', '.join(CHARACTERS)}")
    base_dir = CHAR_DIR / char_id / "base"
    for stem in (f"{char_id}_flux2dev_front.png", f"{char_id}_flux2dev_base.png"):
        p = base_dir / stem
        if p.exists():
            return p
    sys.exit(
        f"No approved figure for '{char_id}' in {base_dir}.\n"
        f"Run `python tools/character_comfy.py base {char_id}` first, or pass --char-images."
    )


def build_prompt(room_id, variant, char_ids, stitched):
    """Fill the scene template: room description + one placement clause per character."""
    clauses = []
    for i, cid in enumerate(char_ids):
        if stitched:
            names = SHEET_POSITIONS.get(len(char_ids))
            where = names[i] if names else f"figure {i + 1} from the left"
            ordinal = f"{where} in {ORDINALS[1]}"
        else:
            ordinal = ORDINALS[i + 1]
        template = PLACEMENTS.get(cid, DEFAULT_PLACEMENT)
        clauses.append(template.format(ordinal=ordinal, desc=CHARACTERS[cid].description))
    count = len(char_ids)
    return SCENE_PROMPTS[variant].format(
        style_lead=STYLE_LEAD,
        room=room_description(room_id),
        count_word=NUMBER_WORDS[count] if count < len(NUMBER_WORDS) else str(count),
        people=" ".join(clauses),
    )


def region_for(room_id, char_id, override=None):
    """The (x, y, w, h) patch this character is painted into, snapped to 16."""
    if override:
        try:
            box = tuple(int(v) for v in override.replace(",", " ").split())
        except ValueError:
            sys.exit("--region wants four numbers: x,y,w,h")
        if len(box) != 4:
            sys.exit("--region wants four numbers: x,y,w,h")
    else:
        entry = REGIONS.get((room_id, char_id))
        if not entry:
            sys.exit(
                f"No region for ({room_id}, {char_id}) in scene_prompts_flux2dev.REGIONS.\n"
                f"Add one, or pass --region x,y,w,h."
            )
        box = entry["box"]
    return tuple(v - v % 16 for v in box)


def build_region_prompt(room_id, variant, char_id, region_override=None):
    """Fill the single-figure template for one character in one patch of a room."""
    entry = REGIONS.get((room_id, char_id))
    if not entry and not region_override:
        sys.exit(f"No region entry for ({room_id}, {char_id}).")
    entry = entry or {}
    return REGION_PROMPTS[variant].format(
        style_lead=STYLE_LEAD,
        surround=entry.get("surround", f"part of the {room_id.replace('_', ' ')} of a 1920s Scottish manor"),
        desc=CHARACTERS[char_id].description,
        pose=entry.get("pose", "They stand still on the open floor, facing the centre of the room."),
    )


# ---- Compositing (local, PIL/numpy) -----------------------------------------


def match_border_colour(rendered, original, ring=24):
    """Nudge the rendered patch so its border ring matches the original's.

    The patch is regenerated, so its floor and wall tones can sit a shade off the
    surrounding frame and leave a visible rectangle. Matching per-channel mean and
    spread over the outer ring -- which is background, not figure -- removes that
    without touching the composition.
    """
    r = np.asarray(rendered, dtype=np.float32)
    o = np.asarray(original, dtype=np.float32)
    if r.shape != o.shape:
        return rendered
    mask = np.zeros(r.shape[:2], dtype=bool)
    mask[:ring, :] = mask[-ring:, :] = True
    mask[:, :ring] = mask[:, -ring:] = True
    out = r.copy()
    for c in range(3):
        rm, rs = r[..., c][mask].mean(), r[..., c][mask].std()
        om, os_ = o[..., c][mask].mean(), o[..., c][mask].std()
        if rs < 1e-3:
            continue
        out[..., c] = (r[..., c] - rm) * (os_ / rs) + om
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


def figure_mask(size, width_frac=0.62, top_frac=0.02, bottom_frac=0.99, feather=32):
    """A soft upright mask covering where the figure (and its shadow) will go.

    Repainting the whole patch lets the model re-imagine the room inside it -- it
    invented a gilt sconce and re-carved a door on the first regional pass. Feeding
    the patch in as the starting latent with only this band unmasked keeps every
    pixel of background it does not need to touch.
    """
    w, h = size
    mask = Image.new("L", (w, h), 0)
    band_w = int(w * width_frac)
    x0 = (w - band_w) // 2
    ImageDraw.Draw(mask).rectangle(
        [x0, int(h * top_frac), x0 + band_w, int(h * bottom_frac)], fill=255
    )
    return mask.filter(ImageFilter.GaussianBlur(feather))


def paste_patch(frame, patch, box, feather=48):
    """Blend a repainted patch back into the frame through a feathered edge."""
    x, y, w, h = box
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rectangle([feather, feather, w - feather - 1, h - feather - 1], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(feather / 2.0))
    out = frame.copy()
    out.paste(patch, (x, y), mask)
    return out


def draw_regions(frame, boxes, labels):
    """Debug overlay: where each figure will be painted, before spending any GPU time."""
    out = frame.copy()
    d = ImageDraw.Draw(out)
    for (x, y, w, h), label in zip(boxes, labels):
        d.rectangle([x, y, x + w - 1, y + h - 1], outline=(255, 80, 80), width=4)
        d.text((x + 8, y + 8), label, fill=(255, 220, 120))
    return out


# ---- Graph ------------------------------------------------------------------


def build_graph(refs, stitched, prompt, seed, guidance, width, height, steps, prefix,
                model=None, cfg=None, init=None, mask=None):
    """Flux 2 multi-reference graph.

    refs: [(server_image_name, megapixels), ...] in conditioning order -- the room
    first, then the characters. A megapixel value of None feeds the image in at its
    native size (what the regional crops want). With `stitched`, every reference
    after the first is joined left-to-right into a single sheet and encoded once.
    """
    model = model or MODELS["dev"]
    if model.kind == "ckpt":
        loader = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": model.file}}
    else:
        loader = {"class_type": "UNETLoader", "inputs": {"unet_name": model.file, "weight_dtype": "default"}}
    if not model.clip:
        sys.exit(f"No text encoder installed for model '{model.file}' -- {model.note}")
    graph = {
        "10": loader,
        "11": {"class_type": "CLIPLoader", "inputs": {"clip_name": model.clip, "type": model.clip_type}},
        "12": {"class_type": "VAELoader", "inputs": {"vae_name": VAE_NAME}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["11", 0], "text": prompt}},
        "15": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "euler"}},
        "16": {"class_type": "Flux2Scheduler", "inputs": {"steps": steps, "width": width, "height": height}},
        "17": {"class_type": "RandomNoise", "inputs": {"noise_seed": seed}},
        "5": {"class_type": "EmptyFlux2LatentImage", "inputs": {"width": width, "height": height, "batch_size": 1}},
    }

    # With init + mask the patch itself is the starting latent and only the masked
    # band is renoised, so the background inside the patch survives untouched.
    latent = ["5", 0]
    if init and mask:
        graph["30"] = {"class_type": "LoadImage", "inputs": {"image": init}}
        graph["31"] = {"class_type": "VAEEncode", "inputs": {"pixels": ["30", 0], "vae": ["12", 0]}}
        graph["32"] = {"class_type": "LoadImage", "inputs": {"image": mask}}
        graph["33"] = {"class_type": "ImageToMask", "inputs": {"image": ["32", 0], "channel": "red"}}
        graph["34"] = {
            "class_type": "SetLatentNoiseMask",
            "inputs": {"samples": ["31", 0], "mask": ["33", 0]},
        }
        latent = ["34", 0]

    # Load every reference image.
    for i, (name, _mp) in enumerate(refs):
        graph[f"{100 + i * 10}"] = {"class_type": "LoadImage", "inputs": {"image": name}}

    # Decide which images become their own reference latent.
    if stitched and len(refs) > 2:
        # Room stays alone; the characters are stitched into one sheet.
        sheet = ["110", 0]
        for i in range(2, len(refs)):
            node = f"{300 + i}"
            graph[node] = {
                "class_type": "ImageStitch",
                "inputs": {
                    "image1": sheet,
                    "image2": [f"{100 + i * 10}", 0],
                    "direction": "right",
                    "match_image_size": True,
                    "spacing_width": 0,
                    "spacing_color": "white",
                },
            }
            sheet = [node, 0]
        sheet_mp = min(2.0, refs[1][1] * (len(refs) - 1))
        sources = [(["100", 0], refs[0][1]), (sheet, sheet_mp)]
    else:
        sources = [([f"{100 + i * 10}", 0], mp) for i, (_name, mp) in enumerate(refs)]

    # Scale -> encode -> chain a ReferenceLatent per source onto the conditioning.
    cond = ["6", 0]
    for i, (image, mp) in enumerate(sources):
        base = 200 + i * 10
        pixels = image
        if mp:  # None = feed it in at its native size (regional crops)
            graph[f"{base}"] = {
                "class_type": "ImageScaleToTotalPixels",
                "inputs": {"image": image, "upscale_method": "lanczos",
                           "megapixels": mp, "resolution_steps": 16},
            }
            pixels = [f"{base}", 0]
        graph[f"{base + 1}"] = {
            "class_type": "VAEEncode",
            "inputs": {"pixels": pixels, "vae": ["12", 0]},
        }
        graph[f"{base + 2}"] = {
            "class_type": "ReferenceLatent",
            "inputs": {"conditioning": cond, "latent": [f"{base + 1}", 0]},
        }
        cond = [f"{base + 2}", 0]

    graph["13"] = {"class_type": "FluxGuidance", "inputs": {"conditioning": cond, "guidance": guidance}}
    if cfg:
        # Klein carries no guidance_in tensor, so FluxGuidance can be inert on it.
        # Real CFG against a zeroed-out negative is the fallback dial.
        graph["19"] = {"class_type": "ConditioningZeroOut", "inputs": {"conditioning": ["6", 0]}}
        graph["14"] = {
            "class_type": "CFGGuider",
            "inputs": {"model": ["10", 0], "positive": ["13", 0], "negative": ["19", 0], "cfg": cfg},
        }
    else:
        graph["14"] = {"class_type": "BasicGuider", "inputs": {"model": ["10", 0], "conditioning": ["13", 0]}}
    graph["18"] = {
        "class_type": "SamplerCustomAdvanced",
        "inputs": {"noise": ["17", 0], "guider": ["14", 0], "sampler": ["15", 0],
                   "sigmas": ["16", 0], "latent_image": latent},
    }
    graph["8"] = {"class_type": "VAEDecode", "inputs": {"samples": ["18", 0], "vae": ["12", 0]}}
    graph["9"] = {"class_type": "SaveImage", "inputs": {"images": ["8", 0], "filename_prefix": prefix}}
    return graph


# ---- Shared setup -----------------------------------------------------------


def resolve_inputs(args):
    """Normalise --chars, find the room image and each character's figure."""
    # Accept "captain host broken", "captain,host,broken" and separate arguments alike
    # (the VS Code task hands the whole list over as one string).
    args.chars = [c for entry in args.chars for c in entry.replace(",", " ").split()]
    unknown = [c for c in args.chars if c not in CHARACTERS]
    if unknown:
        sys.exit(f"Unknown character(s): {', '.join(unknown)}. Known: {', '.join(CHARACTERS)}")
    if args.char_images and len(args.char_images) != len(args.chars):
        sys.exit("--char-images needs exactly one path per --chars entry.")

    room_path = pathlib.Path(args.room_image) if args.room_image else LOCATIONS_DIR / f"{args.room}_{args.variant}.png"
    if not room_path.is_absolute():
        room_path = ROOT / room_path
    if not room_path.exists():
        sys.exit(f"Room image not found: {room_path}")

    char_paths = [
        character_image(cid, args.char_images[i] if args.char_images else None)
        for i, cid in enumerate(args.chars)
    ]
    model = MODELS[args.model]
    steps = args.steps if args.steps is not None else model.steps
    guidance = args.guidance if args.guidance is not None else model.guidance
    return room_path, char_paths, model, steps, guidance


def render(args, refs, prompt, seed, width, height, model, steps, guidance, out_path, prefix,
           init=None, mask=None):
    """Queue one image and download it. Returns the elapsed seconds."""
    t0 = time.time()
    graph = build_graph(refs, False, prompt, seed, guidance, width, height, steps,
                        prefix, model=model, cfg=args.cfg, init=init, mask=mask)
    prompt_id = queue_prompt(graph, args.server)
    images = wait_for_images(prompt_id, args.server, args.timeout)
    download_image(images[0], out_path, args.server)
    return time.time() - t0


# ---- Mode: group (one pass, every character at once) ------------------------


def mode_group(args):
    room_path, char_paths, model, steps, guidance = resolve_inputs(args)
    prompt = args.prompt or build_prompt(args.room, args.variant, args.chars, args.stitch_chars)
    stem = args.stem or f"{args.room}_{'group' if len(args.chars) > 1 else args.chars[0]}_{args.variant}"

    print(f"model      {args.model}  ({model.note})")
    print(f"room       {room_path.relative_to(ROOT)}  ({args.room_mp} MP)")
    for cid, p in zip(args.chars, char_paths):
        print(f"character  {cid:9} {p.relative_to(ROOT)}  ({args.char_mp} MP)")
    if args.stitch_chars:
        print("           (characters stitched into one reference sheet)")
    print(f"size       {args.width}x{args.height}  guidance {guidance}  steps {steps}")
    print(f"\n--- prompt ---\n{prompt}\n--------------\n")
    if args.dry_run:
        return

    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        refs = [(upload_image(room_path, args.server), args.room_mp)]
        refs += [(upload_image(p, args.server), args.char_mp) for p in char_paths]
    except requests.exceptions.ConnectionError:
        sys.exit(f"Cannot reach ComfyUI at {args.server} -- is it running?")

    generated = failed = 0
    for k in range(max(1, args.count)):
        seed = random.randint(0, 2**31 - 1) if args.seed < 0 else args.seed + k
        out_path = next_available_path(out_dir, stem)
        print(f"gen {k + 1}/{args.count} seed={seed} -> {out_path.name} ...", end="", flush=True)
        try:
            elapsed = render(args, refs, prompt, seed, args.width, args.height,
                             model, steps, guidance, out_path, f"scene_{stem}")
        except requests.exceptions.ConnectionError:
            print(" FAILED.")
            sys.exit(f"  Is ComfyUI running at {args.server} ?")
        except Exception as e:  # noqa: BLE001 - report and carry on with the next seed
            print(f" FAILED ({e}).")
            failed += 1
            continue
        print(f" ok ({elapsed:.0f}s)")
        generated += 1

    print(f"\nDone -- {generated} generated, {failed} failed. Output: {out_dir}")


# ---- Mode: insert (one pass per character, one patch at a time) -------------


def mode_insert(args):
    room_path, char_paths, model, steps, guidance = resolve_inputs(args)
    boxes = [region_for(args.room, cid, args.region) for cid in args.chars]
    stem = args.stem or f"{args.room}_insert_{args.variant}"
    out_dir = pathlib.Path(args.out)
    work_dir = out_dir / "_work"

    print(f"model      {args.model}  ({model.note})")
    print(f"room       {room_path.relative_to(ROOT)}")
    for cid, p, box in zip(args.chars, char_paths, boxes):
        print(f"insert     {cid:9} {p.relative_to(ROOT)}  patch {box[2]}x{box[3]} at ({box[0]},{box[1]})")
    print(f"           guidance {guidance}  steps {steps}  feather {args.feather}")

    frame = Image.open(room_path).convert("RGB")

    if args.show_regions:
        out_dir.mkdir(parents=True, exist_ok=True)
        overlay = next_available_path(out_dir, f"{stem}_regions")
        draw_regions(frame, boxes, args.chars).save(overlay)
        print(f"\nRegion overlay -> {overlay}")
        return

    prompts = [build_region_prompt(args.room, args.variant, cid, args.region) for cid in args.chars]
    if args.dry_run:
        for cid, p in zip(args.chars, prompts):
            print(f"\n--- prompt: {cid} ---\n{p}")
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    work_dir.mkdir(parents=True, exist_ok=True)

    done = 0
    for i, (cid, char_path, box, prompt) in enumerate(zip(args.chars, char_paths, boxes, prompts), 1):
        x, y, w, h = box
        patch_src = frame.crop((x, y, x + w, y + h))
        patch_path = work_dir / f"{stem}_{i}_{cid}_src.png"
        patch_src.save(patch_path)

        seed = random.randint(0, 2**31 - 1) if args.seed < 0 else args.seed + i - 1
        out_path = next_available_path(out_dir, f"{stem}_{i}_{cid}")
        print(f"pass {i}/{len(args.chars)} {cid:9} seed={seed} {w}x{h} -> {out_path.name} ...",
              end="", flush=True)
        try:
            # The patch goes in at its native size (mp=None); only the character
            # figure is rescaled.
            refs = [(upload_image(patch_path, args.server), None),
                    (upload_image(char_path, args.server), args.char_mp)]
            init_name = mask_name = None
            if not args.no_mask_figure:
                mask_img = figure_mask((w, h), width_frac=args.mask_width,
                                       feather=max(8, args.feather // 2))
                mask_path = work_dir / f"{stem}_{i}_{cid}_mask.png"
                mask_img.convert("RGB").save(mask_path)
                init_name = upload_image(patch_path, args.server)
                mask_name = upload_image(mask_path, args.server)
            rendered_path = work_dir / f"{stem}_{i}_{cid}_raw.png"
            elapsed = render(args, refs, prompt, seed, w, h, model, steps, guidance,
                             rendered_path, f"scene_{stem}_{cid}",
                             init=init_name, mask=mask_name)
        except requests.exceptions.ConnectionError:
            print(" FAILED.")
            sys.exit(f"  Is ComfyUI running at {args.server} ?")
        except Exception as e:  # noqa: BLE001 - report and stop, the chain needs this pass
            print(f" FAILED ({e}).")
            break

        patch = Image.open(rendered_path).convert("RGB")
        if patch.size != (w, h):
            patch = patch.resize((w, h), Image.LANCZOS)
        if not args.no_match_colour:
            patch = match_border_colour(patch, patch_src)
        frame = paste_patch(frame, patch, box, feather=args.feather)
        frame.save(out_path)
        print(f" ok ({elapsed:.0f}s)")
        done += 1

    if done:
        final = next_available_path(out_dir, f"{stem}_final")
        frame.save(final)
        print(f"\nDone -- {done}/{len(args.chars)} figures inserted. Final: {final}")


# ---- CLI --------------------------------------------------------------------


def add_common(p):
    p.add_argument("room", help="Room id from _locations.md (e.g. entrance_hall).")
    p.add_argument("--chars", nargs="+", required=True,
                   help="Character ids to place, in order (e.g. captain host broken).")
    p.add_argument("--model", default="dev", choices=sorted(MODELS),
                   help="Which model to sample with (default: dev). klein9b fits in VRAM and is much faster.")
    p.add_argument("--variant", default="night", choices=["night", "day"],
                   help="Lighting wording and default room image (default: night).")
    p.add_argument("--room-image", default=None, dest="room_image",
                   help="Room background to start from "
                        "(default: Murder/game/images/locations/<room>_<variant>.png).")
    p.add_argument("--char-images", nargs="+", default=None, dest="char_images",
                   help="Explicit figure images, one per --chars entry.")
    p.add_argument("--seed", type=int, default=-1, help="-1 = random; a fixed value increments per image.")
    p.add_argument("--guidance", type=float, default=None, help="FluxGuidance (default: per model).")
    p.add_argument("--cfg", type=float, default=None,
                   help="Use real CFG at this value instead of FluxGuidance (fallback for Klein, "
                        "which carries no guidance embedding).")
    p.add_argument("--steps", type=int, default=None, help="Sampling steps (default: per model).")
    p.add_argument("--char-mp", type=float, default=0.5, dest="char_mp",
                   help="Megapixels each character reference is scaled to (default 0.5).")
    p.add_argument("--stem", default=None, help="Output filename stem.")
    p.add_argument("--out", default=str(DEFAULT_OUT), help="Output folder.")
    p.add_argument("--dry-run", action="store_true", dest="dry_run",
                   help="Print the prompt(s) and queue nothing.")
    p.add_argument("--server", default=SERVER)
    p.add_argument("--timeout", type=int, default=900, help="Per-image wait timeout (s).")


def main():
    ap = argparse.ArgumentParser(
        description="Bake character figures into a location background (ComfyUI, Flux 2 family)."
    )
    sub = ap.add_subparsers(dest="mode", required=True)

    pi = sub.add_parser("insert", help="One pass per character, repainting only that person's patch.")
    add_common(pi)
    pi.add_argument("--region", default=None,
                    help="Override the patch for every character: x,y,w,h in the full frame.")
    pi.add_argument("--feather", type=int, default=48,
                    help="Pixels of feathered blend at the patch edge (default 48).")
    pi.add_argument("--no-match-colour", action="store_true", dest="no_match_colour",
                    help="Skip matching the patch's border tone to the frame.")
    pi.add_argument("--no-mask-figure", action="store_true", dest="no_mask_figure",
                    help="Repaint the whole patch instead of only the figure's band "
                         "(lets the model re-imagine the background inside the patch).")
    pi.add_argument("--mask-width", type=float, default=0.62, dest="mask_width",
                    help="Width of the repainted band as a fraction of the patch (default 0.62).")
    pi.add_argument("--show-regions", action="store_true", dest="show_regions",
                    help="Write an overlay of the patch boxes and stop -- costs no GPU time.")
    pi.set_defaults(func=mode_insert)

    pg = sub.add_parser("group", help="One pass, every character referenced at once.")
    add_common(pg)
    pg.add_argument("--count", "-n", type=int, default=1, help="How many images, each a different seed.")
    pg.add_argument("--width", type=int, default=1920)
    pg.add_argument("--height", type=int, default=1088)
    pg.add_argument("--room-mp", type=float, default=1.0, dest="room_mp",
                    help="Megapixels the room reference is scaled to (default 1.0).")
    pg.add_argument("--stitch-chars", action="store_true", dest="stitch_chars",
                    help="Join the character references into one side-by-side sheet (cheaper).")
    pg.add_argument("--prompt", default=None, help="Override the ENTIRE prompt for this run.")
    pg.set_defaults(func=mode_group)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
