label init_nurse:

    call nurse_config_map
    
    call nurse_config_menu

    call nurse_config_progress

    python:
        nurse_name = "Rosalind Marsh"

        # Story Variables
        nurse_init_variables = {
            # MAP Menus
            "day1_evening_map_menu" : nurse_day1_evening_map_menu,
            "day2_no_hunt_map_menu" : nurse_day2_no_hunt_map_menu,
            "day3_morning_map_menu" : nurse_day3_morning_map_menu,

            # GENERIC Menus
            # "lad_generic_menu" : lad_generic_menu_nurse,
            # "lad_generic_other_guests_menu" : lad_generic_other_guests_menu_nurse,

            # "captain_generic_menu" : captain_generic_menu_nurse,
            # "captain_generic_other_guests_menu" : captain_generic_other_guests_menu_nurse,

            # "doctor_generic_menu" : doctor_generic_menu_nurse,
            # "doctor_generic_other_guests_menu": doctor_generic_other_guests_menu_nurse,

            # "nurse_generic_menu" : nurse_generic_menu_nurse,
            # "nurse_generic_other_guests_menu" : nurse_generic_other_guests_menu_nurse,
            
            # story var
            "illness_revealed": False,
            "stole_item": False,
            "drugged_guest": False,
        }

        nurse_important_choices = CharacterImportantChoiceList([
            CharacterInformation(
                0, "stole_item",
                "You stole a small silver spoon on the first day",
                content_negative="You resisted the urge to steal on the first day",
                image_file="spoon",
                chapters=['friday_afternoon'],
                relevant_chapters=['friday_afternoon', 'friday_evening'],
            ),
             CharacterInformation(
                0, "drugged_guest",
                "You put a sedative in someone's drink",
                content_negative="You didn't drug anyone",
                image_file="sedative",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_morning'],
            ),
        ])

        nurse_observations = CharacterObservationList([
             CharacterInformation(
                1, "guest_illness",
                "You noticed someone else is also sick",
                content_negative="You didn't notice any other illness",
                image_file="observation_illness",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening'],
            ),
        ])

        nurse_objects = CharacterObjectList([
             CharacterInformation(
                1, "medical_kit",
                "You have your trusty medical kit",
                content_negative="You don't have your medical kit",
                image_file="medical_kit",
                chapters=['start'],
                relevant_chapters=['start', 'friday_afternoon'],
            ),
        ])

        nurse_endings = CharacterEndingList ([
            CharacterInformation(1, "escaped", "You escaped the manor alive", image_file="escape", chapters=['end']), 
            CharacterInformation(2, "succumbed", "You succumbed to your illness", image_file="grave", chapters=['end']), 
        ])

        nurse_extra_information = CharacterDescriptionHiddenList([
            CharacterInformation(1, "job", "nurse most of her life, mostly in the army or at an hospital. Lately, she started to perform at home service for rich individuals", is_important = True), 
            CharacterInformation(2, "clothes", "well-dressed in an understated style", is_important = True),
            CharacterInformation(3, "age", "42 years old", is_important = True),
            CharacterInformation(4, "manor", "got accustomed with grand mansions and how they are run", is_important = True),
            CharacterInformation(5, "sick", "suffers from an incurable disease that leaves her weak and tired", is_important = True),
            CharacterInformation(0, "heroic_act", "She fought in almost all british wars since the cretan revolt. This also includes the Boxers Rebellion and, of course, the Great War", is_important = True),
            CharacterInformation(60, "lie", "stealing from her patients, or from anyone whenever she has the opportunity.", is_important = True),
            ], nurse_name
        )

        nurse_description = """
        A discreet <info:age> woman, she is <info:clothes>. 
        She worked as <info:job>. That's where she <info:manor>.
        <info:heroic_act>.
        She mostly keeps to herself, preferring to go to bed early, and avoiding getting out. Not because she is either shy or lazy, but because she <info:sick>. 
        But that doesn't prevent her from <info:lie>.
        """

        nurse_details  = CharacterDetails(
            text_id = "nurse", 
            locked = False, # Unlocking for testing
            know_real_name = True,
            real_name = nurse_name,
            nickname = "The Nurse",
            description_short = "Middle-aged woman.",
            description_long = nurse_description,
            description_hidden = nurse_extra_information,
            important_choices = nurse_important_choices,
            endings = nurse_endings,
            observations = nurse_observations,
            objects = nurse_objects,
            progress = nurse_progress,
            saved_variables = copy.deepcopy(nurse_init_variables), # copy so the init variables can be use again.
            test_checkpoints = nurse_test_checkpoints,
        )
        nurse = Character("nurse_details.get_name()", image="nurse", dynamic=True)

    return