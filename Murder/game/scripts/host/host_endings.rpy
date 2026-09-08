# --------------------------------------------
#   Host endings
# --------------------------------------------

label host_ending_shot_tea_room:

    $ host_details.endings.unlock('shot_tea_room')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('shot_tea_room'))

    call death_screen_transition

    """
    Captain Sinha asked you for one simple thing, and you could not give it to him.

    That was one mistake too many, and it led to this unfortunate end.

    You are getting closer to the truth.

    If you want to reach the end of this story, you should stop making bad decisions like this.
    """

    jump ending_generic


label host_ending_die_in_sleep:

    $ host_details.endings.unlock('die_in_sleep')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('die_in_sleep'))

    call death_screen_transition

    """
    You do not wake up.

    You died in the night, in your clothes, behind a locked door with a chair wedged beneath the handle.

    You told nobody in that house what you truly were, so you were entirely alone in the night.

    In dangerous situations, it is sometimes best to have an ally to rely on.
    """

    jump ending_generic


label host_ending_shot_in_car:

    $ host_details.endings.unlock('shot_in_car')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('shot_in_car'))

    call death_screen_transition

    """
    You got into a car in the dark with a man you barely knew.

    There were plenty of signs that could have warned you about the risk, but you ignored them.
    """

    jump ending_generic
