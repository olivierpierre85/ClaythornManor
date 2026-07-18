"""Build the in-game manor map images from the AI floor-plan renders.

Sources: Images/maps new ai tests/new_{downstairs,ground_floor,first_floor,attic}.png
(1536x1024 architect-sheet renders sharing the same frame/title template) plus
attic_frame_titles_legend.png, the reusable blank frame (titles, compass, scale,
credits, empty plan area).

For each floor this script:
  1. detects the "<FLOOR> PLAN" and "BUILT 1840" title lines and erases them,
     keeping the floor-name line as a snippet,
  2. crops the plan (outer wall rect + per-floor overflow margins: garden below
     the ground floor, gun-room block below the basement, attic dormers),
  3. scales it so the outer walls land on the COMMON wall rect WALL_T - this is
     what keeps the walls at the same position on every floor of the imagemap,
  4. pastes plan + floor-name snippet into the frame, downsizes to 960x640 and
     writes map_idle/map_hover/map_insensitive_<floor>.png into the game.

It also prints the room hotspot rects (x, y, w, h) for scripts/map.rpy, derived
from ROOMS (room interiors in source-image coordinates). If a source image is
regenerated, re-measure its wall rect (see FLOORS) and rerun.
"""

import os
import random
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageStat

random.seed(7)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "Images", "maps new ai tests")
GAME_MAP = os.path.join(ROOT, "Murder", "game", "images", "ui", "map")

FRAME = Image.open(os.path.join(DIR, "attic_frame_titles_legend.png")).convert("RGB")
FW, FH = FRAME.size

# Common target wall rectangle in frame (1536x1024) space
WALL_T = (285, 185, 1250, 770)
BAND_CENTER = (768, 158)          # where the floor-name line goes
OUT = (960, 640)
FS = OUT[0] / FW

FLOORS = {
    # floor: (file, wall rect in source, crop extras (L, T, R, B),
    #         pre-cover boxes, needs_arrows)
    # needs_arrows: the source's "<FLOOR> PLAN" line has no side ornaments
    # (basement), so the attic's are composed around it.
    0: ("new_downstairs.png",   (179, 180, 1357, 864), (6, 6, 8, 30), [], True),
    1: ("new_ground_floor.png", (241, 165, 1301, 795), (8, 6, 8, 139),
        [(1262, 918, 1345, 1005)], False),   # source's own "All measurements" text
    # B=12 keeps the wall's soft shadow (rows 903-912); the architect credit
    # below it starts at y=939, well clear of the crop
    2: ("better_bedrooms_image.png", (206, 165, 1318, 902), (12, 6, 12, 12), [], False),
    3: ("new_attic.png",        (185, 185, 1339, 856), (8, 10, 14, 16), [], False),
}

MARGIN_SAMPLE = (58, 240, 150, 560)
frame_tone = ImageStat.Stat(FRAME.crop(MARGIN_SAMPLE)).mean


