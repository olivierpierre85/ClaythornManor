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

    Mister Manning is silent, busy drinking from a pocket flask.

    He looks serious, even nervous.

    As per usual, the footman doesn't say a word.

    That means the doctor and I are the only ones talking.
    """
    
    doctor """
    So, Mister Harring, how are you finding it here?

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

    $ lad_details.description_hidden.unlock('background') 

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

    drunk """
    Oh, a rabbit!
    """

    """
    He cocks his gun, shaking slightly.

    Then, he fires.
    """

    play sound gun

    $ stop_music(1)

    pause 2.0

    """
    He missed by a mile. 
    
    By the time I could try again, the rabbit had run off.

    I'm frustrated, but then I hear a cry.
    """

    $ play_music('danger')

    # play sound dying_in_pain TODO better sound

    """
    I turn around and see Doctor Baldwin crying in pain on the ground.
    """

    doctor """
    Ughhh...
    """

    footman """
    Sir, are you alright?
    """

    """
    I start to call for help.
    """

    lad """
    Help! Help!!!

    Someone's been shot!
    """

    """
    I turn to the footman.
    """

    lad """
    Hurry, fetch the others.
    """

    footman """
    Yes, of course, sir.
    """

    drunk """
    Oh no, what have I done?!

    It was an accident.

    I never intended this. Please believe me.
    """

    """
    I ignore Samuel Manning's pleas and sit beside the injured man.

    I don't know how to help.

    But Doctor Baldwin does.
    """

    doctor """
    Quickly, remove my shirt.

    I need to see where the bullet entered.
    """

    """
    In my panic, I tear off his shirt, revealing his blood-soaked abdomen.

    I notice a small entry wound on his right side.

    It doesn't look too bad.
    """

    lad """
    I've found the wound.

    Should I apply pressure?
    """

    """
    The doctor inspects it himself.

    A look of dread washes over his face.
    """

    doctor """
    There's no need.

    The bullet has hit my liver.
    """

    lad """
    But it's just a tiny hole. Maybe we can...
    """

    doctor """
    No, we can't. Liver wounds are fatal.

    It's already too late.
    """

    """
    He casts a venomous glare at Samuel Manning but says nothing.
    """

    lad """
    Is there anything I can do?
    """

    doctor """
    Yes, hand me my bag.
    """

    """
    I search around and locate his medical bag.

    I pass it to him.
    """

    doctor """
    Well, there's nothing more to do now.
    """

    """
    He takes out a small vial and a syringe.

    He fills the syringe in. Then, without hesitation, he injects himself.

    Then he does it a second time.

    And a third.
    """

    doctor """
    Ahhhh, that's better.
    """

    """
    This is all happening too quickly.
    """

    lad """
    What can I do?
    """

    doctor """
    There is nothing to be done.

    I'll lose consciousness soon.

    And likely, I won't awaken again.
    """

    """
    I am speechless.
    """

    doctor """
    Perhaps I deserve this.
    """

    lad """
    Don't say that.

    Your patients would...
    """

    doctor """
    My patients won't care if I live or die.

    I was cruel to them.

    I took advantage of them, took the drugs they needed for myself.

    I certainly don't merit sympathy.

    I shouldn't have come here.

    Yet, in a way, this feels like justice.
    """

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

