# Friday Evening — Test Plans

Thomas Moody (Archibald in disguise) arrives at the manor, rests in the
'Richard the Third' room, then comes down to the tea room where he meets the
doctor, the nurse, the captain and the drunk. The gong calls everyone in to
dinner, where he is seated beside Lady Claythorn. After her welcome speech he
questions her directly over the first course (the `host_generic_menu_broken`
conversation, 90 time units).

After dinner the chapter opens up: he returns to his room and the
`broken_day1_evening_map_menu` map (a second 90-unit budget) lets him roam the
house — the attic, the bedrooms, the ground floor, the servants' floor (gated
behind the footman's livery), and the billiard room where the rest of the party
is gathered. The night ends with the planted army order on his pillow, then a
branch:

- `butler_surprise` unlocked → `broken_ending_day1_throat_cut`
- else `drink_good_whisky` unlocked → `broken_ending_day1_deathbed`
- else → `broken_day2_morning`

Because both conversations are time-budgeted at 90 units, no single playthrough
can reach every branch, so coverage is split across the files below. Some plans
pre-unlock threads (`unlocked_threads`) to bypass a prerequisite and spend the
budget on the branch under test; others unlock the same threads organically so
the unlock paths themselves are exercised.

---

## Coverage matrix

| Branch / consequence                                   | Plan(s)   |
| ------------------------------------------------------ | --------- |
| Host Q: weather                                        | 2         |
| Host Q: background → invite → award (`host_lies`)       | 1         |
| Host Q: other guests                                   | 2         |
| Host Q: the manor                                      | 2         |
| Host Q: her age                                        | 1         |
| Host Q: her room                                       | 1         |
| Host menu: explicit exit                               | 2–7       |
| Map: tea room / dining room / garden / hall            | 2, 7      |
| Map: portrait gallery / library                        | 2         |
| Map: attic refusal (greys the attic)                   | 2         |
| Map: bedroom refusal (greys the bedrooms)              | 2         |
| Servant stair: leave the livery                        | 2         |
| Servant stair: try the livery on (`found_livery`)      | 3         |
| Servant stair: revisit (livery already found)          | 3         |
| Servants' floor refused (no livery yet)                | 3         |
| Kitchen: slip out unseen (no `host_lies`)              | 3         |
| Kitchen: question the maid (`talked_to_maid`)          | 6         |
| Kitchen: leave the maid be                             | 7         |
| Scullery: take the rat poison (`found_poison`)         | 3         |
| Scullery: leave the rat poison                         | 7         |
| Garage (first visit + revisit) / gun room              | 3         |
| Floor crossing: descend (livery on at the threshold)   | 6, 7      |
| Floor crossing: descend is a no-op (livery worn early) | 3         |
| Floor crossing: ascend (change back among the guests)  | 3, 6, 7   |
| Billiard: first visit, with `host_lies` text           | 4, 6, 7   |
| Billiard: first visit, without `host_lies` text        | 5         |
| Billiard: revisit                                      | 6         |
| Billiard: leave the room                               | 4, 5, 6   |
| Captain's story → refill the flask (`drink_good_whisky`)| 5         |
| Captain's story → abstain (+ "whisky gone" text)       | 6         |
| Talk to Dr Baldwin (generic doctor menu)               | 5         |
| Butler: house / staff / about himself                  | 4         |
| Butler: the surprise (`butler_surprise`)               | 4         |
| **Ending: throat cut**                                 | 4         |
| **Ending: deathbed**                                   | 5         |
| **Ending: continue to Saturday morning**               | 1, 2, 3, 6, 7 |

---

## setup_broken_friday_evening_1.json
**Path**: Full host dinner conversation, then straight to bed.
- Walks the gated host chain background → invite → award, which unlocks
  `host_lies`, then her age and her room — the five questions exhaust the 90-unit
  dinner budget exactly, so the menu closes on its own.
- Map: retires immediately. `host_lies` alone triggers no ending, so the night
  ends with the continuation to Saturday morning.

## setup_broken_friday_evening_2.json
**Path**: Remaining host questions, then a sweep of the consequence-free rooms.
- Host: weather, the manor and the other guests, then the explicit exit.
- Map: tea room, dining room, garden, entrance hall, portrait gallery and
  library defaults, then the attic refusal and a bedroom refusal (each greys its
  whole group), and finally the servant stair where he leaves the livery on its
  peg. The nine 10-unit visits exhaust the map budget. Continues to Saturday.

## setup_broken_friday_evening_3.json
**Path**: Below stairs the hard way, never having caught the host lying.
- Map: tries the servants' floor with no disguise (turned back, greying the
  floor), finds and dons the footman's livery in the servant stair
  (`found_livery`), revisits the stair (livery now waiting on its peg), takes the
  rat poison from the scullery (`found_poison`), slips unseen out of the kitchen
  (no `host_lies`, so the maid is never approached), and looks over the garage
  (first visit then revisit) and the gun room. He is still in the livery at
  lights-out, so the chapter changes him back before bed. Continues to Saturday.

## setup_broken_friday_evening_4.json
**Path**: The butler investigation → **throat-cut ending**.
- Pre-unlocks `host_lies` and `talked_to_maid` so the butler conversation and its
  surprise question are both available.
- Map: goes to the billiard room and questions the butler about the house, the
  small staff, himself, and finally the surprise the maid mentioned — which
  unlocks `butler_surprise` and marks Moody. He never wakes.

## setup_broken_friday_evening_5.json
**Path**: The captain's story and the poisoned whisky → **deathbed ending**.
- Map: billiard room (without `host_lies`, so the cautious butler text shows),
  listens to the captain's Boxer Rebellion tale, charges his flask from the bar
  (`drink_good_whisky`, sharing a measure with Harring), then chats with Dr
  Baldwin before leaving. The special whisky is poisoned, so he dies in his
  sleep.

## setup_broken_friday_evening_6.json
**Path**: Billiard revisit, the safe whisky choice and the maid.
- Pre-unlocks `host_lies` and `found_livery`.
- Map: looks in on the billiard room and leaves, then returns (revisit text),
  this time listening to the captain but abstaining from the bar (the whisky is
  gone by the time he looks), then drops below stairs to the kitchen and
  questions the maid (`talked_to_maid`). Descends into the livery at the kitchen
  threshold and is changed back at lights-out. Continues to Saturday (neither
  fatal thread set).

## setup_broken_friday_evening_7.json
**Path**: The cautious below-stairs run.
- Pre-unlocks `host_lies` and `found_livery`.
- Map: leaves the rat poison where it stands, leaves the maid be, then comes back
  up to the tea room (changing out of the livery on the way) before retiring.
  Covers the "leave" side of the scullery and kitchen choices and an ascent in
  the middle of the map rather than only at lights-out. Continues to Saturday.
