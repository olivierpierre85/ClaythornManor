label lad_day2_evening_billiard_room:

    $ change_room('billiard_room')

    if not lad_day2_evening_billiard_room_visited:

        $ lad_day2_evening_billiard_room_visited = True

        """
        As I expected, not a lot of people are there.

        I can only see Captain Sinha sitting on a couch and the butler in the corner.

        Well at least, the bar is still there.
        """

        $ lad_day2_evening_billiard_room_menu = TimedMenu([
            TimedMenuChoice('Talk to Sushil Sinha', 'lad_day2_evening_billiard_room_captain', 20),
            TimedMenuChoice('Go to the bar to have a drink', 'lad_day2_evening_billiard_room_bar', 10),
            TimedMenuChoice('Have another drink, for the nerves', 'lad_day2_evening_billiard_room_bar_2', 10, condition = 'lad_day2_drinks == 1'),
            TimedMenuChoice('I think I still need of few more drinks', 'lad_day2_evening_billiard_room_bar_3', 30, condition = 'lad_day2_drinks == 2'),
            TimedMenuChoice('Oh what the hell, maybe I should just get plastered', 'lad_day2_evening_billiard_room_bar_4', 120, condition = 'lad_day2_drinks == 3'),
            TimedMenuChoice('Leave the room', 'lad_day2_evening_billiard_room_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ lad_day2_evening_billiard_room_menu.early_exit = False

        """
        You are back in the Billiard Room.
        """

    call run_menu(lad_day2_evening_billiard_room_menu)

    return

label lad_day2_evening_billiard_room_captain:

    """
    Captain TODO
    """

    return

label lad_day2_evening_billiard_room_bar:

    """
    There is not much of choice of drinks. So I drink a glass of sherry.
    """

    $ lad_day2_drinks = lad_day2_drinks + 1

    return

label lad_day2_evening_billiard_room_bar_2:
    
    """
    With everything that has happened, one drink is probably not enough.

    I should have another one to help me relax.

    So I pour myself another sherry.
    """

    $ lad_day2_drinks = lad_day2_drinks + 1

    return

label lad_day2_evening_billiard_room_bar_3:
    
    """
    I can't seem to be able to get rid of my anxiety.

    More drinks is probably the answer.
    """

    pause 2.0
    # TODO sound of drink pouring

    """
    After a few more drinks, the captain turns his head towards me.
    """

    captain """
    Are you ok there?

    You sure you haven't had enough for tonight?

    We may have to be sharp early tomorrow.
    """

    lad """
    Naahhh, I am fine....
    """

    """ 
    Shit, am I slurring?

    Maybe he is right.
    """

    $ lad_day2_drinks = lad_day2_drinks + 1

    return

label lad_day2_evening_billiard_room_bar_4:
    
    """
    I ignore the captain judgemental look and head again to the bar.

    Cut me some slack.
    
    These are extraordinary circumstances.

    Beside, one more can't hurt.
    """

    $ lad_day2_drunk = True

    return

label lad_day2_evening_billiard_room_cancel:
    return