"""
Flux 2 Dev prompt wording for tools/scene_comfy.py -- baking approved character
figures into an approved location background as a single group scene.

Kept apart from the runner for the same reason as location_prompts_flux2dev.py:
the wording is the thing that gets tuned, run after run, and it should be
editable without touching the graph code.

Two Flux 2 Dev lessons drive this wording (see the comfyui-flux2-locations and
comfyui-flux2-character memories):

  * Dev is far more literal than the distilled Klein. Light sources, materials
    and props must be named outright, or a night interior renders near-black.
  * There is NO negative prompt in this graph (single-conditioning BasicGuider),
    so the anti-cues ("No text, no watermark, no signature.") are baked into the
    positive text. The signature cue is deliberate: Dev likes to sign its
    paintings in the bottom-right corner.

The reference images are fed in a fixed order -- the ROOM first, then one per
character -- and the prompt points at them by ordinal, so the model knows which
picture each instruction is about.
"""

# Style lead. The room reference carries most of the look, so this stays short
# and deliberately avoids the words that collapsed earlier location runs
# ("cartoon", "visual novel background", "oil painting").
STYLE_LEAD = (
    "A warm, richly painted wide scene illustration for a 1920s murder-mystery "
    "adventure game, in exactly the same painted style, palette and level of "
    "detail as the first reference image"
)

# Spelled-out counts, so the prompt can pin down exactly how many people appear.
# Dev drops or invents figures without it: the first entrance-hall run rendered only
# two of the three characters plus an anonymous shadow in the middle distance.
NUMBER_WORDS = ["no", "one", "two", "three", "four", "five", "six"]

# How the prompt refers to each uploaded reference, in upload order.
ORDINALS = [
    "the first reference image",
    "the second reference image",
    "the third reference image",
    "the fourth reference image",
    "the fifth reference image",
    "the sixth reference image",
]

# Keyed by lighting variant.
# {style_lead} -- STYLE_LEAD above
# {room}       -- room description (pulled from _locations.md + ROOM_DETAILS)
# {people}     -- the placement sentences below, joined into one paragraph
SCENE_PROMPTS = {
    "night": (
        "{style_lead}. "
        "Recreate the room in the first reference image exactly: the same room in a "
        "1920s Scottish manor, seen from the same camera position and in the same "
        "framing, with the same architecture, furniture, ornaments and warm night "
        "lighting. The room is a {room}. It is lit by glowing brass light fittings and "
        "candle wall sconces, warm amber light pooling across the polished wooden floor "
        "and reflecting in it, deep soft shadows gathering in the corners, dark night "
        "windows. "
        "\n\n"
        "Exactly {count_word} people are standing in this room, and nobody else is in "
        "the picture. Each of them is taken from one of the reference images that "
        "follow the room. {people}"
        "\n\n"
        "They are {count_word} different individuals, each wearing only their own "
        "clothes exactly as shown in their own reference image: never give one person "
        "another person's uniform, belt, hat or garment. Every one of them is shown "
        "full length from head to feet, standing clear of the furniture with their "
        "whole body well inside the frame and room to spare above their head, both feet "
        "planted on the floor, drawn at the correct size for where that person stands "
        "in the room's perspective, with a soft dark contact shadow beneath them and a "
        "faint blurred reflection in the polished floor. The warm light falls on them "
        "from above and the wall sconces light them from the side, so their clothes and "
        "faces take on the warm amber tones of the room while their backs and lower "
        "halves fall into shadow. Keep each face, hairstyle and outfit exactly as it is "
        "in that person's own reference image, and paint every figure in the same style "
        "as the room, as though they had always been part of the picture. "
        "No text, no watermark, no signature."
    ),
    "day": (
        "{style_lead}. "
        "Recreate the room in the first reference image exactly: the same room in a "
        "1920s Scottish manor, seen from the same camera position and in the same "
        "framing, with the same architecture, furniture, ornaments and daylight. The "
        "room is a {room}. Soft muted overcast daylight falls through the tall windows, "
        "subdued grey-silver light, gentle soft shadows, no direct sunbeams. "
        "\n\n"
        "Exactly {count_word} people are standing in this room, and nobody else is in "
        "the picture. Each of them is taken from one of the reference images that "
        "follow the room. {people}"
        "\n\n"
        "They are {count_word} different individuals, each wearing only their own "
        "clothes exactly as shown in their own reference image: never give one person "
        "another person's uniform, belt, hat or garment. Every one of them is shown "
        "full length from head to feet, standing clear of the furniture with their "
        "whole body well inside the frame and room to spare above their head, both feet "
        "planted on the floor, drawn at the correct size for where that person stands "
        "in the room's perspective, with a soft contact shadow beneath them. The window "
        "light falls on them from the side, so their clothes and faces take on the cool "
        "daylight of the room while their far sides fall into gentle shadow. Keep each "
        "face, hairstyle and outfit exactly as it is in that person's own reference "
        "image, and paint every figure in the same style as the room, as though they "
        "had always been part of the picture. No text, no watermark, no signature."
    ),
}

