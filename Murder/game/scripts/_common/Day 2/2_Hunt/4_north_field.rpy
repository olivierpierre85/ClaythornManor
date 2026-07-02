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

    # --- Moody attaches himself to the north-field party ---
    if current_character.text_id == "captain":

        broken """
        Doctor Baldwin's party is already three guns strong.

        I shall round out your own, if my lady will have me.
        """

    elif current_character.text_id == "broken":

        """
        That settles one party, then. The doctor, the drunkard, and a footman to mind the pair of them.

        Which leaves our hostess and the Captain wanting a third gun for the other.

        I do not mean to leave that to chance.
        """

        broken """
        Doctor Baldwin and Mr Manning will do well enough together.

        I should be glad to make up your party, my lady, if you will have me.
        """

    host """
    Why, Mr Moody, of course.

    The more the merrier.
    """

    if current_character.text_id == "captain":

        """
        A chill passes through me.

        I would rather have avoided him this afternoon.

        But, I cannot object without drawing attention to myself.
        """

    captain """
    A pleasure, Mr Moody.
    """

    broken """
    The pleasure is entirely mine, Captain.
    """

    if current_character.text_id == "captain":

        """
        The butler steps forward.
        """

    elif current_character.text_id == "broken":

        """
        He returns my courtesy without a flicker.

        He has no notion of what I carry in my pocket, nor what I mean to make of the morning.

        Good.
        """

    # --- The butler splits the field (Ted only exists on the Captain's side) ---
    if current_character.text_id == "captain":

        butler """
        Very good. Doctor Baldwin and Mr Manning to the western grove, with Mr Harring.

        The footman will go along with them.

        My lady, Captain Sinha and Mr Moody to the north field, and I shall attend.
        """

    elif current_character.text_id == "broken":

        butler """
        Very good. Doctor Baldwin and Mr Manning to the western grove.

        The footman will go along with them.

        My lady, Captain Sinha and Mr Moody to the north field, and I shall attend.
        """
    
    return


label common_day2_hunt_north_field_2:

    call change_time(11, 45)

    $ change_room('forest')

    # --- First bird: Moody shoots, the Captain does not even raise ---
    if current_character.text_id == "captain":

        """
        We walk some distance before the first quarry presents itself.

        A pheasant, breaking cover not ten yards from our line.
        """

    elif current_character.text_id == "broken":

        """
        We walk some distance before the first quarry breaks cover. A pheasant, not ten yards off our line.

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

    elif current_character.text_id == "broken":

        """
        I let a little of the mockery show. I cannot help myself.

        So this is the great Captain Sinha. A man who cannot strike a rabbit at twenty paces, who holds forth each evening on Burma and the Boxers as though he had won the Empire single-handed.

        A counterfeit hero in a borrowed reputation. The very hand that signed Tom away to the guns, and then dined out, year upon year, on a war he never once smelt.

        The anger rises in my throat like bile.
        """

        if broken_details.threads.is_unlocked('host_lies'):

            """
            And yet.

            Lady Claythorn fares no better with her piece. Twice the barrel dips toward the earth, and she carries it like a parasol grown unaccountably heavy.

            She is no more a great lady than the Captain is a great soldier. I would stake the letter upon it.

            Perhaps every soul beneath this roof is wearing a face that is not their own.

            And if that is so, the Captain's lie tells me nothing of Tom. It tells me only that he is playing a part, the same as the rest of us.

            The thought sits there, cold and unwelcome, and draws a little of the heat from my anger.
            """

        else:

            """
            Lady Claythorn fares no better with her piece, dipping the barrel and handling it like a parasol.

            But it is the Captain my eye keeps returning to.

            There is not an honest article in this whole party.

            Myself least of all.
            """

        """
        By the time the butler calls us in for luncheon, only I have any game to show for the morning.
        """

    $ host_details.description_hidden.unlock('hunt')

    call change_time(12, 30)

    host """
    Three birds and a pair of rabbits, Mr Moody. You are most impressive.

    I confess I had no notion we should be so splendidly provided for.
    """

    broken """
    Your ladyship is too generous.

    I was just very lucky today, that is all.

    Otherwise, I am certain a decorated veteran like Captain Sinha would have put me quite to shame.
    """

    if current_character.text_id == "captain":

        """
        He says it politely enough, but I feel the mockery in his tone.

        I force a thin smile and say no more.

        We settle for luncheon in a clearing bordered by birches.

        The butler lays out a spread upon a linen cloth and serves the tea with his customary care.

        Mr Moody installs himself at Lady Claythorn's side and keeps up a steady flow of agreeable conversation.

        I eat very little and say less.
        """

    elif current_character.text_id == "broken":

        """
        The Captain says nothing to that. He only smiles, thin and correct.

        We settle for luncheon in a clearing among the birches. The butler lays a cloth and pours the tea with his customary care.
        """

    call change_time(13, 0)

    return
