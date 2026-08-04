label host_config_menu:

    #---------------------------------------------------------------------
    # Drunk (Samuel Manning, seated on her left at the Friday dinner)
    # She cannot ask a guest why he was invited, so the "heroic act" question
    # is dressed up as a hostess asking him to tell the tale himself.
    $ drunk_generic_menu_host = TimedMenu("drunk_generic_menu_host", [
        TimedMenuChoice('I hope the dinner is to your liking?', 'drunk_generic_food_host', 20),
        TimedMenuChoice('What is it that you do, Mr Manning?', 'drunk_generic_background_host', 20, linked_choice = "drunk_generic_heroic_act_host"),
        TimedMenuChoice('Ask him to tell you, in his own words, why he is here', 'drunk_generic_heroic_act_host', 20, condition = "is_linked_choice_hidden('drunk_generic_menu_host', 'drunk_generic_heroic_act_host')"),
        TimedMenuChoice('What do you think of this place?', 'drunk_generic_manor', 10),
        TimedMenuChoice('Have they given you a comfortable room?', 'drunk_generic_room_friday', 10),
        TimedMenuChoice('What do you think of the other guests?', 'drunk_generic_other_guests_friday_dinner', 10),
        TimedMenuChoice('Turn back to the rest of the table', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_left = "drunk")

    #---------------------------------------------------------------------
    # Broken (Thomas Moody, seated on her right at the Friday dinner)
    # He asks the questions. The menu holds her answers, not his questions.
    $ host_day1_dinner_broken_menu = TimedMenu("host_day1_dinner_broken_menu", [
        TimedMenuChoice('Give him the story you were taught', 'host_day1_dinner_broken_tradition', 20, early_exit = True),
        TimedMenuChoice('Say as little as you can decently say', 'host_day1_dinner_broken_vague', 20, early_exit = True),
        TimedMenuChoice('Turn the question back on him', 'host_day1_dinner_broken_deflect', 20, early_exit = True),
    ], image_right = "broken")

    return
