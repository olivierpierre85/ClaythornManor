label psychic_generic_other_guests:

    # TODO extend to phases
    if not 'psychic_generic_other_guests_menu' in locals():
        $ psychic_generic_other_guests_menu = TimedMenu([
            TimedMenuChoice('Ask about Samuel Manning', 'psychic_generic_drunk', 5),
            TimedMenuChoice('Talk about something else', 'psychic_generic_cancel', 0, keep_alive = True, early_exit = True)
        ], image_right = "psychic")

    call run_menu(psychic_generic_other_guests_menu)

    return

label psychic_generic_other_guests_friday:
    
    # DRINKS AND DINNER
    psychic """
    I've just met them. So I can't say to know a lot yet.

    All I know is that this guy over there ...
    """

    """
    She points at Sushil Sinha.
    """

    psychic """
    ... is monopolizing the conversation.

    And he is very noisy too.

    It's not very tactful if you ask me.
    """

    $ captain_details.add_knowledge('talker') 

    return

label psychic_generic_drunk:

    psychic """
    Well, I think by now you can tell as well as I that he is a dangerous drunk.

    We better stay away from him.
    """

    return
