"""
Extract image descriptions from docs/assets/thread_images.md
and write them to docs/assets/thread_image_prompts.txt.

Rows whose thread key appears as a checked task list item ( - [x] key )
are skipped. Click the checkboxes in VS Code preview to mark images as done.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).parent.parent
MD_FILE = ROOT / "docs/assets/thread_images.md"
OUT_FILE = ROOT / "docs/assets/thread_image_prompts.txt"

TASK_RE = re.compile(r"^-\s+\[( |x)\]\s+(\S+)", re.IGNORECASE)


def collect_done_keys(lines):
    """Return the set of thread keys marked [x] in task lists."""
    done = set()
    for line in lines:
        m = TASK_RE.match(line.strip())
        if m and m.group(1).lower() == "x":
            done.add(m.group(2).strip())
    return done


def parse_table_rows(table_lines, done_keys):
    """Return image descriptions from a table, skipping keys in done_keys."""
    descriptions = []
    for line in table_lines:
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) < 3:
            continue
        key_cell = parts[0]
        if key_cell.lower() in ("thread key", "thread_key") or key_cell.startswith("-"):
            continue
        thread_key = key_cell.strip("`").strip()
        image_desc = parts[2].strip()
        if thread_key and image_desc and thread_key not in done_keys:
            descriptions.append(image_desc)
    return descriptions


def main():
    text = MD_FILE.read_text(encoding="utf-8")
    lines = text.splitlines()

    done_keys = collect_done_keys(lines)

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
            descriptions.extend(parse_table_rows(table_lines, done_keys))
            i = j
            continue
        i += 1

    OUT_FILE.write_text("\n".join(descriptions), encoding="utf-8")
    skipped = len(done_keys)
    print(f"Done — {len(descriptions)} descriptions written, {skipped} skipped (already generated)")


if __name__ == "__main__":
    main()
