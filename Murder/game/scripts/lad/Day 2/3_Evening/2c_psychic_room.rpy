label lad_day2_evening_bedroom_psychic:

    $ change_room("bedrooms_hallway")

    call common_day2_evening_lad_psychic_discussion_1

    call run_menu(TimedMenu("lad_day2_evening_bedroom_psychic", [
        TimedMenuChoice('Admit she might be right', 'lad_day2_believe_psychic', 30, early_exit = True ),
        TimedMenuChoice('No way, she is clearly imagining things', 'lad_day2_believe_dont_believe_psychic', 20, early_exit = True)
    ]))

    return

label lad_day2_believe_psychic:

    $ lad_details.important_choices.unlock('trust_psychic')

    call common_day2_evening_lad_psychic_discussion_2

    call psychic_generic

    lad """
    I think I should keep looking around the manor. I might learn something useful.
    """

    psychic """
    It's not a bad idea. I will stay here tonight if you don't mind.

    Good luck.
    """

    lad """
    Thanks.
    """

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
    It's too late for apologies, Mr Harring.

    Please leave my room.

    And good luck to you.
    """

    """
    I have no choice but to leave.
    """

    $ change_room("bedrooms_hallway")

    return
