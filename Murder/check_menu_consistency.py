#!/usr/bin/env python3
"""
check_menu_consistency.py - static audit of TimedMenu / TimedMenuChoice usage.

Parses every .rpy file under Murder/game/scripts/ and checks the in-game menu
conventions:

  [1] MAP ROOM CONFLICTS
      On a map menu (is_map=True), two choices sharing the same room must have
      provably mutually exclusive conditions, otherwise the map screen (first
      match wins) and run_menu/display_choices can disagree on which choice
      fires.

  [2] GREY-OUT CORRECTNESS
      A greyed-out choice is still clickable (tutorial_already_chosen), so the
      data that drives is_already_chosen() must be right:
        - duplicate menu ids (all_menus is keyed by id for a whole playthrough)
        - linked_choice must match the redirect of a choice in the same menu
        - next_menu must reference a menu id that is defined somewhere
        - keep_alive choices without next_menu grey out after one pick; if
          their redirect contains conditional content, re-picking while greyed
          may still show something new (manual review list)

  [3] TIME VALUES
      Every non-exit choice should carry a time_spent value. Exit choices
      (early_exit / generic_cancel) are exempt. Menus where every choice is
      time-free are reported compactly (story beats), menus mixing timed and
      0-cost choices are the likely mistakes.

  [4] NEXT_MENU WIRING
      A choice whose redirect label (transitively, via jump/call) opens another
      menu must declare next_menu with that menu's id, so is_valid() /
      is_menu_valid() / is_already_chosen() work before the sub-menu was ever
      opened.

Usage:
    python Murder/check_menu_consistency.py [--character captain] [--verbose]
"""

import argparse
import ast
import os
import re
import sys
from collections import defaultdict

GAME_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "game")
SCRIPTS_DIR = os.path.join(GAME_DIR, "scripts")

# Engine / debug files whose TimedMenu references are not game content
EXCLUDED_FILES = {"custom_menus.rpy", "debug_choices.rpy", "test_plan_runner.rpy"}

# TimedMenuChoice signature (positional order in custom_menus.rpy)
CHOICE_SIG = [
    "text", "redirect", "time_spent", "choice_repeat", "hidden", "keep_alive",
    "early_exit", "condition", "room", "already_chosen", "next_menu",
    "linked_choice", "parent_menu_id",
]

EXIT_REDIRECTS = {"generic_cancel"}

TOP_LEVEL_STOPPERS = re.compile(
    r"^(label|screen|init|python|define|default|transform|image|style|testcase)\b"
)
LABEL_RE = re.compile(r"^label\s+([A-Za-z_]\w*)\s*(?:\([^)]*\))?\s*:")
JUMP_CALL_RE = re.compile(r"^\s*(?:jump|call)\s+([A-Za-z_]\w*)\s*(\([^)]*\))?\s*$")
STRING_ARG_RE = re.compile(r"['\"]([A-Za-z_]\w*)['\"]")
STRING_CONST_RE = re.compile(r"^\s*([A-Za-z_]\w*)\s*=\s*(\"[^\"]*\"|'[^']*')\s*$")
SAVED_VAR_DICT_RE = re.compile(r"[\"']([A-Za-z_]\w*)[\"']\s*:\s*([A-Za-z_]\w*)")


# --------------------------------------------------------------------------
# Low-level text helpers (comment stripping + string-aware paren matching)
# --------------------------------------------------------------------------

def strip_comments(text):
    """Blank out # comments while preserving offsets and string contents."""
    out = list(text)
    i, n = 0, len(text)
    quote = None       # current quote: ', ", ''', or three-double
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


# --------------------------------------------------------------------------
# Data model
# --------------------------------------------------------------------------

