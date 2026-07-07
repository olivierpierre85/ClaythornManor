"""
Flux 2 Dev prompt templates for tools/location_comfy.py.

These are DEV-TUNED rewrites of the Klein location templates -- the Klein originals
stay untouched in tools/generate_location_images.py, tools/toggle_location_lighting.py
and Murder/game/images/locations/_locations.md.

Why a separate wording: Flux 2 Dev (Mistral text encoder, non-distilled) follows
prompts far more literally than the distilled Klein. Vague phrases fail concretely:
"touches of colorful objects" rendered an actual bag of baubles, and "at night" with
no named light source rendered a near-black room. So every template names its light
sources, materials and props explicitly, and the anti-cues ("No people, no text...")
are baked into the positive text because the BasicGuider graph has no negative prompt.

ROOM_DETAILS adds concrete per-room props on top of the shared _locations.md
description (which stays Klein-compatible). Grow it room by room during rollout.
"""

# Keyed by (section, variant) -- sections come from the _locations.md headings.
PROMPT_TEMPLATES = {
    ("interior", "night"): (
        "A high-quality semi-realistic digital painting of a 1920s Scottish manor "
        "{description}, at night. The room is warmly lit by glowing brass light "
        "fixtures and candle wall sconces, strong cosy amber light filling the room, "
        "warm pools of golden light on the polished surfaces, deep soft shadows only "
        "in the far corners, dark unlit windows. Rich wood panelling, gilt-framed oil "
        "paintings, a few colourful accents such as porcelain, book spines and fresh "
        "flowers. Painted textures with soft visible brushwork, mysterious atmosphere, "
        "wide establishing shot, deep perspective, empty room. "
        "No people, no text, no watermark."
    ),
    ("interior", "day"): (
        "A high-quality semi-realistic digital painting of a 1920s Scottish manor "
        "{description}, by day. Soft muted overcast daylight filtering through tall "
        "windows, subdued grey-silver light, gentle soft shadows, no direct sunbeams, "
        "quiet and slightly dim. Rich wood panelling, gilt-framed oil paintings, a few "
        "colourful accents such as porcelain, book spines and fresh flowers. Painted "
        "textures with soft visible brushwork, quiet mysterious atmosphere, wide "
        "establishing shot, deep perspective, empty room. "
        "No people, no text, no watermark."
    ),
    ("attic", "night"): (
        "A high-quality semi-realistic digital painting of a 1920s Scottish manor "
        "{description}, at night. Dimly lit by the warm flickering glow of a single "
        "oil lamp, faint cold moonlight from a small dormer window, dust in the air, "
        "bare wooden floorboards, muted faded colours, deep soft shadows swallowing "
        "the corners. Painted textures with soft visible brushwork, eerie mysterious "
        "atmosphere, wide establishing shot, deep perspective, empty room. "
        "No people, no text, no watermark."
    ),
    ("attic", "day"): (
        "A high-quality semi-realistic digital painting of a 1920s Scottish manor "
        "{description}, by day. Weak grey daylight from a small dormer window, dust "
        "in the air, bare wooden floorboards, muted faded colours, gentle soft "
        "shadows, quiet and dim. Painted textures with soft visible brushwork, eerie "
        "mysterious atmosphere, wide establishing shot, deep perspective, empty room. "
        "No people, no text, no watermark."
    ),
    ("outdoor", "night"): (
        "A high-quality semi-realistic digital painting of a {description}, at night. "
        "Dark overcast night sky, cool blue moonlit ambient light, deep soft shadows, "
        "cold nocturnal atmosphere with a few warm lit windows or lamps as golden "
        "accents. Painted textures with soft visible brushwork, mysterious atmosphere, "
        "wide establishing shot, rich textures. No text, no watermark."
    ),
    ("outdoor", "day"): (
        "A high-quality semi-realistic digital painting of a {description}, by day. "
        "Soft natural daylight under an overcast Scottish sky, muted greens and greys "
        "with a few warm colour accents, gentle soft shadows. Painted textures with "
        "soft visible brushwork, quiet mysterious atmosphere, wide establishing shot, "
        "rich textures. No text, no watermark."
    ),
}

# Extra concrete props appended to the _locations.md description, per room id.
# Only rooms that have been calibrated get an entry.
ROOM_DETAILS = {
    "entrance_hall": (
        "a red stair runner carpet on the central staircase, "
        "a black grand piano in the far corner"
    ),
}
