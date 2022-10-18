label lad_day2_afternoon:
    call black_screen_transition("Day 2 - afternoon") # Good ?
    scene great_hall with irisout

    call change_time(15,00)
    
    if lad_day2_hunt:
        """
        The rest happened feels like a blur for me.

        After the screaming and crying in the woods, Captain Sinha took charge.

        He made us transported the Doctor on a makeshift stretcher.
 
        It took a while but we finally reached the mansion.
        """
    else:
        """
        I can see the hunting partying entering the house.

        Amalia and Rosalind were already there, near the entrance.

        Lady Claythorn enters first, visibly shocked.

        Then the butler and footman followed suit.

        They are dragging someone on a makeshift stretcher.
        """

    # TODO play dramatic music
    psychic surprised """
    Oh my God ! What Happened !?

    Is that Doctor Baldwin. Is he injured ?

    Oh no ? Is he dead ?
    """

    captain """
    I am sorry dear, I am afraid that he is.
    """

    psychic """
    But but, what happened ?
    """

    captain """
    An accident. 
    """

    drunk sad """
    It was I swear. I have no idea why I hit him.
    I was aiming at a rabbit. I didn't even notice him.
    """

    """
    Everybody turns at him.
    """
        
    psychic angry """
    Fool ! I bet you were too drunk, that's why you hit him.

    You could barely walk this morning. How come they gave you a gun ?
    """

    captain """
    Please, there is no need to blame anyone now. It's too late.

    We'll let the police deal with him.

    By the way, has anyone from the city arrived here yet ?
    """

    nurse """
    I am afraid not.

    We are still waiting for them.
    """

    captain """
    We better tell them to hurry up then.

    Lady Claythorn where is the phone ?
    """

    host """
    Don't worry, I'll take care of it myself.
    """

    """
    She leaves the group with the butler on her trail.

    Now everyone is silent.

    And most of them stare at Sam Manning with hate.

    Then the host comes back.
    """

    host """
    I just spoke with the police. They are not coming today.
    """

    captain """
    What !? Why ?
    """

    host """
    They were halfway there. But they ran into a huge tree blocking the road. 
    
    There was no way to move it.
    
    They say they will be back tomorrow with some help.
    """

    psychic """
    But,... what are we gonna do with him ?
    """

    captain """
    I'll carry him to his bed. 
    
    That's probably the best for the moment.

    Can someone help me carry him.
    """

    lad """
    I'll come with you.
    """
    
    # ?????
    scene bedroom_doctor

    return

