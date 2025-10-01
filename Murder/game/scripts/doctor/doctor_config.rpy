label init_doctor:

    call doctor_config_map
    
    call doctor_config_menu

    call doctor_config_progress
    
    python:

        doctor_name = "Daniel Baldwin"
        # Story Variables
        doctor_init_variables = {
            # MAP Menus
            "day1_evening_map_menu" : doctor_day1_evening_map_menu,

            # Generic Menus
            "broken_generic_menu": broken_generic_menu_doctor,
            "lad_generic_menu" : lad_generic_menu_doctor,
            "nurse_generic_menu" : nurse_generic_menu_doctor,

            # Evening day 1
            "broken_offended": 0,
            "day1_evening_billiard_room_visited" : False,
            "attic_visited": False

        }

        doctor_important_choices = CharacterImportantChoiceList([
            CharacterInformation(
                0, "broken_offended",
                "You offended Thomas Moody by asking him the wrong questions",
                content_negative="You didn't offend Thomas Moody",
                image_file="broken_offended",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening'],
            ),
            # WAS used on the first day BUT should be used later TODO: During the hunt?
            # CharacterInformation(
            #     0, "laudanum_extra_1",
            #     "You took an extra dose of laudanum",
            #     content_negative="You didn't take an extra dose of laudanum",
            #     image_file="laudanum",
            #     chapters=['friday_evening'],
            #     relevant_chapters=['friday_evening', 'saturday_morning'],
            # ),
            CharacterInformation(
                0, "flirt",
                "You flirted with the footman",
                content_negative="You didn't flirt with the footman",
                image_file="flirt",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening'],
            ),
            CharacterInformation(
                0, "broken_unmasked",
                "You removed Thomas Moody's mask",
                content_negative="You didn't remove Thomas Moody's mask",
                image_file="broken_unmasked",
                chapters=['saturday_morning'],
                relevant_chapters=['saturday_morning', 'saturday_evening'],
            ),
        ])

        doctor_objects = CharacterObjectList([
            CharacterInformation(
                1, "book_mystery",
                'You took "The Mysterious Affair at Styles" from the library',
                content_negative='You didn\'t take "The Mysterious Affair at Styles" from the library',
                image_file="book_mystery",
                chapters=['friday_evening'],
                relevant_chapters=['saturday_morning'],
            ),
            CharacterInformation(
                2, "book_opium",
                'You took "Confessions of an English Opium-Eater" from the library',
                content_negative='You didn\'t take "Confessions of an English Opium-Eater" from the library',
                image_file="book_opium",
                chapters=['friday_evening'],
                relevant_chapters=['saturday_morning'],
            ),
        ])

        doctor_observations = CharacterObservationList([
            CharacterInformation(
                1, "footman_french_1",
                "You noticed an odd expression coming from the footman",
                content_negative="You didn't notice an odd expression coming from the footman",
                image_file="footman_french_1",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_evening'],
            ),
            CharacterInformation(
                1, "footman_french_2",
                "You noticed an other odd expression coming from the footman",
                content_negative="You didn't an other odd expression coming from the footman",
                image_file="footman_french_2",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening'],
            ),
        ])

        doctor_endings = CharacterEndingList ([
            CharacterInformation(1, "overdose", "You overdosed on opioids", image_file="laudanum_overdose", chapters=['saturday_morning']), 
            CharacterInformation(3, "shot_by_drunk", "You were shot to death by Samuel Manning", image_file="hunting_rifle", is_intuition=True, chapters=['saturday_evening']), 
        ])

        doctor_extra_information = CharacterDescriptionHiddenList ([
            CharacterInformation(0, "background", "in the military. He later assumed the role of chief physician at a charity hospital", is_important = True), 
            CharacterInformation(0, "heroic_act", "he maintained for over a decade", is_important = True), 
            CharacterInformation(1, "status", "well-regarded, it did not make him a wealthy man. However, it provided him with the opportunity to glimpse the glamorous life of the rich people of his time. Thus, he can at least sort of understand the rules of this kind of world", is_important = True),
            CharacterInformation(2, "age", "39-year-old"),
            CharacterInformation(3, "addict", "sometimes fidgets for no apparent reason. This is common among opioid addicts", is_important = True),
            CharacterInformation(3, "fraud", "an affliction that led him to stealing drugs from his patients", is_important = True),
            # Hide as long as it is not relevant to the story
            # CharacterInformation(3, "gay", "A confirmed bachelor, he never married. This led to some rumours among his staff about his possible \"inversion\"")         <info:gay>.
            ], doctor_name
        )
        # Keep for easy Reading 
        # doctor_description_full_complete = """
        # Glasses on his nose, this 39-year-old doctor began his career in the military. He later assumed the role of chief physician at a charity hospital, a position he maintained for over a decade. 
        # This was impressive enough to give Lady Claythorn reason to include him among the recipients of her special award.
        # Even though his position is well-regarded, it did not make him a wealthy man. However, it provided him with the opportunity to glimpse the glamorous life of the rich people of his time. Thus, he can at least sort of understand the rules of this kind of world.
        # A confirmed bachelor, he never married. This led to some rumours among his staff about his possible "inversion".        
        # Observe the doctor long enough, and you will see that he sometimes fidgets for no apparent reason. This is common among opioid addicts, an affliction that led him to stealing drugs from his patients.
        # """
        doctor_description_full = """
        Glasses on his nose, this <info:age> doctor began his career <info:background>, a position <info:heroic_act>.
        This was impressive enough to give Lady Claythorn reason to include him among the recipients of her special award.
        Even though his position is <info:status>.
        Observe the doctor long enough, and you will see that he <info:addict>, <info:fraud>.
        """

        doctor_details  = CharacterDetails(
            text_id = "doctor", 
            locked = True,
            know_real_name = True,
            real_name = doctor_name,
            nickname = "The Doctor",
            description_short = "Middle-age man",
            description_long = doctor_description_full,
            description_hidden = doctor_extra_information,
            important_choices = doctor_important_choices,
            endings = doctor_endings,
            observations = doctor_observations,
            objects = doctor_objects,
            progress = doctor_progress,
            saved_variables = copy.deepcopy(doctor_init_variables),
            test_checkpoints = doctor_test_checkpoints,
        )
        doctor = Character("doctor_details.get_name()", image="doctor", dynamic=True)

    return