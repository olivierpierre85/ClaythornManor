# Broken - Saturday Afternoon (The Hunt)

Broken joins the hunt. With `talked_to_maid` the chapter opens up; without it,
the path is forced (north field, then a forced kill of the Captain).

Choices (all gated on `talked_to_maid`):
1. **Which party** (`broken_day2_hunt_menu_party`):
   - `broken_day2_hunt_north` — shadow the Captain in the north field.
   - `broken_day2_hunt_western_grove` — shadow the Drunk with the Doctor.
2. **North path** (`broken_day2_hunt_menu_revenge`): spare or kill the Captain.
   Two of the Captain's actions stoke Broken's anger; `host_lies` tempers the
   shooting beat.
3. **Grove path**: the Drunk generic menu (`drunk_generic_menu_broken`) carries
   a letter question. Asking it unlocks the `drunk_letter` thread (Manning was
   turned against the Doctor the same way Broken was turned against the
   Captain) and saves both the Drunk and the Doctor.

The north-field hunt and the kill are shared with the Captain's storyline
(`common_day2_hunt_pairing`, `common_day2_hunt_north_field`,
`common_day2_hunt_captain_confrontation`).

Both north-field outcomes are death endings: KILL -> `broken_ending_silenced`
(the butler strangles him over the Captain's body), SPARE ->
`broken_ending_overtaken` (the butler catches him in the rush). Only the grove
save lets Broken live.

## setup_broken_saturday_afternoon_1.json
No threads. No menus: forced north field, forced kill -> `broken_ending_silenced`.
(`choices: []`)

## setup_broken_saturday_afternoon_2.json
`talked_to_maid`. Party menu -> north; revenge menu -> KILL ->
`broken_ending_silenced`.

## setup_broken_saturday_afternoon_3.json
`talked_to_maid`. Party menu -> north; revenge menu -> SPARE ->
`broken_ending_overtaken`.

## setup_broken_saturday_afternoon_4.json
`host_lies` only (no `talked_to_maid`). The shooting beat is tempered, but with
no maid warning there is no menu: forced north field, forced kill ->
`broken_ending_silenced`. (`choices: []`)

## setup_broken_saturday_afternoon_5.json
`talked_to_maid`. Party menu -> western grove; drunk menu -> the letter
question, unlocking `drunk_letter` and the save-the-Drunk resolution.