class Choice(object):
    def __init__(self, menu, params, file, line):
        self.menu = menu
        self.file = file
        self.line = line
        self.params = params          # name -> (kind, value); kind: lit | expr
        self.time_given = "time_spent" in params

    def _val(self, name, default=None):
        kind, value = self.params.get(name, ("lit", default))
        return value if kind == "lit" else None

    def _raw(self, name):
        if name not in self.params:
            return None
        kind, value = self.params[name]
        return value

    @property
    def text(self):
        kind, value = self.params.get("text", ("lit", "?"))
        return value if kind == "lit" else value  # expr source is readable too

    @property
    def redirect(self):
        return self._val("redirect")

    @property
    def time_spent(self):
        return self._val("time_spent", 0)

    @property
    def keep_alive(self):
        return bool(self._val("keep_alive", False))

    @property
    def early_exit(self):
        return bool(self._val("early_exit", False))

    @property
    def condition(self):
        return self.params.get("condition")   # (kind, value) tuple or None

    @property
    def room(self):
        return self.params.get("room")        # (kind, value) tuple or None

    @property
    def next_menu(self):
        return self._val("next_menu")

    @property
    def linked_choice(self):
        return self._val("linked_choice")

    def is_exit(self):
        return self.early_exit or self.redirect in EXIT_REDIRECTS

    def where(self):
        return "%s:%d" % (self.file, self.line)

    def short(self):
        return "'%s' -> %s" % (self.text, self.redirect)


class MenuDef(object):
    def __init__(self, id, id_is_literal, is_map, var_name, file, line, label):
        self.id = id
        self.id_is_literal = id_is_literal
        self.is_map = is_map
        self.var_name = var_name
        self.file = file
        self.line = line
        self.label = label
        self.choices = []

    def where(self):
        return "%s:%d" % (self.file, self.line)


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------

def literal_or_expr(node):
    try:
        return ("lit", ast.literal_eval(node))
    except (ValueError, SyntaxError):
        return ("expr", ast.unparse(node))


def parse_choice_call(call_node, menu, file, base_line, text):
    params = {}
    for i, arg in enumerate(call_node.args):
        if i < len(CHOICE_SIG):
            params[CHOICE_SIG[i]] = literal_or_expr(arg)
    for kw in call_node.keywords:
        if kw.arg:
            params[kw.arg] = literal_or_expr(kw.value)
    line = base_line + call_node.lineno - 1
    return Choice(menu, params, file, line)


def parse_menu_span(span, file, base_line, var_name, label):
    """span is the source text 'TimedMenu(...)'. Returns MenuDef or None."""
    try:
        tree = ast.parse(span, mode="eval")
    except SyntaxError:
        return None
    call = tree.body
    if not isinstance(call, ast.Call):
        return None

    menu_id, id_is_literal = None, False
    is_map = False
    choices_node = None

    if call.args:
        kind, value = literal_or_expr(call.args[0])
        menu_id, id_is_literal = (value, True) if kind == "lit" else (value, False)
    if len(call.args) > 1 and isinstance(call.args[1], ast.List):
        choices_node = call.args[1]
    for kw in call.keywords:
        if kw.arg == "id":
            kind, value = literal_or_expr(kw.value)
            menu_id, id_is_literal = (value, True) if kind == "lit" else (value, False)
        elif kw.arg == "choices" and isinstance(kw.value, ast.List):
            choices_node = kw.value
        elif kw.arg == "is_map":
            kind, value = literal_or_expr(kw.value)
            is_map = bool(value) if kind == "lit" else False

    menu = MenuDef(menu_id, id_is_literal, is_map, var_name, file,
                   base_line + call.lineno - 1, label)
    if choices_node is not None:
        for elt in choices_node.elts:
            if isinstance(elt, ast.Call) and getattr(elt.func, "id", "") == "TimedMenuChoice":
                menu.choices.append(parse_choice_call(elt, menu, file, base_line, span))
    return menu


class GameModel(object):
    def __init__(self):
        self.menus = []                       # all MenuDef
        self.menus_by_id = defaultdict(list)  # id -> [MenuDef]
        self.var_to_id = {}                   # variable name -> menu id
        self.labels = {}                      # label -> dict(file, line, body, edges, run_menu_args)
        self.string_consts = {}               # name -> string value (condition shortcuts)
        self.saved_var_map = defaultdict(set) # (character, key) -> {menu id}
        self.call_string_args = set()         # string literals passed in call X(...) - dynamic menu ids

    def add_menu(self, menu):
        self.menus.append(menu)
        if menu.id is not None and menu.id_is_literal:
            self.menus_by_id[menu.id].append(menu)
            if menu.var_name:
                self.var_to_id[menu.var_name] = menu.id


def character_of(path):
    rel = os.path.relpath(path, SCRIPTS_DIR)
    first = rel.split(os.sep)[0]
    return "_game" if first == ".." else first


