label lad_config_menu:

    $ psychic_generic_menu_lad = TimedMenu([
        TimedMenuChoice('What do you think of this weather?', 'psychic_generic_weather_friday', 5, condition = "current_day == 'Friday'"),
        TimedMenuChoice('What do you think of this weather?', 'psychic_generic_weather_saturday', 5, condition = "current_day == 'Saturday'"),
        TimedMenuChoice('What do you think of this weather?', 'psychic_generic_weather_sunday', 5, condition = "current_day == 'Sunday'"),
        TimedMenuChoice('Tell me more about yourself.', 'psychic_generic_background', 15),
        TimedMenuChoice('Why were you invited here?', 'psychic_generic_heroic_act', 20, condition = "psychic_details.is_knowledge_unlocked('background')"),
        TimedMenuChoice('What do you think of this place?', 'psychic_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'psychic_generic_age', 5),
        TimedMenuChoice('What room are you in?', 'psychic_generic_room', 5, condition = "not is_unlock_map('psychic_room')"),
        TimedMenuChoice('What do you think of the other guests?', 'psychic_generic_other_guests_friday', 0, condition = "current_day == 'Friday'"),
        TimedMenuChoice('What do you think of the other guests?', 'psychic_generic_other_guests_saturday_morning', 0, keep_alive = True, condition = "(current_day == 'Saturday' and current_phase == 'Morning')"),
        TimedMenuChoice('What do you think of the other guests?', 'psychic_generic_other_guests_saturday_hunt', 0, keep_alive = True, condition = "(current_day == 'Saturday' and current_phase == 'Hunt')"),
        TimedMenuChoice('You don\'t have anymore questions for her', 'psychic_generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "psychic")

    return