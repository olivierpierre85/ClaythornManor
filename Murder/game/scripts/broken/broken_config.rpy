label init_broken:

    # call broken_config_map
    
    # call broken_config_menu
    
    python:
        broken_name = "Thomas Moody"
        
        broken_init_variables = {
        }

        broken_extra_information = CharacterDescriptionHiddenList([
            CharacterInformation(0, "mask", "A broken face or 'Gueule Cassée'. He wears mask that hides most of hist face because of an injury during the war."),
            CharacterInformation(60, "???", "???", is_important = True),       
            ], broken_name
        )

        broken_description_full = """
        A man with a mask on his face.
        """

        broken_details  = CharacterDetails(
            text_id = "broken", 
            locked = True,
            know_real_name = True,
            real_name = broken_name,
            nickname = "The Broken Face",
            description_short = "Masked Man",
            description_long = broken_description_full,
            description_hidden = broken_extra_information,
            important_choices = CharacterInformationList([]),
            endings = CharacterInformationList([]),
            intuitions = CharacterInformationList([]),
            observations = CharacterInformationList([]),
            objects = CharacterInformationList([]),
        )
        broken = Character("broken_details.get_name()", image="broken", dynamic=True)
    
    return