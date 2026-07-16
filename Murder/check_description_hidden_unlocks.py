#!/usr/bin/env python3
"""
check_description_hidden_unlocks.py - static audit of description_hidden.unlock() sites.

Scans every .rpy under Murder/game/scripts/ for
    $ <owner>_details.description_hidden.unlock('<text_id>')
and reports, per described character and per hidden info, WHERE it can be
unlocked as a (playing_character, chapter) pair. That pair is what the
`unlock_chapters=` field of the CharacterInformation entries inside each
CharacterDescriptionHiddenList declaration (in <char>_config.rpy) must hold.

Resolution rules:
  - playing character = first folder under scripts/ (e.g. scripts/captain/...).
    For files in _common/ (shared between storylines) the unlock's enclosing
    label is resolved through the call graph: every character script that
    calls/jumps to it (directly or through another _common label) counts as a
    playing character, and `if current_character == <char>_details` /
    `if current_character.text_id == "<char>"` guards around the unlock
    narrow that set. Sites the graph cannot resolve stay flagged for manual
    attribution.
  - chapter = the chapter='...' argument of the change_time() call found in the
    unlock site's Day N/<phase>/ folder, falling back to a static folder-name
    map. For resolved _common sites the chapter comes from each CALLER's
    folder. Files at a character's folder root (generic choices / other
    guests / endings...) are reachable from several chapters -> flagged for
    manual attribution.

The script never modifies any file. It prints ready-to-paste
`unlock_chapters=[...]` suggestions built from the unambiguous sites only.

Usage:
    python Murder/check_description_hidden_unlocks.py [--character broken]
                                                      [--diff] [--verbose]

    --character  only report hidden infos OF this character (the config file
                 you are editing)
    --diff       compare the scanned pairs against the unlock_chapters already
                 declared in the config files (OK / MISSING / STALE / CHECK)
    --verbose    also print the phase-folder -> chapter resolution table
"""

import argparse
import ast
import os
import re
import sys
from collections import defaultdict

GAME_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "game")
SCRIPTS_DIR = os.path.join(GAME_DIR, "scripts")

# Engine / debug files whose unlock() calls are not story content
EXCLUDED_FILES = {"debug_choices.rpy", "test_utils.rpy", "test_plan_runner.rpy"}
SKIP_DIRS = {"tests", "saves", "cache", "gui"}

UNLOCK_RE = re.compile(
    r"\b(\w+)_details\s*\.\s*description_hidden\s*\.\s*unlock\(\s*['\"](\w+)['\"]"
)
CHANGE_TIME_RE = re.compile(r"change_time\([^)]*chapter\s*=\s*['\"](\w+)['\"]")
LABEL_DEF_RE = re.compile(r"^label\s+([A-Za-z_]\w*)", re.M)
CALL_JUMP_RE = re.compile(r"^\s*(?:call|jump)\s+([A-Za-z_]\w*)", re.M)
QUOTED_NAME_RE = re.compile(r"['\"]([A-Za-z_]\w*)['\"]")
IF_RE = re.compile(r"^\s*(if|elif|else)\b")
COND_CHAR_RE = re.compile(
    r"current_character(?:\s*\.\s*text_id)?\s*(==|!=)\s*"
    r"(?:[\"'](\w+)[\"']|([A-Za-z_]\w*)_details)"
)

# Fallback when a phase folder contains no change_time() call (notably _common/).
# Keyed on (day_folder.lower(), phase name lowercased with its "1_"/"2a_" prefix
# stripped). "No Hunt" is saturday_afternoon for nurse/psychic but
# saturday_afternoon_no_hunt for lad -- if it is ever hit as a fallback, verify.
FALLBACK_PHASE_MAP = {
    ("day 1", "afternoon"): "friday_afternoon",
    ("day 1", "evening"): "friday_evening",
    ("day 2", "morning"): "saturday_morning",
    ("day 2", "hunt"): "saturday_afternoon",
    ("day 2", "no hunt"): "saturday_afternoon",
    ("day 2", "evening"): "saturday_evening",
    ("day 3", "morning"): "sunday_morning",
    ("day 3", "afternoon"): "sunday_afternoon",
}

CHAPTER_ORDER = [
    "friday_afternoon", "friday_evening", "saturday_morning",
    "saturday_afternoon", "saturday_afternoon_no_hunt", "saturday_evening",
    "sunday_morning", "sunday_afternoon", "end",
]

AMBIGUOUS = "?"


