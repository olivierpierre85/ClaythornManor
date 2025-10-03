label doctor_ending_overdose:

    $ doctor_details.endings.unlock('overdose')
    $ doctor_details.add_ending_checkpoint(ending=doctor_details.endings.get_item('overdose'))
    
    call death_screen_transition

    """
    You thought you could manage it, but you were mistaken.

    That last spoonful was one too many.

    You will have to be more careful next time.
    """

    # IF too difficult to understand (the stillness of my room is unbearable), add this ONLY if late
    # if (all_choices IS NOT LAUDANUM DEATH choice)

    #     """
    #     Maybe if you have been occupied, you could have avoided it.
    #     """

    jump ending_generic