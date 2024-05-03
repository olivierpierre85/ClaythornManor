label init_doctor:

    # call doctor_config_map
    
    # call doctor_config_menu
    
    python:

        doctor_name = "Daniel Baldwin"
        # Story Variables
        doctor_init_variables = {
        }

        doctor_extra_information = CharacterDescriptionHiddenList ([
            CharacterInformation(0, "background", "a charity hospital. Before that he served in the military for a bit.", is_important = True), 
            CharacterInformation(0, "heroic_act", "the last decade", is_important = True), 
            CharacterInformation(1, "status", "well-regarded, it did not make him a wealthy man. However, it provided him with the opportunity to glimpse the glamorous life of the rich people of his time. Thus, he can at least sort of understand the rules of this kind of world", is_important = True),
            CharacterInformation(2, "age", "39-year-old"),
            CharacterInformation(3, "addict", "sometimes fidgets for no apparent reason. This is common among opioid addicts", is_important = True),
            CharacterInformation(3, "fraud", "an affliction that led him to stealing drugs from his patients", is_important = True)
            ], doctor_name
        )
        # Keep for easy Reading
        # doctor_description_full_complete = """
        # Glasses on his nose, this 39-year-old doctor has spent the last decade working for a charity hospital. Before that he served in the military for a bit.
        # This feat was impressive enough to give Lady Claythorn reason to include him among the recipients of her special award.
        # Even though his position is well-regarded, it did not make him a wealthy man. However, it provided him with the opportunity to glimpse the glamorous life of the rich people of his time. Thus, he can at least sort of understand the rules of this kind of world.
        # Observe the doctor long enough, and you will see that he sometimes fidgets for no apparent reason. This is common among opioid addicts, an affliction that led him to stealing drugs from his patients.
        # """
        doctor_description_full = """
        Glasses on his nose, this <info:age> doctor has spent <info:heroic_act> working for <info:background>.
        This feat was impressive enough to give Lady Claythorn reason to include him among the recipients of her special award.
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
            important_choices = CharacterInformationList([]),
            endings = CharacterInformationList([]),
            intuitions = CharacterInformationList([]),
            observations = CharacterInformationList([]),
            objects = CharacterInformationList([]),
        )
        doctor = Character("doctor_details.get_name()", image="doctor", dynamic=True)

    return