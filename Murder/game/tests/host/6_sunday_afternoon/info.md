# Sunday Afternoon — Test Plans

Noon in the hall, with the morning's search behind them and Harring and Baxter
waiting in the tea room. Lady Claythorn and Captain Sinha keep to what they
agreed: nothing is said to the other three, and it is the two of them alone.
What they found on the Sunday morning map decides whether there is a choice at
all, and the chapter ends in one of the three Sunday endings.

The chapter is only reachable through `trust_captain` on the Saturday night, so
every plan carries it, although nothing in the afternoon reads it.

There is no next chapter. Every path jumps to a `host_ending_*` label, which
jumps to `ending_generic`, and that shows the `test_end` screen in test mode.

---

## The gate on the car

`host_day3_afternoon` reads two threads from the morning:

```
if car_checked and petrol_tin:
    jump host_day3_afternoon_car            # no menu, she drives
else:
    if car_checked: "dead weight"           # a sound car with a dry tank
    else:           "no car to leave in"
    host_day3_afternoon_menu_foot
```

So the car is the only way to survive, and it needs **both** the garage and
the shed from the morning. Petrol without a car, or a car without petrol, is the
same as nothing: the road on foot. The kitchen basket is not read.

## The one menu

`host_day3_afternoon_menu_foot`, `time_left = 1`, both choices early exits:

| Choice | Redirect | Ending |
| ------ | -------- | ------ |
| Walk out with him, now | `host_day3_afternoon_foot` | `run_over` |
| Let him go alone, and hide in the attic | `host_day3_afternoon_attic` | `shot_by_butler` |

## The attic

`host_day3_afternoon_attic` (2_attic.rpy) reads one saved variable at the attic
door: `day3_morning_attic_visited`. If the Captain opened the attic on the
morning map the door is already unlocked, otherwise the butler's key turns in
the lock that was closed to her on Friday. Nothing else branches: the wait,
Samuel Manning alive on the dining room floor, and the butler in the doorway
all play in one run.

The attic path unlocks hidden information on other characters — `faked_death`
and `lie` on the drunk, `took_valuables` on the butler — and the car path
unlocks `car` on the host.

## Threads and variables read in the chapter

| Name | Where |
| ---- | ----- |
| `car_checked` | the gate, and the Captain's line when there is no petrol |
| `petrol_tin` | the gate |
| `day3_morning_attic_visited` | the attic door |

`trust_captain` and `saw_car` are carried for realism only.

---

## Plans at a glance

| Plan | Morning state | Hall | Menu | Attic door | Ending |
| ---- | ------------- | ---- | ---- | ---------- | ------ |
| 1 | car, petrol | the car will run | none | — | `escape` |
| 2 | petrol, no car | no car to leave in | walk | — | `run_over` |
| 3 | nothing | no car to leave in | attic | locked since Friday | `shot_by_butler` |
| 4 | car, no petrol | dead weight | attic | left unlocked this morning | `shot_by_butler` |

---

## Coverage matrix

| Branch / consequence | Plan(s) |
| -------------------- | ------- |
| Gate: car and petrol, no menu (`host_day3_afternoon_car`) | 1 |
| Gate: car checked, tank dry — "dead weight" | 4 |
| Gate: no car checked — "no car to leave in" | 2, 3 |
| Menu: walk out with him (`host_day3_afternoon_foot`) | 2 |
| Menu: hide in the attic (`host_day3_afternoon_attic`) | 3, 4 |
| Attic door: locked against her on Friday | 3 |
| Attic door: unlocked by the Captain in the morning | 4 |
| Dining room: Samuel Manning alive (`_attic_manning`) | 3, 4 |
| The butler's return (`_attic_butler`) | 3, 4 |
| She can drive (`description_hidden` `car`) | 1 |
| Ending `escape` | 1 |
| Ending `run_over` | 2 |
| Ending `shot_by_butler` | 3, 4 |

---

## setup_host_sunday_afternoon_1.json
**The car, and the only way out.** The second debug checkpoint plus `saw_car`:
`trust_captain`, `saw_car`, `car_checked`, `petrol_tin`. The Captain says the
car will run and the tin will fill it, and there is no menu. Out the back way,
the shed, the garage, the engine catches on the third pull, and she takes the
wheel because she learnt to drive for a part. The butler's car passes them a
mile past the gates and does not turn round. The police station at half past
one, `host_ending_escape`. No choices at all.

## setup_host_sunday_afternoon_2.json
**Petrol and nothing to put it in.** `trust_captain` and `petrol_tin`, the
noon state of a morning that found the shed but never the garage. The Captain
says they have no car to leave in, and she walks out with him rather than stay
behind. Two miles of mud, an engine from the trees, and the car that does not
slow. `host_ending_run_over`.

## setup_host_sunday_afternoon_3.json
**Nothing found, and she hides.** `trust_captain` alone, the first debug
checkpoint. No car to leave in, and she cannot face the walk, so the Captain
goes alone and leaves her the butler's key. `day3_morning_attic_visited` is
left at its default, so the attic door is the one that was locked against her
on Friday and the key turns as if it had never been anything else. Three hours
on a trunk, Samuel Manning sober on the dining room floor, and the butler in
the doorway. `host_ending_shot_by_butler`.

## setup_host_sunday_afternoon_4.json
**A sound car, a dry tank, and the door already open.** `trust_captain`,
`saw_car`, `car_checked` and no `petrol_tin`: the Captain calls the tourer a
dead weight before they come to the menu. She hides, and because
`day3_morning_attic_visited` is set the attic door is unlocked the way the
Captain left it in the morning. The same wait and the same dining room as
plan 3, ending at `host_ending_shot_by_butler`.
