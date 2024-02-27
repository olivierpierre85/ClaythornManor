label psychic_config_menu:
    #---------------------------------------------------------------------
    # Nurse
    $ nurse_generic_menu_psychic = TimedMenu("nurse_generic_menu_psychic", [
        # TimedMenuChoice('What do you think of this weather?', 'nurse_generic_weather_friday', 5, condition = "current_day == 'Friday'"),
        TimedMenuChoice('What do you think of this weather?', 'nurse_generic_weather_saturday', 10, condition = "current_day == 'Saturday'"),
        TimedMenuChoice('Tell me more about yourself.', 'nurse_generic_background', 20),
        TimedMenuChoice('Why were you invited here?', 'nurse_generic_heroic_act', 20, condition = "current_character.saved_variables['knows_nurse_background']"),
        TimedMenuChoice('What do you think of this place?', 'nurse_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'nurse_generic_age', 10),
        TimedMenuChoice('What room are you in?', 'nurse_generic_room', 10),
        # TimedMenuChoice('What do you think of the other guests?', 'nurse_generic_other_guests_friday', 5, condition = "current_day == 'Friday'"),
        TimedMenuChoice('What do you think of the other guests?', 'nurse_generic_other_guests_saturday', 5, keep_alive = True, condition = "current_day == 'Saturday'"),
        TimedMenuChoice('You don\'t have anymore questions for her', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "nurse")

    $ nurse_generic_other_guests_menu_psychic = TimedMenu("nurse_generic_other_guests_menu_psychic", [
        TimedMenuChoice('Ask about Samuel Manning', 'nurse_generic_drunk_saturday_morning', 10),
        TimedMenuChoice('Ask about Lady Claythorn', 'nurse_generic_host_saturday_morning', 10),
        TimedMenuChoice('I want to talk about something else.', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "nurse")
    
    #---------------------------------------------------------------------
    # DOCTOR
    $ doctor_generic_menu_psychic = TimedMenu("doctor_generic_menu_psychic", [
        TimedMenuChoice('What do you think of this weather?', 'doctor_generic_weather_friday', 5, condition = "current_day == 'Friday'"),
        TimedMenuChoice('What do you think of this weather?', 'doctor_generic_weather_saturday', 5, condition = "current_day == 'Saturday'"),
        TimedMenuChoice('Tell me more about yourself.', 'doctor_generic_background', 20),
        TimedMenuChoice('Why were you invited here?', 'doctor_generic_heroic_act', 20, condition = "current_character.saved_variables['knows_doctor_background']"),
        TimedMenuChoice('What do you think of this place?', 'doctor_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'doctor_generic_age', 5),
        TimedMenuChoice('What room are you in?', 'doctor_generic_room', 5),
        TimedMenuChoice('What do you think of the other guests?', 'doctor_generic_other_guests_friday', 5, condition = "current_day == 'Friday'"),
        TimedMenuChoice('What do you think of the other guests?', 'doctor_generic_other_guests_saturday', 5, condition = "current_day == 'Saturday'"),
        TimedMenuChoice('You don\'t have anymore questions for him', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "doctor")

    $ doctor_generic_other_guests_menu_psychic = TimedMenu("doctor_generic_other_guests_menu_psychic", [
        TimedMenuChoice('What about Samuel Manning?', 'doctor_generic_drunk', 5),
        TimedMenuChoice('I want to talk about something else.', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "doctor")


    #---------------------------------------------------------------------
    # CAPTAIN
    $ condition_captain_origin = "current_character.saved_variables['knows_captain_real_origin']"
    $ captain_generic_menu_psychic = TimedMenu("captain_generic_menu_psychic", [
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


    $ captain_generic_other_guests_menu_psychic = TimedMenu("captain_generic_other_guests_menu_psychic", [
        # Friday
        TimedMenuChoice('Ask about Samuel Manning', 'captain_generic_drunk_friday_psychic', 5, condition = condition_friday ),
        TimedMenuChoice('Ask about Lady Claythorn', 'captain_generic_host_friday_psychic', 5, condition = condition_friday),
        TimedMenuChoice('Ask about Rosalind Marsh', 'captain_generic_nurse_friday', 5, condition = condition_friday),        
        TimedMenuChoice('Ask about Thomas Moody', 'captain_generic_broken_friday', 20, condition = condition_friday),
        TimedMenuChoice('Ask about Ted Harring', 'captain_generic_lad_friday_psychic', 10, condition = condition_friday),
        TimedMenuChoice('Ask about Daniel Baldwin', 'captain_generic_doctor_friday', 5, condition = condition_friday),
        # Always Generic 
        TimedMenuChoice('Talk about something else', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "captain")
    
    #---------------------------------------------------------------------
    # LAD

    $ lad_generic_menu_psychic = TimedMenu("lad_generic_menu_psychic", [
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

    $ lad_generic_other_guests_menu_psychic = TimedMenu("lad_generic_other_guests_menu_psychic", [
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