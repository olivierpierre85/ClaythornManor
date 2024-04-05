# --------------------------------------------
#   Doctor
#           
#   Friday - Afternoon
#   
#   14:00 -> 18:30
#
#   Music: Chill, upbeat
#
#   Alive: Everyone
#
#   Notes : 
#       - 
# --------------------------------------------
label doctor_introduction:

    call change_time(14,00, 'Arrival', 'Friday', hide_minutes = True)

    call black_screen_transition("Daniel Baldwin", "Friday Afternoon")

    scene train_inside with irisout 

    play sound train_moving loop

    $ play_music('chill')

    """
    I feel anxious.

    More than I usually do.

    It has been some time since I've been away for this long.

    I wish I could avoid it, but of course, I can't.

    The money offered is too tempting.

    Yet, it's going to be a struggle.

    My gaze shifts to my bag, and I hesitate for a moment.

    I could take the edge off now.

    But it's a terrible idea, and I'm well aware of that.

    I don't want to leave a poor impression.

    Besides, I have a feeling I'll need to be fully alert this weekend.

    I'm conscious of all this.

    Yet, despite it all, I find myself grabbing my bag and heading to the bathroom.
    """

    play sound train_stopping

    """
    The train is stopping.

    Too late for that now.
    """

    scene train_station

    pause 5.0
    
    """
    I gather my things and leave the train.
    """

    pause 1.0

    """
    TODO: Meet BROKEN AND NURSE
    """

    jump work_in_progress
