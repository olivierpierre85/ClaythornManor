# Psychic — Sunday Morning (`psychic_day3_morning`)

A linear chapter with no menus. Amelia wakes, walks to Ted Harring's bedroom, and the pair search the manor before regrouping with Captain Sinha in the tea room and discovering Samuel Manning's body. The only branching point is the `visit_lad` thread, which selects the opening dialogue with Ted.

## setup_psychic_sunday_morning_1.json — Did not visit Ted on Saturday evening
- No threads unlocked.
- Triggers `psychic_day3_morning_has_not_visited_lad` (the standalone "I am sorry to disturb you but something strange is happening" opening).
- Continues through the shared tea-room sequence, Manning's body, and the deaths-end recap.

## setup_psychic_sunday_morning_2.json — Already visited Ted on Saturday evening
- Pre-set thread: `visit_lad`.
- Triggers `common_day3_morning_lad_psychic_journey` (the "my hunch was right yesterday" opening), exercising the `current_character.text_id != "lad"` else branch in that common label.
- Same tea-room and deaths-end follow-up.
