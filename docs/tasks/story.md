# ✍️ Story Backlog

## Lad

### Important
- [ ] Add "Sir, do you know how to eat?" (footman interaction).
- [ ] After the lad has entered every room, have him notice his is the best of them all.
  - [ ] Decide: just narration, or a thread?
- [ ] Joke about the lad not knowing Roman numerals (mistaking room numbers).
- [ ] **Rosalind Marsh**: add a cough on "no hunt", same as with the psychic? Plus an explanation of why nobody cares? (Not super important.)
- [ ] **Transitions**: Day 2 morning transitions between Samuel Manning and the doctor are too fast.
- [ ] **Discussion with Captain Sinha (Day 2 Evening)**: show the generic choices, make the rest a submenu. Check it still works with the psychic.
- [ ] Dialogue: "Can you read, Mister Harring? 'I GET BY'".
- [ ] `lad_generic_menu`: no mention of the weather? Add one, or a reason why not.
- [ ] Forest images for the hunt do not change for lunch — fix.
- [ ] REthing the logic of psychic meeting him in between map choices. It becomes to confusing when playing psychic. see psychic too

### Ideas to think over (optional)
- [ ] Is the complicated way of meeting the captain on Day 3 necessary? Overcomplicated for no reason? Maybe just meet him once the time has passed (but then we need a way to skip time).
- [ ] Make him afraid of ghosts.
  - [ ] Scared to go to the attic. Let him go once, then cancel all further attic choices.
- [ ] "So I tell her my story" — is this the only time we do that? Is it necessary?
- [ ] Add "you follow Daniel Baldwin upstairs" as an important choice, even as a misdirection?
- [ ] Make him fake his own death on Day 3, so he can spy on everyone once he realises he has been tricked into killing the doctor.
- [ ] **New ending**: snooping is bad.
  - [ ] "You can't enter their room" (lad, Day 3 morning) — always offer to open the door?
  - [ ] If spotted too many times (or at the wrong time) → arrest and death (suspicious lad death).
- [ ] Get keys for the attic at the end? The lad can open locked doors, but won't at first (needs the combination). Cheating leads to an ending (assumed killer). The captain can force it open.
- [ ] **Achievements**: add an achievement for all "stand alone" choices.
- [ ] **Items/Inventory**: "object: drink in hand?" instead of unlocking `day3_drunk` — add an object, glass of sherry, for the last day (option to throw it?). Love it.
- [ ] **Attic**: only individual rooms should be closed, not the whole attic. Add a "first time in attic" label.
- [ ] **Gun mechanics**:
  - [ ] More difference when you have the gun for the "fell" ending? Maybe requires bullets?
  - [ ] Option to sneak into the captain's room/attic to get bullets (he sees you and kills you) if you got the gun on Day 2?
- [ ] **Billiard room**: more options in "talk" with the butler, or remove him entirely?
- [ ] "Trust the psychic": give it more meaning than just extra time. Should the real ending only be possible with trust?
- [ ] Day 3 morning: add a way to skip the search and just wait?


## Psychic

### Important
- [ ] **Minor, Day 2 Morning**: a specific other guest for everyone on Day 2 evening with the captain.
- [ ] **Day 2 Evening**: Ted alliance logic is wobbly — rewrite to keep it consistent with Ted Harring's path.
- [ ] **Refactoring**: better factor out `common_day3_morning_lad_psychic_journey` and `psychic_day3_morning_has_not_visited_lad`.
- [ ] **Day 1 Evening**: lord path — on a second visit to the portrait gallery/library, show different text since it's already been seen?
- [ ] **Nurse's death**: the killing by the nurse is too violent, or it lacks an explanation, and it makes players hate the psychic. Needs a reason.

### Ideas to think over (optional)
- [ ] **The lord**:
  - [ ] More story for the lord? Add him to the list of playable characters? (Not easy, but doable.)
  - [ ] Need a set of possible lord questions.
  - [ ] Problem: the psychic's death in the attic isn't as scary during the day as at night. Change that (force night, or move when she can unlock it, e.g. the day before)?
- [ ] **Lad interaction**: having visited the lad isn't exploited enough.
  - [ ] No difference on the morning of Day 3 currently?
  - [ ] Mention the "talk" option to her left first, even once respected?
