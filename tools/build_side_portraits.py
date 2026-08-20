"""Rebuild the framed side portraits from the new full-body character renders.

The side portraits (260x269, gold frame, flat dark backdrop) are used by the
character screen, the progress and thread screens, and the say-screen side
image. Up to four variants exist per character: colour, hover, black-and-white
(a character not yet unlocked) and bw hover.

This keeps each portrait's own frame and backdrop and swaps only the face. It
drops in <char>_full_size_front_head.png -- the head shot cut by
`character_cutout.py head` -- scaled so every crown and chin land in the same
place, then rebuilds the other three variants from the result.

  frame    - the pixels identical across every portrait in side/ (the 7px
             border plus the corner flourishes). Copied over untouched, so the
             frame's anti-aliased edges still blend against that character's
             own backdrop.
  backdrop - a plane fitted to the strips just inside the frame on the left and
             right, sampled above the shoulders and extended down the canvas.
  hover    - a levels curve read off the shipped pairs: out = in * 1.5625 - 22
  bw       - Rec.601 luma, then out = in * 1.3071 - 15.29 for its own hover.

The portraits as they were before this first ran are kept in
Images/characters_original_and_archive/side_before_new_heads/, and that is
where the frame, the backdrop and the list of variants are read from -- so the
script can be rerun over its own output without drifting.

  python tools/build_side_portraits.py                 # every character
  python tools/build_side_portraits.py captain lad     # just these
  python tools/build_side_portraits.py --out <dir>     # preview, game untouched
"""

import argparse
import os
import sys
from glob import glob

import numpy as np
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADS = os.path.join(ROOT, "Images", "characters_new")
SIDES = os.path.join(ROOT, "Murder", "game", "images", "characters")
# The portraits as they shipped before the new heads went in. Frame, backdrop
# and the list of variants each character owns are read from here, so running
# this twice gives the same result rather than compounding on its own output.
ORIGINALS = os.path.join(ROOT, "Images", "characters_original_and_archive",
                         "side_before_new_heads")

CHARACTERS = ["broken", "butler", "captain", "doctor", "drunk", "footman",
              "host", "lad", "maid", "nurse", "psychic"]

# Where the head shot sits inside its own 256x256 square -- these are the
# framing constants character_cutout.py cuts to (HEAD_ROOM and 1/HEAD_FRAME).
SQUARE_CROWN = 0.14
SQUARE_NECK = 0.14 + 1 / 1.55

# Where it should sit in the portrait. The head has to be tall enough for the
# bottom of the square to reach the bottom of the canvas, or the chest would
# stop short and leave a band of bare backdrop under the collar.
CROWN_Y = 18
HEAD_H = 216

# The heads are cut from a render lit on a pale backdrop, so on this dark wash
# they read as a sticker unless something grounds them. A soft shadow cast down
# and to the right does it.
SHADOW = (0.34, 9, (5, 8))      # strength, blur radius, offset

BACKDROP_STRIP = 13     # width of the sampling strip inside each side of frame
BACKDROP_ROWS = 150     # sample above this row only -- shoulders reach the
                        # sides further down and would poison the fit

HOVER = (1.5625, -22.0)
BW_HOVER = (1.3071, -15.29)
LUMA = np.array([0.299, 0.587, 0.114])

SOURCE = ORIGINALS if os.path.isdir(ORIGINALS) else SIDES

VARIANTS = [
    ("side", "{char}"),
    ("side_hover", "{char} hover"),
    ("side_bw", "{char} bw"),
    ("side_bw_hover", "{char} bw hover"),
]


def side_path(root, folder, stem):
    return os.path.join(root, folder, "side " + stem + ".png")


def frame_mask():
    """Pixels every shipped portrait has in common: the frame and its corners."""
    stack = np.stack([np.array(Image.open(f).convert("RGB"), dtype=np.int16)
                      for f in sorted(glob(os.path.join(SOURCE, "side", "*.png")))])
    spread = stack.max(0) - stack.min(0)
    return spread.max(2) < 12


