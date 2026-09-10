# Saturday Evening — Test Plans

The party comes back from the woods with Doctor Baldwin dead, Lady Claythorn
acts a telephone call to a disconnected line, Captain Sinha has Mr Manning
locked in his room, and — if she has given him any reason at all — asks her for
her title in front of the remaining guests. Dinner is read off the butler's
sheet of paper. Afterwards the butler announces that the weekend has been
cancelled, and that the car leaves at eleven with or without her.

Three of the four endings of the chapter are deaths, and the fourth is
`work_in_progress` until Sunday is written.

---

## The gate on the accusation

`host_day2_evening` counts the same faults the Friday debrief did, plus the
rabbit:

```
if not stayed_with_guests or not addressed_manning_first or terrible_shot:
    call host_day2_evening_captain_accusation
else:
    common_day2_evening_samuel_manning_discussion_part_3 / _part_4
```

So the peaceful evening needs **both** Friday threads unlocked **and**
`terrible_shot` locked. Any single slip puts her in front of the Captain in the
tea room, and the accusation is the only way to reach `bested_captain`.

## The three menus

**Accusation** — `host_day2_evening_menu_accusation`, `time_left = 1`, every
choice an early exit:

| Choice | Redirect | Condition |
| ------ | -------- | --------- |
| Give him the title from the library book | `host_day2_evening_accusation_answer` | `family_history` |
| Take offence and refuse the question | `host_day2_evening_accusation_refuse` | — |
| Confess the truth | `host_day2_evening_unmasked_end` | — |

The title is the only survivable answer, and it unlocks `bested_captain`, with
an extra exchange if `no_portrait` is unlocked. Refusing falls straight through
to `host_day2_evening_unmasked_end`, so **refusal and confession end at the same
revolver** — `host_ending_shot_tea_room`. A player without `family_history` has
no way out of the tea room at all.

**Map** — `host_day2_evening_map_menu`, 90 units, 21:30 to 23:00. Rooms cost 10
except the portrait gallery, the library, Mr Manning's room, the female
servants' room and sitting up with the Captain, which cost 20. Two choices are
early exits: the car in the garden and her own locked door. `bested_captain`
swaps the billiard room entry — sitting up with the Captain (20) becomes merely
looking in on an empty room (10) — so **humiliating him in the tea room shuts
the truth out of the night for good**. The butler cannot be reached: his attic
room is locked and he is out on the gravel.

**Billiard room** — `host_day2_evening_menu_billiard_room`, opened from inside
the map, both choices early exits: `host_day2_evening_billiard_room_truth`
unlocks `trust_captain`, `host_day2_evening_billiard_room_small_talk` does not.

## How the night ends

| Exit | Result |
| ---- | ------ |
| Garden, `host_day2_evening_leave_with_butler` | `host_ending_shot_in_car` |
| Clock runs out or her own door, `trust_captain` locked | `host_ending_die_in_sleep` |
| Clock runs out or her own door, `trust_captain` unlocked | `jump work_in_progress` (Sunday not written) |

Note that the map menu closes only on an early exit or on 0 minutes left, so
every plan below either ends on the car, ends on her door, or spends all 90
units exactly.

## Threads read in the chapter

| Thread | Where |
| ------ | ----- |
| `stayed_with_guests`, `addressed_manning_first`, `terrible_shot` | the accusation gate |
| `family_history` | the title choice, and the library at night |
| `no_portrait` | the extra exchange in the answer, and the gallery at night |
| `found_poison` | the missing bottle in the scullery, and the whole plates-and-hands paragraph at dinner |
| `bested_captain` | dinner, the billiard entry, the Captain's bedroom door |
| `trust_captain` | the closing narration |

`go_downstairs` is carried by some plans for realism only — nothing in this
chapter reads it. `accused_butler` is declared in `host_config.rpy` with
`chapters=['saturday_evening']` but is never unlocked anywhere in the script,
so no plan can cover it.

---

## Plans at a glance

| Plan | Tea room | Dinner | Night | End |
| ---- | -------- | ------ | ----- | --- |
| 1 | no accusation | poison | ground floor, scullery, library, tells the Captain the truth | `work_in_progress` |
| 2 | the title, with the portrait | bested | gallery, library, the two dead men, empty billiard room, the car | `shot_in_car` |
| 3 | refuses the question | — | — | `shot_tea_room` |
| 4 | confesses although she has the answer | — | — | `shot_tea_room` |
| 5 | no accusation | poison | the whole attic, the Captain's dark door, small talk in the billiard room | `die_in_sleep` |
| 6 | the title, without the portrait | bested | every bedroom until the clock runs out | `die_in_sleep` |
| 7 | no accusation | plain | below stairs and the library, then the car | `shot_in_car` |

---

## Coverage matrix

