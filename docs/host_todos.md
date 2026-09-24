# Host (Lady Claythorn) — TODOs from the test transcripts

Findings from a full read of the 29 host test transcripts (`Murder/game/tests/host/*/*.txt`, Friday afternoon to Sunday afternoon), cross-checked against the scripts and the hidden-info audit (`python Murder/check_description_hidden_unlocks.py --diff`), 2026-09-24.

Script paths are relative to `Murder/game/scripts/`. Line numbers are as of that date; `~` means approximate. Lines in `_common/` are shared with other routes, so the change shows up there too.

---

## A. Logic errors in the dialogue

| Done | # | Where | Problem | Fix | File |
|---|---|---|---|---|---|
| [ ] | A1 | Fri eve, library | "fifty-nine… I have been telling myself all evening that I look my age" is unclear, and clashes with the nurse's "you look so young" | "Which makes me fifty-nine years old, a good deal older than I am. I can only hope the lamps are kind to me." | `host/Day 1/2_Evening/0_map_choices.rpy:330` |
| [ ] | A2 | Sat morning | "The butler enters the room and comes directly towards me. I did not even notice him come in." contradicts itself | "The butler is suddenly at my elbow." (keep the second line) | `host/Day 2/1_Morning/1_main.rpy:~86` |
| [ ] | A3 | Sat morning | The doctor is "examining him right now", then she questions him downstairs in the next beat, with no transition | Add a narration beat before the question, e.g. "Some minutes later, Doctor Baldwin comes back down." Check it reads correctly for the other callers | `_common/Day 2/1_Morning/1_main.rpy:~74` |
| [ ] | A4 | Hunt | "Nobody answers me." Then the butler answers | "For a moment, nobody answers me." | `host/Day 2/2_Hunt/1_main.rpy:162` |
| [ ] | A5 | Hunt | "He smiles at me… But I am certain he noticed my shot": both "he" read as the butler, but the second should be the Captain | "…certain the Captain noticed how poor my shot was." | `host/Day 2/2_Hunt/1_main.rpy:178` |
| [ ] | A6 | Hunt | "He is… he is truly dead?" is asked before anyone has said he is dead | "Is he… is he dead?" | `_common/Day 2/2_Hunt/5_doctor_death.rpy:160` |
| [ ] | A7 | Hunt, walk back | "came back only minutes before those shots" reads as an alibi, not a suspicion | Add: "…as though he wished to be seen with us when they were." | `host/Day 2/2_Hunt/1_main.rpy:255` |
| [ ] | A8 | Sat eve | She "draws the butler aside and keeps her voice down", yet Baxter and Marsh join the conversation, with Manning in the room | Drop the whisper. Host: "I turn to the butler, too tired to be discreet." Others: "Lady Claythorn turns to her butler." | `_common/Day 2/3_Evening/1_main.rpy:168,174` |
| [ ] | A9 | Sat dinner | The drinks are announced in the dinner speech, then again as "the last line on the butler's paper" | "The plates go out, and I remind them of the drinks in the billiard room, as the paper tells me to. I hear how it sounds in that room." | `host/Day 2/3_Evening/1_main.rpy:239-241` |
| [x] | A10 | Sat eve, bested path | The Captain has just accused her in public, and the butler's visit to her room ignores it | Add an `if bested_captain` exchange at the start of his visit (2–4 lines: he acknowledges the tea room and says the Captain will not try again) | `host/Day 2/3_Evening/1_main.rpy:~77` |
| [x] | A11 | Sat eve, truth to the Captain | "I came to this manor with two other actors" contradicts Friday, when she arrived with the butler and the other two were already there | "Then I came to this manor, where two other actors were waiting to play the footman and the maid you saw this weekend." | `host/Day 2/3_Evening/3_billiard_room.rpy:150` |
| [x] | A12 | Same scene | "First, I am not Lady Claythorn… I'm an actress…" is written as narration, but he "flinches at this revelation", so she says it aloud | Give the four lines to the `host` speaker | `host/Day 2/3_Evening/3_billiard_room.rpy:120-123` |
| [x] | A13 | Same scene | "The reason… remained evasive" (a reason cannot be evasive). "Earlier today the butler claimed": it was after dinner | "He was evasive about the reason, and only told me it was a prank of sorts." / "After dinner, the butler claimed…" | `host/Day 2/3_Evening/3_billiard_room.rpy:142`, `:340` |
| [x] | A14 | Tea room, title answer | "My father… as a great many did after the war": the 3rd Earl was born in 1813 and would be 105 by 1918 | "My father had no patience for ceremony, and preferred that we be known by the house." | `host/Day 2/3_Evening/2_captain_accusation.rpy:49` |
| [ ] | A15 | Tea room, confession | Confessing plays the refusal lead-in "I have nothing left to give him that anybody would believe", which is false when she holds the title | Keep those two lines in the refusal branch only. Give the confession its own lead-in: "I could give him the name from the book. But I have no more lies left in me." | `_common/Day 2/3_Evening/3_captain_host_confrontation.rpy:~209` |
| [ ] | A16 | Ending `shot_tea_room` | "you could not give it to him" is wrong for the confession path | "…and you did not give it to him." | `host/host_endings.rpy:13` |
| [x] | A17 | Car path | "They come out to me… over the next hour" breaks the "in the car by eleven" deadline | "…one at a time, and none of them says a word to me." | `host/Day 2/3_Evening/1_main.rpy:514` |
| [x] | A18 | Ending `shot_in_car` | "a man you barely knew", but he is her "old acquaintance" | "…with a man you had never really known." | `host/host_endings.rpy:53` |
| [x] | A19 | Sat eve, the maid | "I am nearly ready, I promise." gets the reply "No need to apologise." | "No need to hurry." | `host/Day 2/3_Evening/0_map_choices.rpy:448` |
| [ ] | A20 | Sat eve, the doctor laid out | "still in the coat he was shot in", but the jackets went to the stretcher and his shirt was torn open | "…still in the clothes he was shot in." | `host/Day 2/3_Evening/0_map_choices.rpy:355` |
| [ ] | A21 | Sun waking | "It would not be fair to let him in there." | "…to leave him in there." | `host/Day 3/1_Morning/1_main.rpy:152` |
| [x] | A22 | Sun waking | "I do not want to see their face when they learn what we know" is the wrong reason for keeping quiet | "If one of them is behind this, I would rather they did not learn what we know." | `host/Day 3/1_Morning/1_main.rpy:166` |
| [ ] | A23 | Sun, entrance hall | "I can hear Ted Harring and Amelia Baxter" is said after the voices have gone | "That was Ted Harring and Amelia Baxter." | `host/Day 3/1_Morning/0_map_choices.rpy:95` |
| [x] | A24 | Sun, garden | With `saw_car` set, the Captain still says "If we had a car", although she told him about the tourer at waking | Add a `saw_car` branch: "If that tourer of yours will run, this will take us to the town." / host: "Then let us go and look at it." Change the plain branch's "Good, let us…" to "Then let us keep looking." | `host/Day 3/1_Morning/0_map_choices.rpy:398-406` |
| [x] | A25 | Sun noon, car | "I stand at the garage door…", then "We reach the garage from outside." The order is reversed | Move "We reach the garage from outside." ahead of the shed line | `host/Day 3/2_Afternoon/1_main.rpy:~154-158` |
| [x] | A26 | Sun, dining room | Manning: "if it looked as though I had killed myself". There was no blade, and they read it as murder behind a locked door | **Changed direction:** the body now reads as a suicide in every route (razor on the floor beneath his hand, door still locked), so Manning's line stands, plus "I staged it with port wine and my own razor." Rewritten: `_common/Day 3/1_Morning/3_lad_psychic_captain_meeting.rpy`, captain solo find and report (`captain/Day 3/1_Morning/0_map_choices.rpy`, `2b_explore.rpy`), host find (`host/Day 3/1_Morning/0_map_choices.rpy`), lad escape, nurse's hearsay (`_common/Day 3/2_Afternoon/2_lad_stay_with_psychic.rpy`), drunk config and outline | `host/Day 3/2_Afternoon/2_attic.rpy:287,307` |
| [x] | A27 | Sat eve | "He knocks and enters" has no antecedent after the scene change | "The butler knocks and enters…" | `host/Day 2/3_Evening/1_main.rpy:74` |
| [x] | A28 | Fri dinner | Manning's wife answer is still `TODO` and shows on screen | Write it in Manning's voice (drunk, lucid for a moment): a routine operation, young and healthy, the surgeon's hands unsteady that morning. No names, since he does not know it is Baldwin yet | `drunk/drunk_generic_choices.rpy:545-557` |

