label doctor_config_menu:

    # BROKEN
    $ broken_generic_menu_doctor = TimedMenu("broken_generic_menu_doctor", [
        TimedMenuChoice('What do you think of this weather?', 'broken_generic_weather_friday', 10, condition = condition_friday),
        TimedMenuChoice('Tell me more about yourself.', 'broken_generic_background', 30, linked_choice ="broken_generic_heroic_act"),
        TimedMenuChoice('Why were you invited here?', 'broken_generic_heroic_act', 30, condition = "current_character.saved_variables['knows_broken_background']"),
        TimedMenuChoice('What do you think of this place?', 'broken_generic_manor', 20),
        TimedMenuChoice('How old are you?', 'broken_generic_age', 10),
        TimedMenuChoice('What room are you in?', 'broken_generic_room', 10, condition = "not is_unlock_map('bedroom_psychic')"),
        TimedMenuChoice('What do you think of the other guests?', 'broken_generic_other_guests_friday', 10, condition = condition_friday),
        TimedMenuChoice('You don\'t have anymore questions for him', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "broken")

    return