# Claythorn Manor — Claude Guide

## Project Overview

A Ren'Py visual novel set in a Scottish manor in **1924**. The player investigates a murder mystery by playing multiple characters across three days (Friday–Sunday). Each character has its own storyline and perspective; unlocking information in one character's path opens routes in another's.

**Platform**: Ren'Py  
**Primary source folder**: `Murder/game/scripts/`  
**Style & coding rules**: `.claude/rules/grammar-style.md` and `.claude/rules/renpy-structure.md` (loaded automatically — do not repeat their contents here)

---

## Story & Characters

For full character backstories, motivations, and relationships see:
- **[docs/game_story/story_characters.md](docs/game_story/story_characters.md)** — Complete backstories, character bios, and the relationship matrix
- **[docs/game_story/arrivals_timeline.md](docs/game_story/arrivals_timeline.md)** — Who arrives when on Day 1
- **[docs/game_story/locations_objects.md](docs/game_story/locations_objects.md)** — Rooms, interactive objects, and which threads they unlock
- **[docs/game_story/unlock.md](docs/game_story/unlock.md)** — Character unlock order and dependencies (Mermaid graph)
- **[docs/game_story/day3_poisoning_chart.md](docs/game_story/day3_poisoning_chart.md)** — Day 3 death/poisoning timeline
- **[docs/game_story/characters_path/](docs/game_story/characters_path/)** — Per-character flow diagrams (currently: lad)

### Quick Reference — Characters

| Code name | Full name      | Role                                       |
| --------- | -------------- | ------------------------------------------ |
| `lad`     | Ted Harring    | Hero, petty thief, raised in orphanage     |
| `psychic` | Amelia Baxter  | The killer; flowery language               |
| `doctor`  | Daniel Baldwin | Opium addict; stole the Psychic's baby     |
| `captain` | Sushil Sinha   | Formal Indian officer; noble ancestry      |
| `nurse`   | Rosalind Marsh | Pseudo-villain; ratted out the Psychic     |
| `drunk`   | Samuel Manning | Defence lawyer; mostly incoherent          |
| `broken`  | Thomas Moody   | Imposter wearing a mask; amateur sleuth    |
| `host`    | Lady Claythorn | Out-of-work actress hired to run the manor |


### Unlock Order

Details and cross-character prerequisites: [docs/game_story/unlock.md](docs/game_story/unlock.md)

---

## Script Structure

```
Murder/game/scripts/
  <character>/
    <character>_config.rpy          # CharacterDetails object, threads, endings
    <character>_generic_choices.rpy # Shared conversation menus for this character
    Day 1/
      1_Afternoon/1_main.rpy
      2_Evening/1_main.rpy
    Day 2/ ...
    Day 3/ ...
  _common/                          # Shared labels used across characters
```

- Chapter labels follow the pattern `<character>_day<N>_<period>` (e.g. `captain_day1_evening`).
- Inner-monologue narration uses `"""triple quotes"""`.
- Blank line after every dialogue or narration sentence.
- Shared dialogue blocks must be extracted into a named label and `call`ed — never duplicated.

### Cross-character shared dialogue (`_common/`)

Many scenes are witnessed by multiple characters (e.g. the dinner speech, a guest collapsing, a confrontation in the hall). When the same or near-identical dialogue/narration appears in more than one character's script, it must be moved to a label in `_common/` and `call`ed from each character's script.

- Name the label descriptively: `common_day1_dinner_host_speech`, `common_day2_morning_body_discovered`, etc.
- Every label in `_common/` must end with `return`.
- When writing new scenes, check `_common/` first — the scene may already exist.
- When editing an existing scene that appears in multiple characters, locate the shared label in `_common/` and edit it there; do not patch each character file individually.

### Key variables

```renpy
# Threads (player-visible, affect branching / endings)
$ captain_details.threads.unlock('captain_lie_boxer')
$ captain_details.threads.is_unlocked('captain_lie_boxer')

# Saved variables (internal UI / state flags)
$ captain_details.saved_variables['attic_visited'] = True

# Room change
$ change_room('bedroom_captain')
$ change_room('bedroom_captain', dissolve)

# Music
$ play_music('mysterious', 2)
$ stop_music()
```

Cheat sheet for less common patterns: [docs/_code_cheat_sheet.md](docs/_code_cheat_sheet.md)

---

## Progress Screen & Checkpoints

Each character needs a `<char>_config_progress.rpy` file that defines the progress row layout and dev checkpoints.

### File structure

```
<char>_config_progress.rpy   # defines <char>_progress and <char>_test_checkpoints
```

`<char>_config.rpy` must:
1. `call <char>_config_progress` **before** the `python:` block that creates `CharacterDetails`
2. Pass `progress = <char>_progress` and `test_checkpoints = <char>_test_checkpoints` to `CharacterDetails`

### Progress rows (`<char>_progress`)

A list of rows; each row is a list of `Chapter` objects left-to-right:

```python
captain_progress = [
    [
        Chapter(image_checkpoint_start, "start", "captain_introduction", "friday_afternoon"),
        Chapter(image_checkpoint_right, "checkpoint", "captain_day1_evening", "friday_evening"),
        Chapter(image_checkpoint_empty),   # placeholder for unwritten chapters
        ...
        Chapter(image_ending_question, "ending", "poisoned", "end"),
    ],
]
```

