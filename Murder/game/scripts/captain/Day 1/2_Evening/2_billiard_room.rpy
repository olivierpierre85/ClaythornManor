# Billiard room
label captain_day1_evening_billiard_room:

    $ change_room('billiard_room')

    if not captain_details.saved_variables["day1_evening_billiard_room_visited"]:

        $ captain_details.saved_variables["day1_evening_billiard_room_visited"] = True

        """
        The billiard room is warm and well lit.

        Most of the guests have gathered here.

        Thomas Moody stands near the fireplace. Lady Claythorn is in conversation with Miss Marsh.

        Ted Harring hovers near the bar, looking as uncomfortable as ever.

        Daniel Baldwin sits alone in a chair, nursing a glass.

        And Manning is at the bar. Naturally.
        """

        """
        As I enter, a few heads turn my way.

        I recognise that look. They are hoping I will talk.

        Good. That is precisely what I intend to do.
        """

        $ captain_day1_evening_billiard_room_menu = TimedMenu("captain_day1_evening_billiard_room_menu", [
            TimedMenuChoice('Tell the group about the Boxer Rebellion', 'captain_day1_evening_billiard_room_story', 60),
            TimedMenuChoice('Have a drink at the bar', 'captain_day1_evening_billiard_room_bar', 10),
            TimedMenuChoice('Leave the room', 'captain_day1_evening_billiard_room_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ captain_day1_evening_billiard_room_menu.early_exit = False

        """
        I am back in the billiard room.
        """

    call run_menu(captain_day1_evening_billiard_room_menu)

    return


label captain_day1_evening_billiard_room_story:

    """
    I take a position near the fireplace and begin.

    This is my best story. The one I have been saving.

    I have told it so many times that it almost feels true.
    """

    call common_day1_evening_captain_billiard_room_speech_part_1

    """
    Everyone is listening. Even the doctor has looked up from his glass.

    Good. Now for the main act.

    The truth is, during the Boxer Rebellion, I was a supply officer stationed behind the lines.

    I never saw a single Boxer. I never fired a single shot.

    But I have read enough accounts of the expedition to describe it as though I were there.

    And over the years, the story has become so polished that even I sometimes forget the reality.
    """

    $ captain_details.description_hidden.unlock('lie')

    call common_day1_evening_captain_billiard_room_speech_part_2

    """
    I finish the story and pause, letting the silence settle.

    Miss Marsh is studying me. There is something in her expression that I do not quite like.

    But the rest of the room seems satisfied.

    Mr Moody nods approvingly. Lady Claythorn offers a polite smile.

    It is a good story. That is what matters.
    """

    return


label captain_day1_evening_billiard_room_bar:

    """
    I make my way to the bar.

    Manning is there, slumped against the counter.

    I pour myself a small measure of port and stand apart from him.

    There is nothing to be gained from associating with a drunkard.
    """

    return


label captain_day1_evening_billiard_room_cancel:

    """
    I have done enough for one evening.
    """

    return
