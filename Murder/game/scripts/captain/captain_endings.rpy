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
    You were led into the trees by a man who had taken the measure of you on Friday evening.

    There was no battle in your past, and he had guessed as much.

    Perhaps, if you had left your war stories in the drawing room, he would have had no reason to write that letter at all.
    """

    jump ending_generic
