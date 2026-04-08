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

| Code name | Full name | Role |
|-----------|-----------|------|
| `lad` | Ted Harring | Hero, petty thief, raised in orphanage |
| `psychic` | Amelia Baxter | The killer; flowery language |
| `doctor` | Daniel Baldwin | Opium addict; stole the Psychic's baby |
| `captain` | Sushil Sinha | Formal Indian officer; noble ancestry |
| `nurse` | Rosalind Marsh | Pseudo-villain; ratted out the Psychic |
| `drunk` | Samuel Manning | Defence lawyer; mostly incoherent |
| `broken` | Thomas Moody | Imposter wearing a mask; amateur sleuth |
| `host` | Lady Claythorn | Out-of-work actress hired to run the manor |

The **Psychic** is the killer. The **Broken Face** is the first victim (killed Night 1 when the Psychic realises he is not the officer she loved).

### Unlock Order

Lad → Doctor / Psychic → Nurse / Broken → Captain / Drunk → Host → Final run  
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
