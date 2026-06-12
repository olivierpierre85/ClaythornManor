# Doctor — Saturday Evening (`doctor_day2_evening`)

The chapter opens at 15:00 in the entrance hall as the party returns from the hunt with Samuel Manning's body. The captain takes charge, the doctor must explain what happened (`doctor_day2_evening_reason` menu — drunk vs silence). The doctor retires to his bedroom; the post-shock reflection branches on `book_opium` (he resists his vials) versus the default ("I think of the letter I found in Samuel Manning's room.") and adds an extra paragraph on `broken_unmasked` ("The image of Thomas Moody without his mask…"). The dinner gong then sounds. Lady Claythorn delivers her brief speech (`common_day2_evening_dinner_host`), and the doctor faces a 90-minute dinner menu (`doctor_day2_evening_dinner`) — talk to Ted Harring, talk to Rosalind Marsh, or sit in silence. The lad branch consumes time via `lad_generic_menu_doctor`; if `bored_by_lad > 1` after the conversation, the "hardly the most stimulating" line plays.

After dinner the chapter calls `doctor_day2_evening_exploration` (90-minute map menu). The opening narration there branches on `flirt`, `remember_nurse`, and `book_opium`. The map offers: a downstairs visit (maid blocks unless `flirt`, in which case the footman bedroom is unlocked), the standard ground-floor rooms, the bedrooms (most simply show the closed-door narration), the billiard room (Captain + bar), Samuel Manning's room (unlocks `burned_letter`), Thomas Moody's room (unmasks him if not already done), Rosalind Marsh's room (only the `remember_nurse` branch is meaningful; otherwise the doctor is turned away), the male servants room (entered only with `flirt` for a long footman scene that unlocks `footman_actor`), and "Go to sleep, alone". Two trust paths exit to Day 3: the captain mask conversation can lead to `trust_captain` and the nurse remember conversation can lead to `trust_nurse`. Without either, the doctor sleeps alone and dies (`doctor_ending_throat_cut`).

Map exit handling: the exploration label checks `trust_captain` / `trust_nurse` after the menu closes. If neither is set, it prints "It's getting very late, I should go to bed." and jumps to `doctor_day2_evening_sleep_alone` — the same label reached by picking "Go to sleep, alone" directly (which skips that line). Both paths end at `doctor_ending_throat_cut`.

The dinner menu id is `doctor_day2_evening_dinner` and the nurse-bedroom sleep menu id is `doctor_day2_evening_bedroom_nurse_sleep` (both were renamed from inherited / mis-named ids that collided with other menus).

## setup_doctor_saturday_evening_1.json — Default narrative, drunk reason, run-out-of-time death
- No threads pre-unlocked.
- Reason: **Say he was just too drunk** → `doctor_day2_evening_reason_drunk`.
- Bedroom reflection: default else branch (no `book_opium`, no `broken_unmasked`).
- Dinner: **Enjoy the creepy silence** (early exit).
- Map (90 min): tea_room (10), dining_room (10), garden (10), entrance_hall (10), portrait_gallery (10), bedroom_lad (10), library (10), bedroom_captain (10), bedroom_host (10) → 90 used, menu auto-closes.
- Bedroom-closed narration covers both branches: bedroom_captain triggers the first-visit text, bedroom_host triggers the "Nobody is here either." repeat text.
- Exploration falls through with no trust thread → "It's getting very late, I should go to bed." → `doctor_day2_evening_sleep_alone` → `doctor_ending_throat_cut`.

## setup_doctor_saturday_evening_2.json — Opium + silence reason, lad dinner (bored), bar/drunk/broken visits, sleep alone
- Pre-unlocked: `book_opium`.
- Reason: **Say nothing** → `doctor_day2_evening_reason_silence` → `doctor_day2_evening_reason_drunk_silent`.
- Bedroom reflection: `book_opium` branch ("I pace the room, my hands still trembling…").
- Dinner: **Talk to Ted Harring** → `lad_generic_menu_doctor` → "What do you think of the other guests?" submenu picks Samuel Manning (dead variant, +1 bored) → Sushil Sinha (+1) → Lady Claythorn (+1) → "Talk about something else" exits the submenu → "You don't have anymore questions for him" exits the lad menu. After return, `bored_by_lad = 3` triggers the "hardly the most stimulating" line and resets to 0. Dinner: **Enjoy the creepy silence**.
- Exploration narration: `book_opium` paragraph ("I also have to manage symptoms of withdrawal…").
- Map (90 min): bedroom_drunk (20, unlocks `burned_letter`) → bedroom_broken (10, no `broken_unmasked`, removes the mask via `doctor_day2_behind_the_mask`) → billiard_room (0, first visit) → bar (10, with the `book_opium` "free myself from opium entirely" reflection) → "Leave the room" → "Go to sleep, alone" (early exit) → `doctor_ending_throat_cut`.

