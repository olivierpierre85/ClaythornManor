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