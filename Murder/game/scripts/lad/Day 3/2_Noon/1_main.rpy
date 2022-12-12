label lad_day3_noon:

    call black_screen_transition("Ted Harring", "Sunday Afternoon")

    $ change_room("tea_room", irisout)

    call change_time(12,00, "Afternoon", "Sunday")

    """
    We sat down a few minutes to gather our senses.

    When Miss Baxter and I felt a bit better we started discussing our options.
    """

    psychic """

    test
    """

    lad """
    test
    """

    # TODO add call with telephone ? Room with a telephone ?

    # TODO the captain OR YOU saw a car in the garage BUT it's out of gas, AND he can't find the keys, so we'll need to walk

    # TODO captain asks about the gun room. Tell him you have it or not ?
    $ lad_day3_escape_menu = TimedMenu([
        TimedMenuChoice('Stay here with Amelia', 'lad_day3_stay', early_exit = True ),
        TimedMenuChoice('Follow Sushil', 'lad_day3_escape', early_exit = True)
    ], image_left = "psychic",  image_right = "captain")
    $ time_left = 1
    call run_menu(lad_day3_escape_menu)

    # TODO handle possible endings
    # TODO add switch on the 
    # TODO more logic in ending names
    if lad_day3_gun_downed:
        jump lad_gun_downed_ending
    elif lad_day3_poisoned:
        jump lad_ending_day3_poisoned

