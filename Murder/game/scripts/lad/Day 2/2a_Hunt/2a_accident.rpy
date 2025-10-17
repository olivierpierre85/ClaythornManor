label lad_day2_hunt_accident:

    $ change_room("forest")
    
    call change_time(12,00, 'Hunt', 'Saturday')

    $ play_music('chill')

    $ lad_details.important_choices.unlock('hunt_doctor_drunk')

    """
    Despite the risks, I decided to follow Doctor Baldwin and Samuel Manning.

    At least this way, I probably won't be the one embarrassing myself.

    We walked for a while without encountering anything.
    
    Then, we decided to stop for luncheon.

    The four of us sat down in a clearing, sharing a small picnic.

    Mr Manning is silent, busy drinking from a pocket flask.

    He looks serious, even nervous.

    As per usual, the footman doesn't say a word.

    That means the doctor and I are the only ones talking.
    """
    
    doctor """
    So, Mr Harring, how are you finding it here?

    It's a lovely place they have, isn't it?
    """

    lad """
    Certainly. It's a refreshing change of scenery for me.

    I don't often get to see nature like this.
    """

    doctor """
    Ah, so you're a city chap. 
    
    London?
    """

    lad """
    Birmingham. I was born and raised there.
    """

    $ lad_details.description_hidden.unlock('origin') 

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
    Alright, if everyone's ready, we can continue.

    Hopefully, we'll have better luck this time.
    """

    pause 2.0

    """
    For a while, we didn't. 
    
    But then, I spotted something that looked like a rabbit in the distance.

    Doctor Baldwin was ahead of me and didn't notice.

    I point out my prey to the footman, and he nods in approval.

    So, I get into an aiming position.

    But as soon as I do, Samuel Manning, who was behind me, sees what's happening.
    """

    call common_day2_hunt_accident_death

    """
    He coughs up blood.

    And then, silence.
    """

    pause 2.0

    $ doctor_details.description_hidden.unlock('fraud')

    """
    After a while, the footman returns with the others.

    By the time they get here, it's too late.

    Doctor Baldwin has bled out, and he is lying lifeless in the forest.
    """

    pause 2.0

    $ stop_music()

    return

