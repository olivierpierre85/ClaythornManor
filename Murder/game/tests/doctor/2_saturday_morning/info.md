# Doctor — Saturday Morning (`doctor_day2_morning`)

The chapter opens in the doctor's bedroom at 08:00. Two opening narration variants depend on whether `drunk_letter` is unlocked. The morning routine then branches on `book_opium` (the doctor resists his usual habit) versus the default ("As always, I begin with my usual routine."). At breakfast, a 30-minute timed menu offers a chat with Miss Marsh (`nurse_generic_menu_doctor`); the host then pulls the doctor upstairs into the shared `common_day2_breakfast_follow_doctor_lad_host` flow, where `book_mystery` or `drunk_letter` unlock a remove-the-mask choice. Lady Claythorn announces the hunt, the pre-hunt reflection branches on `book_opium` and `flirt`, and the hunt menu (`doctor_day2_morning_hunt`) decides whether to join. The chapter ends with `jump doctor_day2_hunt`.

The 30-minute budget on the nurse menu is too tight to exercise every line in a single plan, so coverage is split across multiple plans. `nurse_generic_background_doctor` costs 30 minutes on its own and closes the menu; `nurse_generic_heroic_act_doctor` is gated behind the background choice being hidden, which makes it unreachable inside this chapter's budget.

## setup_doctor_saturday_morning_1.json — Default narrative, hunt
- No threads pre-unlocked.
- Opening: default ("Strange how those two words came to mind first.").
- Routine: usual cold-water morning.
- Breakfast: talk to Miss Marsh; nurse menu picks weather → manor → age (10+10+10, menu auto-closes).
- `common_day2_breakfast_follow_doctor_lad_host` runs without `broken_offended`, `book_mystery`, or `drunk_letter`, so the mask menu does NOT appear and the doctor falls straight into `common_day2_breakfast_follow_doctor_lad_normal`.
- Pre-hunt: no extra reflection.
- Hunt menu: **Go on the hunt** → `doctor_day2_hunt_choice`.

## setup_doctor_saturday_morning_2.json — Mystery book, mask removed, hunt
- Pre-unlocked: `book_mystery`.
- Opening: default.
- Routine: usual.
- Breakfast: talk to Miss Marsh; nurse menu picks room → other_guests submenu (Samuel Manning, Lady Claythorn) → time runs out and both menus auto-close.
- `common_day2_breakfast_follow_doctor_lad_host`: the `book_mystery` reflection plays ("That book I read yesterday—how did the victim die?"); mask menu fires.
- Mask menu: **Remove the mask** → `doctor_day2_breakfast_follow_doctor_lad_remove_mask` → `doctor_day2_behind_the_mask` (unlocks `broken_unmasked`, hides `lie_mask`).
- Pre-hunt: no extra reflection.
- Hunt menu: **Go on the hunt** → `doctor_day2_hunt_choice`.

## setup_doctor_saturday_morning_3.json — Drunk letter, broken offended, keep mask, stay
- Pre-unlocked: `drunk_letter`, `broken_offended`.
- Opening: drunk_letter variant ("Despite my suspicions, it seems no one tried to harm me in the night.").
- Routine: usual.
- Breakfast: just keep to yourself (skip nurse menu).
- `common_day2_breakfast_follow_doctor_lad_host`: the `broken_offended` reflection plays ("I feel somewhat uneasy."), then the `drunk_letter` reflection ("After discovering the letter in Samuel Manning's room…"); mask menu fires.
- Mask menu: **Don't remove the mask, let him rest in peace** → `common_day2_breakfast_follow_doctor_lad_keep_mask`.
- Pre-hunt: no extra reflection (no `book_opium`, no `flirt`).
- Hunt menu: **Stay here** → `doctor_day2_no_hunt_choice` with the extra `drunk_letter` paragraph ("Samuel Manning may very well use this hunt as an opportunity to harm me.").

## setup_doctor_saturday_morning_4.json — Opium book, flirt, stay
- Pre-unlocked: `book_opium`, `flirt`.
- Opening: default.
- Routine: opium variant ("On most mornings, I would begin in the usual manner. But today is not most mornings.").
- Breakfast: talk to Miss Marsh; nurse menu picks `Tell me more about yourself.` → `nurse_generic_background_doctor` (cost 30, menu closes after; unlocks `remember_nurse`).
- `common_day2_breakfast_follow_doctor_lad_host` runs without `book_mystery` or `drunk_letter`, so the mask menu does NOT appear.
- Pre-hunt: `book_opium` reflection ("Yet I have not taken my 'medicine' today.") and `flirt` reflection ("Besides, if I were to stay, I might spend a little more time with my new friend.").
- Hunt menu: **Stay here** → `doctor_day2_no_hunt_choice` without the `drunk_letter` paragraph.