- Argument order: `(image, chapter_type, label, name)`
- `label` — the Ren'Py label that `add_checkpoint(label)` is called with in the chapter script
- `name` — the `chapter_index` key (e.g. `"friday_evening"`); used for display text and completion checks
- Always fill all 8 columns (start + 6 chapters + ending) even for unwritten chapters — use `Chapter(image_checkpoint_empty)` as placeholders

### Test checkpoints (`<char>_test_checkpoints`)

Maps chapter keys to a list of checkpoint configs used by the debug mode:

```python
captain_test_checkpoints = {
    'friday_afternoon': [
        {"label": "captain_introduction", "threads": {}},
    ],
    'friday_evening': [
        {"label": "captain_day1_evening", "threads": {}},
        {"label": "captain_day1_evening", "threads": {"captain_host_suspicion_name": True}},
    ],
}
```

Only include chapters that have been written. The engine (`load_manual_checkpoints`) creates one `Checkpoint` per entry.

### Wiring into debug mode

After adding a new character's progress config, add `load_manual_checkpoints()` to `debug_choices.rpy` → `label init_debug`:

```renpy
$ current_character = captain_details
$ current_storyline = captain_details
call unlock_captain
$ captain_details.load_manual_checkpoints()   # ← required for breakpoints to appear
```

### image_file is mandatory on all threads

Every `CharacterInformation` item that can appear in the progress details screen **must** have `image_file` set — `None` crashes the screen. Use a placeholder image (e.g. `"lord"`) until a proper image exists.

---

## Testing Framework

### Folder layout

```
Murder/game/tests/
  tests.rpy                    # Global testsuite setup (start/restart between cases)
  test_plan_runner.rpy         # ChapterAutoRunner engine (do not edit)
  <character>/
    <character>_tests.rpy      # Testsuite definition — one testcase per chapter
    <N>_<chapter_id>/
      info.md                  # Human-readable description of what each plan covers
      setup_<char>_<chap>_1.json
      setup_<char>_<chap>_2.json   # One file per path/scenario
      ...
```

### How it works

1. **`<character>_tests.rpy`** declares testcases using:
   ```renpy
   testcase friday_evening:
       python:
           test.run_chapter(captain_details, "friday_evening", "captain_day1_evening")
   ```
   Arguments: `(character_details_object, chapter_id_string, start_label_string)`

2. **`test.run_chapter`** automatically discovers all `.json` files in  
   `tests/<character_id>/<N>_<chapter_id>/` and runs them sequentially within the same testcase.

3. **Each `.json` plan file** drives one playthrough:
   ```json
   {
     "start_label": "captain_day1_evening",
     "unlocked_threads": ["captain_lie_boxer"],
     "saved_variables": {},
     "choices": [
       {
         "menu": "captain_day1_evening_menu_id",
         "selected": "The choice text",
         "redirect": "target_label_name"
       }
     ]
   }
   ```
   - `unlocked_threads` — threads to pre-unlock before the chapter starts.
   - `saved_variables` — key/value pairs to set on `character.saved_variables`.
   - `choices` — ordered list of menu answers. Match by `redirect` first; fall back to `selected` text.
   - A chapter with no menus at all uses `"choices": []`.

4. **`info.md`** (optional but recommended) — one section per plan file describing the scenario covered (which branch, which map rooms visited, etc.). See `tests/nurse/1_friday_evening/info.md` for a good example.

### Adding tests for a new chapter

1. Create the folder: `tests/<character>/<N>_<chapter_id>/`  
   (Use the next available index number, matching the day/period order.)
2. Create at least one `.json` plan covering the happy path.
3. Add a `testcase` entry in `<character>_tests.rpy` (uncomment or add a new block).
4. To capture choice data from a real play-through, use the in-game testing recorder and export the JSON from `tests/testing_mode_choices/`.
5. Write an `info.md` documenting which scenarios each file covers.

### Running tests

Tests run inside Ren'Py's built-in test runner (not a separate CI tool). Launch the game in test mode via the Ren'Py launcher or `renpy.exe … --test`.

### Checking dialogue coverage

`Murder/check_test_dialogue_coverage.py` verifies that every dialogue and narration line in the game is exercised by at least one test plan. It compares `Murder/dialogue.tab` (the authoritative extract of all in-game text) against the `.txt` output files produced by the test runner.

**You must use this script instead of reading script files manually** to assess whether tests cover a chapter. Reading `.rpy` files to find gaps is slow and error-prone; the script does it accurately in one pass.

```bash
# Check one character (own scripts + _common labels that character calls)
python Murder/check_test_dialogue_coverage.py --character captain
```

**What is excluded from the character-specific check:**
- Other characters' scripts (only `scripts/<character>/` + relevant `_common/` labels are scanned)
- `*_generic_choices.rpy` and `*_generic_other_guests.rpy` — these files contain NPC dialogue triggered when *another* character is playing, so they will never appear in this character's own test output
- `_common/` labels that the character never `call`s or `jump`s to

**Interpreting the output:**

```
Scope:                    character=captain
Dialogue entries scanned: 549
Test lines collected:     1823
Covered:                  532
Missing:                  17

  game/scripts/captain/captain_generic_locations.rpy  (3 missing)
    [captain_library_default_...] The library is as I left it. ...
```

Each missing entry shows the Ren'Py identifier and a preview of the text. Add a new `.json` plan (or extend an existing one) to cover the missing branch, then re-run to confirm the count drops to zero.
