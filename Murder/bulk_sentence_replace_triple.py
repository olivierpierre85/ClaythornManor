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
            old, new = parts[0], parts[1]
            if old and old != new:
                pairs.append((old, new))
    return pairs

def replace_in_block(block_text, pairs):
    """
    Replace exact full-line matches inside a triple-quoted block.
    - Match is done on the line *content* stripped of leading/trailing whitespace.
    - Indentation and original EOLs are preserved.
    """
    if not pairs:
        return block_text, 0

    # Build a dict for O(1) lookups
    repl = dict(pairs)
    hits = 0
    out_lines = []

    # Preserve exact line endings
    lines = block_text.splitlines(keepends=True)
    for raw in lines:
        # Keep indentation
        m = re.match(r"^(\s*)(.*?)(\s*)$", raw[:-1] if raw.endswith(("\n", "\r")) else raw)
        if m:
            indent, core, trail_ws = m.groups()
            key = core.strip()
            if key in repl:
                hits += 1
                new_core = repl[key]
                # Rebuild with original indent/trailing whitespace and EOL
                rebuilt = f"{indent}{new_core}{trail_ws}"
                if raw.endswith(("\r\n", "\n", "\r")):
                    # Keep the same EOL sequence
                    eol = "\r\n" if raw.endswith("\r\n") else ("\n" if raw.endswith("\n") else "\r")
                    rebuilt += eol
                out_lines.append(rebuilt)
                continue
        out_lines.append(raw)
    return ("".join(out_lines), hits)

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
