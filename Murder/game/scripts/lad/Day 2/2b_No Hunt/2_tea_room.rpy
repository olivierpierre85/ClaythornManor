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
        It really is. But not to bored miss Marshman, I won't go into details, we can talk about it at another time.
        """

    nurse """
    Anyway, you were saying that you hearing the poor guy who died last night.
    """

    psychic """
    That's right. And I have the feeling that something is not right about his death.
    """

    nurse """
    What do you mean ?
    """

    psychic """
    I am hearing him, and he is disturbed. The sign of an unnatural death.

    There is something wrong here but I can't figure out what.

    But sorry dear, I am not trying to scare you.

    It might be nothing.

    In any case, we'll know more about it when the police will arrive.
    """

    lad """
    That's true, we are still waiting for them right.

    How could Lady Claythorn left and don't let anyone taking care of this ?
    """

    psychic """
    Well, she have staff to deal with that sort of things.
    """

    lad """
    Aren't they all out on the hunt ?
    """

    psychic """
    Oh no dear, there are still are all the kitchen staff, and the maids who remains in the mansion.

    All of this is very well organized in such a house.
    """

    nurse """
    Yes, and let's not forget that it may take a while for the police to reach us anyway.

    It's not like it is a real emergency. THey might not arrived until later this evening.
    """
    
    """
    Okay then. It's a bit weird to think there is a dead guy upstairs, and that nobody is doing anything about it.
    
    In any case, they both went back to their earlier conversation.

    I don't think I should stay here.
    """

    return