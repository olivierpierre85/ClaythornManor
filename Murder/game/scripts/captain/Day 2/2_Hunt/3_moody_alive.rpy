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
    Doctor Baldwin's party is already three guns strong.

    I shall round out your own, if my lady will have me.
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
    The butler steps forward.
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

    Mr Moody must be a remarkable marksman. His modesty is a performance.

    My own turn comes a few minutes later, at a rabbit in the grass.
    """

    play sound gun

    """
    My hands are not as steady as I should like.

    The shot goes a full yard wide.
    """

    broken """
    Hard luck, Captain. Hard luck indeed.

    Though I confess I had expected rather better of a decorated officer.
    """

    captain """
    I misjudged the lead.
    """

    broken """
    Quite. The lead.
    """

    """
    He is saying this playfully, but I cannot help but feel slighted.
    """

    """
    The morning wears on in this fashion.

    More birds burst from the bushes, and Mr Moody takes them without appearing to aim.

    Lady Claythorn's shots go wide. My own find nothing but empty air.

    By the time the butler calls us in, only Mr Moody has game to show.
    """

    call change_time(12, 30)

    """
    We stop for luncheon in a clearing bordered by birches.

    The butler lays out a spread upon a linen cloth and serves the tea with his customary care.

    Mr Moody installs himself at Lady Claythorn's side and keeps up a steady flow of agreeable conversation.

    I eat very little and say less.
    """

    call change_time(13, 00)

    broken """
    Captain, a word, if I may.

    My rifle has been pulling to the left all morning. I should value a second eye upon it.

    A few paces up the track will do.
    """

    """
    I don't like the idea of being led alone into the trees.

    But I can't find a proper reason not to go.

    My manners overrule my better judgement.
    """


    captain """
    Very well.

    Go on, Mr Moody. I shall be behind you.
    """


    $ play_music('danger', 2)
    
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
    I have his gun now pointing straight at me.

    My own rifle hangs at my side. There is a yard too many between us for me to bring it up in time.
    """

    captain """
    Mr Moody. What is the meaning of this?
    """

    broken """
    A letter arrived beneath my door this morning, Captain.

    A most illuminating little document.
    """

    broken """
    An administrative officer, it said. A man who spent the war behind a desk in Rawalpindi pushing paper about.

    And here you are, entertaining the table with tales of Burma and the Boxers as though you had ever heard a shot fired in anger.
    """

    """
    My mouth is dry.

    I have stood in front of angry colonels and unpaid sepoys without flinching.

    Yet here, in the quiet of a Scottish wood, I find the words slow in coming.
    """

    captain """
    There was another such letter placed in my room, Mr Moody.

    I had taken you for its author.
    """

    broken """
    I? Good heavens, no.

    It would appear we share a correspondent.
    """

    captain """
    Then consider what his purpose is.

    Whoever wrote to you means us both harm. You are being used to his end.
    """

    broken """
    How very considerate of you, Captain.

    I can quite look after myself, I assure you.
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
