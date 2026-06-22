<!-- # cSpell:disable -->
Chages for consistency:
   - Rethink the letter to the captain to comply more with the Journalist story


Servant stairs as last room => needs testing for other characters

SERVANT STAIRS and downstairs IS the same ?? shouldn' we cross it to go downstairs? Add the servant stairs as the image when we try to reach downstairs? servant stairs could be servant room, or the upstairs stairs. But it will be fixed when we change the map


### Write Story: NEXT => Broken

**Prerequisites / decisions before writing:**
- Find a way for Broken to unlock the Host. If he does, the Killbreath discovery can come right at the start.
- Test the changing MALUS and the whole Broken branching logic.

#### 1. Map goals & discoveries
- **Broken is well suited to uncovering the Host**, but at the moment the Captain is the one who does it.
- Decide: either make Broken the character who unlocks the Host, or have him simply realise she is keeping information to herself. In the latter case, the natural way to learn more about her is to interrogate the staff.

#### 2. Write story

##### Friday Evening — Dinner
- Add more questions for the Host, with misdirects, until the player reaches the conclusion that she is certainly lying (two proofs).
  - Open question: does this unlock Lady Claythorn only now? Does it conflict with the Captain's path?
- Once the player has the two proofs, they can press the staff further. This leads to interrogating the people below, but going downstairs is dangerous:


##### Friday Evening — Map (after dinner)

  - **Kitchen** — WRITE Maid text and discovery about butler
- **Billiard room** (improvements)
  - Could add a "go to the bar first" option → then Ted Harring doesn't die. (But keeping him alive is complicated.)
  - Add generic doctor/journalist insight, or drop the doctor talks entirely and fixate on the staff.
  - Add a "question the butler" path (if you've unlocked the strange material about the Host) → **do it and you die no matter what.** Reuse throat cut ending
- Add FIND A LETTER, if consistent with the Captain's story.
##### Saturday Morning (Ted is always dead)
- If Ted is dead → an early death for Moody and everyone else, because they have lost their minds (not the same as Moody). Ted was young, so suspicion runs very high: no hunt, just lunch while waiting for the police — then everyone dies.

##### Saturday — Hunt
- Option to kill the Captain, or not, if Broken thinks it is a setup. To be sure it is a setup he needs more suspicious findings — e.g. the Drunk also received a message.
  - If he hasn't found the Drunk's message → he kills the Captain, and the Drunk kills the Doctor (very gory new step).
  - If he has found the message → he knows something is wrong, goes with the Drunk and prevents his death. Back to choosing a hunt partner (since the Lad is dead).

##### Saturday — After the Hunt
- **Without the Captain** — the Host panics and leaves before dinner. With only the Butler present it feels wrong, and everyone dies at dinner — except if you found and took the poison on the first day. Otherwise the Butler burns everyone? And the psychic dies by suicide (first to collapse, apparently from smoke inhalation but actually sleeping pills).
- **Only Ted is dead** — a normal dinner, but the same outcome: everyone dies. If you found the poison you can press on; if you found nothing you die in your sleep when the Butler sets the house on fire.

##### Saturday — After Dinner
- If you found the poison, you gain time to explore in both cases. Now you can partner up with the Drunk → unlocks him (at least partially). Or with someone else?
- If you do not find [???], you burn in your sleep → INTUITION: DO NOT SLEEP. 
  
- The only way to reach Day 3 is to have found the poison AND successfully interrogated all the staff, which makes Broken decide to spend the night in the tea room ("no one should leave our sight")

##### Sunday Morning 
If you survived with everyone but TED harring and host (who sneaked out after dinner), you are now face with what to do. You know you have to leave but how and with whom?
- The car is gone, can you use the other car? NOt enough room?
THE WHol stuff can be decided at the end of the writing


## Assets & artistic Tasks

FOR BROKEN:
- Image for talk with maid (maid side photo should be enough)
- RAT poison bottle check already exists?

Try flux dev on my laptop?

### IMAGES NEXT REBUILD

- [ ] For info_cards, RENAME so it's correct, then change everything to webp?
- [ ] NEW NAME NEEDED ("Blackthorn Manor" / AIMERE (Artificial Intelligence Module for Evidence Reconstruction & Evaluation : AImere House => look again (AI-MERE I am here?))).

### Characters
- [ ] Redraw character face AND add full body size images

#### Locations
Finish normal list- last one is train_second
Multiple Class in train for outside IMAGEs
- Two class at the moment. I think One image by person is more appropriate, with hints in them (bags,...). See to do it later
  
### MAPS

Redraw BETTER maps


  
### MUSIC with producer AI
Get new music from internet and put them at the right place


## Technical Tasks

IDEA => For choices already made (greyed out, add the time they will consume?)
### INTUITION system entirely FOR EVERYONE SAVED concept
Now an intuition is needed to SAVE a person.
When Someone is saved, it add a SAVED over their name in the progress view 
- (need a lot of new images)
- Need a new var saved over time for each character. (is_saved)

- [ ] **Export Choices**: Export_choices_to_file => Find best time to export choices and send to me => Then see if the TEST_MODE with the choices works
- [ ] BUG: **save_transcript_to_file** button not working during menu????
- [ ] **BETTER retry & TESTing management**: I still need a full chapter testing (run EVERY possible choices => Maybe too much?)

- [ ] **New Progress view**
    - Add new **ENDINGS page** for symmetry? Or a tooltip that says, endings can be seen below
    - Add new page with **All threads** ?



## Question for Testers
- What about **NEW PROGRESS PAGE** and no character page
PATHS, “Actions”, Findings, discoveries ? Forks, Threads, Leads
NEW paths PAGE wil ALL the unlockables, different from breakpoint page
- DO I NEED the map menu ? Since there is almost 0 info on it, maybe not
- Are important choices TOO confusing => Everything or NOT? But that means WAY harder to unlock?


## Update ITCH.IO
- Update itch.io
- Switch branch (Check export_file IN SAVE action has been deleted)
- Define config.version = "0.1"
- Export selection choices

Hide hamburger menu => after each upgrade , change context 
container to this :
```
    #ContextContainer {
      position: absolute;
      left: 0px;
      top: 0px;
      color: white;
      visibility: hidden;
    }
```
 




