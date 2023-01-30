label lad_day2_evening_psychic_room:
    
    scene hallway
    
    lad """
    Miss Baxter?

    Are you here? It's Ted Harring
    """

    """
    She slightly opens the door and look in the hallway.

    She looks worried.
    """

    psychic """
    Mister Harring, are you alone?
    """

    lad """
    I am.
    """

    psychic """
    Come on in then.
    """

    $ change_room('psychic_room')

    psychic """
    So have you given any thought about what I told you?

    You agree that something not right is happening?
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

    I've given this a lot of thought, and I think if what I fear is true, he got help from someone else.
    """

    $ play_music("mysterious")

    lad """
    Do you mean a guest? Or someone in the staff could also be involved?
    """

    psychic """
    I wouldn't rule anything, but it's seems less likely that the staff or Lady Claythorn would be involved.

    This would require a tremendous operation.

    No, a more plausible theory is that one or two people heard about the event.
    
    They then stole the place of real guest to infiltrate the place.
    """

    lad """
    But why would they do that?
    """

    psychic """
    Well, it's rather obvious isn't it?

    The prize money of course.

    It was mentioned in the invitation letter, the prize will be handed in bearers bond.
    """

    lad """
    Bearers bond?
    """

    psychic """
    That's a note that you can exchange at the bank without having to prove your identity.

    So it's almost as easy to use as cash.
    """

    lad """
    Yes that's a lot of money hidden somewhere in the manor.
    """

    lad """
    So you think it could be a simple robbery?
    
    Why not just simply attack the manor?
    """

    psychic """
    It's easier to enter incognito.

    To first observe and then take down potential threats discretely.

    That's the most likely explanation I could come up with.
    """

    lad """
    I guess that's possible.

    But there is no way to determine who could be involved.
    """

    psychic """
    Precisely.

    That's why I think we should hide safely in our rooms tonight.
    
    Tomorrow morning, the first one to get up of the two of us will wake the other up.

    Then we stick together the whole day until we are free to leave.

    What do you think of that?
    """

    $ play_music("previous")

    lad """
    It sounds like a good plan.

    Let's do it.
    """

    psychic """
    Great !

    In the meantime, is there something else you wanted to talk about?
    """

    call psychic_generic

    $ lad_details.saved_variables["day2_believe_psychic"] = True

    return

label lad_day2_believe_dont_believe_psychic:

    lad """
    I am sorry, but I think you are imagining things here.

    What happened today was just an unfortunate coincidence.

    There are no reasons to panic.
    """

    psychic angry """
    Really?! That's what you think?

    You believe I hallucinate things?!

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
