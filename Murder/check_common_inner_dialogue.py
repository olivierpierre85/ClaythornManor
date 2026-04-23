#!/usr/bin/env python3
# Find inner monologue blocks in _common/ that are not gated by current_character.
#
# Labels under game/scripts/_common/ are called by multiple characters, so any
# inner-voice narration (triple-quoted block with no speaker prefix) must live
# inside an `if current_character.text_id == "..."` chain - otherwise every
# character would think the same thoughts.
#
# Detection model:
# - A dialogue opener is `speaker <triple-quote>` on its own line.
# - An inner monologue opener is a triple-quote on its own line (no prefix).
# - For each monologue opener we walk the stack of enclosing if/elif/else
#   chains (by indentation). If any clause in an enclosing chain mentions
#   `current_character`, the block is considered character-gated and is fine.
# - Otherwise the block is reported with file:line and the first line of text.
#
# Usage:
#     python check_common_inner_dialogue.py
#     python check_common_inner_dialogue.py --root path/to/Murder

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT_DEFAULT = Path(__file__).resolve().parent
COMMON_SUBDIR = Path("game") / "scripts" / "_common"

# A line that ends with `"""` is either:
#   - TRIPLE_ONLY: `"""` alone (monologue opener, or closing of any block)
#   - TRIPLE_DIALOGUE: something + `"""` (dialogue opener, e.g. `psychic -angry """`)
TRIPLE_LINE = re.compile(r'^(?P<prefix>\s*\S.*?)?\s*"""\s*$')
TRIPLE_ONLY = re.compile(r'^\s*"""\s*$')
IF_HEADER = re.compile(r'^\s*(if|elif|else)\b')
CHAR_GATE = re.compile(r'\bcurrent_character\b')
LABEL_HEADER = re.compile(r'^\s*label\s+([A-Za-z_][A-Za-z0-9_]*)\s*:')


def indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(' '))


def is_blank_or_comment(line: str) -> bool:
    s = line.lstrip()
    return not s or s.startswith('#')


def find_common_files(root: Path) -> list[Path]:
    common = root / COMMON_SUBDIR
    if not common.exists():
        raise SystemExit(f"_common/ folder not found under {root}")
    return sorted(common.rglob("*.rpy"))


def scan_file(path: Path) -> list[dict]:
    # Returns a list of findings {line, label, preview} for the given .rpy file.
    lines = path.read_text(encoding='utf-8').splitlines()
    findings: list[dict] = []

    # Stack of enclosing if/elif/else chains.
    # Each entry: {'header_indent': int, 'char_gated': bool}
    chains: list[dict] = []

    in_triple = False          # inside any triple-quoted block
    current_label = "<file>"

    i = 0
    while i < len(lines):
        line = lines[i]

        if in_triple:
            if TRIPLE_ONLY.match(line):
                in_triple = False
            i += 1
            continue

        if is_blank_or_comment(line):
            i += 1
            continue

        cur_indent = indent_of(line)

        # Pop chains that this line has exited.
        # Keep a chain if the current line is elif/else at the same indent
        # as the chain header — it continues the chain.
        while chains and cur_indent <= chains[-1]['header_indent']:
            top = chains[-1]
            if cur_indent == top['header_indent']:
                m = IF_HEADER.match(line)
                if m and m.group(1) in ('elif', 'else'):
                    if CHAR_GATE.search(line):
                        top['char_gated'] = True
                    break
            chains.pop()

        # Track current label for nicer reporting.
        m_label = LABEL_HEADER.match(line)
        if m_label:
            current_label = m_label.group(1)
            i += 1
            continue

        # Inner monologue opener: `"""` alone on the line.
        if TRIPLE_ONLY.match(line):
            gated = any(c['char_gated'] for c in chains)
            if not gated:
                preview = _first_text_line(lines, i + 1)
                findings.append({
                    'line': i + 1,
                    'label': current_label,
                    'preview': preview,
                })
            in_triple = True
            i += 1
            continue

        # Dialogue opener: anything + `"""` at end of line.
        if TRIPLE_LINE.match(line):
            in_triple = True
            i += 1
            continue

        # New if-chain opener.
        m_if = IF_HEADER.match(line)
        if m_if and m_if.group(1) == 'if':
            chains.append({
                'header_indent': cur_indent,
                'char_gated': bool(CHAR_GATE.search(line)),
            })

        i += 1

    return findings


def _first_text_line(lines: list[str], start: int) -> str:
    for j in range(start, min(start + 20, len(lines))):
        s = lines[j].strip()
        if s and s != '"""' and not s.startswith('#'):
            return s[:120]
    return ""


def format_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root)).replace('\\', '/')
    except ValueError:
        return str(path)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Find inner monologue in _common/ not gated by current_character."
    )
    ap.add_argument('--root', type=Path, default=ROOT_DEFAULT,
                    help="Murder/ folder (default: script's directory)")
    args = ap.parse_args()

    files = find_common_files(args.root)
    total = 0
    for path in files:
        findings = scan_file(path)
        if not findings:
            continue
        rel = format_path(path, args.root)
        print(f"\n{rel}  ({len(findings)} unfiltered)")
        for f in findings:
            total += 1
            preview = f['preview'] or '(empty)'
            print(f"  line {f['line']:>4}  [{f['label']}]  {preview}")

    print()
    if total == 0:
        print("OK - no unfiltered inner monologue found in _common/.")
        return 0
    print(f"Found {total} unfiltered inner monologue block(s) in _common/.")
    return 1


if __name__ == '__main__':
    sys.exit(main())
