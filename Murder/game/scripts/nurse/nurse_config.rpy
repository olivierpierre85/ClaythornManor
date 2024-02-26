label init_nurse:

    # call nurse_config_map
    
    # call nurse_config_menu

    python:
        # Story Variables
        nurse_init_variables = {
            # MAP Menus
            # "day1_evening_map_menu" : nurse_day1_evening_map_menu,
            # "day2_no_hunt_map_menu" : nurse_day2_no_hunt_map_menu,

            # "lad_generic_menu" : lad_generic_menu_psychic,
            # "lad_generic_other_guests_menu" : lad_generic_other_guests_menu_psychic,

            # "captain_generic_menu" : captain_generic_menu_psychic,
            # "captain_generic_other_guests_menu" : captain_generic_other_guests_menu_psychic,

            # "doctor_generic_menu" : doctor_generic_menu_psychic,
            # "doctor_generic_other_guests_menu": doctor_generic_other_guests_menu_psychic,

            # "nurse_generic_menu" : nurse_generic_menu_psychic,
            # "nurse_generic_other_guests_menu" : nurse_generic_other_guests_menu_psychic,
            
            # story var
        }

        nurse_extra_information = [
            CharacterInformation(1, "job", "A nurse.", is_important = True), 
            CharacterInformation(2, "clothes", "Discreet but well dressed.", is_important = True),
            CharacterInformation(3, "age", "42 years old", is_important = True),
            CharacterInformation(4, "manor", "Is familiar with grand mansions", is_important = True),
            CharacterInformation(0, "todo", "todo", is_important = True),
            CharacterInformation(60, "???", "???", is_important = True),
        ]
        nurse_important_choices = CharacterInformationList([])
        nurse_endings = CharacterInformationList([])

        nurse_observations = CharacterInformationList ([],
            notification_text = "You have made a new observation",
            notification_sound = "audio/sound_effects/writing_short.ogg"
        )  

        nurse_details  = CharacterDetails(
            text_id = "nurse", 
            locked = True,
            know_real_name = True,
            real_name = "Rosalind Marsh",
            nickname = "The Nurse",
            description_short = "",
            description_long = "Middle-aged woman.",
            information_list = nurse_extra_information,
            important_choices = CharacterInformationList([]),
            endings = CharacterInformationList([]),
            intuitions = CharacterInformationList([]),
            observations = CharacterInformationList([]),
            objects = CharacterInformationList([]),
        )
        nurse = Character("nurse_details.get_name()", image="nurse", dynamic=True)

    return