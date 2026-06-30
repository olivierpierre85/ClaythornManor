label broken_config_menu:

    #---------------------------------------------------------------------
    # Host
    $ host_generic_menu_broken = TimedMenu("host_generic_menu_broken", [
        TimedMenuChoice('What do you think of this weather?', 'host_generic_weather', 10),
        TimedMenuChoice('Tell me more about yourself.', 'host_generic_background_broken', 20, linked_choice = "host_generic_invite_broken"),
        TimedMenuChoice('Why did you invite us here?', 'host_generic_invite_broken', 20, linked_choice = "host_generic_award", condition = "is_linked_choice_hidden('host_generic_menu_broken', 'host_generic_invite_broken')"),
        TimedMenuChoice('Have you been giving this prize away for long?', 'host_generic_award', 30, condition = "is_linked_choice_hidden('host_generic_menu_broken', 'host_generic_award')"),
        TimedMenuChoice('What do you think of the other guests?', 'host_generic_other_guests_broken', 10),
        TimedMenuChoice('What do you think of this place?', 'host_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'host_generic_age_broken', 10),
        TimedMenuChoice('What room are you in?', 'host_generic_room', 10),
        TimedMenuChoice("You don't have any more questions for her", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_left = "host")

    #---------------------------------------------------------------------
    # Doctor
    $ doctor_generic_menu_broken = TimedMenu("doctor_generic_menu_broken", [
        TimedMenuChoice('What do you think of this weather?', 'doctor_generic_weather_friday', 10, condition = "current_day == 'Friday'"),
        TimedMenuChoice('Tell me more about yourself.', 'doctor_generic_background_broken', 20, linked_choice = "doctor_generic_heroic_act_broken"),
        TimedMenuChoice('Why were you invited here?', 'doctor_generic_heroic_act_broken', 30, linked_choice = "doctor_generic_heroic_act_war", condition = "is_linked_choice_hidden('doctor_generic_menu_broken', 'doctor_generic_heroic_act_broken')"),
        TimedMenuChoice('Which wars did you fight in?', 'doctor_generic_heroic_act_war', 30, condition = "is_linked_choice_hidden('doctor_generic_menu_broken', 'doctor_generic_heroic_act_war')"),
        TimedMenuChoice('What do you think of this place?', 'doctor_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'doctor_generic_age', 10),
        TimedMenuChoice('What room are you in?', 'doctor_generic_room', 10),
        TimedMenuChoice('What do you think of the other guests?', 'doctor_generic_other_guests_friday', 0, condition = "current_day == 'Friday'", next_menu = "doctor_generic_other_guests_menu_broken"),
        TimedMenuChoice('What do you think of the other guests?', 'doctor_generic_other_guests_saturday', 0, condition = "current_day == 'Saturday'", next_menu = "doctor_generic_other_guests_menu_broken"),
        # TODO journalist: add Moody's extra investigative questions for the doctor here (find which ones)
        TimedMenuChoice("You don't have any more questions for him", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "doctor")

    $ doctor_generic_other_guests_menu_broken = TimedMenu("doctor_generic_other_guests_menu_broken", [
        TimedMenuChoice('What about Samuel Manning?', 'doctor_generic_drunk', 10),
        TimedMenuChoice('I want to talk about something else.', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "doctor")

    #---------------------------------------------------------------------
    # Drunk (used when Broken shadows the western-grove party on the hunt)
    $ drunk_generic_menu_broken = TimedMenu("drunk_generic_menu_broken", [
        TimedMenuChoice('What do you make of this place?', 'drunk_generic_manor', 10),
        TimedMenuChoice('You have the look of a man with something on his mind.', 'broken_drunk_hunt_burden', 10),
        TimedMenuChoice("Did you find anything odd in your room last night? A letter, perhaps?", 'broken_drunk_hunt_letter', 20, early_exit = True),
        TimedMenuChoice("Leave him to his flask", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "drunk")

    return
