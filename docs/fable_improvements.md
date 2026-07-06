# Fable Improvements — UI Code Assessment (menus, map, screens)

Assessment of the custom UI layer (custom menus, map, screens — not the dialogue scripts), 2026-07-04.
Files reviewed: `custom_menus.rpy`, `map.rpy`, `custom_screens.rpy`, `custom_functions.rpy`, `screens.rpy`,
`characters.rpy`, `progress.rpy`, `threads_screen.rpy`, `characters_screen.rpy`, `tutorials.rpy`, `script.rpy`,
`bug_report.rpy`, `debug_choices.rpy`, `endings.rpy`, sample map/menu configs.

**Overall verdict:** the design is sound and ambitious (timed menus, per-chapter map menus, checkpoint/restart,
in-screen tutorials, test/autoplay hooks threaded through everything). Newer files (`threads_screen.rpy`,
`bug_report.rpy`) are clean and well-commented. The older core (`custom_menus.rpy`, `characters.rpy`,
`progress.rpy`, `map.rpy`) carries real bugs, save-bloat risk, and heavy copy-paste.

All paths below are relative to `Murder/game/`.

---

## A. Likely bugs (verify, then fix)

- [x] **A1. Duplicate `Room` class with different constructor signatures.**
  `scripts/custom_menus.rpy:450` defines `Room(id, name, floor, area_points)`;
  `scripts/map.rpy:339` defines `Room(floor, area_points, id, name)`. Both at `init -1`.
  `map.rpy` loads later (alphabetical) so its version wins and the game works — but the dead twin is a
  landmine if file order or names ever change. Delete the one in `custom_menus.rpy`.

- [x] **A2. `progress_details` force-enables tutorial mode on every open.**
  `scripts/progress.rpy:621`: `on "show" action SetVariable("tutorial_on", True),` (note stray trailing comma).
  Contradicts the `seen_tutorial_progress_details` gating done by the caller in `screen progress`, and means the
  darkened tutorial overlay re-appears every time chapter details are opened. Almost certainly leftover
  experimentation (see the commented block right above it).

- [x] **A3. `load_test_checkpoints`: `normal_added` is never set to `True`** (`scripts/characters.rpy:825-878`),
  so the "fallback if all combos led to endings" branch *always* runs and adds one extra duplicate checkpoint
  per chapter. Debug-only, but it corrupts the debug checkpoint list.

- [x] **A4. Mutable default arguments** — classic Python trap, several instances:
  - `TimedMenu.__init__(self, id, choices=[], ...)` — `scripts/custom_menus.rpy:299`
  - `CharacterInformation(chapters=[], relevant_chapters=[])` — `scripts/characters.rpy:354-355`
  - `CharacterDetails(saved_variables=dict(), test_checkpoints=dict())` — `scripts/characters.rpy:381-382`
  Any two objects built without those args silently share one list/dict. Use `None` + fallback in the body.

- [x] **A5. `CharacterDetails.know_real_name` parameter is ignored** — accepted as `know_real_name=True` then
  hard-coded to `self.know_real_name = False` (`scripts/characters.rpy:394`). Honour it or remove it.

- [x] **A6. Help screen placeholder buttons shipped** (`screens.rpy:1023-1033`): "Characters", "About" and a
  literal "Max" button all switch to the same Progress tab; the "Clock & Time" and "Progress" tabs still contain
  "Placeholder:" body text.

- [x] **A7. `version_screen` overlay runs `export_transcript` when clicked**
  (`scripts/custom_screens.rpy:160-162`) — a debug action on an always-on overlay every player can press.
  Same for `debug_screen` (`custom_screens.rpy:169-186`).

- [x] **A8. Main menu exposes `Debug` and `Test Mode` buttons to every player** (`screens.rpy:404, 409`).
  Gate behind `config.developer` or a define.

- [x] **A9. Cosmetic / data bugs:**
  - Nurse bedroom named `'Queen Alexandra'` — missing "Bedroom" (`scripts/map.rpy:50`).
  - Dead condition `if current_checkpoint.label_id == "current" or True:` (`scripts/progress.rpy:772`).
  - Identical `if/else` branches printing the same "Previous Choices & Discoveries" title
    (`scripts/progress.rpy:752-761`).