## B. Hidden-info wiring (audit `--diff`)

- [ ] **B1** Moody's `background`, `job` and `city` are declared **only** for `('host','friday_evening')`, and nothing unlocks them, so nobody can ever get them. His dinner line ("boot boy and then footman… pension in Liverpool") is the right place: add `broken_details.description_hidden.unlock('background')` / `'job'` / `'city'` after it (`host/Day 1/2_Evening/1_main.rpy:~303`).
- [ ] **B2** The host's question unlocks Manning's `wife`, but `('host','friday_evening')` is missing from its `unlock_chapters` (`drunk/drunk_config.rpy:147`).
- [ ] **B3** Manning's `lie` is declared for `('host','sunday_afternoon')` but never unlocked. His sober confession in the dining room is exactly that info: add `unlock('lie')` next to `faked_death` (`host/Day 3/2_Afternoon/2_attic.rpy:316`).
- [x] **B4** The butler's `took_valuables` is declared for `('host','sunday_afternoon')` and never unlocked. Unlock it at the empty silver cabinet in Sunday morning's butler room, and change the pair to `('host','sunday_morning')` (`host/Day 3/1_Morning/0_map_choices.rpy`, `butler/butler_config.rpy:21`).
- [x] **B5** Smaller declaration fixes:
  - The butler's `job` and `name` are unlocked on Friday afternoon but not declared: add `('host','friday_afternoon')` (`butler/butler_config.rpy:17,22`).
  - The host's own `lie` is unlocked on Saturday evening but not declared: add `('host','saturday_evening')` (`host/host_config.rpy:184`).
  - The host's `car` is declared for Sunday afternoon and never unlocked: remove it, or unlock it in the escape where the Captain drives (`host/host_config.rpy:182`). **Done:** she now takes the wheel in the escape ("Better than I shoot, Captain.") and `car` is unlocked there.