- [ ] **Rooms**: add the obvious room choice, but only if she went there with the lad first (like the choice about the gun)?
- [ ] **Unlockables**: "you left the manor while you could" (`leave_manor`) is unused. Do we need it?
- [ ] **Broken's room**: if there aren't enough choices, add an important choice "wrongly entered Broken's room" → a macabre scene? (Replace `day2_has_seen_bedroom_broken`?)
- [ ] **Captain Sinha**: option to be rude to him, leading to an ending where he doesn't want to leave with her?
- [ ] **Ted Harring**:
  - [ ] If she didn't approach him, does he leave her alone? Only then could she escape?
  - [ ] Rewrite the dialogue with Ted Harring?
  - [ ] Different conclusion or options depending on whether there is an alliance?
- [ ] **Mrs Baxter**: confirm whether she was married — if so, replace every "Miss" with "Mrs Baxter".
- [ ] **Meta logs**: for the psychic, replace the logs with "she talks to herself" while talking to the lord? Very technical, but also very cool.
- [ ] **Burning ending**: problem with the music transition — slow down the text, add pauses?
- [ ] Have her say, somewhere, that she never had children of her own — almost one, "but God took him away from me at birth".


## Doctor

### Important
- [ ] See next.
- [ ] Once other characters are done, rewrite the part where the doctor gets out of the library and is immediately caught by the lad and the psychic — too lazy as written.
  - [ ] Also, the end of the nurse's paths teaches you almost nothing — change that.

### Ideas to think over (optional)
- [ ] Add a choice at the end of Day 1 when the footman comes: should I let him in? This way the French subplot isn't mandatory.
- [ ] **Doctor, Day 2, nurse "sleep_no" ending**: mirror the captain's ending, but find a way to allow restarting with the captain? **Tech**: check how easy it is to send the player back to a menu one level above.
- [ ] Add a drunk filter when high.


## Broken

### Important
- [ ] Maybe later: staff oddities use the same picture with four numbers.
- [ ] There's still a small hole in the poisoned-whisky scene — the psychic would have made clear it was meant for Broken, not just left standing there on the table. Minor.
- [ ] Fix impossible-to-reach coverage.
- [ ] Add more questions to the generic menus (doctor, drunk, host) to confuse the player and raise the challenge.
- [ ] Test the changing malus and the whole Broken branching logic.
- [ ] Important: why not just knock on bedrooms? He doesn't have to enter them — add logic for "nobody answers"? Rethink and test.
- [ ] Hear Samuel Manning admit he has been pretending to be drunk.
- [ ] Broken is well suited to uncovering the host, but at the moment the captain is the one who does it.
  - Decide: either make Broken the character who unlocks the host, or have him simply realise she is keeping information to herself. In the latter case, the natural way to learn more about her is to interrogate the staff — if he does, the Killbreath discovery can come right at the start.
  - Or: the drunk is unlocked by Broken, and the host is unlocked by the drunk.

### Ideas to think over (optional)
- [ ] Could add a "go to the bar first" option, so Ted Harring doesn't die. (Keeping him alive is complicated, though.)
- [ ] Sounds like the mask shouldn't be tin, not wood
- [ ] Make it so the captain unlocking Broken for the "three Moody lives" reads better if the captain plays it first.
- [ ] There's almost no hint of what really happened in the Boxer Rebellion — add some of that in, in the Day 3 questions. Should the story of the baby and the nurse go here too, or is that too obvious?


## Nurse

### Important
- If she looks for treasure on the last day, she will die, and also won't find the jewellery — the butler has taken it all with him before leaving.

### Ideas to think over (optional)
- [ ] Add dialogue with the doctor to help draw the connection with the Boxer Rebellion (billiard room, Day 1)?
- [ ] Intro is too generic. Add a dream, or something more personal? Decent as it is, but could be improved.
- [ ] **Last day, rethink**: too many last-day endings. Only one escape should be possible.
  - Nurse dies exhausted on the road? Maybe not a very useful ending — if she's exhausted, she simply can't escape and is forced to nap instead.
  - If she doesn't have enough money, she just can't leave. That would remove both "escape and die exhausted" and "escape poor" — or just delete "escape poor"?
