# Endings for Psychic

label psychic_ending_lord:

    # $ lad_details.endings.unlock('poisoned')
    # $ lad_details.add_ending_checkpoint(ending = lad_details.endings.get_item('poisoned'))
    
    call death_screen_transition

    """
    You violently the staircase.

    You are not sure what happened there in the attic, but it got the best of you.
    """

    jump ending_generic


label psychic_ending_burns:
        
    $ psychic_details.intuitions.unlock('leave_castle')    
    
    call death_screen_transition

    """
    The smoke from the fire caused you to lose consciousness.

    Needless to say, you didn't survive it.

    The whole place burned down.

    A tragic ending for Claythorn Manor and everyone still within.
    """

    $ psychic_details.endings.unlock('burned')

    jump ending_generic


label psychic_ending_shot:

    call death_screen_transition

    """
    You were shot.

    That is on you for trusting strangers.

    In tough situations, sometimes the best course of action is to fight.

    Keep that in mind for the future.
    """

    $ psychic_details.endings.unlock('shot')

    jump ending_generic


label psychic_ending_escape:
    
    call survive_screen_transition

    """
    You've made it!

    And you've managed to save one person with you.

    That's not bad, and you could stop there.

    Not everybody needs a happy ending.

    And this one is as good as any.

    So it's up to you to just stop,

    Or to keep playing.
    """

    $ psychic_details.endings.unlock('escape')

    jump survived_generic