---

## B. Architecture & robustness (highest long-term value)

- [x] **B1. Checkpoint × `all_menus` deep-copy = save bloat + per-choice hitching.**
  `add_checkpoint` (`scripts/characters.rpy:643`) does `copy.deepcopy(all_menus)` — every menu object ever
  created — into every checkpoint; checkpoints accumulate for the whole session inside `CharacterDetails`,
  which is pickled into **every autosave**, and autosave fires on every committed choice with `block=True`
  (`scripts/custom_menus.rpy:112-113`). Late-game this means growing save files and a visible pause per choice.
  Fix idea: store only the *dynamic* state (per-menu dict of `{choice_redirect: hidden/already_chosen}`)
  instead of whole `TimedMenu` object graphs; adapt the restore path in `start_again`
  (`scripts/custom_functions.rpy:405-416`) to overlay that state onto menus rebuilt from code.

- [x] **B2. Menu caching blocks content patches.** `run_menu` swaps a freshly constructed `TimedMenu` for the
  cached one in `all_menus` (`scripts/custom_menus.rpy:22-25`), so once a menu exists in a player's save,
  edited text/choices/conditions in code never reach that player. Same fix as B1: rebuild menus from code
  each time, overlay saved dynamic state.

- [x] **B3. Save forward-compatibility.** Nearly all UI state (`seen_tutorial_*`, `all_menus`, `current_room`,
  `tutorial_steps_*`, …) is created by runtime `python:` blocks in `init_technical_variables`
  (`script.rpy:290+`) instead of `default`. Adding any new variable there breaks existing testers' saves
  (AttributeError on Continue) because `start` never re-runs. Migrating to `default` statements is mechanical
  and removes a whole failure class.

- [ ] **B4. Fixed menu-nesting depth of 5** — `selected_choice = [None]*5` (`script.rpy:174`); a 6-deep menu
  chain raises IndexError with no useful message. Also `run_menu` re-displays via recursive
  `call run_menu(current_menu, change_level=False)` (`scripts/custom_menus.rpy:144`), growing the Ren'Py call
  stack once per committed choice until the menu closes. A `while` loop over `is_valid()` would be flatter,
  rollback-friendlier, and remove the `change_level` gymnastics.

- [x] **B5. `eval`-driven indirection where lookups exist:**
  - `eval(character_choice + "_details")` (`scripts/characters.rpy:97`) despite `get_char()` existing 12 lines below.
  - `eval(current_storyline.text_id + "_init_variables")` (`scripts/characters.rpy:687`).
  - Same pattern in `script.rpy:222` (test-mode start).
  A single registry dict (`character_registry['captain'] = (captain_details, captain_init_variables)`) removes
  typo risk. (Keeping *condition strings* on `TimedMenuChoice` is fine — they must pickle.)

- [x] **B6. Hotspot/choice matching logic duplicated** between `screen in_game_map_menu`
  (`scripts/map.rpy:208-245`) and `TimedMenu.display_choices` (`scripts/custom_menus.rpy:418-425`) — the
  "first match wins" rule is enforced twice by parallel code that must be kept in sync manually (a comment
  admits this). Extract one `find_choice_for_room(menu, room_id)` used by both.

- [x] **B7. Deepcopy work inside screens.** `current_status_checkpoint` (`scripts/progress.rpy:174`) and
  `active_checkpoint` (`scripts/progress.rpy:684-694`, including `deepcopy(all_menus)`) are built inline in
  screen bodies, which Ren'Py re-executes on every interaction/hover/prediction. Build them once in the
  opening action or in `on "show"`.

---

## C. Duplication & dead code

- [x] **C1. Map floor-arrow block copy-pasted 4×** (`scripts/map.rpy:139-175` and `263-313`) — a comment admits
  the `manor_map` screen is "a copy of in_game_map_menu because problem with var when use in sub screen".
  A shared `screen floor_arrows(...)` (or passing the variable name into one screen) kills ~80 lines.

