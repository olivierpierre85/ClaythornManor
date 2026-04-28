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


label captain_ending_poisoned:

    $ captain_details.endings.unlock('poisoned')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('poisoned'))

    call death_screen_transition

    """
    You locked the wrong people away.

    Your suspicions had settled upon the household, and so you confined the household, and slept the easier for it.

    But it was never the maids, nor the footman, nor even the butler whose hand you had to fear.

    Whoever poured what was in your glass that night walked freely past your locked doors, and bid you a perfectly civil good night.

    The dead are not always killed by those they suspect.
    """

    jump ending_generic


label captain_ending_shot_butler:

    $ captain_details.endings.unlock('shot_butler')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('shot_butler'))

    call death_screen_transition

    """
    You took the man for an actor in a fine coat, and rushed him as you might have rushed a steward.

    You did not allow for the possibility that an actor in this house might be carrying a revolver.

    A man with a great deal to lose will arm himself, even if it sits ill with his manners.

    He fired only when you left him no other choice. That is, in its way, a courtesy.
    """

    jump ending_generic