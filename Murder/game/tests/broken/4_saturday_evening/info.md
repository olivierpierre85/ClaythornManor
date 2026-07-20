# Broken - Saturday Evening (after the hunt)

Reached only from the western grove path of the hunt (`broken_day2_hunt_drunk`
with `drunk_letter` drawn out), so only Ted Harring is dead. The party returns,
the police are delayed by a fallen tree, and a quiet dinner follows.

The chapter has two gates:

1. **`found_poison` at dinner** (the scullery bottle from Friday night):
   without it the bottle stayed where the killer left it, the meal is
   poisoned and every guest collapses -> `broken_ending_poisoned`.
2. **`gather_everyone` at night**: after dinner a night map opens
   (`broken_day2_evening_map_menu`). The whole point of the night is to win
   the Captain over in the billiard room. Three facts gathered around the
   house each open a question for him - the staff are gone (`staff_missing`),
   the telephone is dead (`phone_dead`), and Mr Manning will stand with him
   (`drunk_partner`). Once both house facts have been told
   (`day2_evening_captain_facts` reaches 2) he is `captain_convinced`, and
   with Manning already onside the last question appears: **Show him the
   order**. That scene wins his trust, he proposes ringing the dinner gong,
   and the gong is rung straight from it
   (`broken_day2_evening_captain_order` calls `broken_day2_evening_ring_gong`
   - never from the map). Ringing it unlocks `gather_everyone` and the run
   goes on to `broken_day3_morning` (the test stops at that chapter
   boundary). Turning in without it -> `broken_day2_evening_failed` ->
   `broken_ending_impaled`.

Menus:
1. **Dinner** (`broken_day2_evening_menu_dinner`): as on Friday, only the
   hostess is within talking distance at the table. Both choices exit the
   table at once (`early_exit`).
   - `broken_day2_dinner_host` — speak to Lady Claythorn (opens the
     `host_generic_menu_broken` conversation).
   - `generic_cancel` — keep to yourself.
2. **Night map** (`broken_day2_evening_map_menu`): the Friday board, but at
   night and with the servants' floor open and deserted. Gathering the
   facts:
   - `staff_missing` needs four staff-oddity marks - the kitchen, scullery,
     gun room and attic each add one (`broken_day2_evening_staff_oddity`);
     the garage carries no clue and stays out of the count.
   - `phone_dead` - the entrance-hall telephone is tried and found dead.
   - The first crossing below stairs (servant stair or any basement room,
     whichever comes first) plays the no-pretence reflection once
     (`day2_evening_no_pretence`).
   - The bedroom doors each have their own dead-end scene (the doctor won't
     wake, the others answer through the wood or not at all); Ted Harring's
     room holds the single rose.
   - Early exit: "Turn in for the night".
3. **Billiard room** (`broken_day2_evening_billiard_menu`, built in
   `broken_day2_evening_billiard_room_scene`): Captain Sinha reads and Mr
   Manning drinks.
   - "Sit with Mr Manning" -> `broken_day2_evening_billiard_drunk`, the
     gratitude exchange that unlocks `drunk_partner`.
   - "Join Captain Sinha" -> the Captain's sub-menu
     (`broken_captain_night_menu`): small talk about the tree and Harring's
     death, then "Tell him the staff are gone" / "Tell him the telephone is
     dead" once those facts are in hand, and finally "Show him the order"
     once `captain_convinced` and `drunk_partner` are both set.
   - "Leave the room".

## setup_broken_saturday_evening_1.json
`talked_to_maid`, `host_lies`, `drunk_letter` (no `found_poison`). Dinner menu
-> keep to yourself. The meal is poisoned and he collapses with the rest
-> `broken_ending_poisoned`.

## setup_broken_saturday_evening_2.json
Same threads plus `found_poison`. Dinner -> speak to Lady Claythorn (immediate
exit from her generic menu). Night map -> the four staff-oddity rooms (kitchen,
scullery, gun room, attic) unlock `staff_missing`, and the entrance hall
unlocks `phone_dead`. Billiard room -> sit with Mr Manning (`drunk_partner`),
then join the Captain and tell him both house facts (`captain_convinced`), then
show him the order. He proposes the gong and it is rung from that scene,
unlocking `gather_everyone`. Leaving the room and turning in ends the night map,
and the run goes on to `broken_day3_morning` (the test stops at the
`sunday_morning` chapter boundary).

## setup_broken_saturday_evening_3.json
Same threads as 2 (`found_poison` unlocked), but he turns in for the night
straight away without gathering anyone -> `broken_day2_evening_failed` ->
`broken_ending_impaled`.

## setup_broken_saturday_evening_4.json
Same threads as 2 (`found_poison` unlocked). A fuller but still failing night:
the entrance hall (`phone_dead`), the servant stair (the no-pretence
reflection) and the garage, then the billiard room for the Captain's small talk
(the tree and Harring's death) and Mr Manning's gratitude exchange
(`drunk_partner`). The house facts are never brought to the Captain, so he is
never convinced and the gong is never rung. Turning in ->
`broken_day2_evening_failed` -> `broken_ending_impaled`.

## setup_broken_saturday_evening_5.json
Dialogue coverage (dinner conversation + ground floor). Speak to Lady Claythorn
and work through the linked chain of her generic menu - the weather, then
"Tell me more about yourself" which opens "Why did you invite us here?", which
in turn opens "Have you been giving this prize away for long?" (the dinner
clock runs out on that last answer and closes the conversation). Then the night
map walks the ground floor rooms that have their own narration - the tea room,
the dining room, the garden, the portrait gallery and the library - and looks
in on the billiard room twice to play its re-visit narration (the "I look in
again" branch). Nothing is gathered and the gong is never rung, so turning in
-> `broken_ending_impaled`.

## setup_broken_saturday_evening_6.json
Dialogue coverage (remaining host questions + every bedroom door). Speak to
Lady Claythorn and ask the standalone questions her menu never gates - the
other guests, the manor, her age and her room - then take the exit. The night
map then knocks at all seven bedroom doors in turn (host, nurse, doctor, drunk,
psychic, captain and Ted Harring's room with the single rose), each its own
dead-end scene. Turning in -> `broken_ending_impaled`.

## setup_broken_saturday_evening_7.json
Convincing the Captain in the other order, to cover the branches setup 2 skips.
Same threads as 2 (`found_poison`). Gather `staff_missing` (kitchen, scullery,
gun room, attic) and `phone_dead` (entrance hall), then in the billiard room
join the Captain *first* and tell him both house facts before speaking to Mr
Manning - so the convinced check fires its "one last thing, see if Manning will
go along" branch rather than the "he will go with me" one. Leave the Captain,
sit with Mr Manning (`drunk_partner`), then re-approach the Captain (the
re-approach else-branch) and show him the order. The gong is rung,
`gather_everyone` unlocks, and the run goes on to `broken_day3_morning`.
