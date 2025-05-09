# Characters description
# TODO REWRITE EVERYTHING
# INFORMATION LIST should have ALL the information 
# BUT now extra_information is list and others are CharacterInformationList

style narrator_style:
    properties gui.text_properties("dialogue")
    color gui.idle_small_color 
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos - 17
    italic True

style letter_style:
    properties gui.text_properties("dialogue")
    color gui.idle_small_color
    font gui.name_text_font
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos - 10

style tutorial_style:
    properties gui.text_properties("dialogue")
    color gui.highlight_color
    font gui.name_text_font
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos - 10

style progress_bar:
    left_bar Frame("gui/bar/progress_bar_left.png", gui.bar_borders)
    right_bar Frame("gui/bar/progress_bar_right.png", gui.bar_borders)

label init_characters:
    # Inside voice style
    define narrator = Character(None, what_style="narrator_style")

    # Non Playable Characters
    define tutorial      = Character("Tutorial", what_style="tutorial_style")

    define letter       = Character("Letter", what_style="letter_style")
    define book         = Character("Book", what_style="letter_style")
    define butler       = Character("Butler", image="butler")
    define footman      = Character("Footman", image="footman")
    define maid_name    = "Young woman"
    define maid         = Character(maid_name, image="maid")
    define lord_name    = "Older Man"
    define lord         = Character(lord_name, image="lord")

    python:

        #  Character full List
        # TODO only use the flat one (refacto use chara)
        char_list = [ 
            [ lad_details, doctor_details, host_details, drunk_details ] , 
            [ psychic_details, broken_details, captain_details, nurse_details ] 
        ]

        char_list_flat = [lad_details, doctor_details, host_details, drunk_details, psychic_details, broken_details, captain_details, nurse_details]

    return

# LABELS
label character_selection:
    scene black_background
    narrator "Select a Character"

    python:
        if not full_testing_mode:
            character_choice = renpy.call_screen('character_selection') 
        else:
            character_choice = full_testing_mode_char

        current_position = 0

        current_character = eval(character_choice + "_details")
        current_run = current_character.get_max_run() + 1 # TODO why? wtf?
        current_storyline = current_character

        current_checkpoint = current_character.get_init_checkpoint()
        

    show screen in_game_menu_btn
    show screen custom_key_listener
    
    jump start_again

