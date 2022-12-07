label lad_day2_evening_psychic_room:
    
    scene hallway
    
    lad """
    Miss Baxter ?

    Are you here ? It's Ted Harring
    """

    """
    She slightly opens the door and look in the hallway.

    She looks worried.
    """

    psychic """
    Mister Harring, are you alone ?
    """

    lad """
    I am.
    """

    psychic """
    Come on in then.
    """

    $ change_room('psychic_room')

    psychic """
    So have you given any thought about what I told you ?

    You agree that something not right is happening ?
    """

    call run_menu(TimedMenu([
        TimedMenuChoice('I think you might be right', 'lad_day2_believe_psychic', 10, early_exit = True ),
        TimedMenuChoice('No, you are clearly hallucinating things', 'lad_day2_believe_dont_believe_psychic', early_exit = True)
    ]))

    return

label lad_day2_believe_psychic:

    lad """
    I am not sure yet. But what happened is strange enough so we can take some precautions.
    """

    psychic """
    I am glad you agree.

    Here what I think we should do :

    Go back to your room and close the door shut.

    Tomorrow morning, the first one to get up of the two of us will wake the other up.

    Then we stick together the whole day until we are free to leave.

    What do you think of that ?
    """

    lad """
    It sounds like a good plan.

    Let's do it.
    """

    psychic """
    Great !

    In the meantime, is there something else you wanted to talk about ?
    """

    call psychic_generic

    $ lad_day2_believe_psychic = True

    return

label lad_day2_believe_dont_believe_psychic:

    lad """
    I am sorry, but I think you are imagining things here.

    What happened today was just an unfortunate coincidence.

    There are no reasons to panic.
    """

    psychic angry """
    Really ?! That's what you think ?

    You believe I hallucinate things ?!

    Well if that's the case you better leave my room !
    """

    lad """
    No that's not what I meant. I am sorry.
    """

    psychic """
    Too late for that Mister Harring.

    Please leave my room.

    And good luck to you.
    """

    """
    I have no choice but to leave.
    """

    scene hallway

    return
