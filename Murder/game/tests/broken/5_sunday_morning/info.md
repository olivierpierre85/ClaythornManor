# Broken - Sunday Morning (An Empty Manor)

Reached only from the Saturday-night vigil (found_poison path), so
`talked_to_maid`, `host_lies`, `drunk_letter`, `found_poison` and
`gather_everyone` are always unlocked. The staff and Lady Claythorn left by
motor car in the night. The watch ends at dawn and the Captain proposes the
seven-mile walk to the police station, but Miss Baxter and Miss Marsh cannot
manage the road, and neither Mr Manning nor the feverish doctor is fit for it.
The Captain therefore proposes that the two men go alone.

The chapter gates on the `ambushed` ENDING (intuition), not on a thread:

- **Without the intuition** there is no menu at all. Moody accepts the split
  -> the two-man walk -> `broken_day3_afternoon`.
- **With it** the argument menu (`broken_day3_morning_menu_convince`) opens
  straight away. It is a timed menu: 30 minutes of patience, and each of the
  four questions costs 10, so three questions may be put to the room before it
  stops listening. Two of them must be the right ones
  (`day3_morning_good_questions >= 2`).

- Two good questions -> `left_together` -> the whole party walks out.
- Fewer -> the argument is lost and the pair sets out. The menu may end either
  because the time ran out (three questions asked) or because the player took
  the exit choice, and the two produce different closing narration.
- Taking off the mask is a trap at any point: the Captain arrests the impostor,
  binds him to his bed and walks out alone -> `broken_ending_burned`.

Every plan except 4 leaves the chapter through `broken_day3_afternoon`, which
branches on `left_together` for the endings themselves.

TODO the four questions are placeholders. Only the Boxer Rebellion and the
culprit questions increment the counter, so the plans below will need their
`selected` text updated once the real questions are written (the `redirect`
targets should stay).

Plan 1 must remain first: it is the only plan that relies on `ambushed` still
being locked, and the runner's `soft_reset` never re-locks endings.

## setup_broken_sunday_morning_1.json
No intuition, no menus at all. The forced split -> the two-man walk.

## setup_broken_sunday_morning_2.json
`unlocked_endings: [ambushed]`. The Boxer Rebellion and the culprit questions
(both good) plus one weak one -> `left_together` -> the departure of six.

## setup_broken_sunday_morning_3.json
`unlocked_endings: [ambushed]`. Both weak questions and only one good one, so
the whole 30 minutes are spent -> the room stops listening -> the pair sets out.

## setup_broken_sunday_morning_4.json
`unlocked_endings: [ambushed]`. Take off the mask on the first question
-> arrested, tied to the bed -> `broken_ending_burned`.

## setup_broken_sunday_morning_5.json
`unlocked_endings: [ambushed]`. The intuition is there but the player argues
nothing and takes the exit choice with time still on the clock -> the pair sets
out.
