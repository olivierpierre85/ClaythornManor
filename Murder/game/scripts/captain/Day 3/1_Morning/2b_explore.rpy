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
    There is no one is the corridor.

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

    Now I need to understand what.
    """

    $ time_left = 150

    call run_menu(captain_details.saved_variables["day3_morning_map_menu"])

    call change_time(11, 30)

    $ change_room('entrance_hall', dissolve)

    """
    I have walked the house from the cellar to the eaves and found nothing alive in it save dust.

    The dead lie where we left them. The living are not in their rooms.

    I come back to the entrance hall to think.
    """

    pause 0.5

    """
    A voice rises from the foot of the stair.
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

    """
    I let the silence sit a moment before I break it.
    """

    captain """
    Have you found anyone else?
    """

    psychic """
    No one.

    We have knocked on every door upstairs.

    Miss Marsh's room is locked and she does not answer.

    Lady Claythorn's room is empty, and her things are scattered about.

    Mr Manning we have not been able to reach.
    """

    if captain_details.saved_variables["day3_morning_drunk_checked"]:

        # The captain went into Manning's room during his own search.
        captain """
        Mr Manning will not be coming down.

        I went into his room myself. He was killed in his bed during the night.
        """

        psychic surprised """
        Oh dear God.
        """

        lad """
        Killed?
        """

        captain """
        Throat cut.

        Whoever did it had a key. He never woke.
        """

        """
        Miss Baxter sits down on the lowest step.

        Mr Harring takes a moment to find his voice.
        """

        if captain_details.saved_variables["day3_morning_nurse_checked"]:

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

        lad """
        What are we to do?
        """

        captain """
        We stop walking the corridors on our own.

        From now on, we keep together.
        """

        psychic """
        Should we not search a little more?

        There may still be someone in the house who needs help.
        """

        captain """
        We will. But not in three separate parties.

        Take a few minutes in the tea room. I will see to Miss Baxter, and then we go on together.
        """

        lad """
        Right. The tea room.
        """

        psychic """
        Thank you, Captain.
        """

        """
        She rises, and the three of us cross the hall together.
        """

        $ change_room('tea_room', dissolve)

    else:

        # The captain never reached Manning's room, so the three of them
        # discover him together, as on the lad's and psychic's paths.
        captain """
        His room is locked, and I am the one with the master key.

        We had better look in on him before we do anything else.
        """

        call common_day3_morning_lad_psychic_captain_death_manning

        if captain_details.saved_variables["day3_morning_nurse_checked"]:

            # death_manning's tail had the captain offer to check the last locked
            # door with the lad. He has already opened it himself, so he stands
            # the boy down and reports what he found instead.
            captain """
            On reflection, Mr Harring, there is no need for you to come.

            The last locked door upstairs is Miss Marsh's, and I let myself into it on my round this morning.
            """

            captain """
            It was empty. Her bed had not been slept in.

            Wherever she is, she did not pass the night there.
            """

            psychic """
            Then she may yet be somewhere in the house.
            """

            captain """
            Perhaps. Rest here a while longer, the both of you.

            I will take another turn about the place and be back before noon.
            """

            """
            The boy sinks back into his chair. Miss Baxter does the same.
            """

        else:

            call common_day3_morning_lad_psychic_captain_marsh_empty

            call common_day3_morning_lad_psychic_captain_deaths_end

    return
