# Doctor — Sunday Afternoon (`doctor_day3_afternoon`)

The chapter opens at 12:00 in the tea room (captain branch) or hidden in the butler's room before moving to the library (nurse branch). It is the final doctor chapter and every plan ends in one of four endings: `escape`, `shot`, `run_over`, or `poisoned`. Branching is driven by `trust_captain` / `trust_nurse` from Saturday Evening, with further variation from `book_opium`, `footman_actor`, `remember_nurse`, and `broken_unmasked`.

## Captain branch (`doctor_day3_afternoon_captain`)

First menu (`doctor_day3_afternoon_captain_choice`):
- **Share what you know with the others** → `doctor_day3_afternoon_captain_share`
- **No, do not trust them.** → `doctor_day3_afternoon_captain_do_not_share`

If shared, second menu (`doctor_day3_afternoon_captain_share`) lets the doctor reveal each observation in turn. Each share option is gated on its thread and increments `saved_variables['doctor_day3_afternoon_captain_share']`:
- **Tell them about the footman{{observation}}** — gated on `footman_actor`
- **Tell them about Rosalind Marsh{{observation}}** — gated on `remember_nurse`
- **Tell them about Thomas Moody{{observation}}** — gated on `broken_unmasked`
- **Do not tell them anything more** — `generic_cancel`, early-exit

After the menu, the chapter splits on the share counter:
- `share > 2` (all three told) → `doctor_day3_afternoon_captain_escape_with_psychic` → `doctor_ending_escape`.
- `share <= 2` → `doctor_day3_afternoon_captain_escape_without_psychic`. Within that label, `share > 1` triggers Ted Harring's "pauses for a second" narration; otherwise he answers "without hesitation". Then `book_opium` decides the death:
  - `book_opium` set → `doctor_ending_run_over`.
  - default → `doctor_ending_shot`.

## Nurse branch (`doctor_day3_afternoon_nurse`)

Menu (`doctor_day3_afternoon_nurse`):
- **Speak to them, they look harmless** → `doctor_day3_afternoon_nurse_talk`
- **Stay hidden, they look dangerous** → `doctor_day3_afternoon_nurse_hide`

Both branches call `doctor_day3_afternoon_nurse_wait_captain_leave`, then rejoin the main flow (psychic and lad in the entrance hall, kitchen scene with poisoned bread) which always ends with `jump doctor_ending_poisoned`.

## setup_doctor_sunday_afternoon_1.json — Trust captain, do not share
- Pre-unlocked: `trust_captain`.
- Captain branch, picks **No, do not trust them.** — runs the `doctor_day3_afternoon_captain_do_not_share` paragraph.
- Share counter stays at 0, so `escape_without_psychic` plays the "without hesitation" branch.
- No `book_opium`, so the chapter ends with `doctor_ending_shot`.

## setup_doctor_sunday_afternoon_2.json — Trust captain + book_opium, share two observations
- Pre-unlocked: `trust_captain`, `book_opium`, `footman_actor`, `remember_nurse`.
- Captain branch, picks **Share what you know with the others** → footman → Rosalind Marsh → cancel.
- Share counter reaches 2, so `escape_without_psychic` plays the "Ted Harring pauses for a second" branch.
- `book_opium` set, so the chapter ends with `doctor_ending_run_over` (covers the withdrawal narration on the road).

## setup_doctor_sunday_afternoon_3.json — Trust captain, share all three
- Pre-unlocked: `trust_captain`, `footman_actor`, `remember_nurse`, `broken_unmasked`.
- Captain branch, picks **Share** → footman → Rosalind Marsh → Thomas Moody → cancel.
- Share counter reaches 3, so the chapter routes through `doctor_day3_afternoon_captain_escape_with_psychic`.
- Covers the `share_broken` paragraph (mask reveal + poisoning suspicion) and the long Aberdeen / police-station epilogue.
- Ends with `doctor_ending_escape` — the only survival ending in this chapter.

## setup_doctor_sunday_afternoon_4.json — Trust nurse, speak to them
- Pre-unlocked: `trust_nurse`.
- Nurse branch, picks **Speak to them, they look harmless** → `doctor_day3_afternoon_nurse_talk`.
- Waits for the captain to leave, then crosses the entrance hall to find Ted Harring and Amelia Baxter.
- Joins the kitchen scene and ends with `doctor_ending_poisoned`.

## setup_doctor_sunday_afternoon_5.json — Trust nurse, stay hidden
- Pre-unlocked: `trust_nurse`.
- Nurse branch, picks **Stay hidden, they look dangerous** → `doctor_day3_afternoon_nurse_hide`.
- Doctor steps out anyway and bumps into Ted Harring and Amelia Baxter ("what a fool I am" narration).
- Joins the kitchen scene and ends with `doctor_ending_poisoned`.
