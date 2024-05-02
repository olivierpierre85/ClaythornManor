label init_doctor:

    # call doctor_config_map
    
    # call doctor_config_menu
    
    python:

        doctor_name = "Daniel Baldwin"
        # Story Variables
        doctor_init_variables = {
        }

        doctor_extra_information = CharacterDescriptionHiddenList ([
            CharacterInformation(0, "background", "He's a doctor and runs an hospital", is_important = True), 
            CharacterInformation(0, "heroic_act", "He has stayed at his charity hospital for 10 years. Which is quite an achievement.", is_important = True), 
            CharacterInformation(1, "status", "Not wealthy.", is_important = True),
            CharacterInformation(2, "age", "He is 39 years old."),
            CharacterInformation(3, "addict", "An opium addict.", is_important = True),
            CharacterInformation(3, "fraud", "He Uses patients for an easy access to drugs.", is_important = True)
            ], doctor_name
        )
        
        doctor_description_full = """
        Glasses on his nose, this peculiar doctor spend a lot time hiding certain aspects of his life.
        He is only <info:age> at the end of the war.
        Born an raised in <info:origin>
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