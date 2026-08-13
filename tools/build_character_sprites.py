"""Build Ren'Py body sprites from the generated character base renders.

The base renders (Images/characters_new/<char>/base/*.png) are all framed the
same way: 832x1216, head to mid-thigh, flat studio background.  Because the
framing is identical for every character we can cut the background out and
scale every image by the same factor, which keeps heads and shoulders aligned
when several sprites stand side by side on screen.

Output: Murder/game/images/characters/body/body_<char>.png
Ren'Py picks those up automatically as the images ``body_lad``, ``body_captain``
and so on (one tag per character, so several can be shown at once).

Usage:
    python tools/build_character_sprites.py                # every character
    python tools/build_character_sprites.py lad captain    # a subset
    python tools/build_character_sprites.py --height 1000  # override the size
"""

import argparse
import io
from pathlib import Path

from PIL import Image, ImageFilter
import numpy as np
from rembg import new_session, remove

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "Images" / "characters_new"
DEST_DIR = ROOT / "Murder" / "game" / "images" / "characters" / "body"

# Sprites stand on the bottom edge of a 1920x1080 screen.  1000px leaves the
# head about 80px below the top of the screen and puts the waist just above the
# text box (which starts at y=802).
TARGET_HEIGHT = 880

# Trim this many pixels off the silhouette before feathering it, to kill the
# fringe of background colour the matting model leaves behind.
EDGE_EROSION = 2
EDGE_FEATHER = 1.0


def pick_base_image(char_dir: Path) -> Path | None:
    """Return the base render for a character, preferring the lowest suffix."""
    base_dir = char_dir / "base"
    if not base_dir.is_dir():
        return None

    candidates = sorted(base_dir.glob("*.png"))
    return candidates[0] if candidates else None


def cut_out(image: Image.Image, session) -> Image.Image:
    """Remove the studio background and clean up the resulting alpha edge."""
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")

    cut = Image.open(
        io.BytesIO(
            remove(
                buffer.getvalue(),
                session=session,
                post_process_mask=True,
            )
        )
    ).convert("RGBA")

    alpha = cut.getchannel("A")

    # Erode, so the leftover halo of background colour goes with the background.
    if EDGE_EROSION > 0:
        alpha = alpha.filter(ImageFilter.MinFilter(EDGE_EROSION * 2 + 1))

    # Anything the model was unsure about is background - a half transparent
    # sprite edge reads as a glow once it sits over a dark room.
    array = np.asarray(alpha, dtype=np.float32)
    array = np.clip((array - 40.0) * (255.0 / 175.0), 0.0, 255.0)
    alpha = Image.fromarray(array.astype(np.uint8), mode="L")

    if EDGE_FEATHER > 0:
        alpha = alpha.filter(ImageFilter.GaussianBlur(EDGE_FEATHER))

    cut.putalpha(alpha)
    return cut


def build_sprite(source: Path, dest: Path, session, height: int) -> None:
    image = Image.open(source).convert("RGB")
    cut = cut_out(image, session)

    # Uniform scale on the full canvas rather than a per-character crop, so
    # every character keeps the same head height and eye line.
    width = round(cut.width * height / cut.height)
    cut = cut.resize((width, height), Image.LANCZOS)

    # Drop the empty columns on either side - they only cost file size, and the
    # figures are centred in the frame so this does not shift them apart.
    bbox = cut.getchannel("A").getbbox()
    if bbox:
        left, _, right, _ = bbox
        cut = cut.crop((left, 0, right, cut.height))

    dest.parent.mkdir(parents=True, exist_ok=True)
    cut.save(dest, optimize=True)
    print(f"{source.relative_to(ROOT)} -> {dest.relative_to(ROOT)} ({cut.width}x{cut.height})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("characters", nargs="*", help="Character folders to build (default: all)")
    parser.add_argument("--height", type=int, default=TARGET_HEIGHT, help="Sprite height in pixels")
    args = parser.parse_args()

    wanted = set(args.characters)
    session = new_session("u2net_human_seg")

    for char_dir in sorted(p for p in SOURCE_DIR.iterdir() if p.is_dir()):
        if wanted and char_dir.name not in wanted:
            continue

        source = pick_base_image(char_dir)
        if source is None:
            print(f"No base render for {char_dir.name}, skipping")
            continue

        build_sprite(source, DEST_DIR / f"body_{char_dir.name}.png", session, args.height)


if __name__ == "__main__":
    main()
