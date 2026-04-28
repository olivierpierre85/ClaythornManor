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


label captain_ending_burned:

    $ captain_details.endings.unlock('burned')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('burned'))

    call death_screen_transition

    """
    You took the man at his word, after he had twice told you he had lied.

    Of all the night's small mistakes, that was the one that had no remedy.

    There was no need of poison, nor of further bullets, nor of any of the small careful violences a household provides.

    A locked door, and a candle laid carelessly close to a curtain, will cover a great many things by morning.

    The manor burnt to its foundations before the dawn.

    The fallen tree across the road was found, in due course, to have been cut.

    Of the gentleman behind it all, no trace was ever recovered.
    """

    jump ending_generic


label captain_ending_shot_butler:

    $ captain_details.endings.unlock('shot_butler')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('shot_butler'))

    call death_screen_transition

    """
    You read the man rightly. A wrist that still, on a hand that holds a revolver, is not the wrist of any honest butler.

    And you went for him all the same.

    There is a courage in that, of a sort, and there is a folly in it of another sort, and the bullet does not greatly distinguish between them.

    He fired only when you left him no other choice. That is, in its way, a courtesy.
    """

    jump ending_generic