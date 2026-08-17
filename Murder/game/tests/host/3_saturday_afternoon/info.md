# Saturday Afternoon — The Hunt — Test Plans

Lady Claythorn takes a rifle from the gun room, is paired off with Captain
Sinha and the butler for the north field, misses a pheasant, then decides what
to do about a rabbit sitting still at twenty paces. Luncheon in the clearing,
two shots from the western grove, and Doctor Baldwin is found dead in the fern.

The chapter has a single menu, `host_day2_hunt_menu_rabbit`, and one thread read
twice, `found_poison`, so the four plans below are the full matrix.

Shared beats come from `_common/Day 2/2_Hunt/`:
`common_day2_hunt_butler_groups`, `common_day2_hunt_pairing`,
`common_day2_hunt_groups_assigned`, `common_day2_hunt_luncheon_served`,
`common_day2_hunt_shots_heard` and `common_day2_hunt_doctor_aftermath`. None of
them holds a menu, and the last three branch on `current_character.text_id`, so
every plan exercises the `"host"` side of those branches.

The chapter ends when the script jumps to `host_day2_evening`, which calls
`change_time` with `chapter='saturday_evening'` so the test runner detects the
chapter change.

---

## setup_host_saturday_afternoon_1.json
**Path**: No threads pre-unlocked, the rabbit is offered to the Captain.
- Skips both `found_poison` paragraphs (the scullery bottle at the waking, and
  the three-deaths reflection on the walk back).
- `host_day2_hunt_rabbit_offer`: the Captain misses a sitting target, she keeps
  `terrible_shot` locked and learns he cannot shoot either.

## setup_host_saturday_afternoon_2.json
**Path**: No threads pre-unlocked, she fires at the rabbit herself.
- `host_day2_hunt_rabbit_shoot`: she misses by a yard in front of the Captain
  and the butler, which unlocks `terrible_shot`.
- The `terrible_shot` thread is what lets Captain Sinha press her in
  `host_day2_evening`, so this is the plan that feeds the evening's accusation.

## setup_host_saturday_afternoon_3.json
**Path**: `found_poison` pre-unlocked, she fires at the rabbit herself.
- Covers both `found_poison` branches: the bottle coming back to her while she
  dresses, and the count of the deaths on the walk home.
- Same rabbit branch as plan 2, so `terrible_shot` is unlocked here too.

## setup_host_saturday_afternoon_4.json
**Path**: `found_poison`, `go_downstairs` and `family_history` pre-unlocked, the
rabbit is offered to the Captain.
- The Friday threads carry no branch of their own in this chapter, they are set
  so the plan matches the state a player who explored on Friday actually reaches
  the hunt with.
- Both `found_poison` paragraphs fire, and `terrible_shot` stays locked.
