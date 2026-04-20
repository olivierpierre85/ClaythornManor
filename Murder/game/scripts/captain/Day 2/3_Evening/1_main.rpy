# --------------------------------------------
#   Captain
#
#   Saturday - Evening
#
#   15:00 -> 23:00
#
#   Music: sad
#
#   Position
#       - House: captain, lad, psychic, nurse, host, butler
#       - Dead : broken, doctor, drunk (confined)
#
#   Notes:
#       - Captain takes charge returning from the woods
#       - Gets the butler's key after escorting Manning
# --------------------------------------------

label captain_day2_evening:

    $ captain_details.add_checkpoint("captain_day2_evening")

    call change_time(15, 00, 'Evening', 'Saturday', chapter='saturday_evening')

    call black_screen_transition("Sushil Sinha", chapters_names[current_chapter])

    $ change_room('entrance_hall', irisout)

    $ play_music('sad', 2)

    """
    The walk back from the western grove felt twice as long as it ought to have.

    Doctor Baldwin was a heavier man than he appeared, and the makeshift stretcher was poor work.

    But that is the sort of thought one keeps firmly to oneself.

    As we carry him through the entrance hall, I hear footsteps on the stair.

    Miss Baxter and Miss Marsh come to a halt at the bottom, and both their faces change at once.
    """

    call common_day2_evening_entrance_dialog

    jump work_in_progress