def scan_file(path, model):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    text = strip_comments(raw)   # comments blanked, offsets preserved
    rel = os.path.relpath(path, GAME_DIR).replace(os.sep, "/")

    # ---- labels and their bodies ----
    lines = text.split("\n")
    label_starts = []   # (line_index, name)
    for idx, line in enumerate(lines):
        m = LABEL_RE.match(line)
        if m:
            label_starts.append((idx, m.group(1)))
        m2 = STRING_CONST_RE.match(line)
        if m2:
            model.string_consts[m2.group(1)] = ast.literal_eval(m2.group(2))

    file_labels = []
    for j, (idx, name) in enumerate(label_starts):
        end = label_starts[j + 1][0] if j + 1 < len(label_starts) else len(lines)
        body = "\n".join(lines[idx + 1:end])
        edges = {}    # target label -> tuple of string literal args (dynamic ids)
        for bl in lines[idx + 1:end]:
            m = JUMP_CALL_RE.match(bl)
            if m and m.group(1) != "run_menu":
                str_args = tuple(STRING_ARG_RE.findall(m.group(2) or ""))
                edges[m.group(1)] = str_args
                model.call_string_args.update(str_args)
        model.labels[name] = {
            "file": rel, "line": idx + 1, "body": body,
            "body_start_line": idx + 2, "edges": edges, "run_menu_args": [],
        }
        file_labels.append((idx + 1, name))

    def label_at(line_no):
        current = None
        for ln, name in file_labels:
            if ln <= line_no:
                current = name
            else:
                break
        return current

    # ---- TimedMenu definitions ----
    for m in re.finditer(r"\bTimedMenu\s*\(", text):
        open_idx = text.index("(", m.start())
        end = match_paren(text, open_idx)
        if end is None:
            continue
        span = text[m.start():end]
        base_line = line_of(text, m.start())
        prefix = text[max(0, m.start() - 200):m.start()]
        am = re.search(r"([A-Za-z_]\w*)\s*=\s*$", prefix)
        var_name = am.group(1) if am else None
        menu = parse_menu_span(span, rel, base_line, var_name, label_at(base_line))
        if menu is not None:
            menu.character = character_of(path)
            # `# no-next-menu: ...` comment inside the menu suppresses the
            # missing-next_menu warning for the whole menu (deliberate skip)
            menu.no_next_menu_pragma = "no-next-menu" in raw[max(0, m.start() - 600):end]
            model.add_menu(menu)

    # ---- run_menu invocations ----
    for m in re.finditer(r"\brun_menu\s*\(", text):
        open_idx = text.index("(", m.start())
        end = match_paren(text, open_idx)
        if end is None:
            continue
        span = text[m.start():end]
        base_line = line_of(text, m.start())
        owner = label_at(base_line)
        if owner and owner in model.labels:
            try:
                call = ast.parse(span, mode="eval").body
                if call.args:
                    model.labels[owner]["run_menu_args"].append(
                        (ast.unparse(call.args[0]), base_line))
            except SyntaxError:
                pass

    # ---- saved_variables dict entries in config files ----
    if os.path.basename(path).endswith("_config.rpy"):
        char = character_of(path)
        for m in SAVED_VAR_DICT_RE.finditer(text):
            model.saved_var_map[(char, m.group(1))].add(m.group(2))


def build_model(character=None):
    model = GameModel()
    for root, dirs, files in os.walk(GAME_DIR):
        dirs[:] = [d for d in dirs if d not in ("tests", "saves", "cache", "gui")]
        for fn in sorted(files):
            if not fn.endswith(".rpy") or fn in EXCLUDED_FILES:
                continue
            scan_file(os.path.join(root, fn), model)
    # second pass: resolve saved_var menu variables to ids
    resolved = defaultdict(set)
    for (char, key), var_names in model.saved_var_map.items():
        for vn in var_names:
            if vn in model.var_to_id:
                resolved[(char, key)].add(model.var_to_id[vn])
    model.saved_var_map = resolved
    return model


# --------------------------------------------------------------------------
# Menu-id resolution + label graph traversal
# --------------------------------------------------------------------------

