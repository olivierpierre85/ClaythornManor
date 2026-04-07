<!-- # cSpell:disable -->
BUG => FULL_TESTINGMODE, if doing a restart, then missing menu???

EVery story but the lad, a memory on the train? 
Or just : Captain, Broken?

## Write nurseStory : Full


Test Nurse manually to get a feel
- now in day2 morning, error if master key and not visited butler room, add dialogs


## Write story captain


### Generic 
- Fun thing, must find lady claythorn is an impostor, leading to her death by an angry mob (or burned at night?) => unlock Lady Claythorn is an impostor, and final character
  - BOOK about genealogy
    - "Lady Claythorn is not a normal Name, Claythorn is the place, she should have a proper surname" Like Lady Grantham of Claythorn Manor.
  - FIND more dinner manner inconsitencies

First option - dinner on saturday evening. 
- Make a scene
- Say nothing
- Try to make her tell the story herself? Trip during conversation? Takes thomas moody seat ? BECAUSE you know that it's how a table must be made. Talk with the butler
How/when to confront? Saturday evening, but she is not in her room? until I go there before a certain time, she is caught leaving?

GIVE him options that others don't have, like **going outside in the rain** : At least it's a place I am allowed to be. BUT he will need a torch t go there. Where to find a torch? in the attic, add a note on the nurse attic visit.
HE HAS all the options in map menu, but will do nothing in most due to proper manners. UNLOCKS an "outside" map. For the search on sunday morning.
THE OUTside shed will show THE **OIL** for the car, that allows him to escape with everyone, but then he will die on the road?
But the Broken will find the bodies of the staff there if he survives.

but to unlock Lady Clay we will need info also from DRUNK (if drunk is unlocked by broken.)

- When he takes charge, he feels like he has too.
  
### Friday
- Friday dinner, Evening dinner: his analytical eye picks up on everyone's social standing

EVENING - Test Ai generate scaffold
=> A lot of duplicates with Psychic, 
=> Map doe he have a choice to wander at this point? NO maybe JUST give a limited choices since he is a stikler? Billiard room and BED?

### Saturday
- Can test the host on the hunt (not dinner)
- ON the hunt he observes and talks to lady claythorn, but he is also trying to appear good at shooting.
(I thouhght I would have a trouble following them, but they are even worst than I am. It was to be expected from Ted Harring, but Lady Claythorn should be better at this, especially since she was the one initiated this)

- On saturday evening, he is suspicious, but don't reveal it to other people BECAUSe he is not trusting them. He as the choice in getting to the billiard room and his bed
- ONe person appears when he is reading? Could it be Lady Claythorn => YES if you make the right choices at dinner and before (Make her understand you are on her side, but you see through her lies)
- Otherwise, who? Lad, psychic, nurse? all of them and rebuff all of them?
- BUT if he managed to find suspicion on Lady Claythorn, he will allow himself to dig deeper?

### Sunday

- Last day, he never stays, always chose to run (not happy if lad also want's to run)

**MAPS**
- After saturdat evening, he has the masterkey to go everywhere, ( But how is it different thant the nurse?)
  - He will find different things because he is more meticulous?
- First day, he is talking, so he won't wander the house, also it's not done.

**endings**
- The hero, to survive AND redempt yourself. You will have the choice to save people. But you first need an intuition. An intuition that escaping alone will kill you? 
- 




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
 




