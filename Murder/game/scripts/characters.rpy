# Characters description
style narrator_style:
    properties gui.text_properties("dialogue")
    color gui.idle_small_color 
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos - 17

style letter_style:
    properties gui.text_properties("dialogue")
    color gui.idle_small_color
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
    define letter       = Character("Letter", what_style="letter_style")
    define butler       = Character("Butler", image="butler")
    define footman      = Character("Footman", image="footman")
    define maid_name    = "Young woman"
    define maid         = Character(maid_name, image="maid")

    #  image side butler = "images/characters/butler_framed_02.png"

    python:
        # 1. The Lad IN OWN FILE
        
        # 2. The Psychic
        psychic_extra_information = [
            CharacterInformation(0, "background", "A psychic. She can talk to the dead apparently.", is_important = True), 
            CharacterInformation(1, "status", "Wealthy enough to know how many people are needed to run a big house.", is_important = True), 
            CharacterInformation(2, "age", "She was .... SO she must be ????"),
            CharacterInformation(3, "heroic act", "She helped the police to find the kidnapper of a baby.", is_important = True),
            CharacterInformation(4, "lie", "She sometimes/always lie about what she sees ?", is_important = True),
            CharacterInformation(5, "drive", "Doesn't have a driving license.")
        ]
        psychic_details  = CharacterDetails(
            text_id = "psychic", 
            locked = True,
            know_real_name = True,
            real_name = "Amelia Baxter",
            nickname = "The Psychic",
            description_short = "Middle-age Woman",
            description_long = "Middle-aged woman, looking a bit eccentric.",
            information_list = psychic_extra_information
        )
        psychic = Character("psychic_details.get_name()", image="psychic", dynamic=True)

        # 3. The Doctor
        doctor_extra_information = [
            CharacterInformation(0, "background", "He's a doctor and runs an hospital.", is_important = True), 
            CharacterInformation(0, "heroic act", "He has stayed at his charity hospital for 10 years. Which is quite an achievement.", is_important = True), 
            CharacterInformation(1, "status", "Not wealthy.", is_important = True),
            CharacterInformation(2, "age", "He is 39 years old."),
            CharacterInformation(3, "addict", "An opium addict.", is_important = True),
            CharacterInformation(3, "lie", "He stays to run an hospital because he has an easy access to drugs.", is_important = True)
        ]
        doctor_details  = CharacterDetails(
            text_id = "doctor", 
            locked = True,
            know_real_name = True,
            real_name = "Daniel Baldwin",
            nickname = "The Doctor",
            description_short = "Middle-age man",
            description_long = "Serious Middle-age man with glasses.",
            information_list = doctor_extra_information
        )
        doctor = Character("doctor_details.get_name()", image="doctor", dynamic=True)

        # 4. The Drunk
        drunk_extra_information = [
            CharacterInformation(0, "background", ""), 
            CharacterInformation(1, "status", ""),
            CharacterInformation(2, "age", "?"),
            CharacterInformation(3, "addict", "Likes to drink a bit too much.", is_important = True),
        ]
        drunk_details  = CharacterDetails(
            text_id = "drunk", 
            locked = True,
            know_real_name = True,
            real_name = "Samuel Manning",
            nickname = "The Drunk",
            description_short = "Drunk Man",
            description_long = "Old man, looking 'exhausted'.",
            information_list = drunk_extra_information
        )
        drunk = Character("drunk_details.get_name()", image="drunk", dynamic=True)

        # 5. The Host
        host_extra_information = [
            CharacterInformation(0, "todo", "todo", is_important = True), 
            CharacterInformation(1, "down_to_earth", "She's not looking down on \"lower\" class people.", is_important = True), 
        ]
        host_details  = CharacterDetails(
            text_id = "host", 
            locked = True,
            know_real_name = True,
            real_name = "Lady Claythorn",
            nickname = "The Host",
            description_short = "Older Lady",
            description_long = "The lady of the mansion.",
            information_list = host_extra_information
        )
        host = Character("host_details.get_name()", image="host", dynamic=True)
        
        # 6. The Broken Face
        broken_extra_information = [
            CharacterInformation(0, "mask", "A broken face or 'Gueule Cassée'. He wears mask that hides most of hist face because of an injury during the war.")            
        ]
        broken_details  = CharacterDetails(
            text_id = "broken", 
            locked = True,
            know_real_name = True,
            real_name = "Thomas Moody",
            nickname = "The Broken Face",
            description_short = "Masked Man",
            description_long = "A man with a mask on his face.",
            information_list = broken_extra_information
        )
        broken = Character("broken_details.get_name()", image="broken", dynamic=True)

        # 7. The Captain
        captain_extra_information = [
            CharacterInformation(0, "wars", "A veteran of several wars, he fought in Burma, China, and in the Great War."), 
            CharacterInformation(1, "talker", "Likes to tell stories in front of an audience.")
        ]
        captain_details  = CharacterDetails(
            text_id = "captain", 
            locked = True,
            know_real_name = True,
            real_name = "Sushil Sinha",
            nickname = "The Captain",
            description_short = "Older Indian man",
            description_long = "Older man from India.",
            information_list = captain_extra_information
        )
        captain = Character("captain_details.get_name()", image="captain", dynamic=True)
        
        # 8. The Nurse
        nurse_extra_information = [
            CharacterInformation(1, "job", "A nurse.", is_important = True), 
            CharacterInformation(0, "todo", "todo", is_important = True)
        ]
        nurse_details  = CharacterDetails(
            text_id = "nurse", 
            locked = True,
            know_real_name = True,
            real_name = "Rosalind Marsh",
            nickname = "The Nurse",
            description_short = "",
            description_long = "Middle-aged woman.",
            information_list = nurse_extra_information
        )
        nurse = Character("nurse_details.get_name()", image="nurse", dynamic=True)

        # X. Character full List
        # TODO only use the flat one (refacto use chara)
        char_list = [ 
            [ lad_details, doctor_details, host_details, drunk_details ] , 
            [ psychic_details, broken_details, captain_details, nurse_details ] 
        ]

        char_list_flat = [lad_details, doctor_details, host_details, drunk_details, psychic_details, broken_details, captain_details, nurse_details]

    # INIT first character
    $ current_character = lad_details

    return

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
    class CharacterDetails():
        def __init__(
            self, 
            text_id,
            locked = True,
            know_real_name = True,
            real_name = "",
            nickname = "",
            description_short = "",
            description_long = "",
            information_list = [],
        ):
            self.text_id = text_id
            self.locked = locked
            self.know_real_name = False    
            self.real_name = real_name 
            self.nickname = nickname
            self.description_short = description_short
            self.description_long = description_long
            self.information_list = information_list

        def get_name(self):
            # if self.know_real_name:
            return self.real_name
            # else:
            #     return self.description_short
        
        # ---------------
        # KNOWLEDGE
        # ---------------
        def get_knowledge(self):
            knowledge_list = []
            for info in self.information_list:
                if info.type == 'knowledge':
                    knowledge_list.append(info)
            return knowledge_list

        def unlock_knowledge(self, text_id):
            for info in self.get_knowledge():
                if text_id == info.text_id and info.locked:
                    # Unlock the info
                    info.locked = False
                    renpy.notify("You have found information about " + self.get_name())
                    renpy.play("audio/sound_effects/writing_short.ogg", "sound")
                    # play sound "audio/sound_effects/unlock.ogg"

                    if self.all_knowledge_unlocked():
                        # Unlock a character
                        renpy.pause(2)
                        renpy.play("audio/sound_effects/unlock_char.ogg", "sound")
                        renpy.notify("You have unlock a new Character : The " + self.text_id)
            # TODO if first time, add a call to an explanation NOT WORKING, MUST BE PUT INSIDE A LABEL ???
            # global seen_tutorial_unlock_knowledge
            # if not seen_tutorial_unlock_knowledge:
            #     seen_tutorial_unlock_knowledge = True
            #     renpy.call('tutorial_unlock_knowledge')
        
        def is_knowledge_unlocked(self, text_id):
            for info in self.get_knowledge():
                if text_id == info.text_id:
                    return not info.locked
            return False

        def all_knowledge_unlocked(self):
            for info in self.get_knowledge():
                if info.locked:
                    return False
            return True

        def get_character_progress(self):
            total_info = 0
            total_unlocked = 0
            progress = 0
            for info in self.get_knowledge():
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
            for info in self.get_knowledge():
                if info.is_important and info.locked:
                    return False
            return True

        # ---------------
        # Observation
        # ---------------
        def get_observations(self):
            observation_list = []
            for info in self.information_list:
                if info.type == 'observation':
                    observation_list.append(info)
            return observation_list

        def unlock_observation(self, text_id):
            for info in self.get_observations():
                if text_id == info.text_id and info.locked:
                    # Unlock the info
                    info.locked = False
                    renpy.notify("You have made a new observation")
                    renpy.play("audio/sound_effects/writing_short.ogg", "sound")
        
        def is_observation_unlocked(self, text_id):
            for info in self.get_observations():
                if text_id == info.text_id:
                    return not info.locked
            return False
        
        # ---------------
        # Intuition
        # ---------------
        def get_intuitions(self):
            intuition_list = []
            for info in self.information_list:
                if info.type == 'intuition':
                    intuition_list.append(info)
            return intuition_list

        def unlock_intuition(self, text_id):
            for info in self.get_intuitions():
                if text_id == info.text_id and info.locked:
                    # Unlock the info
                    info.locked = False
                    renpy.notify("You have a new intuition")
                    renpy.play("audio/sound_effects/writing_short.ogg", "sound")
        
        def is_intuition_unlocked(self, text_id):
            for info in self.get_intuitions():
                if text_id == info.text_id:
                    return not info.locked
            return False

        # ---------------
        # object
        # ---------------
        def get_objects(self):
            object_list = []
            for info in self.information_list:
                if info.type == 'object':
                    object_list.append(info)
            return object_list

        def unlock_object(self, text_id):
            for info in self.get_objects():
                if text_id == info.text_id and info.locked:
                    # Unlock the info
                    info.locked = False
                    renpy.notify("You have found a new object")
                    renpy.play("audio/sound_effects/writing_short.ogg", "sound")
        
        def is_object_unlocked(self, text_id):
            for info in self.get_objects():
                if text_id == info.text_id:
                    return not info.locked

    class CharacterInformation:
        def __init__(
            self, 
            order,
            text_id,             
            content, 
            locked = True,
            is_important = False,
            type = 'knowledge'
        ):
            self.order = order
            self.text_id = text_id
            self.content = content
            self.locked = locked
            self.is_important = is_important
            self.type = type

