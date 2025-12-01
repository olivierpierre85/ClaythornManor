label doctor_day2_evening_exploration:
    
    call change_time(21, 00)

    $ change_room("bedroom_doctor")

    """
    I now face several options.

    The obvious choice would be to stay in my room and wait for the morning.

    I could even move some furniture to prevent anyone from entering.

    But that feels dangerous, there are other ways someone could get at me.

    The other option is to try to uncover who wrote the note to Samuel Manning.

    That's the person I should be worried about.

    Everything points to Lady Claythorn, but I can't be sure.

    If I could trust at least one person, I could approach them to ask for their help.

    It would be safer to investigate in pair, but whom should I put my trust in?
    
    It would ideal to have someone implicitly trustworthy, like a judge.

    But everyone here is suspicious too me.
    """

    if doctor_details.important_choices.is_unlocked('flirt'):

        """
        I could ask Andrew, the time we spent together makes him less likely to be a suspect.

        He is probably downstairs with the staff now. Or maybe he already went to bed.
        """

    if doctor_details.observations.is_unlocked('remember_nurse'):

        """
        By chance, it happens that I already knows Rosalind Marsh, that makes me more comfortable to approach her.
        """

    
    if doctor_details.objects.is_unlocked('book_opium'):
        
        """
        To make things worst, I am going through growing symptoms of withdrawals.

        I am slightly shaking and sweating profusely.

        And it will only increase throughout the night, which won't help.
        """

    """
    I have the feeling to be at a crossroads.
    
    What I do now could be the difference between life and death.

    So what will it be?
    """

    $ time_left = 90
    call run_menu(doctor_details.saved_variables["day2_evening_map_menu"])

    return