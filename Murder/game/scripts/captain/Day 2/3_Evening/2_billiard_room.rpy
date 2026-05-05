# Billiard room — Saturday evening
# Captain enters alone and waits to see who, if anyone, will join him.
label captain_day2_evening_billiard_room:

    $ change_room('billiard_room')

    if not captain_details.saved_variables["day2_evening_billiard_room_visited"]:

        $ captain_details.saved_variables["day2_evening_billiard_room_visited"] = True

        """
        The billiard room is lit much as it was last night, but the warmth of the place has gone out of it.

        The decanters stand untouched on the side.

        The glasses have been laid out in expectation of a company that has chosen not to come.

        I am quite alone.
        """

        $ captain_day2_evening_billiard_room_menu = TimedMenu("captain_day2_evening_billiard_room_menu", [
            TimedMenuChoice('Wait and see who comes', 'captain_day2_evening_billiard_room_wait', 40),
            TimedMenuChoice('Pour a glass of sherry', 'captain_day2_evening_billiard_room_sherry', 10),
            TimedMenuChoice('Leave the room', 'generic_cancel', 0, keep_alive = True, early_exit=True),
        ])

    else:

        """
        I am back in the billiard room.

        The chairs sit much as I left them.
        """

        $ captain_day2_evening_billiard_room_menu.early_exit = False

    call run_menu(captain_day2_evening_billiard_room_menu)

    return


label captain_day2_evening_billiard_room_wait:



    call captain_day2_evening_billiard_room_nurse

    return


label captain_day2_evening_billiard_room_sherry:

    """
    I cross to the sideboard and pour a small measure of sherry from one of the decanters.

    The glass is good crystal, the sherry darker than I would have chosen for myself, but it will do.
    """

    return


label captain_day2_evening_billiard_room_nurse:

    """
    I take down a book from the shelf and settle into a chair by the fire.
    """

    call wait_screen_transition

    """
    A few minutes pass before the door eases open behind me.

    Miss Marsh hesitates a moment in the doorway, then crosses the room with her usual quiet composure.

    Whatever has brought her here, it was not for the company of the decanters.
    """

    call common_day2_evening_billiard_room_nurse_captain_intro

    call common_day2_evening_billiard_room_nurse_captain_two_deaths

    call common_day2_evening_billiard_room_nurse_captain_key

    """
    She regards me a moment longer than I should like.

    She did not believe a word of it.

    But she knows better than to press me on it tonight.
    """

    nurse """
    Good night, Captain.
    """

    captain """
    Good night, Miss Marsh.
    """

    """
    She withdraws as quietly as she came.

    The door clicks shut behind her, and the room is mine again.

    Whatever questions she came in with, she has gone away with most of them.

    But not all.
    """

    return
