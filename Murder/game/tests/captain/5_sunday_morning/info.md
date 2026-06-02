# Captain — Sunday Morning (An Empty Manor)

The morning first branches on `confide_in_nurse` (set Saturday evening):
**nurse path** (Miss Marsh fetches him) or **explore path** (he walks the house alone).

On the explore path, the meeting in the tea room then branches independently on two
flags the captain may have set during his solo round of the map:

- `day3_morning_drunk_checked` — set by visiting **Mr Manning's room** (`captain_day3_morning_bedroom_drunk`)
- `day3_morning_nurse_checked` — set by visiting **Miss Marsh's room** (`captain_day3_morning_bedroom_nurse`)

This gives a 2×2 of meeting outcomes, all four of which must be exercised:

| `drunk` | `nurse` | Manning | Marsh | Wrap-up | Covered by |
| :-----: | :-----: | ------- | ----- | ------- | ---------- |
| F | F | discovered together (`death_manning`) | searched together (`search_nurse` → `marsh_empty`) → `search_report` | `deaths_end` | plans 1, 5 |
| T | F | captain reports it | searched together (`search_nurse` → `marsh_empty`) → `search_report` | `deaths_end` | **plan 6** |
| F | T | discovered together (`death_manning`) | captain reports it | `deaths_end` | **plan 7** |
| T | T | captain reports it | captain reports it | `deaths_end` | plan 2 |

| Plan | Threads preset | Path covered |
| ---- | -------------- | ------------ |
| `setup_captain_sunday_morning_1` | none | **Explore path, minimal.** Waits for the others straight away (no rooms searched). Manning is never checked, so the captain and the others discover his body together (`common_day3_morning_lad_psychic_captain_death_manning`), then on to the afternoon. |
| `setup_captain_sunday_morning_2` | `petrol_tin_in_shed` | **Explore path, full sweep.** Visits the garage (finds the car, sets `seen_car`), the garden (already holds the petrol — the "already found on Saturday" branch), Mr Manning's room (sets `day3_morning_drunk_checked`), his own room, and Miss Marsh's room (opens it with the master key, sets `day3_morning_nurse_checked`), then waits for the others. Because both checks are set, at the meeting he reports both Manning's death and Marsh's empty room himself. Carries `seen_car` + `petrol_tin_in_shed` into the afternoon car branch. |
| `setup_captain_sunday_morning_3` | `confide_in_nurse` | **Nurse path, hide.** Miss Marsh fetches him; they go to ground in the butler's room and wait the morning out, then come down in the afternoon. |
| `setup_captain_sunday_morning_4` | `confide_in_nurse` | **Nurse path, "leave" (false choice).** Miss Marsh cannot face the road and admits she is unwell, so the captain yields and they go to ground after all — falls through to the hide sequence, then comes down in the afternoon. |
| `setup_captain_sunday_morning_5` | none | **Explore path, find the petrol on Sunday.** Visits the garage first (the car, no petrol yet — the "dead weight" branch, sets `seen_car`), then the garden, where with the staff gone he opens the locked shed with the master key and discovers the petrol tin (sets `petrol_tin_in_shed`). Waits for the others. This is the second chance for a player who missed the shed on Saturday evening to still reach the afternoon car branch. |
| `setup_captain_sunday_morning_6` | none | **Explore path, meeting combo `(drunk=T, nurse=F)`.** Visits only Mr Manning's room (sets `day3_morning_drunk_checked`, sees the body alone), then waits. At the meeting he reports Manning's death himself, but Miss Marsh's room is still unchecked, so the three go up and search it together (`search_nurse` → `marsh_empty` → `search_report`) before `deaths_end`. |
| `setup_captain_sunday_morning_7` | none | **Explore path, meeting combo `(drunk=F, nurse=T)`.** Visits only Miss Marsh's room (sets `day3_morning_nurse_checked`, finds it empty), then waits. At the meeting Manning is still unchecked, so they discover his body together (`death_manning`), then the captain reports Marsh's empty room himself, straight into `deaths_end` — no second search party. |
| `setup_captain_sunday_morning_8` | none | **Explore path, grand tour + time runs out.** Visits fifteen rooms at 10 min each (library, tea room, dining room, portrait gallery, billiard room, the five guest bedrooms, the four attic rooms, the kitchen), which drains `time_left` to exactly 0. The map closes itself, triggering the `if time_left <= 0` framing narration, then the meeting plays the `(F, F)` path. Covers the first-visit narration for those rooms (incl. the attic approach intro, the portrait-gallery "no portrait of the host" beat, and the storage-room lantern). **Relies on exact timing: 15 rooms × 10 min = 150.** |
| `setup_captain_sunday_morning_9` | none | **Explore path, basement + entrance hall.** Visits the scullery and the gun room (first-visit narration, basement intro), then leaves the map via the **Entrance Hall** choice (`early_exit`), which covers its narration without exhausting the clock. Meeting plays the `(F, F)` path. |

## Remaining minor gaps (revisit / thread-gated narration)

These are low-priority "already seen this" branches not yet exercised; add later if the coverage report flags them:

- `captain_day3_morning_library` with `captain_host_suspicion_name` unlocked ("I have already read what I needed").
- `captain_portrait_gallery_default` / attic / gun-room **revisit** text (the "already searched" branches — need the room visited twice in one plan, or its `saved_variables` flag preset).
- `captain_day3_morning_garage` / `_garden` are both covered (plans 2 and 5 give both petrol states).
