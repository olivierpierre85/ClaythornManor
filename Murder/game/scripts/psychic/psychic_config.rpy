label init_psychic:

    call psychic_config_map
    
    call psychic_config_menu

    call psychic_config_progress

    python:
        psychic_name = "Amelia Baxter"
        # Story Variables
        psychic_init_variables = {
            # MAP Menus
            "day1_evening_map_menu" : psychic_day1_evening_map_menu,
            "day2_no_hunt_map_menu" : psychic_day2_no_hunt_map_menu,
            "day2_evening_map_menu" : psychic_day2_evening_map_menu,

            "lad_generic_menu" : lad_generic_menu_psychic,
            "lad_generic_other_guests_menu" : lad_generic_other_guests_menu_psychic,

            "captain_generic_menu" : captain_generic_menu_psychic,
            "captain_generic_other_guests_menu" : captain_generic_other_guests_menu_psychic,

            "doctor_generic_menu" : doctor_generic_menu_psychic,
            "doctor_generic_other_guests_menu": doctor_generic_other_guests_menu_psychic,

            "nurse_generic_menu" : nurse_generic_menu_psychic,
            "nurse_generic_other_guests_menu" : nurse_generic_other_guests_menu_psychic,


            # story var
            "day1_evening_billiard_room_visited" : False,
            "portrait_gallery_visited": False,
            "book_read": False,
            "day2_nohunt_bedroom_tries": 0,
            "day2_has_seen_bedroom_broken": False,
            "day2_evening_billiard_room_visited": False,
            "day2_evening_billiard_room_talk_to_captain": False,
            "day1_evening_talk_to_lad": False,
            "day1_evening_talk_to_captain": False,
            "day2_evening_bedroom_tries": 0,
        }

        psychic_important_choices = CharacterImportantChoiceList([
            CharacterInformation(
                0, "visit_lad",
                "You approached Ted Harring",
                content_negative="You didn't approach Ted Harring",
                image_file="trust_psychic",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(
                0, "steal_gun",
                "You tried to take Rosalind's gun by force",
                content_negative="You didn't try to take Rosalind's gun by force",
                image_file="gun",
                chapters=['sunday_afternoon'],
                relevant_chapters=['sunday_afternoon', 'end'],
            ),
            CharacterInformation(
                0, "leave_manor",
                "You left the manor while you still could",
                content_negative="You stayed in the manor despite the risks",
                image_file="leave_manor",
                chapters=['sunday_afternoon'],
                relevant_chapters=['sunday_afternoon', 'end'],
            ),
        ])

        psychic_observations = CharacterObservationList([
            CharacterInformation(
                0, "visited_attic",
                "You visited the attic and met the Lord of this place",
                content_negative="You didn't go to the attic",
                image_file="lord",
                chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening'],
                relevant_chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(
                1, "lord_name",
                "Lord Claythorn's name is Nicholas",
                content_negative="You haven't discovered Lord Claythorn's name",
                image_file="lord_2",
                chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening'],
                relevant_chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(
                1, "lord_age",
                "Lord Claythorn is 111 years old",
                content_negative="You haven't learned Lord Claythorn's age",
                image_file="lord_3",
                chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening'],
                relevant_chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(
                1, "nurse_blood",
                "You noticed blood on Rosalind Marsh's handkerchief",
                content_negative="You didn't notice blood on Rosalind Marsh's handkerchief",
                image_file="blood_handkerchief",
                chapters=['saturday_afternoon'],
                relevant_chapters=['saturday_afternoon', 'saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(
                1, "nurse_sick",
                "Rosalind Marsh told you about her disease",
                content_negative="Rosalind Marsh didn't tell you about her disease",
                image_file="nurse_sick",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(
                1, "silverware",
                "You found silverware in  Rosalind Marsh's room",
                content_negative="You didn't find silverware in  Rosalind Marsh's room",
                image_file="silverware",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning'],
            ),
        ])

        psychic_objects = CharacterObjectList([
            CharacterInformation(
                1, "butler_key",
                "You have the butler's master key",
                content_negative="You don't have the butler's master key",
                image_file="butler_key",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning', 'sunday_afternoon', 'end'],
            ),
        ])

        psychic_endings = CharacterEndingList ([
            CharacterInformation(0, "fell", "You fell down the stairs", image_file="psychic_fell", chapters=['sunday_morning']),
            CharacterInformation(1, "burned", "You were burned along with the manor", image_file="manor_burns", is_intuition=True, chapters=['end']), 
            CharacterInformation(2, "shot", "You were shot by Rosalind Marsh", image_file="gun_firing", chapters=['end']),
            CharacterInformation(3, "escape", "You escaped with Ted Harring", image_file="escape", chapters=['end']),
        ])

        psychic_extra_information = CharacterDescriptionHiddenList([
            CharacterInformation(0, "background","psychic who claims to be able to converse with the dead" , is_important = True), 
            CharacterInformation(1, "status", "London, she obviously knows her way around a grand house", is_important = True), 
            CharacterInformation(2, "age", "disclose her age to anyone"),
            CharacterInformation(3, "heroic_act", "abilities, she was able to help the police find the kidnapper of a Duke's young heir", is_important = True),
            CharacterInformation(4, "lie", "deathbed, she confessed to being a fraud, admitting she is nothing but an con artist", is_important = True),
            CharacterInformation(5, "drive", "cannot drive"),
            CharacterInformation(6, "racist", "a tad racist")
            ], psychic_name
        )        
        # Keep for easy Reading
        # psychic_description_full_complete = """
        # An eccentric-looking middle-aged woman, she won't disclose her age to anyone.
        # Currently residing in London, she obviously knows her way around a grand house.
        # She is a psychic who claims to be able to converse with the dead.
        # Lady Claythorn invited her to the manor because, thanks to her abilities, she was able to help the police find the kidnapper of a Duke's young heir.
        # That is peculiar because on her deathbed, she confessed to being a fraud, admitting she is nothing but an actress.
        # Being a woman of her era, she conforms to most stereotypes, meaning that she cannot drive and that she can be a tad racist.
        # """

        psychic_description_full = """
        An eccentric-looking middle-aged woman, she won't <info:age>.
        Currently residing in <info:status>.
        She is a <info:background>.
        Lady Claythorn invited her to the manor because, thanks to her <info:heroic_act>.
        That is peculiar because on her <info:lie>.
        Being a woman of her era, she conforms to most stereotypes, meaning that she <info:drive> and that she can be <info:racist>.
        """
        # LATER  you discover that she is actually 42, and full story is told

        psychic_details  = CharacterDetails(
            text_id = "psychic", 
            locked = True,
            know_real_name = True,
            real_name = psychic_name,
            nickname = "The Psychic",
            description_short = "Middle-age Woman",
            description_long = psychic_description_full,
            description_hidden = psychic_extra_information,
            important_choices = psychic_important_choices,
            endings = psychic_endings,
            observations = psychic_observations,
            objects = psychic_objects,
            progress = psychic_progress,
            saved_variables = copy.deepcopy(psychic_init_variables),
            test_checkpoints = psychic_test_checkpoints,
        )
        psychic = Character("psychic_details.get_name()", image="psychic", dynamic=True)

    return