# One clause per character id. {ordinal} is filled with the reference the figure
# comes from, {desc} with that character's description from character_comfy.
# The three positions are chosen from the entrance hall's own geometry: the host
# centre on the stair, the captain left by the lamp-lit console table, and Moody
# right and nearer the camera, so the three sit at three different depths.
PLACEMENTS = {
    "host": (
        "In the centre of the frame, at the foot of the central staircase and standing "
        "on its lowest step with the red stair runner climbing behind her, facing the "
        "viewer with her hands lightly clasped in front of her, stands the woman from "
        "{ordinal}: {desc}. She stands furthest from the camera of the three and is "
        "therefore the smallest figure in the frame."
    ),
    "captain": (
        "On the left-hand side of the hall, out on the open floor and well clear of "
        "the furniture, stands the man from {ordinal}: {desc}. He is fully visible from "
        "his grey head to his boots, brightly lit by the lamp on the console table "
        "beside him, holding himself straight-backed and still with his shoulders "
        "level, turned a little towards the woman on the stair. He is the only person "
        "in the picture wearing a military uniform or a leather shoulder strap."
    ),
    "broken": (
        "On the right-hand side of the hall, a few paces nearer the camera than the "
        "other two but still well inside the room, stands the man from {ordinal}: "
        "{desc}. He is half turned away, watching the others from the edge of the "
        "room, his masked face caught by the warm lamplight. His civilian jacket and "
        "waistcoat are plain, with no belt, no shoulder strap and no military "
        "insignia of any kind. He appears only slightly larger than the other two, and "
        "his whole body from cap to shoes is comfortably inside the frame."
    ),
}

# Used for any character without a hand-written placement above.
DEFAULT_PLACEMENT = (
    "Standing on the open floor of the hall, turned towards the centre of the room, "
    "is the person from {ordinal}: {desc}."
)