## C. Grammar, spelling, British English and period (host files)

- [x] Fri afternoon `host/Day 1/1_Afternoon/1_main.rpy:158`: "cannot look more than eighteen" → "cannot be more than eighteen"
- [x] Fri eve `host/Day 1/2_Evening/1_main.rpy:54`: "I come to see" → "I have come to see"
- [x] Fri eve `host/Day 1/2_Evening/0_map_choices.rpy:169`: "a Chekhov's play" → "a Chekhov play"
- [x] Fri eve `host/Day 1/2_Evening/2_billiard_room.rpy:53`: "it has gotten rather late" → "it is getting rather late"
- [x] Sat morning `host/Day 2/1_Morning/1_main.rpy:62`: "fix myself a plate" → "help myself from the sideboard"
- [x] Hunt `host/Day 2/2_Hunt/1_main.rpy:263`: "My mind goes into a race." → "My mind begins to race."
- [x] Sat eve `host/Day 2/3_Evening/1_main.rpy`:
  - `:130` butler "Great." → "Good."
  - `:328` "But what if they are not." → add "?"
  - `:524` "They must be all in their room" → "They must all be in their rooms"
- [x] Sat eve `host/Day 2/3_Evening/0_map_choices.rpy:310`: "I guess he is already asleep" → "I suppose…"
- [x] Sat eve `host/Day 2/3_Evening/3_billiard_room.rpy`:
  - `:342` "the phone is down" → "the telephone is dead"
  - `:416` "You are right, me neither." → "Nor shall I."
  - `:461` remove the stray comma after "we agree"
- [x] Accusation `host/Day 2/3_Evening/2_captain_accusation.rpy`:
  - `:120` "talked like that" → "spoken to like that"
  - `:124` "the right of making" → "the right to make"
  - `:128` "this not an answer" → "this is not an answer"
  - `:130` → "I doubt it would cost you much to simply name your title."
- [x] Sun morning `host/Day 3/1_Morning/1_main.rpy`:
  - `:49` "eerly" → "eerily"
  - `:55` "The staff is gone, we are on our own." → "The staff are gone. We are on our own."
  - `:87` "Well, I guess now there is daylight" → "Well, now that it is daylight"
  - `:158` "Alright" → "All right"
  - `:162` "Ver well." → "Very well."