def resolve_run_menu_arg(model, arg_src):
    """Return set of menu ids the run_menu argument may refer to."""
    try:
        node = ast.parse(arg_src, mode="eval").body
    except SyntaxError:
        return set()
    # inline TimedMenu("id", ...)
    if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "TimedMenu":
        for cand in node.args[:1] + [kw.value for kw in node.keywords if kw.arg == "id"]:
            try:
                return {ast.literal_eval(cand)}
            except (ValueError, SyntaxError):
                return set()
        return set()
    # plain variable
    if isinstance(node, ast.Name):
        if node.id in model.var_to_id:
            return {model.var_to_id[node.id]}
        return set()
    # <details>.saved_variables["key"]
    if (isinstance(node, ast.Subscript)
            and isinstance(node.value, ast.Attribute)
            and node.value.attr == "saved_variables"):
        try:
            key = ast.literal_eval(node.slice)
        except (ValueError, SyntaxError):
            return set()
        owner = ast.unparse(node.value.value)        # e.g. captain_details
        char_hint = owner.replace("_details", "")
        exact = model.saved_var_map.get((char_hint, key))
        if exact:
            return set(exact)
        ids = set()
        for (char, k), v in model.saved_var_map.items():
            if k == key:
                ids |= v
        return ids
    return set()


def subtree_runs_dynamic_menu(model, start_label, max_depth=5, _seen=None):
    """True if the label (or labels it calls) runs a menu whose id is dynamic."""
    if _seen is None:
        _seen = set()
    if start_label in _seen or start_label not in model.labels or max_depth < 0:
        return False
    _seen.add(start_label)
    info = model.labels[start_label]
    for arg_src, _line in info["run_menu_args"]:
        if not resolve_run_menu_arg(model, arg_src):
            return True
    return any(subtree_runs_dynamic_menu(model, t, max_depth - 1, _seen)
               for t in info["edges"])


def menus_opened_from(model, start_label, max_depth=5):
    """All menu ids reachable from a label via jump/call (not via menu choices)."""
    if start_label not in model.labels:
        return None
    seen_labels = set()
    found = set()
    frontier = [(start_label, 0)]
    while frontier:
        label, depth = frontier.pop()
        if label in seen_labels or label not in model.labels:
            continue
        seen_labels.add(label)
        info = model.labels[label]
        for arg_src, _line in info["run_menu_args"]:
            found |= resolve_run_menu_arg(model, arg_src)
        if depth < max_depth:
            for target, str_args in info["edges"].items():
                # call X('some_id', ...) where X builds TimedMenu(id=<param>):
                # the string args are candidate dynamic menu ids
                if str_args and subtree_runs_dynamic_menu(model, target):
                    found.update(str_args)
                frontier.append((target, depth + 1))
    return found


def body_has_conditional_content(model, start_label, max_depth=2):
    """True if the redirect label (transitively) contains if/elif or unlock()."""
    seen = set()
    frontier = [(start_label, 0)]
    pattern = re.compile(r"^\s*(if|elif)\s|\.unlock\(")
    while frontier:
        label, depth = frontier.pop()
        if label in seen or label not in model.labels:
            continue
        seen.add(label)
        body = model.labels[label]["body"]
        for line in body.split("\n"):
            if pattern.search(line):
                return True
        if depth < max_depth:
            for target in model.labels[label]["edges"]:
                frontier.append((target, depth + 1))
    return False


# --------------------------------------------------------------------------
# Condition exclusivity proof (best effort)
# --------------------------------------------------------------------------

def resolve_condition(model, cond):
    """cond is (kind, value) from params or None. Returns condition source or None."""
    if cond is None:
        return None
    kind, value = cond
    if kind == "lit":
        if value is None:
            return None
        return value if isinstance(value, str) else repr(value)
    # expression: a Name may be one of the condition_* string constants
    if value in model.string_consts:
        return model.string_consts[value]
    # 'not ' + condition_x pattern (string concatenation building a negation)
    try:
        node = ast.parse(value, mode="eval").body
    except SyntaxError:
        return value
    if (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add)
            and isinstance(node.left, ast.Constant)
            and isinstance(node.left.value, str)
            and node.left.value.strip() == "not"
            and isinstance(node.right, ast.Name)
            and node.right.id in model.string_consts):
        return "not (%s)" % model.string_consts[node.right.id]
    return value


