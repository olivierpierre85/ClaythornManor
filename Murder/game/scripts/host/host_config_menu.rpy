label host_config_menu:

    # Moody's own interview answers stand in for her "tell me about yourself"
    # question, so the two must never be offered twice.
    $ moody_deflected = "is_choice_already_chosen('host_day1_dinner_broken_menu', 'host_day1_dinner_broken_deflect')"

    #---------------------------------------------------------------------
    # Drunk (Samuel Manning, seated on her left at the Friday dinner)
    # She cannot ask a guest why he was invited, so the "heroic act" question
    # is dressed up as a hostess asking him to tell the tale himself.
    # The food is not in here on purpose: he gives her his verdict on the sole
    # before she can ask him anything (host_day1_dinner_drunk_food).
    $ drunk_generic_menu_host = TimedMenu("drunk_generic_menu_host", [
        TimedMenuChoice('What do you think of this weather?', 'drunk_generic_weather_friday_dinner_host', 10),
        TimedMenuChoice('Tell me more about yourself.', 'drunk_generic_background_host', 20, linked_choice = "drunk_generic_heroic_act_host"),
        TimedMenuChoice('Ask him to tell you, in his own words, why he is here', 'drunk_generic_heroic_act_host', 20, condition = "is_linked_choice_hidden('drunk_generic_menu_host', 'drunk_generic_heroic_act_host')"),
        TimedMenuChoice('What do you think of this place?', 'drunk_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'drunk_generic_age_host', 20),
        TimedMenuChoice('What room are you in?', 'drunk_generic_room_friday', 10),
        TimedMenuChoice('What do you think of the other guests?', 'drunk_generic_other_guests_friday_dinner', 10),
        TimedMenuChoice("You don't have any more questions for him", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_left = "drunk")

    #---------------------------------------------------------------------
    # Broken (Thomas Moody, seated on her right at the Friday dinner)
    # He opens by asking her where the award came from - see
    # host_day1_dinner_broken_menu below - and only then does she get her own
    # questions. Turning his question back on him is itself the "tell me about
    # yourself" answer, so that choice drops out of this menu when she used it,
    # and the invitation question opens on the back of it instead.
    $ broken_generic_menu_host = TimedMenu("broken_generic_menu_host", [
        TimedMenuChoice('What do you think of this weather?', 'broken_generic_weather_friday', 10),
        TimedMenuChoice('Tell me more about yourself.', 'broken_generic_background_host', 20, linked_choice = "broken_generic_heroic_act_host", condition = "not " + moody_deflected),
        TimedMenuChoice('Ask him to tell you, in his own words, why he is here', 'broken_generic_heroic_act_host', 20, condition = "is_linked_choice_hidden('broken_generic_menu_host', 'broken_generic_heroic_act_host') or " + moody_deflected),
        TimedMenuChoice('What do you think of this place?', 'broken_generic_manor_host', 10),
        TimedMenuChoice('How old are you?', 'broken_generic_age_host', 10),
        TimedMenuChoice('What room are you in?', 'broken_generic_room_host', 10),
        TimedMenuChoice('What do you think of the other guests?', 'broken_generic_other_guests_friday_dinner_host', 10),
        TimedMenuChoice("You don't have any more questions for him", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "broken")

    #---------------------------------------------------------------------
    # Her three possible answers to Moody's question about the award. Opened
    # once, from host_day1_dinner_broken, before broken_generic_menu_host.
    $ host_day1_dinner_broken_menu = TimedMenu("host_day1_dinner_broken_menu", [
        TimedMenuChoice('Give him the story you were taught', 'host_day1_dinner_broken_tradition', 20, early_exit = True),
        TimedMenuChoice('Say as little as you can decently say', 'host_day1_dinner_broken_vague', 20, early_exit = True),
        TimedMenuChoice('Turn the question back on him', 'host_day1_dinner_broken_deflect', 20, early_exit = True),
    ], image_right = "broken")

    return
