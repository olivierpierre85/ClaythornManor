"""
Cut a character render out of its studio background and drop them into a room.

Two steps, both local (no ComfyUI, no network):

    cut <char>      Matte the figure off the flat grey backdrop and save a tightly
                    cropped RGBA sprite next to the source render.

    place <char>    Composite that sprite into a location background three times --
                    far, middle and near -- so the size a figure wants to be in a
                    1920x1088 room can be judged at a glance.

    bust <char>     The same sprite zoomed right in and pushed below the bottom edge,
                    so only his top half is on screen: waist-up, chest-up and
                    shoulders-up, one preview each.

Matting uses rembg's `u2net_human_seg` model (cached in ~/.u2net). Its raw mask is
hardened, eroded a pixel or two and feathered, which beats rembg's own alpha matting
here: against a flat low-contrast backdrop that leaves a smoky halo. Nothing is written
into Murder/game/ -- the preview lands beside the character art for eyeballing.

EXAMPLES
--------
  python tools/character_cutout.py cut lad
  python tools/character_cutout.py place lad --room entrance_hall_day
  python tools/character_cutout.py place lad --room library_night --heights 0.5 0.7 0.9
  python tools/character_cutout.py bust  lad --room entrance_hall_day
  python tools/character_cutout.py bust  lad --framing chest --x 0.35
"""
import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).parent.parent.resolve()
OUT_ROOT = ROOT / "Images" / "characters_new"
ROOMS = ROOT / "Murder" / "game" / "images" / "locations"

# Where a figure stands, as fractions of the room frame:
#   x       centre of the figure, 0 = left edge, 1 = right edge
#   feet    ground line, 1 = bottom edge of the frame
#   height  figure height as a share of the frame height
# Further away = higher ground line and smaller figure, which is the whole point of
# the preview: three depths at once.
PLACEMENTS = [
    {"x": 0.20, "feet": 0.74, "height": 0.46},   # far, back of the room
    {"x": 0.50, "feet": 0.88, "height": 0.66},   # middle distance
    {"x": 0.81, "feet": 1.00, "height": 0.90},   # near, foreground
]


def cutout_path(src):
    return src.with_name(src.stem + "_cutout.png")


def mode_cut(args):
    from rembg import new_session, remove

    src = Path(args.src) if args.src else OUT_ROOT / args.char / "base" / f"{args.char}_klein9b_front.png"
    if not src.exists():
        sys.exit(f"Source render not found: {src}\nPass --src <path> to point at another one.")

    img = Image.open(src).convert("RGB")
    session = new_session(args.matte_model)

    # Take the raw mask, NOT rembg's alpha matting: against a flat low-contrast
    # backdrop its trimap turns a wide band of backdrop into half-transparent pixels
    # and the sprite carries a smoky halo into the scene.
    mask = remove(img, session=session, only_mask=True).convert("L")

    # Harden the mask, pull the edge IN by a pixel so no backdrop colour survives
    # along it, then feather a touch so the silhouette is not stair-stepped.
    a = np.array(mask, dtype=np.uint8)
    a = np.where(a > args.threshold, 255, 0).astype(np.uint8)
    alpha = Image.fromarray(a)
    for _ in range(max(0, args.erode)):
        alpha = alpha.filter(ImageFilter.MinFilter(3))
    alpha = alpha.filter(ImageFilter.GaussianBlur(args.feather))

    cut = img.convert("RGBA")
    cut.putalpha(alpha)
    box = cut.getbbox()
    if box:
        cut = cut.crop(box)

    out = cutout_path(src)
    cut.save(out)
    print(f"[cut] {src.name} -> {out.name}  ({cut.width}x{cut.height}, matte {args.matte_model}, "
          f"threshold {args.threshold}, erode {args.erode}, feather {args.feather})")
    print(f"      {out}")


# Zoomed-in framings: the SAME sprite scaled up and pushed down past the bottom edge,
# so only the top of the figure is on screen. `visible` is how much of the whole figure
# stays in frame; `head_top` is where the crown of the head sits in the frame.
BUSTS = [
    {"name": "waist", "visible": 0.52, "head_top": 0.08},
    {"name": "chest", "visible": 0.38, "head_top": 0.09},
    {"name": "shoulders", "visible": 0.27, "head_top": 0.11},
]


def paste_clipped(room, figure, x, y):
    """alpha_composite `figure` at (x, y), trimming whatever falls outside the frame."""
    rw, rh = room.size
    left, top = max(0, -x), max(0, -y)
    right = min(figure.width, rw - x)
    bottom = min(figure.height, rh - y)
    if right <= left or bottom <= top:
        return
    room.alpha_composite(figure.crop((left, top, right, bottom)), (x + left, y + top))


def ground_shadow(size, alpha=110):
    """A soft ellipse to sit under the feet -- without it a sprite floats."""
    w, h = size
    shadow = Image.new("L", (w, h), 0)
    ImageDraw.Draw(shadow).ellipse((0, 0, w - 1, h - 1), fill=alpha)
    return shadow.filter(ImageFilter.GaussianBlur(h / 3.5))


