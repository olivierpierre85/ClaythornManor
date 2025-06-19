label lad_config_menu:

    # PSYCHIC
    $ psychic_generic_menu_lad = TimedMenu("psychic_generic_menu_lad", [
        TimedMenuChoice('What do you think of this weather?', 'psychic_generic_weather_friday', 10, condition = condition_friday),
        TimedMenuChoice('What do you think of this weather?', 'psychic_generic_weather_saturday', 10, condition = condition_saturday),
        TimedMenuChoice('What do you think of this weather?', 'psychic_generic_weather_sunday', 10, condition = condition_sunday),
        TimedMenuChoice('Tell me more about yourself.', 'psychic_generic_background', 30, linked_choice ="psychic_generic_heroic_act"),
        TimedMenuChoice('Why were you invited here?', 'psychic_generic_heroic_act', 30, condition = "all_menus[current_menu.id].choices[3].hidden"), # Can Only show this choice when the one before has be selected because the answers are linked
        TimedMenuChoice('What do you think of this place?', 'psychic_generic_manor', 20),
        TimedMenuChoice('How old are you?', 'psychic_generic_age', 10),
        TimedMenuChoice('What room are you in?', 'psychic_generic_room', 10, condition = "not is_unlock_map('bedroom_psychic')"),
        TimedMenuChoice('What do you think of the other guests?', 'psychic_generic_other_guests_friday', 10, condition = condition_friday),
        TimedMenuChoice('What do you think of the other guests?', 'psychic_generic_other_guests_saturday_morning', 0, keep_alive = True, condition = condition_saturday_morning),
        TimedMenuChoice('What do you think of the other guests?', 'psychic_generic_other_guests_saturday_hunt', 0, keep_alive = True, condition = condition_saturday_hunt),
        TimedMenuChoice('Which guests do you think could be dangerous?', 'psychic_generic_other_guests_saturday_evening', 0, keep_alive = True, condition = condition_saturday_evening),
        TimedMenuChoice('You don\'t have anymore questions for her', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "psychic")

    $ psychic_generic_other_guests_menu_lad = TimedMenu("psychic_generic_other_guests_menu_lad", [
        # Saturday Morning
        TimedMenuChoice('What do you think of Samuel Manning?', 'psychic_generic_drunk_saturday_morning', 10, condition = condition_saturday_morning_or_hunt ),
        TimedMenuChoice('What do you think of Sushil Sinha?', 'psychic_generic_captain_saturday_morning', 10, condition = condition_saturday_morning_or_hunt),
        TimedMenuChoice('What do you think of Lady Claythorn?', 'psychic_generic_host_saturday_morning', 10, condition = condition_saturday_morning_or_hunt),
        TimedMenuChoice('What do you think of Rosalind Marsh?', 'psychic_generic_nurse_saturday_hunt', 10, condition = condition_saturday_hunt),

        # Saturday Evening
        # TimedMenuChoice('What do you think of Samuel Manning', 'psychic_generic_drunk_saturday_morning', 10, condition = condition_saturday_morning_or_hunt ),
        TimedMenuChoice('What do you think of Sushil Sinha?', 'psychic_generic_captain_saturday_evening', 10, condition = condition_saturday_evening),
        TimedMenuChoice('What do you think of Lady Claythorn?', 'psychic_generic_host_saturday_evening', 10, condition = condition_saturday_evening),
        TimedMenuChoice('What do you think of Rosalind Marsh?', 'psychic_generic_nurse_saturday_evening', 10, condition = condition_saturday_evening),
        # Always Generic 
        TimedMenuChoice('Talk about something else', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "psychic")

    # DOCTOR
    $ doctor_generic_menu_lad = TimedMenu("doctor_generic_menu_lad", [
        TimedMenuChoice('What do you think of this weather?', 'doctor_generic_weather_friday', 10, condition = "current_day == 'Friday'"),
        TimedMenuChoice('What do you think of this weather?', 'doctor_generic_weather_saturday', 10, condition = "current_day == 'Saturday'"),
        TimedMenuChoice('Tell me more about yourself.', 'doctor_generic_background', 20, linked_choice ="doctor_generic_heroic_act"),
        TimedMenuChoice('Why were you invited here?', 'doctor_generic_heroic_act', 30, condition = "all_menus[current_menu.id].choices[2].hidden"),
        TimedMenuChoice('What do you think of this place?', 'doctor_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'doctor_generic_age', 10),
        TimedMenuChoice('What room are you in?', 'doctor_generic_room', 10),
        TimedMenuChoice('What do you think of the other guests?', 'doctor_generic_other_guests_friday', 10, condition = "current_day == 'Friday'"),
        TimedMenuChoice('What do you think of the other guests?', 'doctor_generic_other_guests_saturday', 10, condition = "current_day == 'Saturday'"),
        TimedMenuChoice('You don\'t have anymore questions for him', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "doctor")

    $ doctor_generic_other_guests_menu_lad = TimedMenu("doctor_generic_other_guests_menu_lad", [
        TimedMenuChoice('What about Samuel Manning?', 'doctor_generic_drunk', 10),
        TimedMenuChoice('I want to talk about something else.', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "doctor")

    return