# --------------------------------------------------------------------------
# Low-level text helpers (same as check_menu_consistency.py)
# --------------------------------------------------------------------------

def strip_comments(text):
    """Blank out # comments while preserving offsets and string contents."""
    out = list(text)
    i, n = 0, len(text)
    quote = None
    while i < n:
        c = text[i]
        if quote:
            if c == "\\" and len(quote) == 1:
                i += 2
                continue
            if text.startswith(quote, i):
                i += len(quote)
                quote = None
                continue
            i += 1
            continue
        if c in "\"'":
            if text.startswith(c * 3, i):
                quote = c * 3
                i += 3
            else:
                quote = c
                i += 1
            continue
        if c == "#":
            while i < n and text[i] != "\n":
                out[i] = " "
                i += 1
            continue
        i += 1
    return "".join(out)


def mask_triple_strings(text):
    """Blank out the contents of triple-quoted strings (dialogue blocks) while
    preserving offsets, so indentation-based flow analysis is not confused by
    narration text. Expects comment-stripped input."""
    out = list(text)
    i, n = 0, len(text)
    quote = None
    while i < n:
        c = text[i]
        if quote:
            if c == "\\" and len(quote) == 1:
                i += 2
                continue
            if text.startswith(quote, i):
                i += len(quote)
                quote = None
                continue
            if len(quote) == 3 and c != "\n":
                out[i] = " "
            i += 1
            continue
        if c in "\"'":
            if text.startswith(c * 3, i):
                quote = c * 3
                i += 3
            else:
                quote = c
                i += 1
            continue
        i += 1
    return "".join(out)


def match_paren(text, open_idx):
    """Return index just after the parenthesis matching text[open_idx]."""
    assert text[open_idx] == "("
    depth = 0
    quote = None
    i, n = open_idx, len(text)
    while i < n:
        c = text[i]
        if quote:
            if c == "\\" and len(quote) == 1:
                i += 2
                continue
            if text.startswith(quote, i):
                i += len(quote)
                quote = None
                continue
            i += 1
            continue
        if c in "\"'":
            quote = c * 3 if text.startswith(c * 3, i) else c
            i += len(quote)
            continue
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return None


def line_of(text, idx):
    return text.count("\n", 0, idx) + 1


def iter_rpy_files():
    for root, dirs, files in os.walk(SCRIPTS_DIR):
        dirs[:] = [d for d in dirs if d.lower() not in SKIP_DIRS]
        for name in sorted(files):
            if name.endswith(".rpy") and name not in EXCLUDED_FILES:
                yield os.path.join(root, name)


def rel(path):
    return os.path.relpath(path, SCRIPTS_DIR).replace(os.sep, "/")


def chapter_sort_key(chapter):
    return (CHAPTER_ORDER.index(chapter) if chapter in CHAPTER_ORDER else 99, chapter)


# --------------------------------------------------------------------------
# Pass 1 - phase folder -> chapter id, from change_time(..., chapter='X')
# --------------------------------------------------------------------------

def phase_folder_of(rel_path):
    """Return 'char/Day N/Phase' for files inside a day structure, else None."""
    parts = rel_path.split("/")
    if len(parts) >= 4 and parts[1].lower().startswith("day"):
        return "/".join(parts[:3])
    return None


def build_folder_chapter_map(file_texts):
    folder_chapters = defaultdict(set)
    for path, text in file_texts.items():
        folder = phase_folder_of(rel(path))
        if folder:
            for chapter in CHANGE_TIME_RE.findall(text):
                folder_chapters[folder].add(chapter)
    return folder_chapters


def fallback_chapter(folder):
    day, phase = folder.split("/")[1:3]
    phase = re.sub(r"^\d+[a-z]?_", "", phase).lower()
    return FALLBACK_PHASE_MAP.get((day.lower(), phase))


def resolve_chapter(rel_path, folder_chapters):
    """Return (chapter, note). chapter is AMBIGUOUS when unresolvable."""
    parts = rel_path.split("/")
    if len(parts) >= 3 and parts[1].lower() == "endings":
        return "end", None
    folder = phase_folder_of(rel_path)
    if folder is None:
        return AMBIGUOUS, "file at character root, reachable from several chapters"
    chapters = folder_chapters.get(folder)
    if chapters:
        if len(chapters) == 1:
            return next(iter(chapters)), None
        return AMBIGUOUS, "folder declares several chapters: " + ", ".join(sorted(chapters))
    chapter = fallback_chapter(folder)
    if chapter:
        return chapter, None
    return AMBIGUOUS, "no change_time() and no fallback for folder " + folder


