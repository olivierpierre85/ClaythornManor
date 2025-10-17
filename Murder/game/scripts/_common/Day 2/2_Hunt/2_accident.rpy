label common_day2_hunt_accident_footman_1:

    footman """
    Alright, if everyone's ready, we can continue.

    Hopefully, we'll have better luck this time.
    """

    return

label common_day2_hunt_accident_death:

    $ stop_music(1)

    drunk """
    Oh, a rabbit!
    """

    if current_character.text_id == "lad":
        
        """
        He cocks his gun, shaking slightly.

        Then, he fires.
        """

    play sound gun

    $ play_music('danger')

    pause 2.0

    if current_character.text_id == "lad":
        
        """
        He missed by a mile. 
        
        By the time I could try again, the rabbit had run off.

        I'm frustrated, but then I hear a cry.
        """

    elif current_character.text_id == "doctor":
        
        """
        A sharp pain irridiates in my stomach.

        I fall on the ground.

        Bloody hell, the fool shot me.
        """


    # play sound dying_in_pain TODO better sound

    if current_character.text_id == "lad":

        """
        I turn around and see Doctor Baldwin crying in pain on the ground.
        """

    doctor """
    Ughhh...
    """

    footman """
    Sir, are you alright?
    """

    if current_character.text_id == "lad":

        """
        I start to call for help.
        """

    lad """
    Help! Help!!!

    Someone's been shot!
    """

    if current_character.text_id == "lad":

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

    if current_character.text_id == "lad":
    
        """
        I ignore Samuel Manning's pleas and sit beside the injured man.

        I don't know how to help.

        But Doctor Baldwin does.
        """

    doctor """
    Quickly, remove my shirt.

    I need to see where the bullet entered.
    """

    if current_character.text_id == "lad":
        
        """
        In my panic, I tear off his shirt, revealing his blood-soaked abdomen.

        I notice a small entry wound on his right side.

        It doesn't look too bad.
        """

    lad """
    I've found the wound.

    Should I apply pressure?
    """

    if current_character.text_id == "lad":

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

    if current_character.text_id == "lad":
        
        """
        He casts a venomous glare at Samuel Manning but says nothing.
        """

    lad """
    Is there anything I can do?
    """

    doctor """
    Yes, hand me my bag.
    """

    if current_character.text_id == "lad":
        
        """
        I search around and locate his medical bag.

        I pass it to him.
        """

    doctor """
    Well, there's nothing more to do now.
    """

    if current_character.text_id == "lad":
        
        """
        He takes out a small vial and a syringe.

        He fills the syringe in. Then, without hesitation, he injects himself.

        Then he does it a second time.

        And a third.
        """

    doctor """
    Ahhhh, that's better.
    """

    if current_character.text_id == "lad":
        
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

    if current_character.text_id == "lad":

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




    return