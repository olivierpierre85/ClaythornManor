<!-- # cSpell:disable -->

### Write Story: NEXT => Broken, then HOST

1. Broken map goals and discoveries
2. Write story
   1. Friday intro
   2. Friday Evening ...

## Technical Tasks


### INTUITION system entirely FOR EVERYONE SAVED concept
Now an intuition is needed to SAVE a person.
When Someone is saved, it add a SAVED over their name in the progress view 
- (need a lot of new images)
- Need a new var saved over time for each character. (is_saved)

- [ ] **Export Choices**: Export_choices_to_file => Find best time to export choices and send to me => Then see if the TEST_MODE with the choices works
- [ ] BUG: **save_transcript_to_file** button not working during menu????
- [ ] **BETTER retry & TESTing management**: I still need a full chapter testing (run EVERY possible choices => Maybe too much?)

- [ ] **MENUS - Check and changes**: 
    - [ ]  when **Map choice has two possible choices**, it picks the first one. Either make sure there is only one by re-reading everything or put in place something to identity 2 choices conflict (basically, if there is two choices, the condition parameter must be set with mutually excluse values)
    - [ ] DOUBLE Check that when a **choice is greyed out**, there is no point in selected them (tutorial_already_chosen). Check specifically
    - [ ] CHeck that every choice now has a time value. The latest changes in menu management allow to deduct time in a choice, then open the next menu, even if there is not enough time. that allow one extra choice without time, but at least it doesn't break continuity. SI I need to check that every menu is ok now.
    - [ ] Also check that every menu has the next_menu parameter well set. It allows to avoid greying a choice that has multiple options available in the future.

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
 




