label psychic_day2_hunt_tea_room:

    $ change_room("tea_room")

    """
    When I walk into the tea room, Rosalind Marsh is already there, sitting at a table.
    
    I head over to her.
    """

    nurse """
    Miss Baxter, would you like to join me?
    """

    psychic """
    Yes, thank you.
    """

    nurse """
    It seems we haven't really had a chance to talk yet, right?
    """

    # We have 45 minutes until we're interrupted NOT NEEDED NOW but could be working
    # $ remaining_time = time_left - 45
    # $ time_left = 45

    call nurse_generic

    # $ time_left += remaining_time

    """
    While we're talking, a staff member walks in.
    """

    maid """
    Excuse me for interrupting, but do you ladies need some lunch?
    """

    nurse """
    That would be lovely, thank you
    """

    pause 1.0

    """
    After a few minutes, she returns with some plates.

    As we eat, we chat about trivial matters related to the host.
    """

    pause 1.0

    """
    When our lunch is over, Rosalind rises from her seat.
    """

    nurse """
    I'm quite exhausted with all that has happened.

    I think I'll retire to my room. Would you mind being alone?
    """

    psychic """
    Oh no, don't worry.

    There's plenty for me to do.
    """


$ psychic_details.saved_variables["day2_nohunt_has_visited_tea_room"] = True

return


    $ psychic_details.saved_variables["day2_nohunt_has_visited_tea_room"] = True

    return

