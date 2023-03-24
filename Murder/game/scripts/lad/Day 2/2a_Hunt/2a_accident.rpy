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

    As per usual, the footman doesn't say a word.

    That means the doctor and I are the only ones to talk.
    """
    
    doctor """
    So Mister Harring, how do you like it here?

    It's a nice place they have there, don't they?
    """

    lad """
    That's for certain. It's a nice change of scenery for me.

    I don't often get to see nature like this.
    """

    doctor """
    Oh, you're a city chap then. 
    
    London?
    """

    lad """
    Birmingham. I was born and raised there.
    """

    $ lad_details.unlock_knowledge('background') 

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

    $ stop_music(1)

    pause 2.0

    """
    He missed by far. 
    
    And it's too late for me to try again, the rabbit has ran away now.

    I am a bit pissed but then I hear a cry.
    """

    $ play_music('danger')

    # play sound dying_in_pain TODO better sound

    """
    I turn around and spot the doctor in pain on the ground..
    """

    doctor """
    Ughhh....
    """

    footman """
    Sir, sir, are you alright?
    """

    """
    I begin to call for help.
    """

    lad """
    HELP !!!

    Somebody's been shot!
    """

    """
    I face the footman.
    """

    lad """
    Hurry, go get the others. We need their help.
    """

    footman """
    Yes, of course sir.
    """

    drunk """
    Oh no, oh no what have I done?!

    It was an accident.

    An accident.

    I didn't intend for this. Please believe me.
    """


    """
    I ignore Samuel Manning's babbling and sit beside the injured man.

    I am at a loss for how to help.

    But, naturally, Daniel Baldwin knows.
    """

    doctor """
    Quick, remove my shirt.

    I have to see where the bullet entered.
    """

    """
    In a panic, I rip off his shirt, exposing his blood-soaked belly.

    I notice a small puncture on his right side.

    It doesn't seem too bad.
    """

    lad """
    I've found the wound.

    Do you want me to apply pressure?
    """

    """
    The doctor examines it himself.

    Fear washes over his face.
    """

    doctor """
    There's no need.

    The bullet pierced my liver.
    """

    lad """
    But it's just a tiny hole, maybe we can...
    """

    doctor """
    No, we can't. Liver wounds aren't survivable.

    It's already too late.
    """

    """
    He shoots a venomous glare at Samuel Manning but remains silent.
    """

    lad """
    Can I do anything?
    """

    doctor """
    Yes, hand me my bag.
    """

    """
    I search the area and locate his medical bag.

    I hand it to him.
    """

    doctor """
    Well, there's nothing more to do now.
    """

    """
    He takes out a small vial and a syringe.

    He fills the syringe in. Then, without hesitation, he injects himself.
    """

    doctor """
    That's better.

    I'll lose consciousness soon.

    And I likely won't wake up.
    """

    """
    What! Everything is happening too fast.
    """

    lad """
    What can I do?

    Do you have a message for someone?
    """

    doctor """
    No, there's no one.

    It doesn't matter.

    I never did anything worth anyone's attention.

    I probably deserve this.
    """

    lad """
    Don't say that.

    I am sure your patients would be...
    """

    doctor """
    My patients won't care if I live or die.

    I was awful to them.

    I exploited them to get drugs.

    I definitely don't deserve an award.

    I never should have come here.

    But I guess in a way it's a form of justice.
    """

    """
    He coughs up some blood.

    And then he goes silent.
    """

    pause 1.0

    $ doctor_details.unlock_knowledge('fraud')

    """
    After a while, the footman brings the others over.

    By the time they arrive, it's too late.

    Daniel Baldwin has bled out and lies lifeless in the forest.
    """

    pause 2.0

    $ stop_music()

    return

