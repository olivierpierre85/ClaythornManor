label lad_day2_morning_nohunt:
    # call black_screen_transition("The Lad - Inside") # Good ?
    scene bedroom_lad

    call change_time(11,00)

    call change_floor(2)

    """
    I turned down the invitation for the hunt.

    So I stayed with Amalia Baxter and the Rosalind Marsh.

    They are in the tea room, waiting for a small luncheon to be served.

    I retreated in my room to change.

    Now what should I do ?

    """

    $ time_left = 240

    call run_menu(TimedMenu([
            TimedMenuChoice('Meet the others in the Tea Room', 'lad_day2_evening_tea_room', 120, room = 'tea_room'),
            TimedMenuChoice('Library', 'lad_library', 10, room = 'library'), # condition not visited ?
            TimedMenuChoice('Take a nap until the others return', 'lad_day2_nohunt_cancel', early_exit = True, room = 'lad_room'),
            TimedMenuChoice('Richard III Bedroom', 'lad_day2_broken_room', 20, room = 'broken_room')
        ], is_map = True))

    """
    Suddenly, I hear noises from the entrance hall.
    
    I decide to go and see what's happening.
    """

    jump lad_day2_afternoon

label lad_day2_broken_room:

    scene bedroom_broken

    if lad_day2_breakfast_follow:

        """
        The poor man is still there. I don't think he moved.
        """

    else:

        """
        I don't know what kind of macabre feeling made me come here.

        But in case I had doubts, Thomas Moody is there. Not breathing.

        Gosh.
        """

    """
    Well, now that I am here. Maybe I should take a look quickly . 

    Something might help me understand what happened.
    """
    # TODO FIRST REAL INVESTIGATiON CLUE

    return