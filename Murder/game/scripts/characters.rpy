# Characters description
style narrator_style:
    properties gui.text_properties("dialogue")
    color gui.idle_small_color 
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos - 17

label init_characters:
    # Inside voice style
    define narrator = Character(None, what_style="narrator_style")

    # Non Playable Characters
    define butler   = Character("The Butler", image="butler")
    image side butler = "images/characters/butler_framed_02.png"

    python:
        # 1. The Lad
        lad_extra_information = [
            CharacterInformation(0, "background", "Born in Derbshire, he comes from an orphanage.") , 
            CharacterInformation(1, "job", "He is fishmonger")
        ]
        lad_details  = CharacterDetails(
            text_id = "lad", 
            locked = False,
            know_real_name = False,
            real_name = "Ted Harring",
            nickname = "The Lad",
            description_short = "Young Lad",
            description_long = "Good Looking lad, in his early twenties.",
            information_list = lad_extra_information
            )
        lad = Character("lad_details.get_name()", image="lad", dynamic=True)

        lad_day1_drinks = 0

        # 2. The Psychic
        psychic_extra_information = [
            CharacterInformation(0, "background", "Born in Candy City.") , 
            CharacterInformation(1, "job", "A psychic, and a famous one apparently.")
        ]
        psychic_details  = CharacterDetails(
            text_id = "psychic", 
            locked = True,
            know_real_name = False,
            real_name = "Amalia Baxter",
            nickname = "The Psychic",
            description_short = "Middle-age Woman",
            description_long = "Old lady",
            information_list = psychic_extra_information
        )
        psychic = Character("psychic_details.get_name()", image="psychic", dynamic=True)

        # 3. The Drunk
        drunk_extra_information = [
        ]
        drunk_details  = CharacterDetails(
            text_id = "drunk", 
            locked = True,
            know_real_name = False,
            real_name = "TODO",
            nickname = "The Drunk",
            description_short = "Drunk Man",
            description_long = "Drunk Man, not so good looking",
            information_list = drunk_extra_information
        )
        drunk = Character("drunk_details.get_name()", image="drunk", dynamic=True)
        
        # 4. The Doctor
        doctor_extra_information = [
        ]
        doctor_details  = CharacterDetails(
            text_id = "doctor", 
            locked = True,
            know_real_name = False,
            real_name = "",
            nickname = "The Doctor",
            description_short = "Middle-age Woman",
            description_long = "Old lady",
            information_list = doctor_extra_information
        )
        doctor = Character("doctor_details.get_name()", image="doctor", dynamic=True)

        # 5. The Host
        host_extra_information = [
        ]
        host_details  = CharacterDetails(
            text_id = "host", 
            locked = True,
            know_real_name = False,
            real_name = "TODO",
            nickname = "The Host",
            description_short = "Middle-age Woman",
            description_long = "Old Rich lady",
            information_list = host_extra_information
        )
        host = Character("host_details.get_name()", image="host", dynamic=True)
        
        # 6. The Broken Face
        broken_extra_information = [
        ]
        broken_details  = CharacterDetails(
            text_id = "broken", 
            locked = True,
            know_real_name = False,
            real_name = "",
            nickname = "The Broken Face",
            description_short = "Middle-age Woman",
            description_long = "Old lady",
            information_list = broken_extra_information
        )
        broken = Character("broken_details.get_name()", image="broken", dynamic=True)

        # 7. The Captain
        captain_extra_information = [
        ]
        captain_details  = CharacterDetails(
            text_id = "captain", 
            locked = True,
            know_real_name = False,
            real_name = "",
            nickname = "The captain Face",
            description_short = "",
            description_long = "",
            information_list = captain_extra_information
        )
        captain = Character("captain_details.get_name()", image="captain", dynamic=True)
        
        # 8. The Nurse
        nurse_extra_information = [
        ]
        nurse_details  = CharacterDetails(
            text_id = "nurse", 
            locked = True,
            know_real_name = False,
            real_name = "",
            nickname = "The Nurse ",
            description_short = "",
            description_long = "",
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

    # TODO add all side image
    # image side lad = "images/characters/lad.png"
    # image side broken = "images/characters/borken.png"

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
            know_real_name = False,
            real_name = "",
            nickname = "",
            description_short = "",
            description_long = "",
            information_list = []
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
            if self.know_real_name:
                return self.real_name
            else:
                return self.description_short
        
        def introduce(self):
            self.know_real_name = True
        
        def check_characters_knowledge(self, text_id):
            for info in self.information_list:
                if text_id == info.text_id and info.locked:
                    # Unlock the info
                    info.locked = False
                    renpy.notify("You have found the " + text_id + " of " + self.get_name())
                    renpy.play("audio/sound_effects/writing_short.ogg", "sound")
                    # play sound "audio/sound_effects/unlock.ogg"

                    if self.all_information_unlocked():
                        # Unlock a character
                        renpy.pause(2)
                        renpy.play("audio/sound_effects/unlock_char.ogg", "sound")
                        renpy.notify("You have unlock a new Character : The " + self.text_id)
        
        def all_information_unlocked(self):
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
            locked = True
        ):
            self.order = order
            self.text_id = text_id
            self.content = content
            self.locked = locked

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
        label "Select your character":
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
                    textbutton char.nickname:
                        if is_selection:
                            action Return(char.text_id)
                        else:
                            action ShowMenu("character_details", char.text_id)
                    imagebutton:
                        idle "images/characters/" + char.text_id +".png"
                        if is_selection:
                            action Return(char.text_id)
                        else:
                            action ShowMenu("character_details", char.text_id)
                $ char_x_offset += 50

        $ char_x_offset = 0

        if is_selection:
            $ char_y_offset += 340
        else:
            $ char_y_offset += 340

screen character_details(selected_char):
    $ current_char = get_char(selected_char)
    tag menu # ????
    use game_menu(_("Characters"), scroll="viewport"):

        style_prefix "characters" #???

        hbox:
            vbox:
                text current_char.nickname:
                    size 48
                    font gui.name_text_font
                    line_leading 10
                    line_spacing 10
                    color gui.accent_color
                    # outlines [ (absolute(1), "#140303", absolute(0), absolute(0)) ]
                add "images/characters/" + selected_char +".png"
            vbox:
                xoffset 40 
                textbutton _("Return"): 
                    xalign 1.0 
                    yalign 0.0
                    xpos 1000
                    action ShowMenu("characters") 
                
                hbox:
                    
                    yalign 0.5
                    text "Name:  ":
                        color gui.accent_color
                    if current_char.know_real_name:
                        text current_char.real_name 
                    else:
                        text "Unknow" 

                text "Description: " color gui.accent_color
                text current_char.description_long
                for info in current_char.information_list:
                    if not info.locked:
                        text info.content
        
                textbutton _("Return"): 
                    xalign 1.0 
                    yalign 0.0
                    xpos 1000
                    action ShowMenu("characters") 
        
        # TODO show bottom right