# ---------------------------------------------------------------------------
# Regional insertion -- one figure per pass
# ---------------------------------------------------------------------------
# The full-frame route above renders every character from its own reference in a
# single pass, and with two men in the references Flux fused them: the captain
# vanished and Moody was painted wearing the captain's Sam Browne strap. Feeding
# ONE character reference per pass makes that impossible, and cropping the frame
# down to the patch being repainted keeps everything else untouched (no drift for
# figures already placed) while cutting the render to about a quarter of the area.
#
# Each entry is keyed by (room_id, character_id):
#   box       (x, y, w, h) in the full 1920x1088 frame -- the patch that gets
#             repainted. All four values must be multiples of 16. The box IS the
#             scale control: the figure is asked to stand full length inside it,
#             so a taller box makes a bigger person.
#   surround  what is in that patch already, so the model keeps it.
#   pose      how this person stands there.
REGIONS = {
    ("entrance_hall", "captain"): {
        # Boxes are sized off the proportions that read correctly in the group
        # render: the figure ends up roughly 80% of the box height, so height
        # sets the apparent distance. Host smallest (furthest, at the stair),
        # captain mid, Moody largest (nearest the camera).
        "box": (304, 272, 400, 736),
        "surround": (
            "the left-hand side of a grand entrance hall at night, with a tall panelled "
            "wooden door and a gilt-framed portrait on the pale green wall behind, a "
            "small console table carrying a lit lamp to one side, dark wood wainscoting, "
            "and a broad polished wooden floor below"
        ),
        "pose": (
            "He stands straight-backed and perfectly still on the open floor, shoulders "
            "level, hands at his sides, turned very slightly towards the centre of the "
            "hall on his right."
        ),
    },
    ("entrance_hall", "host"): {
        "box": (768, 288, 384, 640),
        "surround": (
            "the centre of a grand entrance hall at night, looking towards the foot of a "
            "wide wooden staircase with a deep red stair runner climbing behind, carved "
            "newel posts to either side, and the polished wooden floor in front of the "
            "bottom step"
        ),
        "pose": (
            "She stands on the floor just in front of the bottom step, facing the viewer "
            "squarely, her hands lightly clasped in front of her, poised and composed."
        ),
    },
    ("entrance_hall", "broken"): {
        "box": (1200, 256, 480, 784),
        "surround": (
            "the right-hand side of a grand entrance hall at night, with a tall carved "
            "wooden doorway and a gilt-framed painting on the pale green wall behind, "
            "dark wood wainscoting, a lit wall sconce casting warm light, and the broad "
            "polished wooden floor below"
        ),
        "pose": (
            "He stands on the open floor turned three-quarters towards the viewer, his "
            "masked face clearly visible and both shoulders in view, watching the room "
            "from its edge with his hands at his sides."
        ),
    },
    # Seated diners. Everything above is a standing figure on open floor; a person
    # at the dinner table is a different problem -- the table cuts them off at the
    # waist -- so these entries carry "template": "seated", which swaps in the
    # <variant>_seated wording below. The boxes sit on the second chair in from the
    # near end on each side, wide enough to hold the chair, the sitter and the strip
    # of tablecloth in front of them.
    ("dining_room", "lad"): {
        # The box is context for the model; "band" is the envelope the figure is
        # actually painted into, and the model fills it edge to edge -- so the band
        # must be the size and shape of the whole seated person, with headroom.
        # Measured off the chair rather than guessed: the chair is 1.20 m from floor
        # (y=890) to the top of its back (y=528), so 302 px to the metre at this
        # depth. A seated adult is then crown y=483, head 69 px, shoulder y=558,
        # seat y=754. A band of y 464-800 holds all of that with room to spare.
        # Getting this wrong does not shrink the figure, it CLIPS it -- an earlier
        # band of y 499-707 sliced the crown flat and cut the body off at the ribs.
        "box": (384, 432, 352, 400),
        "band": {"width": 0.62, "top": 0.08, "bottom": 0.92},
        "surround": (
            "a row of tall carved high-backed dining chairs upholstered in faded rose "
            "damask, ranged down the left-hand side of a long table laid for dinner in a "
            "1920s Scottish manor at night and seen at a sharp angle from the head of the "
            "table, the white linen tablecloth and its laid places running away to the "
            "right, a dark wooden dresser and pale panelled wall behind them, all of it "
            "in warm candlelight and deep shadow"
        ),
        "pose": (
            "He is sitting well in to the table in one of those chairs, seen from the "
            "side: his shoulders run away from the viewer down the length of the table, "
            "his body is turned across the table to his right, and his face is in "
            "three-quarter profile with the cheek and jaw outlined against the dark room "
            "behind. His forearms rest on the cloth beside his place setting."
        ),
        "template": "seated",
    },
    ("dining_room", "host"): {
        "box": (1104, 432, 352, 400),
        "band": {"width": 0.62, "top": 0.08, "bottom": 0.92},
        "surround": (
            "a row of tall carved high-backed dining chairs upholstered in faded rose "
            "damask, ranged down the right-hand side of a long table laid for dinner in a "
            "1920s Scottish manor at night and seen at a sharp angle from the head of the "
            "table, the white linen tablecloth and its laid places running away to the "
            "left, a dark wooden sideboard and a tall curtained window behind them, all of "
            "it in warm candlelight and deep shadow"
        ),
        "pose": (
            "She is sitting well in to the table in one of those chairs, seen from the "
            "side: her shoulders run away from the viewer down the length of the table, "
            "her body is turned across the table to her left, and her face is in "
            "three-quarter profile with the cheek and jaw outlined against the dark room "
            "behind. She sits upright and poised with her hands resting on the cloth."
        ),
        "template": "seated",
    },
}

