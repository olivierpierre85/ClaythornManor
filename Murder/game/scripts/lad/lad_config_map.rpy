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

        # -------------------------
        # Friday
        # -------------------------
        lad_day1_evening_map_menu = TimedMenu(
            "lad_day1_evening_map_menu", 
            [
            # Default values
            TimedMenuChoice(default_room_text('storage'), 'lad_day1_evening_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'lad_day1_evening_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'lad_day1_evening_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'lad_day1_evening_butler_room', 10, room='butler_room'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'lad_day1_evening_bedroom_doctor', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'lad_day1_evening_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'lad_day1_evening_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'lad_day1_evening_bedroom_drunk', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_broken'), 'lad_day1_evening_bedroom_broken', 10, room='bedroom_broken'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'lad_day1_evening_bedroom_nurse', 10, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('library'), 'lad_day1_evening_library', 10, room='library'),
            TimedMenuChoice(default_room_text('tea_room'), 'lad_day1_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'lad_day1_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'lad_day1_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'lad_day1_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'lad_day1_evening_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('kitchen'), 'lad_day1_evening_kitchen', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'lad_day1_evening_scullery', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'lad_day1_evening_garage', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'lad_day1_evening_gun_room', 10, room='gun_room'),
            # Specific actions
            TimedMenuChoice(
                default_room_text('bedroom_psychic'), 
                'lad_day1_evening_bedroom_psychic', 
                10, 
                room = 'bedroom_psychic'
            ),
            TimedMenuChoice(
                'Meet the others in the billiard room', 
                'lad_day1_evening_billiard_room', 
                0, 
                keep_alive = True, 
                room = 'billiard_room'
            ),
            TimedMenuChoice(
                'Go to sleep', 
                'generic_cancel', 
                early_exit = True, 
                room = 'bedroom_lad'
            )
        ], is_map = True)

        # -------------------------
        # Saturday, During the Hunt
        # -------------------------        
        lad_day2_no_hunt_map_menu = TimedMenu("lad_day2_no_hunt_map_menu", [
            TimedMenuChoice(default_room_text('storage'), 'lad_day2_no_hunt_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'lad_day2_no_hunt_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'lad_day2_no_hunt_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'lad_day2_no_hunt_butler_room', 10, room='butler_room'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'lad_day2_no_hunt_bedroom_doctor', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'lad_day2_no_hunt_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 'lad_day2_no_hunt_bedroom_psychic', 10, room='bedroom_psychic'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'lad_day2_no_hunt_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'lad_day2_no_hunt_bedroom_drunk', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('library'), 'lad_day2_no_hunt_library', 10, room='library'),
            TimedMenuChoice(default_room_text('billiard_room'), 'lad_day2_no_hunt_billiard_room', 10, room='billiard_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'lad_day2_no_hunt_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'lad_day2_no_hunt_garden', 30, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'lad_day2_no_hunt_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'lad_day2_no_hunt_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('kitchen'), 'lad_day2_no_hunt_kitchen', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'lad_day2_no_hunt_scullery', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'lad_day2_no_hunt_garage', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'lad_day2_no_hunt_gun_room', 10, room='gun_room'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 
                'lad_day2_no_hunt_bedroom_nurse_busy', 
                10, 
                room='bedroom_nurse',
                condition = "lad_details.saved_variables['day2_nohunt_has_visited_tea_room']"
            ),
            TimedMenuChoice(
                default_room_text('bedroom_nurse'),
                'lad_day2_no_hunt_bedroom_nurse',
                15, 
                room='bedroom_nurse',
                condition = "not lad_details.saved_variables['day2_nohunt_has_visited_tea_room']"
            ),
            TimedMenuChoice(
                'Meet the others in the Tea Room', 
                'lad_day2_hunt_tea_room', 
                120, 
                room = 'tea_room',
                keep_alive = True, 
            ),
            TimedMenuChoice(
                'Go back to the Tea Room', 
                'lad_day2_hunt_tea_room_return',  
                room = 'tea_room',
                condition = "lad_details.saved_variables['day2_nohunt_has_visited_tea_room']",
                keep_alive = True, 
            ),
            TimedMenuChoice(
                'Take a nap until the others return', 
                'lad_day2_no_hunt_cancel', 
                240, 
                early_exit = True, 
                room = 'bedroom_lad'
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'lad_day2_bedroom_broken', 
                20, 
                room = 'bedroom_broken',
            )
        ], is_map = True)
        # -------------------------
        # Saturday, Evening
        # -------------------------
        lad_day2_evening_map_menu = TimedMenu("lad_day2_evening_map_menu", [
            TimedMenuChoice(default_room_text('storage'), 'lad_day2_evening_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'lad_day2_evening_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'lad_day2_evening_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'lad_day2_evening_butler_room', 10, room='butler_room'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'lad_day2_evening_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'lad_day2_evening_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'lad_day2_evening_bedroom_drunk', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'lad_day2_evening_bedroom_nurse', 10, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('library'), 'lad_day2_evening_library', 10, room='library'),
            TimedMenuChoice(default_room_text('tea_room'), 'lad_day2_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'lad_day2_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'lad_day2_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'lad_day2_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'lad_day2_evening_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('kitchen'), 'lad_day2_evening_kitchen', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'lad_day2_evening_scullery', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'lad_day2_evening_garage', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'lad_day2_evening_gun_room', 10, room='gun_room'),
            TimedMenuChoice(
                default_room_text('bedroom_doctor'), 
                'lad_day2_bedroom_doctor', 
                20, 
                room = 'bedroom_doctor',
            ),
            TimedMenuChoice(
                'Go to sleep and hope for the best.', 
                'lad_day2_evening_sleep',
                early_exit = True, 
                room = 'bedroom_lad',
            ),
            TimedMenuChoice(
                'Have a talk with Amelia Baxter', 
                'lad_day2_evening_bedroom_psychic',
                20,
                room = 'bedroom_psychic',
            ),
            TimedMenuChoice(
                'Check if there is someone in the Billiard Room', 
                'lad_day2_evening_billiard_room', 
                0, 
                room = 'billiard_room',
                keep_alive = True, 
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'lad_day2_bedroom_broken', 
                20, 
                room = 'bedroom_broken',
                condition="not lad_details.observations.is_unlocked('green_liquid')"
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'lad_day2_bedroom_broken_back', 
                10, 
                room = 'bedroom_broken',
                condition="lad_details.observations.is_unlocked('green_liquid')"
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'lad_day2_bedroom_broken_back_for_drink', 
                10, 
                room = 'bedroom_broken',
                condition = 'lad_details.saved_variables["day2_evening_taste_from_flask"]'
            ),
        ], is_map = True)    

        # -------------------------
        # Sunday Search MAX 250 !
        # -------------------------
        lad_day3_morning_map_menu = TimedMenu("lad_day3_morning_map_menu", [
            TimedMenuChoice(default_room_text('library'), 'lad_day3_morning_library', 10, room='library'),
            TimedMenuChoice(default_room_text('tea_room'), 'lad_day3_morning_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'lad_day3_morning_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'lad_day3_morning_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'lad_day3_morning_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'lad_day3_morning_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('billiard_room'), 'lad_day3_morning_billiard_room', 10, room='billiard_room'),
            TimedMenuChoice(default_room_text('storage'), 'lad_day3_morning_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'lad_day3_morning_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'lad_day3_morning_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'lad_day3_morning_butler_room', 10, room='butler_room'),
            TimedMenuChoice(
                default_room_text('bedroom_lad'), 
                'lad_day3_morning_bedroom_lad',
                10,
                room = 'bedroom_lad'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_psychic'), 
                'lad_day3_morning_bedroom_psychic',
                10,
                room = 'bedroom_psychic'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_drunk'), 
                'lad_day3_morning_bedroom_drunk',
                10,
                room = 'bedroom_drunk'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_doctor'), 
                'lad_day3_morning_bedroom_doctor',
                10,
                room = 'bedroom_doctor'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_broken'), 
                'lad_day3_morning_bedroom_broken',
                10,
                room = 'bedroom_broken'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_captain'), 
                'lad_day3_morning_bedroom_captain',
                10,
                room = 'bedroom_captain'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_host'), 
                'lad_day3_morning_bedroom_host', 
                20, 
                room = 'bedroom_host'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_nurse'), 
                'lad_day3_morning_bedroom_nurse', 
                20, 
                room = 'bedroom_nurse'
            ),                  
            TimedMenuChoice(
                default_room_text('kitchen'), 
                'lad_day3_morning_kitchen', 
                10, 
                room = 'kitchen'
            ),
            TimedMenuChoice(
                default_room_text('scullery'), 
                'lad_day3_morning_scullery', 
                10, 
                room = 'scullery'
            ),
            TimedMenuChoice(
                default_room_text('garage'), 
                'lad_day3_morning_garage', 
                10, 
                room = 'garage'
            ),
            TimedMenuChoice(
                default_room_text('gun_room'), 
                'lad_day3_morning_gun_room', 
                0, 
                room = 'gun_room'
            ),
            TimedMenuChoice(
                'Go wait for Sushil', 
                'generic_cancel', 
                early_exit = True, 
                room = 'tea_room', 
                condition = 'lad_details.saved_variables["day3_morning_captain_found"]'
            ),

        ], is_map = True)

    return