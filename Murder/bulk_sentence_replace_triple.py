#!/usr/bin/env python3
import argparse, csv, sys, re
from pathlib import Path

TRIPLE_PATTERN = re.compile(r'("""|\'\'\')([\s\S]*?)\1', re.MULTILINE)

def load_pairs(tsv_path):
    pairs = []
    with open(tsv_path, "r", encoding="utf-8", newline="") as f:
        for i, line in enumerate(f, 1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2:
                print(f"[warn] line {i} has fewer than 2 columns; skipping", file=sys.stderr)
                continue
            old, new = parts[0].strip(), parts[1].strip()
            if old and old != new:
                pairs.append((old, new))
    return pairs

def replace_in_block(block_text, pairs):
    """
    Replace exact full-line matches inside a triple-quoted block.
    - Match by trimmed content (ignoring leading/trailing spaces on that line).
    - Preserve: original indentation, original trailing spaces (if any), and the single original EOL.
    - Never adds extra blank lines or spaces.
    """
    if not pairs:
        return block_text, 0

    repl = dict(pairs)
    hits = 0
    out = []

    # iterate physical lines with their exact EOLs
    for raw in block_text.splitlines(keepends=True):
        # split EOL from the rest
        if raw.endswith(("\r\n", "\n", "\r")):
            if raw.endswith("\r\n"):
                eol = "\r\n"
                line_core = raw[:-2]
            else:
                eol = raw[-1]
                line_core = raw[:-1]
        else:
            eol = ""
            line_core = raw

        # split indent and trailing spaces (but keep both to rebuild byte-identical layout)
        i = 0
        while i < len(line_core) and line_core[i] in (" ", "\t"):
            i += 1
        indent = line_core[:i]
        rest = line_core[i:]

        # trailing spaces (before EOL)
        j = len(rest)
        while j > 0 and rest[j-1] in (" ", "\t"):
            j -= 1
        content = rest[:j]        # the actual text without indent or trailing spaces
        trail_ws = rest[j:]       # the original trailing spaces (if any)

        key = content.strip()
        if key in repl and key != "":
            hits += 1
            new_line = f"{indent}{repl[key]}{trail_ws}{eol}"
            out.append(new_line)
        else:
            out.append(raw)

    return "".join(out), hits



def process_file(path, pairs, dry_run=False, create_backup=True):
    text = path.read_text(encoding="utf-8")
    original = text
    total_hits = 0

    def _replacer(m):
        nonlocal total_hits
        quote, inner = m.group(1), m.group(2)
        new_inner, hits = replace_in_block(inner, pairs)
        total_hits += hits
        if hits:
            return f"{quote}{new_inner}{quote}"
        return m.group(0)

    new_text = TRIPLE_PATTERN.sub(_replacer, text)

    if total_hits and not dry_run:
        if create_backup:
            bak = path.with_suffix(path.suffix + ".bak")
            if not bak.exists():
                bak.write_text(original, encoding="utf-8")
        path.write_text(new_text, encoding="utf-8")

    return total_hits

def main():
    ap = argparse.ArgumentParser(
        description="Replace full sentences inside triple-quoted dialogue/narration blocks in .rpy files using a TSV mapping (from<TAB>to)."
    )
    ap.add_argument("project_root", help="Path to your Ren'Py project folder")
    ap.add_argument("mapping_tsv", help="Path to replacements.tsv (from<TAB>to)")
    ap.add_argument("--dry-run", action="store_true", help="Report changes without writing files")
    ap.add_argument("--no-backup", action="store_true", help="Do not write .bak backup files")
    ap.add_argument("--ext", default=".rpy", help="File extension to scan (default: .rpy)")
    args = ap.parse_args()

    root = Path(args.project_root)
    if not root.is_dir():
        print(f"[error] project root not found: {root}", file=sys.stderr)
        sys.exit(1)

    pairs = load_pairs(args.mapping_tsv)
    if not pairs:
        print("[info] no replacement pairs loaded. nothing to do.")
        return

    files = sorted(root.rglob(f"*{args.ext}"))
    if not files:
        print(f"[info] no {args.ext} files found under {root}")
        return

    grand_total = 0
    for p in files:
        hits = process_file(p, pairs, dry_run=args.dry_run, create_backup=not args.no_backup)
        if hits:
            grand_total += hits
            print(f"[ok] {p}: {hits} line(s) replaced")
    if grand_total == 0:
        print("[info] no matches found.")
    else:
        print(f"[done] total lines replaced: {grand_total}")

if __name__ == "__main__":
    main()
