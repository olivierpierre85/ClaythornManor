label init_lad:
    call change_time(17,00, 'Evening', "Friday")

    python:
        # Story Variables
        lad_day1_evening_billiard_room_visited = False
        lad_day1_drinks = 0
        lad_day1_poisoned = False
        lad_day1_drunk = False

        lad_day2_breakfast_follow = False
        lad_day2_hunt = False
        lad_day3_morning_captain_found = False
        lad_day3_gun_downed = False
        lad_day3_poisoned = False

        # Character Class
        lad_extra_information = [
            CharacterInformation(0, "background", "Born in ???") , 
            CharacterInformation(2, "age", "He was 15 at the end of the war. That would make him 22 years old today."),
            CharacterInformation(3, "education", "Not a great reader.")
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
        lad_map_menu = TimedMenu([
            # Friday specific choices
            TimedMenuChoice(
                default_room_text('psychic_room'), 
                'lad_day1_evening_psychic_room', 
                10, 
                room = 'psychic_room', 
                condition = "current_day == 'Friday'"
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
                condition = "current_day == 'Friday'"
            ),
            TimedMenuChoice(
                'Meet the others in the billiard room', 
                'lad_day1_evening_billiard_room', 
                0, 
                keep_alive = True, 
                room = 'billiard_room', 
                condition = "current_day == 'Friday'"
            ),
            TimedMenuChoice(
                'Go to sleep', 
                'lad_day1_evening_cancel', 
                early_exit = True, 
                room = 'lad_room',
                condition = "current_day == 'Friday'"
            ),
            # Generic choices
            TimedMenuChoice(
                default_room_text('library'), 
                'lad_library', 
                20, 
                room = 'library',
                condition = "(not current_day == 'Sunday')"
            ),
        ], is_map = True)

    return