- [x] Sun morning `host/Day 3/1_Morning/0_map_choices.rpy:416`: "Great! Now we can finally leave." → "Then we can leave at last."
- [x] Sun afternoon `host/Day 3/2_Afternoon/1_main.rpy`:
  - `:67` "for three days" → "all weekend"
  - `:202` "hopped on the first train going south" → "caught the first train south"
- [x] Sun afternoon `host/Day 3/2_Afternoon/2_attic.rpy`:
  - `:33` "Weird, I was expecting he argue…" → "Strange. I expected him to argue…"
  - `:35` "I guess" → "I suppose"

## D. Shared `_common` lines (also change other routes)

- [x] `_common/Day 1/2_Evening/1_main.rpy`:
  - `:197` "hundred of men" → "hundreds of men"
  - `:205` "civilized" → "civilised"
- [x] `_common/Day 2/1_Morning/2_follow.rpy`:
  - `:84` "Dead?!!!" → "Dead?"
  - `:98` "Please, My Lady—this way." → "Please, my lady, this way."
- [x] `_common/Day 2/3_Evening/1_main.rpy`:
  - `:12` the Captain's "I'm sorry, dear, but he is." → "I am sorry, Miss Baxter, but he is.", which fits his formal voice
  - `:42` "anyone from the city" → "anyone from the police"
  - `:322` "Mr Sinha" → "Captain Sinha"
  - `:341-343` "What a sad business. But, sadly, there is nothing else…" → "…But I am afraid there is nothing else to be done at the moment."
  - `:358` "come sit next to me" → "come and sit next to me"
- [x] `_common/Day 2/3_Evening/3_captain_host_confrontation.rpy`:
  - `:253` "I was hired for being here." → "I was hired to be here."
  - `:301` → "He answers directly to whoever is behind this."
  - `:457` "week-end" → "weekend"
  - `:467` → "You will all go to your rooms, and you will give me your keys as I lock the doors behind you."

## E. Flagged only (no change planned)

- **`die_in_sleep`:** nothing explains the death. The chair is wedged under the handle, and in the `found_poison` branch she has not eaten. Left vague on purpose.
- **Manning's Friday infos:** `status`, `addict`, `job`, `heroic_act`, `lie` and `food` are declared for `('host','friday_evening')` but cannot be unlocked there (the sole scene is commented out at `host/Day 1/2_Evening/1_main.rpy:238-267`), so that chapter never counts as complete. Left for later.
- **Guns in the hunt:** in 1924, pheasant were shot with shotguns, not rifles. The plot needs a single bullet, so this would be a hunt-wide change across routes.
- **Footman's name:** he goes by "Thomas", the same first name as Thomas Moody (the story doc calls him Andrew).
- **The maid's forms of address:** she switches between "ma'am" and "m'lady". Fine if it is meant to show an untrained actress.
- **Starting the tourer:** the morning uses "tries the starter", the afternoon "swings the handle".
- **Shoes:** she puts her shoes on at waking, and later packs "my own shoes".
- **Duplicated speech:** `broken/Day 2/3_Evening/1_main.rpy:154` repeats the Saturday dinner speech instead of calling `common_day2_evening_dinner_host`.
- **Stale test docs:**
  - `tests/host/3_saturday_afternoon/info.md` still describes the removed walk-back `found_poison` paragraph.
  - `tests/host/5_sunday_morning/info.md` mentions `provisions`, the hamper, and silver "to come back for".
  - `tests/host/6_sunday_afternoon/info.md` still describes `shot_by_butler`, the butler in the doorway, an attic-door branch, and `lie`/`took_valuables` unlocks. The ending is now `burned`.
  - `tests/host/dialogue_coverage.txt` shows the two lines for a garage revisit are never covered.

---

## Verification once fixes are applied

- Re-run `python Murder/check_description_hidden_unlocks.py --diff`. The host-related STALE and MISSING rows from section B should be gone.
- Search for each replaced phrase to confirm no old wording remains, and that the `"""` blocks and blank-line formatting are unchanged.
- Re-run the host test suite in Ren'Py to regenerate the `.txt` transcripts and re-read them. For the edited `_common` labels (A3, A6, A8, A15), also check the other routes' transcripts.
