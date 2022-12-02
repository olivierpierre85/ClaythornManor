label lad_day2_hunt_accident:

    scene forest
    call change_time(12,00, 'Hunt', 'Saturday')

    $ play_music('chill')

    """
    Despite the risks, I decided to follow the doctor Baldwin and Samuel Manning.

    At least, this way I probably won't be the one embarrassing myself.

    We walked a while without encountering anything. 
    
    Then we decided to stop for luncheon.

    The four of us sat down in a clearing where we are sharing a small picnic.

    Mister Manning is silent, busy drinking from a pocket flask.

    He looks serious, even nervous.

    As per usual, the footman is doesn't say a word.

    That means the doctor and I are the only ones to talk.
    """
    
    doctor """
    So Mister Harring, how do you like it here ?

    It's a nice place they have there, don't they ?
    """

    lad """
    That's for certain. It's a nice change of scenery for me.

    I usually don't see nature very often.
    """

    doctor """
    Oh, you're a city chap then. 
    
    London ?
    """

    lad """
    Yes, I've been born and raised there.
    """

    $ lad_details.add_knowledge('background') 

    """
    But I don't really want to talk about that.

    Let's change the subject.
    """

    $ time_left = 30
    call doctor_generic

    call change_time(12,30)

    """
    Our lunch is coming to an end.
    """

    footman """
    Alright, if you are all set. We can go again.

    Hopefully we'll be luckier this time.
    """

    pause 2.0

    """
    For a while we weren't. 
    
    But then I spotted something looking like a rabbit afar.

    Daniel Baldwin was ahead of me and didn't see it.

    I point at my prey to the footman and he nods in approval.

    So I put the gun on aiming position.

    But as soon as I do it. Samuel Manning, who was behind me, realizes what's happening.
    """

    drunk """
    Oh, a rabbit !
    """

    """
    He  cocks his gun, shaking a little.

    Then fires it.
    """

    play sound gun

    # TODO stop music
    pause 2.0

    """
    He missed by far. 
    
    And it's too late for me to try again, the rabbit has ran away now.

    I am a bit pissed but then I hear a cry.
    """

    play music [ danger_01, scary_01]

    # play sound dying_in_pain TODO better sound

    """
    I turn around and see the doctor lying down in agony.
    """

    doctor """
    Argghhhh....
    """

    footman """
    Sir, sir are you okay...
    """

    """
    I watch in silence the scene of the footman trying to help him.

    I start to shout for help.
    """

    lad """
    HELP !!!

    Someone has been shot ! 
    """

    # TODO develop arrival of others
    """
    In the distance I hear the other group responding.

    By the time they reached us, it is too late.

    Daniel Baldwin has bled to death and is lying lifeless in the forest.
    """

    pause 2.0

    return

