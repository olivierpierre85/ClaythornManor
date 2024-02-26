label psychic_day2_hunt_tea_room:

    $ change_room("tea_room")

    """
    As I enter the tea room, I can see Rosalind Marsh already seated at one of the tables.

    I approach her.
    """

    nurse """
    Miss Baxter, would you like to sit with me?
    """

    psychic """
    Of course.
    """

    nurse """
    We haven't had much time to discuss things, have we?
    """

    # Get only 45 minutes before being interrupted, but regain the time for later exploration.
    $ remaining_time = time_left
    $ time_left = 45

    call nurse_generic

    $ time_left += remaining_time

    maid """
    I am sorry to disturb you ladies, but would you like some lunch?
    """

    """
    We make inconsequential chit-chat about the host.

    When we finish, Rosalind Marsh stands up.
    """

    nurse """
    Well, all these events have made me quite tired.

    I will retire to my room for a while if you don't mind being alone for a bit.
    """

    psychic """
    Not at all.

    There is plenty to do here.
    """

    $ psychic_details.saved_variables["day2_nohunt_has_visited_tea_room"] = True

    return