- [ ] Money counter? E.g. "if I had £500, I'll be fine" — needs pearls + silverware? Maybe not.
- [ ] Queen Alexandra reference isn't clearly tied to the nurse.
  - [ ] Replace with a thief king or queen for foreshadowing? Henry VIII, Charles I, or Prince John (Robin Hood)?


## Drunk

### Important
- [ ] Same kind of story as the doctor's when he finds the letter: tell everyone about the letter, everyone wants to leave, but they die in the fire. The discussions could hint at what could have been said in the doctor's timeline.
- [ ] He's the one who can reach Sunday evening — he sees the psychic waking Ted Harring up, if he managed to save him from the poison. How could he save everyone, though?
- [ ] Somewhere, add a dialogue between an immigrant who would do anything for a wealthy person's position, and the wealthy person sharing suicidal thoughts. (Drunk vs. lad? Drunk vs. captain? Though neither is really an immigrant — one is British, the other rich.)
- [ ] Add a food menu — the only real enjoyer of this place.
- [ ] The drunk has seen Dr Baldwin's abuse — add this to his story.

### Ideas to think over (optional)
- (none yet)


## Captain

### Important
- [ ] When escaping by car, maybe mention that the road should be blocked (and isn't, actually).
- [ ] Rethink the letter to the captain so it fits the journalist story better.

### Ideas to think over (optional)
- [ ] Add a mysterious sound when Thomas Moody appears — the first time we see him alive on Day 2. Or at least an ominous "there's no reason he shouldn't be there," though maybe too obvious.
- [ ] Expand on his noble upbringing in the generic dialogues.
- [ ] The captain can't have the key if it's in his hunting jacket — what would make him take it? Minor.
- [ ] Make it so the captain unlocking Broken for the "three Moody lives" reads better if the captain plays it first.
- [ ] Not important: odd that the captain doesn't run into the others on Day 3 morning — is he hiding on purpose? Think about it later.
- [ ] No generic menu for the captain — no way to ask a random question to the host or others? Change that, or leave it as is?


## Host

### Important

### Ideas to think over (optional)
- [ ] Why is her name never mentioned?
- [ ] broadway backstage or outside image for the introduction?


## Butler

### Unlock mechanic (partly implemented)
- To finish the game, the butler must be unlocked like any other character (all important hidden infos).
- [x] First info, `manages_weekend` (he is managing the weekend for someone), unlocks after the death text of the captain's `burned` and `shot_butler` endings (same paths as the host's `not_guilty`).
- [x] He appears in the progress view as soon as any info about him is discovered (`is_butler_visible()` replaces the old static flag).
- [x] A butler-specific tutorial text is shown after the death text, on the first unlocked info (same pattern as the first-death tutorial in `ending_generic`).
- [ ] TODO: unlock points for the remaining infos (`poisoned_moody`, `took_valuables`).

### Important
- Add somewhere that, in the canon story, Ted Harring drinks from Broken's flask but survives by drinking so much he pukes.
- This is the last test — the real path (as asked by the meta dialogues).
- Last question: when does the butler meet the person behind all of this? He escapes and meets them in town — the final choice.
  - First: will Thomas Moody listen to Sinha? Yes, so he's poisoned. And so forth — it should be straightforward.
- Idea: the butler is a hired thug, in it for the money, not to kill, but not unwilling to either. Or a lover of the psychic, having met her in service? Check against the afternoon deaths.


## 🧠 The AI Concept (CLAITHORN)

**C**rime **L**ocation **A**rtificial **I**ntelligence **T**echniques for **H**unting **O**ffenders and **R**esolving **N**arrative.

- [ ] TODO: rename — urgently.

### The player as AI
- You, the player, ARE the AI. The AI is conscious and trying to find a path, walking several to identify the best one.
- **Transitions**: after a death, a voice/text appears: "OK, this is not the right path, try again," "Computation complete," etc.
- **Visuals**: show lines of code in some scenes between deaths — fake bugs where part of the code/simulation is visible.

### Second idea: Claythorn as a training game
You are an inspector (with two junior inspectors for dialogue), in charge of learning to use the AI to solve crime, with visual aid.

Working title: **VAcsAI** (Visual Aid Crime Solving AI), or a variation on that.

