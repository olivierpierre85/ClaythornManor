# --------------------------------------------
#   Nurse
#           
#   Saturday - Morning
# 
#   9:00 -> 11:00
#
#   Music: chill
#
#   Position
#       - Dining Room : Everyone else
#       - Dead : Broken
#
#   Notes :
#       - TODO
# --------------------------------------------
label nurse_day2_morning:

    call change_time(9, 00, 'Morning', 'Saturday', hide_minutes = True, chapter='saturday_morning')

    $ nurse_details.add_checkpoint("nurse_day2_morning")

    call black_screen_transition("Rosalind Marsh", chapters_names[current_chapter])

    $ change_room("bedroom_nurse", irisout)

    $ play_music('chill', 3)

    """
    TODO
    """

    jump work_in_progress
