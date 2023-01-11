label init_lad:
    call change_time(17,00, 'Evening', 'Friday')

    call lad_config_map
    
    call lad_config_menu

    python:
        # Story Variables
        lad_saved_variables = {
            "map_menu" : lad_map_menu,
            "psychic_generic_menu" : psychic_generic_menu_lad,
            # "doctor_generic_menu" : doctor_generic_menu
            "library_visited" : False
        }

        lad_has_met_maid = False
        psychic_generic_other_guests_saturday_morning_ask = False

        lad_day1_evening_billiard_room_visited = False
        lad_day1_drinks = 0
        lad_day1_poisoned = False
        lad_day1_drunk = False # Means he drank poison, but rejected it (used again on day 2 evening with the captain)

        lad_day2_breakfast_follow = False
        lad_day2_hunt = False
        lad_day2_saw_accident = False
        lad_day2_evening_billiard_room_visited = False
        lad_day2_nohunt_has_visited_tea_room = False
        lad_day2_believe_psychic = False
        lad_day2_drinks = 0
        lad_day2_drunk = False
        lad_day2_evening_billiard_room_captain_talked = False
        lad_day2_evening_taste_from_flask = False
        lad_day2_poisoned = False

        lad_day3_morning_captain_found = False
        lad_day3_ending = ""
        lad_day3_seen_car = False

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