- [x] **C2. Per-chapter map menus re-list ~25 rooms** with repeated condition-pair patterns (e.g. broken's
  livery/refused pairs duplicated 4×, `scripts/broken/Day 1/2_Evening/0_map_choices.rpy:51-58`). A small
  builder helper (`default_map_choices(prefix, overrides={...})`) would shrink each file and prevent drift;
  `scripts/TEMPLATE_map_choices.txt` shows this is currently done by copy-paste.

- [x] **C3. `character_card` repeats identical action logic** in its textbutton and imagebutton
  (`scripts/characters_screen.rpy:36-60`). Also `screen characters` sets `last_menu_screen` twice — once via
  `on "show"` and once via an inline `$` that runs on every render (`characters_screen.rpy:6-7`).

- [x] **C4. Overlay screens hardcode the same "hide me on these screens" list** —
  `version_screen` (`custom_screens.rpy:149`) and `bug_report_button` (`bug_report.rpy:224`). One helper
  function or shared define.

- [x] **C5. `char_list` (nested) + `char_list_flat` both maintained** (`scripts/characters.rpy:58-63`, its own
  TODO admits it); `get_char` if/elif chain (`characters.rpy:110-128`) → dict lookup.

- [ ] **C6. Progress timeline header built from ~8 vboxes of empty `text ""` spacers**
  (`scripts/progress.rpy:294-338`) — a grid with fixed `xsize` columns would be robust and half the code.

- [ ] **C7. Two near-identical notification paths** — `CharacterInformationList.unlock`
  (`characters.rpy:169-203`) vs `CharacterDescriptionHiddenList.unlock` (`characters.rpy:303-334`);
  the per-type notify text/sound could be one table.

- [x] **C8. Dead code volume** (delete, git keeps history):
  - Whole commented mobile-variant section, `screens.rpy:1531-1639`.
  - Old restart logic in `start_again`, `scripts/custom_functions.rpy:357-377`.
  - `show_character` / `hide_character`, `custom_functions.rpy:428-437`; `is_sub_menu_active`,
    `custom_functions.rpy:196-207`; `scan_pickle`, `script.rpy:46-66`.
  - Commented imagebutton remnants in `map.rpy` (4 blocks).
  - Duplicate empty style declarations: `style navigation_button` twice (`screens.rpy:364/371`),
    `style history_text is gui_text` twice (`screens.rpy:943/945`).
  - Unused `Hotspot.position` field (`map.rpy:367-380`).
  - `action_needed_fix` hack (`progress.rpy:577`, declared `script.rpy:441`) — use `NullAction()`.
  - Commented-out clock face-position experiments, `custom_screens.rpy:39-53`.

- [x] **C9. `screen map_information` shadows the `map_information` list variable** (`map.rpy:74/177`) —
  rename the screen (e.g. `map_annotations`).

---

## D. UX / polish ideas

- [x] **D1. Keyboard shortcuts bypass tutorial gating**: `K_m/K_p/K_c` (`scripts/custom_screens.rpy:199-201`)
  open Map/Progress/Characters even before the tutorials that unlock those nav buttons; the shortcuts are also
  undocumented in Help (its own TODO says so).

- [x] **D2. `*` marker convention in tooltips** (`scripts/map.rpy:231, 288, 321-326`) — encoding
  "already chosen" as a `*` inside the description string, then stripping it for display, is fragile;
  put a boolean on `Hotspot` instead.

- [ ] **D3. Discord webhook URL committed in source** (`scripts/bug_report.rpy:13`). Fine for a private tester
  build, but anyone with a shipped build (itch.io web included) can extract it and spam the channel.
  Rotate it before any public release and load it from an untracked/ignored file.

- [ ] **D4. i18n consistency**: template screens use `_()`, custom screens mostly don't
  ("Where do you want to go?", "Backstory", "Threads", "Nothing here" is wrapped but tutorial step texts,
  notify strings, etc. are not). Only worth unifying if translation is ever on the table.

- [ ] **D5. Fragile icon-marker handling in `custom_choice`** (`custom_screens.rpy:214-225`):
  `{{intuition}}`/`{{observation}}`/`{{object}}` string replacement chain plus the `"image=images" in btn_text`
  substring check. A small marker→icon table and an explicit flag would be sturdier.

