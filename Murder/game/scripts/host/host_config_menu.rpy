label host_config_menu:

    #---------------------------------------------------------------------
    # Drunk (Samuel Manning, seated on her left at the Friday dinner)
    # She cannot ask a guest why he was invited, so the "heroic act" question
    # is dressed up as a hostess asking him to tell the tale himself.
    # The food is not in here on purpose: he gives her his verdict on the sole
    # before she can ask him anything (host_day1_dinner_drunk_food).
    $ drunk_generic_menu_host = TimedMenu("drunk_generic_menu_host", [
        TimedMenuChoice('What do you think of this weather?', 'drunk_generic_weather_friday_dinner_host', 10),
        TimedMenuChoice('Tell me more about yourself.', 'drunk_generic_background_host', 20, linked_choice = "drunk_generic_wife"),
        TimedMenuChoice('Ask him more about his wife', 'drunk_generic_wife', 20, condition = "is_linked_choice_hidden('drunk_generic_menu_host', 'drunk_generic_wife')"),
        TimedMenuChoice('What do you think of this place?', 'drunk_generic_manor_host', 10),
        TimedMenuChoice('How old are you?', 'drunk_generic_age_host', 20),
        TimedMenuChoice('What do you think of the other guests?', 'drunk_generic_other_guests_friday_dinner', 10),
        TimedMenuChoice("You don't have any more questions for him", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_left = "drunk")

    # Moody (Thomas Moody, seated on her right at the Friday dinner) has no
    # generic menu of his own. He asks all the questions himself, so the whole
    # exchange is written out in host_day1_dinner_broken.

    return
