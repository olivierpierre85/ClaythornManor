# 🚀 Active Work & Next Steps

- [🚀 Active Work \& Next Steps](#-active-work--next-steps)
  - [IMPORTANT](#important)
  - [Write Story : Day 3 - Doctor](#write-story--day-3---doctor)
  - [Proofreading](#proofreading)
  - [Technical Tasks](#technical-tasks)
  - [Assets \& artistic Tasks](#assets--artistic-tasks)
  - [Question for Testers](#question-for-testers)
  - [🚀 Project Completion Timeline (Optimistic First Draft)](#-project-completion-timeline-optimistic-first-draft)
    - [Update ITCH.IO](#update-itchio)

## IMPORTANT
- [ ] REVIEW THIS DOC COMPARE TO GOOGLE DOC.
  - [x] Next page 
  - [x] NEXT : TECH - HUGE FILE TO read for SMALL ideas
  - [x] SORT ASSETS GENERIC IDEA
  - [ ] CHECK every task is at the right place (tech backlog)
  - [ ] GAME STORY NEW MD - DOUBLE CHECK everything
    - [ ] characters
    - [ ] locations object => Add all objects to all rooms like in game????
    - [ ] meta ai
    - [ ] timeline

## Write Story : Day 3 - Doctor
- [ ] RETRY EVERYTHING - BUT FIRST ALL nurses path
- [ ] add Music Death.
- [ ] Nurse Path: More info for poisoned ending (Strychnine).
- [ ] Menus: Ensure "Next menu" is correct everywhere.
- [ ] Gun room has a Menu choice Day 3.
- [ ] Rethink unlocking FULLY

## Proofreading
- Build new protocol to work with antigravity
- Lad : Next  DAY 3
- Psychic: TODO Full
- Doctor: TODO Full

## Technical Tasks
- **SNIPETS** doubld check and extend the new snippet file! 
  - New menu with more current options (change room, sound, music, and their values)
- [ ] **Export Choices**: Export_choices_to_file => Find best time to export choices and send to me => Then see if the TEST_MODE with the choices works
- [ ] BUG: **save_transcript_to_file** button not working during menu????
- [ ] **BETTER retry & TESTing management**: I still need a full chapter testing (run EVERY possible choices => Maybe too much?)
-  [ ] **Testing**: Define paths that test all dialogs for the first 3 character
    - [ ] Doctor
    - [ ] Lad
    - [ ] Psychic
- [ ] **Refactor**: Clean "todo.md" into proper docs (Done!).
- [ ] Rename gun room to armory
- [ ] Replace ALL icons, with the thread icon? Not loops, or .... (just do)
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
- [ ] Try to make background using Nano Banane Pro.
- [ ] NEW NAME NEEDED ("Blackthorn Manor" / AIMERE (Artificial Intelligence Module for Evidence Reconstruction & Evaluation : AImere House => look again (AI-MERE I am here?))).
- [ ] Try Locations with characters inside (Whisk/experimental).

## Question for Testers
- What about **NEW PROGRESS PAGE** and no character page
PATHS, “Actions”, Findings, discoveries ? Forks, Threads, Leads
NEW paths PAGE wil ALL the unlockables, different from breakpoint page
- DO I NEED the map menu ? Since there is almost 0 info on it, maybe not
- Are important choices TOO confusing => Everything or NOT? But that means WAY harder to unlock?

## 🚀 Project Completion Timeline (Optimistic First Draft)
- **Lad**: OK
- **Psychic**: OK
- **Doctor**: 01/2025
- **Nurse**: 04/2026
- **Captain**: 06/2026
- **Drunk**: 08/2026
- **Broken**: 10/2026
- **Host**: 12/2026

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
 