# LABELS
label character_selection:
    scene black_background
    narrator "Select Your Character"

    $ selected_choice = renpy.call_screen('character_selection') 
    if selected_choice == 'lad':
        jump lad_introduction
    else:
        jump lad_day1_evening

# SCREENS
screen characters:
    tag menu
    use game_menu(_("Characters")):
        fixed:
            xalign 0.5
            yoffset 120
            xoffset -100

            use character_list

screen character_selection:
    modal True
    zorder 200

    # Copy of the confirm style (TODO change later properly to a map style)
    style_prefix "confirm"
    
    frame:
        xalign .5
        yalign .5
        margin (310,110,310,150)
        label "Select your Character":
            yoffset -50
            style "confirm_prompt" # TODO specific styling TODO space after label .... why so complicated.....
            xalign 0.5
        use character_list(True)

screen character_list(is_selection = False):
    #Two hbox of 4 characters
    $ char_x_offset = 0
    $ char_y_offset = 0

    for char_sub_list in char_list:
        hbox:
            yoffset char_y_offset
            for char in char_sub_list:
                vbox:
                    xoffset char_x_offset
                    textbutton char.real_name:
                        if is_selection:
                            if char.is_character_unlocked():
                                action Return(char.text_id)
                        else:
                            action ShowMenu("character_details", char)
                    imagebutton:
                        if char.is_character_unlocked():
                            idle "images/characters/side/side " + char.text_id + ".png"
                            hover "images/characters/side_hover/side " + char.text_id + " hover.png"
                        else:
                            idle "images/characters/side_bw/side " + char.text_id + " bw.png"
                            if not is_selection:
                                hover "images/characters/side_bw_hover/side " + char.text_id + " bw hover.png"

                        if is_selection:
                            if char.is_character_unlocked():
                                action Return(char.text_id)   
                        else:
                            action ShowMenu("character_details", char)
                
                $ char_x_offset += 50

        $ char_x_offset = 0

        if is_selection:
            $ char_y_offset += 340
        else:
            $ char_y_offset += 340

