# --------------------------------------------
#   Captain endings
# --------------------------------------------

label captain_ending_strangled:

    $ captain_details.endings.unlock('strangled')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('strangled'))

    call death_screen_transition

    """
    You pressed your hostess at the wrong moment, in the wrong place.

    You felt safe with your gun next to you.

    But a rifle is a poor weapon when the threat comes silently from behind.

    Next time you want to confront someone, choose your ground wisely.
    """

    jump ending_generic


label captain_ending_shot_in_woods:

    $ captain_details.endings.unlock('shot_in_woods')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('shot_in_woods'))

    call death_screen_transition

    """
    You were led into the woods by a man who suspected of wishing you harm.

    You knew the danger, yet good manners compelled you to proceed regardless.

    It is curious how the fear of causing a scene is sometimes stronger than any other.
    """

    jump ending_generic
