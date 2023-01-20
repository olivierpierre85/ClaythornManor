label psychic_config_menu:

    # CAPTAIN
    $ condition_captain_origin = "current_character.saved_variables['knows_captain_real_origin']"
    $ captain_generic_menu_psychic = TimedMenu([
        # In the car ((not really a choice))
        TimedMenuChoice('Where are you from?', 'captain_generic_origin_psychic_1', 5),
        TimedMenuChoice('I mean, where are you \"Really\" from?', 'captain_generic_origin_psychic_2', 5 , condition = "current_character.saved_variables['knows_captain_origin']"),
        # Real Generics
        TimedMenuChoice('Why were you invited here?', 'captain_generic_heroic_act_psychic', 20, condition = condition_captain_origin),
        TimedMenuChoice('What do you think of this place?', 'captain_generic_manor_psychic', 10, condition = condition_captain_origin),
        TimedMenuChoice('How old are you?', 'captain_generic_age_psychic', 5, condition = condition_captain_origin),
        TimedMenuChoice('What room are you in?', 'captain_generic_room_friday', 5, condition = condition_captain_origin + "and " + condition_friday),
        TimedMenuChoice('What room are you in?', 'captain_generic_room_psychic', 5, condition = condition_captain_origin + "and " + " not " + condition_friday),
        TimedMenuChoice('What do you think of the other guests?', 'captain_generic_other_guests_friday', 0, condition = condition_captain_origin + "and " + condition_friday),
        # exit
        TimedMenuChoice('On second thought, I\'d better not talk to him', 'generic_cancel', 0, keep_alive = True, early_exit = True, condition = condition_captain_origin )
    
    ], image_right = "captain")



    # LAD

    $ lad_generic_menu_psychic = TimedMenu([
        TimedMenuChoice('Tell me more about yourself.', 'lad_generic_background_psychic', 15),
        TimedMenuChoice('Why were you invited here?', 'lad_generic_heroic_act_psychic', 20, condition = "psychic_details.saved_variables['knows_lad_background']"),
        TimedMenuChoice('What do you think of this place?', 'lad_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'lad_generic_age_psychic', 5),
        TimedMenuChoice('What room are you in?', 'lad_generic_room_friday', 5, condition = condition_friday),
        TimedMenuChoice('What room are you in?', 'lad_generic_room_psychic', 5, condition = "not " + condition_friday),
        TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_friday', 0, condition = condition_friday),
        # TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_saturday_morning', 0, keep_alive = True, condition = "(current_day == 'Saturday' and current_phase == 'Morning')"),
        # TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_saturday_hunt', 0, keep_alive = True, condition = "(current_day == 'Saturday' and current_phase == 'Hunt')"),
        TimedMenuChoice('You don\'t have anymore questions for him', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "lad")

    $ lad_generic_other_guests_menu_psychic = TimedMenu([
    #     # Saturday Morning
    #     TimedMenuChoice('Ask about Samuel Manning', 'psychic_generic_drunk_saturday_morning', 5, condition = condition_saturday_morning_or_hunt ),
    #     TimedMenuChoice('Ask about Sushil Sinha', 'psychic_generic_captain_saturday_morning', 5, condition = condition_saturday_morning_or_hunt),
    #     TimedMenuChoice('Ask about Lady Claythorn', 'psychic_generic_host_saturday_morning', 5, condition = condition_saturday_morning_or_hunt),
    #     TimedMenuChoice('Ask about Rosalind Marsh', 'psychic_generic_nurse_saturday_hunt', 5, condition = condition_saturday_hunt),

    #     # TimedMenuChoice('Ask about Thomas Moody', 'psychic_generic_broken_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
    #     # TimedMenuChoice('Ask about Rosalind Marsh', 'psychic_generic_nurse_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
    #     # TimedMenuChoice('Ask about Daniel Baldwin', 'psychic_generic_doctor_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
    #     # Always Generic 
        TimedMenuChoice('Talk about something else', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "lad")



    return