def backdrop(orig):
    """The flat wash behind the head, fitted as a plane so it meets the frame
    at exactly the colour that is already painted under the frame's edges."""
    a = np.array(orig.convert("RGB"), dtype=float)
    h, w = a.shape[:2]
    ys, xs = np.mgrid[0:h, 0:w]
    strip = np.zeros((h, w), bool)
    strip[7:BACKDROP_ROWS, 7:7 + BACKDROP_STRIP] = True
    strip[7:BACKDROP_ROWS, w - 7 - BACKDROP_STRIP:w - 7] = True

    basis = np.stack([xs[strip], ys[strip], np.ones(strip.sum())], 1)
    full = np.stack([xs.ravel(), ys.ravel(), np.ones(h * w)], 1)
    out = np.stack([(full @ np.linalg.lstsq(basis, a[..., c][strip], rcond=None)[0])
                    .reshape(h, w) for c in range(3)], 2)
    return np.clip(out, 0, 255)


def place_head(head, size, head_h=None, crown_y=None):
    """Scale the head shot and lay it on a canvas the size of the portrait."""
    head_h = HEAD_H if head_h is None else head_h
    crown_y = CROWN_Y if crown_y is None else crown_y
    w, h = size
    scale = head_h / ((SQUARE_NECK - SQUARE_CROWN) * head.height)
    edge = round(head.width * scale)
    top = round(crown_y - SQUARE_CROWN * edge)
    if top + edge < h:
        print(f"  ! head only reaches y={top + edge} of {h} -- raise HEAD_H")
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    layer.paste(head.resize((edge, edge), Image.LANCZOS), (round(w / 2 - edge / 2), top))
    return layer


def cast_shadow(wash, head):
    """Darken the backdrop under the head so it does not float in the frame."""
    strength, radius, (dx, dy) = SHADOW
    blurred = head.split()[-1].filter(ImageFilter.GaussianBlur(radius))
    shadow = Image.new("L", head.size, 0)
    shadow.paste(blurred, (dx, dy))
    return wash * (1 - strength * (np.array(shadow, dtype=float) / 255)[..., None])


def levels(a, curve):
    return np.clip(a * curve[0] + curve[1], 0, 255)


def build(char, mask, out_root, head_h=None, crown_y=None):
    head_file = os.path.join(HEADS, char, "base", char + "_full_size_front_head.png")
    if not os.path.exists(head_file):
        print(f"[skip] {char}: no head shot at {head_file}")
        return
    orig = Image.open(side_path(SOURCE, "side", char)).convert("RGBA")

    head = place_head(Image.open(head_file).convert("RGBA"), orig.size, head_h, crown_y)
    base = Image.fromarray(cast_shadow(backdrop(orig), head).astype("uint8")).convert("RGBA")
    base.alpha_composite(head)

    # The frame is painted back over the top rather than composited under the
    # head, so a wide hat or a turban is cropped by the frame instead of
    # spilling across it.
    colour = np.where(mask[..., None], np.array(orig, dtype=float),
                      np.array(base, dtype=float))
    grey = np.repeat((colour[..., :3] @ LUMA)[..., None], 3, 2)
    made = {
        "{char}": colour[..., :3],
        "{char} hover": levels(colour[..., :3], HOVER),
        "{char} bw": grey,
        "{char} bw hover": levels(grey, BW_HOVER),
    }

    for folder, pattern in VARIANTS:
        stem = pattern.format(char=char)
        target = side_path(out_root, folder, stem)
        if not os.path.exists(side_path(SOURCE, folder, stem)):
            continue        # this character never had that variant
        rgb = np.rint(made[pattern]).astype("uint8")
        alpha = np.full(rgb.shape[:2] + (1,), 255, "uint8")
        os.makedirs(os.path.dirname(target), exist_ok=True)
        Image.fromarray(np.concatenate([rgb, alpha], 2), "RGBA").save(target)
        print(f"  {os.path.relpath(target, ROOT)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("chars", nargs="*", default=None,
                    help="Characters to rebuild (default: all of them).")
    ap.add_argument("--out", default=SIDES,
                    help="Write somewhere else to look before replacing the game's.")
    ap.add_argument("--head-h", type=float, default=HEAD_H,
                    help=f"Crown-to-throat height in the portrait (default {HEAD_H}).")
    ap.add_argument("--crown-y", type=float, default=CROWN_Y,
                    help=f"Row the top of the head lands on (default {CROWN_Y}).")
    args = ap.parse_args()

    chars = args.chars or CHARACTERS
    unknown = [c for c in chars if c not in CHARACTERS]
    if unknown:
        sys.exit("No portrait for: " + ", ".join(unknown))

    mask = frame_mask()
    for char in chars:
        print(f"[{char}]")
        build(char, mask, args.out, args.head_h, args.crown_y)


if __name__ == "__main__":
    main()
