# 💻 Tech Backlog

## UI

- [ ] Redo The buttons at the bottom of the say dialog (remove backtrack...)
- IN PROGRESS, Make the chapter image 20% bigger so the text on two lines can be bigger (28 instead of 26, 
- ?Replace the —- for the missing description by a redacted marker? 
- [ ] **Map**: Add "You are here" on the map.
- [ ] **MOBILE version**
    Important that the web version is mobile friendly, or I would lose so many players.
    MAKE IT Mobile First ! So the screen can be read in both format without changes?
- [ ] Create **NEW OPTIONS Page**
- [ ] Add Icon for web distribution
- [ ] **doctor** : Remove intuition from burning image, or make better image
- [ ] REvise NEW **Help Page + Tutorials** 
    Fill with all the information needed
    Add IF for the parts that need a tutorial seen
    Move tutorial from script to tutorial page
    REWRITE Tutorials Based on new screen (characters, progress, …)
- **Tutorial** Explain that restarting from a chapter doesn't mean all branches are accessibles from there
  

## Big Ideas (High impact)


### (Minor) (hard) Unlock intuition
An INTUITION in a timeline can CHANGE multiple timelines
Build a screen to unlock intuitions !!!! Yes, some will have a positive effect some not really => Similar bad end theater
Or put it in the CHARACTER screen, add an intuition button on off


### (Minor) (hard) Position of people on map
For each chapters (part of chapter when complicated) there is only one possible position for each character. When you find out where they are, it should be written on the map. Otherwise, the map unlock is not very useful. Test if possible
Very complicated => Maybe for version 2

### (Minor) DEAD PEOPLE IN MENU
For each chapter, at every moment, Show the people who are dead and the one alived in the progress view (add a cross if character dead), a question mark if you don't know where they are

### TIME subtraction: 
- Still a problem when starting a path with a menu a time < 0 ? It stop suddenly when a menu should be available? Try again to make the subtraction only at the end, like the time move? NO because then it allows to read a full menu? Like during no hunt? THINK THINK THINK

## Small Ideas 
## TODO SORT ALL THIS SHIT !!!!!!

## Improve Menu Logs and STYLE

- Generic Menu, spoken by `current_char`
- ALL OTHER menu: Map Choice, or Menu Choice
- Check consistency everywhere, every Menu….

---

## Unlock / threads / IDs

- Only one function `is_unlocked`, that doesn’t take the type into account?  
  - Because too complicated as is (take example to `cond_ ending`)
- Check INTUITION is different enough  
- Add int Id to `TimeMenuChoice` for easier used of all_choices…Hidden…
- Add ID numerical to `TimedMenuChoice` (1, 2, 3,) so it’s easy to check if one is hidden like in:  
  - `all_menus[current_menu.id].choices[25].hidden`

---

## Timing / pauses / time values / flow

- Remove all `pause 1.0`? And replace with `call wait screen`?  
  - Because a pause is often confusing  
  - => Check which one is best
- Make sure a choice with subchoices SPENDs no time, to avoid being stopped before asking something
- Make triple sure that a choice only has ONE possible condition activated!!  
  - (add not condition for regular choices maybe?)
- Check that no choice that is followed by another choice has a time value  
  - Because it means it could stop the flow of talk.
- MAKE sure not ending menu have a 0 value in choice EVERYWHERE
- Double CHECK that when a choice leads to another menu choice, that the time value for the first choice is 0, so the second choice is always displayed  
  - Otherwise, we might exit the current dialog too soon  
  - (ex : `lad_day3_morning_gun_room`)
- BUGGGGG go to bed too early when imbricated choices (can’t run another menu, that may lead to misconception of remaining time)  
  - => See Lad Day 2 talk with captain  
  - => When call a menu, if it’s the first call, we should be able to make at leat ONE choice???
- JUST put 0 for choices that are followed by a new menu!!!!!!  
  - => Test everywhere (map menus, sub menus,....)
- FIX length time of choices to something logical

---

## Map / readability / navigation

- Bigger map text
- The subtext in map choices is not visible enough, even in Golden  
  - Find a way to make it pop
- Should I make exit question Always Bright?  
  - If YES maybe make it the screen, not by changing “already_chosen” because it’s complicated
- Map menu choice is annoying when you want to think where to go  
  - How to hide the map? Add a collapse Map button and a relapse map to show it back
- add a YOU are here on the map !
- IF possible, still show Hotspot on map when locked to have tooltip
- CHeck that if choice is `valid()` also applies to `map_choices` !!!  
  - NOT the case now I think (test with billiard room)
- Replace the background linked questions  
  - NOT GREAT TO HAVE a NUMBER IN IT => TOO Many possibilities of error  
  - => Make a function that will take the redirect (`all_menus[current_menu.id].choices`)
- Return different position in Main menu than in game menu
- FIX hide maps when tutorial not yet seen!!!!!!
- Recheck map content ESPEcially basement (exclude gun room)
- Better map
- QUID MAP menu, if specific choice is hidden  
  - Replace with a standard answer ?  
  - YES, always two choices => standard, I already been there choice?(SAME LIBRARY)

---

## Other guests submenu / “think of other guests” logic

- ALL Other guest should be keep_alive => Check everywhere
- HIDE Talk about other guest when there are no other guest dialog possible
- BUG : think of other guests should be hidden when every option have been used AND the introductory text should display only once a day
- Find an easy way to show some dialog (like the introduction before the dialogs about other guests) only ONCE
- When the submenu other guest is empty, we shouldn’t have the choice ask about guests in the first menu  
  - ALSO SKIP INTRO if choices other guest selected multiple times
- BUG: choices can be shown in actual and previous discoveries  
  - What logic should I keep? Only current? OR new logic with excluding choices ???  
  - => Not super important now, can keep both

---

## Logs / narrator voice / character voice

- In logs, if the answer of a choice is not said by character (but internal, GOdlike dialog), don’t make it say by the character in the log  
  - But that will require an entire rewrite of the menu choice with a new parameter (`character_talked`)

---

## Menu usability / right click / skip / inputs

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

---

## “next_menu” / menu wiring

- ADD next_menu TO EVERY submenu where it is relevant
- Also make next menu important ? Like for the billiard room?

---

## Progress / character screens / “who is dead” display

- The unlocked bar should be in the first character screen, not on the details screen
- Icon fast forward and SKIP should be inverted???
- Add picture of current player : BUT WHERE ? nothing looks good
- Show the current character somewhere? It’s not clear enough
- Add link to progress in Character menu view
- Also launch the tutorial for progress detail when click the Discoveries counter
- Show who is dead in the current time somewhere  
  - In the progress view? Somewhere else?  
  - Cross the face of the characters in the characters menu?  
  - BETTER, show there are dead with their faces changes (if chatgpt allows it)
- Store in a var which characters are dead in the story  
  - THen, show it in the character window!!!
- In progress view, two lines chapters are not centered (I thought that was fixed at some point??? See quit screen)
- In progress details, ORDER C&D by putting ACTivated first, ??? Maybe Later
- Better progress for Final version: Visuals like a boardgame, with more images  
  - Like first night there is a storm, second nigh hunt, third night empty ?
- Put the content of the burned letter in the Progress window
- Start character with the progress view when first ending reached
- Have access to timeline before dying?
- Better Tutorial for progress view???
- Better progress tutorial that includes checkpoint views
- Finish Progress screen AND CHARACTER

---

## Notifications / visuals

- When Found an object or decision: add the image in the notification
- Better looking notifications
- Better Custom transitions (blood dripping for DEATH)
- Background dimmed when the narrator talks (see
- Add unstoppable transitions
- Add constants for often used value (fadeout, fade_in,Min time for dialog choice(5or10?))
- For fun: How to add Blur everything when drunk or poisoned
- Drunk filter (https://midge-the-tree.itch.io/back-when/devlog/274520/renpy-how-to-parallax-camera-and-drunken-blur)
- EFFECT WHEN SEARCHING Captain room (blur)
- Better black transition (two step, one the day, second the name of the player?)
- Add NARRATOR TEXT STYLE, for death AND help ?
- (https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=25453&p=313338&hilit=caption.replace#p313338)

---

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

## Checkpoints / debug / state consistency

- Improve Checkpoints DEBUG
- Reorder variable initialization. They are all over the place
- Adapt Load checkpoints to read some var  
  - (psychic => Knows Captain must be saved in checkpoints!!!)
- Continue LOSE LAST MUSIC status  
  - How to keep music to NOt restart on continue? Not major
- Details checkpoint view:
  - List of checkpoint (viewport with limit) Better text
  - Add type of “linked” choice: go downstair 1, 2, 3 / Drink 1, 2, 3  
    - => 3 cards but the highest one hide the first one
  - Need to Double click the list of Checkpoint????
  - (Hide Lock/unlocked in the checkpoint view when it’s too early for them to be unlocked… Need a start date for each checkpoint => Very Later)next
  - Add description for checkpoints (3 choices, two objects? Or just X unlocked)
- Call to function “Add_ending_checkpoint” not constant when called
- Simplify ALL definitions of add_ending_checkpoint to take only the name…
- Delete current_run if not needed anymore
- Force timeline/progress BEfore first death?
- Bug, Samuel Manning “LOCKED” text not center. Why just him???
- Better DEBUG mode  
  - => when start with debug (all the time for me) option to not count time, so I can do everything !!
- IN debug, have a choice, full testing mode that will set the appropriate variable
- STORYLINE NOT current character selected (when debug at least) TODO CHECK
- Endings code must look the same (diff between psycho and lad)

---

## Intuitions / endings / tutorial messaging

- Add  intuition button ????
- Rethink Intuitions as Endings with intuitions  
  - => Some endings are so terrible, that it will mark you soul in every plane of existence
- ADD menu tutorial when the first GReyed options is shown  
  - => “If this options is greyed it means you’ve made this choice at an earlier time.”
- should certain death just be considered intuition?????  
  - => simpler to understand
- OR BACK TO FIRST IDEA => Intuitions must be earned !!!!
- TWO texts for infocard? If did and didn’t ? With two pictures as well? So no need for both infocards?
- IDEA FOR ENDING: ASK THE player who the most likely culprit is  
  - Then it generates extra dialog with guilty part  
  - But for most people it ends with “PROBABILTY ERROR” message and stops when it becomes an impossibilty
- Show credit when Reach SURVIVE ending
- OTHER transition for FIRSt time (generic theme?)

---

## Bugs / known issues to re-check

- BUG - LAD knows_psychic background not working => Every choice is shown  
  - HAPPENS after reloading first checkpoint (ONLY IN debug mode)  
  - What’s happening with the create checkpoint thingy  
  - => Important to avoid problem while testing  
  - => BUT fixed with below solution  
  - Might be error some places else Though BE CAREFUL
- BUG after first death, info on map unlocking????? why?????
- BUG : bLINKINg when selecting a room ?????
- JUST put 0 for choices that are followed by a new menu!!!!!! => Test everywhere (map menus, sub menus,....)
- Go to bed Option not visible ENOUGH, people will clik on it by accident. Confirm dialog ?
- NOT obvious that you can click characters that are locked !!!!

---

## “Claythorn Manor” / UI / map asset notes

- Screen for introduction => Claythorn MANOR
- Small changes:
  - Elisabeth and others not aligned,
  - drop wall shadows
  - Servants stairs => Service Stairs 1 And 2 + Attic stairs, different keys?
  - Doors not same size
  - Rooms should be square
  - Remove grey lines
  - Add name of manor on the right
  - Remove too many doors for the downstairs servants stairs(only from portrait gallery
  - No hotspot for servants stairs SO no text? (use basement stairs)
  - Don’t make why were you invited here depends on tell me more about yourself?
  - Text zone should be bigger (Yaxis,
- Better image for Start menu
- Clean images ui file
- Mouse icon change on clickable => EVERYWHERE
- Put smaller mouse icons for web (and everywhere actually?)
- Menu with character, change character picture when hovering their name

---

## Tutorial

- Tuto
  - Rewrite Help Screen
  - Explain Log screen
  - Double check if we need to make a step by step tutorial for other tutorial
  - Add the tutorial text in the help menu (improve with multiple tabs?)  
    - Or the box on the left is a choice and the one on the right display the tutorial text
  - Explain why some text is grey (already pick this text havent you)
  - “If the text is dark, then you already have explore all the possible path following this choice)
- ADD TUTORIAL MENU
- Add tutorial text (special characters) for:
  - Unlock Observation
  - Unlock object
  - Unlock intuition
- Better Tutorial for progress view???

---

## Refactors / organization / architecture

- Refacto character information => top class with children (observations,...
- specific subclass FOR character informationLIST?
- Knowledge like choices?
- Create text for character with info not on line, but integrated.
- Conditions shortcuts in a CONSTANT files
- Refacto run menu, no need for var ??
- Only ONE button for character list (not a text and an image)
- NO need for text FOR EVERY menu map item (take simple default when no text)
- ?Different colour for character dialog
- ?Different Transition Style by character?
- OPTIONS menu (FORBID skip transition)
- LAbel disabled and window not working(style?) Was it working in initial theme?
- Hide other screens (same char selection, deaths,...)
- Be sure NVL is deactivated (OR make it work?)
- At unlocking character, show the character image (with fadout ?)
- Fix viewport in character page(fix size?
- Different sub class for menu (map menu, quickmenu, menu), for clarity
- TWO Class HOTSPOT => WTF???
- Add a property for some choice to never be grey (or use keep_alive)  
  - they are normally the exit button  
  - CHECK if there are other cases
- Saved_variables["day1_evening_map_menu"].hide_specific_choice  
  - => Should be done on ALL_MENUS now, because the menus are erased from init var when a new menu is called
- Better choices visuals
- Striped choices when visited partially => TOO complicated not important
- !!!! What about choice with conditions that can be met in the future?  
  - If a choice is grey it means there is no more choices in the next menu  
  - But it could be next time you play this dialog  
  - Find a way to keep it in Striped too?
- Menu? Need to save different menus in VAR or NOT?
- Find good autoformatter
- Look up all the TODO before next phase

---

## Web build / itch.io

- Use butler to upload files: it only uploads what's changed, generates patches for the itch.io app, and you can automate it.
- Problems webbuild for itch.io invite only (draft OR restricted
- CHANGE loading background => check web-presplash => NOT WORKING after build. Should I replace it each time?
- Change weird menu (in index html only?)
- Fix the web style for smartphone !!! (error in menu, bigger text?)
- Try to download all images BEFORE in progressive Loading
- FOR WEB => MAP other color when NOT ALREADY CLICKED???  
  - A third color ? Or replace insensitive with n??? Or a second choice when in map?

---

## Progress rebuild / persistence ideas

- Entirely REBUILD PROGRESS
- ONLY big choices saved, and once found, possibility to activate them
- BUT THEN it’s possible to only save important choices? But what about fun var like numbers of drinks,...?)
- BUG reset information? Mettre tout dans informationList?
- REplace SAVES and checkpoint by persistent data renpy? TOO complicated I think (fun variables like number of drinks…)

---

## Storyline / full testing mode / generator

- FULL STORYLINES GENERATOR => full_testing_mode .
  - Should be running without me pressing CTR
  - Should save DIALOGS not just choices (maybe in a tree, db or else?)
  - NORMAL loop 20s
- ALL possibilities generator
  - Loop over all possibilities for character, when reach an ending, save path, then starts again
  - Needs a tree of all possibilities =>
    - Sqlite? NOT possible https://lemmasoft.renai.us/forums/viewtopic.php?t=45801
    - JSONDB
    - So create json file?
  - Table node,
    - Is_end (bool,
    - menu_choices,
    - IS end() function, that will check if all subchoices exists and have is_end at true
  - The file shoulb be HUGE  
    - => So it’s important to group all the leaves with same results at the end (ending, AND important var/unlocked,...)  
    - Because we will have to start again from those endings for other characters, it’s gonna be exponential ….
  - AFTER JSON CREATED, I need a tool to read it properly, group by endings,....
- !! REformat record mode, maybe not needed anymore because of full_testing_mode,....

---

## Misc remaining notes (kept)

- Add Shortcut to character menu when choice between talking to multiple characters  
  - This way, we can decide to whom to talk to by clicking on the one with less information. Not major
- Replace all day1, day2 with the real day?
- Easter Egg options => use old visual (same_name but add old in the change location function!!!)
- Add new rooms generic content AND images
- Recheck map content ESPEcially basement (exclude gun room)
- Retest in depth progress and charting
- Make debug path to test quickly all endings
- Write credits (Credits with LOADING BAR !!!!)
- Rewrite code endings (info and labels) to something more efficient
- Build Claythorn manor extension for vs code  
  - New menu with more current options (change room, sound, music, and their values)
- For fun later, change faces when facing a choice (like abandoning amelia baxter, change her face to angry when hovering to leave her)
- ==> Better fix, rebuild the selected choice, custom menu logic ENTIRELY, to avoid errors when we don’t exit a menu (previously when choosing between hunt and no hunt)
- Make sure all menus have a unique name (make script to check that? Or fun hex search)
- Test -angry is still necessary, it doens’t feel like it is
- ?NOT DONE Think on a how to organise INTUITIONS, Knowledge, objects
- A NEW icon, when new information about a character is added  
  - check it exists, and if some fields are already hidden => change those fields to special var that will display an icon, or another style for already visited path  
  - OR add a param to menus that is never reset( menuhistory,) with every choice already visited in another timeline
- Replace all day1, day2 with the real day?
- Better DEBUG mode => when start with debug (all the time for me) option to not count time, so I can do everything !!
- Replace all day1, day2 with the real day?
- NORMAL loop 20s