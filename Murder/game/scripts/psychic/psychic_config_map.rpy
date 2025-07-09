label psychic_config_map:
    python:        
        # Map choices

        # LORD conditions, can happen at any time
        attic_visited = "psychic_details.observations.is_unlocked('visited_attic')"
        attic_not_visited = "not psychic_details.observations.is_unlocked('visited_attic')"

        knows_lord_name = "psychic_details.observations.is_unlocked('lord_name')"
        attic_visited_do_not_know_lord_name = "(psychic_details.observations.is_unlocked('visited_attic') and not psychic_details.observations.is_unlocked('lord_name'))"
        attic_default = "not psychic_details.observations.is_unlocked('lord_age')"
        attic_return = "psychic_details.observations.is_unlocked('lord_age')"

        attic_return_too_soon = "psychic_details.observations.is_unlocked('visited_attic') and not psychic_details.observations.is_unlocked('lord_age')"

        lord_choices = [
            TimedMenuChoice(default_room_text('library'), 'psychic_library_default', 10, room='library', condition=attic_not_visited),
            TimedMenuChoice(default_room_text('library'), 'psychic_library_look_for_lord_failed', 20, room='library',condition=attic_visited_do_not_know_lord_name),
            TimedMenuChoice(default_room_text('library'), 'psychic_library_look_for_lord_succeed', 30, room='library',condition=knows_lord_name),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'psychic_portrait_gallery_look_for_lord', 40, room='portrait_gallery',condition=attic_visited),   
            TimedMenuChoice(default_room_text('portrait_gallery'), 'psychic_portrait_gallery_default', 10, room='portrait_gallery',condition=attic_not_visited),   

            TimedMenuChoice("Return to the Attic", 'psychic_attic_return', 10, room='storage', condition=attic_return),
            TimedMenuChoice("Return to the Attic", 'psychic_attic_return', 10, room='males_room', condition=attic_return),
            TimedMenuChoice("Return to the Attic", 'psychic_attic_return', 10, room='females_room', condition=attic_return),
            TimedMenuChoice("Return to the Attic", 'psychic_attic_return', 10, room='butler_room',condition=attic_return),     
        ]

        # -------------------------
        # Friday
        # -------------------------
        psychic_day1_evening_map_menu= TimedMenu("psychic_day1_evening_map_menu", [
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'psychic_day1_evening_downstairs_default', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'psychic_day1_evening_downstairs_default', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'psychic_day1_evening_downstairs_default', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'psychic_day1_evening_downstairs_default', 10, room='gun_room'),
            # first floor
            TimedMenuChoice(default_room_text('tea_room'), 'psychic_tea_room_default', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'psychic_dining_room_default', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'psychic_day1_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'psychic_entrance_hall_default', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'psychic_day1_evening_portrait_gallery', 10, room='portrait_gallery'),
            #Bedrooms
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'psychic_day1_evening_default_bedroom', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'psychic_day1_evening_default_bedroom', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'psychic_day1_evening_default_bedroom', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'psychic_day1_evening_default_bedroom', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_broken'), 'psychic_day1_evening_default_bedroom', 10, room='bedroom_broken'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'psychic_day1_evening_default_bedroom', 10, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('bedroom_lad'), 'psychic_day1_evening_default_bedroom', 10, room='bedroom_lad'),
            # attic
            TimedMenuChoice(default_room_text('storage'), 'psychic_day1_evening_attic_default', 60, room='storage', condition=attic_default),
            TimedMenuChoice(default_room_text('males_room'), 'psychic_day1_evening_attic_default', 60, room='males_room', condition=attic_default),
            TimedMenuChoice(default_room_text('females_room'), 'psychic_day1_evening_attic_default', 60, room='females_room', condition=attic_default),
            TimedMenuChoice(default_room_text('butler_room'), 'psychic_day1_evening_attic_default', 60, room='butler_room', condition=attic_default),

            # Specific actions
            TimedMenuChoice(
                'Go to bed', 
                'generic_cancel', 
                room = 'bedroom_psychic', 
                early_exit = True
            ),
            TimedMenuChoice(
                'Meet the others in the billiard room', 
                'psychic_day1_evening_billiard_room', 
                0, 
                keep_alive = True, 
                room = 'billiard_room'
            ),
        ] + copy.deepcopy(lord_choices)
        , is_map = True)

        # -------------------------
        # Saturday, During the Hunt
        # -------------------------        
        psychic_day2_no_hunt_map_menu = TimedMenu("psychic_day2_no_hunt_map_menu", [
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'psychic_day2_no_hunt_downstairs_default', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'psychic_day2_no_hunt_downstairs_default', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'psychic_day2_no_hunt_downstairs_default', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'psychic_day2_no_hunt_downstairs_default', 10, room='gun_room'),
            # first floor
            TimedMenuChoice(default_room_text('billiard_room'), 'psychic_billiard_room_default', 10, room='billiard_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'psychic_dining_room_default', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'psychic_garden_default', 30, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'psychic_entrance_hall_default', 10, room='entrance_hall'),
            # Bedrooms 
            TimedMenuChoice(default_room_text('bedroom_lad'), 'psychic_day2_no_hunt_bedroom_lad', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'psychic_day2_no_hunt_bedroom_doctor', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'psychic_day2_no_hunt_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 'psychic_day2_no_hunt_bedroom_psychic', 10, room='bedroom_psychic'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'psychic_day2_no_hunt_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'psychic_day2_no_hunt_bedroom_drunk', 10, room='bedroom_drunk'),
            # attic
            TimedMenuChoice(default_room_text('storage'), 'psychic_day2_no_hunt_attic_default', 60, room='storage', condition=attic_default),
            TimedMenuChoice(default_room_text('males_room'), 'psychic_day2_no_hunt_attic_default', 60, room='males_room', condition=attic_default),
            TimedMenuChoice(default_room_text('females_room'), 'psychic_day2_no_hunt_attic_default', 60, room='females_room', condition=attic_default),
            TimedMenuChoice(default_room_text('butler_room'), 'psychic_day2_no_hunt_attic_default', 60, room='butler_room', condition=attic_default),
            
            TimedMenuChoice(default_room_text('storage'), 'psychic_day2_no_hunt_attic_return_too_soon', 10, room='storage', condition=attic_return_too_soon),
            TimedMenuChoice(default_room_text('males_room'), 'psychic_day2_no_hunt_attic_return_too_soon', 10, room='males_room', condition=attic_return_too_soon),
            TimedMenuChoice(default_room_text('females_room'), 'psychic_day2_no_hunt_attic_return_too_soon', 10, room='females_room', condition=attic_return_too_soon),
            TimedMenuChoice(default_room_text('butler_room'), 'psychic_day2_no_hunt_attic_return_too_soon', 10, room='butler_room', condition=attic_return_too_soon),

            TimedMenuChoice(default_room_text('bedroom_nurse'), 
                'psychic_day2_no_hunt_bedroom_nurse_busy', 
                10, 
                room='bedroom_nurse',
                condition = "psychic_details.saved_variables['day2_nohunt_has_visited_tea_room']"
            ),
            TimedMenuChoice(
                default_room_text('bedroom_nurse'),
                'psychic_day2_no_hunt_bedroom_nurse',
                15, 
                room='bedroom_nurse',
                condition = "not psychic_details.saved_variables['day2_nohunt_has_visited_tea_room']"
            ),
            TimedMenuChoice(
                'Meet Rosalind Marsh in the Tea Room', 
                'psychic_day2_hunt_tea_room', 
                150, 
                room = 'tea_room'
            ),
            # Not needed right now
            # TimedMenuChoice(
            #     'Go back to the Tea Room', 
            #     'psychic_tea_room_default',  
            #     room = 'tea_room',
            #     condition = "psychic_details.saved_variables['day2_nohunt_has_visited_tea_room']",
            #     keep_alive = True, 
            # ),
            TimedMenuChoice(
                'Wait in your room the others return', 
                'psychic_day2_no_hunt_cancel', 
                240, 
                early_exit = True, 
                room = 'bedroom_psychic'
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'psychic_day2_bedroom_broken', 
                20, 
                room = 'bedroom_broken',
            )
        ] + copy.deepcopy(lord_choices), 
        is_map = True)

        psychic_day2_evening_map_menu = TimedMenu("psychic_day2_evening_map_menu", [
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'psychic_day2_evening_downstairs_default', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'psychic_day2_evening_downstairs_default', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'psychic_day2_evening_downstairs_default', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'psychic_day2_evening_downstairs_default', 10, room='gun_room'),
            # first floor
            TimedMenuChoice(default_room_text('tea_room'), 'psychic_tea_room_default', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'psychic_dining_room_default', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'psychic_day2_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'psychic_entrance_hall_default', 10, room='entrance_hall'),
            # Bedrooms 
            TimedMenuChoice(default_room_text('bedroom_lad'), 'psychic_day2_evening_bedroom_lad', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'psychic_day2_evening_bedroom_doctor', 20, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'psychic_day2_evening_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'psychic_day2_evening_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'psychic_day2_evening_bedroom_drunk', 10, room='bedroom_drunk'),
            # attic
            TimedMenuChoice(default_room_text('storage'), 'psychic_day2_evening_attic_default', 10, room='storage', condition=attic_default),
            TimedMenuChoice(default_room_text('males_room'), 'psychic_day2_evening_attic_default', 10, room='males_room', condition=attic_default),
            TimedMenuChoice(default_room_text('females_room'), 'psychic_day2_evening_attic_default', 10, room='females_room', condition=attic_default),
            TimedMenuChoice(default_room_text('butler_room'), 'psychic_day2_evening_attic_default', 10, room='butler_room', condition=attic_default),

            TimedMenuChoice(default_room_text('storage'), 'psychic_day2_evening_attic_return_too_soon', 10, room='storage', condition=attic_return_too_soon),
            TimedMenuChoice(default_room_text('males_room'), 'psychic_day2_evening_attic_return_too_soon', 10, room='males_room', condition=attic_return_too_soon),
            TimedMenuChoice(default_room_text('females_room'), 'psychic_day2_evening_attic_return_too_soon', 10, room='females_room', condition=attic_return_too_soon),
            TimedMenuChoice(default_room_text('butler_room'), 'psychic_day2_evening_attic_return_too_soon', 10, room='butler_room', condition=attic_return_too_soon),

            TimedMenuChoice(
                'Check if there is someone in the Billiard Room', 
                'psychic_day2_evening_billiard_room', 
                10, 
                room = 'billiard_room',
                keep_alive = True, 
            ),

            # TimedMenuChoice(
            #     default_room_text('bedroom_nurse'),
            #     'psychic_day2_no_hunt_bedroom_nurse',
            #     20, 
            #     room='bedroom_nurse',
            #     condition = "not psychic_details.saved_variables['day2_nohunt_has_visited_tea_room']"
            # ),

            TimedMenuChoice(
                'Wait in your room for Ted Harring', 
                'psychic_day2_evening_cancel', 
                0, 
                early_exit = True, 
                room = 'bedroom_psychic',
                condition = "psychic_details.important_choices.is_unlocked('visit_lad')"
            ),
            TimedMenuChoice(
                'Wait in your room', 
                'psychic_day2_evening_cancel', 
                0, 
                early_exit = True, 
                room = 'bedroom_psychic',
                condition = "not psychic_details.important_choices.is_unlocked('visit_lad')"
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'psychic_day2_bedroom_broken', 
                20, 
                room = 'bedroom_broken',
                condition = "psychic_details.saved_variables['day2_has_seen_bedroom_broken'] == False"
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'psychic_day2_bedroom_broken_already_see', 
                20, 
                room = 'bedroom_broken',
                condition = "psychic_details.saved_variables['day2_has_seen_bedroom_broken'] == True"
            )
        ] + copy.deepcopy(lord_choices), 
        is_map = True)
    return