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

    $ change_room("bedrooms_hallway")

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



label doctor_day2_evening_sleep_alone:    

    $ change_room("bedroom_doctor", dissolve)

    """
    I reach my room alone.

    I lock my door and do what I can to secure it.
    """

    play sound door_locked

    """
    Then I drag a chair and the small chest of drawers against the door, in case Lady Claythorn or one of her accomplices decides to pay me a visit.
    """

    play sound moving_furniture

    """
    Now that everything is in place, I lie down upon the bed, fully dressed in case I need to move quickly.
    """

    call doctor_day2_evening_captain_sleep_options

    $ stop_music()

    $ change_room("black_background", dissolve)

    $ play_music('danger', 2)

    """
    I do not know how long I have slept when a faint sound rouses me.

    It is a soft scrape, close by my ear, out of place in the stillness of the room.
    """

    """
    Before I can stir, a hand clamps hard across my mouth, stifling any cry.

    The weight of a body leans over me, pinning me to the mattress.
    """

    """
    I clutch at the arm that holds me, but my limbs feel heavy and slow, still dulled by sleep.

    My heart hammers so loudly that I can scarcely hear my own thoughts.
    """

    """
    Something cold touches the bare skin of my throat.

    For one dreadful instant I understand exactly what is about to happen.
    """

    """
    Pain sears across my neck in a sudden, burning line.

    Hot wetness spills down my collar, soaking the front of my shirt.
    """

    """
    I struggle blindly, fingers clawing at the air and at the implacable hand that silences me.

    My strength ebbs almost at once, as if it were pouring away with my blood.
    """

    jump doctor_ending_throat_cut


label doctor_day2_evening_bedroom_drunk:
    
    $ change_room("bedroom_drunk")

    """
    I am back in Samuel Manning's room.

    It is still a mess.

    But now Samuel Manning is lying on his bed, seemingly at peace.

    I remember that Captain Sinha and Ted Harring carried him here.

    I do not know why I have come back.

    Perhaps I wished to look one last time upon the man I killed.

    I approach the bed.

    He looks peaceful.

    I try to convince myself that I had no choice, that it was either him or me.

    But that does not make the guilt go away.

    My thoughts return to the simple letter that set all of this in motion.

    I wonder if it is still here.

    I look around and do not find it on the desk.

    Then I spot something in the fire. 
    
    The letter is there, burned so badly I cannot make out what was written.

    If I had hoped to use it as proof of my innocence, I am too late.

    Samuel Manning has taken care to erase all trace of his plans.

    There is no point in lingering here any longer.
    """

    $ doctor_details.threads.unlock('burned_letter')

    return


label doctor_day2_evening_males_room:

    call doctor_attic_default

    play sound door_knock

    footman """
    Who is it?
    """

    if doctor_details.threads.is_unlocked('flirt'):
        
        """
        I answer in a whisper.
        """

        doctor """
        Andrew, it's me, Daniel.
        """

        # TODO Andrew opens, they talk, Doctor hears another odd expression and confronts him.
        # He learns something, but Andrew insists he should return to his own room to sleep.

    else:

        doctor """
        It is Doctor Baldwin.
        """

        footman """
        Oh.

        What can I do for you, doctor?
        """

        doctor """
        Well... I am not entirely sure.

        I was merely exploring, and wondered what was in the attic.
        """

        footman """
        I do not think you are supposed to be here, doctor.

        This is the servants quarters.

        I was about to go to bed myself, as I have to be up early tomorrow.
        """

        doctor """
        Of course, my apologies for disturbing you.

        Good night.
        """

        footman """
        Goodnight, sir.
        """

        """
        Well, that was rather embarrassing.

        That is what happens when one wanders about a house without a clear purpose, I suppose.
        """

    return
