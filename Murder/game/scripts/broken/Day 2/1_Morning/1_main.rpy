# --------------------------------------------
#   Broken
#
#   Saturday - Morning
#
#   08:30 -> ...
#
#   Music: mysterious
#
#   Position
#       - Bedroom : Broken
#
#   Notes :
#       - 
# --------------------------------------------
label broken_day2_morning:

    call change_time(8, 30, 'Morning', 'Saturday', hide_minutes = True, chapter='saturday_morning')

    $ broken_details.add_checkpoint("broken_day2_morning")

    call black_screen_transition("Thomas Moody", chapters_names[current_chapter])

    $ change_room("bedroom_broken", irisout)

    $ play_music('mysterious', 2)

    """
    I wake to a thin grey light and the unfamiliar weight of a strange bed.

    For a moment I cannot place myself.

    Then it comes back to me. The manor. The mask. Thomas.

    Day two.
    """

    """
    I came through the first night without being found out, which is more than I dared hope for yesterday.

    But the hardest part is still ahead of me.

    I sit up and reach for the mask on the bedside table.
    """

    """
    Spirit gum and old leather. The smell of it is familiar enough by now.

    I fix it in place by feel, the way I have done a hundred times, and a dead man's ruined face looks back at me from the glass.

    Thomas Moody is awake.
    """

    """
    I wash and dress with care.

    A man in my supposed condition cannot be seen fumbling, nor be caught without the mask, not even for an instant.

    Whatever this day brings, I must be ready to meet it.
    """

    jump work_in_progress
