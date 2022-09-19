# Characters description
label init_characters:
    python:
        # 1. The hero
        hero_extra_information = [
            CharacterInformation(0, "background", "Born in Derbshire, he comes from an orphanage.") , 
            CharacterInformation(1, "job", "He is fishmonger")
        ]

        hero_details  = CharacterDetails(
            text_id = "hero", 
            locked = False,
            know_real_name = False,
            real_name = "Ted Harring",
            description_short = "Young Lad",
            description_long = "Good Looking lad, in his early twenties.",
            information_list = hero_extra_information
            )
        hero  = Character("hero_details.get_name()", image="hero", dynamic=True, what_style="hero_style")

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

# Selection
label character_selection:
    scene black_background
    narrator "Select Your Character"

    $ selected_choice = renpy.call_screen('character_selection') 
    if selected_choice == 'lad':
            jump hero_introduction
    else:
            jump hero_day1_evening