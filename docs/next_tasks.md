# 🚀 Active Work & Next Steps

- [ ] GAME STORY NEW MD - DOUBLE CHECK everything
  - [ ] characters
  - [ ] locations object => Add all objects to all rooms like in game????
  - [ ] meta ai
  - [ ] timeline

## Write Story : Day 3 - Doctor FINIS DOCTOR
- [ ] RETRY EVERYTHING - BUT FIRST ALL nurses path
- [ ] add Music Death.
- [ ] Nurse Path: More info for poisoned ending (Strychnine).
- [ ] Menus: Ensure "Next menu" is correct everywhere.
- [ ] Gun room has a Menu choice Day 3.
- [ ] Rethink unlocking FULLY

## Proofreading
- Fix grammar workflow
  - Workflow and Agent guidelines ok
  - Find a way to to this for more that one run in chapter, but for all the runs in the chapter that cover all the texts
- TODO add internal logic worflow? /logic-test that will read the same file but not correct grammar?
- NOW Must go hand in hand with TESTING by chapter
- Lad : Next  DAY 3
- Psychic: TODO Full
- Doctor: TODO Full

## Technical Tasks

- [ ] **Export Choices**: Export_choices_to_file => Find best time to export choices and send to me => Then see if the TEST_MODE with the choices works
- [ ] BUG: **save_transcript_to_file** button not working during menu????
- [ ] **BETTER retry & TESTing management**: I still need a full chapter testing (run EVERY possible choices => Maybe too much?)
-  [ ] **Testing**: Define paths that test all dialogs for the first 3 character
    - [ ] Doctor
    - [ ] Lad
    - [ ] Psychic
- [ ] **MENUS - Big Challenge**: 
    - [ ] Menus: Ensure "Next menu" is correct everywhere AND That every choice with a following menu DOESNT have a time value
        - [ ] Doctor
        - [ ] Lad
        - [ ] Psychic
    - [ ] ALSO when **Map choice has two possible choices**, it picks the first one. Either make sure there is only one by re-reading everything or put in place something to identity 2 choices conflict
    - [ ] DOUBLE Check that when a **choice is greyed out**, there is no point in selected them (tutorial_already_chosen). Check specifically :
        - Problem in Angry Broken (doctor path) the option next menu should be the menu where you can actually do something with the “angered” broken. Or maybe
        - Ending Gun downed with sushil ted harring: Add a second choice when you escape with the gun. To avoid greying when there is another possible ending. (“Go out, you have a gun it’s safe”)

- [ ] New Progress view
    - Add new **ENDINGS page** for symmetry? Or a tooltip that says, endings can be seen below
    - LOCKED not always centered in character_view ?
    - Should the icons (endings,...) be Slightly bigger (same as characters)?
    - Add new page with **All threads** ?


## Assets & artistic Tasks
- [ ] Try a extension or App to do easy repetitive things
  - [ ] Add a border to an image
  - [ ] Resize to 1920 ,With cropping when needed
- [ ] For infocards, RENAME so it's correct, then change everything to webp?
- [ ] Try to make background using Nano Banane Pro.
- [ ] Try to make new Character side image
- [ ] Try to make characteres FULL size 
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
- Switch branch
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
 




