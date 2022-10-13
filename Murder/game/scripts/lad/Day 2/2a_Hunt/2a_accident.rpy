label lad_day2_hunt_accident:

    scene forest
    call change_time(12,00)

    """
    Despite the risks, I decided to follow the doctor and the drunk fellow.

    At least, this way I probably won't be the one embarrassing myself.

    We walked a while without encountering anything. 
    
    Then we decided to stop for luncheon.

    The four of us sat down in a clearing where we are sharing a small picnic.

    The drunk is very silent, and busy drinking from a pocket flask.

    He looks serious, even nervous.

    As per usual, the footman is silent.

    That means the doctor and I are the only to talk.
    """

    if not 'doctor' in current_character.has_met:
        # TODO introduction in generic ???
        doctor "I am sorry we actually havent been formaly introduce...TODO"

    
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

    Hopefully we'll be more lucky this time.
    """


    # TODO play music suspensful_01 fadein 5.0
    """
    And for a while we weren't. 
    
    But then I spotted something looking like a rabbit afar.

    The doctor was ahead of me and didn't see it.

    I point at my prey to the footman and he nods in approval.

    So I put the gun on aiming position.

    But as soon as I do it. The drunk who was behind realize what's happening.
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
    I stop immediately
    """
    # Add cry sound.


    return

