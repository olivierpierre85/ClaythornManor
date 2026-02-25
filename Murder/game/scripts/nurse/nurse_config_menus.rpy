label nurse_config_menu:

    #---------------------------------------------------------------------
    # Drunk
    $ drunk_generic_menu_nurse = TimedMenu("drunk_generic_menu_nurse", [
        TimedMenuChoice('What do you think of this weather?', 'drunk_generic_weather_friday_dinner', 10, condition = condition_friday_dinner),
        TimedMenuChoice('Tell me more about yourself.', 'drunk_generic_background_nurse', 0, linked_choice ="drunk_generic_heroic_act_nurse", next_menu="drunk_generic_background_nurse"),
        TimedMenuChoice('Why were you invited here?', 'drunk_generic_heroic_act_nurse', 30, condition = "is_linked_choice_hidden('drunk_generic_menu_nurse', 'drunk_generic_heroic_act_nurse')"),
        TimedMenuChoice('What do you think of this place?', 'drunk_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'drunk_generic_age', 10),
        TimedMenuChoice('What room are you in?', 'drunk_generic_room_friday', 10, condition = condition_friday_dinner),
        TimedMenuChoice('What room are you in?', 'drunk_generic_room_nurse', 10, condition = "not " + condition_friday_dinner),
        TimedMenuChoice('What do you think of the other guests?', 'drunk_generic_other_guests_friday_dinner', 10, condition = condition_friday_dinner),
        TimedMenuChoice('What do you think of the other guests?', 'drunk_generic_other_guests_friday_nurse', 10, condition = "not " + condition_friday_dinner + " and not " + condition_saturday),
        TimedMenuChoice('What do you think of the other guests?', 'drunk_generic_other_guests_saturday_nurse', 0, keep_alive = True, next_menu='drunk_generic_other_guests_menu_nurse', condition = condition_saturday),
        TimedMenuChoice("You don't have anymore questions for him", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "drunk")

    return