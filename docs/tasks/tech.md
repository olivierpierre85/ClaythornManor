# 💻 Tech Backlog

## UI

### Generic

- [ ] Redo The buttons at the bottom of the say dialog (remove backtrack...)
- IN PROGRESS, Make the chapter image 20% bigger so the text on two lines can be bigger (28 instead of 26, 
- ?Replace the —- for the missing description by a redacted marker? 
- [ ] **Map**: Add "You are here" on the map.
- [ ] Create **NEW OPTIONS Page**
- [ ] Add Icon for web distribution
- [ ] **doctor** : Remove intuition from burning image, or make better image
- [ ] REvise NEW **Help Page + Tutorials** 
    Fill with all the information needed
    Add IF for the parts that need a tutorial seen
    Move tutorial from script to tutorial page
    REWRITE Tutorials Based on new screen (characters, progress, …)
- **Tutorial** Explain that restarting from a chapter doesn't mean all branches are accessibles from there

### Menu usability / right click / skip / inputs

- Right click for menu send to OPTIONs not latest screen ? But push button works?  
  - Simple solution Disable right click in prod
- Disable BACK roll
- PREVENT Mouse ROLL TO MOVE STORY!!!
- SHOW ON SCREEN WHEN TEXT IS SKIPPABLE
- Add a skip option TO every MENU (stand alone, …)  
  - But only visible when everything done??? OR All the time  
  - Example first menu add => Don’t talk to anybody, let them come to you?
- When all choices are Completed:  
  - Add a possibility to skip ? (ex: don’t talk to anyone like a true loner)  
  - Or just always add an option to skip to go faster
- provide an option on mobile to skip. Or just Bigger button ?
- Check all keyboard shortcuts are deactivated
- Fix problem with menu navigation with arrows and gamepad
  

### Notifications / visuals

- When Found an object or decision: add the image in the notification
- At unlocking character, show the character image (with fadout ?)
- Better looking notifications

### BEtter transitions ()
- Better Custom transitions (blood dripping for DEATH)
- Background dimmed when the narrator talks
- Add unstoppable transitions
- Add constants for often used value (fadeout, fade_in,Min time for dialog choice(5or10?)) => Make random transition when none provided?

- Better black transition (two step, one the day, second the name of the player?)
- Add NARRATOR TEXT STYLE, for death AND help ?
- (https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=25453&p=313338&hilit=caption.replace#p313338)


## TIME subtraction: 
- Still a problem when starting a path with a menu a time < 0 ? It stop suddenly when a menu should be available? Try again to make the subtraction only at the end, like the time move? NO because then it allows to read a full menu? Like during no hunt? THINK THINK THINK

## Improve Time Menus

- Make triple sure that a choice only has ONE possible condition activated!!  
  - (add not condition for regular choices maybe?)
- Check that no choice that is followed by another choice has a time value  
  - Because it means it could stop the flow of talk.
- Double CHECK that when a choice leads to another menu choice, that the time value for the first choice is 0, so the second choice is always displayed  
  - Otherwise, we might exit the current dialog too soon  
  - (ex : `lad_day3_morning_gun_room`)
- FIX length time of choices to something logical
- ALL Other guest should be keep_alive => Check everywhere
- Find an easy way to show some dialog (like the introduction before the dialogs about other guests) only ONCE
- When the submenu other guest is empty, we shouldn’t have the choice ask about guests in the first menu  
  - ALSO SKIP INTRO if choices other guest selected multiple times
- Striped choices when visited partially => TOO complicated not important
- !!!! What about choice with conditions that can be met in the future?  
  - If a choice is grey it means there is no more choices in the next menu  
  - But it could be next time you play this dialog  
  - Find a way to keep it in Striped too?


## Timing / pauses / time values / flow

- Remove all `pause 1.0`? And replace with `call wait screen`?  
  - Because a pause is often confusing  
  - => Check which one is best


---

## Map / readability / navigation

- Should I make exit question Always Bright?  
  - If YES maybe make it the screen, not by changing “already_chosen” because it’s complicated
- Map menu choice is annoying when you want to think where to go  
  - How to hide the map? Add a collapse Map button and a relapse map to show it back
- add a YOU are here on the map !
- IF possible, still show Hotspot on map when locked to have tooltip
- CHeck that if choice is `valid()` also applies to `map_choices` !!!  
  - NOT the case now I think (test with billiard room)
- Recheck map content ESPEcially basement (exclude gun room)
- Better map
- QUID MAP menu, if specific choice is hidden  
  - Replace with a standard answer ?  
  - YES, always two choices => standard, I already been there choice?(SAME LIBRARY)


## Autosaves / saves / continue / new game safety

- AUTOSAVE ON QUIT NOT WORKING ANYMORE (or maybe just when fast forwarding? Try without the save on choices to be sure)
- Autosave NEVER working (see in incognito mode)
- Replaced by quicksave, BUT must be a manual save
- Dangerous, not enough saves  
  - => it would be better to add a quicksave after each menu, or chapter???  
  - But only works on action
- Improve like below:

```renpy
if renpy.variant("pc"):

    ## The quit button is banned on iOS and unnecessary on Android and Web.
    textbutton _("Quit") action Quit(confirm=not main_menu)
```

- Fix the Continue - load last save (autosave?)
- WHY ALWAYS SAVE THE FIRST ITEM IN THE menu
- Add if on the continue button, to make different call when auto, quick, normal
- Add button with shortcut to those menu (replace load and save) in quick menu
- BETTER SAVE MANAGEMENT ??? or just keep the standard with auto save activated
- !!! Important !!! Add confirm window before starting a new game if a game is currently started?
- persistent._clear() WHEN NEW GAME (with warnings)
- WHEN NEW GAME => WARNING AND DELETE PERSISTENT
- NO LOAD GAME, NEW GAME is normal start, continue is debug_choice OR LOAD IS DEBUG???

---


## Intuitions / endings / tutorial messaging

- Rethink Intuitions as Endings with intuitions  
  - => Some endings are so terrible, that it will mark you soul in every plane of existence
- should certain death just be considered intuition?OR BACK TO FIRST IDEA => Intuitions must be earned !!!!
  - NEED for a game that allows you to unlock intuitions? 
- IDEA FOR ENDING: ASK THE player who the most likely culprit is  
  - Then it generates extra dialog with guilty part  
  - But for most people it ends with “PROBABILTY ERROR” message and stops when it becomes an impossibilty

---

## Web build / itch.io
- Use butler to upload files: it only uploads whats changed, generates patches for the itch.io app, and you can automate it.
- Fix the web style for smartphone !!! (error in menu, bigger text?)
- Try to download all images BEFORE in progressive Loading
- FOR WEB => MAP other color when NOT ALREADY CLICKED???  
  - A third color ? Or replace insensitive with n??? Or a second choice when in map?
  **MOBILE version**
    Important that the web version is mobile friendly, or I would lose so many players.
    MAKE IT Mobile First ! So the screen can be read in both format without changes?

## (Minor) (hard) Unlock intuition
An INTUITION in a timeline can CHANGE multiple timelines
Build a screen to unlock intuitions !!!! Yes, some will have a positive effect some not really => Similar bad end theater
Or put it in the CHARACTER screen, add an intuition button on off


## (Minor) (hard) Position of people on map
For each chapters (part of chapter when complicated) there is only one possible position for each character. When you find out where they are, it should be written on the map. Otherwise, the map unlock is not very useful. Test if possible
Very complicated => Maybe for version 2

## (Minor) DEAD PEOPLE IN MENU
For each chapter, at every moment, Show the people who are dead and the one alived in the progress view (add a cross if character dead), a question mark if you don't know where they are.
BETTER, show there are dead with their faces changes (if chatgpt allows it), or just cross their faces

## Generic Changes - TO sort

- BUG: Threads can be shown in actual and previous discoveries  => REBUILD DETAIL SCREEN???
  - What logic should I keep? Only current? OR new logic with excluding choices ???  
  - => Not super important now, can keep both
- ? If current player text not enough? Add picture of current player : BUT WHERE ? nothing looks good
- Have access to timeline before dying?
- Reorder variable initialization. They are all over the place
- Endings code must look the same (diff between psycho and lad)
- Show credit when Reach SURVIVE ending (So create credits with only my name :-) MUCH LATER
- Put smaller mouse icons for web (and everywhere actually?)
- REDO all tutorials BUT mostly progress view when validated
- Be sure NVL is deactivated (OR make it work?)
- Add Shortcut to character menu when choice between talking to multiple characters  
  - This way, we can decide to whom to talk to by clicking on the one with less information. Not major
- Replace all day1, day2 with the real day?
- Easter Egg options => use old visual (same_name but add old in the change location function!!!) SEE META
- Test -angry is still necessary, it doens’t feel like it is
- Replace all day1, day2 with the real day?
