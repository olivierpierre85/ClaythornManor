label doctor_day1_laudanum_1:

    """
    For some reason, I feel more nervous than usual.

    But I suppose there's no harm in spending a little more time alone.
    """

    call wait_screen_transition()

    call change_time(22, 00)

    """
    That's better.

    I'd best go and join the others now, otherwise it'll look suspicious.
    """

    # unlock extra dose of laudanum
    $ doctor_details.important_choices.unlock('laudanum_extra_1')

    call run_menu(TimedMenu("doctor_day1_evening_2", [
        TimedMenuChoice("Let's go down to meet the others", 'generic_cancel', early_exit=True),
        TimedMenuChoice("Maybe one last time", 'doctor_laudanum_death', 60, early_exit=True),
    ]))

    return


label doctor_laudanum_death:

    $ play_music('sad', 2)

    """
    Just one more can't hurt. 
    
    Though a flicker of doubt appears at the edge of my mind, I quickly dismiss it.

    My hand trembles as I lift the spoon to my lips. 
    
    The bitter draught slides down my throat, and I wait for it's sweet relaxing effect.
    
    My pulse slows. The room tilts. 
    
    My eyelids grow heavy. 

    The voices, the ones that have haunted me for as long, are finally quiet.

    All is silent now.
    """

    jump doctor_ending_overdose