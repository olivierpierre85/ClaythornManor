"""
Extract image descriptions from docs/assets/thread_images.md
and write them to docs/assets/thread_image_prompts.txt.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).parent.parent
MD_FILE = ROOT / "docs/assets/thread_images.md"
OUT_FILE = ROOT / "docs/assets/thread_image_prompts.txt"


def parse_table_rows(table_lines):
    """Return (thread_key, image_description) pairs from a markdown table block."""
    rows = []
    for line in table_lines:
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) < 3:
            continue
        key_cell = parts[0]
        desc_cell = parts[2]
        # Skip header and separator rows
        if key_cell.lower() in ("thread key", "thread_key") or key_cell.startswith("-"):
            continue
        thread_key = key_cell.strip("`").strip()
        image_desc = desc_cell.strip()
        if thread_key and image_desc:
            rows.append((thread_key, image_desc))
    return rows


def main():
    text = MD_FILE.read_text(encoding="utf-8")
    lines = text.splitlines()

    descriptions = []
    i = 0

    while i < len(lines):
        line = lines[i]

        if line.strip().startswith("|"):
            table_lines = []
            j = i
            while j < len(lines) and lines[j].strip().startswith("|"):
                table_lines.append(lines[j])
                j += 1
            rows = parse_table_rows(table_lines)
            for _, image_desc in rows:
                descriptions.append(image_desc)
            i = j
            continue

        i += 1

    OUT_FILE.write_text("\n".join(descriptions), encoding="utf-8")
    print(f"Done — {len(descriptions)} image descriptions written to {OUT_FILE}")


if __name__ == "__main__":
    main()
