label init_lad:
    call change_time(17,00, 'Evening', 'Friday')

    python:
        # Story Variables
        lad_library_visited = False
        lad_has_met_maid = False
        psychic_generic_other_guests_saturday_morning_ask = False

        lad_day1_evening_billiard_room_visited = False
        lad_day1_drinks = 0
        lad_day1_poisoned = False
        lad_day1_drunk = False # Means he drank poison, but rejected it (used again on day 2 evening with the captain)

        lad_day2_breakfast_follow = False
        lad_day2_hunt = False
        lad_day2_saw_accident = False
        lad_day2_evening_billiard_room_visited = False
        lad_day2_nohunt_has_visited_tea_room = False
        lad_day2_believe_psychic = False
        lad_day2_drinks = 0
        lad_day2_drunk = False
        lad_day2_evening_billiard_room_captain_talked = False
        lad_day2_evening_taste_from_flask = False
        lad_day2_poisoned = False

        lad_day3_morning_captain_found = False
        lad_day3_gun_downed = False
        lad_day3_poisoned = False
        lad_day3_seen_car = False

        # Character Class
        lad_extra_information = [
            CharacterInformation(0, "background", "Born and raised in London.") , 
            CharacterInformation(2, "age", "He was 15 at the end of the war. That would make him 22 years old today."),
            CharacterInformation(3, "education", "Not a great reader."),
            CharacterInformation(4, "poor_drinker", "Can't hold his liqueur."),
            CharacterInformation(5, "drive", "Can't drive.")
        ]
        lad_details  = CharacterDetails(
            text_id = "lad", 
            locked = False,
            know_real_name = True,
            real_name = "Ted Harring",
            nickname = "The Lad",
            description_short = "Young man",
            description_long = "Good Looking lad, in his early twenties.",
            information_list = lad_extra_information,
            has_met = set()
            )
        lad = Character("lad_details.get_name()", image="lad", dynamic=True)

        # Map choices
        # TODO BEFORE REWRITE VAR, check it exists, and if some fields are already hidden
        # => change those fields to special var that will display an icon, or another style
        # for already visited path
        # https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=25453&p=313338&hilit=caption.replace#p313338

        condition_hunt = "(current_day == 'Saturday' and current_phase == 'Hunt')"
        condition_friday = "current_day == 'Friday'"
        condition_saturday_evening = "(current_day == 'Saturday' and current_phase == 'Evening')"
        condition_sunday_morning = "(current_day == 'Sunday' and current_phase == 'Morning')"

        lad_map_menu = TimedMenu([
            # -------------------------
            # Friday
            # -------------------------
            TimedMenuChoice(
                default_room_text('psychic_room'), 
                'lad_day1_evening_psychic_room', 
                10, 
                room = 'psychic_room', 
                condition = condition_friday
            ),
            # TimedMenuChoice(
            #     default_room_text('host_room'), 
            #     'lad_day1_evening_host_room', 
            #     10, 
            #     room = 'host_room', 
            #     condition = "current_day == 'Friday'"
            # ),
            TimedMenuChoice(
                default_room_text('garden'), 
                'garden_friday', 
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
                'lad_day1_evening_cancel', 
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
                condition = condition_hunt,
                keep_alive = True, 
            ),
            TimedMenuChoice(
                'Go back to the Tea Room', 
                'lad_day2_hunt_tea_room_return',  
                room = 'tea_room',
                condition = condition_hunt + " and " + "lad_day2_nohunt_has_visited_tea_room",
                keep_alive = True, 
            ),
            TimedMenuChoice(
                'Take a nap until the others return', 
                'lad_day2_nohunt_cancel', 
                240, 
                early_exit = True, 
                room = 'lad_room',
                condition = condition_hunt
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'lad_day2_broken_room', 
                20, 
                room = 'broken_room',
                condition = condition_hunt + " or " + condition_saturday_evening
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
                default_room_text('psychic_room'), 
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
                condition = "lad_day2_evening_taste_from_flask"
            ),
            # -------------------------
            # Sunday Search
            # -------------------------
            TimedMenuChoice(
                default_room_text('lad_room'), 
                'lad_day3_morning_lad_room',
                10,
                room = 'lad_room',
                condition = condition_sunday_morning
            ),
            TimedMenuChoice(
                default_room_text('psychic_room'), 
                'lad_day3_morning_psychic_room',
                10,
                room = 'psychic_room',
                condition = condition_sunday_morning
            ),
            TimedMenuChoice(
                default_room_text('drunk_room'), 
                'lad_day3_morning_drunk_room',
                10,
                room = 'drunk_room',
                condition = condition_sunday_morning
            ),
            TimedMenuChoice(
                default_room_text('doctor_room'), 
                'lad_day3_morning_doctor_room',
                10,
                room = 'doctor_room',
                condition = condition_sunday_morning
            ),
            TimedMenuChoice(
                default_room_text('broken_room'), 
                'lad_day3_morning_broken_room',
                10,
                room = 'broken_room',
                condition = condition_sunday_morning
            ),
            TimedMenuChoice(
                default_room_text('captain_room'), 
                'lad_day3_morning_captain_room',
                10,
                room = 'captain_room',
                condition = condition_sunday_morning
            ),
            TimedMenuChoice(
                default_room_text('host_room'), 
                'lad_day3_morning_host_room', 
                20, 
                room = 'host_room',
                condition = condition_sunday_morning
            ),
            TimedMenuChoice(
                default_room_text('nurse_room'), 
                'lad_day3_morning_nurse_room', 
                10, 
                room = 'nurse_room',
                condition = condition_sunday_morning
            ),                  
            TimedMenuChoice(
                default_room_text('kitchen'), 
                'lad_day3_morning_kitchen', 
                10, 
                room = 'kitchen',
                condition = condition_sunday_morning
            ),
            TimedMenuChoice(
                default_room_text('scullery'), 
                'lad_day3_morning_scullery', 
                10, 
                room = 'scullery',
                condition = condition_sunday_morning
            ),
            TimedMenuChoice(
                default_room_text('garage'), 
                'lad_day3_morning_garage', 
                10, 
                room = 'garage',
                condition = condition_sunday_morning
            ),
            TimedMenuChoice(
                default_room_text('gun_room'), 
                'lad_day3_morning_gun_room', 
                10, 
                room = 'gun_room',
                condition = condition_sunday_morning
            ),
            TimedMenuChoice(
                'Go wait for Sushil', 
                'lad_day3_morning_give_up', 
                early_exit = True, 
                room = 'tea_room', 
                condition = "lad_day3_morning_captain_found"
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
                condition = "(not current_day == 'Sunday' and lad_library_visited)",
                keep_alive = True, 
            ),

        ], is_map = True)

    return