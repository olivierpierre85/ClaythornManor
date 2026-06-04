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


label captain_ending_bludgeoned:

    $ captain_details.endings.unlock('bludgeoned')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('bludgeoned'))

    call death_screen_transition

    """
    You laid hands upon a frightened woman, and the man who answers for her did not hesitate.

    A confrontation is not something to be taken lightly.

    Sometimes, it is best to keep your doubts to yourself.
    """

    jump ending_generic


label captain_ending_throat_cut:

    $ captain_details.endings.unlock('throat_cut')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('throat_cut'))

    call death_screen_transition

    """
    You thought a locked door enough to see you safely to the morning.

    But a bolt is no great obstacle.

    The person who came for you was practised, and quiet, and as patient as they needed to be.

    You knew nothing of it until there was nothing left to know.
    """

    jump ending_generic


label captain_ending_car_ambush:

    call death_screen_transition

    $ captain_details.endings.unlock('car_ambush')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('car_ambush'))

    """
    You trusted the open road more than the house you fled.

    But the road was theirs as surely as the manor was.

    A stalled engine, a quiet wood, and a man waiting where the trees came close.

    You never saw the one who fired.

    A leader does not get the rest of his party killed simply because he could not bear to wait a little longer.
    """

    jump ending_generic


label captain_ending_shot_fleeing:

    call death_screen_transition

    $ captain_details.endings.unlock('shot_fleeing')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('shot_fleeing'))

    """
    You set out alone, on foot, into open country you did not know.

    A soldier ought to have known better than to cross such ground without cover.

    But you were no soldier, whatever the medals said.

    The shot came from the treeline, and you did not hear the second one.
    """

    jump ending_generic


label captain_ending_run_over:

    call death_screen_transition

    $ captain_details.endings.unlock('run_over')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('run_over'))

    """
    You left a sick woman behind and set out alone, certain the open road was safer than the house.

    You heard the motor in good time.

    A real soldier would have read it for what it was and taken to the trees.

    Instead you stood in the road and waited to be saved.

    The road belonged to them, just as the manor had.
    """

    jump ending_generic


label captain_ending_survives:

    call survive_screen_transition

    $ play_music('end_credits')

    $ captain_details.endings.unlock('survives')
    $ captain_details.add_ending_checkpoint(ending=captain_details.endings.get_item('survives'))

    """
    You took the only motor that ran, and you took it alone.

    You told yourself it was sense, and perhaps it was.

    The others would only have slowed you, and the road was no place for a frightened woman or a half-grown boy.

    That is what you told yourself, all the long miles to the town.

    You reached it alive.

    A coward reaches it alive too.

    Once a coward, always a coward.
    """

    $ is_death = False

    jump ending_generic