| Branch / consequence | Plan(s) |
| -------------------- | ------- |
| Gate: peaceful evening (Manning taken up quietly) | 1, 5, 7 |
| Gate: accusation from the missing billiard evening | 2, 6 |
| Gate: accusation from all three faults at once | 3 |
| Gate: accusation from the rabbit alone | 4 |
| Accusation: the title answered (`bested_captain`) | 2, 6 |
| Accusation: the title plus the missing portrait | 2 |
| Accusation: the title without the portrait | 6 |
| Accusation: refusal, then the revolver | 3 |
| Accusation: confession, with the answer still on the table | 4 |
| Dinner: the plates and the butler's hands (`found_poison`) | 1, 5 |
| Dinner: `I eat very little.` | 2, 6, 7 |
| Dinner: the Captain will not look at her (`bested_captain`) | 2, 6 |
| Map: kitchen | 7 |
| Map: scullery, the bottle gone (`found_poison`) | 1, 5 |
| Map: scullery, dirty dishes only | 7 |
| Map: garage (`host_garage_default`) | 7 |
| Map: gun room, emptied for the car | 7 |
| Map: tea room | 1 |
| Map: dining room | 1 |
| Map: entrance hall | 1 |
| Map: servant stair (`host_servant_stairs_default`) | 7 |
| Map: portrait gallery, revisit (`no_portrait`) | 2 |
| Map: portrait gallery, first look | 6 |
| Map: library, revisit (`family_history`) | 1, 2 |
| Map: library, the book unread | 7 |
| Map: Mr Harring barricading his door | 6 |
| Map: Miss Marsh's door | 6 |
| Map: Miss Baxter's door | 6 |
| Map: Mr Manning's door | 6 |
| Map: the Captain's door, lamplight and shame (`bested_captain`) | 6 |
| Map: the Captain's door, dark and empty | 5 |
| Map: Doctor Baldwin laid out | 2 |
| Map: Mr Moody under the sheet | 2 |
| Map: butler's attic room, locked | 5 |
| Map: attic storage, locked | 5 |
| Map: male servants' room | 5 |
| Map: female servants' room, the maid packing | 5 |
| Map: sit up with the Captain, the truth (`trust_captain`) | 1 |
| Map: sit up with the Captain, small talk | 5 |
| Map: billiard room empty (`bested_captain`) | 2, 6 |
| Map: the car in the garden | 2, 7 |
| Map: her own locked door | 1, 5 |
| Map: budget runs out on its own | 6 |
| Ending: `shot_tea_room` | 3, 4 |
| Ending: `shot_in_car` | 2, 7 |
| Ending: `die_in_sleep` | 5, 6 |
| Closing narration: somebody else knows what she is | 1 |

---

## setup_host_saturday_evening_1.json
**A clean Friday, and she puts herself in the Captain's hands.** The thread set
of the fourth debug checkpoint — both Friday courtesies, below stairs, the
poison and the family history — so Mr Manning goes up without a word and no
accusation is made. Dinner is the long paragraph about which plate goes to
which guest. A round of the ground floor, the scullery where the bottle has
gone, the library she has finished with, then she sits up with Captain Sinha
and tells him everything. She locks her door with ten minutes to spare.
`trust_captain` sends the chapter to `work_in_progress`, which is where Sunday
will begin.

## setup_host_saturday_evening_2.json
**She answers the accusation and leaves anyway.** She never turned to Mr
Manning on the Friday, so the Captain asks for her title and she gives him
Kilbraith, with the portrait gallery thrown in his face after it. He apologises
to her in front of the house, which costs her the only company she might have
had at eleven o'clock: the billiard room is empty when she looks in. The
gallery, the library, both dead men, and then the car — the forest road and
`host_ending_shot_in_car`.

## setup_host_saturday_evening_3.json
**Nothing to fall back on.** No threads at all: three faults, the accusation,
and no title to give because she never opened the book in the library. Taking
offence buys her one exchange before the Captain calls it what it is, and the
butler's revolver comes out. `host_ending_shot_tea_room`.

## setup_host_saturday_evening_4.json
**The answer in her hand, and she puts it down.** A faultless Friday undone by
one shot at a sitting rabbit. She has `family_history`, so the title is on the
menu, and she confesses instead. Same room, same revolver — this is the plan
that proves the confession is reachable with the safe answer still available.

## setup_host_saturday_evening_5.json
**The house put to bed, and nothing said.** A clean Friday again, but she
spends her ninety minutes in the attic among the staff — the maid packing and
apologising, the locked storage, the butler's abandoned room — looks at the
Captain's dark door, and then keeps to small talk when she finally sits down
with him. She locks her door alone. `host_ending_die_in_sleep`.

## setup_host_saturday_evening_6.json
**Bested him, then walked the corridor until the clock ran out.** She sat with
nobody on the Friday, so the accusation comes, and the title answers it without
the portrait exchange. Then every bedroom in turn — Harring dragging furniture,
Marsh, Baxter, Manning, and the Captain's lamplit door he will not open — and
a look at the empty billiard room takes the last ten minutes. No early exit at
all: the map closes on 0 and she goes to bed. `host_ending_die_in_sleep`.

## setup_host_saturday_evening_7.json
**Below stairs, then out.** A quiet Friday with none of the discoveries, so
dinner is a single line and the scullery holds nothing but dirty dishes. The
kitchen, the garage, the gun room, the library she never read and the servant
stair, and then she takes the seat she was offered in the car.
`host_ending_shot_in_car`.
