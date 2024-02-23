# Endings for Psychic

label psychic_ending_lord:

    # $ lad_details.endings.unlock('poisoned')
    # $ lad_details.add_ending_checkpoint(ending = lad_details.endings.get_item('poisoned'))
    
    call death_screen_transition

    $ play_music('mysterious')

    """
    You violently fell in staircase.

    Nervously fighting o;
    """

    jump ending_generic