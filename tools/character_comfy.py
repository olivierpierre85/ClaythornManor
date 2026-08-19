"""
Character art harness for the local ComfyUI server (native API at
http://127.0.0.1:8188).

TWO MODELS drive the very same pipeline -- pick with --model / -m:

    klein9b   (default) Flux 2 Klein 9B distilled: cfg 1.0, 12 steps, ~35 s an
              image. It fits in VRAM, so nothing is streamed from system RAM.
    dev       Flux 2 Dev: guidance 3.5, 24 steps, ~140 s an image. The reference
              finish and the strongest likeness -- worth a final pass once the
              pose and outfit are settled.

MATCHING DEV'S FINISH ON KLEIN
------------------------------
Left alone, Klein paints flat cel shading with hard outlines. Two things fix it and
both are on by default: the PAINTERLY suffix appended to its prompts, and -- doing
most of the work -- a Dev render chained in as a SECOND reference, which carries the
painterly house style across. The exemplar transfers style only: another character's
Dev picture does not leak their face or clothes, so a character with no Dev render of
their own still gets the right finish from STYLE_EXEMPLAR.

    --style-ref <path>   use this Dev render as the exemplar
    --no-style-ref       identity reference alone (flat Klein look)

Resolution order: --style-ref, then <char>_flux2dev_front.png, then any Dev render of
that character, then STYLE_EXEMPLAR.

Outputs are tagged with the model (`lad_klein9b_base.png` vs `lad_flux2dev_base.png`)
so the two never overwrite each other, and each model has its own approved front
slot (`<char>_klein9b_front.png` / `<char>_flux2dev_front.png`).

TWO STAGES:

    base <char>   Head-shot  ->  a darker, subtly-stylised FULL-BODY FRONTAL figure
                  (head to feet, shoes included). The likeness comes from the
                  head-shot (fed through ReferenceLatent); the outfit and everything
                  else come from the character description.

    turn <char>   Take the APPROVED frontal base and turn the figure (still full-body,
                  head to feet). The reference is now the front image, which already
                  carries the outfit, so the clothes stay identical across the turn --
                  only the pose changes. Two angles:
                    --angle three_quarter  45 degrees (default). BIMODAL on Klein: some
                                           seeds collapse back to frontal, so roll 3-4
                                           and pick.
                    --angle profile        side-on, face in silhouette. Reliable.
                  --direction left|right picks which way they turn.

WORKFLOW
--------
1.  python tools/character_comfy.py base captain            # a few frontal candidates
2.  pick the best one and copy it to the approved front slot:
        Images/characters_new/captain/base/captain_klein9b_front.png
3.  python tools/character_comfy.py turn captain            # 3/4 turns of that front

Each character has an entry in CHARACTERS (head-shot path + description). Because both
stages render the whole body, descriptions must cover trousers/skirt and footwear too.
Outputs are numbered (never overwritten) under Images/characters_new/<char>/base/.

EXAMPLES
--------
  python tools/character_comfy.py base lad --count 3
  python tools/character_comfy.py base lad --model dev --count 3
  python tools/character_comfy.py base captain --seed 1924 --count 1
  python tools/character_comfy.py turn captain --count 4
  python tools/character_comfy.py turn lad --angle profile --count 2
  python tools/character_comfy.py turn lad --angle profile --direction right --count 2
"""
import argparse
import json
import random
import sys
import time
import urllib.parse
from pathlib import Path

import requests
from PIL import Image

ROOT = Path(__file__).parent.parent.resolve()
OUT_ROOT = ROOT / "Images" / "characters_new"
SERVER = "http://127.0.0.1:8188"

# ---- Models ----------------------------------------------------------------
# Two models drive the very same pipeline (same registry names as
# tools/scene_comfy.py). They differ in three places only: which loader carries
# the weights, how the reference image is rescaled, and how the conditioning is
# guided.
#
#   guider "flux"  -> FluxGuidance + BasicGuider                  (dev, guidance 3.5)
#   guider "cfg"   -> CFGGuider against a ConditioningZeroOut negative, cfg 1.0
#                     (klein9b -- it is guidance-distilled, so FluxGuidance is inert)