def resolve_playing(rel_path):
    """Return (playing_char, note)."""
    top = rel_path.split("/")[0]
    if top == "_common":
        return AMBIGUOUS, "_common file, shared between storylines"
    if top.endswith(".rpy"):
        return AMBIGUOUS, "file at scripts root"
    return top, None


# --------------------------------------------------------------------------
# _common resolution - call graph + current_character guards
# --------------------------------------------------------------------------

def build_label_index(flow_texts):
    """(file_labels: path -> sorted [(line, name)], label_callers: name -> [(path, line)])."""
    file_labels = {}
    common_label_names = set()
    for path, text in flow_texts.items():
        labels = [(line_of(text, m.start()), m.group(1))
                  for m in LABEL_DEF_RE.finditer(text)]
        file_labels[path] = labels
        if rel(path).split("/")[0] == "_common":
            common_label_names.update(name for _, name in labels)

    label_callers = defaultdict(set)
    for path, text in flow_texts.items():
        for m in CALL_JUMP_RE.finditer(text):
            label_callers[m.group(1)].add((path, line_of(text, m.start())))
        # Menu redirects and call expressions reference labels as quoted
        # strings; only worth tracking for the _common labels we resolve.
        # NOTE: flow_texts has triple-quoted contents masked, so dialogue
        # cannot produce false positives here; single-quoted refs survive.
        for m in QUOTED_NAME_RE.finditer(text):
            if m.group(1) in common_label_names:
                label_callers[m.group(1)].add((path, line_of(text, m.start())))
    return file_labels, label_callers


def enclosing_label(path, line, file_labels):
    result = None
    for label_line, name in file_labels.get(path, []):
        if label_line <= line:
            result = name
        else:
            break
    return result


def guard_characters(flow_text, target_line):
    """Walk the enclosing blocks of target_line upward.

    Returns (includes, excludes, unresolved):
      includes  - the unlock only runs when current_character is one of these
      excludes  - the unlock never runs for these characters
      unresolved - a guard involves current_character in a way this static
                   walk cannot interpret; attribute by hand.
    """
    lines = flow_text.split("\n")

    def indent(s):
        return len(s) - len(s.lstrip())

    idx = target_line - 1
    cur = indent(lines[idx])
    includes, excludes = set(), set()
    unresolved = False

    def chain_conditions(start, ind):
        """== characters of the if/elif chain above an else/elif at indent ind."""
        chars = []
        j = start
        while j >= 0:
            l2 = lines[j]
            if not l2.strip():
                j -= 1
                continue
            ind2 = indent(l2)
            if ind2 > ind:
                j -= 1
                continue
            if ind2 < ind:
                break
            m2 = IF_RE.match(l2)
            if not m2:
                break
            for op, ch_str, ch_obj in COND_CHAR_RE.findall(l2):
                chars.append((op, ch_str or ch_obj))
            if m2.group(1) == "if":
                break
            j -= 1
        return chars

    i = idx - 1
    while i >= 0 and cur > 0:
        line = lines[i]
        if not line.strip():
            i -= 1
            continue
        ind = indent(line)
        if ind < cur:
            m = IF_RE.match(line)
            if m:
                conds = COND_CHAR_RE.findall(line)
                if conds:
                    if len(conds) > 1:
                        unresolved = True  # compound and/or of characters
                    for op, ch_str, ch_obj in conds:
                        ch = ch_str or ch_obj
                        if op == "==":
                            includes.add(ch)
                        else:
                            excludes.add(ch)
                elif m.group(1) in ("elif", "else"):
                    # branch without its own character test: it excludes every
                    # character matched by the earlier branches of the chain
                    for op, ch in chain_conditions(i - 1, ind):
                        if op == "==":
                            excludes.add(ch)
                        else:
                            unresolved = True
            cur = ind
        i -= 1
    return includes, excludes, unresolved


def resolve_common_site(path, line, file_labels, label_callers, folder_chapters):
    """Trace which character scripts reach the label enclosing a _common
    unlock site. Returns a list of (playing, chapter, via_file_line)."""
    label = enclosing_label(path, line, file_labels)
    if label is None:
        return []
    visited = {label}
    stack = [label]
    found = []
    while stack:
        current = stack.pop()
        for cpath, cline in sorted(label_callers.get(current, [])):
            crel = rel(cpath)
            if crel.split("/")[0] == "_common":
                enclosing = enclosing_label(cpath, cline, file_labels)
                if enclosing and enclosing not in visited:
                    visited.add(enclosing)
                    stack.append(enclosing)
            else:
                playing, _note = resolve_playing(crel)
                chapter, _note = resolve_chapter(crel, folder_chapters)
                found.append((playing, chapter, "{}:{}".format(crel, cline)))
    return found


