label psychic_day1_evening_billiard_room:

    $ change_room('billiard_room')

    if not psychic_details.saved_variables["day1_evening_billiard_room_visited"]:

        $ psychic_details.saved_variables["day1_evening_billiard_room_visited"] = True

        """
        It appears that most guests have chosen to gather here.

        Daniel Baldwin stands alone in the corner.

        Ted Harring is at the bar with Samuel Manning.

        A crowd has formed around Sushil Sinha.

        He is likely monopolizing the conversation.
        """


        $ psychic_day1_evening_billiard_room_menu = TimedMenu("psychic_day1_evening_billiard_room_menu", [
            TimedMenuChoice('Talk to Daniel Baldwin', 'psychic_day1_evening_billiard_room_doctor', 10),
            TimedMenuChoice('Suffer an other story by Mister Sinha', 'psychic_day1_evening_billiard_room_group', 120),
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
    Mister Baldwin, we haven't been introduced yet.

    I am Amelia Baxter.
    """

    doctor """
    Nice to meet you miss Baxter.
    """

    call doctor_generic

    return

label psychic_day1_evening_billiard_room_group:

    """
    I discretely approach the group.

    The story has just begun.
    """

    call common_day1_evening_captain_billiard_room_speech_part_1

    call common_day1_evening_captain_billiard_room_speech_part_2

    """
    Well that was a long detour for such a simple question.
    """

    return

label psychic_day1_evening_billiard_room_bar:

    psychic """
    Hello again, Mister Harring.

    Mister Manning.
    """

    lad """
    Oh, hi Miss Baxter.

    Don't mind Mister Manning.

    I think he might have had one too many.
    """

    """
    Yes, or maybe ten too many.
    """

    lad """
    Would you like something to drink?

    We have port and sherry.
    """

    psychic """
    That's not a wide selection.

    But I'll take a sherry, thank you.
    """

    lad """
    No problem. I'll pour one for myself as well.
    """

    """
    He is shaking slightly while pouring the drinks.

    Could he be a bit drunk as well?
    """

    # TODO: ADD fun question for a drunk lad.
    call lad_generic

    return
