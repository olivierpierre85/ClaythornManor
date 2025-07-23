label doctor_config_map:
    python:        
        # Map choices
        doctor_day1_evening_map_menu = TimedMenu(
            "doctor_day1_evening_map_menu", 
            [
            # Default values
            TimedMenuChoice(default_room_text('storage'), 'doctor_day1_evening_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'doctor_day1_evening_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'doctor_day1_evening_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'doctor_day1_evening_butler_room', 10, room='butler_room'),
            TimedMenuChoice(default_room_text('bedroom_lad'), 'doctor_day1_evening_bedroom_lad', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'doctor_day1_evening_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'doctor_day1_evening_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'doctor_day1_evening_bedroom_drunk', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_broken'), 'doctor_day1_evening_bedroom_broken', 10, room='bedroom_broken'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'doctor_day1_evening_bedroom_nurse', 10, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('library'), 'doctor_day1_evening_library', 10, room='library'),
            TimedMenuChoice(default_room_text('tea_room'), 'doctor_day1_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'doctor_day1_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'doctor_day1_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'doctor_day1_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'doctor_day1_evening_portrait_gallery', 10, room='portrait_gallery'),
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'doctor_day1_evening_downstairs_default', 0, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'doctor_day1_evening_downstairs_default', 0, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'doctor_day1_evening_downstairs_default', 0, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'doctor_day1_evening_downstairs_default', 0, room='gun_room'),
            # Specific actions
            TimedMenuChoice(
                default_room_text('bedroom_psychic'), 
                'doctor_day1_evening_bedroom_psychic', 
                10, 
                room = 'bedroom_psychic'
            ),
            TimedMenuChoice(
                'Meet the others in the billiard room', 
                'doctor_day1_evening_billiard_room', 
                0, 
                keep_alive = True, 
                room = 'billiard_room',
                next_menu = 'doctor_day1_evening_billiard_room_menu'
            ),
            TimedMenuChoice(
                'Go to sleep', 
                'generic_cancel', 
                early_exit = True, 
                room = 'bedroom_doctor'
            )
        ], is_map = True)