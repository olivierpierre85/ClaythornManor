# Captain — Sunday Afternoon (Final Decisions)

Both morning paths converge on `captain_day3_afternoon`. The single menu
(`captain_day3_afternoon_car_menu`) only appears when the captain has a working
car (`seen_car` + `petrol_tin_in_shed`) **and** has already unlocked the
`car_ambush` ending — the intuition that to leave together is to die together.

`seen_car` reaches the afternoon from two places: the explore-path garage visit
(sunday morning) or the lad's report on the confide/hide path (unlocked during
the confide arrival here). So the car routes are reachable on **both** morning
paths, and `car_together` has two arrival variants — the hiding Miss Marsh
appears at the front door (explore), or she is already with the party (confide).

## ⚠️ Test-runner constraint: endings leak between plans

The runner restores threads / saved variables / progress / observations between
plans, **but not endings** (and `reset_information` doesn't re-lock them either).
So once any plan reaches the `car_ambush` ending, it stays unlocked for every
later plan in the run. Consequences for plan design:

- A **no-menu** car plan (`choices: []`) only works while `car_ambush` is still
  locked, i.e. before any car plan runs. There can be exactly **one**, and it
  must run before the others — here that is plan 2 (plan 1 is `shot_fleeing`, so
  it doesn't unlock `car_ambush`).
- Every **other** car plan presets `car_ambush` via `unlocked_endings` and
  provides a menu choice, so the menu always appears and the choice is consumed
  regardless of run order.

This is why the "no intuition" direct jump is exercised once (plan 2) and the
remaining car plans are all menu-driven.

## Branch map

```
captain_day3_afternoon
├─ confide_in_nurse?  arrival narration (confide arrival also unlocks seen_car)
├─ shared discussion (common_day3_afternoon_lad_psychic_captain_discussion_1)
├─ seen_car AND petrol_tin_in_shed?
│   ├─ car_ambush already unlocked (intuition) -> car_menu
│   │     ├─ "leave together" -> car_together -> car_ambush
│   │     └─ "drive off alone" -> lie_alone   -> survives
│   └─ no intuition           -> car_together -> car_ambush   (direct jump, no menu)
│        car_together: nurse appears at the door (explore) / already aboard (confide)
└─ no working car             -> on_foot      -> shot_fleeing
```

## Plans

| Plan | Threads / endings preset | Menu | Path covered |
| ---- | ------------------------ | ---- | ------------ |
| `..._1` | none | — | **Explore, no car.** On foot → `shot_fleeing`. |
| `..._2` | `seen_car`, `petrol_tin_in_shed` | none | **Explore, car, no intuition.** Runs while `car_ambush` is still locked → the *direct jump* (no menu); Miss Marsh appears at the door → `car_ambush`. |
| `..._3` | `confide_in_nurse` | — | **Confide, no car.** Comes down from hiding, then on foot → `shot_fleeing`. |
| `..._4` | `seen_car`, `petrol_tin_in_shed`, ending `car_ambush` | leave together | **Explore, car, intuition.** Menu → `car_together` (nurse appears) → `car_ambush`. |
| `..._5` | `seen_car`, `petrol_tin_in_shed`, ending `car_ambush` | drive off alone | **Explore, car, intuition.** Menu → `lie_alone` → `survives`. |
| `..._6` | `confide_in_nurse`, `seen_car`, `petrol_tin_in_shed`, ending `car_ambush` | leave together | **Confide, car, intuition.** Menu → `car_together` *else* (nurse already aboard) → `car_ambush`. |
| `..._7` | `confide_in_nurse`, `seen_car`, `petrol_tin_in_shed`, ending `car_ambush` | drive off alone | **Confide, car, intuition.** Menu → `lie_alone` → `survives`. |

## Coverage

- **Endings:** `shot_fleeing` (1, 3), `car_ambush` (2, 4, 6), `survives` (5, 7).
- **`car_together` branches:** nurse appears at the door (2, 4); nurse already
  aboard (6).
- **`car_menu` choices:** leave together (4, 6); drive off alone (5, 7).
- **No-menu direct jump** (`"It is settled, then…"`): plan 2 only.
- **Arrival narration:** explore (1, 2, 4, 5); confide-in-nurse (3, 6, 7).
