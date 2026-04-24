<!-- # cSpell:disable -->
BUG => FULL_TESTINGMODE, if doing a restart, then missing menu???

EVery story but the lad, a memory on the train? 
Or just : Captain, Broken?

BUG??? Or by design. WHY Is there a call the generic LAD in psychic day 1 billiard room?


BUG CHECK all commons for inner dialogs with person filter => Exemple Day2 Evening..

Search in common for  """"

NEW

TRY CONSOLE

## Write Story: Captain (Sushil Sinha)

Detailed narrative logic and branches have been moved to: [story_outline.md](file:///c:/Projects/ClaythornManor/docs/game_story/characters_path/captain/story_outline.md)


INTUITION WHERE to place it? 



THREAD, locked shed image

- [x] Friday Afternoon
- [x] Friday Evening
- [x] Saturday Morning
- [ ] Saturday Hunt - **almost**
  - [ ] TODO: ADD info unlocks
    - [ ] LADY not independant, just incompetent? Rewrite text properly => Prepare unlock?
    - [ ] NO unlock for Thomas Moody ? Or find something else? => add the single thing? NO, no need. REWRITE STORY of thomas moody and the link with his brother? The real thomas is an orphan. Archie grew up with staff, so he pretends to be staff. BUT WHY??? I don't think Archie is Thomas Brother,  just his FRIEND for war? Lover? He knows everything about THomas moody. Needs rewrite the doctor. So you don't have the unlock BROTHER from doctor escape, just happy to escape. You'll need to ///. ALSO to unlock Thomas moody, add the captain notice he is the only one fitting perfectly. He is clearly posh. Yet, he told me he was a simple soldier, a former footman. That makes no sense. => Maybe it's the only way to survive for him. Befriend the Broken.?
- [ ] Saturday evening - **ongoing**
  - [ ] **Major confrontation** -You need to have all suspicion (so you held your tongue in moody's death path) so now you can accuse the host in front of everybody. First, send the butler to accompany Sam Manning => then isolated everyone the a room, the tea room, close the door. Big reveal discussion about link between everyone => Is everyone really an impostor, or something else? In the end, everyone burned down? No the butler might kill one person, but not everyone? => If good choice => unlock intuition that will unlock Thomas moody.
  - [ ] BUG -> Now sushil sinha comes back The captain is sushil sinha, its incorrect
  - [ ] IF confront => no key to explore everywhere (no shed, no oil, no car
  - [ ] If confront
  - Add and validate tests
  

NEXT CHARACTER - UNlocked by Nurse (and psychic)

## Proofreading
- TODO add internal logic workflow? /logic-test that will read the same file but not correct grammar?
- NOW Must go hand in hand with TESTING by chapter
- Lad : Next  DAY 3
- Psychic: TODO Full
- Doctor: TODO Full

## Technical Tasks

### INTUITION system entirely FOR EVERYONE SAVED concept
Now an intuition is needed to SAVE a person.
When Someone is saved, it add a SAVED over their name in the progress view 
- (need a lot of new images)
- Need a new var saved over time for each character. (is_saved)
- 
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

### MUSIC with producer AI
Get new music from internet and put them at the right place

## New place

India
A room in a nice india house calcuta, 1880.

New music, captain's theme? Old india ? or no music?

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
- 
## add captain feared expression, showed only for his confession

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
 