init -100 python:
    def get_char(text_id):
        if text_id == "lad":
            return lad_details
        elif text_id == "doctor":
            return doctor_details
        elif text_id == "host":
            return host_details
        elif text_id == "drunk":
            return drunk_details
        elif text_id == "psychic":
            return psychic_details
        elif text_id == "broken":
            return broken_details
        elif text_id == "captain":
            return captain_details
        elif text_id == "nurse":
            return nurse_details
        else:
            return False

    # Python Classes
    class CharacterInformationList:
        def __init__(
            self, 
            information_list,
            notification_text = None,
            notification_sound = None,
        ):
            self.information_list = information_list
            self.notification_text = notification_text
            self.notification_sound = notification_sound

        def __str__(self):
            return self.information_list

        def get_list(self):
            return self.information_list
        
        def get_item(self, text_id ):
            for info in self.information_list:
                if text_id == info.text_id: 
                    return info
        
        def unlock(self, text_id, is_restart = False):
            global seen_tutorial_progress
            for info in self.information_list:
                if text_id == info.text_id and info.locked:
                    info.locked = False
                    info.discovered = True

                    if not hide_notifications and not is_restart:
                        if self.notification_text:
                            renpy.notify(self.notification_text)
                        if self.notification_sound:
                            renpy.play(self.notification_sound, "sound")

            if not seen_tutorial_progress:
                seen_tutorial_progress = True
                renpy.call('tutorial_progress')

        def is_unlocked(self, text_id):
            for info in self.information_list:
                if text_id == info.text_id:
                    return not info.locked
            return False

        def get_unlocked(self):
            unlocked = []
            for info in self.information_list:
                if not info.locked:
                    unlocked.append(info.text_id)
            return unlocked

        def __iter__(self):
            return iter(self.information_list)

    # Extensions of information list
    class CharacterImportantChoiceList(CharacterInformationList):
        def __init__(self, important_choice_list):
            super().__init__(
                important_choice_list,
                notification_text = "This decision may have consequences",
                notification_sound = "audio/sound_effects/writing_short.ogg"
            )
            for item in important_choice_list:
                item.type = "choice"


    class CharacterEndingList(CharacterInformationList):
        def __init__(self, ending_list):
            super().__init__(
                ending_list,
                is_intuition
            )


    class CharacterObservationList(CharacterInformationList):
        def __init__(self, observation_list):
            super().__init__(
                observation_list,
                notification_text = "You have made a new observation",
                notification_sound = "audio/sound_effects/writing_short.ogg"
            )
            for item in observation_list:
                item.type = "observation"


    class CharacterObjectList(CharacterInformationList):
        def __init__(self, object_list):
            super().__init__(
                object_list,
                notification_text="You have found a new object",
                notification_sound="audio/sound_effects/writing_short.ogg",
            )
            for item in object_list:
                item.type = "object"


    class CharacterDescriptionHiddenList(CharacterInformationList):
        def __init__(self, information_list, character_name):
            super().__init__(
                information_list,
            )
            self.character_name = character_name

        def unlock(self, text_id):
            global seen_tutorial_description_hidden, seen_tutorial_unlock_character, show_tutorial_unlock_character
            for info in self.information_list:
                if text_id == info.text_id and info.locked:
                    # Unlock the info
                    info.locked = False
                    info.discovered = True
                    if not hide_notifications:
                        renpy.notify("You have found information about " + self.character_name)
                        renpy.play("audio/sound_effects/writing_short.ogg", "sound")

                    if self.all_description_hidden_unlocked():
                        if not hide_notifications:
                            # Unlock a character
                            renpy.pause(2)
                            renpy.play("audio/sound_effects/unlock_char.ogg", "sound")
                            renpy.notify("You have unlock a new Character : " + self.character_name)
                            if not seen_tutorial_unlock_character:
                                seen_tutorial_unlock_character = True
                                show_tutorial_unlock_character = True
            
            if not seen_tutorial_description_hidden:
                seen_tutorial_description_hidden = True
                renpy.call('tutorial_description_hidden')

        def all_description_hidden_unlocked(self):
            for info in self.information_list:
                if info.locked:
                    return False
            return True


    class CharacterInformation:
        def __init__(
            self, 
            order,
            text_id,             
            content, 
            content_negative = None,
            locked = True,
            is_important = False,
            image_file = None,
            is_intuition = False,
            chapters = [],
        ):
            self.order = order
            self.text_id = text_id
            self.content = content
            self.content_negative = content_negative
            self.locked = locked
            self.is_important = is_important
            self.image_file = image_file
            self.is_intuition = is_intuition
            self.chapters = chapters
            self.discovered = False
            self.type = None


    class CharacterDetails():
        def __init__(
            self, 
            text_id,
            description_hidden,
            important_choices,
            endings,      
            objects,
            observations, 
            progress,
            saved_variables = dict(),
            test_checkpoints = dict(),
            locked = True,
            know_real_name = True,
            real_name = "",
            nickname = "",
            description_short = "",
            description_long = ""            
        ):
            self.text_id = text_id
            self.locked = locked
            self.know_real_name = False    
            self.real_name = real_name 
            self.nickname = nickname
            self.description_short = description_short
            self.description_long = description_long
            self.description_hidden = description_hidden or []
            self.important_choices = important_choices or []
            self.endings = endings or []
            self.objects = objects or []
            self.observations = observations or [] 
            self.progress = progress or [] 
            self.saved_variables = saved_variables or dict()
            self.checkpoints = []
            self.test_checkpoints = test_checkpoints or dict()
            

        def get_name(self):
            # if self.know_real_name:
            return self.real_name
            # else:
            #     return self.description_short
        
        def reset_information(self):
            for info in self.objects:
                info.locked = True
            
            for info in self.observations:
                info.locked = True

            for important_choice in self.important_choices:
                important_choice.locked = True

        def get_description_full(self):
            text_with_holes = self.description_long
            for char_info in self.description_hidden:
                placeholder = f'<info:{char_info.text_id}>'
                
                if placeholder in text_with_holes:
                    if char_info.locked:
                        # Replace each character with '_' if it's a letter or a digit. Keep punctuation as is.
                        masked_content = ''.join(['_' if c.isalnum() else c for c in char_info.content])
                        text_with_holes = text_with_holes.replace(placeholder, masked_content)
                    else:
                        # When unlocked, wrap the content in <i> </i> and gui.accent color
                        italic_content = f'{{color=#DBB100}}{{i}}{char_info.content}{{/i}}{{/color}}'
                        text_with_holes = text_with_holes.replace(placeholder, italic_content)
            
            return textwrap.dedent(text_with_holes).split('\n')

        # ---------------
        # Character Unlocking
        # ---------------
        def get_character_progress(self):
            total_info = 0
            total_unlocked = 0
            progress = 0
            for info in self.description_hidden:
                if info.is_important:
                    total_info += 1
                    if not info.locked:
                        total_unlocked += 1
            if total_info == 0:
                return 100
            elif total_unlocked == 0:
                return 0
            else:
                return int(total_unlocked / total_info * 100)

        def is_character_unlocked(self):
            for info in self.description_hidden:
                if info.is_important and info.locked:
                    return False
            return True

        def is_everything_completed(self):
            if self.get_total_unlocked_discoveries() == self.get_total_discoveries():
                return True
            return False

        def get_total_unlocked_discoveries(self):
            total = 0
            for item in self.important_choices:
                if item.discovered:
                    total += 1
            
            for item in self.observations:
                if item.discovered:
                    total += 1

            for item in self.objects:
                if item.discovered:
                    total += 1
            
            return total

        def get_total_discoveries(self):
            return len(self.important_choices.information_list) + len(self.observations.information_list) + len(self.objects.information_list)

        def get_choices_and_discoveries(self):
            return self.important_choices.information_list + self.observations.information_list + self.objects.information_list

        # Put the not discovered at the end for clarity
        def get_choices_and_discoveries_ordered(self):
            discovered = []
            not_discovered = []
            for item in self.get_choices_and_discoveries():
                if item.discovered:
                    discovered.append(item)
                else:
                    not_discovered.append(item)

            return discovered + not_discovered

        def get_choices_and_discoveries_by_chapter(self, chapter, is_current=False):
            # guard against unknown chapter names
            if chapter not in chapter_index:
                # return []
                raise ValueError(f"Unknown chapter `{chapter}`")

            current_idx = chapter_index[chapter]
            choices_and_discoveries = []
            for item in self.get_choices_and_discoveries_ordered():
                # item.chapters is a list of chapter‐keys like ['friday_afternoon', 'saturday_evening', …]
                # we keep the item if *any* of those keys is at or before current_idx
                for chap in item.chapters:
                    chap_idx = chapter_index.get(chap)
                    # skip any unknown chap names in the item
                    if chap_idx is None:
                        continue

                    if chap_idx < current_idx and not (is_current and chapter in item.chapters):
                        choices_and_discoveries.append(item)
                        break  # no need to check the rest of this item's chapters

            return choices_and_discoveries

        def get_choices_and_discoveries_by_chapter_only_current(self, chapter):
            choices_and_discoveries = []
            for item in self.get_choices_and_discoveries_ordered():
                if chapter in item.chapters:
                    choices_and_discoveries.append(item)
            return choices_and_discoveries
        
        def get_chapter_by_name(self, name):
            all_chapters = [chapter for line in self.progress for chapter in line]
            for chapter in all_chapters:
                if chapter.name == name:
                    return chapter
            return None

        def is_chapter_completed(self, chapter):
            for item in self.get_choices_and_discoveries_by_chapter_only_current(chapter):
                if item.discovered == False:
                    return False
            return True

        # ---------------------------------------------------------------------------------------
        #                                Checkpoints
        # ---------------------------------------------------------------------------------------
        def add_checkpoint(self, label_id = ""):
            global current_position, current_run, has_been_restarted, all_menus

            current_position = current_position + 1
            if not has_been_restarted:
                new_checkpoint = Checkpoint(
                    run = current_run,
                    position = current_position,
                    objects = copy.deepcopy(self.objects.get_unlocked()), 
                    observations = copy.deepcopy(self.observations.get_unlocked()),
                    important_choices = copy.deepcopy(self.important_choices.get_unlocked()),
                    label_id = label_id,
                    saved_variables = copy.deepcopy(current_character.saved_variables),
                    all_menus = copy.deepcopy(all_menus),
                )
                self.checkpoints.append(new_checkpoint)
                
            else:
                has_been_restarted = False
        
        def add_ending_checkpoint(self, ending):
            global current_position, current_run, has_been_restarted

            current_position = current_position + 1

            if not has_been_restarted:
                new_checkpoint = Checkpoint(
                    run = current_run,
                    position = current_position,
                    objects = copy.deepcopy(self.objects.get_unlocked()), 
                    observations = copy.deepcopy(self.observations.get_unlocked()),
                    important_choices = copy.deepcopy(self.important_choices.get_unlocked()),
                    label_id = ending.text_id,
                    saved_variables = copy.deepcopy(current_character.saved_variables),
                    ending = ending
                )
                self.checkpoints.append(new_checkpoint)
            else:
                has_been_restarted = False

        def get_checkpoints_by_chapter(self, chapter_label):
            chapter_checkpoints = []
            for checkpoint in self.checkpoints:
                if checkpoint.label_id == chapter_label:
                    chapter_checkpoints.append(checkpoint)

            return chapter_checkpoints

        def get_init_checkpoint(self):
            global current_storyline
            return Checkpoint(
                        run = 1,
                        position = 0,
                        objects = [],
                        observations = [],
                        important_choices = [],
                        label_id = current_storyline.text_id + "_introduction",
                        saved_variables = eval(current_storyline.text_id + "_init_variables")
                    )
            
        def get_max_run(self):
            max_run = 1
            for checkpoint in self.checkpoints:
                if checkpoint.run > max_run:
                    max_run = checkpoint.run

            return max_run

        def __str__(self):
            return 'Name:' + str(self.get_name()) + '; Nb checkpoints:' + str(len(self.checkpoints))
        
        
        def load_test_checkpoints(self) -> None:
            """
            Build every test-checkpoint and tag it with the character-specific label
            found in `self.test_checkpoints[chapter_key]`.

            Example mapping for Lad (attach this dict when you build the character):
                lad_test_checkpoints = {
                    'friday_afternoon':        "lad_introduction",
                    'friday_evening':          "lad_day1_evening",
                    'saturday_morning':        "lad_day2_morning",
                    'saturday_afternoon':      "lad_day2_hunt",
                    'saturday_afternoon_no_hunt': "lad_day2_no_hunt",
                    'saturday_evening':        "lad_day2_evening",
                    'sunday_morning':          "lad_day3_morning",
                    'sunday_afternoon':        "lad_day3_afternoon",
                }
            """
            global current_run
            current_run = 0
            test_run    = 0

            # ------------- helper to gather unlockables for one chapter -------------
            def _collect_unlockables(chap: str) -> List[Tuple[str, str]]:
                u: List[Tuple[str, str]] = []
                for choice in self.important_choices.information_list:
                    if chap in choice.chapters:
                        u.append(("important_choice", choice.text_id))
                for obj in self.objects.information_list:
                    if chap in obj.chapters:
                        u.append(("object", obj.text_id))
                for obs in self.observations.information_list:
                    if chap in obs.chapters:
                        u.append(("observation", obs.text_id))
                return u

            # --------- narrative traversal (keeps declaration order ties) ----------
            chapter_order = sorted(
                chapter_index.items(),
                key=lambda kv: (kv[1], list(chapter_index).index(kv[0]))
            )

            for chap_key, _ in chapter_order:
                toggle_list = _collect_unlockables(chap_key)

                # character-specific Ren’Py label for this chapter
                label_id = self.test_checkpoints.get(chap_key, chap_key)

                # If chapter has no unlockables we still add one checkpoint
                if not toggle_list:
                    self.add_checkpoint(label_id)
                    continue

                # Every Boolean combination of unlockables
                for combo in itertools.product([False, True], repeat=len(toggle_list)):
                    test_run   += 1
                    current_run = test_run
                    self.reset_information()

                    toggles = {}
                    for is_on, (kind, uid) in zip(combo, toggle_list):
                        toggles[uid] = is_on
                        if not is_on:
                            continue
                        if kind == "important_choice":
                            self.important_choices.unlock(uid)
                        elif kind == "object":
                            self.objects.unlock(uid)
                        elif kind == "observation":
                            self.observations.unlock(uid)

                    # evaluate endings
                    triggered = []
                    for ending in self.endings.information_list:
                        cond_fn = endings_conditions.CONDITIONS_DICT.get(
                            getattr(ending, "condition_id", ending.text_id)
                        )
                        if cond_fn and cond_fn(toggles):
                            triggered.append(ending.text_id)

                    if triggered:      # add ending checkpoints
                        for eid in triggered:
                            self.endings.unlock(eid)
                            self.add_ending_checkpoint(self.endings.get_item(eid))
                    else:              # add normal chapter checkpoint
                        self.add_checkpoint(label_id)