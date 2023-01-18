label psychic_config_menu:

    # CAPTAIN
    $ captain_generic_menu_psychic = TimedMenu([
        # In the car ((not really a choice))
        TimedMenuChoice('Where are you from?', 'captain_generic_origin_psychic_1', 5),
        TimedMenuChoice('I mean, where are you \"Really\" from?', 'captain_generic_origin_psychic_2', 5 , condition = "psychic_details.is_knowledge_unlocked('racist')"),
    ], image_right = "captain")



    # LAD

    $ lad_generic_menu_psychic = TimedMenu([
        # TimedMenuChoice('What do you think of this weather?', 'lad_generic_weather_saturday', 5, condition = condition_saturday),
        # TimedMenuChoice('What do you think of this weather?', 'lad_generic_weather_sunday', 5, condition = "current_day == 'Sunday'"),
        TimedMenuChoice('Tell me more about yourself.', 'lad_generic_background', 15),
        TimedMenuChoice('Why were you invited here?', 'lad_generic_heroic_act', 20, condition = "lad_details.is_knowledge_unlocked('background')"),
        TimedMenuChoice('What do you think of this place?', 'lad_generic_manor_lad', 10),
        TimedMenuChoice('How old are you?', 'lad_generic_age_psychic', 5),
        TimedMenuChoice('What room are you in?', 'lad_generic_room_friday', 5, condition = condition_friday),
        TimedMenuChoice('What room are you in?', 'lad_generic_room_psychic', 5, condition = "not " + condition_friday),
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



    return