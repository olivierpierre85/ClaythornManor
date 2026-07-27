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
}
