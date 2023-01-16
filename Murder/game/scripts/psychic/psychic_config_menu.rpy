label psychic_config_menu:

    # LAD

    $ lad_generic_menu_psychic = TimedMenu([
        TimedMenuChoice('What do you think of this weather?', 'lad_generic_weather_saturday', 5, condition = condition_saturday),
        TimedMenuChoice('What do you think of this weather?', 'lad_generic_weather_sunday', 5, condition = "current_day == 'Sunday'"),
        TimedMenuChoice('Tell me more about yourself.', 'lad_generic_background', 15),
        TimedMenuChoice('Why were you invited here?', 'lad_generic_heroic_act', 20, condition = "lad_details.is_knowledge_unlocked('background')"),
        TimedMenuChoice('What do you think of this place?', 'lad_generic_manor_lad', 10),
        TimedMenuChoice('How old are you?', 'lad_generic_age', 5),
        TimedMenuChoice('What room are you in?', 'lad_generic_room', 5, condition = "not is_unlock_map('lad_room')"),
        # TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_friday', 0, condition = "current_day == 'Friday'"),
        # TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_saturday_morning', 0, keep_alive = True, condition = "(current_day == 'Saturday' and current_phase == 'Morning')"),
        # TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_saturday_hunt', 0, keep_alive = True, condition = "(current_day == 'Saturday' and current_phase == 'Hunt')"),
        # TimedMenuChoice('You don\'t have anymore questions for her', 'lad_generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "lad")

    # $ psychic_generic_other_guests_menu_lad = TimedMenu([
    #     # Saturday Morning
    #     TimedMenuChoice('Ask about Samuel Manning', 'psychic_generic_drunk_saturday_morning', 5, condition = condition_saturday_morning_or_hunt ),
    #     TimedMenuChoice('Ask about Sushil Sinha', 'psychic_generic_captain_saturday_morning', 5, condition = condition_saturday_morning_or_hunt),
    #     TimedMenuChoice('Ask about Lady Claythorn', 'psychic_generic_host_saturday_morning', 5, condition = condition_saturday_morning_or_hunt),
    #     TimedMenuChoice('Ask about Rosalind Marsh', 'psychic_generic_nurse_saturday_hunt', 5, condition = condition_saturday_hunt),

    #     # TimedMenuChoice('Ask about Thomas Moody', 'psychic_generic_broken_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
    #     # TimedMenuChoice('Ask about Rosalind Marsh', 'psychic_generic_nurse_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
    #     # TimedMenuChoice('Ask about Daniel Baldwin', 'psychic_generic_doctor_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
    #     # Always Generic 
    #     TimedMenuChoice('Talk about something else', 'psychic_generic_cancel', 0, keep_alive = True, early_exit = True)
    # ], image_right = "psychic")

    # DOCTOR
    # $ doctor_generic_menu_lad = TimedMenu([
    #     TimedMenuChoice('What do you think of this weather?', 'doctor_generic_weather_friday', 5, condition = "current_day == 'Friday'"),
    #     TimedMenuChoice('What do you think of this weather?', 'doctor_generic_weather_saturday', 5, condition = "current_day == 'Saturday'"),
    #     TimedMenuChoice('Tell me more about yourself.', 'doctor_generic_background', 20),
    #     TimedMenuChoice('Why were you invited here?', 'doctor_generic_heroic_act', 20, condition = "doctor_details.is_knowledge_unlocked('background')"),
    #     TimedMenuChoice('What do you think of this place?', 'doctor_generic_manor', 10),
    #     TimedMenuChoice('How old are you?', 'doctor_generic_age', 5),
    #     TimedMenuChoice('What room are you in?', 'doctor_generic_room', 5),
    #     TimedMenuChoice('What do you think of the other guests?', 'doctor_generic_other_guests_friday', 5, condition = "current_day == 'Friday'"),
    #     TimedMenuChoice('What do you think of the other guests?', 'doctor_generic_other_guests_saturday', 5, condition = "current_day == 'Saturday'"),
    #     TimedMenuChoice('You don\'t have anymore questions for him', 'doctor_generic_cancel', 0, keep_alive = True, early_exit = True)
    # ], image_right = "doctor")

    # $ doctor_generic_other_guests_menu_lad = TimedMenu([
    #     TimedMenuChoice('What about Samuel Manning?', 'doctor_generic_drunk', 5),
    #     TimedMenuChoice('I want to talk about something else.', 'doctor_generic_cancel', 0, keep_alive = True, early_exit = True)
    # ], image_right = "doctor")

    return