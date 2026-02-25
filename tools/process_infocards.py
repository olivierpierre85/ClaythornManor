import os
import argparse
from pathlib import Path
from PIL import Image

# Configuration
SOURCE_DIR = Path(r"c:\Projects\ClaythornManor\Images\info_cards")
DEST_DIR = Path(r"c:\Projects\ClaythornManor\Murder\game\images\info_cards")
BORDER_IMAGE_PATH = SOURCE_DIR / "addons" / "main_border.png"
TARGET_SIZE = (75, 75)

# Addon configurations for specific images
# Format: "filename.ext": [("suffix", "addon_filename.ext")]
WITH_ADDONS = {
    "cutlery.png": [
        ("1", "letter_i_art_deco.png"),
        ("2", "number_2_art_deco.png")
    ]
}

def process_images(global_addon=None):
    # Ensure destination directory exists
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    if not BORDER_IMAGE_PATH.exists():
        print(f"Error: Border image not found at {BORDER_IMAGE_PATH}")
        return

    try:
        border_img = Image.open(BORDER_IMAGE_PATH).convert("RGBA")
    except Exception as e:
        print(f"Error loading border image: {e}")
        return

    print(f"Processing images from {SOURCE_DIR}...")

    # Iterate through all files in source directory
    for file_path in SOURCE_DIR.iterdir():
        if file_path.is_dir():
            print(f"Skipping subfolder: {file_path.name}")
            continue

        if file_path.is_file() and file_path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.webp']:
            # Skip the border image itself
            if file_path.name == BORDER_IMAGE_PATH.name:
                continue
                
            # Determine processing variants (base + any addons)
            variants = [] # (suffix, addon_filename)
            
            if global_addon:
                # Decide on suffix dynamically
                if global_addon == "letter_i_art_deco.png":
                    suffix = "1"
                elif global_addon.startswith("number_"):
                    suffix = global_addon.split("_")[1]
                else:
                    suffix = Path(global_addon).stem
                variants.append((suffix, global_addon))
            else:
                variants.append((None, None))
                if file_path.name in WITH_ADDONS:
                    variants.extend(WITH_ADDONS[file_path.name])

            try:
                # Load source image
                base_img = Image.open(file_path).convert("RGBA")

                # Resize image to fit inside border if needed
                if base_img.size != border_img.size:
                    base_img = base_img.resize(border_img.size, Image.Resampling.LANCZOS)
                
                for suffix, addon_filename in variants:
                    target_name = f"{file_path.stem}_{suffix}" if suffix else file_path.stem
                    target_filename = f"{target_name}.webp"
                    target_bw_filename = f"{target_name}_bw.webp"
                    target_path = DEST_DIR / target_filename
                    target_bw_path = DEST_DIR / target_bw_filename

                    # Check if destination file already exists
                    if target_path.exists():
                        print(f"Skipping {target_filename} (already exists)")
                        continue

                    # Create a base canvas (transparent)
                    combined = Image.new("RGBA", border_img.size)
                    combined.paste(base_img, (0, 0))
                    
                    # If there's an addon, load and paste it
                    if addon_filename:
                        addon_path = SOURCE_DIR / "addons" / addon_filename
                        if addon_path.exists():
                            addon_img = Image.open(addon_path).convert("RGBA")
                            if addon_img.size != border_img.size:
                                addon_img = addon_img.resize(border_img.size, Image.Resampling.LANCZOS)
                            combined.paste(addon_img, (0, 0), mask=addon_img)
                        else:
                            print(f"Warning: Addon {addon_filename} not found.")

                    # Paste border on top
                    combined.paste(border_img, (0, 0), mask=border_img)

                    # Resize to target size
                    resized_img = combined.resize(TARGET_SIZE, Image.Resampling.LANCZOS)

                    # Save Color Version
                    resized_img.save(target_path, "WEBP")
                    print(f"Saved {target_filename}")

                    # Create and Save BW Version
                    bw_img = resized_img.convert("L")
                    bw_img.save(target_bw_path, "WEBP")
                    print(f"Saved {target_bw_filename}")

            except Exception as e:
                print(f"Failed to process {file_path.name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process info cards.")
    parser.add_argument("--addon", type=str, help="Global addon file to apply to all images")
    args = parser.parse_args()
    process_images(global_addon=args.addon)
