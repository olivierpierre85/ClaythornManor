# Broken - Sunday Morning (An Empty Manor)

Reached only from the Saturday-night vigil (found_poison path), so
`talked_to_maid`, `host_lies`, `drunk_letter`, `found_poison` and
`gather_everyone` are always unlocked. The staff and Lady Claythorn left by
motor car in the night. The watch ends at dawn and the Captain proposes the
seven-mile walk to the police station, but Miss Baxter and Miss Marsh cannot
manage the road, and neither Mr Manning nor the feverish doctor is fit for it.
The Captain therefore proposes that the two men go alone.

The chapter gates on the `massacre` ENDING (intuition), not on a thread:

- **Without the intuition** there is no menu at all. Moody accepts the split
  -> the two-man walk -> `broken_day3_afternoon`.
- **With it** the argument menu (`broken_day3_morning_menu_convince`) opens
  straight away. It is a timed menu: 30 minutes of patience, and each question
  costs 10, so three questions may be put to the room before it stops
  listening. Three questions are offered at present: the poison, the Boxer
  Rebellion and the culprit. `..._question_letters` is written but not yet
  wired into the menu.

There is only one winning line, and it runs through the mask:

1. `..._question_boxer` — needs the `doctor_boxer` observation. Four of them
   served in the Boxer Rebellion, which is too many for a coincidence.
2. `..._question_culprit` — only offered once the Boxer question has been
   asked. If Lady Claythorn did not write the letters then nobody may be
   crossed off, so a shut door behind four people is worse than an open road.
   Miss Baxter answers it by claiming she saw beneath the mask in the night,
   which opens `broken_day3_morning_menu_mask` with four answers.
3. `..._mask_honour` — plead a soldier's honour. Captain Sinha takes his part,
   the mask stays on, the argument is won: the label sets `early_exit` on the
   convince menu so the room stops listening, and `left_together` is unlocked.

Every other answer to the mask demand falls through to `..._mask_removed`
(shared), then the arrest and `broken_ending_burned`:

- `..._mask_frighten` — plead the horror of the face, which brings Doctor
  Baldwin forward offering to look alone. Refusing him would say the thing
  plainly, so the mask comes off anyway.
- `..._mask_decency` — take offence. Nobody buys it with a dead man upstairs.
- `..._show_face` — take it off at once.

`..._question_poison` carries no weight at all now. It is there to be spent.

- Honour pleaded -> `left_together` -> the whole party walks out.
- Anything else -> the pair sets out.

The chapter still has two closing narrations for the lost argument, one for the
clock running out and one for the player taking the exit choice. With only
three questions in the menu the clock branch is currently unreachable: the
poison and the Boxer question spend 20 of the 30 minutes, and the only thing
left to spend the last 10 on is the culprit question, which either wins the
argument or ends in `broken_ending_burned`. Wiring `..._question_letters` back
into the menu would make that branch reachable again.

Every plan except 4, 6 and 7 leaves the chapter through `broken_day3_afternoon`,
which branches on `left_together` for the endings themselves.

Plan 1 must remain first: it is the only plan that relies on `massacre` still
being locked, and the runner's `soft_reset` never re-locks endings.

## setup_broken_sunday_morning_1.json
No intuition, no menus at all. The forced split -> the two-man walk.

## setup_broken_sunday_morning_2.json
`unlocked_endings: [massacre]`, `doctor_boxer` unlocked. The winning line:
Boxer -> culprit -> the mask answered on a soldier's honour -> the menu
early-exits with 10 minutes still on the clock -> `left_together` -> the
departure of six.

## setup_broken_sunday_morning_3.json
`unlocked_endings: [massacre]`, `doctor_boxer` unlocked. The poison and the
Boxer question, then the exit with 10 minutes still on the clock. The culprit
question is offered after the Boxer one but never asked -> the pair sets out.

## setup_broken_sunday_morning_4.json
`unlocked_endings: [massacre]`, `doctor_boxer` unlocked. Reach the culprit
question, then take the mask off at once -> arrested, tied to the bed ->
`broken_ending_burned`.

## setup_broken_sunday_morning_5.json
`unlocked_endings: [massacre]`. The intuition is there but the player argues
nothing and takes the exit choice with time still on the clock -> the pair sets
out.

## setup_broken_sunday_morning_6.json
`unlocked_endings: [massacre]`, `doctor_boxer` unlocked. Reach the culprit
question, then plead the horror of the face. Doctor Baldwin offers to look
alone, which cannot be refused -> the mask comes off -> `broken_ending_burned`.

## setup_broken_sunday_morning_7.json
`unlocked_endings: [massacre]`, `doctor_boxer` unlocked. Reach the culprit
question, then plead common decency. Nobody buys it with a dead man upstairs
-> the mask comes off -> `broken_ending_burned`.
