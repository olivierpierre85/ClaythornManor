label psychic_day1_evening_billiard_room:

    $ change_room('billiard_room')

    if not psychic_details.saved_variables["day1_evening_billiard_room_visited"]:

        $ psychic_details.saved_variables["day1_evening_billiard_room_visited"] = True

        """
        It appears that most guests have chosen to gather here.

        Daniel Baldwin stands alone in the corner.

        Ted Harring is at the bar with Samuel Manning.

        A crowd has formed around Sushil Sinha.

        He is likely monopolising the conversation.
        """


        $ psychic_day1_evening_billiard_room_menu = TimedMenu("psychic_day1_evening_billiard_room_menu", [
            TimedMenuChoice('Talk to Daniel Baldwin', 'psychic_day1_evening_billiard_room_doctor', 10),
            TimedMenuChoice('Endure another story by Mr Sinha', 'psychic_day1_evening_billiard_room_group', 120),
            TimedMenuChoice('Go to the bar', 'psychic_day1_evening_billiard_room_bar', 20),
            TimedMenuChoice('Leave the room', 'generic_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ psychic_day1_evening_billiard_room_menu.early_exit = False

        """
        I should check again what's happening here.
        """

    call run_menu(psychic_day1_evening_billiard_room_menu)
    
    return


label psychic_day1_evening_billiard_room_doctor:
    
    psychic """
    Mr Baldwin, we have not been introduced yet.

    I am Amelia Baxter.
    """

    doctor """
    Pleased to meet you, Miss Baxter.
    """

    call doctor_generic

    return


label psychic_day1_evening_billiard_room_group:

    """
    I discreetly approach the group.

    The story has just begun.
    """

    call common_day1_evening_captain_billiard_room_speech_part_1

    call common_day1_evening_captain_billiard_room_speech_part_2

    """
    Well, that was a long detour for such a simple question.
    """

    return


label psychic_day1_evening_billiard_room_bar:

    psychic """
    Good evening, Mr Harring.

    Mr Manning.
    """

    lad """
    Oh, hi Miss Baxter.

    Don't mind Mr Manning.

    I think he might have had one too many.
    """

    """
    Yes, or perhaps ten too many.
    """

    lad """
    Would you like something to drink?

    We have port and sherry.
    """

    psychic """
    That is not a wide selection.

    But I shall have a sherry, thank you.
    """

    lad """
    No problem. I'll pour one for myself as well.
    """

    """
    He is trembling slightly while pouring the drinks.

    Could he be a little drunk as well?
    """

    # TODO: ADD fun question for a drunk lad.
    call lad_generic

    return
