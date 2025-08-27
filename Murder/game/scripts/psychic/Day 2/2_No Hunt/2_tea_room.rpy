label psychic_day2_hunt_tea_room:

    $ change_room("tea_room")

    """
    I am the first to arrive, so I pick a table and wait for Rosalind Marsh.

    I am seated comfortably, lost in my thoughts when she enters the room.
    """

    call change_time(12, 0)

    psychic """
    Miss Marsh, would you like to join me?
    """

    nurse """
    Yes, thank you.
    """

    psychic """
    It seems we haven't really had a chance to talk yet, right?
    """

    call nurse_generic

    """
    Suddenly, a staff member walks in.
    """

    maid """
    Excuse me for interrupting, but do you ladies need some lunch?
    """

    nurse """
    That would be lovely, thank you.
    """

    pause 1.0

    """
    After a few minutes, she returns with some plates.

    As we eat, we chat about trivial matters.
    """

    pause 1.0

    """
    When our lunch is over, Rosalind rises from her seat.
    """

    play sound woman_cough

    """
    She lets out a painful cough.
    """

    nurse """
    I'm feeling rather poorly.  

    I think I will retire to my room.  

    Would you mind being left on your own?
    """

    psychic """
    Not at all, please don't concern yourself.  

    There is more than enough here to occupy me.
    """

    """
    With the manor so quiet, I might seize the chance to explore unnoticed.  

    And perhaps I should call upon Rosalind Marsh later, to see how she is doing.
    """

    return

