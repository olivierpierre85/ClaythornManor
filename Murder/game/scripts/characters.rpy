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
        # psychic_extra_information = [
        #     CharacterInformation(0, "background", "Born in Candy City") , 
        #     CharacterInformation(1, "job", "A psychic, and a famous one apparently")
    # ]
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
        
        def unlock_information(self, text_id):
            pass #TODO


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


# Selection
label character_selection:
    scene black_background
    narrator "Select Your Character"

    $ selected_choice = renpy.call_screen('character_selection') 
    if selected_choice == 'lad':
            jump hero_introduction
    else:
            jump hero_day1_evening