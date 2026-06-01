# Captain — Sunday Morning (An Empty Manor)

The morning branches on `confide_in_nurse` (set Saturday evening).

| Plan | Threads preset | Path covered |
| ---- | -------------- | ------------ |
| `setup_captain_sunday_morning_1` | none | **Explore path, minimal.** Waits for the others straight away (no rooms searched). Manning is never checked, so the captain and the others discover his body together (`common_day3_morning_lad_psychic_captain_death_manning`), then on to the afternoon. |
| `setup_captain_sunday_morning_2` | `petrol_tin_in_shed` | **Explore path, full sweep.** Visits the garage (finds the car, sets `seen_car`), the garden (already holds the petrol — the "already found on Saturday" branch) and Mr Manning's room (sets `day3_morning_drunk_checked`), then waits for the others. Carries `seen_car` + `petrol_tin_in_shed` into the afternoon car branch. |
| `setup_captain_sunday_morning_3` | `confide_in_nurse` | **Nurse path, hide.** Miss Marsh fetches him; they go to ground in the butler's room and wait the morning out, then come down in the afternoon. |
| `setup_captain_sunday_morning_4` | `confide_in_nurse` | **Nurse path, "leave" (false choice).** Miss Marsh cannot face the road and admits she is unwell, so the captain yields and they go to ground after all — falls through to the hide sequence, then comes down in the afternoon. |
| `setup_captain_sunday_morning_5` | none | **Explore path, find the petrol on Sunday.** Visits the garage first (the car, no petrol yet — the "dead weight" branch, sets `seen_car`), then the garden, where with the staff gone he opens the locked shed with the master key and discovers the petrol tin (sets `petrol_tin_in_shed`). Waits for the others. This is the second chance for a player who missed the shed on Saturday evening to still reach the afternoon car branch. |
