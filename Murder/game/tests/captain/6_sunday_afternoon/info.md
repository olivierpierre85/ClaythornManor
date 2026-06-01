# Captain — Sunday Afternoon (Final Decisions)

Both morning paths converge on `captain_day3_afternoon`. The only menu
(`captain_day3_afternoon_car_menu`) appears solely when the captain has a
working car **and** has already unlocked the `car_ambush` ending (the
intuition). That intuition cannot be pre-set from thread state, so the
coward's-lie / `survives` branch is exercised by reaching `car_ambush`
first and replaying, not by a standalone plan here.

| Plan | Threads preset | Path covered |
| ---- | -------------- | ------------ |
| `setup_captain_sunday_afternoon_1` | none | **No working car.** Explore-path arrival, leaves alone on foot → `shot_fleeing` ending. No menus. |
| `setup_captain_sunday_afternoon_2` | `seen_car`, `petrol_tin_in_shed` | **Working car, no intuition.** All four leave together by motor; Miss Marsh appears and climbs in; the car is stopped and he is shot → `car_ambush` ending. No menus. |
| `setup_captain_sunday_afternoon_3` | `confide_in_nurse` | **Nurse-path arrival, no car.** He and Miss Marsh come down from hiding, find the others, then he sets out alone on foot → `shot_fleeing` ending. No menus. |
