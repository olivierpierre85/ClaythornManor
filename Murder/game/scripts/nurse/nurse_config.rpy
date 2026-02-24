label init_nurse:

    call nurse_day1_evening_map_menu
    
    call nurse_config_menu

    call nurse_config_progress

    python:
        nurse_name = "Rosalind Marsh"

        # Story Variables
        nurse_init_variables = {
            # MAP Menus
            # "day1_evening_map_menu" : nurse_day1_evening_map_menu,
            # "day2_no_hunt_map_menu" : nurse_day2_no_hunt_map_menu,

            # Generic Menus
            "drunk_generic_menu" : drunk_generic_menu_nurse,
            "drunk_generic_other_guests_menu" : drunk_generic_menu_nurse,
            
            # story var
        }

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
            important_choices = CharacterInformationList([]),
            endings = CharacterInformationList([]),
            observations = CharacterInformationList([]),
            objects = CharacterInformationList([]),
            progress = nurse_progress,
            saved_variables = copy.deepcopy(nurse_init_variables),
            test_checkpoints = nurse_test_checkpoints,
        )
        nurse = Character("nurse_details.get_name()", image="nurse", dynamic=True)

    return