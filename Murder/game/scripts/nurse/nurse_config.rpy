label init_nurse:

    call nurse_day1_evening_map_menu
    call nurse_day2_no_hunt_map_menu
    call nurse_day2_evening_map_menu
    call nurse_day2_evening_billiard_room_menu #TODO check needed

    call nurse_config_menu

    call nurse_config_progress

    python:
        nurse_name = "Rosalind Marsh"

        # Story Variables
        nurse_init_variables = {
            # MAP Menus
            "day1_evening_map_menu" : nurse_day1_evening_map_menu,
            "day2_no_hunt_map_menu" : nurse_day2_no_hunt_map_menu,
            "day2_evening_map_menu" : nurse_day2_evening_map_menu,

            # Generic Menus
            "drunk_generic_menu" : drunk_generic_menu_nurse,
            "drunk_generic_other_guests_menu" : drunk_generic_other_guests_menu_nurse,

            "psychic_generic_menu": psychic_generic_menu_nurse,
            "psychic_generic_other_guests_menu": psychic_generic_other_guests_menu_nurse,
            
            # story var
            "lockpick_seen" : False,
            "bedroom_too_dangerous_seen" : False,
            "day2_evening_bedroom_closed" : False,
            "day1_evening_billiard_room_visited" : False,
            "library_visited": False,
            "portrait_gallery_visited": False,
            "attic_visited": False,
            "day2_hunt_tea_room_early" : False,
        }

        nurse_important_choices = CharacterImportantChoiceList([
            CharacterInformation(
                0, "day1_exhaustion",
                "You overexerted yourself on Friday evening and suffered a coughing fit",
                content_negative="You didn't overexerted yourself on Friday evening",
                image_file="blood_handkerchief_1",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_morning' ,'saturday_evening'],
            ),
            CharacterInformation(
                0, "spotted_by_psychic",
                "You were spotted by Mrs Baxter while searching her room",
                content_negative="Mrs Baxter did not notice anything amiss",
                image_file="psychic",
                chapters=['saturday_afternoon'],
                relevant_chapters=['saturday_afternoon', 'saturday_evening'],
            ),
        ])

        
        nurse_observations = CharacterObservationList([
            CharacterInformation(
                1, "captain_lie_rank",
                "You noticed an inconsistency in Captain Sinha's story about his rank",
                content_negative="You didn't notice the inconsistency in Captain Sinha's story",
                image_file="captain",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening'],
            ),
            CharacterInformation(
                0, "footman_belgian",
                "You found out that the footman is actually from Belgium.",
                content_negative="You don't know much about the footman.",
                image_file="footman_belgian",
                chapters=['saturday_afternoon'],
                relevant_chapters=['saturday_afternoon', 'saturday_evening'],
            ),
            CharacterInformation(
                0, "maid_actress",
                "You discovered that the maid used to be an aspiring actress.",
                content_negative="You don't know much about the maid.",
                image_file="maid_actress",
                chapters=['saturday_afternoon'],
                relevant_chapters=['saturday_afternoon', 'saturday_evening'],
            ),
        ])

        nurse_objects = CharacterObjectList([
            CharacterInformation(
                0, "steal_cutlery_1",
                "You took some cutlery after Friday's dinner",
                content_negative="You did not take some cutlery after Friday's dinner",
                image_file="cutlery_1",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening','sunday_afternoon'],
            ),
            CharacterInformation(
                0, "steal_cutlery_2",
                "You took some cutlery after Saturday's breakfast",
                content_negative="You did not take some cutlery after Saturday's breakfast",
                image_file="cutlery_2",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening','sunday_afternoon'],
            ),
            CharacterInformation(
                0, "steal_pearls",
                "You took some pearls from Lady Claythorn's room",
                content_negative="You did not take some pearls from Lady Claythorn's room",
                image_file="pearls",
                chapters=['saturday_afternoon'],
                relevant_chapters=['saturday_afternoon','sunday_afternoon'],
            ),
            CharacterInformation(
                0, "take_gun",
                "You took a revolver from the gun room",
                content_negative="You did not take a revolver from the gun room",
                image_file="gun",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening','sunday_afternoon'],
            ),
            CharacterInformation(
                0, "find_bullets",
                "You found a stash of military calibre bullets hidden in the attic storage room",
                content_negative="You did not find the hidden bullets",
                image_file="bullets",
                chapters=['saturday_afternoon'],
                relevant_chapters=['saturday_afternoon','saturday_evening'],
            ),
        ])

        nurse_extra_information = CharacterDescriptionHiddenList([
            CharacterInformation(1, "job", "nurse most of her life, mostly in the army or at an hospital. Lately, she started to perform at home service for rich individuals", is_important = True), 
            CharacterInformation(2, "clothes", "well-dressed in an understated style", is_important = True),
            CharacterInformation(3, "age", "42 years old", is_important = True),
            CharacterInformation(4, "manor", "got accustomed with grand mansions and how they are run", is_important = True),
            CharacterInformation(5, "sick", "suffers from an incurable disease that leaves her weak and tired", is_important = True),
            CharacterInformation(0, "heroic_act", "She fought in almost all british wars since the cretan revolt. This also includes the Boxers Rebellion and, of course, the Great War", is_important = True),
            CharacterInformation(60, "lie", "stealing from her patients, or from anyone whenever she has the opportunity.", is_important = True),
            ], nurse_name
        )
        # nurse_description_full = """
        # A discreet 42 years old woman, she is well-dressed in an understated style. 
        # She worked as nurse most of her life, mostly in the army or at an hospital.
        # Lately, she started to perform at home service for rich individuals. That's where she got accustomed with grand mansions and how they are run.
        # She fought in almost all british wars since the cretan revolt. This also includes the Boxers Rebellion and, of course, the Great War.
        # She mostly keeps to herself, preferring to go to bed early, and avoiding getting out. Not because she is either shy or lazy, but because she suffers from an illness, in which a visible symptom is coughing blood. 
        # But that doesn't prevent her from stealing from her patients, or from anyone whenever she has the opportunity.
        # """

        nurse_description = """
        A discreet <info:age> woman, she is <info:clothes>. 
        She worked as <info:job>. That's where she <info:manor>.
        <info:heroic_act>.
        She mostly keeps to herself, preferring to go to bed early, and avoiding getting out. Not because she is either shy or lazy, but because she <info:sick>. 
        But that doesn't prevent her from <info:lie>.
        """

        nurse_details  = CharacterDetails(
            text_id = "nurse", 
            locked = True,
            know_real_name = True,
            real_name = nurse_name,
            nickname = "The Nurse",
            description_short = "Middle-aged woman.",
            description_long = nurse_description,
            description_hidden = nurse_extra_information,
            important_choices = nurse_important_choices,
            endings = CharacterInformationList([]),
            observations = nurse_observations,
            objects = nurse_objects,
            progress = nurse_progress,
            saved_variables = copy.deepcopy(nurse_init_variables),
            test_checkpoints = nurse_test_checkpoints,
        )
        nurse = Character("nurse_details.get_name()", image="nurse", dynamic=True)

    return