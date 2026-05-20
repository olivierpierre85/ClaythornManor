import base64, requests, os

URL = "http://127.0.0.1:7860"
D = r"Images/characters_original_and_archive/Models for flux/lad split"

def b64(p):
    with open(p, "rb") as f:
        return base64.b64encode(f.read()).decode()

refs = [b64(os.path.join(D, n)) for n in
        ("lad_neutral.png", "lad_smiling.png", "lad_shocked.png", "lad_profile.png")]
init = b64(os.path.join(D, "lad_neutral.png"))

payload = {
    "prompt": "A high-quality stylised digital painting of a young blond man with blue eyes, "
              "neutral calm expression, front view head and shoulders portrait, 1920s period collar shirt. "
              "Painterly illustration with visible brush strokes, smooth idealised skin, soft even neutral lighting, "
              "plain neutral background, smooth airbrushed shading, slightly stylised features, "
              "polished character art, matte illustration.",
    "negative_prompt": "photograph, photorealistic, photo, realistic skin pores, freckles, blemishes, skin texture, "
                       "dramatic shadows, coloured lighting, frame, border, text, watermark, deformed",
    "init_images": [init],
    "denoising_strength": 0.82,
    "width": 1008, "height": 1043,
    "steps": 28, "cfg_scale": 1.0, "distilled_cfg_scale": 3.0,
    "sampler_name": "Euler", "scheduler": "simple", "seed": 1924,
    "send_images": True, "save_images": False,
    "alwayson_scripts": {
        "ImageStitch Integrated": {"args": [True, refs, 1024]}
    },
}

r = requests.post(f"{URL}/sdapi/v1/img2img", json=payload, timeout=600)
if r.status_code != 200:
    print("STATUS", r.status_code); print(r.text[:1500]); raise SystemExit(1)
out = os.path.join(D, "lad_neutral_styled.png")
with open(out, "wb") as f:
    f.write(base64.b64decode(r.json()["images"][0]))
print("saved", out)
