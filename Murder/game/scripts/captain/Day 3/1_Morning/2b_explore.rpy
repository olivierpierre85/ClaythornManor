# --------------------------------------------
#   Captain — Sunday morning, exploration path
#
#   No confidence with Miss Marsh.
#   The captain wakes in his room, walks the house alone, then meets
#   Ted Harring and Amelia Baxter in the entrance hall as the morning ends.
# --------------------------------------------

label captain_day3_morning_explore:

    $ change_room('bedroom_captain', irisout)

    """
    I sleep in fits and wake well before the gong should have sounded.

    The house is silent.

    Not the ordinary silence of an early hour.

    A heavier kind.

    No footsteps below stairs. No fires being laid. No clatter of breakfast trays.

    I dress without hurry, and check the master key is still in my waistcoat pocket.

    Then I open the door.
    """

    call change_time(9, 0)

    $ change_room('bedrooms_hallway', dissolve)

    """
    There is no one in the corridor.

    The doors are all shut.

    I head to the dining room.
    """

    $ change_room('dining_room', dissolve)

    """
    The room is empty.

    The table has not been laid.

    No one has been down before me.

    A cold feeling engulfs me.

    All my doubts, the things I had noticed about our host, were not my imagination.

    Something is clearly wrong in this house.

    I think about the telephone, I believe it was somewhere in the entrance hall.
    """

    $ change_room("entrance_hall")

    """
    I found the telephone in the corner of the room and pick it up.

    No signal.

    Maybe Lady Claythorn disconnected it before she left.

    Or maybe it was never working.

    I consider what to do.

    My instincts tell me to search the house and find out what has become of the others.

    But I could also shut myself in my own room, lock the door, and simply wait to see what happens.
    """

    call change_time(9, 30)

    $ time_left = 120

    call run_menu(captain_details.saved_variables["day3_morning_map_menu"])

    if time_left <= 0:

        $ change_room('entrance_hall', dissolve)

        """
        I have been searching the house for some time now.

        I come back to the entrance hall to think.
        """

    call change_time(11, 30)

    pause 1

    """
    Suddenly, I hear a voice rising.
    """

    lad """
    Hello? Is anyone there?
    """

    captain """
    Mr Harring. I am here.
    """

    """
    Ted Harring appears at the bottom of the stair, with Miss Baxter just behind him.

    Some of the colour comes back into his face when he sees me.
    """

    call common_day3_morning_meeting_captain

    captain """
    We have got a lot to talk about, maybe we should settle somewhere more comfortable.
    """

    psychic """
    The tea room perhaps?
    """

    captain """
    Perfect.
    """

    $ change_room("tea_room")

    """
    Everyone finds a chair before we can continue our conversation.
    """

    captain """
    So you have not found anyone else?
    """

    psychic """
    No one.

    We have knocked on every door upstairs.

    Miss Marsh's room is locked and she does not answer.

    Lady Claythorn's room is empty, and her things are scattered about.

    Mr Manning we have not been able to reach.
    """

    # On his solo round the captain may already have settled two of the rooms
    #   day3_morning_drunk_checked - he found Mr Manning dead in his bed
    #   day3_morning_nurse_checked - he let himself into Miss Marsh's empty room

    if captain_details.saved_variables["day3_morning_drunk_checked"]:

        # He saw Manning's body himself, so he breaks the news here rather than
        # leading the others up to discover it.
        captain """
        Mr Manning will not be coming down.

        I went into his room myself. He was killed in his bed during the night.
        """

        psychic surprised """
        Oh dear God.
        """

        lad -scared """
        Killed?
        """

        captain """
        Throat cut.

        Whoever did it had a key. He never woke.
        """

        """
        Miss Baxter sinks into the nearest chair.

        Mr Harring takes a moment to find his voice.
        """

    else:

        # The captain never reached Manning's room, so the three of them
        # discover him together, as on the lad's and psychic's paths.
        captain """
        Well, Samuel Manning is normally in his room, since I locked him there yesterday. 

        We had better look in on him before we do anything else.
        """

        call common_day3_morning_lad_psychic_captain_death_manning

    if captain_details.saved_variables["day3_morning_nurse_checked"]:

        # He opened Miss Marsh's room on his round too, so he can speak to it.
        captain """
        There is Miss Marsh's room besides. I let myself into it this morning.

        It was empty, her bed not slept in. She was not there.
        """

        psychic """
        Then she is somewhere about the house, or gone from it altogether.
        """

        captain """
        One or the other. We shall not settle which by standing apart.
        """

    else:

        call common_day3_morning_lad_psychic_captain_search_nurse

        call common_day3_morning_lad_psychic_captain_marsh_empty

        call common_day3_morning_lad_psychic_captain_search_report

    call common_day3_morning_lad_psychic_captain_deaths_end


    return
