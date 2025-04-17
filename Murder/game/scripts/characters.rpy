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


    class CharacterEndingList(CharacterInformationList):
        def __init__(self, ending_list):
            super().__init__(
                ending_list,
            )


    class CharacterIntuitionList(CharacterInformationList):
        def __init__(self, intuition_list):
            super().__init__(
                intuition_list,
                notification_text = "You have a new intuition",
                notification_sound = "audio/sound_effects/writing_short.ogg"
            )
        
        def unlock(self, text_id):
            global seen_tutorial_intuition
            for info in self.information_list:
                if text_id == info.text_id and info.locked:
                    info.locked = False
                    info.discovered = True

                    if not hide_notifications:
                        renpy.notify(self.notification_text)
                        renpy.play(self.notification_sound, "sound")

            if not seen_tutorial_intuition:
                seen_tutorial_intuition = True
                renpy.call('tutorial_intuition')


    class CharacterObservationList(CharacterInformationList):
        def __init__(self, observation_list):
            super().__init__(
                observation_list,
                notification_text = "You have made a new observation",
                notification_sound = "audio/sound_effects/writing_short.ogg"
            )


    class CharacterObjectList(CharacterInformationList):
        def __init__(self, object_list):
            super().__init__(
                object_list,
                notification_text="You have found a new object",
                notification_sound="audio/sound_effects/writing_short.ogg",
            )


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
            locked = True,
            is_important = False,
            image_file = None
        ):
            self.order = order
            self.text_id = text_id
            self.content = content
            self.locked = locked
            self.is_important = is_important
            self.image_file = image_file
            self.discovered = False


    class CharacterDetails():
        def __init__(
            self, 
            text_id,
            description_hidden,
            important_choices,
            endings,      
            intuitions,
            objects,
            observations, 
            progress,
            saved_variables = dict(),
            test_checkpoints = [],
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
            self.intuitions = intuitions or []
            self.objects = objects or []
            self.observations = observations or [] 
            self.progress = progress or [] 
            self.saved_variables = saved_variables or dict()
            self.checkpoints = []
            self.test_checkpoints = test_checkpoints or []
            

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

        def load_test_checkpoints(self):
            global current_run

            test_run = 0

            for (chapter_label, toggle_list, possible_endings) in self.test_checkpoints:

                # Generate all boolean combinations
                for combination in itertools.product([False, True], repeat=len(toggle_list)):
                    test_run += 1
                    current_run = test_run

                    # Reset or start fresh for each new "run"
                    self.reset_information()

                    # Build a dictionary of toggles => bool
                    toggles_dict = {}
                    for i, is_unlocked in enumerate(combination):
                        unlock_type, unlock_id = toggle_list[i]
                        toggles_dict[unlock_id] = is_unlocked

                        # Actually unlock them in your data structures if True
                        if is_unlocked:
                            if unlock_type == "object":
                                self.objects.unlock(unlock_id)
                            elif unlock_type == "important_choice":
                                self.important_choices.unlock(unlock_id)
                            elif unlock_type == "observation":
                                self.observations.unlock(unlock_id)
                            # etc.

                    # Now check if any ending condition(s) apply
                    triggered_endings = []
                    for ending_info in possible_endings:
                        condition_func = endings_conditions.CONDITIONS_DICT[ending_info['condition_id']]
                        if condition_func(toggles_dict):
                            triggered_endings.append(ending_info['label'])

                    # If one or more endings are triggered, skip normal checkpoint
                    # and add an ending checkpoint for each triggered ending.
                    if triggered_endings:
                        for ending_label in triggered_endings:
                            self.endings.unlock(ending_label)
                            ending_data = self.endings.get_item(ending_label)
                            self.add_ending_checkpoint(ending_data)
                    else:
                        # No ending triggered => add a normal checkpoint
                        self.add_checkpoint(chapter_label)


            return