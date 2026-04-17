<!-- # cSpell:disable -->
BUG => FULL_TESTINGMODE, if doing a restart, then missing menu???

EVery story but the lad, a memory on the train? 
Or just : Captain, Broken?

BUG??? Or by design. WHY Is there a call the generic LAD in psychic day 1 billiard room?


NEW

## Write Story: Captain (Sushil Sinha)

Detailed narrative logic and branches have been moved to: [story_outline.md](file:///c:/Projects/ClaythornManor/docs/game_story/characters_path/captain/story_outline.md)


THREAD, locked shed image

- [x] Friday Afternoon
- [x] Friday Evening
- [x] Saturday Morning
- [x] Saturday Hunt
  - There are two main paths during the hunt,
    - **Version 1** : Thomas moody is dead
      - In that case, Ted harring goes with doctor and drunk
      - Captain is alone with Lady Claythorn. Which means he will observe a third suspicion thread. She is not very good at this ("Even worse than I am"). She will compliment captain's shooting that is not great at all
      - If you already have the two other suspicions, there is a menu asking to confront her (but point out that confronted someone with a gun might not be the best idea). If you do, she will admit that she is not who she says she is, but not entirely (some info for unlock, but not all). Captain ask about the letter, she knows nothing of it. About Thomas Moody,... Captain points gun at Lady to have a more complete confessions. By then the butler who was away comes back, see the situation and, and shot him after a small exchange between the two men. Ending shot in the woods.
      - If you don't have all suspicions then, or you don't confront lady claythorn. The hunt happens the same as usual (death of drunk)
    - **Version 2 **: Thomas moody is alive
      - In that case, Thomas Moody insists on going with Lady and captain. That makes captain uneasy, but he can't really say no.
      - The nervousness makes captain even worse at shooting that usual (which is not great). So thomas Moody teases him. He is himself very good, and is congratulated by Lady Claythorn. After lunch, thomas moody manages to isolate the captain, then point it's gun at him. Captain panics. Thomas moody says something like "It's pretty obvious you never saw battle. Well, that is as close as it gets". Shot in the woods by thomas Moody ending.
    - Note of the two deaths.Maybe being twice is too repetitive, keep the shot in the woods for the most likely, find another for one of the two. 
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
 




