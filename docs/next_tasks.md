<!-- # cSpell:disable -->
BUG => FULL_TESTINGMODE, if doing a restart, missing menu???

## Write Story : NURSE - Day 2

- [ ] Part 1 - Hunt
    - [ ] TEST TEST TESTS create manuel PATH WITH EVERYTHING;
    - [ ] CHECK Music and sound => New music when caught by psychic
    - [ ] EXTEND OTHER GUESTS for Psychic? Too similar that first day ? Maybe Later

  - [ ]** Part 2 EVENING**
  - - NEXT => MAP ROOM
    - [ ] - IDEAS - For evening
    - [ ] THIEF ENDING => Host notices nurse pocketing a some cutlery. If you've already stolen stuff => You are lock into you room? 
    - Ask the maid why she is an actress? need the unlock from her room?
    - Or tell the captain that the people are not what to expect
      - need the footman and the maid unlock?
      - **Storage room**, if all three choices not exhausted, don't hide entirely? too complicated, make only one option to search or not?? Think about => Could be that you need a clue to find bullets, in multiple menus impossible to find without the clue. You'll get the clue only after a certain death?
      -  Add clue about Lady Claythorn in her room? We've got nothing now, it's a good place to do that. YES for captain (add to footman and maid unlocks)
    - [ ] Cough warning (call to every choice in map choice ), if time < x """ I m exhausting my self"
    - [ ] MAKe on death (or escape) possible when NO exhaustion at all
    - [ ] HOw to get butler's key ? Also, this way you learn something about the butler, making the whole staff suspicious => ? New key choice for captain, team up with captain?
  - [ ] DRAFT ONLY made by AI -> Re read EVERYTHING
  - [ ] Discussion with captain SINHA => NEED the 2 unlock from before AND ask him in details about boxer's rebellion. If you can spot the lie => UNMASK him. => Then, make friend or die?
  
  ### Endings
- Exhaustion => Possible from the hunt? Evening? (if exhausted the day before?)
  
## Write Story : NURSE - Day 3

???
  
## Write Story : Day 3 - Doctor FINIS DOCTOR
- [ ] RETRY EVERYTHING
- [ ] Nurse Path: More info for poisoned ending (Strychnine).
- [ ] Menus: Ensure "Next menu" is correct everywhere.
- [ ] Gun room has a Menu choice Day 3.
- [ ] Rethink unlocking FULLY


## Proofreading
- TODO add internal logic workflow? /logic-test that will read the same file but not correct grammar?
- NOW Must go hand in hand with TESTING by chapter
- Lad : Next  DAY 3
- Psychic: TODO Full
- Doctor: TODO Full

## Technical Tasks
- Make TEST_mode useful. Get
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
 