# {style_lead} {surround} {desc} {pose} -- one person, one reference, no ordinals
# needed beyond "the second reference image".
REGION_PROMPTS = {
    "night": (
        "{style_lead}. "
        "The first reference image shows {surround}. Repaint that exact view, keeping "
        "the walls, the woodwork, the furniture, the ornaments and the warm night "
        "lighting precisely as they are, and place one single person standing on the "
        "floor in the middle of it: {desc}. {pose} "
        "\n\n"
        "Only one person is in the picture and nobody else, and nothing else in the "
        "view changes at all: do not add, move or remove any door, window, lamp, "
        "chandelier, wall sconce, painting or piece of furniture, and do not alter the "
        "walls, the woodwork or the floor. The one and only difference from the "
        "reference image is the person now standing there. "
        "The figure stands in the middle of the picture, squarely on the floor, shown "
        "full length from the top of the head down to the shoes and filling most of "
        "the height of the picture, with only a little clear space above the head and "
        "below the feet. Warm "
        "amber light from the chandelier and the wall sconces falls on them from above "
        "and from the side, their far side dropping into soft shadow, with a soft dark "
        "contact shadow on the floor beneath their shoes and a faint blurred reflection "
        "in the polished floorboards. Keep the face, the hair and every piece of "
        "clothing exactly as they are in the second reference image, and paint the "
        "figure in the same style as the room, as though they had always been part of "
        "the picture. No text, no watermark, no signature."
    ),
    "day": (
        "{style_lead}. "
        "The first reference image shows {surround}. Repaint that exact view, keeping "
        "the walls, the woodwork, the furniture, the ornaments and the daylight "
        "precisely as they are, and place one single person standing on the floor in "
        "the middle of it: {desc}. {pose} "
        "\n\n"
        "Only one person is in the picture and nobody else, and nothing else in the "
        "view changes at all: do not add, move or remove any door, window, lamp, "
        "chandelier, wall sconce, painting or piece of furniture, and do not alter the "
        "walls, the woodwork or the floor. The one and only difference from the "
        "reference image is the person now standing there. "
        "The figure stands in the middle of the picture, squarely on the floor, shown "
        "full length from the top of the head down to the shoes and filling most of "
        "the height of the picture, with only a little clear space above the head and "
        "below the feet. Soft "
        "grey daylight falls on them from the side, their far side dropping into gentle "
        "shadow, with a soft contact shadow on the floor beneath their shoes. Keep the "
        "face, the hair and every piece of clothing exactly as they are in the second "
        "reference image, and paint the figure in the same style as the room, as though "
        "they had always been part of the picture. No text, no watermark, no signature."
    ),
    # A sitter is not a standing figure with the legs cropped off: the table hides
    # everything below the chest, the head sits no higher than the chair back, and
    # the light comes up off the candles on the cloth rather than down off the floor.
    # Both anti-cues below earn their place -- asked for a person "in" a dining room,
    # Flux stands them up beside the chair and paints their shoes through the table.
    # A sitter is not a standing figure with the legs cropped off. Three things have
    # to be said outright or Flux paints a standing-sized person hovering in front of
    # the chair row, facing the camera: that the chair back is behind their shoulders,
    # that the tablecloth crosses in front of their chest, and how big they are
    # relative to the empty chairs beside them.
    # A sitter is not a standing figure with the legs cropped off, and it is not a
    # bust either. Two failures to guard against, both seen on this room: Flux
    # paints a standing-sized person hovering in front of the chair row, and -- if
    # told the table hides the lower body -- it paints a torso that simply stops.
    # The table here is BESIDE the side-seats, not in front of them, so the whole
    # seated body down to the chair cushion has to be painted.
    "night_seated": (
        "{style_lead}. "
        "The first reference image shows {surround}. Repaint that exact view, keeping "
        "the walls, the woodwork, the chairs, the table, the tablecloth and everything "
        "laid on it, and the warm candlelight, precisely as they are, and seat one "
        "single person in one of the chairs: {desc}. {pose} "
        "\n\n"
        "They are one diner sitting at a long dinner table, seen from the head of that "
        "table -- not a portrait and not posed for the viewer. Paint the whole seated "
        "body, not a bust: they are sitting right back in the chair with their weight "
        "on the seat, their hips and the tops of their thighs on the cushion, their "
        "knees going in underneath the table and their lower legs hidden behind the "
        "hanging tablecloth. The carved back of the chair rises behind their shoulders "
        "and the arm nearest the viewer comes forward so the hand rests on the cloth. "
        "The body is continuous and complete from the head down to the seat of the "
        "chair, with no part of it cut off, faded out or left unpainted. "
        "\n\n"
        "Size them against the chair they are sitting in: the top of their head rises "
        "only a little above the carved crest of that chair back, their shoulders are "
        "level with the middle of the chair back, and their head is about a fifth as "
        "tall as the chair is from the floor to the top of its back. They are sitting "
        "some way down a long table, so they are a small figure in the picture. Their "
        "whole head is inside the picture with clear space above the hair. "
        "\n\n"
        "Only one person is in the picture and nobody else, and nothing else in the "
        "view changes at all: do not add, move or remove any chair, plate, glass, "
        "candlestick, painting or piece of furniture, and do not alter the walls, the "
        "woodwork, the table or the tablecloth. "
        "The candle flames on the table light the side of their face and the front of "
        "their clothes with a warm flickering glow, the side turned away from the "
        "table drops into deep shadow, and the chair casts its shadow behind them. "
        "Keep the face, the hair and the clothes exactly as they are in the second "
        "reference image, and paint the figure in the same style, the same soft "
        "brushwork and the same warm palette as the room, as though they had always "
        "been part of the picture. "
        "No standing figure, no floating person without a chair, no one facing the "
        "viewer, no flat-topped or cut-off head, no body that stops at the chest, no "
        "text, no watermark, no signature."
    ),
    "day_seated": (
        "{style_lead}. "
        "The first reference image shows {surround}. Repaint that exact view, keeping "
        "the walls, the woodwork, the chairs, the table, the tablecloth and everything "
        "laid on it, and the daylight, precisely as they are, and seat one single "
        "person in one of the chairs: {desc}. {pose} "
        "\n\n"
        "They are one diner sitting at a long dinner table, seen from the head of that "
        "table -- not a portrait and not posed for the viewer. Paint the whole seated "
        "body, not a bust: they are sitting right back in the chair with their weight "
        "on the seat, their hips and the tops of their thighs on the cushion, their "
        "knees going in underneath the table and their lower legs hidden behind the "
        "hanging tablecloth. The carved back of the chair rises behind their shoulders "
        "and the arm nearest the viewer comes forward so the hand rests on the cloth. "
        "The body is continuous and complete from the head down to the seat of the "
        "chair, with no part of it cut off, faded out or left unpainted. "
        "\n\n"
        "Size them against the chair they are sitting in: the top of their head rises "
        "only a little above the carved crest of that chair back, their shoulders are "
        "level with the middle of the chair back, and their head is about a fifth as "
        "tall as the chair is from the floor to the top of its back. They are sitting "
        "some way down a long table, so they are a small figure in the picture. Their "
        "whole head is inside the picture with clear space above the hair. "
        "\n\n"
        "Only one person is in the picture and nobody else, and nothing else in the "
        "view changes at all: do not add, move or remove any chair, plate, glass, "
        "candlestick, painting or piece of furniture, and do not alter the walls, the "
        "woodwork, the table or the tablecloth. "
        "Soft grey daylight from the window falls across them from the side, their far "
        "side dropping into gentle shadow. "
        "Keep the face, the hair and the clothes exactly as they are in the second "
        "reference image, and paint the figure in the same style, the same soft "
        "brushwork and the same warm palette as the room, as though they had always "
        "been part of the picture. "
        "No standing figure, no floating person without a chair, no one facing the "
        "viewer, no flat-topped or cut-off head, no body that stops at the chest, no "
        "text, no watermark, no signature."
    ),
}
