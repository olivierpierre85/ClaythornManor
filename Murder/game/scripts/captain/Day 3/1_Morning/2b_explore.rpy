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

    Not the ordinary silence of an early hour, when the staff move quietly about their work.

    A heavier kind.

    No footsteps below stairs. No fires being laid. No clatter of breakfast trays.
    """

    captain """
    Something is wrong.
    """

    """
    I dress without hurry, and check the master key is still in my waistcoat pocket.

    Then I open the door.
    """

    call change_time(9, 0)

    $ change_room('bedrooms_hallway', dissolve)

    """
    The corridor is empty.

    The doors are all shut.

    I had thought I would meet at least one of the others up and dressed by now, but no one stirs.

    I have a few hours before the house ought to be sitting down to luncheon.

    I shall use them.
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

    return
