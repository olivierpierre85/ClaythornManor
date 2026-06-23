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

    I would rather have avoided him this afternoon.

    But, I cannot object without drawing attention to myself.
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

    My own shots find nothing but empty air.

    By the time the butler calls us in, only Mr Moody has game to show.
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

    My rifle has been pulling to the left all morning.

    I should value a second eye upon it.

    A few paces up the track will do.
    """

    """
    I do not like the idea of following him alone into the trees.

    And it is hard to believe there is anything wrong with his weapon.

    But I cannot find a polite reason to refuse.

    My manners overrule my better judgement.
    """

    captain """
    Very well.

    Lead on, Mr Moody.

    I shall be right behind you.
    """

    $ play_music('danger', 2)

    """
    I follow him up the track.

    He walks easily, his rifle slung over his shoulder.

    Thirty yards from the clearing, the cover thickens.

    The voices from the luncheon fall away.

    He stops, turns, and lifts the rifle from his shoulder.

    Not to show me.

    To hold.
    """

    broken """
    That is quite far enough, I think, Captain.
    """

    """
    His gun is now pointing directly at my chest.

    My own rifle hangs uselessly at my side.

    There is a yard too many between us for me to raise it in time.
    """
    
    captain """
    Mr Moody.

    What is the meaning of this?
    """

    broken """
    You see, Captain, I found a piece of paper upon my bed yesterday.

    An old army order, written in the autumn of 1917. A transfer.

    Until then, the officer named upon it had held the safest billet in France.

    Conducting officer to the war correspondents, minding the gentlemen of the press well back of the guns, where no harm could come to him.

    This order pulled him off it and sent him up to the line.

    I assume you can guess his name: Thomas Moody.

    And at the foot of the order, the name of the man who put his signature to it.

    Captain S. Sinha, Staff Officer, General Headquarters.

    A stroke of your pen, and a man was taken from safety and marched into the worst of the war.

    Most who were sent up that season are in the Flanders mud yet.

    And the few who came back were not much luckier.

    They go through life as living monsters, hiding behind a mask such as this.
    """

    """
    He taps the porcelain of his mask with two gloved fingers.
    """

    """
    My mouth is dry.

    I have signed a great many papers in my time.

    Transfers, requisitions, routine dispatches.

    Most of them I could not recall if my life depended upon it.

    It is true that by that autumn, they were combing the soft billets for officers to throw into the thick of battle.

    Yet, that was never my job.
    """

    captain """
    You are mistaken, Mr Moody.

    I only ever signed what was laid before me, drafted by other hands.

    I never chose a single name, least of all his.
    """

    broken """
    Ah! How convenient for you, Captain.

    But I have no reason to believe you, in any case.

    Especially since I am now sure that you are not the war hero you claim.

    It was obvious today, when you could not even shoot a bird right under your nose.

    Yet yesterday you were entertaining everyone with tales of Burma and the Boxers, as though you had fought in them yourself.

    You are a fraud, that is clear enough.

    And maybe somebody is using me to hurt you.

    But I am very happy to oblige.
    """

    """
    He does not lower the rifle.

    His gaze is resolute, heavy with hatred.
    """

    captain """
    Please, Mr Moody, consider what is at stake here.

    Someone here is manufacturing all of this.

    They were likely hoping for precisely this to happen.

    You are being used to their end.

    And you are no safer than I am.
    """

    broken """
    How very considerate of you, Captain.

    But I can quite look after myself, I assure you.
    """

    captain """
    Thomas. Please.

    It is all a mistake.
    """

    broken """
    You will not sway me by using that name.

    You will only anger me the more.
    """

    captain """
    What do you mean?
    """

    broken """
    Well, I suppose there is no reason to hide it anymore.

    Thomas was the name of someone very dear to me.

    I would call him Tom, and he would call me Archie.

    But that is over now.

    All because of you.
    """

    $ broken_details.description_hidden.unlock('lie_name')

    """
    Before I can make sense of what he is saying, he levels the rifle at my head.

    I raise my hands to protect myself.
    """

    broken """
    Ah! Further proof you never saw battle, Captain.

    Well.

    This is as close as it gets.
    """

    play sound gun

    $ stop_music(1)

    pause 1.0

    jump captain_ending_shot_in_woods