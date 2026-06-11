<!-- # cSpell:disable -->

### TEST and validate

FIX EVERYONE CAPTAIN MEETING Day 3 morning for
- ted
  - Add a way to skip search and to just wait?
  - When call captain, make it more dramatic
  - Remove kept searching the manor
- psychic 
  - Remove Captain sinha comes back
- Others?
  - Nurse?
  - Doc?

## FABLE 5

Take advantage to change CODE while it is available

## Write Story: Captain (Sushil Sinha)
- [x] Friday Afternoon
- [x] Friday Evening
- [x] Saturday Morning
- [x] Saturday Hunt
- [x] Saturday evening
- [ ] sunday Morning
  - [ ] Nurse path information
    - [ ] Rewrite entirely : captain_day3_attic_ask_prize
    - [ ] FIX grammar in whole file
- [x] **sunday AFternoon**

NOT important : Weird that the captain doesn't run into the others? Should he hide on purpose? To think about, but LATER

## No config menu for captain? No way to ask random question to host or other? Change that? Or ok like this?

### Threads Captain to redraw: 
- shot on the road, not shot in the woods
- strangle with a lace, not hang in the woods
- Add Beaten to death instead of nose
- Maybe better shot from behind?
- Change place between run over and survive
- Add car on the survive thread
- Add intuition to the right thread

### Write Story: NEXT => Broken or HOST?

## Technical Tasks

### Simplify already visited (not needed from chapter to chapter) => 
Check everywhere? TEST now logic => No hunt for Psychic and Nurse SEEMS Ok, now give values all the time?

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

- [ ] **New Progress view**
    - Add new **ENDINGS page** for symmetry? Or a tooltip that says, endings can be seen below
    - Add new page with **All threads** ?




## Assets & artistic Tasks

### MUSIC with producer AI
Get new music from internet and put them at the right place


### FLUX REBUILD

- [ ] For info_cards, RENAME so it's correct, then change everything to webp?
- [ ] NEW NAME NEEDED ("Blackthorn Manor" / AIMERE (Artificial Intelligence Module for Evidence Reconstruction & Evaluation : AImere House => look again (AI-MERE I am here?))).
- [ ] REDRAW full locations with flux, day and night
- [ ] Redraw character face AND add full body size images

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
 




