label lad_day3_afternoon:

    call black_screen_transition("Ted Harring", "Sunday Afternoon")

    $ change_room("tea_room", irisout)

    call change_time(12,00, "Afternoon", "Sunday")

    """
    After leaving us in the tea room to gather our strength, Mister Sinha left to explore the mansion a bit more.

    When he came back, we were starting to feel a bit better.
    """

    captain """
    I just tried the phone, it's not working.

    So we can't call for help.

    I don't think we have a choice, we have to leave this place.

    The longer we stay here the more we are at risk something will happen to us.
    """

    psychic """
    But,... can't we stay here and wait for the police?

    They were supposed to come here today, they might arrive any moment;
    """

    captain """
    I wouldn't count on it.

    For what I understand, there is no proof anyone called the police yesterday.
    """

    psychic """
    But Miss Claythorn she said...
    """

    """
    She stops mid sentence, realizing the implication.
    """

    psychic """
    So you think it was a setup?

    That she never called the police.

    Those were just lies she told us.
    """

    captain """
    That's the most logical explanation for me.

    Nobody was around the phone calls that Miss Claythorn and her butler supposedly made.

    So there is no way to know if they actually made them.

    And there disappearence this morning probably means they were in on it together.
    
    Probably the whole staff was.
    """

    lad """
    But in on what?

    What would they want to do something like this?

    I don't understand what is happening and why!
    """

    captain """
    Me neither.

    I tried thinking about it an I have no idea why we were all asked to come here.

    But I know that was not to give us any money.

    In any case, all I know is we better leave this place as soon as possible.
    """

    psychic """
    But how?

    We are miles from the next town.

    I can't walk that far.
    """


    # TODO add call with telephone ? Room with a telephone ?

    # TODO the captain OR YOU saw a car in the garage BUT it's out of gas, AND he can't find the keys, so we'll need to walk

    # TODO captain asks about the gun room. Tell him you have it or not ?
    $ lad_day3_escape_menu = TimedMenu([
        TimedMenuChoice('Stay here with Amelia Baxter', 'lad_day3_stay', early_exit = True ),
        TimedMenuChoice('Follow Sushil Sinha', 'lad_day3_escape', early_exit = True)
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