# Left to itself Klein paints flat cel shading with hard outlines. This pushes it back
# towards the painterly finish Dev gives for free -- it is only half the job, though:
# the style REFERENCE below does the rest.
PAINTERLY = (
    " Rendered as a soft oil painting: visible painted brushwork, smoothly blended "
    "gradient shading, warm reflected light and soft shadow edges, fine skin texture "
    "and woven cloth grain, delicate painted detail throughout. No flat cel shading, "
    "no hard black ink outlines, no clean vector lineart, no comic-book look."
)

# A Dev render chained in as a SECOND reference is what actually carries the house
# finish over to Klein. It transfers style only -- a picture of another character does
# not leak that character's face or clothes -- so any approved Dev image works as the
# fallback exemplar for a character that has no Dev render of their own yet.
STYLE_EXEMPLAR = "Images/characters_new/captain/base/captain_flux2dev_base.png"


class Model:
    """A diffusion model plus the text encoder, loaders and dials it needs.

    kind "unet" loads through UNETLoader (models/diffusion_models), kind "ckpt"
    through CheckpointLoaderSimple (models/checkpoints) taking ONLY its MODEL
    output -- both files are transformer-only, so the text encoder and the VAE
    are always loaded separately.

    The text encoder is NOT interchangeable: Klein was trained against Qwen 3 8B
    and Dev against Mistral 3 Small: pairing the wrong one fails in the sampler
    with "mat1 and mat2 shapes cannot be multiplied" (see tools/scene_comfy.py).
    """

    def __init__(self, kind, file, tag, clip, clip_type, steps, base_guidance,
                 turn_guidance, guider, note, style_suffix="", wants_style_ref=False):
        self.kind = kind
        self.file = file
        self.tag = tag                      # goes into the output filenames
        self.clip = clip
        self.clip_type = clip_type
        self.steps = steps
        self.base_guidance = base_guidance
        self.turn_guidance = turn_guidance
        self.guider = guider                # "flux" | "cfg"
        self.note = note
        self.style_suffix = style_suffix     # extra prompt wording this model needs
        self.wants_style_ref = wants_style_ref


VAE_NAME = "flux2-vae.safetensors"

MODELS = {
    # Default. Klein 9B is size- AND step-distilled and fits in the 12.8 GB card
    # outright, so a figure lands in ~35 s instead of ~140 s. cfg 1.0 comes from
    # ComfyUI's own "Image Edit (Flux.2 Klein 9B Distilled)" template (which samples
    # at 4 steps); 12 steps is where the painted texture stops improving -- 20 looked
    # no better, and 8 came out smoother and more airbrushed.
    "klein9b": Model("ckpt", "flux-2-klein-9b-nvfp4.safetensors", "klein9b",
                     "qwen_3_8b.safetensors", "flux2", 12, 1.0, 1.0, "cfg",
                     "Flux 2 Klein 9B, 5.4 GB -- fits in VRAM, distilled, fast",
                     style_suffix=PAINTERLY, wants_style_ref=True),
    # The original path: slower and heavier, but the strongest likeness and the finish
    # everything else is matched against. Dev paints it unprompted, so it needs neither
    # the PAINTERLY suffix nor an exemplar. Worth it for a final approved front.
    "dev": Model("unet", "flux2-dev-nvfp4.safetensors", "flux2dev",
                 "mistral_3_small_flux2_fp4_mixed.safetensors", "flux2", 24, 3.5, 3.0, "flux",
                 "Flux 2 Dev, 19.6 GB -- best likeness, offloads to RAM, slow"),
}

