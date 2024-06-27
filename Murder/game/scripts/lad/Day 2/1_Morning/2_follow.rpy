label lad_day2_breakfast_follow:

    $ lad_details.saved_variables["day2_breakfast_follow"]  = True

    $ change_room("bedrooms_hallway")

    """
    I jump from my seat and walk behind the doctor.

    Soon, we stop in front of the Richard III Bedroom.

    They're so concerned that they don't say anything about my presence.
    """

    butler """
    Here we are. Thomas Moody's room.
    """

    doctor """
    Is he the one with the mask?
    """

    butler """
    Correct, Sir.
    """

    $ unlock_map('bedroom_broken')

    "We all enter the room."

    $ change_room('bedroom_broken')

    butler """
    He's here in his bed. He didn't respond when I tried to wake him up.
    """

    """
    The doctor approaches the bed and takes the man's wrist.
    """

    $ stop_music(fadeout_length=1)

    doctor """
    No pulse.

    He's dead.
    """

    $ play_music('scary')

    host surprised """
    Dead?!!!

    How is that possible?
    """

    doctor """
    I'm not sure yet. I'll need to examine him further.

    You may want to leave for this part.

    I'll come back downstairs when I have more information.
    """

    butler """
    Please come with me, My Lady.
    """

    host """
    Oh... Yes, of course...
    """

    """
    The butler escorts the Lady out of the room.

    The doctor turns to face me.
    """

    doctor """
    Why are you here?
    """

    lad """
    I was just... I thought I could...
    """

    doctor """
    Never mind. Since you're here, make yourself useful.

    Help me turn him over to check for injuries.
    """

    """
    He then examines the body thoroughly for a while.
    """

    lad """
    What could have caused this, Doctor?
    """

    doctor """
    I'm not sure. 

    He seemed in good health.

    But with injuries like the ones he sustained during the war, one can never be too sure.  

    A patient can be stable for years, and then suddenly, his body can fail him.  
    """

    lad """
    So it's a natural death?
    """

    doctor """
    It's possible, but I can't confirm.

    I can't rule out anything right now.

    We'd need an autopsy for a definitive answer.

    The next step is to notify the authorities.

    I need a phone.
    """

    """
    He then exits the room.

    I follow him back to the dining room.
    """

    $ change_room('dining_room')

    return