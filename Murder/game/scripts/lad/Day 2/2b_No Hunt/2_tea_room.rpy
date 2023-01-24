label lad_day2_hunt_tea_room:

    $ change_room('tea_room')

    """
    Amelia Baxter and Rosalind Marsh are in the room.
    
    They are drinking tea and talking calmly.

    I join them.
    """

    nurse """
    Oh Mister Harring, I am glad you are here.

    Miss Baxter was just talking about something fascinating.

    You should sit with us.
    """

    lad """
    Of course, I'll be glad to discuss with for a bit. What were you talking about ?
    """

    nurse """
    Miss Baxter was actually talking about ghosts and how she can talk to dead people.
    """

    # TODO if the psychic knowledge not known, make resume it here ? or just call the text?
    if current_character.saved_variables['knows_psychic_background']:
        lad """
        Oh yes, we talked about it already.
        """
        
    else:
        lad """
        Really ? How fascinating. 
        """

        psychic """
        Yes, but to not bored miss Marsh, I won't go into details again.
        
        But if you'd like, we can talk about it at another time.
        """

    nurse """
    Anyway, you were saying that you we were worried about the poor guy who died last night.
    """

    psychic """
    That's right. And I have the feeling that something is not right about his death.
    """

    nurse """
    What do you mean ?
    """

    psychic """
    I am sensing him, and he is disturbed. The sign of an unnatural death.

    There is something wrong here but I can't figure out what.

    But sorry dear, I am not trying to scare you.

    It might be nothing.

    In any case, we'll know more about it when the police will arrive.
    """

    lad """
    That's true, we are still waiting for them right.

    But Lady Claythorn left and don't let anyone taking care of this ?
    """

    psychic """
    Well, she have staff to deal with that sort of things.
    """

    if lad_details.saved_variables["has_met_maid"]:

        lad """
        Oh right, like the girl I met trying to go downstairs.
        """

        psychic """
        What were you trying to do downstairs ?

        That's not a place where we should venture Mister Harring.

        But in any case, there is probably a lot more staff that you haven't met yet.

        They are needed to run such a big house.
        """

    else:
        lad """
        Aren't they all out on the hunt ?
        """

        psychic """
        Oh no dear, there are still are all the kitchen staff, and the maids who remains in the mansion.

        All of this is very well organized in such a house.
        """

    psychic """
    So don't worry, there will definitely be someone to deal with the police.
    """

    nurse """
    Yes, and it may take a while for the police to reach us anyway.

    It's not like it is a real emergency. They might not arrived until later this evening.
    """

    """
    It's creepy to think there is a dead guy upstairs, and that nobody is doing anything about it.

    He is there in his room, like nothing happened.

    Weird.

    While we are talking, someone enters the room.
    """


    maid """
    I am glad to find you all here.

    I just finished to cook a small luncheon.
    
    I can bring it to you if you want.
    """

    psychic """
    Thank you miss, that would be lovely.

    But I am terribly sorry, did you say you cooked it ?
    
    Are you the cook ? I thought I saw you cleaning up my room this morning.
    """

    maid """
    Um, ... the true is I am the cook. But I sometimes help out as a maid when needed.
    """

    psychic """
    A cook and a maid ? That's a lot of work you must have.
    """

    maid """
    Oh don't worry about me. I can handle it.

    I will fetch your food now.
    """
    
    psychic """
    Well, it's worse than I thought. A cook that doubles up as a maid.

    I've never seen something like this.
    """

    """
    Miss Marsh and I remain silent. 

    I guess she doesn't know more than I do about the running of a house.

    Or maybe she doesn't want to say bad things about our host.

    After a while the cook comes with our food and we enjoy it exchanging banalities.

    When we are all finished Rosalind Marsh stands up.
    """

    nurse """
    That was great. 

    No if you'll excuse me, I think I will retreat to my room to rest a little.

    I afraid that I haven't slept very well tonight.

    This storm got me up all night.
    """

    psychic """
    Of course, we understand.

    We'll see you later.
    """

    """
    Rosalind Marsh then exists the tea room.

    I am left alone with Amalia Baxter.
    """

    psychic """
    It looks it's just you and me Mister Harring.
    """

    $ lad_details.saved_variables["day2_nohunt_has_visited_tea_room"] = True

    call psychic_generic

    return

label lad_day2_hunt_tea_room_return:

    $ change_room('tea_room')    

    """
    I return to the tea room.

    Amalia Baxter is still there, reading a book.

    I approach her.
    """

    psychic """
    Yes Mister Harring. 

    What can I do for you ?
    """

    call psychic_generic

    return