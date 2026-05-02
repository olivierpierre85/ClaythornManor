# Doctor — Sunday Morning (`doctor_day3_morning`)

The chapter opens at 08:30 in whichever bedroom the doctor slept in at the end of Saturday Evening. The body of the chapter is purely narrative — there are no menus and no map. Branching is entirely driven by which trust thread was unlocked the night before:

- `trust_captain` → `doctor_day3_morning_captain` — the doctor wakes in the captain's room, they search the dining room, kitchen and entrance hall, meet Ted Harring and Amelia Baxter, then break into Miss Marsh's empty bedroom together and agree to regroup in the tea room. A `book_opium` paragraph adds the doctor's withdrawal reflection while dressing.
- `trust_nurse` → `doctor_day3_morning_nurse` — the doctor wakes in Miss Marsh's room, she reports the empty house, they hear Ted Harring and Amelia Baxter pass by, dodge Captain Sinha in the corridor and hide in the butler's room in the attic.

Both branches end with `jump doctor_day3_afternoon`, which calls `change_time(..., chapter='sunday_afternoon')` and ends the test.

The chapter has no menus, so every plan uses `"choices": []`.

## setup_doctor_sunday_morning_1.json — Trust captain, default narration
- Pre-unlocked: `trust_captain`.
- Captain branch without the `book_opium` withdrawal paragraph.
- Exits to Day 3 afternoon.

## setup_doctor_sunday_morning_2.json — Trust captain + book_opium
- Pre-unlocked: `trust_captain`, `book_opium`.
- Captain branch with the withdrawal paragraph ("I have been sweating all night, my body aching for a dose of laudanum…").
- Exits to Day 3 afternoon.

## setup_doctor_sunday_morning_3.json — Trust nurse
- Pre-unlocked: `trust_nurse`.
- Nurse branch — hide in the butler's room.
- Exits to Day 3 afternoon.
