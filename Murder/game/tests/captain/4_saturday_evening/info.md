## File 1 — Confront the host, accept confinement, burn

### Pre-unlocked threads
- `captain_host_suspicion_name`
- `captain_host_suspicion_portrait`
- `captain_host_suspicion_shooting`

### Path
- All three host suspicions trigger the confrontation menu after the Manning discussion.
- Picks "Send the butler with Manning, and challenge her" -> `captain_day2_evening_confront_host`.
- Lady Claythorn confesses, the butler returns and produces a revolver.
- Picks "Accepts being confined" -> `captain_day2_evening_butler_offer_confine`.
- Captain is locked in his bedroom, wakes to smoke under the door, the manor burns.
- Ends at `captain_ending_burned`.

## File 2 — Confront the host, lunge for the gun, shot

### Pre-unlocked threads
- `captain_host_suspicion_name`
- `captain_host_suspicion_portrait`
- `captain_host_suspicion_shooting`

### Path
- Same setup as File 1; suspicions unlock the confrontation menu.
- Picks "Send the butler with Manning, and challenge her" -> `captain_day2_evening_confront_host`.
- Lady Claythorn confesses, the butler returns and produces a revolver.
- Picks "Lunge at him and grab the gun" -> `captain_day2_evening_butler_offer_attack`.
- Captain reads the butler's competence with the weapon but charges anyway, and is shot before closing the distance.
- Ends at `captain_ending_shot_butler`.

## File 3 — Suspicions, take Manning up, confide in nurse and lad, accuse the host

### Pre-unlocked threads
- `captain_host_suspicion_name`
- `captain_host_suspicion_portrait`
- `captain_host_suspicion_shooting`

### Path
- Confrontation menu offered; picks "Take Manning up myself" -> `captain_day2_evening_normal_escort` (covers the normal escort + butler key narration).
- Dinner menu picks "Speak to Miss Baxter" -> `captain_day2_dinner_psychic`.
- Map menu picks "Look in on the billiard room" -> `captain_day2_evening_billiard_room`.
- Six successive "Wait and see who comes" choices walk the captain through every billiard slot:
  - 21:00–21:20 -> `captain_day2_evening_billiard_room_nurse_with_suspicions`; nurse menu picks "Tell her about your doubts" -> `_nurse_agree` (unlocks `confide_in_nurse`).
  - 21:20–21:40 -> `captain_day2_evening_billiard_room_empty_1`.
  - 21:40–22:00 -> `captain_day2_evening_billiard_room_lad_with_suspicions`; lad menu picks "Tell him about your doubts" -> `_lad_agree` (unlocks `confide_in_lad`).
  - 22:00–22:20 -> `captain_day2_evening_billiard_room_empty_2`.
  - 22:20–22:40 -> `captain_day2_evening_billiard_room_empty_3`.
  - 22:40–23:00 -> `captain_day2_evening_billiard_room_host_with_suspicions`; host menu picks "Confront her with what I know" -> `_host_accuse`.
- Time runs out, the map menu closes on its own, and `confide_in_lad` routes the captain to `captain_ending_throat_cut`.

## File 4 — No suspicions, normal evening through every billiard slot

### Pre-unlocked threads
- (none)

### Path
- No suspicions -> the confrontation menu does not appear; the captain auto-runs `captain_day2_evening_normal_escort`.
- Dinner menu picks "Speak to Miss Baxter" -> `captain_day2_dinner_psychic`.
- Map menu picks "Look in on the billiard room" -> `captain_day2_evening_billiard_room`.
- Six successive waits cycle through the no-suspicion slots (no sub-menus open):
  - 21:00–21:20 -> `_nurse_no_suspicions` (auto-dismiss path).
  - 21:20–21:40 -> `_empty_1`.
  - 21:40–22:00 -> `_lad_no_suspicions` (auto-dismiss path with the hypothesis_drunk shared dialogue).
  - 22:00–22:20 -> `_empty_2`.
  - 22:20–22:40 -> `_empty_3`.
  - 22:40–23:00 -> `_host_no_suspicions` (the captain swallows the thin travelling-coat excuse).
