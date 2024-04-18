label init_drunk:

    # call drunk_config_map
    
    # call drunk_config_menu
    
    python:
        drunk_name = "Samuel Manning"
        
        drunk_init_variables = {
        }

        drunk_extra_information = CharacterDescriptionHiddenList([
            CharacterInformation(0, "background", ""), 
            CharacterInformation(1, "status", ""),
            CharacterInformation(2, "age", "?"),
            CharacterInformation(3, "addict", "Likes to drink a bit too much.", is_important = True),
            CharacterInformation(60, "???", "???", is_important = True),
            ], drunk_name
        )

        drunk_description_full = """
        Old man, looking 'exhausted'.
        """

        drunk_details  = CharacterDetails(
            text_id = "drunk", 
            locked = True,
            know_real_name = True,
            real_name = drunk_name,
            nickname = "The Drunk",
            description_short = "Drunk Man",
            description_long = drunk_description_full,
            description_hidden = drunk_extra_information,
            important_choices = CharacterInformationList([]),
            endings = CharacterInformationList([]),
            intuitions = CharacterInformationList([]),
            observations = CharacterInformationList([]),
            objects = CharacterInformationList([]),
        )
        drunk = Character("drunk_details.get_name()", image="drunk", dynamic=True)

    return