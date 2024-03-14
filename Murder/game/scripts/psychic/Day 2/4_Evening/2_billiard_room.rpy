label psychic_day2_evening_billiard_room:

    $ change_room('billiard_room')

    if not psychic_details.saved_variables["day2_evening_billiard_room_visited"]:

        $ psychic_details.saved_variables["day2_evening_billiard_room_visited"] = True

        """
        Just as I expected, the place is almost empty.

        Besides the butler, I can only see one other person in the room:

        Captain Sinha.

        Bloody hell.

        He has spotted me.

        Now, I can't avoid talking to him without looking impolite.

        At least the bar is still there.
        """

        # day2_evening_billiard_room_talk_to_captain
        # TODO: add interaction with the butler
        $ psychic_day2_evening_billiard_room_menu = TimedMenu("psychic_day2_evening_billiard_room_menu", [
            TimedMenuChoice("First things first, go to the bar for a drink", 'psychic_day2_evening_billiard_room_bar', 10),
            TimedMenuChoice("Reluctantly talk to Sushil Sinha", 'psychic_day2_evening_billiard_room_captain', 20),
            TimedMenuChoice("Politeness be damned, I'm out of here", 'generic_cancel', 0, condition="not psychic_details.saved_variables['day2_evening_billiard_room_talk_to_captain']", keep_alive=True, early_exit=True),
            TimedMenuChoice("Leave the room", 'generic_cancel', 0, condition="psychic_details.saved_variables['day2_evening_billiard_room_talk_to_captain']", keep_alive=True, early_exit=True),
        ])

    else:
        # Reset menu
        $ psychic_day2_evening_billiard_room_menu.early_exit = False

        """
        I am back in the Billiard Room.
        """

    call run_menu(psychic_day2_evening_billiard_room_menu)

    return

label psychic_day2_evening_billiard_room_bar:

    """
    I'll have a glass of sherry, as it's the only decent drink I can see.
    """

    if not psychic_details.saved_variables['day2_evening_billiard_room_talk_to_captain']:
    
        """
        Captain Sinha has looked up from his book and is now staring at me.

        I can't very well ignore him now.
        """

    return


label psychic_day2_evening_billiard_room_captain:

    $ psychic_details.saved_variables["day2_evening_billiard_room_talk_to_captain"] = True

    """
    I suppose I have no choice but to speak with him, at least for a little while.

    Approaching him, I notice his expression is quite grave. 

    He looks at me with piercing look, as if to assess wether I am a threat.
    
    I sit down beside him, acutely aware of the tension between us.
    """

    captain """
    Miss Baxter.

    I wouldn't have thought you'd come here.
    """

    psychic """
    I wasn't sure I would to be honest.

    The atmosphere of this house has become quite sinister.

    But the idea of waiting alone in my room is not very reassuring either, so here I am.
    """

    captain """
    Yes, sorry that there isn't a larger company here.

    Everyone else seems to have been too scared to come.
    """

    psychic """
    Oh that's quite alright.

    But I am afraid I am not be staying long anyway.
    """

    # captain """
    # I hope you are not afraid of me?
    # """

    call captain_generic

    return
