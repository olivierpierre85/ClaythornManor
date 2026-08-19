# --------------------------------------------
#   Host endings
# --------------------------------------------

label host_ending_shot_tea_room:

    $ host_details.endings.unlock('shot_tea_room')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('shot_tea_room'))

    call death_screen_transition

    """
    Captain Sinha asked you for a single word, and you had not a single word to give him.

    So the mask came off in front of witnesses, and the man who had been giving you your orders all weekend came down to see what had become of his weekend.

    The bullet was never meant for you.

    That is the whole of your part, in the end.

    You had been standing in the wrong corner of somebody else's play since the day you took the fee.
    """

    jump ending_generic
