## File 1 — Moody alive, no suspicions

### Pre-unlocked threads
- (none)

### Path
- `tell_boxer_story` not unlocked -> Moody invites himself along, linear shooting in the woods.
- No host suspicions, so the extra "her outfit is perfect" paragraph is skipped.
- The "Next to her, stands Thomas Moody" paragraph fires (Moody is alive).
- Ends at `captain_ending_shot_in_woods`.

## File 2 — Moody alive, both host suspicions

### Pre-unlocked threads
- `captain_host_suspicion_name`
- `captain_host_suspicion_portrait`

### Path
- `tell_boxer_story` not unlocked -> Moody alive branch.
- Both suspicions fire the extra "her outfit is perfect" paragraph during the garden gathering.
- Moody paragraph also fires (alive branch).
- Ends at `captain_ending_shot_in_woods`.

## File 3 — Moody dead, no suspicions (silent luncheon auto)

### Pre-unlocked threads
- `tell_boxer_story`

### Path
- Moody dead branch -> Captain pairs with Lady + butler.
- No suspicions, so the confrontation menu is skipped and the `else` branch plays the "need more evidence" reflection automatically.
- Butler leaves, shots from the grove, doctor is found dead.
- Unlocks `captain_host_suspicion_shooting` during the hunt.
- Returns to main and jumps to `work_in_progress`.

## File 4 — Moody dead, both suspicions, hold tongue

### Pre-unlocked threads
- `tell_boxer_story`
- `captain_host_suspicion_name`
- `captain_host_suspicion_portrait`

### Path
- Moody dead branch with both suspicions active.
- Covers the "her outfit is perfect" paragraph and the "Whatever she conceals" paragraph inside the dead branch.
- At the confrontation menu, picks "Hold my tongue, for now" -> `captain_day2_hunt_silent_luncheon`.
- Silent luncheon plays, doctor is found shot in the grove.
- Returns to main and jumps to `work_in_progress`.

## File 5 — Moody dead, both suspicions, press her

### Pre-unlocked threads
- `tell_boxer_story`
- `captain_host_suspicion_name`
- `captain_host_suspicion_portrait`

### Path
- Moody dead branch with both suspicions active.
- At the confrontation menu, picks "Press her on who she really is" -> `captain_day2_hunt_confront_host`.
- Captain interrogates Lady Claythorn, butler strangles him from behind.
- Ends at `captain_ending_strangled`.
