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
    A chill passes through me.

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

    pause 1.0

    """
    The morning wears on in this fashion.

    More birds burst from the bushes, and Mr Moody takes them without appearing to aim.

    Lady Claythorn's shots go wide. 
    
    My own find nothing but empty air.

    By the time the butler calls us in, only Mr Moody has game to show.
    """

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

    """
    He says it politely enough, but I feel the mockery in his tone.

    I force a thin smile and say no more.

    We settle for luncheon in a clearing bordered by birches.

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

    Thirty yards from the clearing, the cover thickens. 
    
    The voices from the luncheon fall away.

    He stops, turns, and lifts the rifle from his shoulder.

    Not to show me. To hold.
    """

    broken """
    That's far enough, I think, Captain.
    """

    """
    I have his gun now pointing straight at me.
    """
    
    captain """
    Mr Moody. What is the meaning of this?
    """

    """
    My own rifle hangs at my side. There is a yard too many between us for me to bring it up in time.
    """

    broken """
    I found a letter on my bed yesterday.

    It told an interesting story.

    One about an administrative officer from India, a man who spent his wars pushing paper about.

    I believe you recognise whose story this is, Captain.

    Yet here you are, entertaining the table with tales of Burma and the Boxers as though you had fought in them yourself.
    """

    broken """
    But the true sting of it, Captain, lay in the final page.

    Owing to a blatant failure of communication, a column was sent up an open ridge in the autumn of '17.

    Three hundred men were cut down in the space of an afternoon, and many more gravely wounded.

    Some were left so disfigured that they must wear masks such as this for the rest of their days.
    """

    """
    He taps the porcelain of his mask with two gloved fingers.
    """

    broken """
    Their lives were ruined forever.

    And the letter was careful to note who signed the wrong order.

    You shall not be surprised to learn it was you, Captain.

    So many innocent victims, because of your incompetence.s
    """

    """
    My mouth is dry.

    I have stood in front of angry colonels without flinching.

    Yet here, in the quiet of a Scottish wood, I find the words stuck in my throat.

    I have signed a great many papers in my time. Transfers, requisitions, routine dispatches.

    Most of them I could not recall if my life depended upon it.

    Yet I cannot believe I am the man his letter describes.

    Amid all the horrors of those years, a sin of that magnitude would not have slipped my memory.

    Whatever happened to him, I am not responsible. I am sure of that.
    """

    captain """
    That is a slander, Mr Moody.

    I have never sent men to their deaths by mistake.

    I am in no way responsible for your... for your... condition.
    """

    """
    He does not lower the rifle.

    His gaze is resolute, heavy with a hatred.

    I see now there is nothing I can say that will change his mind.
    """

    captain """
    Then you were the one who placed the letter in my room.

    The one accusing me.
    """

    broken """
    A letter in your room?

    No, that was not me.

    Why would I have done something so foolish?

    It would only have tipped you off.
    """

    captain """
    Then consider what its purpose is.

    Someone here is manufacturing all of this.

    He was likely hoping for precisely this to happen.

    You are being used to his end.

    And you are no safer than I.
    """

    broken """
    How very considerate of you, Captain.

    I can quite look after myself, I assure you.
    """

    """
    He levels the rifle at my head.

    I raise a hand, uselessly.
    """

    broken """
    It is rather plain you never saw battle, Captain.

    Well. This is as close as it gets.
    """

    play sound gun

    $ stop_music(1)

    pause 1.0

    jump captain_ending_shot_in_woods