def _parse_cond(src):
    """Parse a condition source, rewriting `'not ' + X` into `not (X)`."""
    try:
        node = ast.parse(src, mode="eval").body
    except SyntaxError:
        return None
    if (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add)
            and isinstance(node.left, ast.Constant)
            and isinstance(node.left.value, str)
            and node.left.value.strip() == "not"):
        return ast.UnaryOp(op=ast.Not(), operand=node.right)
    return node


def _conjuncts(node):
    out = []

    def flatten(n):
        if isinstance(n, ast.BoolOp) and isinstance(n.op, ast.And):
            for v in n.values:
                flatten(v)
        else:
            out.append(n)

    flatten(node)
    return out


def _normalize(n):
    """Normalise a conjunct to ('truth', expr_dump, negated) or ('eq', lhs_dump, literal)."""
    if (isinstance(n, ast.Compare) and len(n.ops) == 1
            and isinstance(n.ops[0], ast.Eq) and len(n.comparators) == 1):
        try:
            lit = ast.literal_eval(n.comparators[0])
        except (ValueError, SyntaxError):
            return ("truth", ast.dump(n), False)
        if lit is True:
            return ("truth", ast.dump(n.left), False)
        if lit is False:
            return ("truth", ast.dump(n.left), True)
        return ("eq", ast.dump(n.left), repr(lit))
    if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.Not):
        inner = _normalize(n.operand)
        if inner[0] == "truth":
            return ("truth", inner[1], not inner[2])
        return ("truth", ast.dump(n.operand), True)
    return ("truth", ast.dump(n), False)


def _conj_exclusive(na, nb):
    if na[0] != nb[0]:
        return False
    if na[0] == "eq":
        return na[1] == nb[1] and na[2] != nb[2]
    return na[1] == nb[1] and na[2] != nb[2]


def provably_exclusive(cond_a, cond_b):
    """True when the two conditions can never hold simultaneously.

    Decomposes `and` conjunctions: A and B excludes C if any single conjunct
    contradicts one of the other side (negation or == on different literals).
    """
    if cond_a is None or cond_b is None:
        return False
    na, nb = _parse_cond(cond_a), _parse_cond(cond_b)
    if na is None or nb is None:
        return False
    # compare individual conjuncts plus the whole expression, so that both
    # `A and X` vs `not A` and `not (A and X)` vs `A and X` are caught
    list_a = _conjuncts(na) + ([na] if isinstance(na, ast.BoolOp) else [])
    list_b = _conjuncts(nb) + ([nb] if isinstance(nb, ast.BoolOp) else [])
    for ca in list_a:
        norm_a = _normalize(ca)
        for cb in list_b:
            if _conj_exclusive(norm_a, _normalize(cb)):
                return True
    return False


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

class Report(object):
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.notes = []

    def error(self, section, msg):
        self.errors.append((section, msg))

    def warn(self, section, msg):
        self.warnings.append((section, msg))

    def note(self, section, msg):
        self.notes.append((section, msg))


def filter_menus(model, character):
    if not character:
        return model.menus
    return [m for m in model.menus if getattr(m, "character", "") == character]


def check_map_room_conflicts(model, menus, rep):
    for menu in menus:
        if not menu.is_map:
            continue
        by_room = defaultdict(list)
        for c in menu.choices:
            room = c.room
            if room is None:
                continue
            kind, value = room
            key = value if kind == "lit" else "<expr> " + str(value)
            by_room[key].append(c)
        for room, group in sorted(by_room.items()):
            if len(group) < 2:
                continue
            conds = [resolve_condition(model, c.condition) for c in group]
            unconditioned = [c for c, cd in zip(group, conds) if cd is None]
            if len(unconditioned) >= 2 or (unconditioned and len(group) > 1):
                lines = "\n".join(
                    "        - %s (condition=%s)  %s"
                    % (c.short(), cd, c.where()) for c, cd in zip(group, conds))
                rep.error("1", "map menu '%s' room '%s': %d choices and at least "
                               "one has NO condition (always matches):\n%s"
                          % (menu.id, room, len(group), lines))
                continue
            # all have conditions: prove pairwise exclusivity
            unproven = []
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    if not provably_exclusive(conds[i], conds[j]):
                        unproven.append((group[i], conds[i], group[j], conds[j]))
            if unproven:
                lines = "\n".join(
                    "        - %s  vs  %s\n          [%s] / [%s]  %s"
                    % (a.short(), b.short(), ca, cb, a.where())
                    for a, ca, b, cb in unproven)
                rep.warn("1", "map menu '%s' room '%s': conditions not provably "
                              "mutually exclusive, verify by hand:\n%s"
                         % (menu.id, room, lines))


