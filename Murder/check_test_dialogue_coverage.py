#!/usr/bin/env python3
"""Check that every dialogue line in dialogue.tab is covered by at least one test text file.

dialogue.tab format (tab-separated, header on line 1):
    Identifier  Character  Dialogue  Filename  Line Number  Ren'Py Script

Test .txt format (one of):
    Chapter: ...           (header, ignored)
    Character: ...         (header, ignored)
    Menu Choice: ...       (UI marker, ignored)
    Map Choice: ...        (UI marker, ignored)
    Speaker Name: dialogue
    bare narration line

Usage:
    python check_test_dialogue_coverage.py                     # all characters, all tests
    python check_test_dialogue_coverage.py --character captain # one character only
    python check_test_dialogue_coverage.py --limit 5           # cap output per source file

Character mode
--------------
  Dialogue source : game/scripts/<character>/ only (excludes _common/)
  Test pool       : game/tests/<character>/

  _common/ labels are excluded in character mode because they are shared across multiple
  characters and are best reviewed at the suite level. Run without --character to include
  them.
"""

import argparse
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIALOGUE_TAB = ROOT / "dialogue.tab"
TESTS_ROOT = ROOT / "game" / "tests"

SKIP_PREFIXES = ("Chapter:", "Character:", "Menu Choice:", "Map Choice:")

CHARACTERS = ("broken", "captain", "doctor", "drunk", "host", "lad", "nurse", "psychic")

# Files in a character's own folder that contain dialogue spoken *to* other characters
# (i.e. NPC responses when another character is playing). These must be excluded from
# the character-specific coverage check because they never appear in that character's tests.
EXCLUDED_OWN_SUFFIXES = ("_generic_choices.rpy", "_generic_other_guests.rpy")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def load_dialogue_tab(path: Path, character: str | None):
    """Yield (identifier, filename, dialogue) tuples, optionally filtered by character.

    In character mode, only dialogue under game/scripts/<character>/ is included.
    _common/ and other characters' scripts are skipped.
    """
    with path.open(encoding="utf-8") as f:
        f.readline()  # header
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            ident, _speaker, dialogue, filename = parts[0], parts[1], parts[2], parts[3]
            if not dialogue.strip():
                continue
            if character:
                norm = filename.replace("\\", "/")
                if f"/scripts/{character}/" not in norm:
                    continue
                # Exclude NPC files — dialogue accessed when other characters are playing
                if any(norm.endswith(suffix) for suffix in EXCLUDED_OWN_SUFFIXES):
                    continue
            yield ident, filename, dialogue


def collect_test_lines(tests_root: Path, character: str | None) -> set[str]:
    """Return set of normalised dialogue strings found in the relevant test .txt files."""
    search_root = tests_root / character if character else tests_root
    if not search_root.exists():
        return set()

    lines: set[str] = set()
    for txt in search_root.rglob("*.txt"):
        for raw in txt.read_text(encoding="utf-8").splitlines():
            stripped = raw.strip()
            if not stripped or stripped.startswith(SKIP_PREFIXES):
                continue
            lines.add(normalize(stripped))
            # Also store the form with any "Speaker: " prefix removed.
            if ": " in stripped:
                _speaker, _, content = stripped.partition(": ")
                lines.add(normalize(content))
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--character", choices=CHARACTERS, help="Restrict to one character (+ shared _common/ scripts)")
    parser.add_argument("--dialogue", default=str(DIALOGUE_TAB), help="Path to dialogue.tab")
    parser.add_argument("--tests", default=str(TESTS_ROOT), help="Path to tests root")
    parser.add_argument("--limit", type=int, default=0, help="Print at most N missing entries per source file (0 = all)")
    args = parser.parse_args()

    dialogue_path = Path(args.dialogue)
    tests_path = Path(args.tests)

    if not dialogue_path.exists():
        print(f"ERROR: dialogue file not found: {dialogue_path}", file=sys.stderr)
        return 2
    if not tests_path.exists():
        print(f"ERROR: tests root not found: {tests_path}", file=sys.stderr)
        return 2

    character = args.character
    test_lines = collect_test_lines(tests_path, character)

    total = 0
    missing_by_file: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for ident, filename, dialogue in load_dialogue_tab(dialogue_path, character):
        total += 1
        if normalize(dialogue) not in test_lines:
            missing_by_file[filename].append((ident, dialogue))

    scope = f"character={character}" if character else "all characters"
    missing_total = sum(len(v) for v in missing_by_file.values())
    covered = total - missing_total

    output_lines: list[str] = []

    def out(line: str = "") -> None:
        print(line)
        output_lines.append(line)

    out(f"Generated:                {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    out(f"Scope:                    {scope}")
    out(f"Dialogue entries scanned: {total}")
    out(f"Test lines collected:     {len(test_lines)}")
    out(f"Covered:                  {covered}")
    out(f"Missing:                  {missing_total}")
    out()

    if missing_by_file:
        for filename in sorted(missing_by_file):
            entries = missing_by_file[filename]
            out(f"  {filename}  ({len(entries)} missing)")
            shown = entries if args.limit <= 0 else entries[: args.limit]
            for ident, text in shown:
                preview = text if len(text) <= 110 else text[:107] + "..."
                out(f"    [{ident}] {preview}")
            if args.limit > 0 and len(entries) > args.limit:
                out(f"    ... {len(entries) - args.limit} more")
            out()
        exit_code = 1
    else:
        out("All dialogue lines covered.")
        exit_code = 0

    # Save the report alongside the tests it describes.
    if character:
        report_path = tests_path / character / "dialogue_coverage.txt"
    else:
        report_path = tests_path / "dialogue_coverage.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(output_lines) + "\n", encoding="utf-8")
    print(f"Report saved to: {report_path}")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
