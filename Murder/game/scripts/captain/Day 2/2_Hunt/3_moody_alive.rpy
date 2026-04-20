# --------------------------------------------
#   Captain - Saturday Hunt - V2 (Moody alive)
#
#   Grouping:
#       - Captain + Lady Claythorn + Thomas Moody + butler
#       - Doctor + Drunk + Lad + footman
#
#   Linear path: Moody isolates the Captain after luncheon
#                 and shoots him in the woods.
# --------------------------------------------

label captain_day2_hunt_moody_alive:

    broken """
    Come now, surely you shall have room for one more in the lady's party?

    I should be sorry to miss our hostess's company.
    """

    host """
    Why, Mr Moody, of course.

    The more the merrier.
    """

    """
    A chill passes through me at his easy smile.

    The letter on my bedside table.

    The man who may have written it, now inviting himself into my shooting party.

    I cannot object without drawing attention to myself.
    """

    captain """
    A pleasure, Mr Moody.
    """

    broken """
    The pleasure is entirely mine, Captain.
    """

    """
    The butler, who has watched the parties form with the unobtrusive attention of his trade, steps forward.
    """

    butler """
    Very good. Doctor Baldwin and Mr Manning to the western grove, with Mr Harring.

    The footman will go along with them.

    My lady, Captain Sinha and Mr Moody to the north field, and I shall attend.
    """

    call change_time(11, 45)

    $ change_room('forest')

    """
    We walk some distance before the first quarry presents itself.

    A pheasant, breaking cover not ten yards from our line.
    """

    play sound gun

    pause 1.0

    """
    Mr Moody's rifle cracks before mine is even at my shoulder.

    The bird drops cleanly.
    """

    host """
    Bravo, Mr Moody. A splendid shot.
    """

    broken """
    You flatter me, my lady.

    One does one's best.
    """

    """
    I do not care for the ease of it.

    That was not the shot of a man merely doing his best.
    """

    play sound gun

    pause 1.0

    """
    My own turn comes a few minutes later, at a rabbit in the heather.

    My hands are not as steady as I should like.

    The shot goes a full yard wide.
    """

    broken """
    Hard luck, Captain. Hard luck indeed.

    Though I confess I had expected rather better of a decorated officer.
    """

    # TODO: That's the host excuse's, find a better one
    captain """
    The light is most unhelpful today.
    """

    broken """
    Quite. The light.
    """

    """
    His tone carries the smallest edge, no more than a gentleman could credibly notice.

    I feel it nonetheless.
    """

    host """
    Oh, do leave the Captain in peace, Mr Moody.

    Not every gentleman cares to spend his weekends slaughtering birds.
    """

    """
    A kind intervention, though offered a touch too late to count as kind.
    """

    call change_time(12, 30)

    """
    We stop for luncheon in a clearing bordered by birches.

    The butler lays out a spread upon a linen cloth and serves the tea with his customary care.

    Mr Moody installs himself at Lady Claythorn's side and keeps up a steady flow of agreeable conversation.

    I eat very little and say less.
    """

    $ play_music('danger', 2)

    broken """
    Captain, you must come and see this.

    There's a rather curious cairn a few paces off, up the track.

    I wager you know your antiquities better than I do.
    """

    """
    I have not the slightest interest in his cairn.

    I have every interest in not being led alone into the trees.
    """

    host """
    Do go, Captain. Mr Moody has quite the eye for these things.
    """

    """
    The butler is tending to the horse at the edge of the clearing.

    Lady Claythorn has already returned to her tea.

    To refuse now would be conspicuous.
    """

    captain """
    Very well.
    """

    call change_time(13, 00)

    """
    I follow him up the track.

    He walks easily, his rifle slung at his shoulder, whistling a tune I do not recognise.

    Thirty yards from the clearing, the cover thickens. The voices from the luncheon fall away.

    He stops, turns, and lifts the rifle from his shoulder.

    Not to show me. To hold.
    """

    broken """
    That's far enough, I think, Captain.
    """

    """
    The muzzle is not yet levelled, but the grip is wrong for a man out for rabbits.

    My own rifle hangs at my side. There is a yard too many between us for me to bring it up in time.
    """

    captain """
    Mr Moody. What is the meaning of this?
    """

    # TODO: He didn't write a letter, but he receives another explaining who the captain was
    # The captain will explain that it means he is also in danger.
    # But thomas moody says he can quite look after hiself

    broken """
    The letter, Captain.

    You did read it, I hope.

    One hates to go to the trouble and find the recipient hasn't bothered.
    """

    captain """
    You wrote it.
    """

    broken """
    Of course I wrote it.

    An administrative officer, Captain. A man who spent the war behind a desk in Rawalpindi pushing paper about.

    And here you are, entertaining the table with tales of Burma and the Boxers as though you had ever heard a shot fired in anger.
    """

    """
    My mouth is dry.

    I have stood in front of angry colonels and unpaid sepoys without flinching.

    Yet here, in the quiet of a Scottish wood, I find I cannot speak.
    """

    broken """
    It's rather plain you never saw battle, Captain.

    Well. This is as close as it gets.
    """

    """
    He lifts the rifle in one clean movement.

    I raise a hand, uselessly.
    """

    play sound gun

    $ stop_music(1)

    pause 2.0

    jump captain_ending_shot_in_woods
