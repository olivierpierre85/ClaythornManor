<!-- # cSpell:disable -->

## Technical Tasks !IMPORTANT USE FABLE 5 why we can!!!!!

Ongoing AI ollama tester, try with longer run. maybe needed to use a better LLM that local

IDEA => For choices already made (greyed out, add the time they will consume?)

### ???? INTUITION system entirely FOR EVERYONE SAVED concept
Now an intuition is needed to SAVE a person.
When Someone is saved, it add a SAVED over their name in the progress view

- (need a lot of new images)
- Need a new var saved over time for each character. (is_saved)

- [ ] BUG: **save_transcript_to_file** button not working during menu????

- [ ] BUG (structural FABLE FINDING): chapters are entered with `call <chapter_label>` from each character's `_main.rpy` (e.g. `call captain_day2_hunt_moody_alive`), but branches that reach an ending exit via `jump captain_ending_xxx` instead of `return`. Ren'Py's `call`/`return` stack is global and only popped by `return` - a `jump` leaves the pushed return address dangling forever (it's even saved in savegames). Over a full playthrough this piles up dozens of orphaned stack frames from every character death, and was directly visible in a crash traceback where a `captain` call frame sat as the "parent" of an unrelated, currently-executing `lad` call frame. Harmless by itself, but a stray extra `return` anywhere in the game could eventually pop into one of these stale frames and teleport execution into unrelated script. Proper fix likely means auditing every `_main.rpy` "call chapter" site + every ending label across all 8 characters, and either switching those calls to `jump` or making endings `return` instead of `jump`.

----
TODO myself, clean the tutorial highlights, text and position.

For the progress view, just say you can explore it and the other tutorials start they open the screen
----------------------------------------------------------
Chages for consistency:
   - Rethink the letter to the captain to comply more with the Journalist story
  
GARDEN and entrance same on map but not on pictures?

Servant stairs as last room => needs testing for other characters

SERVANT STAIRS and downstairs IS the same ?? shouldn' we cross it to go downstairs? Add the servant stairs as the image when we try to reach downstairs? servant stairs could be servant room, or the upstairs stairs. But it will be fixed when we change the map

### Write Story: NEXT => Broken

- REWRITE ALL THREADS, too complexe text

- ADD MORE MORE questions in the generic menus (Doctor, Drunk, host) to confuse the player and make the game more challenging.

- Test the changing MALUS and the whole Broken branching logic.

- **Broken is well suited to uncovering the Host**, but at the moment the Captain is the one who does it.
- Decide: either make Broken the character who unlocks the Host, or have him simply realise she is keeping information to herself. In the latter case, the natural way to learn more about her is to interrogate the staff.  If he does, the Killbreath discovery can come right at the start.

##### **Friday Evening**


##### Saturday — After Dinner

you need to convince everyone something is not right.
=> You have to admit who you are.
=> THere must be clues downstairs. 
  - Kitchen totally empty, no staff;
=> Lady Claythorn not there

REDO FULL upstairs => Nobody is there?

REDO full billiard room

Mybe Later => Staff oddities use the same picture with 4 Numbers

MAYBE later => new ending, find the staff dead in the garden shed??? Not necessary for story but dramatic effect. Only if i can see it in the picture

##### Sunday Morning 
If you survived with everyone but TED harring and host (who sneaked out after dinner), you are now face with what to do. You know you have to leave but how and with whom?
- The car is gone, can you use the other car? NOt enough room?
THE WHol stuff can be decided at the end of the writing


## Assets & artistic Tasks


### BROKEN : 

PHONE IMAGE 
need a staff leaving image

NEED a version unmaske of broken for when he is downstairs. I think I have it

### OTHER


PROBLEM, **PSYCHIC** death in attic during the day not as scary as during the night. Change that?

### IMAGES NEXT REBUILD

- [ ] For info_cards, RENAME so it's correct, then change everything to webp?
- [ ] NEW NAME NEEDED ("Blackthorn Manor" / AIMERE (Artificial Intelligence Module for Evidence Reconstruction & Evaluation : AImere House => look again (AI-MERE I am here?))).

### Characters
- [ ] Redraw character face AND add full body size images

#### Locations
Finish normal list- last one is train_second
Multiple Class in train for outside IMAGEs
- Two class at the moment. I think One image by person is more appropriate, with hints in them (bags,...). See to do it later in V4 ()
  
### MAPS

Redraw BETTER maps for manor, not

  
### MUSIC with producer AI
Get new music from internet and put them at the right place



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
 




