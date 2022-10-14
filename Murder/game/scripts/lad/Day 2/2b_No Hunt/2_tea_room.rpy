label lad_day2_evening_tea_room:

    """
    The two ladies are sipping team and talking.

    I join them.
    """

    nurse """
    Oh Mister Harring, I am glad you are here.

    Misses Baxter was just talking about something fascinating.

    You should join us.
    """

    # Needed ?
    """
    There is something about the way she said that that makes me uneasy.
    """

    lad """
    Of course, I'll be glad to discuss with for a bit. What were you talking about ?
    """

    nurse """
    Miss Baxter was actually talking about ghosts and how she can talk to dead people.
    """
    # TODO if the psychic knowledge not known, make resume it here ? or just call the text?
    if psychic_details.check_knowledge_unlocked('heroic act'):
        lad """
        Oh yes, we talked about it already.
        """

    else:
        lad """
        Really how fascinating. 
        """

        psychic """
        It really is. But not to bored miss TODO, I won't enter into the details. we can talk about it at another time.
        """

    nurse """
    Anyway, you were saying that you feeling the poor guy who died last night.
    """

    psychic """
    Right, I have the feeling, something is not right about his death.
    """

    nurse """
    What do you mean ?
    """

    psychic """
    I have this recurrent feeling of him, ...
    """









    return