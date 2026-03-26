<!-- # cSpell:disable -->
BUG => FULL_TESTINGMODE, if doing a restart, then missing menu???

n Can you make sure that the tests checkpoints for nurse cover all the possible unlocked threads when starting a new chapter? I need to be able to reach every dialogs from the list of checkpoints for a 

IDIOT !!!!!!! THERE IS NO NUMBER ONe in the infocard => YOU added the I of intuition, that is reserved for endings. CORRECT EVERYTHING

EVery story but the lad, a memory on the train? 
Or just : Captain, Broken?

## Write nurseStory : Full

CHECK NEW ENDINGs


- Re test all captain possibilities, and unlocks incompatibilities
  - Check that the texts where she is scared of captain don't appear if she has unlocked captain secret (or just delete them.)
  - SHE DOESN't say where she found the gun (I always have one with me, for protection?)
  - WHAT TO DO WITH THE captain's lie other than staff then ? Just a way to reach killed by captain


I've rethink the ebtire thing.
The way I see a total revamping.  4 lines of questionning for nurse to captain

A - 2 Actors in the middle of nowhere => THat is weird I garantee, but there is still could be a an explantion
B - 3 persons were at the same war on zanzibar => Samesies
C - Captain lies about his services => Admits he as embellished some stories, everybody does the same => unlock his stories are not always true BUT not the there are extremely wrong? Just a minor lie in the his bio
D - Manning (Not needed for )

Z - I Have a weapon, and even bullets
We'll need the 3 (A,B,C) to unlock this. Ask captain to Confront Lady Claythorn, OR the butler? => Then I am just a fraud. Now, the nurse insists that if he doesn't help her to confront host or butler, she will tell his story => NOW we have the captain sinha kills her ending, plus we've unlocked the big lie, so probably unlock him as well. 

What do you think ?

- Recheck leave with money or without logic, I might forgotten something there

NEXT add a label at the end of path A, B, and C, the label will give a different text based on how many path have been completed:
0 : I'll need more that to convince him
1 : He looked suspicious enough, but i'll need a small push to decide him
2 : "You are are right, that is too suspicious" .... I wish but I need to have ...



- [ ] RETRY EVERYTHING
  - [ ] Friday afternoon
  - [ ] Friday evening
  - [ ] Saturday Morning
  - [ ] Saturday Hunts
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
 




