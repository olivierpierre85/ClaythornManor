## File 1 — Alive branch, no suspicion

### Pre-unlocked threads
- (none)

### Path
- `tell_boxer_story` not unlocked -> `captain_day2_morning_breakfast_alive`
- Moody enters the dining room, Lady Claythorn announces the hunt.
- Covers the baseline intro narration (without the host-suspicion paragraph).

## File 2 — Alive branch, both host suspicions

### Pre-unlocked threads
- `captain_host_suspicion_name`
- `captain_host_suspicion_portrait`

### Path
- `tell_boxer_story` not unlocked -> `captain_day2_morning_breakfast_alive`
- Both suspicion threads active, so the extra intro paragraph about the hostess is shown.
- Moody arrives alive, hunt announcement proceeds as normal.

## File 3 — Death branch, both host suspicions

### Pre-unlocked threads
- `tell_boxer_story`
- `captain_host_suspicion_name`
- `captain_host_suspicion_portrait`

### Path
- `tell_boxer_story` unlocked -> `captain_day2_morning_breakfast_death`
- Hostess pulls the doctor aside (`common_day2_morning_host_to_doctor`).
- Captain exchanges greetings with Miss Baxter (`common_day2_morning_captain_psychic_greeting`).
- Host returns with the news of Moody's death (`common_day2_morning_host_death`, `common_day2_morning_host_death_doctor`).
- Both suspicion threads trigger the additional reflection paragraph after the doctor's verdict.
- Hunt announcement under the shadow of the death (`common_day2_morning_host_hunt`).
