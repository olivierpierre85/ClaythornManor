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