- Time runs out; the captain falls through to `captain_day3_morning`.

## File 5 — Suspicions, silent dinner, dismiss nurse and lad, let the host go

### Pre-unlocked threads
- `captain_host_suspicion_name`
- `captain_host_suspicion_portrait`
- `captain_host_suspicion_shooting`

### Path
- Confrontation menu picks "Take Manning up myself" -> `captain_day2_evening_normal_escort`.
- Dinner menu picks "Say nothing, eat in silence" (covers the silent-dinner narration).
- Map menu picks the billiard room and waits through all six slots:
  - 21:00–21:20 -> `_nurse_with_suspicions`; nurse menu picks "Keep pretending everything is fine" -> `_nurse_dismiss` (manual-dismiss branch and the shared captain<->nurse "two deaths" exchange).
  - 21:20–21:40 -> `_empty_1`.
  - 21:40–22:00 -> `_lad_with_suspicions`; lad menu picks "Keep pretending everything is fine" -> `_lad_dismiss` (manual-dismiss branch and the shared captain<->lad dialogue).
  - 22:00–22:20 -> `_empty_2`.
  - 22:20–22:40 -> `_empty_3`.
  - 22:40–23:00 -> `_host_with_suspicions`; host menu picks "Let her go and say nothing" -> `_host_silent`.
- `confide_in_lad` is never set; time runs out and the captain falls through to `captain_day3_morning`.

## File 6 — Map exploration: attic, garden/shed, bedrooms

### Pre-unlocked threads
- (none)

### Path
- Dinner menu picks "Speak to Miss Baxter" so the dinner conversation runs once.
- Map menu visits: storage (unlocks the lantern), garden with lantern -> outbuilding (unlocks `garden_shed_locked` and the petrol tin via the master key), storage again (lantern-already-have branch), butler's room (cabinet inspection), butler's room again (already-seen branch), footmen's room (rejection letter), maids' room (actress photograph), then bedrooms for Miss Baxter, Doctor Baldwin, Mr Manning, Mr Harring and Mr Moody.
- Time runs out after the last bedroom; the map closes naturally and the captain falls through to `captain_day3_morning`.

## File 7 — Map exploration: first floor, downstairs, gallery and library revisits

### Pre-unlocked threads
- `captain_host_suspicion_name`
- `captain_host_suspicion_portrait`

### Pre-set saved variables
- `visited_library = true`

### Path
- Dinner menu picks "Say nothing, eat in silence".
- Map menu visits: kitchen (downstairs default; the four downstairs choices are coalesced after the first), tea room, dining room, entrance hall, garden (no-lantern branch: captain goes out, spots the shed, turns back without approaching), portrait gallery (revisit, with `captain_host_suspicion_portrait` already unlocked), library (revisit, with `captain_host_suspicion_name` already unlocked), Miss Marsh's room and Lady Claythorn's room.
- "Retire for the night" closes the chapter.
- Covers the revisit branches of the library and gallery, the no-lantern garden text, and the small bedrooms skipped in File 6.

## File 8 — Billiard re-entry, sherry, attic revisits

### Pre-unlocked threads
- (none)

### Path
- Dinner menu picks "Speak to Miss Baxter".
- Map menu visits storage first to pick up the lantern, then dips into the billiard room early to cover the "Pour a glass of sherry" choice and a wait that resolves to `_nurse_no_suspicions` before leaving via "Leave the room" (early exit).
- Back on the map, the captain visits the footmen's room twice and the maids' room twice to exercise the already-visited branches for both attic dormitories.
- The captain then returns to the billiard room, which now triggers the re-entry narration ("I am back in the billiard room. The chairs sit much as I left them.") before a final wait resolves to `_host_no_suspicions`.
- Time runs out, the map closes naturally and the captain falls through to `captain_day3_morning`.
