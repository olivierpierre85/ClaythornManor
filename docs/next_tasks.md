<!-- # cSpell:disable -->
BUG => FULL_TESTINGMODE, if doing a restart, then missing menu??? Also doesn't restart thread => AVOID RESTART


## Simplify already visited (not needed from chapter to chapter) => Check everywhere? TEST now logic => No hunt for Psychic and Nurse SEEMS Ok, now give values all the time?

## BEFORE NEW STORY :

FIX EVERYONE CAPTAIN MEETING Day 3 morning for
- ted
- psychic 
- Others?

## Write Story: Captain (Sushil Sinha)

IDEA THE Butler is hired thug, in here for the money, not to kill, but not not to kill. OR LOVER of Psychic, they met in service? => Check afternoon deaths

UNLOCKS HOST Rethink with Broken

Maybe twist, add a character the butler. Yes there is a hidden butler, if you find something about him, it unlocks him OR, WHEN ALL THE CHARACTER HAVE BEEN SAVED. Only captain, host, broken and drunk could find info.. With new things to unlock. And only one possible path, one choice at the beginning. I'll d what you want... Character selection => I

THREAD, locked shed image

- [x] Friday Afternoon
- [x] Friday Evening
- [x] Saturday Morning
- [ ] Saturday Hunt - **almost**
  - [ ] TODO: **ADD info unlocks**
    - [ ] LADY not independant, just incompetent? Rewrite text properly => Prepare unlock?
    - [ ] NO unlock for Thomas Moody ? Or find something else?
- [x] Saturday evening
- [ ] sunday Morning
  - [ ] hard to reach DIALOG but unlocks NOTHINg => **Find something to put there**. 
- [x] **sunday AFternoon**

**Captain's gun**
**Add dialog somewhere to say he has a gun.**
QUID gun for the captain ? Has one when he confront the nurse, so he should have one, or a way to get one? It seems assume he has one with him at all time? Or should I rewrite that ?

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
 




