label lad_config_map:
    python:        
        # Map choices
        # TODO BEFORE REWRITE VAR, check it exists, and if some fields are already hidden
        # => change those fields to special var that will display an icon, or another style
        # for already visited path
        # https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=25453&p=313338&hilit=caption.replace#p313338


        condition_friday = "current_day == 'Friday'"
        condition_saturday_evening = "(current_day == 'Saturday' and current_phase == 'Evening')"
        condition_saturday_hunt = "(current_day == 'Saturday' and current_phase == 'Hunt')"
        condition_sunday = "(current_day == 'Sunday' and current_phase == 'Morning')"

        lad_map_menu = TimedMenu([
            # -------------------------
            # Friday
            # -------------------------
            # Default values
            TimedMenuChoice(default_room_text('storage'), 'lad_day1_evening_storage', 10, room='storage', condition=condition_friday),
            TimedMenuChoice(default_room_text('males_room'), 'lad_day1_evening_males_room', 10, room='males_room', condition=condition_friday),
            TimedMenuChoice(default_room_text('females_room'), 'lad_day1_evening_females_room', 10, room='females_room', condition=condition_friday),
            TimedMenuChoice(default_room_text('butler_room'), 'lad_day1_evening_butler_room', 10, room='butler_room', condition=condition_friday),
            TimedMenuChoice(default_room_text('doctor_room'), 'lad_day1_evening_doctor_room', 10, room='doctor_room', condition=condition_friday),
            TimedMenuChoice(default_room_text('captain_room'), 'lad_day1_evening_captain_room', 10, room='captain_room', condition=condition_friday),
            TimedMenuChoice(default_room_text('host_room'), 'lad_day1_evening_host_room', 10, room='host_room', condition=condition_friday),
            TimedMenuChoice(default_room_text('drunk_room'), 'lad_day1_evening_drunk_room', 10, room='drunk_room', condition=condition_friday),
            TimedMenuChoice(default_room_text('broken_room'), 'lad_day1_evening_broken_room', 10, room='broken_room', condition=condition_friday),
            TimedMenuChoice(default_room_text('nurse_room'), 'lad_day1_evening_nurse_room', 10, room='nurse_room', condition=condition_friday),
            TimedMenuChoice(default_room_text('library'), 'lad_day1_evening_library', 10, room='library', condition=condition_friday),
            TimedMenuChoice(default_room_text('tea_room'), 'lad_day1_evening_tea_room', 10, room='tea_room', condition=condition_friday),
            TimedMenuChoice(default_room_text('dining_room'), 'lad_day1_evening_dining_room', 10, room='dining_room', condition=condition_friday),
            TimedMenuChoice(default_room_text('garden'), 'lad_day1_evening_garden', 10, room='garden', condition=condition_friday),
            TimedMenuChoice(default_room_text('entrance_hall'), 'lad_day1_evening_entrance_hall', 10, room='entrance_hall', condition=condition_friday),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'lad_day1_evening_portrait_gallery', 10, room='portrait_gallery', condition=condition_friday),
            TimedMenuChoice(default_room_text('kitchen'), 'lad_day1_evening_kitchen', 10, room='kitchen', condition=condition_friday),
            TimedMenuChoice(default_room_text('scullery'), 'lad_day1_evening_scullery', 10, room='scullery', condition=condition_friday),
            TimedMenuChoice(default_room_text('garage'), 'lad_day1_evening_garage', 10, room='garage', condition=condition_friday),
            TimedMenuChoice(default_room_text('gun_room'), 'lad_day1_evening_gun_room', 10, room='gun_room', condition=condition_friday),
            # Specific actions
            TimedMenuChoice(
                default_room_text('psychic_room'), 
                'lad_day1_evening_psychic_room', 
                10, 
                room = 'psychic_room', 
                condition = condition_friday
            ),
            TimedMenuChoice(
                default_room_text('garden'), 
                'lad_day1_evening_garden', 
                5, 
                room = 'garden', 
                condition = condition_friday
            ),
            TimedMenuChoice(
                'Meet the others in the billiard room', 
                'lad_day1_evening_billiard_room', 
                0, 
                keep_alive = True, 
                room = 'billiard_room', 
                condition = condition_friday
            ),
            TimedMenuChoice(
                'Go to sleep', 
                'generic_cancel', 
                early_exit = True, 
                room = 'lad_room',
                condition = condition_friday
            ),
            # -------------------------
            # Saturday, During the Hunt
            # -------------------------
            TimedMenuChoice(
                'Meet the others in the Tea Room', 
                'lad_day2_hunt_tea_room', 
                120, 
                room = 'tea_room',
                condition = condition_saturday_hunt,
                keep_alive = True, 
            ),
            TimedMenuChoice(
                'Go back to the Tea Room', 
                'lad_day2_hunt_tea_room_return',  
                room = 'tea_room',
                condition = condition_saturday_hunt + " and " + "lad_details.saved_variables['day2_nohunt_has_visited_tea_room']",
                keep_alive = True, 
            ),
            TimedMenuChoice(
                'Take a nap until the others return', 
                'lad_day2_no_hunt_cancel', 
                240, 
                early_exit = True, 
                room = 'lad_room',
                condition = condition_saturday_hunt
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'lad_day2_broken_room', 
                20, 
                room = 'broken_room',
                condition = condition_saturday_hunt + " or " + condition_saturday_evening
            ),
            # -------------------------
            # Saturday, Evening
            # -------------------------
            TimedMenuChoice(
                default_room_text('doctor_room'), 
                'lad_day2_doctor_room', 
                20, 
                room = 'doctor_room',
                condition = condition_saturday_evening
            ),
            TimedMenuChoice(
                'Go to sleep and hope for the best.', 
                'lad_day2_evening_sleep',
                early_exit = True, 
                room = 'lad_room',
                condition = condition_saturday_evening
            ),
            TimedMenuChoice(
                'Have a talk with Amelia Baxter', 
                'lad_day2_evening_psychic_room',
                20,
                room = 'psychic_room',
                condition = condition_saturday_evening
            ),
            TimedMenuChoice(
                'Check if there is someone in the Billiard Room', 
                'lad_day2_evening_billiard_room', 
                10, 
                room = 'billiard_room',
                condition = condition_saturday_evening,
                keep_alive = True, 
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'lad_day2_broken_room_back', 
                10, 
                room = 'broken_room',
                condition = 'lad_details.saved_variables["day2_evening_taste_from_flask"]'
            ),
            # -------------------------
            # Sunday Search
            # -------------------------
            TimedMenuChoice(
                default_room_text('lad_room'), 
                'lad_day3_morning_lad_room',
                10,
                room = 'lad_room',
                condition = condition_sunday
            ),
            TimedMenuChoice(
                default_room_text('psychic_room'), 
                'lad_day3_morning_psychic_room',
                10,
                room = 'psychic_room',
                condition = condition_sunday
            ),
            TimedMenuChoice(
                default_room_text('drunk_room'), 
                'lad_day3_morning_drunk_room',
                10,
                room = 'drunk_room',
                condition = condition_sunday
            ),
            TimedMenuChoice(
                default_room_text('doctor_room'), 
                'lad_day3_morning_doctor_room',
                10,
                room = 'doctor_room',
                condition = condition_sunday
            ),
            TimedMenuChoice(
                default_room_text('broken_room'), 
                'lad_day3_morning_broken_room',
                10,
                room = 'broken_room',
                condition = condition_sunday
            ),
            TimedMenuChoice(
                default_room_text('captain_room'), 
                'lad_day3_morning_captain_room',
                10,
                room = 'captain_room',
                condition = condition_sunday
            ),
            TimedMenuChoice(
                default_room_text('host_room'), 
                'lad_day3_morning_host_room', 
                20, 
                room = 'host_room',
                condition = condition_sunday
            ),
            TimedMenuChoice(
                default_room_text('nurse_room'), 
                'lad_day3_morning_nurse_room', 
                20, 
                room = 'nurse_room',
                condition = condition_sunday
            ),                  
            TimedMenuChoice(
                default_room_text('kitchen'), 
                'lad_day3_morning_kitchen', 
                10, 
                room = 'kitchen',
                condition = condition_sunday
            ),
            TimedMenuChoice(
                default_room_text('scullery'), 
                'lad_day3_morning_scullery', 
                10, 
                room = 'scullery',
                condition = condition_sunday
            ),
            TimedMenuChoice(
                default_room_text('garage'), 
                'lad_day3_morning_garage', 
                10, 
                room = 'garage',
                condition = condition_sunday
            ),
            TimedMenuChoice(
                default_room_text('gun_room'), 
                'lad_day3_morning_gun_room', 
                10, 
                room = 'gun_room',
                condition = condition_sunday
            ),
            TimedMenuChoice(
                'Go wait for Sushil', 
                'generic_cancel', 
                early_exit = True, 
                room = 'tea_room', 
                condition = 'lad_details.saved_variables["day3_morning_captain_found"]'
            ),
            # -------------------------
            # Generic choices
            # -------------------------
            TimedMenuChoice(
                default_room_text('library'), 
                'lad_library', 
                20, 
                room = 'library',
                condition = "(not current_day == 'Sunday')"
            ),
            TimedMenuChoice(
                default_room_text('library'), 
                'lad_library_visited', 
                20, 
                room = 'library',
                condition = "(not current_day == 'Sunday' and lad_details.saved_variables['library_visited'])"
            ),

        ], is_map = True)

    return