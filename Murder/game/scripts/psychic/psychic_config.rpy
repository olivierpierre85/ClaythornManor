label init_psychic:

    # call psychic_config_map
    
    call psychic_config_menu

    python:
        # Story Variables
        psychic_init_variables = {
            # "map_menu" : psychic_map_menu,
            "lad_generic_menu" : lad_generic_menu_psychic,
            "captain_generic_menu" : captain_generic_menu_psychic
        }

        psychic_extra_information = [
            CharacterInformation(0, "background", "A psychic. She can talk to the dead apparently.", is_important = True), 
            CharacterInformation(1, "status", "Wealthy enough to know how many people are needed to run a big house.", is_important = True), 
            CharacterInformation(2, "age", "She was .... SO she must be ????"),
            CharacterInformation(3, "heroic act", "She helped the police to find the kidnapper of a baby.", is_important = True),
            CharacterInformation(4, "lie", "She is a fraud. All she said about talking with spirit was a lie.", is_important = True),
            CharacterInformation(5, "drive", "Doesn't have a driving license."),
            CharacterInformation(6, "racist", "She believes only white people come from England.")
        ]
        psychic_details  = CharacterDetails(
            text_id = "psychic", 
            locked = True,
            know_real_name = True,
            real_name = "Amelia Baxter",
            nickname = "The Psychic",
            description_short = "Middle-age Woman",
            description_long = "Middle-aged woman, looking a bit eccentric.",
            information_list = psychic_extra_information,
            saved_variables = psychic_init_variables
        )
        psychic = Character("psychic_details.get_name()", image="psychic", dynamic=True)

    return