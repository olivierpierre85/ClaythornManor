# --------------------------------------------
#   Common - Saturday Hunt - The North Field party
#
#   The Captain and the false Thomas Moody hunt the north field together with
#   Lady Claythorn and the butler. Shared by both storylines; narration
#   branches on current_character.text_id:
#       - "captain" : the Captain's point of view  (Ted Harring is alive)
#       - "broken"  : Moody's point of view         (Ted Harring is dead)
#
#   Callers:
#       - captain_day2_hunt_moody_alive -> common_day2_hunt_north_field
#       - broken_day2_hunt          -> both
# --------------------------------------------


# Moody joins the host's party, the shoot, and the luncheon, up to the point
# where the Captain is at Moody's mercy. Stops before the confrontation/choice.

label common_day2_hunt_north_field:

    call change_time(11, 45)

    $ change_room('forest_edge')

    # --- First bird: Moody shoots, the Captain does not even raise ---
    if current_character.text_id == "captain":

        """
        We walk some distance before the first quarry presents itself.

        A pheasant, breaking cover not ten yards from our line.
        """

    elif current_character.text_id == "broken":

        """
        We walk some distance before I spot a pheasant, not ten yards off our line.

        I have it before the Captain's rifle is even at his shoulder.
        """

    play sound gun

    if current_character.text_id == "captain":

        """
        Mr Moody's rifle cracks before mine is even at my shoulder.

        The bird drops cleanly.
        """

    elif current_character.text_id == "broken":

        pause 1.0

        """
        The bird drops cleanly.
        """

    host """
    Bravo, Mr Moody. A splendid shot.
    """

    broken """
    You flatter me, my lady.

    One does one's best.
    """

    # --- The Captain's turn: a clean miss at a sitting rabbit ---
    if current_character.text_id == "captain":

        """
        I do not care for the ease of it.

        Mr Moody must be a remarkable marksman. His modesty is a performance.

        My own turn comes a few minutes later, at a rabbit in the grass.
        """

    elif current_character.text_id == "broken":

        """
        The Captain's turn comes a few minutes on, at a rabbit sat in the grass.
        """

    play sound gun

    if current_character.text_id == "captain":

        """
        My hands are not as steady as I should like.

        The shot goes a full yard wide.
        """

    elif current_character.text_id == "broken":

        pause 1.0

        """
        He misses by a yard, and not for want of a steady morning.

        A decorated soldier, and he cannot put a ball into a rabbit sitting still in the open.

        I had wondered at it. Now I am sure.

        Whatever he was in the war, it was not what he tells the dinner table.
        """

    broken """
    Hard luck, Captain. Hard luck indeed.
    """

    captain """
    I misjudged the lead.
    """

    broken """
    Quite. The lead.
    """

    if current_character.text_id == "captain":

        """
        He is saying this playfully, but I cannot help but feel slighted.
        """

        pause 1.0

        """
        The morning wears on in this fashion.

        More birds burst from the bushes, and Mr Moody takes them without appearing to aim.

        Lady Claythorn's shots go wide.

        My own shots find nothing but empty air.

        By the time the butler calls us in, only Mr Moody has game to show.
        """

        $ host_details.description_hidden.unlock('hunt')

    elif current_character.text_id == "broken":

        """
        I let a little of the mockery show. I cannot help myself.

        So this is the great Captain Sinha. A man who cannot strike a rabbit at twenty paces, who holds forth each evening on Burma and the Boxers as though he had won the Empire single-handed.

        A counterfeit hero in a borrowed reputation. 
        
        Someone who sent others to the guns, and then dined out, year upon year, on a war he never once smelt.

        The anger rises in my throat like bile.
        """

        if broken_details.threads.is_unlocked('host_lies'):

            """
            And yet.

            Lady Claythorn fares no better with her piece. Twice the barrel dips toward the earth, and she carries it like a parasol grown unaccountably heavy.

            First her strange behavior during diner, then this.

            She is no more a great lady than the Captain is a great soldier.

            The thought sits there, cold and unwelcome, and draws a little of the heat from my anger.
            """

            $ host_details.description_hidden.unlock('hunt')

        """
        By the time the butler calls us in for luncheon, only I have any game to show for the morning.
        """

    call change_time(12, 30)

    $ change_room('forest_clearing', dissolve)

    host """
    Three birds and a pair of rabbits, Mr Moody. You are most impressive.

    I confess I had no notion we should be so splendidly provided for.
    """

    broken """
    Your ladyship is too generous.

    I was just very lucky today, that is all.

    Otherwise, I am certain a decorated veteran like Captain Sinha would have put me quite to shame.
    """

    return
