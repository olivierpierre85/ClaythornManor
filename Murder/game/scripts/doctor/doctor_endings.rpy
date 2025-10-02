label doctor_ending_overdose:

    $ doctor_details.endings.unlock('overdose')
    $ doctor_details.add_ending_checkpoint(ending=doctor_details.endings.get_item('overdose'))
    
    call death_screen_transition

    """
    You thought you could manage it, but you were mistaken.

    That last spoonful was one dose too many.

    You will have to be more careful next time.
    """

    jump ending_generic