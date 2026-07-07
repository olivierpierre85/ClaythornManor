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
        "A warmly hand-painted background illustration for a classic animated film, "
        "showing a 1920s Scottish manor {description}, at night. Painterly "
        "matte-painting style, soft brush rendering with realistic proportions and "
        "perspective, gently simplified detail, soft painterly edges, warm saturated "
        "colours. The room is brightly and warmly lit by glowing brass light "
        "fittings and candle wall sconces, cosy amber light filling the whole room, "
        "warm golden reflections on the polished wooden floor, soft shadows in the "
        "far corners, dark unlit windows. Pale painted walls above warm wood "
        "wainscoting, gilt-framed paintings, colourful porcelain, book spines and "
        "fresh flowers. Mysterious yet inviting atmosphere, wide establishing shot, "
        "deep perspective, empty room. No people, no text, no watermark."
    ),
    ("interior", "day"): (
        "A warmly hand-painted background illustration for a classic animated film, "
        "showing a 1920s Scottish manor {description}, by day. Painterly "
        "matte-painting style, soft brush rendering with realistic proportions and "
        "perspective, gently simplified detail, soft painterly edges. Soft muted "
        "overcast daylight filtering through tall windows, subdued grey-silver "
        "light, gentle soft shadows, no direct sunbeams, quiet and slightly dim. "
        "Pale painted walls above warm wood wainscoting, gilt-framed paintings, "
        "colourful porcelain, book spines and fresh flowers. Quiet mysterious "
        "atmosphere, wide establishing shot, deep perspective, empty room. "
        "No people, no text, no watermark."
    ),
    ("attic", "night"): (
        "A hand-painted background illustration for a classic animated film, "
        "showing a 1920s Scottish manor {description}, at night. Painterly "
        "matte-painting style, soft brush rendering with realistic proportions and "
        "perspective, gently simplified detail, soft painterly edges. Dimly lit by "
        "the warm flickering glow of a single oil lamp, faint cold moonlight from a "
        "small dormer window, dust in the air, bare wooden floorboards, muted faded "
        "colours, deep soft shadows swallowing the corners. Eerie mysterious "
        "atmosphere, wide establishing shot, deep perspective, empty room. "
        "No people, no text, no watermark."
    ),
    ("attic", "day"): (
        "A hand-painted background illustration for a classic animated film, "
        "showing a 1920s Scottish manor {description}, by day. Painterly "
        "matte-painting style, soft brush rendering with realistic proportions and "
        "perspective, gently simplified detail, soft painterly edges. Weak grey "
        "daylight from a small dormer window, dust in the air, bare wooden "
        "floorboards, muted faded colours, gentle soft shadows, quiet and dim. "
        "Eerie mysterious atmosphere, wide establishing shot, deep perspective, "
        "empty room. No people, no text, no watermark."
    ),
    ("outdoor", "night"): (
        "A hand-painted background illustration for a classic animated film, "
        "showing a {description}, at night. Painterly matte-painting style, soft "
        "brush rendering with realistic proportions and perspective, gently "
        "simplified detail, soft painterly edges. Dark overcast night sky, cool "
        "blue moonlit ambient light, deep soft shadows, cold nocturnal atmosphere "
        "with a few warm lit windows or lamps as golden accents. Mysterious "
        "atmosphere, wide establishing shot, rich textures. No text, no watermark."
    ),
    ("outdoor", "day"): (
        "A warmly hand-painted background illustration for a classic animated film, "
        "showing a {description}, by day. Painterly matte-painting style, soft "
        "brush rendering with realistic proportions and perspective, gently "
        "simplified detail, soft painterly edges. Soft natural daylight under an "
        "overcast Scottish sky, muted greens and greys with a few warm colour "
        "accents, gentle soft shadows. Quiet mysterious atmosphere, wide "
        "establishing shot, rich textures. No text, no watermark."
    ),
}

# Extra concrete props appended to the _locations.md description, per room id.
# Only rooms that have been calibrated get an entry.
ROOM_DETAILS = {
    "entrance_hall": (
        "a red stair runner carpet on the central staircase, "
        "a black grand piano in the far corner"
    ),
    "library": (
        "walls lined with tall floor-to-ceiling bookshelves packed with "
        "leather-bound books, a leather reading armchair"
    ),
}
