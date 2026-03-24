<!-- # cSpell:disable -->
BUG => FULL_TESTINGMODE, if doing a restart, then missing menu???

n Can you make sure that the tests checkpoints for nurse cover all the possible unlocked threads when starting a new chapter? I need to be able to reach every dialogs from the list of checkpoints for a 

IDIOT !!!!!!! THERE IS NO NUMBER ONe in the infocard => YOU added the I of intuition, that is reserved for endings. CORRECT EVERYTHING


## Write Story : Full

CHECK NEW ENDINGs

ENDING WITH MONEY => NEED Pearls, all the shit and ONE cutlery at least? Or just big silverware?

ENDING ESCAPING at night, caught for thievery =>** If you escape at night, you might spot the staff leaving in the car**
You notice it => Rethink the endings (escape during the night => Not possible to die of exhaution ?) INTUITON UNLOCKED?????

ALSO, add if pearl => add that the butler show that as well, and the host noticing ! That's were they were? I was planning on wearing them tonight!

=> Then to die of exhaution, you need 2/3 exhaution unlock => add one during the hunt ?



- [ ] RETRY EVERYTHING
  - [ ] Friday afternoon
  - [ ] Friday evening
  - [ ] Saturday Morning
  - [ ] Saturday Hunt
  - [ ] --
  - [ ] Sat evening
  - [ ] Sun mornning
  - [ ] Sun ENDING
- [ ] Nurse Path: More info for poisoned ending (Strychnine).
- [ ] Gun room has a Menu choice Day 3.
- [ ] Rethink unlocking FULLY


## Proofreading
- TODO add internal logic workflow? /logic-test that will read the same file but not correct grammar?
- NOW Must go hand in hand with TESTING by chapter
- Lad : Next  DAY 3
- Psychic: TODO Full
- Doctor: TODO Full

## Technical Tasks
-  [ ] **Testing**: Define paths that test all dialogs for the first 3 character
    - [ ] Doctor
    - [ ] Lad
    - [ ] Psychic
- [ ] WEB run for testing, so antigravity can take printscreen? 
  - [ ] OR just a command to take printscreen when testing (at location change for isntance) and check if ok.
  - [ ] Or add a condition to fail test is the image is missing (but how?)
- [ ] **Export Choices**: Export_choices_to_file => Find best time to export choices and send to me => Then see if the TEST_MODE with the choices works
- [ ] BUG: **save_transcript_to_file** button not working during menu????
- [ ] **BETTER retry & TESTing management**: I still need a full chapter testing (run EVERY possible choices => Maybe too much?)

- [ ] **MENUS - Big Challenge**: 
    - [x] Menus: Ensure "Next menu" is correct everywhere AND That every choice with a following menu doesn't have a time value
        - [x] Doctor
        - [x] Lad
        - [x] Psychic
    - [ ]  when **Map choice has two possible choices**, it picks the first one. Either make sure there is only one by re-reading everything or put in place something to identity 2 choices conflict
    - [ ] DOUBLE Check that when a **choice is greyed out**, there is no point in selected them (tutorial_already_chosen). Check specifically :
        - [x] Problem in Angry Broken (doctor path) the option next menu should be the menu where you can actually do something with the “angered” broken. Or maybe removed (fixed by removing the next_menu param so choices don't lock)
        - Ending Gun downed with sushil ted harring: Add a second choice when you escape with the gun. To avoid greying when there is another possible ending. (“Go out, you have a gun it’s safe”)

- [ ] New Progress view
    - Add new **ENDINGS page** for symmetry? Or a tooltip that says, endings can be seen below
    - Add new page with **All threads** ?


## Assets & artistic Tasks

### STABLE DIFFUSION FUN

Flow or SDXL ?
=> Flow slower but I think much better.
ADAPTA FLOW TO GENERATE IMAGES, but with a more cartoonish style


- [ ] For info_cards, RENAME so it's correct, then change everything to webp?
- [ ] NEW NAME NEEDED ("Blackthorn Manor" / AIMERE (Artificial Intelligence Module for Evidence Reconstruction & Evaluation : AImere House => look again (AI-MERE I am here?))).
- [ ] Try Locations with characters inside (Whisk/experimental).

## Question for Testers
- What about **NEW PROGRESS PAGE** and no character page
PATHS, “Actions”, Findings, discoveries ? Forks, Threads, Leads
NEW paths PAGE wil ALL the unlockables, different from breakpoint page
- DO I NEED the map menu ? Since there is almost 0 info on it, maybe not
- Are important choices TOO confusing => Everything or NOT? But that means WAY harder to unlock?

### Update ITCH.IO
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
 




