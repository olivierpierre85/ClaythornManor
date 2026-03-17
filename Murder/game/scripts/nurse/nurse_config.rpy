label init_nurse:

    call nurse_day1_evening_map_menu
    call nurse_day2_no_hunt_map_menu
    call nurse_day2_evening_map_menu

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

            "host_generic_menu": host_generic_menu_nurse,
            
            # story var
            "lockpick_seen" : False,
            "bedroom_too_dangerous_seen" : False,
            "day2_evening_bedroom_closed" : False,
            "day1_evening_billiard_room_visited" : False,
            "day2_evening_billiard_room_visited" : False,
            "visited_library": False,
            "visited_portrait_gallery": False,
            "generic_attic_visited": False,
            "visited_attic_females_room": False,
            "visited_attic_butler_room": False,
            "tried_butler_cabinet": False,
            "visited_attic_males_room": False,
            "visited_attic_storage": False,
            "visited_garage": False,
            "visited_gun_room": False,
            "day2_hunt_tea_room_early" : False,
            "day2_evening_exhaustion_triggered" : False,
        }

        nurse_important_choices = CharacterImportantChoiceList([
            CharacterInformation(
                0, "day1_exhaustion",
                "You overexerted yourself on Friday evening and suffered a coughing fit",
                content_negative="You didn't overexerted yourself on Friday evening",
                image_file="blood_handkerchief_1",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_morning', 'saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(
                0, "day2_exhaustion",
                "You overexerted yourself on Saturday evening and suffered a coughing fit",
                content_negative="You didn't overexert yourself on Saturday evening",
                image_file="blood_handkerchief_2",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(
                0, "spotted_by_psychic",
                "You were spotted by Mrs Baxter while searching her room",
                content_negative="Mrs Baxter did not notice anything amiss",
                image_file="psychic_angry",
                chapters=['saturday_afternoon'],
                relevant_chapters=['saturday_afternoon', 'saturday_evening'],
            ),
            CharacterInformation(
                0, "swapped_plates",
                "You swapped your plate with Mr Harring's before luncheon",
                content_negative="You did not swap plates before luncheon",
                image_file="swapping_of_plates",
                chapters=['sunday_afternoon'],
                relevant_chapters=['sunday_afternoon'],
            ),
        ])

        
        nurse_observations = CharacterObservationList([
            CharacterInformation(
                1, "captain_lie_boxer",
                "You noticed an inconsistency in Captain Sinha's story about his rank",
                content_negative="You didn't notice the inconsistency in Captain Sinha's story",
                image_file="captain_lie_boxer",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_evening'],
            ),
            CharacterInformation(
                1, "captain_lie_zanzibar",
                "You noticed something odd in the way Captain Sinha spoke about the Anglo-Zanzibar War.",
                content_negative="You didn't notice anything unusual about the Captain's story.",
                image_file="captain_lie_zanzibar",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_evening'],
            ),
            CharacterInformation(
                0, "remember_doctor",
                "You realised that you worked with Doctor Baldwin during the Boxer Rebellion.",
                content_negative="You didn't realise that you worked with Doctor Baldwin during the Boxer Rebellion.",
                image_file="remember_nurse",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_morning', 'saturday_evening'],
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
                relevant_chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_afternoon'],
            ),
            CharacterInformation(
                0, "steal_cutlery_2",
                "You took some cutlery after Saturday's breakfast",
                content_negative="You did not take some cutlery after Saturday's breakfast",
                image_file="cutlery_2",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_afternoon'],
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
                relevant_chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_afternoon'],
            ),
            CharacterInformation(
                0, "find_bullets",
                "You found a stash of military calibre bullets hidden in the attic storage room",
                content_negative="You did not find the hidden bullets",
                image_file="bullets",
                chapters=['saturday_afternoon'],
                relevant_chapters=['saturday_afternoon', 'saturday_evening', 'sunday_afternoon'],
            ),
        ])

        nurse_endings = CharacterEndingList ([
            CharacterInformation(1, "exhausted", "You collapsed from exhaustion", image_file="nurse_sick", chapters=['saturday_evening']),
            CharacterInformation(1, "escape_poor", "You escaped, but with very little to show for it", image_file="escape", chapters=['saturday_evening']),
            CharacterInformation(1, "billiard_room_death", "You died in the billiard room after confronting the Captain", image_file="fight_nurse_and_captain", chapters=['saturday_evening']),
            CharacterInformation(2, "gunned_down", "You were killed by a gunshot", image_file="gun_firing", chapters=['sunday_afternoon']),
            CharacterInformation(1, "poisoned", "You were poisoned at luncheon on Sunday", image_file="poison_food", chapters=['sunday_afternoon']),
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
            endings = nurse_endings,
            observations = nurse_observations,
            objects = nurse_objects,
            progress = nurse_progress,
            saved_variables = copy.deepcopy(nurse_init_variables),
            test_checkpoints = nurse_test_checkpoints,
        )
        nurse = Character("nurse_details.get_name()", image="nurse", dynamic=True)

    return