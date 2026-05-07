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

    With you in it.
    """

    jump ending_generic


label captain_ending_shot_butler:

    $ captain_details.endings.unlock('shot_butler')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('shot_butler'))

    call death_screen_transition

    """
    You read your opponent rightly.

    A dangerous man to engage, not an ordinary butler.

    And you went for him all the same.

    Years of staying on the sidelines of battles made you want to try yourself at a real one.

    There is a courage in that, but also folly.

    And the bullet does not greatly distinguish between them.

    Your first battle will also be your last one.
    """

    jump ending_generic


label captain_ending_throat_slit:

    $ captain_details.endings.unlock('throat_slit')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('throat_slit'))

    call death_screen_transition

    """
    You took young Mr Harring into your confidence, and thought a locked door enough to see you safely to the morning.

    A frightened young man, fresh from his first taste of real danger, cannot keep a secret long when pressed.

    Your suspicions reached the wrong ears within the hour.

    A bolt is no great obstacle to those who keep the keys of a house.

    The man who came for you was practised, and quiet, and quite as patient as he needed to be.

    You knew nothing of it until there was nothing left to know.
    """

    jump ending_generic