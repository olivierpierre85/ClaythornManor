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
            TimedMenuChoice('Go to the bar to have a drink', 'lad_day2_evening_billiard_room_bar', 20),
            # TODO talk to the butler ? To say what ????
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
    Captain
    """

    return

label lad_day2_evening_billiard_room_bar:

    """
    drink
    """

    return

label lad_day2_evening_billiard_room_cancel:
    return