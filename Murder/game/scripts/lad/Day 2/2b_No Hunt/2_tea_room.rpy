label lad_day2_hunt_tea_room:

    $ change_room('tea_room')

    """
    Amelia Baxter and Rosalind Marsh are in the room.
    
    They're drinking tea and talking calmly.

    I join them.
    """

    nurse """
    Oh Mr Harring, I'm glad you're here.

    Miss Baxter and I were just discussing something fascinating.

    You should join us.
    """

    lad """
    Of course, I'd be happy to chat with you for a bit. 
    
    What were you talking about?
    """

    nurse """
    Miss Baxter was talking about how she can communicate with the dead.
    """

    # TODO if the psychic knowledge is not known, summarize it here? or just display the text?
    if all_menus.get("psychic_generic_menu_lad") and all_menus["psychic_generic_menu_lad"].choices[3].hidden:

        lad """
        Ah, yes, we've discussed that before.
        """
    
    else:

        lad """
        Really? That's fascinating. 
        """

        psychic """
        Yes, but to not bore Miss Marsh, I won't go into the details again.
        
        But if you're interested, we can discuss it another time.
        """

    nurse """
    Anyway, you mentioned being concerned about the man who died last night.
    """

    psychic """
    That's correct. I have a feeling that something is off about his death.
    """

    nurse """
    What do you mean?
    """
    #TODO: WHY is she suspicious?
    psychic """
    I sense his spirit, and it's restless. It's a sign of an unnatural death.

    There's something amiss, I just can't figure what.

    But I don't mean to alarm you.

    It might be nothing.

    In any case, we'll know more once the police arrive.
    """

    lad """
    That's true. We're still waiting for them, right?

    But Lady Claythorn left and didn't assign anyone to handle this matter?
    """

    psychic """
    Well, she has staff to manage such situations.
    """

    if lad_details.saved_variables["has_met_maid"]:

        lad """
        Ah, like the girl I encountered when I tried to go downstairs.
        """

        psychic """
        What were you attempting to do downstairs?

        That area isn't somewhere we should wander into, Mr Harring.

        Regardless, there are probably many staff members you haven't met yet.

        Such a large house requires a sizable team.
        """

    else:
        lad """
        Aren't they all out on the hunt?
        """

        psychic """
        No, dear. The kitchen staff and some maids remain in the mansion.

        Everything in such a home is well-organized.
        """

    psychic """
    So, don't worry. There will definitely be someone available to talk with the police.
    """

    nurse """
    Indeed, and it might take a while for the police to get here.

    It's not a pressing emergency. They might not arrive until later this evening.
    """

    """
    It's creepy to realize there's a dead man upstairs.

    He's there in his bed, as if nothing happened.

    Strange.

    While we talk, someone enters the room.
    """

    maid """
    I'm glad to find you all here.

    I've prepared a light luncheon.
    
    Would you like me to bring it over?
    """

    psychic """
    Thank you, Miss. That sounds wonderful.

    But I must ask, did you cook it?
    
    Aren't you the maid? I thought I saw you tidying my room earlier.
    """

    maid """
    Well, ... the truth is, I am the cook. But I occasionally assist as a maid when needed.
    """

    psychic """
    A cook and a maid? That's quite the workload.
    """

    maid """
    Don't be concerned for me. I can manage.

    I'll fetch your meal now.
    """

    """
    She exits the room.
    """
    
    psychic """
    It seems worse than I initially thought. A cook who also acts as a maid.

    That's rather unusual.
    """

    """
    Miss Marsh and I stay silent. 

    Perhaps she's as clueless as I am about the workings of this household.

    Or she might be refraining from criticising our host.

    After a moment, the cook returns with our food, and we enjoy a light chat while dining.

    Once we're done, Rosalind Marsh stands up.
    """

    nurse """
    That was delightful. 

    If you'll excuse me, I need to rest in my room for a bit.

    The storm kept me awake most of the night.
    """

    psychic """
    Certainly, we understand.

    See you later.
    """

    """
    Rosalind Marsh leaves the tea room.

    I'm left with Amelia Baxter.
    """

    psychic """
    It seems it's just you and me, Mr Harring.
    """

    $ lad_details.saved_variables["day2_nohunt_has_visited_tea_room"] = True

    call psychic_generic

    return

label lad_day2_hunt_tea_room_return:

    $ change_room('tea_room')    

    """
    I re-enter the tea room.

    Amelia Baxter is still present, engrossed in a book.

    I approach her.
    """

    psychic """
    Mr Harring? 

    How may I assist you?
    """

    call psychic_generic

    return