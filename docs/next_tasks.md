<!-- # cSpell:disable -->

### Write Story: NEXT => Broken, then HOST

Change for consistency

=> If thomas is journalist, rethink the letter to the captain as the reason for his scar

----

Prequisite, ADD servant stairs as last room => needs testing



1. Broken map goals and discoveries
   1. Is well suited to uncover the host, but the captain does it? Or should I add something to make the broken be the one unlocking the host OR he could just realise that the HOST is keeping information to herself SO the most common way to learn about her is to.... Interrogate the staff
2. Write story
   1. 
   2. Friday Evening
         1. Add that his discoveries reveals her Name is Killbreath, but it not a major deal !!! 
         2. PATH where as a journalist, you have to ask the best question. If you do, at the end of the interaction you unlock a THREAD => HOst is hiding something. 
            1. NOT bad now, but I should add more questions, with misdirect. Until we reach the final (SHE IS Lying for sure TWO proofs) => Unlocks lady claythorn only NOW? Or conflict with captain ?
         3. Once you have that, you can ask the staff more question. That leads to questionning the following BUT if you go downstairs.
            1. Footman and maid, good if you have found their picture ? but key? Need one downstairs?
            2. Butler => Question him, you die,
         4. You'll discover things about actresses same as the others, make more connections. IF you can extract info from staff, you unlock a path towards all of them killed in the tooshed or the basement.
      1. MAP CHOICES First in tea room, goes to take a drink, leave his flask near the bar then sees the captain telling a story. When he meet ted at the bar, that is becaused he realised he forgot his flask, so he goes back to get it and dies gives to ted. If he doesn't go back to get it, TED dies also, but you only find it back the next day? where!!!
      2.  If not, (do not want to listen to this, USE intuition alreaydy?), he keeps at the bar and try to talk to DRUNK. -> he is the one who can unlock drunk with his clever investigative skills.
   3. Saturday Morning
      1. Ted is ALWAYS dead. Same kind of talk, you follow the doctor into ted harring room, call back but new text. You enter in full Detective story.
   4. Hunt
      1. As option to kill captain, or not if he thinks it is a setup. But to be sure it is a setup, he needs to find more suspicious things? Like DRUNK also receives a message. If he didn't find drunk message, he kills captain. Drunk kills doctor. VEry gore new step
      2. IF he finds message, he knows something is up and goes with drunk and prevents his death. BACK to having multiple choice of partner for hunt since lad is dead.
   5. After hunt
      1. lots of death.
         1. Without captain, host panick and decides to leave even before dinner. So she is not there, only butler, that is weird, everone dies. EXCEPT if you had found AND taken the poison the first day.
      2. Just Ted is dead.
         1. NOrmal dinner, but SAME that with poison, EVERYone DIES
   6. Satuday after dinner.
      1. IF you found poison, you gain some time to explore, in both cases. Now you can?????? PARNER UP WITH THE DRUNK => Unlocks HIm(at least partially)
      2. IF you do not find XXXXXX, you burn in your sleep. There is only one way to see day3 and it is to?
         1. leave ?
            1. Alone
            2. Not alone, wake everyone up before the fire, but then dead anyway?
         2. HIDE in the garden shed?


# Art for broke

Multiple Class in train for outside IMAGEs

Victorian pauper apartement, with a disfigured dead man on his bed. 

## Technical Tasks

IDEA => For choices already made (greyed out, add the time they will consume?)
### INTUITION system entirely FOR EVERYONE SAVED concept
Now an intuition is needed to SAVE a person.
When Someone is saved, it add a SAVED over their name in the progress view 
- (need a lot of new images)
- Need a new var saved over time for each character. (is_saved)

- [ ] **Export Choices**: Export_choices_to_file => Find best time to export choices and send to me => Then see if the TEST_MODE with the choices works
- [ ] BUG: **save_transcript_to_file** button not working during menu????
- [ ] **BETTER retry & TESTing management**: I still need a full chapter testing (run EVERY possible choices => Maybe too much?)

- [x] **MENUS - Check and changes** (done June 2026 — `Murder/check_menu_consistency.py` audits all four rules, run it after any menu edit; conventions documented in CLAUDE.md):
    - [x]  when **Map choice has two possible choices**, it picks the first one. `display_choices` now breaks on first match like the map screen; the checker proves condition exclusivity per room; conflicting conditions fixed (lad no-hunt tea room, lad day2 evening Richard III bedroom)
    - [x] DOUBLE Check that when a **choice is greyed out**, there is no point in selected them (tutorial_already_chosen). Fixed: 2 duplicate menu ids (doctor day2 dinner + bedroom-nurse sleep), broken `linked_choice` refs in captain day3 attic (the ask-china follow-up choice was missing — re-added with the silence label), undefined `next_menu` on doctor day1 billiard
    - [x] CHeck that every choice now has a time value. All map choices now charge a visit cost (incl. sub-menu openers, per the test fixture note in captain day2); conversation navigation openers deliberately stay at 0 (sub-menu questions charge)
    - [x] Also check that every menu has the next_menu parameter well set. Filled everywhere it tracks grey-out; deliberate omissions (unique scene + shared generic menu) are marked `# no-next-menu`

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
 




