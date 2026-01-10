label doctor_day3_afternoon_captain:

    # In the discussion, if uunlocked:
    # TODO  include => Footman is an actor
    # TODO include => nurse is not unknown, => THen captain not either.

    # At the end, conclusion that the lad will stay with psychic, and doctor and captain will leave.
    # Obstruction from the psychic that want the doctor to stay with her?
    
    $ change_room("tea_room", irisout)

    """
    We all seat, each of us deep in thought.

    The manor feels hollow now, stripped of its usual life.

    Captain Sinha breaks the silence.
    """

    captain """
    Whatever happened here was coordinated.

    Staff and guests alike did not simply wander off.
    """

    lad """
    But why? 
    """

    """
    Captain Sinha leans over me and whisper in my ear
    """

    captain """
    Maybe it's better to tell them everything.

    We might need their help if we want to get out of here intact.

    What do you think doctor?
    """

    psychic """
    Excuse me, what are you two whispering about?
    """

    call run_menu( TimedMenu("doctor_day3_afternoon_captain_choice", [
        TimedMenuChoice("Share what you know with others", 'doctor_day3_afternoon_captain_share', 0, early_exit=True),
        TimedMenuChoice("No don't, trust them.", 'doctor_day3_afternoon_captain_do_not_share', 0, early_exit=True),
        ])
    )


    # call run_menu(TimedMenu("TOD", [
    #     TimedMenuChoice('Reveal Daniel Baldwin\'s opium addiction{{observation}}', 'lad_day2_evening_billiard_room_captain_hypothesis_doctor', 10, condition="lad_details.threads.is_unlocked('laudanum')"),
    #     TimedMenuChoice('Point out the strange liquid on Thomas Moody\'s room{{observation}}', 'lad_day2_evening_billiard_room_captain_hypothesis_broken', 10, condition="lad_details.threads.is_unlocked('green_liquid')"),
    #     TimedMenuChoice('Show the letter found in Samuel\'s Manning room{{object}}', 'lad_day2_evening_billiard_room_captain_hypothesis_drunk_letter', 10, condition="lad_details.threads.is_unlocked('burned_letter')"),
    #     TimedMenuChoice('Question Samuel Manning\'s state of inebriation at the time of the accident', 'lad_day2_evening_billiard_room_captain_hypothesis_drunk', 10),
    #     # TODO: If you have ALL the suspicions, you can convince the captain something strange is afoot. Need to decide next steps.
    #     TimedMenuChoice('Accept you don\'t have any real suspicions', 'lad_day2_evening_billiard_room_captain_hypothesis_cancel', keep_alive=True, early_exit=True),
    #     ])
    # )


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