# ---- Per-character registry -------------------------------------------------
# head_shot: source portrait for the `base` stage (relative to repo root).
# description: the full subject sentence injected into the prompts -- spell out
#   face AND clothing/uniform, or the likeness and outfit will drift. Set to None
#   until written; the tool refuses to run a character whose description is None.
#   The stages render the FULL body (head to feet), so describe trousers/skirt and
#   footwear as well -- anything left unsaid is re-invented on every seed.


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
            "leather Sam Browne belt and diagonal shoulder strap, matching olive-drab "
            "uniform trousers with a sharp crease, polished dark brown leather ankle boots"
        ),
    ),
    "lad": Character(
        head_shot="Images/characters_original_and_archive/side/side lad.png",
        description=(
            "a young man of about twenty-two, fair skin with a faint ruddy flush, tousled "
            "light blond hair swept across the forehead, clear green eyes, clean-shaven with "
            "soft youthful features and a full mouth, a wary watchful expression, wearing a "
            "a light brown 1920s waistcoat over a white collarless shirt with the sleeves "
            "rolled up, no jacket, dark brown wool trousers held up by braces and a little "
            "loose at the ankle, heavy old-fashioned 1920s working boots of scuffed brown "
            "leather, laced high over the ankle through metal eyelets, with a blunt rounded "
            "toe, thick stitched leather soles and a low stacked heel, the clothes clean but "
            "a little cheap and ill-fitting, only subtly worn with no visible dirt or stains, "
            "the clothes of a working man trying to pass in gentry company"
        ),
    ),
    "psychic": Character(
        head_shot="Images/characters_original_and_archive/side/side psychic.png",
        description=(
            "a gaunt woman in her early sixties, a deeply lined careworn face with hollow "
            "cheeks, pale skin and calm pale hazel eyes with an ordinary, steady gaze, thin "
            "lips touched with dark red, greying hair wrapped in a soft draped headscarf or "
            "cloche of dusky violet silk, small drop earrings, wearing a layered 1920s dress "
            "in deep plum, a long fringed shawl in muted teal and burnt orange with an "
            "embroidered paisley border, long strings of amber and amethyst beads, colours "
            "that are rich and jewel-toned but softened and dusty rather than bright, the "
            "skirt falling to mid-calf over dark warm-brown stockings, soft worn "
            "oxblood-brown leather shoes with a low heel and a button strap, the leather a "
            "warm reddish brown that picks up the amber beads rather than plain black, the "
            "theatrical look of a spiritualist medium"
        ),
    ),
    "doctor": Character(
        head_shot="Images/characters_original_and_archive/side/side doctor.png",
        description=(
            "a gaunt middle-aged man of about fifty, greying dark hair combed back from a "
            "high forehead, round wire-rimmed spectacles, sunken tired eyes with dark shadows "
            "beneath, pale sallow skin and hollow lined cheeks, clean-shaven, a weary faintly "
            "furtive expression, wearing a respectable bottle-green 1920s three-piece tweed "
            "suit with a waistcoat and a warm brown tie, tidy and well-kept, matching tweed "
            "trousers with turn-ups at the ankle, black leather 1920s Oxford shoes with a "
            "plain rounded toe, closed lacing over the instep and a low stacked leather heel, "
            "the proper middle-class look of a charity-hospital doctor with a quiet morphine habit"
        ),
    ),
    "nurse": Character(
        head_shot="Images/characters_original_and_archive/side/side nurse.png",
        description=(
            "a plain woman in her early fifties, dark brown hair lightly greying, parted in "
            "the centre and drawn loosely back, pale lined skin, cool blue-grey eyes, an "
            "unadorned ageing face with a reserved, faintly severe and disapproving "
            "expression, wearing a plain high-collared dark 1920s dress with a pale collar and "
            "a small brooch, the skirt falling to mid-calf over dark stockings, sensible black "
            "leather laced walking shoes with a rounded toe, a stitched toe cap and a low "
            "stacked heel, austere, spinsterish and respectable"
        ),
    ),
    "drunk": Character(
        head_shot="Images/characters_original_and_archive/side/side drunk.png",
        description=(
            "a grizzled older man of about sixty, unkempt greying hair and a grey stubbled "
            "beard, ruddy weathered and deeply lined skin, bleary bloodshot eyes and a loose "
            "wry half-smile, wearing a rumpled dark charcoal-grey 1920s three-piece suit with "
            "a crooked loosened tie and an unbuttoned waistcoat, the suit clean but well-worn "
            "and creased, only subtly shabby with no visible dirt or stains, matching "
            "charcoal-grey trousers bagging at the knee and rumpled over the shoe, scuffed "
            "black leather 1920s Oxford shoes with a rounded toe, closed lacing and a low "
            "stacked heel, a once-respectable barrister gone to drink"
        ),
    ),
    "broken": Character(
        # Masked -- his in-game identity (the side portrait is masked too). For the
        # disfigured face instead, point at the maskless portrait and describe the scarring.
        head_shot="Images/characters_original_and_archive/side/side broken.png",
        description=(
            "a lean young man of about thirty, a smooth unlined youthful face with a firm "
            "jaw and taut clear skin, no grey whatsoever in his hair and none at the "
            "temples, wearing a carved painted wooden half-mask (a mask of "
            "pale carved wood in muted browns, with a visible wood grain) that covers the "
            "disfigured nose and upper face, weary watchful eyes visible through it, a soft "
            "flat cloth cap over short dark brown hair, wearing a plain working-class 1920s "
            "outfit of "
            "collarless pale shirt, waistcoat and jacket in muted tones, full-length dark "
            "hard-wearing wool trousers hanging straight down, narrow at the ankle with the "
            "hem resting on the top of the boot, scuffed dark brown leather 1920s working "
            "boots on a narrow close-fitting last, laced high over the ankle through six "
            "pairs of small metal eyelets, with a tapered almond toe, a thin stitched "
            "leather sole with a slim welted edge and a low stacked heel built of visible "
            "layers of leather, the leather matte and worn rather than polished, no thick "
            "moulded rubber sole and no bulbous round-toed modern work boot, a disfigured "
            "war veteran hiding behind the mask"
        ),
    ),
    "host": Character(
        head_shot="Images/characters_original_and_archive/side/side host.png",
        description=(
            "an elegant woman of about forty-five, softly waved silver-grey hair set in a "
            "1920s finger-wave bob, arched brows, striking green eyes, pale powdered skin and "
            "dark red lips, a poised composed and faintly theatrical expression, wearing a "
            "refined dark red 1920s evening gown with a beaded collar and ropes of pearls, "
            "the gown hanging straight down to the ankle, pale silk stockings, dark red satin "
            "1920s evening bar shoes with a rounded almond toe and a single narrow strap "
            "buttoned across the instep, set on a curved Louis heel of middling height that "
            "flares out again where it meets the ground, no slender modern stiletto and no "
            "strap around the ankle, an out-of-work actress playing the part of a grand lady"
        ),
    ),
    # --- staff ---
    "butler": Character(
        head_shot="Images/characters_original_and_archive/side/side butler.png",
        description=(
            "a solidly built older man of about sixty, broad-shouldered and powerfully built, "
            "greying hair swept back from a weathered composed face, green-hazel eyes and a "
            "faint reserved smile, clean-shaven, wearing formal butler's attire of a black "
            "1920s tailcoat, white wing-collar shirt and black bow tie, black formal trousers "
            "with a sharp crease, highly polished black leather Oxford shoes with a plain "
            "rounded toe and a low heel, dignified and imposing"
        ),
    ),
    "footman": Character(
        head_shot="Images/characters_original_and_archive/side/side footman.png",
        description=(
            "a handsome man of about thirty-five, dark brown hair combed back, clean-shaven "
            "with no moustache, blue-grey eyes and a smooth composed expression, wearing "
            "footman's livery of a dark tailcoat with a high stand collar and brass buttons "
            "over a white shirt, dark livery trousers with a narrow braid stripe down the "
            "outside seam, polished black leather shoes with a rounded toe and a low heel, "
            "poised and well-groomed"
        ),
    ),
    "maid": Character(
        head_shot="Images/characters_original_and_archive/side/side maid.png",
        description=(
            "a young woman of about twenty-two, dark brown hair pinned back beneath a white "
            "cap, fair freckled skin, blue-grey eyes and a plain fresh reserved face, wearing "
            "a black 1920s housemaid's dress with a white apron, white collar and cuffs, the "
            "skirt falling to mid-calf over black stockings, plain flat black leather laced "
            "shoes with a rounded toe and a low stacked heel, neat and demure"
        ),
    ),
}

