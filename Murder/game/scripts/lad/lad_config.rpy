label init_lad:
    
    call lad_config_map
    
    call lad_config_menu

    python:
        # Story Variables
        lad_init_variables = {
            # MAP Menus
            "day1_evening_map_menu" : lad_day1_evening_map_menu,
            "day2_no_hunt_map_menu" : lad_day2_no_hunt_map_menu,
            "day2_evening_map_menu": lad_day2_evening_map_menu,
            "day3_morning_map_menu" : lad_day3_morning_map_menu,

            "psychic_generic_menu" : psychic_generic_menu_lad,
            "psychic_generic_other_guests_menu": psychic_generic_other_guests_menu_lad,
            "knows_psychic_background": False,
            "knows_bedroom_psychic": False,
            
            "doctor_generic_menu" : doctor_generic_menu_lad,
            "doctor_generic_other_guests_menu": doctor_generic_other_guests_menu_lad,

            "knows_doctor_background": False,
            "knows_doctor_addict": False,

            "library_visited" : False,
            "portrait_gallery_visited": False,
            "attic_visited" : False,
            "has_met_maid" : False,
            "psychic_generic_other_guests_saturday_morning_ask" : False,
            "has_try_sneaking_downstairs" : 0,

            "day1_evening_billiard_room_visited" : False,
            "day1_drinks" : 0,
            "day1_poisoned" : False,
            "day1_drunk" : False, # Means he drank poison, but rejected it (used again on day 2 evening with the captain)
            
            "day2_breakfast_follow" : False,
            "day2_hunt" : False,
            "day2_saw_accident" : False,
            "day2_evening_billiard_room_visited" : False,
            "day2_nohunt_has_visited_tea_room" : False,
            "day2_nohunt_bedroom_tries" : 0,
            "day2_believe_psychic" : False,

            "day2_drinks" : 0,
            "day2_drunk" : False,
            "day2_evening_billiard_room_captain_talked" : False,
            "day2_evening_taste_from_flask" : False,
            "day2_poisoned" : False,

            "day3_morning_captain_found" : False,
            "day3_ending" : "",
            "day3_seen_car" : False,
            "day3_downstairs_visited" : False
        }

        # Character Class
        lad_important_choices = CharacterImportantChoiceList ([
            CharacterInformation(0, "hunt", "You decided to go hunting", image_file="gun")
        ])

        lad_endings = CharacterEndingList ([
            CharacterInformation(1, "gunned_down", "You die stoned to death", image_file="gun_downed"), 
            CharacterInformation(2, "poisoned", "You were poisoned", image_file="poisoned"), 
            CharacterInformation(3, "fell", "You fell on a picked fence", image_file="poisoned"), 
        ])

        lad_intuitions = CharacterIntuitionList ([            
                CharacterInformation(1, "psychic_poisons", "Sunday, your lunch was poisoned.", image_file="gun")
            ]
        )

        lad_observations = CharacterObservationList ([    
                CharacterInformation(1, "green_liquid", "There was a green liquid next to Thomas Moody death bed.", image_file="poison") 
            ]
        )  

        lad_objects = CharacterObjectList([  
                CharacterInformation(1, "gun", "A empty handgun found in the gun room", image_file="gun"),
                CharacterInformation(2, "burned_letter", "A burned letter found in Samuel Manning's room", image_file="burned_letter")
            ],
        )

        lad_description_hidden = CharacterDescriptionHiddenList ([
            CharacterInformation(0, "age", "22 years old - which means he was merely 15"),
            CharacterInformation(0, "origin", "Birmingham"), 
            CharacterInformation(0, "poor", "a wealthy family, nor even a decent one"),
            CharacterInformation(0, "childhood", "he doesn't have a family at all; he was raised in an orphanage"),# LAST ONE!!!!!
            CharacterInformation(0, "education", "the best education, and, like a large number of individuals from similar backgrounds, he can barely read"),
            CharacterInformation(0, "job", "on the 'informal sector' for employment"), 
            CharacterInformation(0, "thief", "sometimes means being on the wrong side of the law"), 
            CharacterInformation(0, "heroic_act", "saving a infant from a burning building. This act of heroism made him the subject of a newspaper article"), 
            CharacterInformation(0, "poor_drinker", "drinker"),
            CharacterInformation(0, "drive", "drive a car"),
            CharacterInformation(0, "cook", "cook a meal"),
            ], "Ted Harring"
        )
        # Keep for easy Reading
        # lad_description_full_complete = """
        # A good-looking young lad, he is only "22 years old - which means he was merely 15" at the end of the war.
        # Born and raised in "Birmingham", we can't say he comes from "a wealthy family, nor even a decent one". In fact, "he doesn't have a family at all; he was raised in an orphanage".
        # His childhood didn't offer him "the best education, and, like a large number of individuals from similar backgrounds, he can barely read".
        # That is also why he had to rely "on the 'informal sector' for employment", and as everyone knows, this "sometimes means ending up on the wrong side of the law".
        # One day, he found himself in the right place at the right moment and, against all odds, did the right thing by "saving a infant from a burning building. This act of heroism made him the subject of a newspaper article", which was enough for Lady Claythorn to invite him to her manor.
        # Not a great "drinker", he is also not able to "drive a car" or "cook a meal".
        # """

        lad_description_full = """
        A good-looking young lad, he is only <info:age> at the end of the war.
        Born and raised in <info:origin>, we can't say he comes from <info:poor>. In fact, <info:childhood>.
        His childhood didn't offer him <info:education>.
        That is also why he had to rely <info:job>, and as everyone knows, this <info:thief>.
        One day, he found himself in the right place at the right moment and, against all odds, did the right thing by <info:heroic_act>, which was enough for Lady Claythorn to invite him to her manor.
        Not a great <info:poor_drinker>, he is also not able to <info:drive> or <info:cook>.
        """

        lad_progress = [
            # First Line
            [
                Chapter(image_checkpoint_start), 
                Chapter(image_checkpoint_right, "lad_day1_evening", "Evening"),
                Chapter(image_checkpoint_right, "lad_day2_morning", "Morning"),
                Chapter(image_checkpoint_right, "lad_day2_hunt", "The Hunt"),
                Chapter(image_checkpoint_right, "lad_day2_afternoon", "Afternoon"),
                Chapter(image_checkpoint_right, "lad_day2_evening", "Evening"),
                Chapter(image_checkpoint_right, "lad_day3_morning", "Morning"),
                Chapter(image_checkpoint_right, "lad_day3_afternoon", "Afternoon"),
                Chapter(image_ending_question),
            ],
            # Second line, ...
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_corner),
                Chapter(image_checkpoint_right, "lad_day2_no_hunt", "No Hunt"),
                Chapter(image_checkpoint_corner_merge),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question),
            ],
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question), # TODO Ending 
                Chapter(image_checkpoint_empty_filler), # Empty filler after ending
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question),
            ],
                        [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question),
            ],
        ]

        lad_details  = CharacterDetails(
            text_id = "lad", 
            locked = False,
            know_real_name = True,
            real_name = "Ted Harring",
            nickname = "The Lad",
            description_short = "Young man",
            description_long = lad_description_full,
            description_hidden = lad_description_hidden,
            important_choices = lad_important_choices,
            endings = lad_endings,
            intuitions = lad_intuitions,
            observations = lad_observations,
            objects = lad_objects,
            progress = lad_progress,
            saved_variables = copy.deepcopy(lad_init_variables), # copy so the init variables can be use again.
        )
        lad = Character("lad_details.get_name()", image="lad", dynamic=True)

    return