label init_host:

    # call host_config_map
    
    # call host_config_menu
    
    python:
        host_name = "Lady Claythorn"
        
        host_init_variables = {
        }

        host_extra_information = CharacterDescriptionHiddenList ([
            CharacterInformation(0, "todo", "todo", is_important = True), 
            # CharacterInformation(0, "name", "Her first name is Elisabeth", is_important = True), 
            CharacterInformation(1, "down_to_earth", "look down the \"lower class\" people.", is_important = True), 
            CharacterInformation(60, "???", "???", is_important = True),
            ], host_name
        )

        host_description_full = """
        The lady of the mansion. Elegant and well spoken, she doesn't look down the "lower class" people.

        """
        host_description = """
        The lady of the mansion.
        """

        host_details  = CharacterDetails(
            text_id = "host", 
            locked = True,
            know_real_name = True,
            real_name = host_name,
            nickname = "The Host",
            description_short = "Older Lady",
            description_long = host_description,
            description_hidden = host_extra_information,
            important_choices = CharacterInformationList([]),
            endings = CharacterInformationList([]),
            intuitions = CharacterInformationList([]),
            observations = CharacterInformationList([]),
            objects = CharacterInformationList([]),
        )
        host = Character("host_details.get_name()", image="host", dynamic=True)
    
    return