# Doctor — Saturday Afternoon (`doctor_day2_hunt`)

The chapter opens at 11:00 outside the manor with the doctor changing for the hunt. Opening narration branches on `drunk_letter` (suspicion of Manning) and `flirt` (Andrew vs the footman). After the butler splits the party, Manning insists on partnering with the doctor, and Ted asks to tag along. Control passes into `doctor_day2_hunt_accident` where the group walks into the forest and stops for luncheon. Forest narration branches on `flirt` again. If `drunk_letter` is unlocked the doctor faces a timed choice (`doctor_day2_hunt_accident`): **confront** Manning (jumps to `doctor_day2_evening`) or **ignore him** and chat with Ted; without `drunk_letter` the conversation with Ted runs unconditionally.

The Ted conversation opens `lad_generic_menu_doctor` with a 30-minute budget. The reflection that follows it branches on `book_opium`, `flirt`, and the default ("medicine"), then Manning shoots and the doctor dies. The closing narration branches on `book_opium` ("I would have managed to quit") versus the default ("this is likely how I was meant to go anyway"), and the chapter ends via `jump doctor_ending_shot_by_drunk` (i.e. `ending_generic`).

The 30-minute budget on the lad menu is too tight to exercise every branch in one plan, so coverage is split across multiple plans. `lad_generic_heroic_act_doctor` is gated behind the linked "Tell me more about yourself." choice having been picked once (which then hides it). `lad_generic_background_doctor` is cost 0 but opens a sub-menu costing 15 (cancel) or 30 (thief).

## setup_doctor_saturday_afternoon_1.json — Default narrative
- No threads pre-unlocked.
- Opening: default ("I can only hope he has sobered up.").
- Footman narration: "The footman is there as well."
- Manning partner exchange: default ("Well... no, of course not.").
- Forest narration: default footman, no drunk-letter timed menu.
- Lad menu picks: room (10) → manor (10) → age (10) → menu auto-closes at 0.
- Pre-death reflection: default ("I regret not taking my 'medicine'…") and default "I am roused from my stupor".
- `bored_by_lad` stays at 0, so the post-menu line is "After a short while, we're ready to keep going with the hunt."
- Closing: default ending narration ("this is likely how I was meant to go anyway.").

## setup_doctor_saturday_afternoon_2.json — Drunk letter, ignore Manning
- Pre-unlocked: `drunk_letter`.
- Opening: drunk_letter variant ("I must watch him carefully.").
- Manning partner exchange: drunk_letter narration ("He is too eager to join me.") and confident response.
- Forest narration: default footman, then the timed `doctor_day2_hunt_accident` menu fires.
- Timed menu: **Ignore him and talk with Ted Harring** → `doctor_day2_hunt_accident_lad_conversation`.
- Lad menu picks: "What do you think of the other guests?" (cost 0) → submenu picks Samuel Manning (10) → Sushil Sinha (10) → Lady Claythorn (10) → both menus auto-close at 0.
- Pre-death reflection: drunk_letter ("As I did this morning, I take care to keep Samuel Manning within my line of sight."), default ("I regret not taking my 'medicine'…"), drunk_letter ("I am lost in my thoughts when I hear Samuel Manning shout.").
- Death common: drunk_letter narration ("I allowed myself a moment of distraction…", "He avoids my gaze, feigning remorse.").
- `bored_by_lad` is incremented 3× by the sub-options, triggering the "Well, that was hardly the most stimulating conversation." narration.
- Closing: default ending narration.

## setup_doctor_saturday_afternoon_3.json — Drunk letter, confront Manning
- Pre-unlocked: `drunk_letter`.
- Opening / partner exchange: drunk_letter variants (same as plan 2).
- Forest: default footman, then the timed menu fires.
- Timed menu: **Confront the drunk man with a gun** → `doctor_day2_hunt_accident_confront_drunk`.
- Confront dialogue plays in full (unlocks `drunk_details.description_hidden.lie` and `wife`).
- Manning shoots himself in the struggle; chapter ends via `jump doctor_day2_evening` (chapter changes to `saturday_evening`).
- Lad menu and the post-menu reflection / death scene are not reached on this path.

## setup_doctor_saturday_afternoon_4.json — Flirt with the footman
- Pre-unlocked: `flirt`.
- Opening: default ("I can only hope he has sobered up.").
- Footman narration: flirt variant ("Andrew is there too.").
- Manning partner exchange: default response.
- Lad-tag-along: flirt narration ("Andrew stands at his side and gives me a meaningful look.").
- Forest narration: flirt variant ("I should like to speak further with Andrew…").
- No drunk-letter timed menu.
- Lad menu picks: "Tell me more about yourself." (cost 0) → submenu **No, let us just leave it at that** (cost 15) → main menu reopens with `lad_generic_heroic_act_doctor` now visible (linked-choice unlocked) → "Why were you invited here?" (cost 30) → menu closes.
- Pre-death reflection: flirt branch ("Despite my caution, my gaze is drawn again and again to Andrew…") — this only fires when `flirt` is set and `book_opium` is not.
- `bored_by_lad` stays at 0; "After a short while…" plays.
- Closing: default ending narration.

## setup_doctor_saturday_afternoon_5.json — Opium withdrawal
- Pre-unlocked: `book_opium`.
- Opening: default.
- Footman / partner exchange / lad-tag-along: default narration.
- Forest narration: default footman.
- No drunk-letter timed menu.
- Lad menu picks: "Tell me more about yourself." (cost 0) → submenu **I might have something to sell you** (cost 30, opens the thief variant `lad_generic_background_doctor_thief`) → both menus close at 0.
- Pre-death reflection: book_opium branch ("The fact is that I have begun to notice the first symptoms of withdrawal…").
- `bored_by_lad` stays at 0; "After a short while…" plays.
- Closing: book_opium ending narration ("Ironically, I truly believe I would have managed to quit this time.").