# ---- Prompt templates -------------------------------------------------------
# Shared house style. Character specifics live in {desc}; keep this generic.
STYLE = (
    "a refined semi-realistic digital illustration with a gentle, very subtle touch "
    "of cartoon stylisation, muted low-key colour palette"
)

# Stage 1: head-shot -> frontal FULL-BODY figure (head to feet, nothing cropped).
BASE_PROMPT = (
    "{style}, of {desc}. Depict them as a full-length full-body standing portrait, the "
    "whole figure visible from the top of the head down to the feet, both legs and both "
    "shoes entirely inside the frame, nothing cut off at any edge, a clear margin of "
    "empty background above the head and below the shoes, the standing figure filling "
    "the height of the tall narrow frame. Shot from a distance at eye level with the "
    "whole body in view, facing directly forward toward the viewer, body squared to the "
    "camera, shoulders straight and level, feet flat on the ground and slightly apart, "
    "the head small within the frame, natural head-to-body proportions with the figure "
    "about seven and a half heads tall, hands resting at their sides. Soft naturalistic "
    "brushwork with slightly cleaner, gently stylised shading, realistic facial structure "
    "and lifelike proportions, matte illustration, soft even studio lighting, plain "
    "neutral warm-grey background."
)

# Stage 2: turn the approved front. Klein ignores a polite "about twenty degrees" and
# hands back a frontal figure, so each angle is spelled out anatomically -- which side
# comes forward, what happens to the far cheek and the far ear. No hedges like "still
# facing the viewer": those collapse it straight back to frontal (see memory).
# NOTE: no left/right wording. Klein ignores it -- it turns the figure to the viewer's
# left whatever the prompt says -- and asking made the 45-degree pose land less often.
# Use --mirror for the other side.
TURN_POSES = {
    "three_quarter": (
        "Show the exact same character from the reference image, {desc}. Keep the outfit, "
        "face, hair and colours identical to the reference, only change the pose: they have "
        "turned halfway to the side, standing at forty-five degrees to the camera, their "
        "near shoulder closer to the viewer and the far shoulder drawn back behind them, "
        "the head turned the same way so the face is seen at three-quarters, the far cheek "
        "narrowed and the far ear hidden, the line of the nose breaking the edge of the far "
        "cheek. A three-quarter view of a standing figure."
    ),
    "profile": (
        "Show the exact same character from the reference image, {desc}. Keep the outfit, "
        "face, hair and colours identical to the reference, only change the pose: they have "
        "turned to stand side-on to the viewer, their whole body rotated ninety degrees so "
        "we see them from the side, one shoulder toward the camera and the other hidden "
        "behind it, the face in full profile looking off to the side, the nose and chin in "
        "silhouette against the background, the far arm hidden behind the torso. A side "
        "view of a standing figure."
    ),
}

