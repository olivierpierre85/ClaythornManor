label init_lad:
    python:
        # Story Variables
        lad_day1_evening_billiard_room_visited = False
        lad_day1_drinks = 0
        lad_day1_poisoned = False

        lad_visited_library = False
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
        lad_map_menu = TimedMenu([
            # Friday specific choices
            TimedMenuChoice(
                'Go knock on the the door of Amelia Baxter', 
                'lad_day1_evening_psychic_room', 
                55, 
                room = 'psychic_room', 
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
            )
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