# --------------------------------------------------------------------------
# Pass 2 - unlock sites
# --------------------------------------------------------------------------

class Site(object):
    def __init__(self, owner, text_id, playing, chapter, rel_path, line, notes):
        self.owner = owner
        self.text_id = text_id
        self.playing = playing
        self.chapter = chapter
        self.rel_path = rel_path
        self.line = line
        self.notes = notes

    @property
    def ambiguous(self):
        return AMBIGUOUS in (self.playing, self.chapter)

    @property
    def pair(self):
        return (self.playing, self.chapter)


def collect_sites(file_texts, folder_chapters, flow_texts, file_labels, label_callers):
    sites = []
    for path, text in sorted(file_texts.items()):
        rel_path = rel(path)
        for m in UNLOCK_RE.finditer(text):
            owner, text_id = m.group(1), m.group(2)
            line = line_of(text, m.start())

            if rel_path.split("/")[0] == "_common":
                sites.extend(common_sites(owner, text_id, path, rel_path, line,
                                          flow_texts, file_labels, label_callers,
                                          folder_chapters))
                continue

            playing, note_p = resolve_playing(rel_path)
            chapter, note_c = resolve_chapter(rel_path, folder_chapters)
            notes = [n for n in (note_p, note_c) if n]
            sites.append(Site(owner, text_id, playing, chapter, rel_path, line, notes))
    return sites


def common_sites(owner, text_id, path, rel_path, line, flow_texts, file_labels,
                 label_callers, folder_chapters):
    """One Site per (playing, chapter) pair resolved through the call graph,
    or a single ambiguous Site when resolution fails."""
    callers = resolve_common_site(path, line, file_labels, label_callers,
                                  folder_chapters)
    includes, excludes, unresolved = guard_characters(flow_texts[path], line)

    if callers and not unresolved:
        merged = {}
        for p_char, p_chap, via in callers:
            if p_char in excludes:
                continue
            if includes and p_char not in includes:
                continue
            merged.setdefault((p_char, p_chap), []).append(via)
        if merged:
            result = []
            for (p_char, p_chap), vias in sorted(merged.items()):
                note = "called from " + ", ".join(vias)
                if includes:
                    note += " | guard: current_character == " + p_char
                elif excludes:
                    note += " | guard excludes " + ", ".join(sorted(excludes))
                result.append(Site(owner, text_id, p_char, p_chap,
                                   rel_path, line, [note]))
            return result

    if unresolved:
        note = "_common file, current_character guard too complex"
    elif callers:
        note = "_common file, guard removed every caller"
    else:
        note = "_common file, no caller found for enclosing label"
    chapter, note_c = resolve_chapter(rel_path, folder_chapters)
    return [Site(owner, text_id, AMBIGUOUS, chapter, rel_path, line,
                 [n for n in (note, note_c) if n])]


# --------------------------------------------------------------------------
# Pass 3 - declared hidden infos in <char>_config.rpy
# --------------------------------------------------------------------------

def collect_declared(file_texts):
    """owner -> ordered list of (text_id, declared_unlock_chapters)."""
    declared = {}
    for path, text in sorted(file_texts.items()):
        rel_path = rel(path)
        if not rel_path.endswith("_config.rpy"):
            continue
        # Some configs write "CharacterDescriptionHiddenList (" with a space
        idx = text.find("CharacterDescriptionHiddenList")
        if idx == -1:
            continue
        owner = rel_path.split("/")[0]
        end = match_paren(text, text.index("(", idx))
        block = text[idx:end]
        entries = []
        pos = 0
        while True:
            call = block.find("CharacterInformation", pos)
            if call == -1:
                break
            call_end = match_paren(block, block.index("(", call))
            src = block[call:call_end].strip()
            pos = call_end
            try:
                node = ast.parse(src, mode="eval").body
            except SyntaxError:
                print("WARNING: could not parse entry in {}".format(rel_path))
                continue
            text_id = node.args[1].value if len(node.args) > 1 else None
            pairs = []
            for kw in node.keywords:
                if kw.arg == "unlock_chapters":
                    try:
                        pairs = [tuple(p) for p in ast.literal_eval(kw.value)]
                    except (ValueError, TypeError):
                        print("WARNING: unparseable unlock_chapters for '{}' in {}".format(
                            text_id, rel_path))
            entries.append((text_id, pairs))
        declared[owner] = entries
    return declared


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------

