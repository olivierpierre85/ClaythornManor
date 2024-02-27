label psychic_day2_hunt_tea_room:

    $ change_room("tea_room")

    """
    When I walk into the tea room, Rosalind Marsh is already there, sitting at a table.
    
    I head over to her.
    """

    nurse """
    Miss Baxter, would you like to join me?
    """

    psychic """
    Yes, thank you.
    """

    nurse """
    It seems we haven't really had a chance to talk yet, right?
    """

    # We have 45 minutes until we're interrupted NOT NEEDED NOW but could be working
    # $ remaining_time = time_left - 45
    # $ time_left = 45

    # QUICKFIX TO KEEP THE 120 TO make the hour turn, but should
    $ old_selected_choice = selected_choice

    call nurse_generic

    $ time_diff = datetime.combine(date.today(), current_time) + timedelta(minutes=old_selected_choice.time_spent)

    """
    While we're talking, a staff member walks in.
    """

    maid """
    Excuse me for interrupting, but do you ladies need some lunch?
    """

    """
    We chat about trivial things related to the host.

    After our conversation, Rosalind gets up from her seat.
    """

    nurse """
    I'm quite worn out with all that's happened.

    I think I'll go rest in my room. Don't mind being on your own?
    """

    psychic """
    Not a problem.

    There's a lot I can do.
    """

    $ psychic_details.saved_variables["day2_nohunt_has_visited_tea_room"] = True

    return

