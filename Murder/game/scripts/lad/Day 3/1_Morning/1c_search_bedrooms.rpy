label lad_day3_morning_lad_room:

    """
    No need to double check my room.

    I know what's there.
    """

    return

label lad_day3_morning_nurse_room:

    scene hallway
    
    """ 
    I knock on the door.

    Nobody answers.
    """

    psychic """
    No need for formalities.

    We better just try to enter.
    """

    """
    And before I could say anything, she opens the door.
    """

    $ change_room("nurse_room")

    psychic """
    I believe it's Miss Marsh's Room.
    """

    $ unlock_map("nurse_room")

    psychic """
    She is not here.

    And the room is neatly ordered.

    No sign of struggle or hurry here.
    """

    lad """
    Where could she be?
    """

    psychic """
    I don't know.

    This place is not that big.

    We should have run into her.
    
    In any case, let's look around.

    There might some clue on where she could be.
    """

    pause 1.0
    
    """
    We looked for a while but found nothing of interest.
    """

    return


label lad_day3_morning_captain_room:

    scene hallway

    play sound door_knock

    lad """
    Is there someone in there?
    """

    captain """
    Yes, what is it?
    """

    $ unlock_map('captain_room')

    lad """
    It's Ted Harring. I am here with Amelia Baxter.

    We would like to talk to you.
    """

    captain """
    Alright come on in.
    """

    $ change_room('captain_room')

    """
    We enter the bedroom.

    It is very tidy.

    The captain is already dressed.

    He was reading a book sitting on a chair.

    As we enter, he stands up, looking surprised.
    """

    captain """
    Well, I was not expecting visitors this early.
    
    What can I do for you?
    """

    # TODO add if depending on the number of rooms already visited, specially the host room
    psychic """
    We believe something strange is going on.

    You and mister Harring are the only persons I encountered this morning,.

    We don't seem to find any of the servants, nor any other guests so far.
    """

    captain """
    Now that you mention it, nobody came to tend the fire this morning.

    It's rather unusual.

    But I don't think it is that concerning. There probably is very going explanation.
    """

    lad """
    We hope so too. 

    But just in case, we where looking inside the manor for someone to explain us what's happening.
    """

    captain """
    I understand. I can come with you if you want.
    """

    psychic """
    Thank you but,... maybe,... maybe it's best if we split up.

    We could cover more ground this way.
    """

    """
    Amelia seemed nervous when she answered.
    """

    captain """
    Good thinking. I'll look on my own, and we can meet later.

    Maybe in the tea room?
    """

    psychic """
    That sounds perfect.

    See you then.
    """

    $ lad_details.saved_variables["day3_morning_captain_found"] = True

    return 

label lad_day3_morning_host_room:

    scene hallway

    play sound door_knock

    psychic """
    This is Lady Claythorn Room.
    """

    $ unlock_map('host_room')

    lad """
    Miss Claythorn?

    Are you there?
    """

    """
    There is no response.
    """

    # psychic """
    # I told you she was not there.
    # """

    """
    Then, she put her on hand on the clutch.

    The door opens.
    """

    lad surprised """
    What are you doing? 

    We can't enter like that !
    """

    """
    But it's too late. She's already rushed inside.

    I have no choice but to follow her.
    """

    $ change_room('host_room')

    """
    It's empty.

    The wardrobe is wide open. There are some clothes on the floor.
    """

    psychic """
    It looks like she left in a hurry.
    """

    """
    We looked for a clue of what happened but found nothing.
    """

    psychic """
    Well, she either have left, or she is still hiding somewhere in the manor.

    There is no need to dwell here any longer.
    """
    
    return 

label lad_day3_morning_drunk_room:

    scene hallway

    # # TODO without captain, not possible,
    # if not lad_details.saved_variables["day3_morning_captain_found"]:

    psychic """
    It's Samuel Manning room.
    """

    $ unlock_map('drunk_room')

    lad """
    Mister Manning?

    Are you alright?
    """

    """
    No answer.
    """

    lad """
    Well the door is closed anyway.

    Mister Sinha has the key.
    """

    # else:
    #     captain """
    #     Move aside, I am gonna open it.
    #     """

    #     $ change_room('drunk_room')

    return

label lad_day3_morning_psychic_room:

    $ change_room('psychic_room')

    psychic """
    What are you doing in my room?

    You don't think someone is hiding here?
    """

    lad """
    Probably not, but it's better to be thorough.
    """

    """
    But she is right.

    There is nothing or nobody here.
    """

    return

label lad_day3_morning_doctor_room:

    $ change_room('doctor_room')

    """
    I am back in Daniel Baldwin room.

    His body is still on the bed.

    Besides there is nothing else out of the ordinary.

    I don't want to dwell here more then I have to.
    """

    return

label lad_day3_morning_broken_room:

    $ change_room('broken_room')

    $ unlock_map('broken_room')

    """
    Thomas Moody's room.

    He is still lying on the bed.

    But I don't see anyone else here.

    No need to stay longer.
    """

    return