def check_greyout(model, menus, rep):
    # duplicate ids (whole game scope, but reported once)
    for mid, defs in sorted(model.menus_by_id.items()):
        files = {d.file for d in defs}
        if len(files) > 1:
            sites = "\n".join("        - %s" % d.where() for d in defs)
            rep.error("2", "menu id '%s' is defined in %d different files "
                           "(all_menus is keyed by id for the whole playthrough, "
                           "the second definition is ignored at runtime):\n%s"
                      % (mid, len(files), sites))
        elif len(defs) > 1:
            sites = "\n".join("        - %s" % d.where() for d in defs)
            rep.note("2", "menu id '%s' defined %d times in the same file "
                          "(fine if these are exclusive branches):\n%s"
                     % (mid, len(defs), sites))

    for menu in menus:
        redirects = {c.redirect for c in menu.choices}
        for c in menu.choices:
            lc = c.linked_choice
            if lc and lc not in redirects:
                rep.error("2", "choice %s in menu '%s' has linked_choice='%s' "
                               "but no choice in this menu has that redirect "
                               "(is_already_chosen() will grey it immediately)  %s"
                          % (c.short(), menu.id, lc, c.where()))
            nm = c.next_menu
            if nm and nm not in model.menus_by_id and nm not in model.call_string_args:
                rep.error("2", "choice %s in menu '%s' has next_menu='%s' which is "
                               "never defined anywhere (choice will NEVER grey out "
                               "and is_menu_valid() always passes)  %s"
                          % (c.short(), menu.id, nm, c.where()))

        # keep_alive without next_menu greys after one pick; conditional content
        for c in menu.choices:
            if (c.keep_alive and not c.is_exit() and not c.next_menu
                    and not c.linked_choice and c.redirect
                    and body_has_conditional_content(model, c.redirect)):
                rep.note("2", "keep_alive choice %s in menu '%s' greys out after one "
                              "pick but its redirect has conditional content - check "
                              "a second (greyed) pick cannot show anything new  %s"
                         % (c.short(), menu.id, c.where()))


def check_time_values(model, menus, rep):
    for menu in menus:
        flagged = [c for c in menu.choices if not c.is_exit()]
        if not flagged:
            continue
        zero = [c for c in flagged
                if not c.time_given or (c.time_spent is not None and c.time_spent == 0)]
        timed = [c for c in flagged if c not in zero]
        if not zero:
            continue
        if menu.is_map:
            for c in zero:
                if c.next_menu:
                    rep.warn("3", "map menu '%s': choice %s has no time cost and opens "
                                  "next_menu='%s' (old pattern: cost charged inside the "
                                  "sub-menu - decide if the visit itself should now "
                                  "cost time)  %s"
                             % (menu.id, c.short(), c.next_menu, c.where()))
                else:
                    rep.error("3", "map menu '%s': choice %s has no time cost  %s"
                              % (menu.id, c.short(), c.where()))
        elif timed:
            for c in zero:
                if c.next_menu:
                    # established convention: a pure navigation opener costs 0,
                    # the sub-menu's own choices charge the time
                    rep.note("3", "menu '%s': navigation opener %s costs 0, time is "
                                  "charged inside next_menu='%s'  %s"
                             % (menu.id, c.short(), c.next_menu, c.where()))
                else:
                    rep.warn("3", "menu '%s' mixes timed and time-free choices: %s "
                                  "has no time cost  %s"
                             % (menu.id, c.short(), c.where()))
        else:
            rep.note("3", "menu '%s': all %d non-exit choices are time-free "
                          "(fine if this is a story beat, not free-roam)  %s"
                     % (menu.id, len(zero), menu.where()))


