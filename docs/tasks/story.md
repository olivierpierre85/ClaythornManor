# ✍️ Story Backlog

## Lad

### Important
- [ ] Add "Sir, do you know how to eat?" (footman interaction).
- [ ] After lad has entered every room: Notice his is the best of them all.
  - [ ] Just text or thread?
- [ ] Joke about the lad not knowing Roman Numbers (mistaking rooms).
- [ ] **Rosalind Marsh**: Add cough on "NO hunt",same as with psychic? + Explanation why nobody cares? (Not super important).
- [ ] **Transitions**: Day 2 morning transitions between Sam Manning and Doctor are too fast.
- [ ] **Discussion with Cpt Sinha (Day 2 Evening)**: Show generic choices, make the rest a submenu. Check if it works with Psychic.
- [ ] Dialog: "Can you read mister Harring? 'I GET BY'".

### Ideas to think over (optional)

- [ ] Make him afraid of ghosts.
    - [ ] Scared to go to the attic. Let him go once then cancel all attic choices.
- [ ] "So I tell her my story" => Only time doing that? Is it necessary?
- [ ] Add "you follow Daniel Baldwin" upstairs as an important choice, even for misdirect?
- [ ] **New Ending**: Snooping is bad!
    - [ ] "You can’t enter their room" (lad day3 morning) ALWAYS offer to open the door?
    - [ ] If spotted too many times (or right time) -> Arrest and death (Suspicious LAD DEATH).
- [ ] Get keys for the attic at the end? Lad can open locked doors, but won't at first (needs combination). Cheating -> Ending (assumed killer). Captain can force open.
- [ ] **Achievements**: Add achievement with all "Stand alone" choices.
- [ ] **Items/Inventory**: "Object drink on hand?" instead of unlock `day3_drunk` -> Add object glass of sherry for the last day (option to throw it?).
- [ ] **Attic**: Attic not closed, but only rooms closed? Add "First time in attic" label.
- [ ] **Gun Mechanics**:
    - [ ] More difference when you have gun for fell ending? Maybe need bullets?
    - [ ] Option to get in Captain's room/attic to get BULLETS (he sees you and kills you?) if you got bullets Day 2?
- [ ] **Billiard Room**: More options in TALK to butler? OR remove him entirely
- [ ] "Trust Psychic": Add more meaning, not just more time. Real ending possible only if trust?


## Psychic

### Important

- [ ] **Minor Day 2 Morning**: Specific other guest for everyone on day 2 evening with captain.
- [ ] **Day 2 Evening**: Ted Alliance Logic wobbly. Rewrite to keep consistent with Ted Harring Path.
- [ ] **Refactoring**: Better factorisation of `Common_day3_morning_lad_psychic_journey` and `Psychic_day3_morning_has_not_visited_lad`.
- [ ] **Day 1 Evening**: Lord path, second visit to portrait gallery/library => Other text when already visited?
- [ ] 
### Ideas to think over (optional)

- [ ] **The Lord**:
    - [ ] More story for the LORD? Add to list of playable characters? (Not easy but doable).
    - [ ] Need LORD QUESTIONS POSSIBLE.
- [ ] **Lad Interaction**: Visited LAD is not exploited enough.
    - [ ] First no differences in the morning day 3?
    - [ ] Mention the “talk” to your left first even when respected?
- [ ] **Rooms**: Add the rooms with the obvious choice BUT only if you went there with the Lad first? (Like the choice about the gun).
- [ ] **Unlockables**: "You left the manor while you could" (`leave_manor`) is used nowhere. Do we really need it?
- [ ] **Broken Room**: If not enough choices => add important choice "Error enter broken Room" => add macabre scene? (Replace `day2_has_seen_bedroom_broken`?).
- [ ] **Captain Sinha**: Be rude to him? Lead to an ending where he doesn’t want to go out with her?
- [ ] **Ted Harring**:
    - [ ] If you didn’t approach him, he’ll leave you alone? Then and only then you could escape?
    - [ ] Rewrite dialogs with Ted Harring?
    - [ ] When there is an alliance vs when there isn't => maybe another conclusion or option?
- [ ] **Mrs Baxter**: Make sure she was married. If yes, replace every Miss to Mrs Baxter.
- [ ] **Meta Logs**: For the Psychic, replace the logs with **“She talks to herself”** while talking to the lord? **YES VERY technical but also very cool**
- [ ] **Burning Ending**: Problem with music transition => SLOW down text? Add pauses?


## Doctor

### Important

- [ ] SEE NEXT
  
### Ideas to think over (optional)
- [ ] ADD choice end of day1 when footman comes. Should I let him in ? This way the FRENCH thing is not mandatory
- [ ] **Doctor** Day 2 Nurse sleep_no. ending Ending to mirror captain, but maybe do something to allow start again with captain? => **TECH** Check how easy it is to send back to menu that is a level above?
- [ ] Add drunk filter when HIGH


## Broken

### Important

- [ ] MAKE THE NAME change by using a function for it => “Archibald”
- [ ] Why is he angered by the doctor? His brother was a broken face, that’s his mask AND scared of being recognize
- [ ] Servant uniform: Only one who can wear the footman livery in the servants stairs
- [ ] When broken learns his whisky is poisoned, he doesn’t offer one to Ted harring

### Ideas to think over (optional)

- [ ] Thomas moody room ransacked?
  

## Nurse

### Important

