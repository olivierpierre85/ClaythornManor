label nurse_config_menu:

    #---------------------------------------------------------------------
    # Drunk
    $ drunk_generic_menu_nurse = TimedMenu("drunk_generic_menu_nurse", [
        TimedMenuChoice('What do you think of this weather?', 'drunk_generic_weather_friday_dinner', 10, condition = condition_friday_dinner),
        TimedMenuChoice('Tell me more about yourself.', 'drunk_generic_background_nurse', 20, linked_choice ="drunk_generic_heroic_act_nurse", next_menu="drunk_generic_background_nurse"),
        TimedMenuChoice('Why were you invited here?', 'drunk_generic_heroic_act_nurse', 20, condition = "is_linked_choice_hidden('drunk_generic_menu_nurse', 'drunk_generic_heroic_act_nurse')"),
        TimedMenuChoice('What do you think of this place?', 'drunk_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'drunk_generic_age', 20),
        TimedMenuChoice('What room are you in?', 'drunk_generic_room_friday', 10, condition = condition_friday_dinner),
        TimedMenuChoice('What room are you in?', 'drunk_generic_room_nurse', 10, condition = "not " + condition_friday_dinner),
        TimedMenuChoice('What do you think of the other guests?', 'drunk_generic_other_guests_friday_dinner', 10, condition = condition_friday_dinner),
        TimedMenuChoice('What do you think of the other guests?', 'drunk_generic_other_guests_friday_nurse', 10, condition = "not " + condition_friday_dinner + " and not " + condition_saturday),
        TimedMenuChoice('What do you think of the other guests?', 'drunk_generic_other_guests_saturday_nurse', 0, keep_alive = True, next_menu='drunk_generic_other_guests_menu_nurse', condition = condition_saturday),
        TimedMenuChoice("You don't have anymore questions for him", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "drunk")

    $ drunk_generic_other_guests_menu_nurse = TimedMenu("drunk_generic_other_guests_menu_nurse", [
        TimedMenuChoice('What do you think of Lady Claythorn?', 'drunk_generic_host_saturday_nurse', 10, condition = condition_saturday),
        TimedMenuChoice('What do you think of Daniel Baldwin?', 'drunk_generic_doctor_saturday_nurse', 10, condition = condition_saturday),
        TimedMenuChoice('What do you think of Sushil Sinha?', 'drunk_generic_captain_saturday_nurse', 10, condition = condition_saturday),
        TimedMenuChoice('Talk about something else', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "drunk")

    #---------------------------------------------------------------------
    # Psychic
    $ psychic_generic_menu_nurse = TimedMenu("psychic_generic_menu_nurse", [
        TimedMenuChoice('What do you think of this weather?', 'psychic_generic_weather_saturday_nurse', 10, condition = condition_saturday),
        TimedMenuChoice('Tell me more about yourself.', 'psychic_generic_background_nurse', 20, linked_choice = "psychic_generic_heroic_act_nurse"),
        TimedMenuChoice('Why were you invited here?', 'psychic_generic_heroic_act_nurse', 20, condition = "is_linked_choice_hidden('psychic_generic_menu_nurse', 'psychic_generic_heroic_act_nurse')"),
        TimedMenuChoice('What do you think of this place?', 'psychic_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'psychic_generic_age_nurse', 10),
        TimedMenuChoice('What room are you in?', 'psychic_generic_room', 10),
        TimedMenuChoice('What do you think of the other guests?', 'psychic_generic_other_guests_saturday_morning', 0, keep_alive = True, condition = condition_saturday, next_menu = 'psychic_generic_other_guests_menu_nurse'),
        TimedMenuChoice("You don't have anymore questions for her", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "psychic")

    $ psychic_generic_other_guests_menu_nurse = TimedMenu("psychic_generic_other_guests_menu_nurse", [
        TimedMenuChoice('What do you think of Samuel Manning?', 'psychic_generic_drunk_saturday_morning', 10, condition = condition_saturday),
        TimedMenuChoice('What do you think of Sushil Sinha?', 'psychic_generic_captain_saturday_morning', 10, condition = condition_saturday),
        TimedMenuChoice('What do you think of Lady Claythorn?', 'psychic_generic_host_saturday_morning', 10, condition = condition_saturday),
        TimedMenuChoice('Talk about something else', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "psychic")

    #---------------------------------------------------------------------
    # Host
    $ host_generic_menu_nurse = TimedMenu("host_generic_menu_nurse", [
        TimedMenuChoice('Tell me more about yourself.', 'host_generic_background_nurse', 20, linked_choice ="host_generic_invite_nurse"),
        TimedMenuChoice('Why did you invite us here?', 'host_generic_invite_nurse', 20, condition = "is_linked_choice_hidden('host_generic_menu_nurse', 'host_generic_invite_nurse')"),
        TimedMenuChoice('What do you think of the other guests?', 'host_generic_other_guests_nurse', 10),
        TimedMenuChoice('What do you think of this place?', 'host_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'host_generic_age', 10),
        TimedMenuChoice('What room are you in?', 'host_generic_room', 10),
        TimedMenuChoice("You don't have anymore questions for her", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "host")

    return