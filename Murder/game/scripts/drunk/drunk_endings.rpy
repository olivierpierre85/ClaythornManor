# --------------------------------------------
#   Drunk endings
# --------------------------------------------

label drunk_ending_despair:

    $ drunk_mode = False

    $ drunk_details.endings.unlock('despair')
    $ drunk_details.add_ending_checkpoint(ending=drunk_details.endings.get_item('despair'))

    call death_screen_transition

    """
    You went into the woods with a full flask, and you came out of them the way a drunk comes out of everything.

    Daniel Baldwin was dead in the fern, and you had done it, and you could not say whether you had meant to.

    That is the whole of what the drink has left you. You cannot even tell your own crimes from your own accidents.

    There was a letter on your desk on Friday night. You read it, and you reached for the bottle, because that is what you always do.

    You are going to have to find another thing to do.
    """

    jump ending_generic


label drunk_ending_spared:

    $ drunk_details.endings.unlock('spared')
    $ drunk_details.add_ending_checkpoint(ending=drunk_details.endings.get_item('spared'))

    call death_screen_transition

    """
    You lowered the rifle.

    It was the decent thing, and it was the only decent thing anybody did in that house all weekend, and it killed you.

    Daniel Baldwin was not the man who let Eleanor die. Perhaps he was. You will never know now.

    But the letter was not written by a stranger. Whoever wrote it knows what he is, and wanted him dead, and had you brought here to do it.

    When you would not, they did it themselves, and they tidied you away with him.

    Some things are wrong, and you know they are wrong, and you have to do them anyway. Nothing in Claythorn Manor moves until that man is in the ground.
    """

    jump ending_generic


label drunk_ending_throat_cut:

    $ drunk_mode = False

    $ drunk_details.endings.unlock('throat_cut')
    $ drunk_details.add_ending_checkpoint(ending=drunk_details.endings.get_item('throat_cut'))

    call death_screen_transition

    """
    Nobody came in the night.

    Nobody needed to.

    In the morning Captain Sinha will open that door and see what you left him, and he will say a man with a key did it, and everybody will nod.

    You have watched juries nod like that for twenty years. It is what people do when they have decided not to see something.

    You had a bottle, a razor, and a locked door, and you found the one use for the three of them that ended with you dead.

    There was another.
    """

    jump ending_generic


label drunk_ending_silenced:

    $ drunk_details.endings.unlock('silenced')
    $ drunk_details.add_ending_checkpoint(ending=drunk_details.endings.get_item('silenced'))

    call death_screen_transition

    """
    You were right.

    You stood at a locked door and told a whole house that there was a killer among them, and you were right about every word of it.

    And the man who shot the doctor this afternoon, who could not walk straight on Friday and could not hold a spoon this morning, was never going to be believed.

    You have known that about yourself for years. You made a living out of it.

    But one person in that corridor believed you.

    They had the key.
    """

    jump ending_generic


label drunk_ending_found_out:

    $ drunk_details.endings.unlock('found_out')
    $ drunk_details.add_ending_checkpoint(ending=drunk_details.endings.get_item('found_out'))

    call death_screen_transition

    """
    Captain Sinha stood in the doorway and saw a cut throat and did not come closer.

    The butler came closer.

    That was always the difference between the two of them, and you had a whole day in that bed to think about it.

    You watched a woman move two plates, and you knew what it meant, and you sat behind a door and let it happen.

    A man who does nothing is not a witness. He is only a man who was there.
    """

    jump ending_generic


label drunk_ending_survived:

    call survive_screen_transition

    $ play_music('end_credits')

    $ drunk_details.endings.unlock('survived')
    $ drunk_details.add_ending_checkpoint(ending=drunk_details.endings.get_item('survived'))

    """
    You lay dead for a day and a night, and you walked out of Claythorn Manor on your own two feet.

    You know who wrote the letter now. You know why you were on the list, and you know whose son was sleeping on the dining room floor.

    You could not save Daniel Baldwin, because you were the one who killed him.

    But you put two plates back where they belonged, and a boy who was meant to sleep through it slept through it.

    Nobody will believe a word of what you have to tell. You are Samuel Manning. That has never stopped you before.
    """

    $ is_death = False

    jump ending_generic
