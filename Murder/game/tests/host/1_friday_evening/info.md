# Friday Evening — Test Plans

The actress hired to play Lady Claythorn dresses, takes the butler's last
briefing, gives the welcome speech (`common_day1_evening_host_welcome_speech`)
and sits down to her own dinner.

## The three menus

**Dinner** — `host_day1_evening_menu_dinner`, 90 units:

| Choice | Redirect | Cost |
| ------ | -------- | ---- |
| Turn to Mr Manning, on your left | `host_day1_dinner_drunk` | 20 |
| Turn to Mr Moody, on your right  | `host_day1_dinner_broken` | 90 |
| Keep to yourself                 | `generic_cancel` (early exit) | — |

Manning unlocks the `addressed_manning_first` thread — the only place it is
ever unlocked — and opens `drunk_generic_menu_host` (weather 10, himself 20,
his wife 20 (only after "Tell me more about yourself."), the manor 10, his age
20, the other guests 10, exit 0). Moody costs the whole budget, so **the two
neighbours can only be had in that order**: Manning first leaves 70 units,
Moody first ends dinner on the spot.

**Map** — `host_day1_evening_map_menu`, 90 units. Below stairs (kitchen 20,
scullery 20, garage 10, gun room 10) routes through
`host_day1_evening_go_downstairs`, which unlocks `go_downstairs` on the first
visit only. The billiard room costs 90, so it is always the last thing she
does. Map rooms are hidden once visited, so no room can be seen twice in this
chapter — the revisit branches of `host_library_default` and
`host_portrait_gallery_default` belong to the Saturday plans.

**Debrief** — `host_day1_evening_debrief` has no menu. It counts faults:

| Fault | Condition |
| ----- | --------- |
| The order at dinner | `addressed_manning_first` locked |
| Below stairs        | `go_downstairs` unlocked |
| The empty billiard room | `stayed_with_guests` locked |

The first fault reads differently depending on how it happened: the butler
tells "you went to your right first" from "you spoke to neither of them" by
whether the Moody choice was ever taken
(`is_choice_already_chosen('host_day1_evening_menu_dinner',
'host_day1_dinner_broken')`). The opening line, the closing line and the
joining lines in `host_day1_evening_debrief_next_fault` all branch on the total,
so the count matters as much as which faults they are.

---

## Plans at a glance

| Plan | Dinner | Map | Faults |
| ---- | ------ | --- | ------ |
| 1 | Manning (weather, himself, his wife, the other guests), then Moody | library, portrait gallery, billiard room | **0** |
| 2 | Moody first | scullery, kitchen, garage, gun room, attic, a bedroom, tea room | **3** — order (right first), below stairs, billiard |
| 3 | Silence | dining room, hall, servant stair, garden, retires early | **2** — order (neither), billiard |
| 4 | Manning (the manor, his age), then keeps to herself | garage, gun room, billiard room | **1** — below stairs |
| 5 | Moody first | portrait gallery, billiard room | **1** — order (right first) |
| 6 | Manning (weather, himself), then keeps to herself | library, portrait gallery, tea room, garden, dining room, hall | **1** — billiard |
| 7 | Silence | billiard room | **1** — order (neither) |

Plans 4 to 7 exist to put each fault on the table **alone**, which is the only
way to reach the `host_debrief_fault_count == 1` opening and closing lines
next to each of the three reproaches in turn.

---

## Coverage matrix

| Branch / consequence | Plan(s) |
| -------------------- | ------- |
| Dinner: Manning first (correct order) | 1, 4, 6 |
| Dinner: Moody first, whole meal spent on him | 2, 5 |
| Dinner: silence throughout | 3, 7 |
| Dinner: both neighbours in one meal | 1 |
| Dinner: leaves the table early after Manning | 4, 6 |
| Manning: the weather | 1, 6 |
| Manning: tell me about yourself | 1, 6 |
| Manning: his wife (unlocked by the question above) | 1 |
| Manning: the manor | 4 |
| Manning: his age | 4 |
| Manning: the other guests | 1 |
| Manning: explicit exit from his menu | 1, 4, 6 |
| Map: library, first read (`family_history`) | 1, 6 |
| Map: portrait gallery, first look (`no_portrait`) | 1, 5, 6 |
| Map: billiard room + the captain's Boxer tale (`stayed_with_guests`) | 1, 4, 5, 7 |
| Map: first descent below stairs (`go_downstairs`) | 2, 4 |
| Map: second room below stairs (silent re-entry) | 2, 4 |
| Map: scullery, the rat poison (`found_poison`) | 2 |
| Map: kitchen and the maid | 2 |
| Map: garage | 2, 4 |
| Map: gun room | 2, 4 |
| Map: attic, locked (`day1_evening_attic_tried`, greys the attic) | 2 |
| Map: bedroom refusal (greys all seven bedrooms) | 2 |
| Map: tea room | 2, 6 |
| Map: dining room | 3, 6 |
| Map: entrance hall | 3, 6 |
| Map: servant stair (the landing, not the descent) | 3 |
| Map: garden | 3, 6 |
| Map: retires early | 3 |
| Map: budget runs out on its own | 2, 6 |
| Map: budget overrun by the billiard room | 1, 4, 5 |
| Debrief: clean night | 1 |
| Debrief: one fault (opening and closing variants) | 4, 5, 6, 7 |
| Debrief: two faults (`And there is one other thing.`) | 3 |
| Debrief: three faults (`That is not the whole of it.` + `And the last of it.`) | 2 |
| Debrief: reproach — went to your right first | 2, 5 |
| Debrief: reproach — spoke to neither of them | 3, 7 |
| Debrief: reproach — below stairs | 2, 4 |
| Debrief: reproach — never looked in on the billiard room | 2, 3, 6 |
| `I am exhausted` closing narration (billiard missed) | 2, 3, 6 |

---

## setup_host_friday_evening_1.json
**A faultless evening.** Manning first, four of his questions including his
wife, then the rest of the meal on Moody, who interrogates her instead. The
library and the portrait gallery, then she sits up with her guests for the
captain's story. The butler comes up pleased.

## setup_host_friday_evening_2.json
**Everything wrong, and the whole house searched.** She gives the meal to
Moody, then spends the evening below stairs — the poison in the scullery, the
maid in the kitchen, the garage, the gun room — tries the locked attic and a
guest's bedroom, and never appears in the billiard room. All three faults.

## setup_host_friday_evening_3.json
**The frightened hostess.** Not a word to either neighbour. A short round of
the rooms where nothing can happen to her, then bed. Two faults: the silence
and the empty billiard room.

## setup_host_friday_evening_4.json
**One slip.** Manning about the manor and his age, then she lets the meal
close. A brief look at the garage and the gun room is the only thing against
her, and she still sits up with her guests. Below stairs as a single fault.

## setup_host_friday_evening_5.json
**Wrong side of the table, nothing else.** The whole meal on Moody, the
portrait gallery, and then the billiard room. The order as a single fault.

## setup_host_friday_evening_6.json
**A long tour of an empty house.** Manning about the weather and himself, then
she leaves the table. Six ground-floor rooms until the clock runs out, and the
guests sit up without her. The billiard room as a single fault.

## setup_host_friday_evening_7.json
**Silent at table, present afterwards.** Nothing to either neighbour, then
straight to the billiard room for the rest of the night. The silence as a
single fault.
