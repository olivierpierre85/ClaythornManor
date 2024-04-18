label init_captain:
    
    # call captain_config_map
    
    # call captain_config_menu

    python:
        captain_name = "Sushil Sinha"
        # Story Variables
        captain_init_variables = {
            # "map_menu" : captain_map_menu,
        }

        # Character Class
        captain_extra_information = CharacterDescriptionHiddenList ([
            CharacterInformation(0, "wars",     "A veteran of several wars, he fought in Burma, China, and in the Great War."), 
            CharacterInformation(10, "talker",  "Likes to tell stories in front of an audience.", is_important = True),
            CharacterInformation(40, "heroic act", "Was commanded for participating in most conflicts when he retired"),
            CharacterInformation(20, "age", "54 years old.", is_important = True),
            CharacterInformation(30, "mansion", "He knows a a lot about victorian mansions and their renovations."),
            CharacterInformation(60, "lie", "He never saw battle, was an administrative officer", is_important = True),
            ], captain_name
        )
        
        captain_description_full = """
        Older man from India.
        """

        captain_details  = CharacterDetails(
            text_id = "captain", 
            locked = True,
            know_real_name = True,
            real_name = captain_name,
            nickname = "The Captain",
            description_short = "Older Indian man",
            description_long = captain_description_full,
            description_hidden = captain_extra_information,
            important_choices = CharacterInformationList([]),
            endings = CharacterInformationList([]),
            intuitions = CharacterInformationList([]),
            observations = CharacterInformationList([]),
            objects = CharacterInformationList([]),
            saved_variables = copy.deepcopy(captain_init_variables),
        )
        captain = Character("captain_details.get_name()", image="captain", dynamic=True)
            
        

    return