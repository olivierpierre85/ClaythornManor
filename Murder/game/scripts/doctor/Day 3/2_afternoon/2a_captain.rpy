label doctor_day3_afternoon_captain:

    # TODO say that the only place not visited is Miss Marsh room.
    # GO there break in, notice there is no one.
    # So settle to the tea room to discuss the next step.


    # In the discussion, if uunlocked:
    # TODO  include => Footman is an actor
    # TODO include => nurse is not unknown, => THen captain not either.

    # At the end, conclusion that the lad will stay with psychic, and doctor and captain will leave.
    # Obstruction from the psychic that want the doctor to stay with her?
    
    $ change_room("tea_room", irisout)

    """
    We all seat, each of us deep in thought.

    The manor feels hollow now, stripped of its usual life.
    """

    captain """
    Whatever happened here was coordinated.

    Staff and guests alike did not simply wander off.
    """

    lad """
    But why? 
    """

    captain """
    Well, we don't have a full explanation, but Doctor Baldwin discovered something two days ago that could help understand.

    Doctor, I believe it's time we share our knowledge. 

    I don't know that we can trust them, but since we the four of us in it together, maybe we should try.

    What do you think?
    """

    # TODO Maybe possibility to refuse, because too dangerous. Then what happens?


    doctor """
    I believe you are right captain.

    We might as well tell you everything we know.
    """

    """
    So I tell them about the letter found in Samuel Manning's room.
    """


    # TODO put this is in a menu,
    # If you have said all options: Psychic don't let you leave?
    if doctor_details.threads.is_unlocked('footman_actor'):

        doctor """
        There is something else you should know.

        The footman was not who he claimed to be.

        He was an actor.
        """

        lad """
        You're joking.

        That bloke could barely pour tea.
        """

        captain """
        An actor?

        That would explain a great deal.
        """

    if doctor_details.threads.is_unlocked('broken_unmasked'):

        """
        Tell them about BROKEN NOT FACE
        """

    if doctor_details.threads.is_unlocked('remember_nurse'):

        doctor """
        And Miss Marsh was not unknown to me.

        Nor, I suspect, to you either, Captain.
        """

        captain """
        No.

        She and I have crossed paths before.

        Under very different circumstances.
        """

        psychic """
        Then this was never random.
        """


    lad """
    So what now?

    We can't just sit around waiting for answers.
    """

    captain """
    No.

    We must act sensibly.
    """

    # ESCAPE? Discuss who will leave?
    # What about the car? No gas, so no good. Also no keys?


    jump work_in_progress