- [ ] **D6. Quick-menu / preferences imagemaps use raw hotspot coordinates** (`screens.rpy:268-275, 751-754`) —
  expected in Ren'Py, but a short comment mapping coordinates → button names would help future edits.

- [ ] **D7. Accessibility**: imagebuttons and hotspots have no `alt` text, so self-voicing (the V key,
  advertised in Help) says nothing useful on the map/progress screens. Low priority.

---

## E. Suggested order of attack

1. **Quick wins (~1 session):** all of section A — delete dup `Room`, fix the `on "show"` tutorial bug,
   mutable defaults, hide debug buttons, help-screen placeholders.
2. **Save health:** B3 (`default` migration), then B1+B2 together (dynamic-state checkpoints — biggest payoff;
   needs care plus a save-reset/migration story for testers).
3. **Refactors that pay rent while writing the remaining characters (host/drunk):** C1–C2 (map screen +
   map-menu builder), B6 (single choice-matcher).
4. **Cleanup passes:** C5–C9 dead code, B7 deepcopy-in-screen, D items opportunistically.

## Application status (2026-07-06)

Everything ticked above was applied on branch `feature_fable_improvements`. Implementation notes:

- **B1/B2 mechanism:** `TimedMenu.templates` (class attribute, never pickled) records the latest
  instance constructed from code; `run_menu` refreshes the cached `all_menus` instance *in place*
  from that template (`refresh_menu_from_template`), preserving hidden/already-chosen/next-menu
  state keyed by `(room or text, redirect)`. Checkpoints now store a sparse
  `menus_state` snapshot (`capture_all_menus_state`) instead of `deepcopy(all_menus)`, and
  `copy_saved_variables` keeps `TimedMenu` values in `saved_variables` by reference.
  A new `label after_load` re-runs the pure construction labels (`<char>_config_menu` and the
  `*_map_menu` labels, whose name matches the menu id by convention) so menu edits also reach
  players who load an existing save. Old checkpoints with the legacy `.all_menus` deep copy are
  converted on the fly in `start_again`.
- **B2 residual:** a menu built in some *other* init label (not `*_config_menu` / `*_map_menu`,
  not constructed inline at its `run_menu` call site) would still be pinned in old saves until
  first reopened. No current menu falls in that gap; keep the label-name conventions when adding
  characters.
- **B5:** `character_selection` and the test-mode start now use `get_char()`;
  `get_init_checkpoint` uses `getattr(renpy.store, ...)` instead of `eval`. Condition strings on
  `TimedMenuChoice` intentionally stay strings (they must pickle).
- **A5:** `know_real_name` was removed outright (class + all 9 config files) — it was hard-coded
  off and never read.
- **A6:** the Help placeholder tabs got real body text (Clock & Time, Progress); the M/P
  shortcuts are documented under Controls.
- **C2:** `map_choice()` helper added in `map.rpy`; broken's two map menus converted as the
  reference; `TEMPLATE_map_choices.txt` updated. Converting the other characters' map files is
  mechanical follow-up.

**Deliberately not done (yet):**

- **B4** (fixed nesting depth 5 + `run_menu` self-call recursion) — reworking `run_menu`'s
  control flow into a loop touches rollback behaviour; do it in its own session with manual
  play-testing.
- **C6** (progress header spacer vboxes) and **C7** (merging the two notify paths) — visual /
  behavioural risk outweighs the cleanup value right now.
- **D3** — the Discord webhook is still in source; rotate it and move it out before any public
  release (user action).
- **D4–D7** — i18n pass, `custom_choice` icon-marker table, imagemap coordinate comments,
  `alt` text: opportunistic.

## Verification (when fixes land)

Launch the game and exercise: a map menu + sub-menu chain (time deduction, early exit, greyed choices);
Progress → chapter details (tutorial must *not* reopen every time); save → edit a menu's text in code →
load (edit should appear once B1/B2 land); restart-from-checkpoint; and run the JSON test plans under
`Murder/game/tests/`, which drive `run_menu` and `display_choices` directly.
