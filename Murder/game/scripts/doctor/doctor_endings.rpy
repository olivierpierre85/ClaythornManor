label doctor_ending_run_over:

    $ doctor_details.endings.unlock('run_over')
    $ doctor_details.add_ending_checkpoint(ending=doctor_details.endings.get_item('run_over'))

    call death_screen_transition

    """
    You were hit by a car while crouching on the floor.

    If you had more strength, you probably could have outrun it, or at least avoided it.

    Perhaps it was the wrong moment to stop taking drugs.
    """

    jump ending_generic


label doctor_ending_shot:

    $ doctor_details.endings.unlock('shot')
    $ doctor_details.add_ending_checkpoint(ending=doctor_details.endings.get_item('shot'))

    call death_screen_transition

    """
    You were shot in the face.

    It happened so quickly that you did not even see who pulled the trigger.

    There was no warning.

    No time to think.

    Only the sharp crack of a pistol, and a brief, dreadful heat.

    You were so close to getting out alive.

    What a pity.
    """

    jump ending_generic


label doctor_ending_burn:

    $ doctor_details.endings.unlock('burned')
    $ doctor_details.add_ending_checkpoint(ending=doctor_details.endings.get_item('burned'))
    
    call death_screen_transition

    """
    A dreadful fire burned the manor down.

    Trapped in your room, there was no possible way to escape.

    What a ghastly end.
    """

    jump ending_generic


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


label doctor_ending_shot_by_drunk:

    $ doctor_details.endings.unlock('shot_by_drunk')
    $ doctor_details.add_ending_checkpoint(ending=doctor_details.endings.get_item('shot_by_drunk'))
    
    call death_screen_transition

    """
    Despite knowing better, you still joined a hunt with a half-drunk man and a loaded gun.

    At least this dreadful end might teach you to make wiser choices next time.
    """

    jump ending_generic


label doctor_ending_throat_cut:

    $ doctor_details.endings.unlock('throat_cut')
    $ doctor_details.add_ending_checkpoint(ending=doctor_details.endings.get_item('throat_cut'))
    
    call death_screen_transition

    """
    You believed yourself safe.

    Yet there was something you failed to see.

    Alone in your room, you were an easy  target for whoever wished you harm.
    
    Sometimes the safest path lies in choosing whom to trust, rather than trusting no one at all.

    It's dangerous to go alone.
    """

    jump ending_generic
