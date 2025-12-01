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
        He missed by a long way. 
        
        By the time I could try again, the rabbit had bolted.

        I'm frustrated, but then I hear a cry.
        """

    elif current_character.text_id == "doctor":
        
        """
        A sharp pain irradiates through my stomach.

        My legs give way and I fall to the ground.
        """

        if doctor_details.observations.is_unlocked('drunk_letter'):

            """
            I allowed myself a moment of distraction and he seized it.

            Bloody hell.
            """
        
        else:
            
            """
            Bloody hell, the fool has shot me.
            """

    if current_character.text_id == "lad":

        """
        I turn and see Doctor Baldwin crying out in pain on the ground.
        """

    doctor """
    Ughhh...
    """

    footman """
    Sir, are you all right?
    """

    if current_character.text_id == "lad":

        """
        I start to call for help.
        """

    lad """
    Help! Help!

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
        I ignore Samuel Manning entirely and crouch beside the doctor.

        I have no idea how to help him.

        But he will know what to do.
        """

    elif current_character.text_id == "doctor":

        if doctor_details.observations.is_unlocked('drunk_letter'):

            """
            He avoids my gaze, feigning remorse.

            Yet I can see the truth in his eyes.

            He is delighted.

            I was a fool to let him anywhere near me.
            """

        else:

            """
            He stands there trembling, shame washing over his face.

            There is something else in his expression, yet I cannot place it.
            """

        """
        But there is no time for that now.

        I must act quickly.

        I call out to Ted Harring.
        """

    doctor """
    Quickly, remove my shirt.

    I need to see where the bullet went in.
    """

    if current_character.text_id == "lad":
        
        """
        My hands shake as I tear open his shirt.

        Blood has soaked through the fabric.

        I see a small hole on his right side.

        At first glance, it does not appear too dreadful.
        """

    elif current_character.text_id == "doctor":

        """
        The lad helps me remove my shirt as best he can, though he is shaking like a leaf.
        """

    lad """
    I found the wound.

    Do you want me to press on it?
    """

    if current_character.text_id == "lad":

        """
        The doctor inspects it himself.

        A look of dread washes over his face.
        """

    elif current_character.text_id == "doctor":

        """
        I look down at the small, neat hole in my abdomen.

        Dark blood oozes slowly, thick and heavy.

        The liver.

        Of all the places it could strike, it had to be the liver.

        Damn it.
        """

    doctor """
    There is no need.

    The bullet has struck my liver.
    """

    lad """
    But it's such a tiny hole.

    Surely there must be something we can do?
    """

    doctor """
    No.

    Liver wounds are fatal.

    It is already far too late.
    """

    if current_character.text_id == "lad":
        
        """
        He looks towards Samuel Manning with pure hatred, yet says nothing aloud.
        """
    
    elif current_character.text_id == "doctor":
            
        """
        Filled with anger, I turn my eyes upon the man who has shot me.
        """

        """
        But it doesn't matter now.

        Ted Harring speaks again.
        """

    lad """
    Tell me what I can do.
    """

    doctor """
    Hand me my bag.
    """

    if current_character.text_id == "lad":
        
        """
        I look round until I spot the leather bag.

        I grab it and pass it to him.
        """

    elif current_character.text_id == "doctor":

        """
        He fumbles about, then places my bag into my hands.
        """

    doctor """
    Well, there is very little to be done now.
    """

    if current_character.text_id == "lad":
        
        """
        He takes a small vial from his bag.

        Without a word, he pulls the cork and drinks it.

        Then another.

        And a third.
        """

    elif current_character.text_id == "doctor":

        """
        Time for one final indulgence.

        I take a few vials from my bag and drink them down as swiftly as I can manage.
        """

    doctor """
    Ahh, that is better.
    """

    if current_character.text_id == "lad":
        
        """
        This is all happening far too fast.

        I can scarcely keep up.
        """

    lad """
    What should I do?
    """

    doctor """
    Nothing.

    I shall lose consciousness before long.

    I doubt I shall wake again.
    """

    if current_character.text_id == "lad":

        """
        I cannot speak.

        My throat is tight.
        """

    doctor """
    Perhaps it is no more than I deserve.
    """

    lad """
    Don't say that.

    Your patients would...
    """

    doctor """
    My patients will not care whether I live or die.

    I was harsh with them.

    I took advantage of them.

    I stole the medicines they needed for myself.

    I do not disserve sympathy.

    I should never have come here.

    Yet, in a strange way, this feels like justice.
    """

    return
