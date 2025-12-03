label doctor_day2_evening_exploration:
    
    call change_time(21, 00)

    $ change_room("bedroom_doctor")

    $ play_music('mysterious', 2)

    """
    I now find myself faced with several courses of action.

    The most obvious would be to remain here in my room and wait for the morning.

    I could even move some furniture against the door to make certain no one can enter.

    Yet that, too, feels dangerous. There are other ways for someone to reach me.

    The alternative is to attempt to discover who wrote that note to Samuel Manning.

    That is the person I ought to fear.

    Everything points towards Lady Claythorn, yet I cannot be sure.

    If only I could trust at least one other person, I might ask for their assistance.

    It would be safer to investigate in company, but in whom ought I place my trust?

    It would be ideal to have someone implicitly trustworthy, like a judge.

    But everyone here appears suspicious to me.
    """

    if doctor_details.threads.is_unlocked('flirt'):

        """
        I might turn to Andrew. After the time we have spent together, I find it hard to picture him as a likely culprit.

        He is probably downstairs with the staff at present, unless he has already retired for the night.
        """

    if doctor_details.threads.is_unlocked('remember_nurse'):

        """
        By good fortune, I already know Nurse Rosalind Marsh. That acquaintance makes me more comfortable about approaching her.
        """

    if doctor_details.threads.is_unlocked('book_opium'):
        
        """
        I also have to manage symptoms of withdrawal.

        My hands tremble, and I am sweating more than is reasonable.

        They will only grow worse as the night wears on, which will not be in my favour.
        """

    """
    I feel very much at a crossroads.

    What I decide to do now may mean the difference between life and death.

    So what shall it be?
    """

    $ time_left = 90
    call run_menu(doctor_details.saved_variables["day2_evening_map_menu"])

    if doctor_details.threads.is_unlocked('trust_captain'):

        jump doctor_day3_morning_captain

    else:

        jump doctor_day3_morning_nurse

# Notable explorations
label doctor_day2_evening_bedroom_lad:

    $ change_room('bedroom_lad')

    play sound door_knock

    doctor """
    Mr Harring, are you there?
    """

    """
    For a moment there is no answer.

    Then I hear a faint voice from behind the door.
    """

    lad """
    Doctor Baldwin, is that you?
    """

    doctor """
    Yes.

    I should like a word with you, it is rather important.

    May I come in?
    """

    lad """
    Well, I don't know, doctor.

    I've already dragged a desk in front of the door.

    Might be better if we did the talking through it.
    """

    doctor """
    I am afraid it is a very sensitive matter.

    I would not care for anyone overhearing us.
    """

    lad """
    Oh.

    In that case, it is probably best if we wait until the morning.

    It will be easier to talk then.

    Good night, doctor.
    """

    doctor """
    No, it might be too late by then, I need to...
    """

    """
    I hear his footsteps recede and the faint creak of floorboards further inside the room.

    It seems Mr Harring has no intention of opening his door tonight.

    I had better try somewhere else.
    """
    
    return


label doctor_day2_evening_bedroom_broken:

    $ change_room('bedroom_broken')

    """
    Thomas Moody's room looks exactly as it did this morning.
    """

    if doctor_details.threads.is_unlocked('broken_unmasked'):

        """
        With all that has transpired since, I have scarcely given a thought to the mystery of Thomas Moody's mask.

        It is one more reason to question everything that is happening in this house.

        But there is nothing I can do about it from here.

        I should leave.
        """

    else:

        """
        The poor man's body lies just as before upon the bed.

        This morning I chose not to look beneath his mask, out of respect.

        After all that has occurred since, that restraint feels misplaced.

        I am compelled to examine him more closely.

        I step nearer to the bed and lean over him.

        At once I notice small details, such as the way the face beneath the mask does not seem as peaceful as it ought.

        Almost before I realise what I am doing, my hand reaches for the mask and I lift it away.
        """

        call doctor_day2_behind_the_mask
        

    return
