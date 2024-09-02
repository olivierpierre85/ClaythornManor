label init_host:

    # call host_config_map
    
    # call host_config_menu
    
    python:
        host_name = "Lady Claythorn"
        
        host_init_variables = {
        }

        host_extra_information = CharacterDescriptionHiddenList ([
            CharacterInformation(0, "name_age", "Elisabeth - is born in 1865 and", is_important = True), 
            CharacterInformation(1, "down_to_earth", "look down upon 'lower class' individuals", is_important = True), 
            CharacterInformation(60, "independent", "realise she's more independent than most women of her status"), 
            CharacterInformation(60, "guns", "firearms"), 
            CharacterInformation(60, "car", "drive a car", is_important = True),
            CharacterInformation(60, "lie", "a progressive aristocrat close to the people. She is, in fact, one of the people - an out-of-work actress playing her most dangerous role", is_important = True),
            ], host_name
        )

        # host_description_full = """
        # Elegant and well-spoken, Lady Claythorn - first name Elisabeth - is born in 1865 and appears at first glance to embody everything expected of a wealthy lady.
        # However, if you delve deeper, you'll realise she's more independent than most women of her status. She is familiar with firearms and can also drive a car, which would raise more than a few eyebrows in her era.
        # And, for a member of the nobility, she does not look down upon 'lower class' individuals.
        # But as it turns out, she is not a progressive aristocrat close to the people. She is, in fact, one of the people - an out-of-work actress playing her most dangerous role.
        # """

        host_description = """
        Elegant and well-spoken, Lady Claythorn - first name <info:name_age> appears at first glance to embody everything expected of a wealthy lady.
        However, if you delve deeper, you'll <info:independent>. She is familiar with <info:guns> and can also <info:car>, which would raise more than a few eyebrows in her era.
        And, for a member of the nobility, she does not <info:down_to_earth>.
        But as it turns out, she is not <info:lie>.
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