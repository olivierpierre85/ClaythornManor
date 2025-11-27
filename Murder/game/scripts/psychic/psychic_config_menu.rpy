label psychic_config_menu:
    #---------------------------------------------------------------------
    # Nurse
    $ nurse_generic_menu_psychic = TimedMenu("nurse_generic_menu_psychic", [
        # TimedMenuChoice('What do you think of this weather?', 'nurse_generic_weather_friday', 5, condition = "current_day == 'Friday'"),
        TimedMenuChoice('What do you think of this weather?', 'nurse_generic_weather_saturday_morning', 10, condition = condition_saturday),
        TimedMenuChoice('Tell me more about yourself.', 'nurse_generic_background_psychic', 20, linked_choice ="nurse_generic_heroic_act_psychic"),
        TimedMenuChoice('Why were you invited here?', 'nurse_generic_heroic_act_psychic', 20, condition = "all_menus['nurse_generic_menu_psychic'].choices[1].hidden"),
        TimedMenuChoice('What do you think of this place?', 'nurse_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'nurse_generic_age', 10),
        TimedMenuChoice('What room are you in?', 'nurse_generic_room', 10),
        # TimedMenuChoice('What do you think of the other guests?', 'nurse_generic_other_guests_friday', 5, condition = "current_day == 'Friday'"),
        TimedMenuChoice('What do you think of the other guests?', 'nurse_generic_other_guests_saturday_morning', 0, keep_alive = True, condition = condition_saturday, next_menu='nurse_generic_other_guests_menu_psychic' ),
        TimedMenuChoice('You don\'t have anymore questions for her', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "nurse")

    $ nurse_generic_other_guests_menu_psychic = TimedMenu("nurse_generic_other_guests_menu_psychic", [
        TimedMenuChoice('What do you think of Samuel Manning', 'nurse_generic_drunk_saturday_morning', 10),
        TimedMenuChoice('What do you think of Lady Claythorn', 'nurse_generic_host_saturday', 10),
        TimedMenuChoice('I want to talk about something else.', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "nurse")
    
    #---------------------------------------------------------------------
    # DOCTOR
    $ doctor_generic_menu_psychic = TimedMenu("doctor_generic_menu_psychic", [
        TimedMenuChoice('What do you think of this weather?', 'doctor_generic_weather_friday', 10, condition = "current_day == 'Friday'"),
        TimedMenuChoice('What do you think of this weather?', 'doctor_generic_weather_saturday', 10, condition = "current_day == 'Saturday'"),
        TimedMenuChoice('Tell me more about yourself.', 'doctor_generic_background', 20, linked_choice ="doctor_generic_heroic_act"),
        TimedMenuChoice('Why were you invited here?', 'doctor_generic_heroic_act', 20, condition = "all_menus['doctor_generic_menu_psychic'].choices[2].hidden"),
        TimedMenuChoice('What do you think of this place?', 'doctor_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'doctor_generic_age', 10),
        TimedMenuChoice('What room are you in?', 'doctor_generic_room', 10),
        TimedMenuChoice('What do you think of the other guests?', 'doctor_generic_other_guests_friday', 10, condition = "current_day == 'Friday'", next_menu="doctor_generic_other_guests_menu_psychic"),
        TimedMenuChoice('What do you think of the other guests?', 'doctor_generic_other_guests_saturday', 0, keep_alive = True, condition = "current_day == 'Saturday'", next_menu="doctor_generic_other_guests_menu_psychic"),
        TimedMenuChoice('You don\'t have anymore questions for him', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "doctor")

    $ doctor_generic_other_guests_menu_psychic = TimedMenu("doctor_generic_other_guests_menu_psychic", [
        TimedMenuChoice('What about Samuel Manning?', 'doctor_generic_drunk', 5),
        TimedMenuChoice('I want to talk about something else.', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "doctor")


    #---------------------------------------------------------------------
    # CAPTAIN

    $ captain_generic_menu_psychic = TimedMenu("captain_generic_menu_psychic", [
        TimedMenuChoice('Tell me more about yourself', 'captain_generic_background_psychic', 30),
        # TimedMenuChoice('I would like to know a bit more about you', 'captain_generic_background_psychic_2', 30, condition = "all_menus['captain_generic_menu_psychic'].choices[0].hidden"),
        # TimedMenuChoice('Isn\'t there anything else you can tell me about yourself?', 'captain_generic_background_psychic_3', 30, condition = "all_menus['captain_generic_menu_psychic'].choices[1].hidden"),
        TimedMenuChoice('Why were you invited here?', 'captain_generic_heroic_act_psychic', 30, condition =  "all_menus['captain_generic_menu_psychic'].choices[0].hidden"),
        TimedMenuChoice('What do you think of this place?', 'captain_generic_manor_psychic', 30),
        TimedMenuChoice('How old are you?', 'captain_generic_age_psychic', 10),
        TimedMenuChoice('What room are you in?', 'captain_generic_room_friday', 10, condition = condition_friday),
        TimedMenuChoice('What room are you in?', 'captain_generic_room', 10, condition = "not " + condition_friday),
        TimedMenuChoice('What do you think of the other guests?', 'captain_generic_other_guests_friday', 0, condition = condition_friday, next_menu="captain_generic_other_guests_menu_psychic"),
        TimedMenuChoice('What do you think of the other guests?', 'captain_generic_other_guests_saturday_morning', 0, condition = condition_saturday_morning, keep_alive = True, next_menu="captain_generic_other_guests_menu_psychic"),
        TimedMenuChoice('What do you think of the other guests?', 'captain_generic_other_guests_saturday_evening', 0, condition = condition_saturday_evening, keep_alive = True, next_menu="captain_generic_other_guests_menu_psychic"),
        TimedMenuChoice('There is something weird about Rosalind Marsh{{observation}}', 'psychic_day2_evening_nurse_captain', 0, condition = condition_saturday + " and psychic_details.observations.is_unlocked('silverware')"),
        # exit
        TimedMenuChoice('On second thought, I\'d better not talk to him', 'generic_cancel', 0, keep_alive = True, early_exit = True )
    ], image_right = "captain")


    $ captain_generic_other_guests_menu_psychic = TimedMenu("captain_generic_other_guests_menu_psychic", [
        # Same on friday an saturday
        TimedMenuChoice('What do you think of Lady Claythorn?', 'captain_generic_host_friday_psychic', 10, condition = condition_friday_or_saturday),
        TimedMenuChoice('What do you think of Rosalind Marsh?', 'captain_generic_nurse_friday', 10, condition = condition_friday_or_saturday),        
        TimedMenuChoice('What do you think of Ted Harring?', 'captain_generic_lad_friday_psychic', 10, condition = condition_friday_or_saturday),
        # Others
        TimedMenuChoice('What do you think of Samuel Manning?', 'captain_generic_drunk_friday_psychic', 10, condition = condition_friday_or_saturday_morning ),
        TimedMenuChoice('What do you think of Thomas Moody?', 'captain_generic_broken_friday', 20, condition = condition_friday_or_saturday_morning),
        TimedMenuChoice('What do you think of Daniel Baldwin?', 'captain_generic_doctor_friday', 10, condition = condition_friday_or_saturday_morning),
        # Saturday different for the dead and the killer
        TimedMenuChoice('What do you think of Samuel Manning?', 'captain_generic_drunk_saturday_psychic', 10, condition = condition_saturday_evening ),      
        TimedMenuChoice('What do you think of Thomas Moody?', 'captain_generic_broken_saturday', 10, condition = condition_saturday_evening),
        TimedMenuChoice('What do you think of Daniel Baldwin?', 'captain_generic_doctor_saturday', 10, condition = condition_saturday_evening),
        # Always Generic 
        TimedMenuChoice('Talk about something else', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "captain")
    
    #---------------------------------------------------------------------
    # LAD

    $ lad_generic_menu_psychic = TimedMenu("lad_generic_menu_psychic", [
        TimedMenuChoice('Tell me more about yourself.', 'lad_generic_background_psychic', 15, linked_choice ="lad_generic_heroic_act_psychic"),
        TimedMenuChoice('Why were you invited here?', 'lad_generic_heroic_act_psychic', 40, condition = "all_menus['lad_generic_menu_psychic'].choices[0].hidden"),
        TimedMenuChoice('What do you think of this place?', 'lad_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'lad_generic_age_psychic', 10),
        TimedMenuChoice('What room are you in?', 'lad_generic_room_friday', 10, condition = condition_friday),
        TimedMenuChoice('What room are you in?', 'lad_generic_room_psychic', 10, condition = "not " + condition_friday),
        TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_friday_dinner', 10, condition = condition_friday),
        # TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_saturday_morning', 0, keep_alive = True, condition = "(current_day == 'Saturday' and current_phase == 'Morning')"),
        # TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_saturday_hunt', 0, keep_alive = True, condition = "(current_day == 'Saturday' and current_phase == 'The Hunt')"),
        TimedMenuChoice('You don\'t have anymore questions for him', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "lad")

    $ lad_generic_other_guests_menu_psychic = TimedMenu("lad_generic_other_guests_menu_psychic", [
    #     # Saturday Morning
    #     TimedMenuChoice('What do you think of Samuel Manning?', 'psychic_generic_drunk_saturday_morning', 5, condition = condition_saturday_morning_or_hunt ),
    #     TimedMenuChoice('What do you think of Sushil Sinha?', 'psychic_generic_captain_saturday_morning', 5, condition = condition_saturday_morning_or_hunt),
    #     TimedMenuChoice('What do you think of Lady Claythorn?', 'psychic_generic_host_saturday_morning', 5, condition = condition_saturday_morning_or_hunt),
    #     TimedMenuChoice('What do you think of Rosalind Marsh,', 'psychic_generic_nurse_saturday_hunt', 5, condition = condition_saturday_hunt),

    #     # TimedMenuChoice('What do you think of Thomas Moody?', 'psychic_generic_broken_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
    #     # TimedMenuChoice('What do you think of Rosalind Marsh?', 'psychic_generic_nurse_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
    #     # TimedMenuChoice('What do you think of Daniel Baldwin?', 'psychic_generic_doctor_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
    #     # Always Generic 
        TimedMenuChoice('Talk about something else', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "lad")


    return