label psychic_config_map:
    python:        
        # Map choices

        # -------------------------
        # Friday
        # -------------------------
        psychic_day1_evening_map_menu= TimedMenu("psychic_day1_evening_map_menu", [
            # Default values
            TimedMenuChoice(default_room_text('storage'), 'psychic_day1_evening_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'psychic_day1_evening_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'psychic_day1_evening_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'psychic_day1_evening_butler_room', 10, room='butler_room'),
            TimedMenuChoice(default_room_text('doctor_room'), 'psychic_day1_evening_doctor_room', 10, room='doctor_room'),
            TimedMenuChoice(default_room_text('captain_room'), 'psychic_day1_evening_captain_room', 10, room='captain_room'),
            TimedMenuChoice(default_room_text('host_room'), 'psychic_day1_evening_host_room', 10, room='host_room'),
            TimedMenuChoice(default_room_text('drunk_room'), 'psychic_day1_evening_drunk_room', 10, room='drunk_room'),
            TimedMenuChoice(default_room_text('broken_room'), 'psychic_day1_evening_broken_room', 10, room='broken_room'),
            TimedMenuChoice(default_room_text('nurse_room'), 'psychic_day1_evening_nurse_room', 10, room='nurse_room'),
            TimedMenuChoice(default_room_text('lad_room'), 'psychic_day1_evening_lad_room', 10, room='lad_room'),
            TimedMenuChoice(default_room_text('library'), 'psychic_day1_evening_library', 10, room='library'),
            TimedMenuChoice(default_room_text('tea_room'), 'psychic_day1_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'psychic_day1_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'psychic_day1_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'psychic_day1_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'psychic_day1_evening_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('kitchen'), 'psychic_day1_evening_kitchen', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'psychic_day1_evening_scullery', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'psychic_day1_evening_garage', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'psychic_day1_evening_gun_room', 10, room='gun_room'),
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
        ], is_map = True)

    return