# Shared tail: same full-body framing as the base stage.
TURN_FRAME = (
    " A full-length full-body standing portrait, the whole figure visible from the top of "
    "the head down to the feet, both shoes entirely inside the frame, a clear margin of "
    "empty background above the head and below the shoes, hands resting at their sides, "
    "{style}, matte illustration, soft even studio lighting, plain neutral warm-grey "
    "background."
)

# Filename tag per angle.
ANGLE_TAGS = {"three_quarter": "3q", "profile": "profile"}

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


def build_graph(be, refs, prompt, seed, guidance, width, height, steps, prefix):
    """The Flux 2 reference/pose graph, wired for model `be`.

    refs: [server_image_name, ...] in conditioning order -- the identity reference
    (head-shot, or the approved front) first, then an optional style exemplar. Each
    one is encoded and stacked onto the conditioning as its own ReferenceLatent.

    Same skeleton for both models. Only the loaders, the reference rescale node and
    the guider change.
    """
    if be.kind == "ckpt":
        loader = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": be.file}}
    else:
        loader = {"class_type": "UNETLoader", "inputs": {"unet_name": be.file, "weight_dtype": "default"}}

    g = {
        "10": loader,
        "11": {"class_type": "CLIPLoader", "inputs": {"clip_name": be.clip, "type": be.clip_type}},
        "12": {"class_type": "VAELoader", "inputs": {"vae_name": VAE_NAME}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["11", 0], "text": prompt}},
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

    # Klein guides with a real (if toothless) CFG pair, so the references have to be
    # stacked onto the zeroed-out negative as well -- the Dev path has no negative.
    pos = ["6", 0]
    neg = None
    if be.guider == "cfg":
        g["7"] = {"class_type": "ConditioningZeroOut", "inputs": {"conditioning": ["6", 0]}}
        neg = ["7", 0]

    for i, name in enumerate(refs):
        n = 200 + i * 10
        if be.guider == "cfg":
            # Klein has no Kontext rescale step: it takes its references at 1 megapixel.
            scale = {"class_type": "ImageScaleToTotalPixels",
                     "inputs": {"image": [f"{n}", 0], "upscale_method": "lanczos",
                                "megapixels": 1.0, "resolution_steps": 16}}
        else:
            scale = {"class_type": "FluxKontextImageScale", "inputs": {"image": [f"{n}", 0]}}
        g[f"{n}"] = {"class_type": "LoadImage", "inputs": {"image": name}}
        g[f"{n + 1}"] = scale
        g[f"{n + 2}"] = {"class_type": "VAEEncode", "inputs": {"pixels": [f"{n + 1}", 0], "vae": ["12", 0]}}
        g[f"{n + 3}"] = {"class_type": "ReferenceLatent",
                         "inputs": {"conditioning": pos, "latent": [f"{n + 2}", 0]}}
        pos = [f"{n + 3}", 0]
        if neg:
            g[f"{n + 4}"] = {"class_type": "ReferenceLatent",
                             "inputs": {"conditioning": neg, "latent": [f"{n + 2}", 0]}}
            neg = [f"{n + 4}", 0]

    if be.guider == "cfg":
        g["14"] = {"class_type": "CFGGuider",
                   "inputs": {"model": ["10", 0], "positive": pos, "negative": neg, "cfg": guidance}}
    else:
        g["13"] = {"class_type": "FluxGuidance", "inputs": {"conditioning": pos, "guidance": guidance}}
        g["14"] = {"class_type": "BasicGuider", "inputs": {"model": ["10", 0], "conditioning": ["13", 0]}}
    return g


