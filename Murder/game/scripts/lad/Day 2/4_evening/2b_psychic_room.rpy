label lad_day2_evening_psychic_room:

    $ change_room("bedrooms_hallway")

    lad """
    Miss Baxter?

    Are you here? It's Ted Harring.
    """

    """
    She slightly opens the door and looks in the hallway.

    She seems worried.
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
    So, have you given any thought to what I told you?

    Do you agree that something isn't right?
    """

    call run_menu(TimedMenu("lad_day2_evening_psychic_room", [
        TimedMenuChoice('I think you might be right', 'lad_day2_believe_psychic', 10, early_exit = True ),
        TimedMenuChoice('No, you are clearly imagining things', 'lad_day2_believe_dont_believe_psychic', early_exit = True)
    ]))

    return

label lad_day2_believe_psychic:

    lad """
    I'm not sure yet. But what happened is strange enough that we should take some precautions.
    """

    psychic """
    I'm glad you agree.

    I've given this a lot of thought, and I believe if what I fear is true, Samuel Manning had help from someone else.
    """

    $ play_music("mysterious")

    lad """
    Do you mean a guest? Or could someone from the staff be involved?
    """

    psychic """
    I wouldn't rule anything out, but it seems less likely that the staff or Lady Claythorn would be involved.

    Such an act would require a massive operation.

    No, a more plausible theory is that one or two individuals heard about the event and took the places of real guests to infiltrate the manor.
    """

    lad """
    But why would they do that?
    """

    psychic """
    Well, it's rather obvious, isn't it?

    The prize money, of course.

    It was mentioned in the invitation letter that the prize will be given in bearer's bonds.
    """

    lad """
    Bearer's bonds?
    """

    psychic """
    That's a note that you can exchange at the bank without having to prove your identity.

    So, it's almost as easy to use as cash.
    """

    lad """
    That's a lot of money hidden somewhere in the manor.
    """

    lad """
    So you think it could be a mere robbery?
    
    Why not just directly attack the manor?
    """

    psychic """
    It's easier to enter incognito.

    First, observe and then discreetly eliminate potential threats.

    That's the most likely explanation I could think of.
    """

    lad """
    I suppose that's possible.

    But there's no way to determine who might be involved.
    """

    psychic """
    Exactly.

    That's why I suggest we stay safely in our rooms tonight.

    Tomorrow morning, the first one of us to wake up should alert the other.

    Then we stick together the entire day until we can safely leave.

    What do you think?
    """

    $ play_music("PREVIOUS")

    lad """
    It sounds like a good plan.

    Let's do it.
    """

    psychic """
    Great!

    Is there anything else you'd like to discuss?
    """

    call psychic_generic

    $ lad_details.saved_variables["day2_believe_psychic"] = True

    return

label lad_day2_believe_dont_believe_psychic:

    lad """
    I'm sorry, but I believe you might be overthinking things.

    Today's incident was probably just an unfortunate coincidence.

    I don't see any reason to panic.
    """

    psychic angry """
    Really?! That's what you think?

    You think I'm just imagining things?!

    If that's your stance, then you better leave my room!
    """

    lad """
    That's not what I meant. I'm sorry.
    """

    psychic """
    It's too late for apologies, Mister Harring.

    Please leave my room.

    And good luck to you.
    """

    """
    I have no choice but to leave.
    """

    $ change_room("bedrooms_hallway")

    return
