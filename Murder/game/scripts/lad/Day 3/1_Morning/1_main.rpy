label lad_day3_morning:

    call change_time(7,00)

    call black_screen_transition("Sunday")

    call change_room('lad_room')

    play sound door_knock
    
    """
    I woke up suddenly with the sound of someone knocking frantically at the door.
    """

    play sound door_knock

    psychic """
    Mister Harring are you there ?
    """
    
    """
    Miss Baxter again ?

    What could she want ?
    """

    lad """
    I am coming !
    """

    """
    I dress up in a hurry and open the door.
    """

    lad """
    Miss Baxter, what is happening ?
    """

    psychic """
    I am not sure but I don't like it.

    I woke early as usual and tried to get a cup of tea before breakfast.

    But no one is there.
    """

    lad """
    What do you mean ?
    """

    psychic """
    That the staff is gone, all of them.

    I tried the kitchen, outside, the whole place even.

    I saw nobody.
    """

    lad """
    Can't they be still asleep ?
    """

    psychic """
    Oh Mister Harring, that's impossible.

    They are supposed to be awake since dawn to get the house ready for the day.

    They couldn't have just slept in.

    I also went to check on misses Claythorn and she doesn't answer.
    """

    lad """
    Don't worry, I am sure it's not so bad.
    """

    psychic """
    I don't know.

    But I don't want to keep on searching alone.

    Would please accompany me to check on the others ?
    """

    lad """
    Well, I am awake now so why not.

    If that can appease you.
    """

    """
    We decide it's better we check again every room together.

    So first we go to ...
    """

    $ time_left = 90
    # TODO test every room before it's over
    # WHERE TO FIND the captain ? in it's room ?
    call run_menu(TimedMenu([
        TimedMenuChoice('Library', 'lad_day3_morning_library', 10, room = 'library'), # condition not already visited ?
        TimedMenuChoice('Richard III Bedroom', 'lad_day3_morning_broken_room', 20, room = 'broken_room'),
        TimedMenuChoice('Edward II Bedroom', 'lad_day3_morning_doctor_room', 20, room = 'doctor_room'),
        TimedMenuChoice('Captain', 'lad_day3_morning_captain_room', 20, room = 'captain_room'),
        TimedMenuChoice('Go to sleep and hope for the best.', 'lad_day3_morning_sleep', early_exit = True, room = 'lad_room'),
    ], is_map = True))

    """
    I believe we looked everywhere.

    So we settled in the tea room to discuss what will be our next move.
    """

    captain """
    That's unbelievable, but it looks like we are the three remaining living souls in this place.
    """

    return

label lad_day3_morning_captain_room:

    call change_room('captain_room')

    play sound door_knock

    lad """
    Captain !

    Are you here ?
    """

    captain """
    Yes, who is it ?
    """

    return 

    