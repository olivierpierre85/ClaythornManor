label lad_day2_morning_nohunt:
    # call black_screen_transition("The Lad - Inside") # Good ?
    scene bedroom_lad

    call change_time(11,00)

    """
    I turned down the invitation for the hunt.

    So I stayed with Amalia Baxter and the nurse.TODO introduce everyone.

    They are in the tea room, waiting for a small luncheon to be served.

    I retreated in my room.

    Now what should I do ?

    """

    $ time_left = 120

    call run_menu(TimedMenu([
            TimedMenuChoice('Meet the others in the Tea Room', 'lad_day2_evening_tea_room', 0, keep_alive = True, room = 'tea_room'),
            TimedMenuChoice('Library', 'lad_library', 40, room = 'library'), # condition not visited ?
            TimedMenuChoice('Sleep until the others return.', 'lad_day2_nohunt_cancel', early_exit = True, room = 'lad_room')
        ], is_map = True))

    "Suddenly, the hunting partying enters the li...."

    return