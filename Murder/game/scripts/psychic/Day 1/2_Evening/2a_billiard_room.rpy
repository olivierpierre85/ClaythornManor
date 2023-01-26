label psychic_day1_evening_billiard_room:

    $ change_room('billiard_room')

    if not psychic_details.saved_variables["day1_evening_billiard_room_visited"]:

        $ psychic_details.saved_variables["day1_evening_billiard_room_visited"] = True

        """
        It seems that most guests have decided to come here.

        There is Daniel Baldwin alone in the corner.

        Ted Harring is at bar with Samuel Manning.

        And there is a circle around Sushil Sinha.
        
        He is probably boring everyone.
        """

        $ psychic_day1_evening_billiard_room_menu = TimedMenu([
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

    call captain_billiard_room_speech_part_1

    call captain_billiard_room_speech_part_2

    """
    Well that was a long detour for such a simple question.
    """

    return

label psychic_day1_evening_billiard_room_bar:

    # Normal lad choices, but EXTRA question if drunk?
    psychic """
    Hello again Mister Harring.

    Mister Manning.
    """

    lad """
    Oh hi Miss Baxter.

    Don't pay attention to mister Manning.

    I think he may have drank one too many.
    """

    """
    Yes, or ten too many more like.
    """

    lad """
    Would like something to drink?

    There is port and sherry.
    """

    psychic """
    That's not a lot of choice.

    But a sherry will do. Thank you.
    """

    lad """
    No problem. I'll pour one for myself as well.
    """

    psychic """
    He is slightly shaking while pouring the drinks.

    Is he also a bit drunk?
    """

    # TODO ADD fun question for a drunk lad.
    call lad_generic

    return