# --------------------------------------------
#   Nurse
#           
#   Friday - Afternoon
#   
#   14:00 -> 16:30
#
#   Music: Chill, upbeat
#
#   Alive: Everyone
#
# --------------------------------------------
label nurse_introduction:

    call change_time(14, 0, 'Arrival', 'Friday', hide_minutes=True, chapter='friday_afternoon')

    call black_screen_transition("", "Rosalind Marsh")

    $ change_room("train_inside", irisout)

    play sound train_moving loop

    $ play_music('chill')

    """
    TODO
    """

    jump work_in_progress

    # play sound train_stopping

    # $ change_room("train_station")

    # pause 2.0
    
    # """
    # TODO 
    # """

    # $ change_room("inside_car")

    # jump nurse_day1_evening
