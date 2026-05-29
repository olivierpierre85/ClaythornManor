# Captain — Sunday Morning (An Empty Manor)

The morning branches on `confide_in_nurse` (set Saturday evening).

| Plan | Threads preset | Path covered |
| ---- | -------------- | ------------ |
| `setup_captain_sunday_morning_1` | none | **Explore path, minimal.** Waits for the others straight away (no rooms searched). Manning is never checked, so the captain and the others discover his body together (`common_day3_morning_lad_psychic_captain_death_manning`), then on to the afternoon. |
| `setup_captain_sunday_morning_2` | `petrol_tin_in_shed` | **Explore path, full sweep.** Visits the garage (finds the car, sets `seen_car`) and Mr Manning's room (sets `day3_morning_drunk_checked`), then waits for the others. With petrol already found, this is the only morning path that carries `seen_car` + `petrol_tin_in_shed` into the afternoon car branch. |
| `setup_captain_sunday_morning_3` | `confide_in_nurse` | **Nurse path, hide.** Miss Marsh fetches him; they go to ground in the butler's room and wait the morning out, then come down in the afternoon. |
| `setup_captain_sunday_morning_4` | `confide_in_nurse` | **Nurse path, leave early.** They try to quit the house at once, run into Mr Harring and Miss Baxter, take the old car, and are ambushed on the road → `car_ambush` ending (terminal). |
