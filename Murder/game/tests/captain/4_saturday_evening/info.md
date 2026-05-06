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

## File 3 — Suspicions, take Manning up, accuse the host in the billiard room

### Pre-unlocked threads
- `captain_host_suspicion_name`
- `captain_host_suspicion_portrait`
- `captain_host_suspicion_shooting`

### Path
- Confrontation menu is offered; picks "Take Manning up myself" -> `captain_day2_evening_normal_escort` (covers the normal escort + butler key narration).
- Dinner menu picks "Speak to Miss Baxter" -> `captain_day2_dinner_psychic`.
- Map menu picks "Look in on the billiard room" -> `captain_day2_evening_billiard_room`.
- Three "Wait and see who comes" choices in succession bring in Miss Marsh (nurse), Mr Harring (lad), then Lady Claythorn (host).
- With all three suspicions active, the lad arrival opens the agree/dismiss menu; picks "Tell him he is right to be uneasy" -> `captain_day2_evening_billiard_room_lad_agree`.
- With all three suspicions active, the host arrival opens the confront menu; picks "Confront her with what I know" -> `captain_day2_evening_billiard_room_host_accuse`.
- Captain leaves the billiard room and the chapter wraps up normally.

## File 4 — No suspicions, normal evening with billiard room visit

### Pre-unlocked threads
- (none)

### Path
- No suspicions -> the confrontation menu does not appear; the captain auto-runs `captain_day2_evening_normal_escort`.
- Dinner menu picks "Speak to Miss Baxter" -> `captain_day2_dinner_psychic`.
- Map menu picks "Look in on the billiard room" -> `captain_day2_evening_billiard_room`.
- Three waits cycle through nurse, lad and host. With no suspicions, the lad arrival auto-runs the dismiss path (no menu) and the host arrival skips the confront menu — the captain swallows her thin "turn outside" excuse.
- Covers the no-suspicions branch of the host billiard scene, the auto-dismiss branch of the lad billiard scene, and the dinner narration with no host suspicions.

## File 5 — Suspicions, take Manning up, let the host go in silence

### Pre-unlocked threads
- `captain_host_suspicion_name`
- `captain_host_suspicion_portrait`
- `captain_host_suspicion_shooting`

### Path
- Confrontation menu picks "Take Manning up myself" -> `captain_day2_evening_normal_escort`.
- Dinner menu picks "Say nothing, eat in silence" (covers the silent dinner branch).
- Map menu picks the billiard room and the captain waits through the three slots.
- With suspicions active, the lad arrival opens the agree/dismiss menu; picks "Hold the line — nothing is amiss" -> `captain_day2_evening_billiard_room_lad_dismiss` (covers the manual-dismiss branch and the shared captain↔lad dialogue).
- At the host arrival the confront menu picks "Let her go and say nothing" -> `captain_day2_evening_billiard_room_host_silent`.
- Captain leaves the billiard room and the chapter wraps up normally.

## File 6 — Map exploration: attic, garden/shed, bedrooms

### Pre-unlocked threads
- (none)

### Path
- Dinner menu picks "Speak to Miss Baxter" so the dinner conversation runs once.
- Map menu visits: storage (unlocks the lantern), garden with lantern -> shed (unlocks the petrol tin), garden again (already-seen branch), storage again (lantern-already-have branch), butler's room (cabinet inspection), butler's room again (already-seen branch), footmen's room (rejection letter), maids' room (actress photograph), then bedrooms for Miss Baxter, Doctor Baldwin, Mr Manning, Mr Harring and Mr Moody.
- "Retire for the night" closes the chapter once the time runs out.

## File 7 — Map exploration: first floor, downstairs, gallery and library revisits

### Pre-unlocked threads
- `captain_host_suspicion_name`
- `captain_host_suspicion_portrait`

### Pre-set saved variables
- `visited_library = true`

### Path
- Dinner menu picks "Say nothing, eat in silence".
- Map menu visits: kitchen (downstairs default; the four downstairs choices are coalesced after the first), tea room, dining room, entrance hall, garden (no lantern branch), portrait gallery (revisit, with `captain_host_suspicion_portrait` already unlocked), library (revisit, with `captain_host_suspicion_name` already unlocked), Miss Marsh's room and Lady Claythorn's room.
- "Retire for the night" closes the chapter.
- Covers the revisit branches of the library and gallery, the no-lantern garden text, and the small bedrooms skipped in File 6.
