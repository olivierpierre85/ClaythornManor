# Doctor — Friday Evening (`doctor_day1_evening`)

The chapter opens in the tea room with `broken_generic_menu_doctor` (50-minute budget), then runs through Captain Sinha's arrival, the dinner gong, the dinner-table choice (`doctor_day1_evening` menu, 90-minute budget), and the post-dinner laudanum decision (`doctor_day1_evening_3`, 90-minute budget). After that comes `doctor_day1_evening_map_menu` (90-minute budget) for room exploration. The chapter ends with a flirt/book branching block before sleeping; the no-flirt-no-book fallback drops the doctor into `doctor_laudanum_death` for an automatic overdose.

The broken_generic budget (50 minutes) is too tight for a single-plan full Q&A, so the not-offended and offended branches are split across multiple plans.

## setup_doctor_friday_evening_1.json — Default narrative, mystery book sleep
- Skip broken_generic immediately.
- Dinner: ignore Ted Harring.
- Post-dinner: go down and meet the others.
- Map: tea room → library (mystery book) → portrait gallery → dining room → garden → entrance hall → Elizabeth I (psychic, talks) → George IV (drunk, no shot pre — auto not_enter else branch) → storage → William the Conqueror (lad, closed bedroom) → Go to sleep.
- End: `book_mystery` thread → reads the Christie novel and sleeps through to Saturday morning.

## setup_doctor_friday_evening_2.json — Broken not-offended round 1, apologise downstairs, no library book → overdose
- broken_generic round 1: weather (10), heroic_act → "Nod, but don't engage" (20), manor → "The war didn't change much for me" (20). Total 50, the menu auto-closes when time hits zero.
- Dinner: ignore Ted.
- Post-dinner: go down.
- Map: kitchen → "No, he clearly won't change his mind" → `doctor_downstairs_apologize`; library → "On second thought, I'd better not take anything"; Go to sleep.
- End: no flirt, no book → falls into `doctor_laudanum_death` → `doctor_ending_overdose`.

## setup_doctor_friday_evening_3.json — Broken not-offended round 2, full lad chat (leave it), flirt + opium book
- broken_generic round 2: background → "That's a very noble profession", room → "Me neither", other_guests → "Yes, it must be that". Total cost 30. Exit explicitly.
- Dinner: talk to Ted Harring → full `lad_generic_menu_doctor` Q&A: background → "No, let us just leave it at that"; "Why were you invited here?"; manor; age; room (Friday version); other_guests_friday_dinner. Exit.
- Post-dinner: go down.
- Map: kitchen → "Try flirting with him" → `doctor_downstairs_flirt` (`flirt` thread); library → opium book; billiard room (lad approaches; lad_generic exits since everything was already asked); Go to sleep.
- End: `flirt` + `book_opium` → footman knock scene (`footman_french_1`) and the long opium reading.

## setup_doctor_friday_evening_4.json — Offend Thomas Moody (path A), lad "sell to me", overdose
- broken_generic offences A:
  1. Background → "Did you have to change profession because of the war?" → "Wait? Really?" (offence 1)
  2. Manor → "Of course, the war changed everyone perspective" (offence 2)
  3. Heroic act → "What do you mean?" (offence 3 — unlocks `broken_offended` thread).
- Triggers the post-menu "Excuse me, I have something to do." block in main.rpy.
- Dinner: talk to Ted Harring → background → "I might have something to sell you" → `lad_generic_background_doctor_thief` (`thief` description). Exit lad menu.
- Post-dinner: **Stay here—this might be more... enjoyable** → `doctor_laudanum_death` → `doctor_ending_overdose`.

## setup_doctor_friday_evening_5.json — Offend Thomas Moody (path B), Go to sleep → overdose
- broken_generic offences B:
  1. Room → "I saw a Shakespeare's play about him" → `broken_generic_room_offended` (offence 1)
  2. Age (auto-offence 2)
  3. Other_guests → "I can think of another reason she was uneasy" → `broken_generic_other_guests_friday_offended` (offence 3 — unlocks `broken_offended`).
- "Excuse me" block fires.
- Dinner: ignore Ted.
- Post-dinner: go down → map opens → Go to sleep immediately.
- End: no flirt, no book → `doctor_laudanum_death` → `doctor_ending_overdose`.

## setup_doctor_friday_evening_6.json — Drunk's bedroom, leave manor, stay awake → burn ending
- Pre-set ending: `shot_by_drunk` (forces the timed `doctor_day1_evening_bedroom_drunk` menu and the "intrusive feeling" preamble).
- Map: George IV → **Follow your intuition** → enter bedroom_drunk (covers `drunk_letter` discovery, `drunk_letter` thread).
- bedroom_drunk_enter menu: **Do not risk your life — leave this place** → confronts the others in the billiard room, locked in by the captain.
- leave_manor menu: **I should stay awake to be safe** → `doctor_ending_burn`.

## setup_doctor_friday_evening_7.json — Drunk's bedroom, leave manor, sleep → overdose ending
- Same pre-set `shot_by_drunk` ending.
- Same path as plan 6 up to the leave_manor menu.
- leave_manor menu: **I know something that will help me sleep** → `doctor_laudanum_death` → `doctor_ending_overdose`.

## setup_doctor_friday_evening_8.json — Drunk's bedroom, stay; default overdose at end of chapter
- Same pre-set `shot_by_drunk` ending.
- bedroom_drunk_enter menu: **Do not risk losing the money — stay** → returns to map.
- Go to sleep → no flirt and no book unlocked → `doctor_laudanum_death` → `doctor_ending_overdose`.

## setup_doctor_friday_evening_9.json — Flirt with the footman, no book
- Skip broken_generic immediately.
- Dinner: ignore Ted.
- Post-dinner: go down.
- Map: kitchen → **Try flirting with him** → `doctor_downstairs_flirt` (`flirt` thread); Go to sleep.
- End: `flirt` unlocked but no book → footman knock scene (`footman_french_1`) followed by the no-book fallback ("It is quiet now, but my mind is at ease." / "I fall asleep easily.").