def run_batch(args, be, ref_paths, prompt, guidance, stem):
    """Upload the references, then generate args.count images (incrementing/rolling seeds)."""
    out_dir = OUT_ROOT / args.char / "base"
    out_dir.mkdir(parents=True, exist_ok=True)

    steps = args.steps if args.steps is not None else be.steps
    dial = "cfg" if be.guider == "cfg" else "guidance"
    shown = "  +  ".join(Path(r).name for r in ref_paths)
    print(f"       model = {args.model}  reference = {shown}")
    print(f"       {dial} = {guidance}  steps = {steps}  size = {args.width}x{args.height}")
    refs = [upload_image(r, args.server) for r in ref_paths]

    made = []
    for k in range(max(1, args.count)):
        seed = random.randint(0, 2**31 - 1) if args.seed < 0 else args.seed + k
        graph = build_graph(be, refs, prompt, seed, guidance, args.width, args.height, steps, stem)
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


def resolve_model(args):
    if args.model not in MODELS:
        sys.exit(f"Unknown model '{args.model}'. Known: {', '.join(MODELS)}")
    return MODELS[args.model]


def resolve_style_ref(args, be):
    """The Dev render chained in behind the identity reference to carry the house finish.

    --style-ref wins; --no-style-ref switches it off. Otherwise, for a model that asks
    for one, take this character's own approved Dev front, else any Dev render of them,
    else the project exemplar.
    """
    if args.no_style_ref:
        return None
    if args.style_ref:
        path = Path(args.style_ref)
        if not path.exists():
            sys.exit(f"Style reference not found: {path}")
        return path
    if not be.wants_style_ref:
        return None

    base_dir = OUT_ROOT / args.char / "base"
    front = base_dir / f"{args.char}_flux2dev_front.png"
    if front.exists():
        return front
    own = sorted(base_dir.glob(f"{args.char}_flux2dev_*.png"))
    if own:
        return own[0]
    exemplar = ROOT / STYLE_EXEMPLAR
    if exemplar.exists():
        return exemplar
    print(f"  ! no style reference found -- {args.model} will paint flatter than Dev. "
          f"Pass --style-ref <a Dev render> or generate one with --model dev.")
    return None


def mode_base(args):
    ch, desc = resolve_character(args)
    be = resolve_model(args)
    head = Path(args.head_shot) if args.head_shot else (ROOT / ch.head_shot) if ch.head_shot else None
    if not head or not head.exists():
        sys.exit(f"Head-shot not found for '{args.char}'. Set it in CHARACTERS or pass --head-shot.")

    prompt = args.prompt or (BASE_PROMPT.format(style=STYLE, desc=desc) + be.style_suffix)
    guidance = args.guidance if args.guidance is not None else be.base_guidance
    refs = [str(head)]
    style = resolve_style_ref(args, be)
    if style:
        refs.append(str(style))
    print(f"[base] char={args.char}  (head-shot -> frontal full-body figure)")
    made, out_dir = run_batch(args, be, refs, prompt, guidance, f"{args.char}_{be.tag}_base")
    print(f"[base] {len(made)} image(s) -> {out_dir}")
    print(f"       promote your pick to: {out_dir / (args.char + '_' + be.tag + '_front.png')}")