def check_next_menu(model, menus, rep):
    for menu in menus:
        for c in menu.choices:
            if c.is_exit() or not c.redirect:
                continue
            opened = menus_opened_from(model, c.redirect)
            declared = c.next_menu
            # generic guest menus exist once per playing character; keep only
            # the ones belonging to the character whose menu we are checking
            if opened and getattr(menu, "character", None):
                same_char = {
                    mid for mid in opened
                    if mid in model.menus_by_id
                    and any(getattr(d, "character", None) == menu.character
                            for d in model.menus_by_id[mid])
                }
                dynamic = {mid for mid in opened if mid not in model.menus_by_id}
                if same_char:
                    opened = same_char | dynamic
            if opened is None:
                if declared:
                    rep.note("4", "choice %s in menu '%s' declares next_menu='%s' but "
                                  "redirect label was not found (dynamic?)  %s"
                             % (c.short(), menu.id, declared, c.where()))
                continue
            opened.discard(menu.id)   # re-entering its own menu is not a sub-menu
            if declared and opened and declared not in opened:
                rep.error("4", "choice %s in menu '%s': next_menu='%s' but the "
                               "redirect actually opens %s  %s"
                          % (c.short(), menu.id, declared, sorted(opened), c.where()))
            elif not declared and opened:
                if getattr(menu, "no_next_menu_pragma", False):
                    rep.note("4", "choice %s in menu '%s' opens %s without next_menu "
                                  "- accepted (no-next-menu pragma on the menu)  %s"
                             % (c.short(), menu.id, sorted(opened), c.where()))
                elif c.keep_alive:
                    rep.warn("4", "keep_alive choice %s in menu '%s' opens %s but has "
                                  "no next_menu (grey-out cannot track the sub-menu "
                                  "when its opening is conditional)  %s"
                             % (c.short(), menu.id, sorted(opened), c.where()))
                else:
                    rep.note("4", "one-shot choice %s in menu '%s' opens %s without "
                                  "next_menu (only pre-pick visibility is affected; "
                                  "fine when the redirect has unique scene content)  %s"
                             % (c.short(), menu.id, sorted(opened), c.where()))
            elif declared and not opened:
                rep.note("4", "choice %s in menu '%s' declares next_menu='%s' but no "
                              "run_menu was found under its redirect (check by hand)  %s"
                         % (c.short(), menu.id, declared, c.where()))


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

SECTION_TITLES = {
    "1": "[1] MAP ROOM CONFLICTS",
    "2": "[2] GREY-OUT CORRECTNESS",
    "3": "[3] TIME VALUES",
    "4": "[4] NEXT_MENU WIRING",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--character", help="only audit menus defined under scripts/<character>/")
    ap.add_argument("--verbose", action="store_true", help="also print informational notes")
    args = ap.parse_args()

    model = build_model()
    menus = filter_menus(model, args.character)

    rep = Report()
    check_map_room_conflicts(model, menus, rep)
    check_greyout(model, menus, rep)
    check_time_values(model, menus, rep)
    check_next_menu(model, menus, rep)

    n_choices = sum(len(m.choices) for m in menus)
    print("=" * 72)
    print("MENU CONSISTENCY AUDIT")
    print("=" * 72)
    scope = args.character or "all characters"
    print("Scope:   %s" % scope)
    print("Menus:   %d   Choices: %d   Labels: %d"
          % (len(menus), n_choices, len(model.labels)))
    print()

    for section in ("1", "2", "3", "4"):
        errs = [m for s, m in rep.errors if s == section]
        warns = [m for s, m in rep.warnings if s == section]
        notes = [m for s, m in rep.notes if s == section]
        print(SECTION_TITLES[section])
        print("-" * 72)
        if not errs and not warns and (not notes or not args.verbose):
            print("  OK (%d note(s) hidden, use --verbose)" % len(notes)
                  if notes and not args.verbose else "  OK")
        for m in errs:
            print("  ERROR: %s" % m)
        for m in warns:
            print("  WARN:  %s" % m)
        if args.verbose:
            for m in notes:
                print("  note:  %s" % m)
        elif notes and (errs or warns):
            print("  (%d note(s) hidden, use --verbose)" % len(notes))
        print()

    print("Summary: %d error(s), %d warning(s), %d note(s)"
          % (len(rep.errors), len(rep.warnings), len(rep.notes)))
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
