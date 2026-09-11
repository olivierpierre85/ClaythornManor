label init_host:

    call host_config_progress

    call host_config_menu

    call host_day1_evening_map_menu

    call host_day2_evening_map_menu

    call host_day3_morning_map_menu

    python:
        host_name = "Lady Claythorn"

        host_init_variables = {
            # Generic Menus
            "drunk_generic_menu" : drunk_generic_menu_host,

            # MAP Menus
            "day1_evening_map_menu" : host_day1_evening_map_menu,
            "day2_evening_map_menu" : host_day2_evening_map_menu,
            "day3_morning_map_menu" : host_day3_morning_map_menu,

            "day1_evening_manning_spoken" : False,
            "day1_evening_moody_spoken" : False,
            "day1_evening_attic_tried" : False,

            # Sunday morning: first-visit framings, and the two doors that
            # the Captain opens with the master key
            "day3_morning_downstairs_visited" : False,
            "day3_morning_attic_visited" : False,
            "day3_morning_others_heard" : False,
            "day3_morning_manning_checked" : False,
            "day3_morning_nurse_checked" : False,
        }

        host_important_choices = CharacterImportantChoiceList([
            CharacterInformation(
                1, "addressed_manning_first",
                "You turned first to Mr Manning, on your left, at dinner",
                content_negative="You did not turn  first to Mr Manning, on your left, at dinner",
                image_file="drunk_character",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_evening'],
            ),
            CharacterInformation(
                2, "stayed_with_guests",
                "You sat up with your guests in the billiard room",
                content_negative="You left your guests to themselves for the whole evening",
                image_file="captain",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_evening'],
            ),
            CharacterInformation(
                3, "go_downstairs",
                "You went below stairs, where the mistress of the house has no business being",
                content_negative="You did not go below stairs",
                image_file="downstairs",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_evening'],
            ),
            CharacterInformation(
                4, "terrible_shot",
                "You fired at a sitting rabbit in front of Captain Sinha, and missed it by a yard",
                content_negative="You gave the rabbit to Captain Sinha rather than fire a second time",
                image_file="poor_shot",
                chapters=['saturday_afternoon'],
                relevant_chapters=['saturday_afternoon', 'saturday_evening'],
            ),
            CharacterInformation(
                5, "accused_butler",
                "You put the open bottle of rat poison to the butler, to his face",
                content_negative="You kept what you saw in the scullery to yourself",
                image_file="rat_poison",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(
                6, "trust_captain",
                "You told Captain Sinha what you truly are, and put yourself in his hands",
                content_negative="You told nobody in the house what you truly are",
                image_file="trust_captain",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(
                7, "bested_captain",
                "You answered Captain Sinha's accusation with your title, and he apologised before the whole house",
                content_negative="You did not best Captain Sinha before the other guests",
                image_file="captain_host_suspicion_name",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning'],
            ),
        ])

        host_observations = CharacterObservationList([
            CharacterInformation(
                1, "family_history",
                "You learned the family's real name and title",
                content_negative="You didn't learn the family's real name and title",
                image_file="captain_host_suspicion_name",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(
                2, "no_portrait",
                "You noticed there is no portrait of Lady Claythorn anywhere in the gallery",
                content_negative="You didn't visit the portrait gallery",
                image_file="captain_host_suspicion_portrait",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_evening'],
            ),
            CharacterInformation(
                1, "found_poison",
                "You found an open bottle of rat poison in the scullery",
                content_negative="You didn't go below stairs to the scullery",
                image_file="rat_poison",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_morning', 'saturday_afternoon', 'saturday_evening', 'sunday_morning', 'sunday_afternoon'],
            ),
            CharacterInformation(
                4, "seen_car",
                "You looked over the old tourer in the garage with Captain Sinha. The engine is sound, and the tank is dry",
                content_negative="You never went down to look at the old car in the garage",
                image_file="seen_car",
                chapters=['sunday_morning'],
                relevant_chapters=['sunday_morning', 'sunday_afternoon'],
            ),
        ])

        host_objects = CharacterObjectList([
            CharacterInformation(
                1, "petrol_tin",
                "You found a full tin of petrol in the garden shed, behind the butler's lock",
                content_negative="You found no petrol for the car",
                image_file="petrol_tin",
                chapters=['sunday_morning'],
                relevant_chapters=['sunday_morning', 'sunday_afternoon'],
            ),
            CharacterInformation(
                2, "provisions",
                "You packed what food was left in the kitchen into a basket for the road",
                content_negative="You left the kitchen as you found it",
                image_file="cutlery",   # TODO proper image, a basket of provisions
                chapters=['sunday_morning'],
                relevant_chapters=['sunday_morning', 'sunday_afternoon'],
            ),
        ])

        host_endings = CharacterEndingList([
            CharacterInformation(1, "shot_tea_room",
                "You were shot in the tea room when Captain Sinha went for the butler's revolver",
                image_file="gun_firing",
                chapters=['saturday_evening']),
            CharacterInformation(2, "die_in_sleep",
                "You died in your sleep, alone behind a locked door, on the second night",
                image_file="deathbed",
                chapters=['saturday_evening']),
            CharacterInformation(3, "shot_in_car",
                "The butler shot you on the forest road, in the car you took to be your way out",
                image_file="escape_car",
                chapters=['saturday_evening']),
            CharacterInformation(4, "escape",
                "You drove out of Claythorn Manor with Captain Sinha, and you did not look back",
                image_file="escape_car",
                chapters=['sunday_afternoon']),
            CharacterInformation(5, "run_over",
                "You set out on foot with Captain Sinha, and the butler's car met you on the forest road",
                image_file="run_over",
                chapters=['sunday_afternoon']),
            CharacterInformation(6, "shot_by_butler",
                "The butler came back for what he had left behind, and found you the only one left alive at the table",
                image_file="butler",
                chapters=['sunday_afternoon']),
        ])

        host_extra_information = CharacterDescriptionHiddenList ([
            CharacterInformation(0, "name_age", "Elisabeth - is born in 1865 and", is_important = True, unlock_chapters=[('host', 'friday_evening')]),
            CharacterInformation(1, "down_to_earth", "look down upon 'lower class' individuals", is_important = True), 
            CharacterInformation(60, "hunt", "cannot hunt at the level expected of a lady of her station", is_important = True, unlock_chapters=[('broken', 'saturday_afternoon'), ('captain', 'saturday_afternoon')]),
            CharacterInformation(60, "car", "to drive a car", is_important = True, unlock_chapters=[('nurse', 'saturday_evening'), ('host', 'sunday_afternoon')]),
            CharacterInformation(60, "table_manners", "table manners are not quite what they ought to be", unlock_chapters=[('captain', 'friday_evening')]),
            CharacterInformation(60, "lie", "a progressive aristocrat close to the people. She is, in fact, one of the people - an out-of-work actress playing her most dangerous role", is_important = True, unlock_chapters=[('captain', 'saturday_afternoon'), ('captain', 'saturday_evening')]),
            CharacterInformation(60, "not_guilty", "guilty, she is not the mastermind behind the whole operation. She is not even in charge of it, the butler is.", is_important = True, unlock_chapters=[('captain', 'saturday_evening')]),
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
        But as it turns out, she is not <info:lie>. Even if it makes her look <info:not_guilty>.
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
            endings = host_endings,
            observations = host_observations,
            objects = host_objects,
            progress = host_progress,
            saved_variables = copy.deepcopy(host_init_variables),
            test_checkpoints = host_test_checkpoints,
        )
        host = Character("host_details.get_name()", image="host", dynamic=True)
    
    return