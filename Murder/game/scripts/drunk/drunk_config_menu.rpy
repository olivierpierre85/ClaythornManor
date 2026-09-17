label drunk_config_menu:

    #---------------------------------------------------------------------
    # Saturday evening, locked in his room: he talks the weekend over with
    # himself. Every topic is a piece of the picture. The letter, the
    # telephone call and the butler's face are the three that make the
    # picture whole (drunk_day2_evening_think_conclusion counts them).
    $ drunk_day2_evening_menu_think = TimedMenu("drunk_day2_evening_menu_think", [
        TimedMenuChoice('The letter, and who could have written it', 'drunk_day2_evening_think_letter', 20),
        TimedMenuChoice('Thomas Moody, dead in his bed', 'drunk_day2_evening_think_moody', 10),
        TimedMenuChoice("Lady Claythorn's telephone call", 'drunk_day2_evening_think_telephone', 10),
        TimedMenuChoice('The butler', 'drunk_day2_evening_think_butler', 20),
        TimedMenuChoice('Miss Baxter, and the way she looks at the boy', 'drunk_day2_evening_think_psychic', 10),
        TimedMenuChoice('Why you, of all people', 'drunk_day2_evening_think_self', 10),
        TimedMenuChoice("You have thought enough", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_left = "drunk")

    return
