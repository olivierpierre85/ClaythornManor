# Friday Evening — Test Plans

Ted arrives, mingles in the tea room, dines, then has free time on the bedroom floor.
Key branches: drinks at the bar (bar_1 unlocks `whisky` thread, bar_3 unlocks `day1_drunk`).
If `whisky` is set without `day1_drunk`, the chapter ends in the `lad_ending_day1_deathbed`
ending.

---

## setup_lad_friday_evening_1.json
**Path**: Drinks (Manning silent + Amelia cancel) → Dinner with Doctor (full menu) → Map: Tea
Room → Library → Portrait Gallery → Billiard Room → Listen to captain's full story.

---

## setup_lad_friday_evening_2.json
**Path**: Drinks (Amelia: weather + background) → Dinner with Amelia (full psychic menu) → Map:
Male/Female Servants Rooms → Butler's Room → Storage → Queen Alexandra → Richard III → George
IV → Henry IV → Elizabeth I (psychic bedroom).

---

## setup_lad_friday_evening_3.json
**Path**: Stand awkwardly → Eat in silence → Map → Billiard Room: doctor (cancel), group
→ leave group → leave room → Garden (bad weather narration) → back to Billiard Room ("I am
back in the billiard room") → bar_1 (whisky + Moody intro) → bar_2 (sherry) → bar_3 (port
→ drunk) → Leave → sleep (puke + jump to Saturday morning).
- Covers `lad_day1_evening_garden`, `lad_day1_evening_billiard_room_doctor`,
  `lad_day1_evening_billiard_group_cancel`, `lad_day1_evening_billiard_room_cancel`,
  all three bar labels, and the drunk-puke branch in `lad_day1_evening`.

---

## setup_lad_friday_evening_4.json
**Path**: Stand awkwardly → Eat in silence → Map → Billiard Room → bar_1 only (`whisky`
unlocked, no `day1_drunk`) → Leave → sleep → `lad_ending_day1_deathbed` ending.
- Covers the deathbed ending where Moody's whisky is poisoned but Ted does not drown it
  out with port.

---

## setup_lad_friday_evening_5.json
**Path**: Stand awkwardly → Eat in silence → Map: Servant Stairs → sleep.
- Covers `lad_servant_stairs_default` (the only chapter where that map room is reachable).
