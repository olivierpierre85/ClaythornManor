# Endings for Psychic

label psychic_ending_lord:

    # $ lad_details.endings.unlock('poisoned')
    # $ lad_details.add_ending_checkpoint(ending = lad_details.endings.get_item('poisoned'))
    
    call death_screen_transition

    """
    You violently fell in staircase.

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


