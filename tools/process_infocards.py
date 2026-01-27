import os
from pathlib import Path
from PIL import Image

# Configuration
SOURCE_DIR = Path(r"c:\Projects\ClaythornManor\Images\info_cards")
DEST_DIR = Path(r"c:\Projects\ClaythornManor\Murder\game\images\info_cards")
BORDER_IMAGE_PATH = SOURCE_DIR / "main_border.png"
TARGET_SIZE = (75, 75)

def process_images():
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
        if file_path.is_file() and file_path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.webp']:
            # Skip the border image itself
            if file_path.name == BORDER_IMAGE_PATH.name:
                continue

            target_filename = file_path.stem + ".webp"
            target_bw_filename = file_path.stem + "_bw.webp"
            target_path = DEST_DIR / target_filename
            target_bw_path = DEST_DIR / target_bw_filename

            # Check if destination file already exists
            if target_path.exists():
                print(f"Skipping {file_path.name} (already exists)")
                continue

            try:
                # Load source image
                img = Image.open(file_path).convert("RGBA")

                # Resize image to fit inside border if needed
                # Assuming simple overlay for now. 
                # Better approach: Resize source to match border size, then composite
                if img.size != border_img.size:
                    img = img.resize(border_img.size, Image.Resampling.LANCZOS)
                
                # Composite: Image under border? or Image over border?
                # Usually frame is on top.
                # Create a base canvas (transparent)
                combined = Image.new("RGBA", border_img.size)
                combined.paste(img, (0, 0))
                combined.paste(border_img, (0, 0), mask=border_img)

                # Resize to target size
                resized_img = combined.resize(TARGET_SIZE, Image.Resampling.LANCZOS)

                # Save Color Version
                resized_img.save(target_path, "WEBP")
                print(f"Saved {target_filename}")

                # Create and Save BW Version
                # Convert to grayscale (L) then back to RGB/RGBA prevents color tinting issues in some viewers, 
                # but WebP supports grayscale. Sticking to simple 'L' conversion.
                bw_img = resized_img.convert("L")
                bw_img.save(target_bw_path, "WEBP")
                print(f"Saved {target_bw_filename}")

            except Exception as e:
                print(f"Failed to process {file_path.name}: {e}")

if __name__ == "__main__":
    process_images()