def format_pairs(pairs):
    return "[" + ", ".join(
        "('{}', '{}')".format(c, ch)
        for c, ch in sorted(pairs, key=lambda p: (chapter_sort_key(p[1]), p[0]))
    ) + "]"


def report(sites, declared, only_character=None, diff=False):
    by_owner = defaultdict(lambda: defaultdict(list))
    for site in sites:
        by_owner[site.owner][site.text_id].append(site)

    owners = sorted(set(by_owner) | set(declared))
    if only_character:
        owners = [o for o in owners if o == only_character]

    problems = 0
    for owner in owners:
        print("\n== {} ==".format(owner))
        declared_entries = declared.get(owner, [])
        declared_ids = [text_id for text_id, _ in declared_entries]
        scanned = by_owner.get(owner, {})

        for text_id, declared_pairs in declared_entries:
            entry_sites = scanned.get(text_id, [])
            clean = sorted({s.pair for s in entry_sites if not s.ambiguous},
                           key=lambda p: (chapter_sort_key(p[1]), p[0]))
            dirty = [s for s in entry_sites if s.ambiguous]

            print("  {}:".format(text_id))
            if not entry_sites:
                print("    no story unlock() found (debug-only or TODO)")
            for site in entry_sites:
                if site.ambiguous:
                    marker = "   << attribute by hand: " + "; ".join(site.notes)
                elif site.notes:
                    marker = "   [" + "; ".join(site.notes) + "]"
                else:
                    marker = ""
                print("    ('{}', '{}')   {}:{}{}".format(
                    site.playing, site.chapter, site.rel_path, site.line, marker))
            if clean:
                print("    suggested: unlock_chapters={}".format(format_pairs(clean)))

            if diff:
                missing = [p for p in clean if p not in declared_pairs]
                stale = [p for p in declared_pairs if p not in clean]
                if missing:
                    problems += 1
                    print("    DIFF MISSING (scanned but not declared): {}".format(format_pairs(missing)))
                # A stale pair may be a deliberate manual attribution of an
                # ambiguous site -- only a problem when nothing is ambiguous.
                if stale and not dirty:
                    problems += 1
                    print("    DIFF STALE (declared but not found in scripts): {}".format(format_pairs(stale)))
                elif stale and dirty:
                    print("    DIFF CHECK (declared, presumably manual attribution of the flagged sites): {}".format(format_pairs(stale)))
                if not missing and not stale and (clean or declared_pairs):
                    print("    DIFF OK")

        undeclared = [tid for tid in sorted(scanned) if tid not in declared_ids]
        for text_id in undeclared:
            problems += 1
            print("  {}: UNLOCKED BUT NOT DECLARED in {}_config.rpy (typo?)".format(text_id, owner))
            for site in scanned[text_id]:
                print("    {}:{}".format(site.rel_path, site.line))

    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("--character", help="only report hidden infos of this character")
    parser.add_argument("--diff", action="store_true",
                        help="compare scanned pairs against declared unlock_chapters")
    parser.add_argument("--verbose", action="store_true",
                        help="print the phase-folder -> chapter resolution table")
    args = parser.parse_args()

    file_texts = {}
    for path in iter_rpy_files():
        with open(path, "r", encoding="utf-8") as handle:
            file_texts[path] = strip_comments(handle.read())

    folder_chapters = build_folder_chapter_map(file_texts)
    if args.verbose:
        print("Phase-folder -> chapter resolution:")
        for folder in sorted(folder_chapters):
            print("  {}  ->  {}".format(folder, ", ".join(sorted(folder_chapters[folder]))))

    flow_texts = {path: mask_triple_strings(text) for path, text in file_texts.items()}
    file_labels, label_callers = build_label_index(flow_texts)
    sites = collect_sites(file_texts, folder_chapters, flow_texts, file_labels, label_callers)
    declared = collect_declared(file_texts)
    problems = report(sites, declared, args.character, args.diff)

    total = len(sites)
    flagged = len([s for s in sites if s.ambiguous])
    print("\n{} unlock sites scanned, {} need manual attribution.".format(total, flagged))
    if args.diff and problems:
        print("{} diff problem(s) found.".format(problems))
        sys.exit(1)


if __name__ == "__main__":
    main()
