label init_host:
    # call host_config_menu
    
    call host_config_progress
    
    python:
        host_name = "Lady Claythorn"
        
        host_init_variables = {
        }

        host_important_choices = CharacterImportantChoiceList([])
        host_observations = CharacterObservationList([])
        host_objects = CharacterObjectList([])

        host_extra_information = CharacterDescriptionHiddenList ([
            CharacterInformation(0, "name_age", "Elisabeth - is born in 1865 and", is_important = True), 
            CharacterInformation(1, "down_to_earth", "look down upon 'lower class' individuals", is_important = True), 
            CharacterInformation(60, "hunt", "cannot hunt at the level expected of a lady of her station", is_important = True),
            CharacterInformation(60, "car", "to drive a car", is_important = True),
            CharacterInformation(60, "table_manners", "table manners are not quite what they ought to be"),
            CharacterInformation(60, "lie", "a progressive aristocrat close to the people. She is, in fact, one of the people - an out-of-work actress playing her most dangerous role", is_important = True),
            CharacterInformation(60, "not_guilty", "guilty, she is not the mastermind behind the whole operation. She is not even in charge of it, the butler is.", is_important = True),
            ], host_name
        )

        # host_description_full = """
        # Elegant and well-spoken, Lady Claythorn - first name Elisabeth - is born in 1865 and appears at first glance to embody everything expected of a wealthy lady.
        # However, if you delve deeper, you'll notice her table manners are not quite what they ought to be. Also, she cannot hunt at the level expected of a lady of her station, a telling failing in a house such as this, though she has, oddly, learnt to drive a car.
        # And, for a member of the nobility, she does not look down upon 'lower class' individuals.
        # But as it turns out, she is not a progressive aristocrat close to the people. She is, in fact, one of the people - an out-of-work actress playing her most dangerous role.
        # """

        host_description = """
        Elegant and well-spoken, Lady Claythorn - first name <info:name_age> appears at first glance to embody everything expected of a wealthy lady.
        However, if you delve deeper, you'll notice her <info:table_manners>. Also, she <info:hunt>, a telling failing in a house such as this, though she has, oddly, learnt <info:car>.
        And, for a member of the nobility, she does not <info:down_to_earth>.
        But as it turns out, she is not <info:lie>. Even if it makes her look <not_guilty>.
        """

        host_details  = CharacterDetails(
            text_id = "host", 
            locked = True,
            real_name = host_name,
            nickname = "The Host",
            description_short = "Older Lady",
            description_long = host_description,
            description_hidden = host_extra_information,
            important_choices = host_important_choices,
            endings = CharacterInformationList([]),
            observations = host_observations,
            objects = host_objects,
            progress = host_progress,
            saved_variables = copy.deepcopy(host_init_variables),
            test_checkpoints = host_test_checkpoints,
        )
        host = Character("host_details.get_name()", image="host", dynamic=True)
    
    return