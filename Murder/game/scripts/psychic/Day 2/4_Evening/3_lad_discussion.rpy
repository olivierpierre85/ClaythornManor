label psychic_day2_evening_lad_discussion:

    $ change_room('psychic_room', dissolve)

    pause 2.0

    """
    After a little while, someone knocks at my door.
    """

    call common_day2_evening_lad_psychic_discussion_1

    call common_day2_evening_lad_psychic_discussion_2

    lad """
    Not really. About what?
    """

    call change_time(22, 30)

    $ time_left = 30

    call lad_generic

    psychic """
    I believe it's getting quite late.

    We ought to get some rest now.
    """

    lad """
    Of course, I'll see you tomorrow.
    """
    
    return
