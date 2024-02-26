label psychic_config_map:
    python:        
        # Map choices

        # LORD conditions, can happen at any time
        attic_visited = "psychic_details.saved_variables['attic_visited']"
        attic_not_visited = "psychic_details.saved_variables['attic_visited']==False"

        knows_lord_name = "psychic_details.saved_variables['knows_lord_name']"
        attic_visited_do_not_know_lord_name = "(psychic_details.saved_variables['attic_visited'] and psychic_details.saved_variables['knows_lord_name']==False)"
        attic_default = "psychic_details.observations.is_unlocked('lord')==False"
        attic_return = "psychic_details.observations.is_unlocked('lord')"

        lord_choices = [
            TimedMenuChoice(default_room_text('library'), 'psychic_library_default', 10, room='library', condition=attic_not_visited),
            TimedMenuChoice(default_room_text('library'), 'psychic_library_look_for_lord_failed', 20, room='library',condition=attic_visited_do_not_know_lord_name),
            TimedMenuChoice(default_room_text('library'), 'psychic_library_look_for_lord_succeed', 20, room='library',condition=knows_lord_name),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'psychic_portrait_gallery_look_for_lord', 20, room='portrait_gallery',condition=attic_visited),   
            TimedMenuChoice(default_room_text('portrait_gallery'), 'psychic_portrait_gallery_default', 10, room='portrait_gallery',condition=attic_not_visited),   

            TimedMenuChoice("Return to the Attic", 'psychic_attic_return', 10, room='storage', condition=attic_return),
            TimedMenuChoice("Return to the Attic", 'psychic_attic_return', 10, room='males_room', condition=attic_return),
            TimedMenuChoice("Return to the Attic", 'psychic_attic_return', 10, room='females_room', condition=attic_return),
            TimedMenuChoice("Return to the Attic", 'psychic_attic_return', 10, room='butler_room', condition=attic_return),     
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
            TimedMenuChoice(default_room_text('doctor_room'), 'psychic_day1_evening_default_bedroom', 10, room='doctor_room'),
            TimedMenuChoice(default_room_text('captain_room'), 'psychic_day1_evening_default_bedroom', 10, room='captain_room'),
            TimedMenuChoice(default_room_text('host_room'), 'psychic_day1_evening_default_bedroom', 10, room='host_room'),
            TimedMenuChoice(default_room_text('drunk_room'), 'psychic_day1_evening_default_bedroom', 10, room='drunk_room'),
            TimedMenuChoice(default_room_text('broken_room'), 'psychic_day1_evening_default_bedroom', 10, room='broken_room'),
            TimedMenuChoice(default_room_text('nurse_room'), 'psychic_day1_evening_default_bedroom', 10, room='nurse_room'),
            TimedMenuChoice(default_room_text('lad_room'), 'psychic_day1_evening_default_bedroom', 10, room='lad_room'),
            # attic
            TimedMenuChoice(default_room_text('storage'), 'psychic_day1_evening_attic_default', 10, room='storage', condition=attic_default),
            TimedMenuChoice(default_room_text('males_room'), 'psychic_day1_evening_attic_default', 10, room='males_room', condition=attic_default),
            TimedMenuChoice(default_room_text('females_room'), 'psychic_day1_evening_attic_default', 10, room='females_room', condition=attic_default),
            TimedMenuChoice(default_room_text('butler_room'), 'psychic_day1_evening_attic_default', 10, room='butler_room', condition=attic_default),

            # Specific actions
            TimedMenuChoice(
                'Go to bed', 
                'generic_cancel', 
                room = 'psychic_room', 
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
            TimedMenuChoice(default_room_text('lad_room'), 'psychic_day2_no_hunt_lad_room', 10, room='lad_room'),
            TimedMenuChoice(default_room_text('doctor_room'), 'psychic_day2_no_hunt_doctor_room', 10, room='doctor_room'),
            TimedMenuChoice(default_room_text('captain_room'), 'psychic_day2_no_hunt_captain_room', 10, room='captain_room'),
            TimedMenuChoice(default_room_text('psychic_room'), 'psychic_day2_no_hunt_psychic_room', 10, room='psychic_room'),
            TimedMenuChoice(default_room_text('host_room'), 'psychic_day2_no_hunt_host_room', 10, room='host_room'),
            TimedMenuChoice(default_room_text('drunk_room'), 'psychic_day2_no_hunt_drunk_room', 10, room='drunk_room'),
            # attic
            TimedMenuChoice(default_room_text('storage'), 'psychic_day2_no_hunt_attic_default', 10, room='storage', condition=attic_default),
            TimedMenuChoice(default_room_text('males_room'), 'psychic_day2_no_hunt_attic_default', 10, room='males_room', condition=attic_default),
            TimedMenuChoice(default_room_text('females_room'), 'psychic_day2_no_hunt_attic_default', 10, room='females_room', condition=attic_default),
            TimedMenuChoice(default_room_text('butler_room'), 'psychic_day2_no_hunt_attic_default', 10, room='butler_room', condition=attic_default),

            TimedMenuChoice(default_room_text('nurse_room'), 
                'psychic_day2_no_hunt_nurse_room_busy', 
                10, 
                room='nurse_room',
                condition = "psychic_details.saved_variables['day2_nohunt_has_visited_tea_room']"
            ),
            TimedMenuChoice(
                default_room_text('nurse_room'),
                'psychic_day2_no_hunt_nurse_room',
                15, 
                room='nurse_room',
                condition = "psychic_details.saved_variables['day2_nohunt_has_visited_tea_room']==False"
            ),
            TimedMenuChoice(
                'Meet Rosalind Marsh in the Tea Room', 
                'psychic_day2_hunt_tea_room', 
                120, 
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
                room = 'psychic_room'
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'psychic_day2_broken_room', 
                20, 
                room = 'broken_room',
            )
        ] + copy.deepcopy(lord_choices), 
        is_map = True)
        
    return