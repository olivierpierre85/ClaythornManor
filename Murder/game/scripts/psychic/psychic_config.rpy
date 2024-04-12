label init_psychic:

    call psychic_config_map
    
    call psychic_config_menu

    python:
        # Story Variables
        psychic_init_variables = {
            # MAP Menus
            "day1_evening_map_menu" : psychic_day1_evening_map_menu,
            "day2_no_hunt_map_menu" : psychic_day2_no_hunt_map_menu,
            "day2_evening_map_menu" : psychic_day2_evening_map_menu,

            "lad_generic_menu" : lad_generic_menu_psychic,
            "lad_generic_other_guests_menu" : lad_generic_other_guests_menu_psychic,

            "captain_generic_menu" : captain_generic_menu_psychic,
            "captain_generic_other_guests_menu" : captain_generic_other_guests_menu_psychic,

            "doctor_generic_menu" : doctor_generic_menu_psychic,
            "doctor_generic_other_guests_menu": doctor_generic_other_guests_menu_psychic,

            "nurse_generic_menu" : nurse_generic_menu_psychic,
            "nurse_generic_other_guests_menu" : nurse_generic_other_guests_menu_psychic,

            "knows_doctor_background": False,
            
            # story var
            "knows_lad_background" : False,
            "knows_captain_origin" : False,
            "knows_captain_real_origin" : False,
            "day1_evening_billiard_room_visited" : False,
            "portrait_gallery_visited": False,
            "attic_visited": False,
            "knows_lord_name": False,
            "book_read": False,
            "day2_nohunt_bedroom_tries": 0,
            "day2_nohunt_has_visited_tea_room": False,
            "knows_nurse_background": False,
            "day2_evening_billiard_room_visited": False,
            "day2_evening_billiard_room_talk_to_captain": False,
        }

        psychic_extra_information = [
            CharacterInformation(0, "background", "A psychic. She can talk to the dead apparently.", is_important = True), 
            CharacterInformation(1, "status", "Wealthy enough to know how many people are needed to run a big house.", is_important = True), 
            CharacterInformation(2, "age", "She was .... SO she must be????"),
            CharacterInformation(3, "heroic_act", "She helped the police to find the kidnapper of a baby.", is_important = True),
            CharacterInformation(4, "lie", "She is not really a psychic. but an actress", is_important = True),
            CharacterInformation(5, "drive", "Doesn't have a driving license."),
            CharacterInformation(6, "racist", "She believes only white people come from England.")
        ]
        psychic_important_choices = CharacterInformationList([])
        
        psychic_endings = CharacterInformationList ([
            CharacterInformation(1, "burned", "You burn with the Manor", type="ending", image_file="gun_downed"), 
            CharacterInformation(2, "shot", "You were shot by Rosalind Marsh", type="ending", image_file="gun"),
            CharacterInformation(2, "escape", "You escape with Ted Harring", type="ending", image_file="gun"),
        ])

        psychic_observations = CharacterInformationList ([    
                CharacterInformation(1, "lord", "Lord Claythorn is 111 years old", type="observation", image_file="poison") 
            ],
            notification_text = "You have made a new observation",
            notification_sound = "audio/sound_effects/writing_short.ogg"
        )  

        psychic_intuitions = CharacterInformationList ([            
                CharacterInformation(1, "leave_castle", "Don't stay in the manor more than you have too.", type="intuition", image_file="gun")
            ],
            notification_text = "You have a new intuition",
            notification_sound = "audio/sound_effects/writing_short.ogg"
        )

        psychic_details  = CharacterDetails(
            text_id = "psychic", 
            locked = True,
            know_real_name = True,
            real_name = "Amelia Baxter",
            nickname = "The Psychic",
            description_short = "Middle-age Woman",
            description_long = "Middle-aged woman, looking a bit eccentric.",
            description_hidden = psychic_extra_information,
            important_choices = psychic_important_choices,
            endings = psychic_endings,
            intuitions = psychic_intuitions,
            observations = psychic_observations,
            objects = CharacterInformationList([]),
            saved_variables = psychic_init_variables
        )
        psychic = Character("psychic_details.get_name()", image="psychic", dynamic=True)

    return