screen character_details(selected_char):
    # $ selected_char = get_char(char_id)
    tag menu # ????
    use game_menu(_("Characters"), scroll="viewport"):

        #style_prefix "characters" #???

        hbox:
            vbox:
                text selected_char.real_name:
                    size 48
                    font gui.name_text_font
                    line_leading 10
                    line_spacing 10
                    color gui.accent_color
                    # outlines [ (absolute(1), "#140303", absolute(0), absolute(0)) ]
                
                if selected_char.is_character_unlocked():
                    add "images/characters/side/side " + selected_char.text_id +".png"
                    text "Unlocked":
                        size 36
                        xalign 0.5
                else:
                    add "images/characters/side_bw/side " + selected_char.text_id +" bw.png"
                    text "Locked":
                        # yoffset -25 inside
                        size 36
                        xalign 0.5
                    bar:
                        value selected_char.get_character_progress() 
                        range 100
                        xmaximum 260
                        style 'progress_bar'

                
            vbox:
                xoffset 40 
                textbutton _("Return"): 
                    xalign 1.0 
                    yalign 0.0
                    xpos 1000
                    action ShowMenu("characters") 
                
                # hbox:                    
                #     yalign 0.5
                #     text "Name:  ":
                #         color gui.accent_color
                #     text selected_char.real_name 

                text "Description: " color gui.accent_color
                text selected_char.description_long
                
                for info in selected_char.information_list:
                    if not info.locked:
                        text info.content
        
                # textbutton _("Return"): 
                #     xalign 1.0 
                #     yalign 0.0
                #     xpos 1000
                #     action ShowMenu("characters") 
        
        # TODO show bottom right

