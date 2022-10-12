label lad_day2_breakfast_follow:

    $ lad_day2_breakfast_follow  = True

    scene hallway

    """
    I jump from my seat and walks behind the doctor.

    Soon, we stop in front the Richard III Bedroom.

    They are so concerned that they don't say anything about my presence.
    """

    butler "There we are. Thomas Moody's room."

    doctor "Is he the chap with the mask ?"

    butler "Correct Sir."

    call unlock_map('broken_room')
    $ broken_details.introduce() 

    "We all enter the room."

    scene bedroom_broken

    butler "He is here in his bed. He was not responding at all when I tried to wake him up."

    """
    The doctor approaches the bed. He takes the wrist of the man.
    """

    doctor """
    No pulse.

    He is dead.
    """

    play music scary_01

    host surprised """

    Dead ?!!!

    How could that be ?

    """

    doctor """
    I don't know. I will have to examine him further.

    You don't need to stay for that part.

    I'll come back downstairs when I know more.
    """

    butler "Come with me My Lady."
    
    host """
    Oh... Of course...
    """

    "The butler escorts the Lady out of the room."

    "The doctor turns himself towards me."

    doctor "And why are you here again ?"

    lad "Well, I was... I wanted to .."

    doctor """
    Never mind. Since you are here make yourself useful.

    Help me turning him over to check for injury.
    """

    """
    He then thoroughly examined the body for a while.
    """

    lad """
    So, what could have caused this doctor ?
    """

    doctor """
    I am not sure. 

    This guy seemed in good health.

    But with injuries like the ones he suffered during the war, you can never be sure.  

    A patient can be fine for years, then suddenly his body can give up.  
    """

    lad """
    So it's a natural death ?
    """

    doctor """
    I am not saying that either.
    
    I can't really rule out anything at this point.

    We would need a autopsy to be certain.

    So the next thing to do now is to notify the authorities.

    I need a phone.
    """

    """
    He then leaves the room.

    I followed him back to the dining hall.
    
    """

    scene dining_hall

    return