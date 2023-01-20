label psychic_config_map:
    python:        
        # Map choices

        psychic_map_menu = TimedMenu([
            # -------------------------
            # Friday
            # -------------------------
            TimedMenuChoice(
                'Go to bed', 
                'generic_cancel', 
                10, 
                room = 'psychic_room', 
                condition = condition_friday,
                early_exit = True
            ),
            # TimedMenuChoice(
            #     default_room_text('garden'), 
            #     'garden_friday', 
            #     5, 
            #     room = 'garden', 
            #     condition = condition_friday
            # ),
            TimedMenuChoice(
                'Meet the others in the billiard room', 
                'lad_day1_evening_billiard_room', 
                0, 
                keep_alive = True, 
                room = 'billiard_room', 
                condition = condition_friday
            ),
            # -------------------------
            # Generic choices
            # -------------------------
            TimedMenuChoice(
                default_room_text('library'), 
                'psychic_library', 
                20, 
                room = 'library',
                condition = "(not current_day == 'Sunday')"
            ),

        ], is_map = True)

    return