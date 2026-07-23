# Broken - Sunday Morning (An Empty Manor)

Reached only from the Saturday-night vigil (found_poison path), so
`talked_to_maid`, `host_lies`, `drunk_letter`, `found_poison` and
`gather_everyone` are always unlocked. The staff and Lady Claythorn left by
motor car in the night. The watch ends at dawn and the Captain proposes the
seven-mile walk to the police station, but Miss Baxter and Miss Marsh cannot
manage the road, Mr Manning is no better, and the doctor has a fever. The
doctor and Mr Manning stay to look after the ladies, and the Captain quietly
proposes that the two men go alone.

The chapter gates on the `ambushed` ENDING (intuition), not on a thread:

- **Without the intuition** there is no menu at all. Moody accepts the split
  -> the two-man walk -> `broken_ending_ambushed` (both shot on the road).
- **With it** the departure menu (`broken_day3_morning_menu_leave`) opens:
  set out with the Captain anyway, or refuse to be split.

Refusing opens the argument menu (`broken_day3_morning_menu_convince`). The
budget allows three of the four questions before the room stops listening, and
two of them must be the right ones (`day3_morning_good_questions >= 2`).

- Two good questions -> `left_together` -> the whole party walks out
  -> `broken_ending_walked_out`.
- Fewer -> the argument is lost, the pair sets out -> `broken_ending_ambushed`.
- Taking off the mask is a trap at any point: the Captain arrests the impostor,
  binds him to his bed and walks out alone -> `broken_ending_burned`.

TODO the four questions are placeholders. Only the Boxer Rebellion and the
culprit questions increment the counter, so the plans below will need their
`selected` text updated once the real questions are written (the `redirect`
targets should stay).

Plan 1 must remain first: it is the only plan that relies on `ambushed` still
being locked, and the runner's `soft_reset` never re-locks endings.

## setup_broken_sunday_morning_1.json
No intuition, no menus at all. The forced split -> `broken_ending_ambushed`.

## setup_broken_sunday_morning_2.json
`unlocked_endings: [ambushed]`. Refuse the split, then the Boxer Rebellion and
the culprit questions (both good) plus one weak one -> `left_together` -> the
walk together -> `broken_ending_walked_out`.

## setup_broken_sunday_morning_3.json
`unlocked_endings: [ambushed]`. Refuse the split, then both weak questions and
only one good one -> the argument is lost -> `broken_ending_ambushed`.

## setup_broken_sunday_morning_4.json
`unlocked_endings: [ambushed]`. Refuse the split, then take off the mask
-> arrested, tied to the bed -> `broken_ending_burned`.

## setup_broken_sunday_morning_5.json
`unlocked_endings: [ambushed]`. The intuition is there but the player ignores
it and sets out with the Captain anyway -> `broken_ending_ambushed`.