def mode_place(args):
    src = Path(args.src) if args.src else OUT_ROOT / args.char / "base" / f"{args.char}_klein9b_front.png"
    sprite_path = Path(args.cutout) if args.cutout else cutout_path(src)
    if not sprite_path.exists():
        sys.exit(f"Cutout not found: {sprite_path}\nRun `cut {args.char}` first.")

    room_path = ROOMS / f"{args.room}.png"
    if not room_path.exists():
        sys.exit(f"Room not found: {room_path}")

    room = Image.open(room_path).convert("RGBA")
    sprite = Image.open(sprite_path).convert("RGBA")
    rw, rh = room.size

    heights = args.heights or [p["height"] for p in PLACEMENTS]
    if len(heights) != len(PLACEMENTS):
        sys.exit(f"--heights takes exactly {len(PLACEMENTS)} values (far, middle, near).")

    # Near figures go down last so they overlap the ones behind them.
    for spot, height_frac in sorted(zip(PLACEMENTS, heights), key=lambda p: p[1]):
        h = int(rh * height_frac)
        w = max(1, round(sprite.width * h / sprite.height))
        figure = sprite.resize((w, h), Image.LANCZOS)
        feet_y = int(rh * spot["feet"])
        x = int(rw * spot["x"] - w / 2)

        shadow = ground_shadow((int(w * 0.95), max(8, int(h * 0.055))))
        room.paste((0, 0, 0), (x + int(w * 0.025), feet_y - shadow.height // 2), shadow)
        room.alpha_composite(figure, (x, feet_y - h))
        print(f"  placed {w}x{h} at x={x} feet={feet_y}  ({height_frac:.2f} of frame height)")

    out = OUT_ROOT / args.char / f"{args.char}_scale_test_{args.room}.png"
    room.convert("RGB").save(out, quality=95)
    print(f"[place] {sprite_path.name} x3 in {args.room} -> {out}")


def mode_bust(args):
    src = Path(args.src) if args.src else OUT_ROOT / args.char / "base" / f"{args.char}_klein9b_front.png"
    sprite_path = Path(args.cutout) if args.cutout else cutout_path(src)
    if not sprite_path.exists():
        sys.exit(f"Cutout not found: {sprite_path}\nRun `cut {args.char}` first.")

    room_path = ROOMS / f"{args.room}.png"
    if not room_path.exists():
        sys.exit(f"Room not found: {room_path}")

    sprite = Image.open(sprite_path).convert("RGBA")
    wanted = [b for b in BUSTS if args.framing in (None, b["name"])]
    if not wanted:
        sys.exit(f"Unknown framing '{args.framing}'. Known: {', '.join(b['name'] for b in BUSTS)}")

    for bust in wanted:
        room = Image.open(room_path).convert("RGBA")
        rw, rh = room.size
        # The visible band runs from the crown of the head to the bottom edge, and that
        # band is `visible` of the whole figure -- which fixes how far to zoom in.
        y0 = int(rh * bust["head_top"])
        h = int((rh - y0) / bust["visible"])
        w = max(1, round(sprite.width * h / sprite.height))
        figure = sprite.resize((w, h), Image.LANCZOS)
        x = int(rw * args.x - w / 2)
        paste_clipped(room, figure, x, y0)

        out = OUT_ROOT / args.char / f"{args.char}_bust_test_{args.room}_{bust['name']}.png"
        room.convert("RGB").save(out, quality=95)
        print(f"  {bust['name']:<9} figure {w}x{h} ({h / rh:.1f}x frame height), "
              f"head at y={y0}, {bust['visible']:.0%} of him on screen -> {out.name}")
    print(f"[bust] {len(wanted)} preview(s) -> {OUT_ROOT / args.char}")


def main():
    ap = argparse.ArgumentParser(description="Cut a character out and preview them in a room.")
    sub = ap.add_subparsers(dest="mode", required=True)

    pc = sub.add_parser("cut", help="Matte the figure off its backdrop into an RGBA sprite.")
    pc.add_argument("char")
    pc.add_argument("--src", default=None, help="Source render (default: <char>_klein9b_front.png).")
    pc.add_argument("--matte-model", default="u2net_human_seg", dest="matte_model",
                    help="rembg model (default: u2net_human_seg).")
    pc.add_argument("--threshold", type=int, default=140, help="Mask cut-off, 0-255 (default 140).")
    pc.add_argument("--erode", type=int, default=2, help="Pixels to pull the edge in (default 2).")
    pc.add_argument("--feather", type=float, default=0.8, help="Edge blur in pixels (default 0.8).")
    pc.set_defaults(func=mode_cut)

    pp = sub.add_parser("place", help="Composite the sprite into a room at three depths.")
    pp.add_argument("char")
    pp.add_argument("--room", default="entrance_hall_day", help="Location image stem.")
    pp.add_argument("--src", default=None, help="Source render the cutout was made from.")
    pp.add_argument("--cutout", default=None, help="Sprite to place (default: <src>_cutout.png).")
    pp.add_argument("--heights", type=float, nargs="*", default=None,
                    help="Three figure heights as fractions of the frame (far middle near).")
    pp.set_defaults(func=mode_place)

    pb = sub.add_parser("bust", help="Zoom the sprite in and run it off the bottom edge.")
    pb.add_argument("char")
    pb.add_argument("--room", default="entrance_hall_day", help="Location image stem.")
    pb.add_argument("--src", default=None, help="Source render the cutout was made from.")
    pb.add_argument("--cutout", default=None, help="Sprite to place (default: <src>_cutout.png).")
    pb.add_argument("--framing", default=None, choices=[b["name"] for b in BUSTS],
                    help="Just one framing (default: all three).")
    pb.add_argument("--x", type=float, default=0.5, help="Where he stands across the frame (0-1).")
    pb.set_defaults(func=mode_bust)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
