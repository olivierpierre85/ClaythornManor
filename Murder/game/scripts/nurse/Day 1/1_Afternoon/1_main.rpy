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


    # TODO: Write the introduction of nurse.

    # She is coming after receiving the same invite as the others
    # But, unlike the others, she knows there is something fishy about it
    # She recognizes a scam because she is a scammer hersef.
    # She will come anyway, trying to steal enough to make her trip worth it.
    
    """
    TODO: 
    """

    jump work_in_progress

    play sound train_stopping

    $ change_room("train_station")

    pause 2.0
    

    # TODO: Write interaction with the others
    # She arrives with the same train as doctor and broken.
    # Check the doctor point of view to write the nurses
    """
    TODO 
    """

    $ change_room("inside_car")

    jump nurse_day1_evening
