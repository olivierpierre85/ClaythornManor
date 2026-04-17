label init_captain:

    call captain_config_progress

    call captain_day1_evening_map_menu

    # call captain_config_menu

    python:
        captain_name = "Sushil Sinha"
        # Story Variables
        captain_init_variables = {
            # MAP Menus
            "day1_evening_map_menu" : captain_day1_evening_map_menu,

            # Evening day 1
            "day1_evening_billiard_room_visited" : False,
            "day1_evening_bedroom_refusals" : 0,
        }

        captain_important_choices = CharacterImportantChoiceList([
            CharacterInformation(
                0, "tell_boxer_story",
                "You told a story about the Boxer Rebellion",
                content_negative="You didn't tell a story about the Boxer Rebellion",
                image_file="boxer_rebellion",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_morning' , 'saturday_afternoon', 'saturday_evening', 'sunday_morning'],
            ),
        ])

        captain_observations = CharacterObservationList([
            CharacterInformation(1, "captain_host_suspicion_name", "You noticed a problem with the name 'Lady Claythorn'",
                content_negative="You didn't investigate the library",
                image_file="captain_host_suspicion_name",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_morning', 'saturday_evening'],
            ),
            CharacterInformation(2, "captain_host_suspicion_portrait", "You couldn't find Lady Claythorn's portrait in the gallery",
                content_negative="You didn't investigate the portrait gallery",
                image_file="captain_host_suspicion_portrait",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_morning', 'saturday_evening'],
            ),
            CharacterInformation(3, "captain_garden_shed_locked", "You found the garden shed, locked",
                content_negative="You didn't investigate the garden shed",
                image_file="outdoor_shed_locked",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_morning', 'saturday_evening'],
            ),
            CharacterInformation(4, "captain_host_suspicion_shooting",
                "You noticed Lady Claythorn shoots very poorly",
                content_negative="You didn't observe Lady Claythorn on the hunt",
                image_file="outdoor_shed_locked", # TODO placeholder, needs proper image
                chapters=['saturday_afternoon'],
                relevant_chapters=['saturday_afternoon', 'saturday_evening'],
            ),
        ])

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
            CharacterInformation(1, "strangled",
                "You were strangled by the butler in the woods",
                image_file="outdoor_shed_locked", # TODO placeholder, needs proper image
                chapters=['saturday_afternoon']),
            CharacterInformation(2, "shot_in_woods",
                "You were shot in the woods by Thomas Moody",
                image_file="outdoor_shed_locked", # TODO placeholder, needs proper image
                chapters=['saturday_afternoon']),
        ])

        # Character Class
        captain_extra_information = CharacterDescriptionHiddenList ([
            CharacterInformation(0, "wars", "his exploits in one of the several wars he fought in. Whether it was Burma, during the Great War or the Boxer's Rebellion in China"), 
            CharacterInformation(10, "talker",  "being at the centre of attention, so he tend to monopolize the conversation", is_important = True),
            CharacterInformation(40, "heroic_act", "impressive military career", is_important = True),
            CharacterInformation(40, "city", "London"), # TODO unlock somewhere, ? In captain walkthroug?
            CharacterInformation(20, "age", "54 years ago"),
            CharacterInformation(30, "mansion", "running of a large mansion", is_important = True),
            CharacterInformation(30, "table", "proper table manners", is_important = True),
            CharacterInformation(30, "family", "noble lineage ensured he received an education far superior to most", is_important = True), # TODO unlock somewhere, ? In captain walkthroug?            
            CharacterInformation(45, "embellishment", " some of the details may have been somewhat enhanced over the years"),
            CharacterInformation(60, "lie", "they do not really include the fighting he claims to have participated in. As an administrative officer, he spent most of his time behind desks", is_important = True),
            ], captain_name
        )

        # captain_description_full = """
        # When you enter a room, chances are you'll immediately notice this retired army officer. 
        # He cannot resist being at the centre of attention, so he tend to monopolize the conversation, usually by telling tales of his exploits in one of the several wars he fought in. Whether it was Burma, China, or during the Great War. They are great stories, even though <info:embellishment>.
        # Born in India 54 years ago, he now resides London.  
        # Although he came from a region often looked down upon by the British, his noble lineage ensured he received an education far superior to most. That also means that the running of a large mansion and proper table manners have no secrets for him.
        # Invited to the manor for his impressive military career, it turns out they do not really include the fighting he claims to have participated in. As an administrative officer, he spent most of his time behind desks.
        # """

        captain_description = """
        When you enter a room, chances are you'll immediately notice this retired army officer. 
        He cannot resist <info:talker>. And usually its by telling tales of <info:wars>. They are great stories, even though <info:embellishment>.
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
            important_choices = captain_important_choices,
            endings = captain_endings,
            observations = captain_observations,
            objects = captain_objects,
            progress = captain_progress,
            test_checkpoints = captain_test_checkpoints,
            saved_variables = copy.deepcopy(captain_init_variables),
        )
        captain = Character("captain_details.get_name()", image="captain", dynamic=True)
            
        

    return