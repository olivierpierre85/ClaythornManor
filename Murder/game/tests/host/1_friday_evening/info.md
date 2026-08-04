# Friday Evening — Test Plans

The actress hired to be Lady Claythorn dresses, takes the butler's last
briefing (which is where the placement and the left-first rule are given), and
walks into her own dinner. After the welcome speech
(`common_day1_evening_host_welcome_speech`) the dinner menu
(`host_day1_evening_menu_dinner`, 90 units) offers her two neighbours:

- **Mr Manning on her left** — `host_day1_dinner_drunk`, opening
  `drunk_generic_menu_host`. The food question is the one that matters: it
  unlocks his `status` and `lie` infos and her own `manning_act` observation.
- **Mr Moody on her right** — `host_day1_dinner_broken`, a single interview
  with three possible answers (`host_day1_dinner_broken_menu`).
- **Keep to yourself** — `generic_cancel`.

After dinner the `host_day1_evening_map_menu` map (120 units) opens the house,
and the night always ends with the butler at her door
(`host_day1_evening_debrief`), followed by `work_in_progress` — Saturday is
not written yet.

## Marks against the performance

`day1_evening_suspicious_acting` is incremented by:

| Lapse                                          | Where                                 |
| ---------------------------------------------- | ------------------------------------- |
| Turning to Moody before Manning                | `host_day1_dinner_broken`             |
| Saying nothing to either neighbour all dinner  | end of the dinner menu                |
| Inventing the history of the award for Moody   | `host_day1_dinner_broken_tradition`   |
| Never looking in on the billiard room          | end of the map                        |

Any mark at all sends the butler up to correct her (and unlocks the
`suspicious_acting` thread). None, and he comes up to say it went well.

---

## Coverage matrix

| Branch / consequence                                    | Plan(s) |
| ------------------------------------------------------- | ------- |
| Dinner: Manning first (correct order)                   | 1, 4    |
| Dinner: Moody first (mark)                              | 2       |
| Dinner: silence throughout (mark)                       | 3       |
| Manning: the food (`manning_act`, `status`, `lie`)      | 1, 2    |
| Manning: his profession (`job`)                         | 1, 4    |
| Manning: why he is here (`heroic_act`)                  | 1, 4    |
| Manning: the manor / his room / the other guests        | 2       |
| Manning: explicit exit from his menu                    | 1, 2, 4 |
| Moody: invent the tradition (mark)                      | 2       |
| Moody: say as little as possible                        | 4       |
| Moody: turn the question back on him                    | 1       |
| Map: billiard room (`stayed_with_guests`)               | 1, 4    |
| Map: billiard room revisit                              | 4       |
| Map: library (`family_history`, `name_age`)             | 1       |
| Map: library revisit                                    | 1       |
| Map: portrait gallery (`no_portrait`)                   | 1, 4    |
| Map: portrait gallery revisit                           | 4       |
| Map: kitchen, the staff who will not break character    | 2       |
| Map: kitchen revisit                                    | 2       |
| Map: scullery (`found_poison`)                          | 2       |
| Map: scullery revisit                                   | 2       |
| Map: garage / gun room                                  | 2       |
| Map: attic refusal (locked, greys the attic)            | 2       |
| Map: bedroom refusal (greys the bedrooms)               | 2       |
| Map: tea room / dining room / hall / garden / stair     | 3       |
| Map: retire early                                       | 3       |
| Map: budget runs out on its own                         | 1, 2, 4 |
| Debrief: clean night                                    | 1, 4    |
| Debrief: chastised, dinner order + billiard + tradition | 2       |
| Debrief: chastised, silence + billiard                  | 3       |
| Debrief Q: the name and the title                       | 1       |
| Debrief Q: the missing portrait                         | 1, 4    |
| Debrief Q: the rat poison                               | 2       |
| Debrief Q: the attic key                                | 2       |
| Debrief Q: who is paying                                | 1, 2, 3 |

---

## setup_host_friday_evening_1.json
**Path**: The evening played correctly, and the library.
- Manning first, the whole of his conversation (food, profession, why he is
  here), then Moody, turning his question back on him — which is where she
  learns her right-hand neighbour spent ten years as a footman.
- Map: the billiard room and the captain's Boxer Rebellion tale, then the
  library twice (the second visit takes the already-read branch) and the
  portrait gallery, which exhausts the 120 units exactly.
- Debrief: no marks, so the butler comes up pleased. She puts the name, the
  portrait and the money to him.

## setup_host_friday_evening_2.json
**Path**: Everything done wrong, and everything found out.
- Turns to Moody first (mark) and gives him the invented history of the award
  (mark), then spends the rest of dinner on Manning's smaller talk.
- Map: below stairs for the whole evening — the scullery and the kitchen twice
  each, the garage, the gun room, the locked attic and a guest bedroom — so the
  billiard room is never visited (mark).
- Debrief: all three chastisements, then the poison, the attic key and the
  question of who is paying for the weekend.

## setup_host_friday_evening_3.json
**Path**: The frightened hostess.
- Says nothing to either neighbour for the whole dinner (mark).
- Map: a quick round of the consequence-free rooms — tea room, dining room,
  entrance hall, garden, servant stair — then retires early, so the billiard
  room is missed (mark).
- Debrief: chastised for the silence and the empty chair. Only the question
  about the money is available to her.

## setup_host_friday_evening_4.json
**Path**: The careful answer, and a long evening among the guests.
- Manning first (profession and why he is here), then Moody, given as little as
  can decently be given — no mark.
- Map: the billiard room, then a second look in (revisit text), and the portrait
  gallery twice.
- Debrief: clean night, and she raises the missing portrait before letting him
  go to bed.
