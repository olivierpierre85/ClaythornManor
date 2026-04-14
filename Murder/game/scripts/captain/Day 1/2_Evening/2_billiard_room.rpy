# Billiard room
label captain_day1_evening_billiard_room:

    $ change_room('billiard_room')

    if not captain_details.saved_variables["day1_evening_billiard_room_visited"]:

        $ captain_details.saved_variables["day1_evening_billiard_room_visited"] = True

        """
        The billiard room is warm and well lit.

        Most of the guests have gathered here.

        Lady Claythorn is in conversation with Miss Marsh and Thomas Moody.

        Ted Harring hovers near them, looking as uncomfortable as ever.

        Daniel Baldwin sits alone in a chair, nursing a glass.

        And Manning is at the bar. Naturally.

        As I enter, a few heads turn my way.

        I recognise that look. They are bored and waiting for any kind of distraction.
        """

        $ captain_day1_evening_billiard_room_menu = TimedMenu("captain_day1_evening_billiard_room_menu", [
            TimedMenuChoice('Approach the large group', 'captain_day1_evening_billiard_room_story', 60),
            TimedMenuChoice('Have a drink at the bar', 'captain_day1_evening_billiard_room_bar', 10),
            TimedMenuChoice('Approach Dr Baldwin', 'captain_day1_evening_billiard_room_baldwin', 10),
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
    I make my way towards Lady Claythorn and the others.
    """

    host """
    Captain Sinha. Do come and join us.
    """

    captain """
    Thank you, Lady Claythorn.
    """

    nurse """
    Captain, you must tell us one of your stories.

    Mr Moody was just saying what a fine storyteller you are.
    """

    captain """
    How kind of him.

    Well, if you insist.
    """

    """
    I take a position near the fireplace and begin.

    This is my best story.

    I have told it so many times that it almost feels true.

    I speak of the Boxer Rebellion. The Eight-Nation Alliance. The march on Beijing.

    I give them the full account.
    """

    """
    Everyone is listening. Even the doctor has looked up from his glass.

    Good.

    The truth is, during the Boxer Rebellion, I was a supply officer stationed behind the lines.

    I never saw a single Boxer. I never fired a single shot.

    But I have read enough accounts of the expedition to describe it as though I were there.

    And over the years, the story has become so polished that even I sometimes forget the reality.
    """

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


label captain_day1_evening_billiard_room_baldwin:

    """
    I approach Baldwin.

    He looks up. His eyes are flat, offering nothing.

    I stop, give a small nod, and withdraw.

    Some conversations are better never begun.
    """

    return


label captain_day1_evening_billiard_room_cancel:

    """
    There is little here that warrants my attention.

    I leave.
    """

    return
