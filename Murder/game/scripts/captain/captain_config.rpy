label init_captain:
    
    # call captain_config_map
    
    # call captain_config_menu

    python:
        captain_name = "Sushil Sinha"
        # Story Variables
        captain_init_variables = {
            # "map_menu" : captain_map_menu,
        }

        captain_objects = CharacterObjectList([
            CharacterInformation(
                1, "butler_key",
                "You have the butler's master key",
                content_negative="You don't have the butler's master key",
                image_file="butler_key",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning', 'sunday_afternoon', 'end'],
            ),
        ])

        captain_endings = CharacterEndingList ([
            CharacterInformation(1, "todo", "You died in your sleep", image_file="deathbed", chapters=['saturday_morning']),
        ])

        # Character Class
        captain_extra_information = CharacterDescriptionHiddenList ([
            CharacterInformation(0, "wars", "his exploits in one of the several wars he fought in. Whether it was Burma, China, or during the Great War"), 
            CharacterInformation(10, "talker",  "being at the centre of attention, so he tend to monopolize the conversation", is_important = True),
            CharacterInformation(40, "heroic_act", "was so heroic during the war", is_important = True),
            CharacterInformation(40, "city", "London"), # TODO unlock somewhere, ? In captain walkthroug?
            CharacterInformation(20, "age", "54 years ago"),
            CharacterInformation(30, "mansion", "running of a large mansion", is_important = True),
            CharacterInformation(30, "table", "proper table manners", is_important = True),
            CharacterInformation(30, "family", "noble lineage ensured he received an education far superior to most", is_important = True), # TODO unlock somewhere, ? In captain walkthroug?            
            CharacterInformation(60, "lie", "they do not really include the fighting he claims to have participated in. As an administrative officer, he most likely spent most of his time behind desks", is_important = True),
            ], captain_name
        )

        # captain_description_full = """
        # When you enter a room, chances are you'll immediately notice this retired army officer. 
        # He cannot resist being at the centre of attention, so he tend to monopolize the conversation, usually by telling tales of his exploits in one of the several wars he fought in. Whether it was Burma, China, or during the Great War.
        # Born in India 54 years ago, he now resides London. 
        # Although he came from a region often looked down upon by the British, his noble lineage ensured he received an education far superior to most. That also means that the running of a large mansion and proper table manners have no secrets for him.
        # Invited to the manor for his impressive military career, it turns out they do not really include the fighting he claims to have participated in. As an administrative officer, he most likely spent most of his time behind desks.
        # """

        captain_description = """
        When you enter a room, chances are you'll immediately notice this retired army officer. 
        He cannot resist <info:talker>. And usually its by telling tales of <info:wars>.
        Born in India <info:age>, he now resides <info:city>. 
        Although he came from a region often looked down upon by the British, his <info:family>. That also means that the <info:mansion> and <info:table> have no secrets for him.
        Invited to the manor for his <info:heroic_act>, it turns out <info:lie>.
        """

        captain_details  = CharacterDetails(
            text_id = "captain", 
            locked = True,
            know_real_name = True,
            real_name = captain_name,
            nickname = "The Captain",
            description_short = "Older Indian man",
            description_long = captain_description,
            description_hidden = captain_extra_information,
            important_choices = CharacterInformationList([]),
            endings = captain_endings,
            observations = CharacterInformationList([]),
            objects = captain_objects,
            progress = [],
            saved_variables = copy.deepcopy(captain_init_variables),
        )
        captain = Character("captain_details.get_name()", image="captain", dynamic=True)
            
        

    return