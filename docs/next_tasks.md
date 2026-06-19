<!-- # cSpell:disable -->
Chages for consistency:
   - Rethink the letter to the captain to comply more with the Journalist story


Servant stairs as last room => needs testing for other characters

SERVANT STAIRS and downstairs IS the same ?? shouldn' we cross it to go downstairs? Add the servant stairs as the image when we try to reach downstairs? servant stairs could be servant room, or the upstairs stairs. But it will be fixed when we change the map


### Write Story: NEXT => Broken

FIND a way to make Broken unlock HOST !! 
   - If so, you can make the Killbreath discovery at the beginning
  
TEST the changing MALUS and the whole broken logic


1. Broken map goals and discoveries
   1. Is well suited to uncover the host, but the captain does it? Or should I add something to make the broken be the one unlocking the host OR he could just realise that the HOST is keeping information to herself SO the most common way to learn about her is to.... Interrogate the staff
2. Write story
   1. 
   2. Friday Evening 
      1. Dinner -> Add more questions for host but**I should add more questions**, with misdirect. Until we reach the final (SHE IS Lying for sure TWO proofs) => Unlocks lady claythorn only NOW? Or conflict with captain ?
         1. Once you have that, you can ask the staff more question. That leads to questionning the following BUT if you go downstairs.
            1. KITCHEN : Either hide and just moves around, directly talk to the maid and "FOOTMAN helping"?
               1. => Disturb the staff unlocks => Will kill you during the night
               2. Hide and look around in the scullery => Find rat poison a bit too visible, and open. TAke it to unlock you found poison? Prevent more deaths by poisoning (lunch saturday)
            2. Footman and maid, good if you have found their picture ? but key? Need one downstairs? WHERE to go to get keys? Or won't be able to enter their room
               1. Needs to talk to 
            3. Butler => Question him, you die,
      2. MAP - after dinner
         1. add FIND A LETTER if consistant with captain story !!!!!!!!!
         2. You'll discover things about actresses same as the others, make more connections. IF you can extract info from staff, you unlock a path towards all of them killed in the tooshed or the basement.
         3. Billiard room improvement
            1.  But I could add a go to the bar first=> Then **ted harring doesn't DIE**! but it is complicated that he doesn't die
            2. Add generic doctor journalist insight OR remove the doctor talks entirely, and fixates on the staff?
            3. **ADD a question the butler path** (if unlocked weird stuff about host?) => Do that and die regardless of what you do
3. 
   1. Saturday Morning (TED is always DED)
      1. IF Ted is dead => EARLY death for moody's and everybody else, because lost their mind. Not same as moody. Ted was young so HYPER suspicious NO hunt, just lunch while waiting for the police,then everybody dies
   2. Hunt
      1. As option to kill captain, or not if he thinks it is a setup. But to be sure it is a setup, he needs to find more suspicious things? Like DRUNK also receives a message. If he didn't find drunk message, he kills captain. Drunk kills doctor. VEry gore new step
      2. IF he finds message, he knows something is up and goes with drunk and prevents his death. BACK to having multiple choice of partner for hunt since lad is dead.
   3. After hunt
      1. Lots of death.
         1. Without captain, host panick and decides to leave even before dinner. So she is not there, only butler, that is weird, everone dies during dinner. EXCEPT if you had found AND taken the poison the first day. IF not the butler burns everyone? but the psychic? Suicide (first to collapse of SMOKE inhalation (but actually sleeping pill))
      2. Just Ted is dead.
         1. NOrmal dinner, but SAME that with poison, EVERYone DIES. IF found poison you can go ahead. If you found nothing you die in your sleep, as the butler has set the house on fire
   4. Satuday after dinner.
      1. IF you found poison, you gain some time to explore, in both cases. Now you can?????? PARNER UP WITH THE DRUNK => Unlocks HIm(at least partially) OR WITH someone else?
      2. IF you do not find XXXXXX, you burn in your sleep => INTUITON DO NOT SLEEP!!. There is only one way to see day3 and it is to HAVE found poison AND INTERROGATE sucessfully ALL of the STAFF MAKES him decide to **spend the night in the tea room** NOONE should leave our sight. 
         1. leave ?
            1. Alone
            2. Not alone, wake everyone up before the fire, but then dead anyway?
         2. HIDE in the garden shed?

## Assets & artistic Tasks

Try flux dev on my laptop?

### IMAGES NEXT REBUILD

- [ ] For info_cards, RENAME so it's correct, then change everything to webp?
- [ ] NEW NAME NEEDED ("Blackthorn Manor" / AIMERE (Artificial Intelligence Module for Evidence Reconstruction & Evaluation : AImere House => look again (AI-MERE I am here?))).

### Characters
- [ ] Redraw character face AND add full body size images

#### Locations
Finish normal list- last one is train_second
Multiple Class in train for outside IMAGEs
- Two class at the moment. I think One image by person is more appropriate, with hints in them (bags,...). See to do it later
  
### MAPS

Redraw BETTER maps


  
### MUSIC with producer AI
Get new music from internet and put them at the right place


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

- [ ] **New Progress view**
    - Add new **ENDINGS page** for symmetry? Or a tooltip that says, endings can be seen below
    - Add new page with **All threads** ?



## Question for Testers
- What about **NEW PROGRESS PAGE** and no character page
PATHS, “Actions”, Findings, discoveries ? Forks, Threads, Leads
NEW paths PAGE wil ALL the unlockables, different from breakpoint page
- DO I NEED the map menu ? Since there is almost 0 info on it, maybe not
- Are important choices TOO confusing => Everything or NOT? But that means WAY harder to unlock?


## Update ITCH.IO
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
 