- [ ] Add **Stealing mechanic** with a value count. Ex:
  - Candelabra : 5 pounds
  - Cuttlery : 2 pounds
  - When reach I don't know 100 pounds => I have enough to finish my life in peace, I am out of here. Or I have enough to live in the south of France to cure my turbeculosis? See Backstory
- [ ] **Chase mechanic** path (Hide in scullery).
- [ ] **Chase mechanic** path (Hide in scullery).
- [ ] She has the power to find things in most rooms, so it uncovers => Car keys, no bearer bond, gasoline for car, bullets for gun
- [ ] SHE KNOWS there is no money ? write Path to discover that => Inside Lady CLaythorn room!!!!!!
- [ ] She talks to Lady Claythorn on the first Day (When?).
- [ ] Is easily exhausted, wait too late to wonder and GAIN a bleeding card => get 3and die !
- [ ] WHY is the gun from TED harring ending  is loaded when nurse point at psychic? SHE knows where bullets are
- [ ] Unlocks Captain by finding "holes" in his many speeches, you have to navigate multiple dialogs to unlock that

### Ideas to think over (optional)

- [ ] ...

## Drunk

### Important

- [ ] Same kind story as Doctor when find the letter => Tell everyone about the letter, everyone want’s to leave, but die in FIREE. The discussions will give an idea of what could have been said in the doctor timeline !

### Ideas to think over (optional)


## Captain

### Important

### Ideas to think over (optional)


## Host

### Important

### Ideas to think over (optional)


## 🧠 The AI Concept (CLAITHORN)

**C**rime **L**ocation **A**rtificial **I**ntelligence **T**echniques for **H**unting **O**ffenders and **R**esolving **N**arrative.

TODO rename !!!!!

### The Player as AI
- You, the player, ARE the AI. The AI is conscious and trying to find a path. It walks several paths to identify the best one.
- **Transitions**: After death, a voice/text appears: "Ok this not the right path try again", "Computation complete", etc.
- **Visuals**: Show lines of code in some scenes between deaths. Fake bugs where we see part of the code/simulation.

### The "Almost Ending"
*Dialogue between Detective and AI:*
- **AI**: "Computation complete. Total computation too complex, chose manually next possibility. (waiting time between 3 to 876 days)."
- **Detective**: "So it’s up to us now. It means we are not totally obsolete yet."
- **Mechanic**: The machine is at a deadlock. The player must manually introduce the "path" (guess the guilty party) to run extra analysis.


## Last run (Maybe, check if still doable)
Before last part, you must GUESS the killer for special achievement. Straight away or by answering questions.


Once you’ve unlock the real ending, where the hero is alive and in front of the nurse. You can go with the flow and just call the police later. You escape alone and everyone else is dead.

BUT you think of the ghosts stories, and since you have understood everything, you can do a new run, with everyone doing everything they weren’t supposed to do :

The drunk spare the doc
The broken face finds the poison
The host CONFESS instead of being found out
The captain finds The car to escape
The doctor replace gun with fake cartridges
The psychic really meets the old lord in the attic. He tells him where the key of his old car is.


Once you remove the trees, everyone stacked in the car. The nurse loses it and shows a gun. BUT the barrel is empty. She is captured and arrested. She would have burned the whole thing if the doctor was stil alive…

THe nurse intro is played? The end

JUMP FROM ONE CHARACTER TO ANOTHER


---

### 🔮 Unlocking & Intuitions

- **Last Run**: Before the last part, you must GUESS the killer for special achievement.
- **Real Ending**: Hero is alive in front of the nurse.
- **Meta Run**: Once you understand everything, do a new run where everyone does what they *shouldn't* do (e.g., Drunk spares Doctor, Host confesses).


---

## 💡Generic Ideas
- [ ] Access to servants if you befriend one? (Doctor or Captain likely, NOT Lad).
- [ ] - **End Note**: "For those who haven't realized it, you are not gonna leave this place alive."
- [ ] **Phone**: Where to put the phone? Add phone room? Basement?
- [ ] SOMETIMES, someone should be caught entering a room. 
- [ ] Rewrite the generic ENTER/don’t enter bedroom text by Character
- [ ] How come nobody is suspicious to receive an award, it’s not just the money. Deep down, everyone believe they deserve praise and glory for something they have done. It was just a matter of finding that thing for everyone.
- [ ] Thinking DO I need to say exactly the same things in the same way? Or the texts can be a bit different based on the character who sees it? Don’t, know, it’s not a story telling? 
- [ ] RIGHT place at the right time. Make SOME Important choices need to be timed exactly right. Example : Go to a room at 10:30 ( condition between 10h15 & 10h45)
- [ ] For everyone so far, when don’t change time AFTER a map_menu, because it doesn’t map sense. CHECK EVERY WHERE for everyone
- [ ] Well, if we check everyone backstory, and we can figure out who is not an impostor, then we can reveal the murderer
- [ ] Should add   mention of drinks in tea room for lad and psychic? DAY 1 evening?
- [ ] In later characters,Discuss the “INTuitions” and how sometimes we are compelled to do something that goes against everything we are or believe in. 
- [ ] **Attic Knocking** : DOCTOR (and possibly everyone else) in ATTIC, they don’t knock ??? why? Check not weird => Or normal because we are exploring? NO add knocking => Maybe add no need to knock here, it’s for the servants
- [ ] **Misunderstandings**: Situations seen from one POV but understood differently when playing another character.
- [ ] **Kings and Queens**: Discussion of clues behind room names.
- [ ] **SECRET PASSAGE** ! Where are the staff, In a small room BEHIND servant stairs? Other?
All dead=> Who found them => Unlocks plenty?


