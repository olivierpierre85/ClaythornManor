label init_lad:
    
    call lad_config_map
    
    call lad_config_menu

    python:
        # Story Variables
        lad_init_variables = {
            "map_menu" : lad_map_menu,
            "day1_evening_map_menu" : lad_day1_evening_map_menu,

            "psychic_generic_menu" : psychic_generic_menu_lad,
            "psychic_generic_other_guests_menu": psychic_generic_other_guests_menu_lad,
            "knows_psychic_background": False,
            "knows_psychic_room": False,
            
            "doctor_generic_menu" : doctor_generic_menu_lad,
            "doctor_generic_other_guests_menu": doctor_generic_other_guests_menu_lad,

            "knows_doctor_background": False,
            "knows_doctor_addict": False,

            "library_visited" : False,
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
            CharacterInformation(0, "origin", "Born and raised in Birmingham."), 
            CharacterInformation(10, "job", "A seller of stuff..."), 
            CharacterInformation(11, "thief", "... of stolen stuff apparently."), 
            CharacterInformation(20, "age", "He is 22 years old. He was only 15 at the end of the war."),
            CharacterInformation(30, "education", "Not a great reader."),
            CharacterInformation(40, "poor_drinker", "Can't hold his liqueur."),
            CharacterInformation(50, "drive", "He never learned how to drive."),
            CharacterInformation(60, "cook", "He is not much of a cook."),
            CharacterInformation(70, "poor", "It's rather obvious he is not from the upper class, to say the least.")
        ]
        lad_important_choices = CharacterInformationList ([
            CharacterInformation(0, "hunt", "You decided to go hunting", type="choice", image_file="gun")
        ])

        lad_endings = CharacterInformationList ([
            CharacterInformation(1, "gunned_down", "You die stoned to death", type="ending", image_file="gun_downed"), 
            CharacterInformation(2, "poisoned", "You were poisoned", type="ending", image_file="poisoned"), 
            CharacterInformation(3, "fell", "You fell on a picked fence", type="ending", image_file="poisoned"), 
        ])

        lad_intuitions = CharacterInformationList ([            
                CharacterInformation(1, "psychic_poisons", "Sunday, your lunch was poisoned.", type="intuition", image_file="gun")
            ],
            notification_text = "You have a new intuition",
            notification_sound = "audio/sound_effects/writing_short.ogg"
        )

        lad_observations = CharacterInformationList ([    
                CharacterInformation(1, "green_liquid", "There was a green liquid next to Thomas Moody death bed.", type="observation", image_file="poison") 
            ],
            notification_text = "You have made a new observation",
            notification_sound = "audio/sound_effects/writing_short.ogg"
        )  

        lad_objects = CharacterInformationList ([  
                CharacterInformation(1, "gun", "A empty handgun found in the gun room", type="object", image_file="gun")
            ], 
            notification_text = "You have found a new object",
            notification_sound = "audio/sound_effects/writing_short.ogg"
        )

        lad_details  = CharacterDetails(
            text_id = "lad", 
            locked = False,
            know_real_name = True,
            real_name = "Ted Harring",
            nickname = "The Lad",
            description_short = "Young man",
            description_long = "Good Looking lad, in his early twenties.",
            information_list = lad_extra_information,
            important_choices = lad_important_choices,
            endings = lad_endings,
            intuitions = lad_intuitions,
            observations = lad_observations,
            objects = lad_objects,
            saved_variables = copy.deepcopy(lad_init_variables), # copy so the init variables can be used again.
        )
        lad = Character("lad_details.get_name()", image="lad", dynamic=True)

    return