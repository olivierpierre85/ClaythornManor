# Broken - Saturday Evening (after the hunt)

Reached only from the western grove path of the hunt (`broken_day2_hunt_drunk`
with `drunk_letter` drawn out), so only Ted Harring is dead. The party returns,
the police are delayed by a fallen tree, and a quiet dinner follows.

The chapter gates on `found_poison` (the scullery bottle from Friday night):

- **Without it** Broken retires after dinner and the manor burns in the night
  -> `broken_ending_burned`.
- **With it** he refuses to sleep: a map exploration follows (the billiard
  room holds Captain Sinha and a sober Mr Manning), then the night vigil -
  he watches the staff's motor car leave at four in the morning and goes on
  to `broken_day3_morning`.

Choices:
1. **Dinner** (`broken_day2_evening_menu_dinner`):
   - `broken_day2_evening_dinner_manning` — a quiet word with Mr Manning
     (seeds the partnership).
   - `generic_cancel` — keep his own counsel.
2. **Map** (`broken_day2_evening_map_menu`, found_poison only): ground-floor
   rooms plus the billiard room (`broken_day2_evening_billiard_menu` -> the
   Captain's menu `broken_captain_night_menu` and Manning's menu
   `broken_drunk_night_menu`). Early exit: take up the watch for the night.

## setup_broken_saturday_evening_1.json
`talked_to_maid`, `host_lies`, `drunk_letter` (no `found_poison`). Dinner menu
-> keep his own counsel. He drinks the wine, retires and burns
-> `broken_ending_burned`.

## setup_broken_saturday_evening_2.json
Same threads plus `found_poison`. Dinner menu -> speak to Mr Manning. Map ->
billiard room (Captain: tomorrow question, Manning: the letters), then take up
the watch. The run continues into Sunday morning (no intuition, so the only
option is to leave with the Captain) and ends at `broken_ending_ambushed`.