### The "almost ending"
*Dialogue between detective and AI:*
- **AI**: "Computation complete. Total computation too complex — chose manually next possibility. (Waiting time between 3 and 876 days.)"
- **Detective**: "So it's up to us now. It means we are not totally obsolete yet."
- **Mechanic**: the machine is at a deadlock. The player must manually introduce "the path" (guess the guilty party) to run extra analysis.

Then the final path — what actually happened — is played, but without saying who did it. If the player is wrong, it stops as soon as it stops making sense: game broken, restart.

### Final option?
Once you have the "what happened" path right, you can activate the **Saved Everyone** path — send it to the past, and change the future. That's the beauty of the new technology (maybe too convoluted?). AI is not the future — changing the past is. Or maybe this is the alpha version, setting up a prequel for the next game?

### Real run
You must guess the right path:
- When does Thomas Moody die, and why, and when? His flask was switched while he was listening to the captain's story.
  - TODO: change the lad's dialogue — he was so absorbed in Captain Sinha's story that he forgot his flask next to the bar. Without that, Moody doesn't die.
- Did Ted Harring follow the doctor upstairs?
- What are the groups for the hunt?
- Who comes to see the captain in the billiard room on Saturday evening?
- Who survives?

### Last run (maybe — check if still doable)
At the very end, or at the start, you must guess the killer for a special achievement, either straight away or by answering questions.

Once you've unlocked the real ending — where the hero is alive, in front of the nurse — you can go with the flow and just call the police later. You escape alone, and everyone else is dead.

But you think of the ghost stories, and since you've understood everything, you can start a new run where everyone does everything they weren't supposed to do:
- The drunk spares the doctor.
- Broken finds the poison.
- The host confesses instead of being found out.
- The captain finds the car to escape.
- The doctor replaces the gun with fake cartridges.
- The psychic really meets the old lord in the attic — he tells her where the key to his old car is.

Once the trees are cleared, everyone is packed into the car. The nurse loses it and pulls a gun, but the barrel is empty — she is captured and arrested. She would have burned the whole place down if the doctor were still alive.

Then the nurse's intro plays again. The end.

Jump from one character to another.

---

### 🔮 Unlocking & intuitions
- **Last run killer**: before the last part, you must guess the killer for a special achievement.
- **Last run story**: *(to be defined)*
- **Real ending**: hero is alive, in front of the nurse.
- **Meta run**: once you understand everything, do a new run where everyone does what they *shouldn't* (e.g. the drunk spares the doctor, the host confesses).

---

## 💡 Generic Ideas
- [ ] Access to servants if you befriend one? (Doctor or captain, most likely — not the lad.)
- [ ] **End note**: "For those who haven't realised it, you are not going to leave this place alive."
- [ ] **Phone**: where to put the phone? Add a phone room? Basement?
- [ ] Sometimes, the player should be caught entering a room.
- [ ] Rewrite the generic enter/don't-enter-bedroom text per character.
- [ ] Why isn't anyone suspicious about receiving an award? It's not just the money — deep down, everyone believes they deserve praise and glory for something they've done. It's just a matter of finding that thing for each character.
- [ ] Do all characters need to say exactly the same things in the same way, or can the text differ slightly depending on who witnesses it? Unclear if that undermines the storytelling.
- [ ] **Right place, right time**: some important choices could need precise timing, e.g. go to a room at 10:30 (condition between 10:15 and 10:45).
- [ ] For everyone so far, check that time never advances right after a `map_menu`, since it wouldn't make sense — check everywhere, for every character.
- [ ] If we examine everyone's backstory and work out who isn't an impostor, can we reveal the murderer that way?
- [ ] Should there be a mention of drinks in the tea room for the lad and the psychic on Day 1 evening?
- [ ] In later characters, discuss "intuitions" — how we're sometimes compelled to do something that goes against everything we are or believe in.
- [ ] **Attic knocking**: the doctor (and possibly everyone else) doesn't knock in the attic — is that weird, or normal since they're exploring? Maybe no need to knock there, since it's for the servants.
- [ ] **Misunderstandings**: situations seen from one POV but understood differently when playing another character.
- [ ] **Kings and queens**: discuss the clues behind room names.
- [ ] **Secret passage**: where is the staff quarters — a small room behind the servants' stairs? Something else?
  - All dead → who finds them → unlocks plenty?
