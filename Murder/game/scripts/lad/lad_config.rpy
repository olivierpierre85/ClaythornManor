label init_lad:
    call change_time(17,00, 'Evening', 'Friday')

    call lad_config_map
    
    call lad_config_menu

    python:
        # Story Variables
        lad_saved_variables = {
            "map_menu" : lad_map_menu,

            "psychic_generic_menu" : psychic_generic_menu_lad,
            "psychic_generic_other_guests_menu": psychic_generic_other_guests_menu_lad,

            "doctor_generic_menu" : doctor_generic_menu_lad,
            "doctor_generic_other_guests_menu": doctor_generic_other_guests_menu_lad,

            "library_visited" : False,
            "has_met_maid" : False,
            "psychic_generic_other_guests_saturday_morning_ask" : False,

            "day1_evening_billiard_room_visited" : False,
            "day1_drinks" : 0,
            "day1_poisoned" : False,
            "day1_drunk" : False, # Means he drank poison, but rejected it (used again on day 2 evening with the captain)
            
            "day2_breakfast_follow" : False,
            "day2_hunt" : False,
            "day2_saw_accident" : False,
            "day2_evening_billiard_room_visited" : False,
            "day2_nohunt_has_visited_tea_room" : False,
            "day2_believe_psychic" : False,
            "day2_drinks" : 0,
            "day2_drunk" : False,
            "day2_evening_billiard_room_captain_talked" : False,
            "day2_evening_taste_from_flask" : False,
            "day2_poisoned" : False,

            "day3_morning_captain_found" : False,
            "day3_ending" : "",
            "day3_seen_car" : False,
        }

        # Character Class
        lad_extra_information = [
            # knowledge
            CharacterInformation(0, "background", "Born and raised in London.") , 
            CharacterInformation(2, "age", "He was 15 at the end of the war. That would make him 22 years old today."),
            CharacterInformation(3, "education", "Not a great reader."),
            CharacterInformation(4, "poor_drinker", "Can't hold his liqueur."),
            CharacterInformation(5, "drive", "He never learned how to drive."),
            CharacterInformation(6, "cook", "He is not much of a cook."),
            # Observations
            CharacterInformation(1, "green_liquid", "There was a green liquid next to Thomas Moody death bed.", type="observation", image_file="poison"), 
            # Objects
            CharacterInformation(1, "gun", "A empty handgun found in the gun room", type="object", image_file="gun"), 
            # Intuitions
            CharacterInformation(1, "psychic_poisons", "Sunday, your lunch was poisoned.", type="intuition", image_file="gun"), 
            # Endings
            CharacterInformation(1, "gunned_down", "You die stoned to death", type="ending", image_file="gun"), 
        ]

        lad_details  = CharacterDetails(
            text_id = "lad", 
            locked = False,
            know_real_name = True,
            real_name = "Ted Harring",
            nickname = "The Lad",
            description_short = "Young man",
            description_long = "Good Looking lad, in his early twenties.",
            information_list = lad_extra_information,
            saved_variables = lad_saved_variables
        )
        lad = Character("lad_details.get_name()", image="lad", dynamic=True)

    return