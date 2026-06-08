# Captain — Sunday Afternoon (Final Decisions)

Both morning paths (explore / nurse-hide) converge on `captain_day3_afternoon`.
The afternoon itself no longer branches on `confide_in_nurse` — the arrival
narration, the shared discussion, and `car_together` are identical whichever
morning path was taken. Only the car threads change what happens here.

The single menu (`captain_day3_afternoon_car_menu`) only appears when the captain
has a working car (`seen_car` + `petrol_tin_in_shed`) **and** has already unlocked
the `car_ambush` ending — the intuition that to leave together is to die together.

`seen_car` can reach the afternoon from either morning path (the explore-path
garage visit, or the lad's report on the confide/hide path), so the car routes
are reachable regardless of the morning. The afternoon plays them the same way.

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
├─ shared discussion (common_day3_afternoon_lad_psychic_captain_discussion_1)
├─ seen_car AND petrol_tin_in_shed?
│   ├─ car_ambush already unlocked (intuition) -> car_menu
│   │     ├─ "leave together" -> car_together -> car_ambush
│   │     └─ "drive off alone" -> lie_alone   -> survives
│   └─ no intuition           -> car_together -> car_ambush   (direct jump, no menu)
│        car_together: the nurse always emerges from the front door
└─ no working car             -> on_foot      -> shot_fleeing
```

## Plans

| Plan | Threads / endings preset | Menu | Path covered |
| ---- | ------------------------ | ---- | ------------ |
| `..._1` | none | — | **No car.** On foot → `shot_fleeing`. |
| `..._2` | `seen_car`, `petrol_tin_in_shed` | none | **Car, no intuition.** Runs while `car_ambush` is still locked → the *direct jump* (no menu) → `car_together` → `car_ambush`. |
| `..._3` | `seen_car`, `petrol_tin_in_shed`, ending `car_ambush` | leave together | **Car, intuition.** Menu → `car_together` → `car_ambush`. |
| `..._4` | `seen_car`, `petrol_tin_in_shed`, ending `car_ambush` | drive off alone | **Car, intuition.** Menu → `lie_alone` → `survives`. |

## Coverage

- **Endings:** `shot_fleeing` (1), `car_ambush` (2, 3), `survives` (4).
- **`car_menu` choices:** leave together (3); drive off alone (4).
- **No-menu direct jump** (`"It is settled, then…"`): plan 2 only.
- **`car_together`:** reached by the direct jump (2) and the menu (3).