## setup_doctor_saturday_evening_3.json — Broken unmasked, drunk reason, nurse dinner, trust captain → Day 3
- Pre-unlocked: `broken_unmasked`.
- Reason: **Say he was just too drunk**.
- Bedroom reflection: default else branch with the `broken_unmasked` extra paragraph ("The image of Thomas Moody without his mask…").
- Dinner: **Talk to Rosalind Marsh** → `nurse_generic_menu_doctor`: "Tell me more about yourself." (cost 30, `nurse_generic_background_doctor`, unlocks `remember_nurse` and hides the linked choice) → "Why were you invited here?" (cost 20, `nurse_generic_heroic_act_doctor`) → exit. Dinner: **Enjoy the creepy silence**.
- Map (90 min): bedroom_drunk (20, unlocks `burned_letter`) → bedroom_broken (10, `broken_unmasked` branch — brief variant) → billiard_room (0, first visit) → captain submenu: "Tell him about the letter" (with the `burned_letter` extra paragraph "He burned the letter before leaving for the hunt.") → "Tell him about Thomas Moody's face {{observation}}" (mask hidden after the letter pick) → sleep menu **Accept his offer** (cost TIME_MAX) → `doctor_day2_evening_captain_sleep_yes` (default `captain_sleep_options` since no `book_opium`) unlocks `trust_captain`.
- Exploration end: `trust_captain` → `jump doctor_day3_morning` (chapter changes to `sunday_morning`, test ends).

## setup_doctor_saturday_evening_4.json — Remember nurse, drunk reason, nurse dinner (Saturday-evening submenu), trust nurse → Day 3
- Pre-unlocked: `remember_nurse`.
- Reason: **Say he was just too drunk**.
- Bedroom reflection: default else branch (no `book_opium`, no `broken_unmasked`).
- Dinner: **Talk to Rosalind Marsh** → `nurse_generic_menu_doctor`: "What do you think of this weather?" (saturday-evening variant) → "What do you think of the other guests?" (cost 0, opens `nurse_generic_other_guests_menu_doctor`) → submenu picks Lady Claythorn (`nurse_generic_host_saturday`) → Amelia Baxter (`nurse_generic_psychic_saturday_evening_doctor`) → exit. Dinner: **Enjoy the creepy silence**.
- Exploration narration: `remember_nurse` paragraph ("By good fortune, I already know Nurse Rosalind Marsh…").
- Map: Queen Alexandra (cost 0, `bedroom_nurse_remember` — letter explained in full) → sleep menu **I guess it's the safest thing to do** (cost TIME_MAX) → `doctor_day2_evening_bedroom_nurse_sleep_yes` unlocks `trust_nurse`.
- Exploration end: `trust_nurse` → `jump doctor_day3_morning` (test ends).

## setup_doctor_saturday_evening_5.json — Flirt, footman, sleep alone via choice
- Pre-unlocked: `flirt`.
- Reason: **Say he was just too drunk**.
- Bedroom reflection: default else branch.
- Dinner: **Enjoy the creepy silence**.
- Exploration narration: `flirt` paragraph ("I might turn to Andrew…").
- Map: Kitchen (cost 20, `doctor_day2_evening_downstairs_default` flirt branch — maid points the doctor to the attic and unlocks `bedroom_footman` on the map) → Male Servants Room (cost 60, `doctor_day2_evening_males_room_enter` — full footman conversation, unlocks `footman_actor`) → "Go to sleep, alone" (early exit) → `doctor_ending_throat_cut`.

## setup_doctor_saturday_evening_6.json — Remember nurse, billiard avoid + repeat, no-flirt attic, nurse sleep no
- Pre-unlocked: `remember_nurse`.
- Reason: **Say he was just too drunk**.
- Bedroom reflection: default else branch.
- Dinner: **Enjoy the creepy silence**.
- Exploration narration: `remember_nurse` paragraph.
- Map (90 min):
  - billiard_room (cost 0, first visit "Just as I imagined, the room is almost deserted.") → bar (10, default — no `book_opium` extra paragraph) → "Talk to Sushil Sinha" (captain narration) → captain submenu **Leave him alone** (cost 20, early exit) → "Leave the room" (early exit).
  - billiard_room again (cost 0, repeat-visit narration "I find myself once more in the billiard room.") → "Leave the room" (early exit).
  - Male Servants Room (cost 20, no `flirt` → `doctor_day2_evening_males_room_do_no_enter` — the embarrassed knock-and-leave variant).
  - Queen Alexandra (cost 0, `bedroom_nurse_remember`) → sleep menu **I'd rather sleep alone** (cost 0, early exit) → `doctor_day2_evening_bedroom_nurse_sleep_no` → `jump doctor_day2_evening_sleep_alone` → `doctor_ending_throat_cut`.

## setup_doctor_saturday_evening_7.json — Broken unmasked, downstairs blocked, psychic + nurse rebuffs, captain refused
- Pre-unlocked: `broken_unmasked`.
- Reason: **Say he was just too drunk**.
- Bedroom reflection: default else branch with the `broken_unmasked` extra paragraph.
- Dinner: **Enjoy the creepy silence**.
- Map (90 min):
  - Kitchen (cost 20, no `flirt` → `doctor_day2_evening_downstairs_default` default branch — maid blocks, "Specific instructions forbidding guests to go downstairs do not sit well with me.").
  - Elizabeth I Bedroom (cost 20, `doctor_day2_evening_bedroom_psychic` — `doctor_bedroom_psychic_evening` plus the day-2 follow-up "She must be wary of speaking with me.").
  - Queen Alexandra (cost 20, no `remember_nurse` → `doctor_day2_evening_bedroom_nurse_do_not_remember` — nurse refuses, doctor withdraws politely).
  - billiard_room (cost 0) → "Talk to Sushil Sinha" → "Tell him about the letter" (no `burned_letter`) → "Tell him about Thomas Moody's face {{observation}}" → sleep menu **Refuse** (cost 0, early exit) → `doctor_day2_evening_captain_sleep_no` → `jump doctor_day2_evening_sleep_alone` → `doctor_ending_throat_cut`.
