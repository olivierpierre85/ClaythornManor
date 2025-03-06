label init_lad:
    
    call lad_config_map
    
    call lad_config_menu

    call lad_config_progress

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

            "day1_evening_billiard_room_visited" : False,
            "day1_drinks" : 0,
            
            "day2_breakfast_follow" : False,
            "day2_hunt" : False,
            "day2_evening_billiard_room_visited" : False,
            "day2_nohunt_has_visited_tea_room" : False,
            "day2_nohunt_bedroom_tries" : 0,

            "day2_drinks" : 0,
            "day2_evening_billiard_room_captain_talked" : False,
            "day2_evening_taste_from_flask" : False,

            "day3_morning_captain_found" : False,
            "day3_ending" : "",
            "day3_downstairs_visited" : False
        }

        lad_important_choices = CharacterImportantChoiceList ([
            CharacterInformation(0, "whisky", "You went to the bar for a drink on the first night", image_file="whisky"),
            CharacterInformation(0, "day1_drunk", "You got drunk the first night", image_file="drunk"),
            CharacterInformation(0, "downstairs_1", "You attempted to go downstairs", image_file="downstairs"),
            CharacterInformation(0, "hunt", "You decided to go hunting", image_file="hunt"),
            CharacterInformation(0, "hunt_captain_host", "You hunted with a Captain and a Lady", image_file="hunt_captain_host"),
            CharacterInformation(0, "hunt_doctor_drunk", "You hunted with a Doctor and a Drunk", image_file="hunt_doctor_drunk"),

            CharacterInformation(0, "downstairs_2", "You tried again to go downstairs", image_file="downstairs_2"),
            CharacterInformation(0, "day2_drunk", "You got drunk the second night", image_file="drunk_2"),
            CharacterInformation(0, "trust_psychic", "You decided to trust Amelia Baxter", image_file="trust_psychic"),
            
            CharacterInformation(0, "abandoned_psychic", "You abandoned Amelia Baxter and left the manor", image_file="leave_manor"),
            CharacterInformation(0, "protect_food", "You didn't leave your food unattended for too long", image_file="poison_food"),
            # DO we need the alternative? You left ? 
            CharacterInformation(0, "downstairs_3", "You pushed your luck a third time by going downstairs", image_file="downstairs_3"),
            CharacterInformation(0, "day3_drunk", "You got drunk the third night", image_file="drunk_3"),
        ])

        lad_endings = CharacterEndingList ([
            CharacterInformation(1, "deathbed", "You died in your sleep", image_file="deathbed"), 
            CharacterInformation(2, "gunned_down", "You were killed by a gunshot", image_file="gun_firing"), 
            CharacterInformation(3, "poisoned", "Your food was poisoned", image_file="poison_food"), 
            CharacterInformation(4, "fell", "You got impaled on a picket fence", image_file="fence"), 
            CharacterInformation(5, "escape", "You escaped, alone", image_file="escape"), 
        ])

        lad_intuitions = CharacterIntuitionList ([            
                CharacterInformation(1, "psychic_poisons", "On Sunday, your lunch was poisoned.", image_file="poison_food")
            ]
        )

        lad_observations = CharacterObservationList ([    
                CharacterInformation(1, "green_liquid", "There was a green liquid on Thomas Moody's nightstand.", image_file="poison_bedstand"), 
                CharacterInformation(1, "seen_car", "There is a car in the basement, but it has no gas", image_file="seen_car"),
                # TODO add seen car in observation =>
            ]
        )  

        lad_objects = CharacterObjectList([  
                CharacterInformation(1, "gun", "You took an empty handgun found in the gun room", image_file="gun"),
                CharacterInformation(2, "burned_letter", "A burned letter found in Samuel Manning's room", image_file="burned_letter"),
                # TODO: Add GAS ? Bullets ? Here or for someone else?
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
            test_checkpoints = lad_test_checkpoints,
        )
        lad = Character("lad_details.get_name()", image="lad", dynamic=True)

    return