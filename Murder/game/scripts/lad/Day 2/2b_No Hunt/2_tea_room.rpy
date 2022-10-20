label lad_day2_evening_tea_room:

    """
    The two ladies are sipping team and talking.

    I join them.
    """

    nurse """
    Oh Mister Harring, I am glad you are here.

    Misses Baxter was just talking about something fascinating.

    You should sit with us.
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
        Really ? How fascinating. 
        """

        psychic """
        yes, but to not bored miss Marsh, I won't go into details again.
        
        But if you'd like, we can talk about it at another time.
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

    It's not like it is a real emergency. They might not arrived until later this evening.
    """

    """
    It's creepy to think there is a dead guy upstairs, and that nobody is doing anything about it.

    He is there in his room, like nothing happened.

    Weird.

    While we are still talking the butler enters the room.
    """

    # TODO THey eat a  small lunch + time jump ?

    cook """
    I am glad you are all here.

    I just finished to cook a small luncheon.
    
    I can bring it to you if you want.
    """

    psychic """
    Thank you miss, that would be lovely.

    But I am terribly sorry, are you the cook ?

    I thought I saw you cleaning up my room this morning.
    """

    cook """
    Um, ... the true is I am the cook, but also a maid when needed.
    """

    psychic """
    A cook and a maid ? That's a lot of work you must have.
    """

    cook """
    Oh don't worry about me, I can handle it.

    I will fetch your food now.
    """
    
    psychic """
    Well, it's worse than I thought. A cook that doubles up as a maid.

    I've never seen something like this.
    """

    """
    Miss Marsh and I stay silent. 

    I guess she doesn't know more than I do about the running of a house.

    Or maybe she doesn't want to say bad things about our host.

    After a while the cook comes with our food and we enjoy it exchanging banalities.

    Then I decide I don't have much to say to them, so I leave.
    """

    # TODO OR I SHOOULD ADD GENERIC NURSE AND PSYCHIC ??? 


    return