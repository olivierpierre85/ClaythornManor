# Billiard room — Saturday evening
# Captain enters alone. The evening runs 21:00 → 23:00.
# Each "wait" costs 20 minutes. Whoever joins him depends on the time slot
# the wait begins in:
#   21:00 – 21:20 → Miss Marsh (nurse)            -> 2a_nurse.rpy
#   21:20 – 21:40 → Empty — captain reads, no one comes
#   21:40 – 22:00 → Mr Harring (lad)              -> 2b_lad.rpy
#   22:00 – 22:20 → Empty — captain reads, no one comes
#   22:20 – 22:40 → Empty — captain reads, no one comes
#   22:40 – 23:00 → Lady Claythorn (host)         -> 2c_host.rpy
# A captain who lingers elsewhere first will simply miss earlier visitors.
label captain_day2_evening_billiard_room:

    $ change_room('billiard_room')

    if not captain_details.saved_variables["day2_evening_billiard_room_visited"]:

        $ captain_details.saved_variables["day2_evening_billiard_room_visited"] = True

        """
        The billiard room is lit much as it was last night, but the warmth of the place has gone out of it.

        The decanters stand untouched on the side.

        The glasses have been laid out in expectation of company that has chosen not to come.

        I am quite alone.
        """

        $ captain_day2_evening_billiard_room_menu = TimedMenu("captain_day2_evening_billiard_room_menu", [
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_nurse_with_suspicions', 20, next_menu="captain_day2_evening_billiard_room_nurse_menu",
                condition="time_left>100 and " + condition_captain_host_suspicions),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_nurse_no_suspicions', 20,
                condition="time_left>100 and not " + condition_captain_host_suspicions),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_empty_1', 20,
                condition="time_left>80 and time_left<=100"),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_lad_with_suspicions', 20, next_menu="captain_day2_evening_billiard_room_lad_menu",
                condition="time_left>60 and time_left<=80 and " + condition_captain_host_suspicions),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_lad_no_suspicions', 20,
                condition="time_left>60 and time_left<=80 and not " + condition_captain_host_suspicions),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_empty_2', 20,
                condition="time_left>40 and time_left<=60"),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_empty_3', 20,
                condition="time_left>20 and time_left<=40"),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_host_with_suspicions', 0, next_menu="captain_day2_evening_billiard_room_host_menu",
                condition="time_left<=20 and " + condition_captain_host_suspicions),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_host_no_suspicions', 20,
                condition="time_left<=20 and not " + condition_captain_host_suspicions),
            TimedMenuChoice('Pour a glass of sherry',
                'captain_day2_evening_billiard_room_sherry', 10),
            TimedMenuChoice('Leave the room',
                'generic_cancel', 0, keep_alive=True, early_exit=True),
        ])

    else:

        """
        I am back in the billiard room.

        The chairs sit much as I left them.
        """

        $ captain_day2_evening_billiard_room_menu.early_exit = False

    call run_menu(captain_day2_evening_billiard_room_menu)

    return


label captain_day2_evening_billiard_room_sherry:

    """
    I cross to the sideboard and pour a small measure of sherry from one of the decanters.

    The glass is good crystal, the sherry darker than I would have chosen for myself, but it will do.
    """

    return

label captain_day2_evening_billiard_room_wait:

    if captain_details.saved_variables["day2_evening_billiard_encounters"] == 0:

        """
        I sit down on a chair by the fire.
        
        On the table next to it is a book: "The Seven and a Half Lives of Evelyn Softhovel".

        It is not at all the sort of thing I should choose for myself, but the evening offers little else, so I take it up.
        """

        call wait_screen_transition

    elif captain_details.saved_variables["day2_evening_billiard_encounters"] == 1:

        """
        I turn a few more pages, more for the look of the thing than to read.
        """

        call wait_screen_transition

        """
        After a little while, the door opens a second time.
        """

    else:

        """
        It is getting late, yet I feel as though I could wait a little longer.

        Mostly because I cannot set the book down.
        """

        call wait_screen_transition

        """
        The door opens a third time — and stops short.
        """

    $ captain_details.saved_variables["day2_evening_billiard_encounters"] += 1

    return


# ------------------------------------
#   Empty waits — captain reads, no one comes
# ------------------------------------
label captain_day2_evening_billiard_room_empty_1:

    """
    I turn back to my book and try to settle to it.

    A page or two go by, easily enough.
    """

    call wait_screen_transition

    """
    The fire shifts in the grate, and the clock on the mantel ticks on.

    Nobody disturbs me.
    """

    return


label captain_day2_evening_billiard_room_empty_2:

    """
    I read on, though the words come more slowly now.
    """

    call wait_screen_transition

    """
    Nothing stirs in the corridor beyond.

    The house has gone properly quiet.
    """

    return


label captain_day2_evening_billiard_room_empty_3:

    """
    I am quite absorbed in the book now, and pay attention to little else.
    """

    call wait_screen_transition

    """
    Still no one comes.
    """

    return