def mode_turn(args):
    ch, desc = resolve_character(args)
    be = resolve_model(args)
    front = Path(args.front) if args.front else OUT_ROOT / args.char / "base" / f"{args.char}_{be.tag}_front.png"
    if not front.exists():
        sys.exit(
            f"Approved front not found: {front}\n"
            f"Run `base {args.char}` first, then copy your chosen candidate to that path."
        )

    prompt = args.prompt or (
        TURN_POSES[args.angle].format(desc=desc)
        + TURN_FRAME.format(style=STYLE)
        + be.style_suffix
    )
    guidance = args.guidance if args.guidance is not None else be.turn_guidance
    refs = [str(front)]
    style = resolve_style_ref(args, be)
    # The front IS the style when it came out of the same model family as the exemplar.
    if style and style.resolve() != front.resolve():
        refs.append(str(style))
    angle_word = "side-on profile" if args.angle == "profile" else "three-quarter turn"
    stem = f"{args.char}_{be.tag}_{ANGLE_TAGS[args.angle]}"
    print(f"[turn] char={args.char}  (front -> {angle_word}, facing the viewer's left)")
    made, out_dir = run_batch(args, be, refs, prompt, guidance, stem)
    if args.mirror:
        for path in made:
            Image.open(path).transpose(Image.FLIP_LEFT_RIGHT).save(path)
        print(f"[turn] mirrored to face the other way "
              f"(check any asymmetric kit -- straps, buttoning -- ended up on the right side)")
    print(f"[turn] {len(made)} image(s) -> {out_dir}")


# ---- CLI --------------------------------------------------------------------


def add_common(p):
    p.add_argument("char", help="Character id (e.g. captain). See CHARACTERS.")
    p.add_argument("--count", "-n", type=int, default=3, help="How many images (each a different seed).")
    p.add_argument("--seed", type=int, default=-1, help="-1 = random per image; a fixed value increments per --count.")
    p.add_argument("--model", "-m", choices=sorted(MODELS), default="klein9b",
                   help="Which model to sample with (default: klein9b, the fast distilled one).")
    p.add_argument("--guidance", type=float, default=None,
                   help="klein9b: CFG (default 1.0). dev: FluxGuidance (default base 3.5, turn 3.0).")
    p.add_argument("--steps", type=int, default=None, help="Sampling steps (default: klein9b 8, dev 24).")
    p.add_argument("--width", type=int, default=768)
    p.add_argument("--height", type=int, default=1408)
    p.add_argument("--style-ref", default=None, dest="style_ref",
                   help="Dev render to chain in as the style exemplar (default: this "
                        "character's Dev render, else the project exemplar).")
    p.add_argument("--no-style-ref", action="store_true", dest="no_style_ref",
                   help="Generate from the identity reference alone.")
    p.add_argument("--desc", default=None, help="Override the character description for this run.")
    p.add_argument("--prompt", default=None, help="Override the ENTIRE prompt for this run.")
    p.add_argument("--server", default=SERVER)
    p.add_argument("--timeout", type=int, default=600)


def main():
    ap = argparse.ArgumentParser(description="ComfyUI Flux 2 Dev character art harness.")
    sub = ap.add_subparsers(dest="mode", required=True)

    pb = sub.add_parser("base", help="Head-shot -> frontal full-body figure (head to feet).")
    add_common(pb)
    pb.add_argument("--head-shot", default=None, dest="head_shot", help="Override the source head-shot path.")
    pb.set_defaults(func=mode_base)

    pt = sub.add_parser("turn", help="Turn the approved front into a moderate 3/4 view.")
    add_common(pt)
    pt.add_argument("--front", default=None, help="Override the approved front reference path.")
    pt.add_argument("--angle", choices=sorted(TURN_POSES), default="three_quarter",
                    help="How far round: three_quarter (45 degrees) or profile (side-on).")
    pt.add_argument("--mirror", action="store_true",
                    help="Flip the finished image so he faces the other way. Mirrors any "
                         "asymmetric kit too (a Sam Browne strap swaps shoulders).")
    pt.set_defaults(func=mode_turn)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
