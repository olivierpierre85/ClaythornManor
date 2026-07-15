# Broken - Saturday Evening (after the hunt)

Reached only from the western grove path of the hunt (`broken_day2_hunt_drunk`
with `drunk_letter` drawn out), so only Ted Harring is dead. The party returns,
the police are delayed by a fallen tree, and a quiet dinner follows.

The chapter has two gates:

1. **`found_poison` at dinner** (the scullery bottle from Friday night):
   without it the bottle stayed where the killer left it, the meal is
   poisoned and every guest collapses -> `broken_ending_poisoned`.
2. **`gather_everyone` at night**: after dinner a night map opens
   (`broken_day2_evening_map_menu`). Warning the Captain and Mr Manning in
   the billiard room (the watch proposal) AND calling at every occupied
   bedroom door (doctor, psychic, nurse, host) unlocks `gather_everyone`. Turning
   in without it -> `broken_ending_impaled`. With it the watch holds, Broken
   takes the small-hours shift, sees the motor car leave at four, and goes
   on to `broken_day3_morning`.

Choices:
1. **Dinner** (`broken_day2_evening_menu_dinner`): as on Friday, only the
   hostess is within talking distance at the table.
   - `broken_day2_dinner_host` — speak to Lady Claythorn (opens the
     `host_generic_menu_broken` conversation).
   - `generic_cancel` — keep his own counsel.
2. **Night map** (`broken_day2_evening_map_menu`): the Friday board, but at
   night. The billiard room (`broken_day2_evening_billiard_menu`) holds Captain Sinha
   (reading; menu `broken_captain_night_menu`) and Mr Manning (drinking;
   menu `broken_drunk_night_menu`; the first approach plays the gratitude
   exchange that seeds the partnership), plus the watch proposal
   (`broken_day2_evening_propose_watch`). The bedroom doors each have their
   own scene (the doctor won't wake, the psychic and the nurse answer
   through the wood, the host puts her light out). The entrance hall pays
   off the telephone he resolved to try - the line is dead (unlocks
   `phone_dead`). The servants' floor stands open tonight and deserted: the
   first visit to the servant stair or to any room below stairs (whichever
   comes first) plays the no-pretence reflection once
   (`day2_evening_no_pretence`). The kitchen, scullery and gun room each add
   one staff-oddity mark (`day2_evening_staff_oddities`), and the third mark
   unlocks `staff_missing` - the garage carries no clue and stays out of the
   count. Early exit: turn in for the night.

## setup_broken_saturday_evening_1.json
`talked_to_maid`, `host_lies`, `drunk_letter` (no `found_poison`). Dinner menu
-> keep his own counsel. The meal is poisoned and he collapses with the rest
-> `broken_ending_poisoned`.

## setup_broken_saturday_evening_2.json
Same threads plus `found_poison`. Dinner menu -> speak to Lady Claythorn
(immediate exit from her generic menu). Map -> billiard room (Captain: tomorrow
question; Manning: the gratitude exchange on approach, then the letters),
the watch proposal, then all four occupied bedroom doors (gather_everyone
unlocks on the last), then turn in. The run continues into Sunday morning
(no intuition, so the only option is to leave with the Captain) and ends at
`broken_ending_ambushed`.

## setup_broken_saturday_evening_3.json
Same threads as 2 (`found_poison` unlocked), but he turns in for the night
straight away without gathering anyone -> `broken_ending_impaled`.