def make_parchment_fill(src, w, h):
    sources = [(58, 240, 150, 560), (1388, 200, 1478, 780)]

    def random_patch(size):
        sx0, sy0, sx1, sy1 = random.choice(sources)
        x = random.randint(sx0, sx1 - size)
        y = random.randint(sy0, sy1 - size)
        return src.crop((x, y, x + size, y + size))

    base = Image.new("RGB", (w, h))
    step = 64
    for ty in range(0, h, step):
        for tx in range(0, w, step):
            base.paste(random_patch(step), (tx, ty))
    base = base.filter(ImageFilter.GaussianBlur(24))

    psize = 72
    fmask = Image.new("L", (psize, psize), 0)
    d = ImageDraw.Draw(fmask)
    d.ellipse((6, 6, psize - 6, psize - 6), fill=255)
    fmask = fmask.filter(ImageFilter.GaussianBlur(8))
    n = max((w // 20) * (max(h, 40) // 20), 40)
    for _ in range(n):
        p = random_patch(psize)
        base.paste(p, (random.randint(-36, max(w - 36, 1)),
                       random.randint(-36, max(h - 36, 1))), fmask)
    return base


def cover(canvas, src, box, feather=3):
    """Replace box with synthesised parchment, feathered into the canvas."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    tex = make_parchment_fill(src, w, h)
    layer = canvas.copy()
    layer.paste(tex, (x0, y0))
    mask = Image.new("L", canvas.size, 0)
    s = feather // 2 + 1
    mask.paste(Image.new("L", (w - 2 * s, h - 2 * s), 255), (x0 + s, y0 + s))
    mask = mask.filter(ImageFilter.GaussianBlur(feather))
    return Image.composite(layer, canvas, mask)


def paste_feathered(canvas, snippet, topleft, feather=2):
    w, h = snippet.size
    x0, y0 = topleft
    layer = canvas.copy()
    layer.paste(snippet, (x0, y0))
    mask = Image.new("L", canvas.size, 0)
    mask.paste(Image.new("L", (w - 4, h - 4), 255), (x0 + 2, y0 + 2))
    mask = mask.filter(ImageFilter.GaussianBlur(feather))
    return Image.composite(layer, canvas, mask)


def title_lines(gray, wall_top):
    """Return (plan_line_box, built_line_box) via row-gap grouping."""
    px = gray.load()
    rows = []
    for y in range(92, wall_top - 4):
        n = sum(1 for x in range(420, 1160, 2) if px[x, y] < 140)
        rows.append((y, n))
    groups = []
    cur = None
    for y, n in rows:
        if n > 3:
            if cur is None:
                cur = [y, y]
            else:
                cur[1] = y
        else:
            if cur and cur[1] - cur[0] >= 6:
                groups.append(tuple(cur))
            cur = None
    if cur and cur[1] - cur[0] >= 6:
        groups.append(tuple(cur))
    assert len(groups) >= 2, groups
    plan_rows, built_rows = groups[-2], groups[-1]

    def xspan(r0, r1):
        xmin, xmax = None, None
        for x in range(350, 1200):
            for y in range(r0, r1 + 1, 2):
                if px[x, y] < 140:
                    if xmin is None:
                        xmin = x
                    xmax = x
                    break
        return xmin, xmax

    px0, px1 = xspan(*plan_rows)
    bx0, bx1 = xspan(*built_rows)
    plan_box = (px0 - 10, plan_rows[0] - 6, px1 + 10, plan_rows[1] + 5)
    built_box = (bx0 - 8, built_rows[0] - 5, bx1 + 8, built_rows[1] + 4)
    return plan_box, built_box


def channel_scale(img, r, g, b):
    cr, cg, cb = img.split()
    cr = cr.point(lambda v: min(255, int(v * r)))
    cg = cg.point(lambda v: min(255, int(v * g)))
    cb = cb.point(lambda v: min(255, int(v * b)))
    return Image.merge("RGB", (cr, cg, cb))


transforms = {}

# Arrow ornaments flanking the title lines, borrowed from the attic's
# "ATTIC FLOOR PLAN" (dark-run groups at x 569-614 and 939-983, 14px from
# the text) for sources that lack them.
_attic = Image.open(os.path.join(DIR, FLOORS[3][0])).convert("RGB")
_abox, _ = title_lines(_attic.convert("L"), FLOORS[3][1][1])
ARROW_L = _attic.crop((566, _abox[1], 618, _abox[3]))
ARROW_R = _attic.crop((935, _abox[1], 987, _abox[3]))
ARROW_GAP = 14

for floor, (fname, wall, extras, precover, needs_arrows) in FLOORS.items():
    src = Image.open(os.path.join(DIR, fname)).convert("RGB")
    assert abs(src.width - FW) <= 4 and abs(src.height - FH) <= 4, (fname, src.size)
    gray = src.convert("L")

    plan_box, built_box = title_lines(gray, wall[1])
    snippet = src.crop(plan_box)

    clean = cover(src, src, plan_box)
    clean = cover(clean, src, built_box)
    for box in precover:
        clean = cover(clean, src, box)

    L, T, R, B = extras
    crop_box = (wall[0] - L, wall[1] - T, wall[2] + R, wall[3] + B)
    crop = clean.crop(crop_box)

    # tone-match this source's parchment to the frame's
    tone = ImageStat.Stat(src.crop(MARGIN_SAMPLE)).mean
    ratios = [frame_tone[i] / tone[i] for i in range(3)]
    if max(abs(1 - r) for r in ratios) > 0.006:
        crop = channel_scale(crop, *ratios)

    kx = (WALL_T[2] - WALL_T[0]) / (wall[2] - wall[0])
    ky = (WALL_T[3] - WALL_T[1]) / (wall[3] - wall[1])
    crop = crop.resize((round(crop.width * kx), round(crop.height * ky)), Image.LANCZOS)

    canvas = FRAME.copy()
    dest = (round(WALL_T[0] - L * kx), round(WALL_T[1] - T * ky))
    canvas = paste_feathered(canvas, crop, dest, feather=3)

    sw, sh = snippet.size
    if needs_arrows:
        law, lah = ARROW_L.size
        raw, rah = ARROW_R.size
        total = law + ARROW_GAP + sw + ARROW_GAP + raw
        x = BAND_CENTER[0] - total // 2
        canvas = paste_feathered(canvas, ARROW_L, (x, BAND_CENTER[1] - lah // 2))
        canvas = paste_feathered(
            canvas, snippet,
            (x + law + ARROW_GAP, BAND_CENTER[1] - sh // 2))
        canvas = paste_feathered(
            canvas, ARROW_R,
            (x + law + ARROW_GAP + sw + ARROW_GAP, BAND_CENTER[1] - rah // 2))
    else:
        canvas = paste_feathered(
            canvas, snippet,
            (BAND_CENTER[0] - sw // 2, BAND_CENTER[1] - sh // 2))

    idle = canvas.resize(OUT, Image.LANCZOS)
    hover = channel_scale(ImageEnhance.Color(idle).enhance(1.25), 1.04, 0.97, 0.78)
    insensitive = ImageEnhance.Brightness(idle).enhance(0.84)

    idle.save(os.path.join(GAME_MAP, "map_idle_%d.png" % floor))
    hover.save(os.path.join(GAME_MAP, "map_hover_%d.png" % floor))
    insensitive.save(os.path.join(GAME_MAP, "map_insensitive_%d.png" % floor))

    transforms[floor] = (wall, kx, ky)
    print(floor, fname, "plan_box:", plan_box, "kx=%.3f ky=%.3f" % (kx, ky))

# Room interiors in SOURCE-image coordinates, hotspots go to the wall midline
ROOMS = {
    3: {
        "storage": (215, 215, 590, 820),
        "males_room": (955, 200, 1310, 400),
        "females_room": (955, 415, 1310, 620),
        "attic_butler_room": (955, 635, 1310, 825),
    },
    2: {
        "bedroom_lad": (223, 182, 608, 377),
        "bedroom_doctor": (223, 377, 608, 550),
        "bedroom_captain": (223, 550, 608, 707),
        "bedroom_psychic": (223, 707, 608, 888),
        "bedroom_host": (936, 182, 1301, 377),
        "bedroom_drunk": (936, 377, 1301, 550),
        "bedroom_broken": (936, 550, 1301, 707),
        "bedroom_nurse": (936, 707, 1301, 888),
    },
    1: {
        "tea_room": (270, 195, 515, 450),
        "library": (270, 465, 515, 770),
        "servant_stairs": (540, 190, 985, 265),
        "portrait_gallery": (540, 285, 985, 440),
        "entrance_hall": (540, 455, 985, 770),
        "billiard_room": (1010, 195, 1275, 450),
        "dining_room": (1010, 465, 1275, 770),
        "manor_garden": (420, 810, 1010, 930),
    },
    0: {
        "scullery": (215, 205, 640, 395),
        "kitchen": (215, 410, 640, 845),
        "gun_room": (660, 600, 980, 855),
        "garage": (1005, 210, 1340, 845),
    },
}

print("\n--- hotspot rects (x, y, w, h) in 960x640 for scripts/map.rpy ---")
for floor in sorted(ROOMS):
    wall, kx, ky = transforms[floor]
    for rid, (x0, y0, x1, y1) in ROOMS[floor].items():
        X0 = (WALL_T[0] + (x0 - wall[0]) * kx) * FS
        Y0 = (WALL_T[1] + (y0 - wall[1]) * ky) * FS
        X1 = (WALL_T[0] + (x1 - wall[0]) * kx) * FS
        Y1 = (WALL_T[1] + (y1 - wall[1]) * ky) * FS
        print(floor, rid, (round(X0), round(Y0), round(X1 - X0), round(Y1 - Y0)))
