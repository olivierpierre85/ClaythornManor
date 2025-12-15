label doctor_day2_evening_males_room_default:

    call doctor_attic_default
    
    play sound door_knock

    """
    I could just barge in, but I prefer to knock just in case.
    """

    footman """
    Who is it?
    """

    return


label doctor_day2_evening_males_room_do_no_enter:

    call doctor_day2_evening_males_room_default

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


label doctor_day2_evening_males_room_enter:

    call doctor_day2_evening_males_room_default
        
    """
    I answer in a whisper.
    """

    doctor """
    Andrew, it's me, Daniel.
    """

    # Write an implied sexual encounter.

    # at the end the footman ask the doctor to leave

    # the doctor tries to insist, but the footman says he as a lot of things to do
    # while explaining, the doctor notice the weather it might rain again, 
    # the footman says "I am not made out of sugar" which makes the doctor ask him where he got this weird expression
    # that leads to the confession of andrew being a birtley belgian
    # The doctor also learn something that will unlock something the next day (Everybody is gone, someone told meme..)

    return