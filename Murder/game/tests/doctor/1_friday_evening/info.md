# Doctor — Friday Evening (`doctor_day1_evening`)

The chapter opens in the tea room with `broken_generic_menu_doctor`, then runs through Captain Sinha's arrival, the dinner gong, the dinner-table choice (`doctor_day1_evening` menu), and the post-dinner laudanum decision (`doctor_day1_evening_3`). After that comes `doctor_day1_evening_map_menu` for room exploration. The chapter ends with a flirt/book branching block before sleeping; the no-flirt-no-book fallback drops the doctor into `doctor_laudanum_death` for an automatic overdose.

## setup_doctor_friday_evening_1.json — Default narrative, mystery book sleep
- Skip broken_generic immediately.
- Dinner: ignore Ted Harring.
- Post-dinner: go down and meet the others.
- Map: tea room → library (mystery book) → portrait gallery → dining room → garden → entrance hall → Elizabeth I (psychic, talks) → George IV (drunk, no shot pre — auto not_enter else branch) → storage → William the Conqueror (lad, closed bedroom) → Go to sleep.
- End: `book_mystery` thread → reads the Christie novel and sleeps through to Saturday morning.

## setup_doctor_friday_evening_2.json — Full broken & lad chats, flirt + opium book
- broken_generic full Q&A picking the **not-offended** branches everywhere (weather, background → noble, heroic_act → nod, manor → didn't change, room → me neither, other_guests → must be that). Skips the age question (which would auto-offend).
- Dinner: talk to Ted Harring → full lad_generic_menu_doctor (background, heroic_act, manor, age, room (Friday version), other_guests_friday_dinner).
- Map: kitchen → flirt with the footman (`flirt` thread) → library (opium book) → billiard room (lad joins, exits the lad_generic menu) → Go to sleep.
- End: `flirt` + `book_opium` → footman knock scene (`footman_french_1`) and the long opium reading.

## setup_doctor_friday_evening_3.json — Offend Thomas Moody, overdose ending
- broken_generic Q&A with three offences in a row to unlock the `broken_offended` thread:
  1. Background → "Did you have to change profession because of the war?" → "Wait? Really?" (1)
  2. Manor → "Of course, the war changed everyone perspective" (2)
  3. Heroic act → "What do you mean?" (3 — unlocks the thread; menu auto-closes since every option is gated on `not broken_offended`).
- Triggers the post-menu "Excuse me, I have something to do." block in main.rpy.
- Dinner: ignore Ted.
- Post-dinner: **Stay here—this might be more... enjoyable** → `doctor_laudanum_death` → `doctor_ending_overdose`.

## setup_doctor_friday_evening_4.json — Drunk's bedroom, leave manor, stay awake → burn ending
- Pre-set ending: `shot_by_drunk` (forces the timed `doctor_day1_evening_bedroom_drunk` menu and the "intrusive feeling" preamble).
- Map: George IV → **Follow your intuition** → enter bedroom_drunk (covers `drunk_letter` discovery, `drunk_letter` thread).
- bedroom_drunk_enter menu: **Do not risk your life — leave this place** → confronts the others in the billiard room, locked in by the captain.
- leave_manor menu: **I should stay awake to be safe** → `doctor_ending_burn`.

## setup_doctor_friday_evening_5.json — Drunk's bedroom, leave manor, sleep → overdose ending
- Same pre-set `shot_by_drunk` ending.
- Same path as plan 4 up to the leave_manor menu.
- leave_manor menu: **I know something that will help me sleep** → `doctor_laudanum_death` → `doctor_ending_overdose`.

## setup_doctor_friday_evening_6.json — Drunk's bedroom, stay; default overdose at end of chapter
- Same pre-set `shot_by_drunk` ending.
- bedroom_drunk_enter menu: **Do not risk losing the money — stay** → returns to map.
- Go to sleep → no flirt and no book unlocked → falls into the `else` branch in `doctor_day1_evening` → `doctor_laudanum_death` → `doctor_ending_overdose`.
