# Broken - Sunday Morning (An Empty Manor)

Reached only from the Saturday-night vigil (found_poison path), so
`talked_to_maid`, `host_lies`, `drunk_letter` and `found_poison` are always
unlocked. The staff and Lady Claythorn left by motor car in the night. Broken
finds the butler's keys by the door, the garage empty and the telephone dead,
and proposes walking the seven miles to the police station together. The
others refuse - only the Captain agrees.

The departure menu (`broken_day3_morning_menu_leave`) gates on the `ambushed`
ENDING (intuition), not on a thread:

- **Without the intuition** the only option is to set out with the Captain
  -> the two-man walk -> `broken_ending_ambushed` (both shot on the road).
- **With it** an extra option appears: lay everything before the others
  (the two letters, the poison, the unmasking). Everyone is convinced,
  `left_together` is unlocked -> the whole party walks out
  -> `broken_ending_walked_out`.

## setup_broken_sunday_morning_1.json
No intuition. Menu -> set out with the Captain -> `broken_ending_ambushed`.

## setup_broken_sunday_morning_2.json
`unlocked_endings: [ambushed]`. Menu -> the reveal (intuition option) ->
`left_together` -> the walk together -> `broken_ending_walked_out`.
