label init_doctor:

    # call doctor_config_map
    
    call doctor_config_menu

    call doctor_config_progress
    
    python:

        doctor_name = "Daniel Baldwin"
        # Story Variables
        doctor_init_variables = {
            "broken_generic_menu": broken_generic_menu_doctor,
            "broken_offended": 0,
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
        ])

        doctor_extra_information = CharacterDescriptionHiddenList ([
            CharacterInformation(0, "background", "in the military. He later assumed the role of chief physician at a charity hospital", is_important = True), 
            CharacterInformation(0, "heroic_act", "he maintained for over a decade", is_important = True), 
            CharacterInformation(1, "status", "well-regarded, it did not make him a wealthy man. However, it provided him with the opportunity to glimpse the glamorous life of the rich people of his time. Thus, he can at least sort of understand the rules of this kind of world", is_important = True),
            CharacterInformation(2, "age", "39-year-old"),
            CharacterInformation(3, "addict", "sometimes fidgets for no apparent reason. This is common among opioid addicts", is_important = True),
            CharacterInformation(3, "fraud", "an affliction that led him to stealing drugs from his patients", is_important = True),
            CharacterInformation(3, "gay", "A confirmed bachelor, he never married. This led to some rumours among his staff about his possible \"inversion\"")
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
        <info:gay>.
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
            endings = CharacterInformationList([]),
            observations = CharacterInformationList([]),
            objects = CharacterInformationList([]),
            progress = doctor_progress,
            saved_variables = copy.deepcopy(doctor_init_variables),
            test_checkpoints = doctor_test_checkpoints,
        )
        doctor = Character("doctor_details.get_name()", image="doctor", dynamic=True)

    return