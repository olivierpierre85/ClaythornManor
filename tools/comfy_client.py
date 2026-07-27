"""
Shared HTTP plumbing for the local ComfyUI server (native API at
http://127.0.0.1:8188).

These helpers were originally copy-pasted into tools/character_comfy.py and
tools/location_comfy.py. They are lifted here verbatim so a third tool
(tools/scene_comfy.py) does not add a third copy. The two older tools are left
untouched on purpose -- they are proven, and migrating them is optional tidying.

Typical use:

    from comfy_client import upload_image, queue_prompt, wait_for_images, \
        download_image, next_available_path

    ref_name = upload_image("Images/.../captain.png", SERVER)
    prompt_id = queue_prompt(graph, SERVER)
    images = wait_for_images(prompt_id, SERVER, timeout=900)
    download_image(images[0], out_path, SERVER)
"""
import json
import time
import urllib.parse
from pathlib import Path

import requests

SERVER = "http://127.0.0.1:8188"


def upload_image(path, server=SERVER):
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


def queue_prompt(graph, server=SERVER):
    r = requests.post(f"{server}/prompt", json={"prompt": graph}, timeout=60)
    if r.status_code != 200:
        raise RuntimeError(f"/prompt HTTP {r.status_code}: {r.text[:500]}")
    j = r.json()
    if j.get("node_errors"):
        raise RuntimeError(f"node_errors: {json.dumps(j['node_errors'])[:500]}")
    return j["prompt_id"]


def wait_for_images(prompt_id, server=SERVER, timeout=900):
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


def download_image(img, out_path, server=SERVER):
    params = urllib.parse.urlencode(
        {
            "filename": img["filename"],
            "subfolder": img.get("subfolder", ""),
            "type": img.get("type", "output"),
        }
    )
    r = requests.get(f"{server}/view?{params}", timeout=120)
    r.raise_for_status()
    Path(out_path).write_bytes(r.content)


def next_available_path(out_dir, stem):
    """Return <stem>.png, or <stem>_1.png, _2.png ... if earlier ones exist."""
    out_dir = Path(out_dir)
    candidate = out_dir / f"{stem}.png"
    if not candidate.exists():
        return candidate
    n = 1
    while (out_dir / f"{stem}_{n}.png").exists():
        n += 1
    return out_dir / f"{stem}_{n}.png"
