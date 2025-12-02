label psychic_config_map:
    python:        
        # Map choices

        # LORD conditions, can happen at any time
        attic_visited = "psychic_details.threads.is_unlocked('visited_attic')"
        attic_not_visited = "not psychic_details.threads.is_unlocked('visited_attic')"

        knows_lord_name = "psychic_details.threads.is_unlocked('lord_name')"
        attic_visited_do_not_know_lord_name = "(psychic_details.threads.is_unlocked('visited_attic') and not psychic_details.threads.is_unlocked('lord_name'))"
        attic_default = "not psychic_details.threads.is_unlocked('lord_age')"
        attic_return = "psychic_details.threads.is_unlocked('lord_age')"

        attic_return_too_soon = "psychic_details.threads.is_unlocked('visited_attic') and not psychic_details.threads.is_unlocked('lord_age')"

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

    call psychic_day1_evening_map_menu

    call psychic_day2_no_hunt_map_menu

    call psychic_day2_evening_map_menu
    
    return