# Characters description
label init_characters:
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
            description_short = "Young Lad",
            description_long = "Good Looking lad, in his early twenties.",
            information_list = lad_extra_information
            )
        lad  = Character("lad_details.get_name()", image="lad", dynamic=True, what_style="lad_style")

        # 2. The Psychic
        psychic_extra_information = [
            CharacterInformation(0, "background", "Born in Candy City") , 
            CharacterInformation(1, "job", "A psychic, and a famous one apparently")
        ]
        psychic_details  = CharacterDetails(
            text_id = "psychic", 
            locked = True,
            know_real_name = False,
            real_name = "Amalia Baxter",
            description_short = "Middle-age Woman",
            description_long = "Old lady",
            information_list = psychic_extra_information
        )
        psychic    = Character("psychic_details.get_name()", image="psychic", dynamic=True)

        # 3. The Doctor

        char_list = [ 
            [ lad_details ] , 
            [ psychic_details ] 
        ]
        #     [("The Lad", "lad"), ("The Psychic", "psychic"), ("The Captain", "captain"), ("The Broken Face", "broken")],
        #     [("The Doctor", "doctor"), ("The Drunk", "drunk"), ("The Host", "host"), ("The Nurse", "nurse")]
        # ]


        def get_char(text_id):
            if text_id == "lad":
                return lad_details
            elif text_id == "psychic":
                return psychic_details
            else:
                return False



    return

init -100 python:
# Python Classes
    class CharacterDetails():
        def __init__(
            self, 
            text_id,
            locked = True,
            know_real_name = False,
            real_name = "",
            description_short = "",
            description_long = "",
            information_list = []
        ):
            self.text_id = text_id
            self.locked = locked
            self.know_real_name = False    
            self.real_name = real_name 
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
                    textbutton char.get_name():
                        if is_selection:
                            action Return(char.text_id)
                        else:
                            action ShowMenu("character_detail", char.text_id)
                    imagebutton:
                        idle "images/characters/" + char.text_id +".png"
                        if is_selection:
                            action Return(char.text_id)
                        else:
                            action ShowMenu("character_detail", char.text_id)
                $ char_x_offset += 50

        $ char_x_offset = 0

        if is_selection:
            $ char_y_offset += 340
        else:
            $ char_y_offset += 340

screen character_detail(selected_char):
    $ current_char = get_char(selected_char)
    tag menu # ????
    use game_menu(_("Characters"), scroll="viewport"):

        style_prefix "characters" #???

        vbox:
            text current_char.get_name()
            add "images/characters/" + selected_char +".png"
        
        # TODO show bottom right
        textbutton _("Return") action ShowMenu("characters") xalign 0.95 yalign 0.93