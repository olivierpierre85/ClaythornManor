label lad_day2_hunt_noaccident:

    $ change_room("forest")
    
    call change_time(12,30, 'Hunt', 'Saturday')

    $ lad_details.important_choices.unlock('hunt_captain_host')

    """
    Following our hostess seemed to be the safest course of action.

    The only problem is that both she and Sushil Sinha are completely in their element.

    While I clearly am not.

    They've already shot a few rabbits and a pheasant.

    Out of pity, they even tried to help me shoot a deer that crossed my path.

    However, I merely managed to scare the animal away.
    """

    captain """
    Tough luck, Mr. Harring. I'm sure you'll get the next one.
    """

    lad """
    Thank you, but I don't think this is for me. I believe I missed it by several feet.
    """

    captain """
    Don't fret, you just lack practice.

    Then again, it might be for the best. You wouldn't have wanted to serve in the war.

    It was truly brutal. Nothing like the previous conflicts I participated in.
    """

    lad """
    Have you fought in many wars?
    """

    captain """
    Indeed, I began my career in India and encountered my first battle during the war with Burma.

    I was also involved in the Chinese rebellion. Then ...
    """
    
    $ captain_details.description_hidden.unlock('wars')

    """
    Our conversation about the wars seemed to make Lady Claythorn uneasy, as she suddenly interrupts us.
    """

    host """
    Well, I believe it's time for luncheon. How would you feel about settling here for our picnic?
    """

    captain """
    Yes, it's a perfect spot.
    """

    """
    We began setting up the picnic.

    However, before we could start eating, we heard a gunshot nearby.
    """

    $ stop_music(3)

    play sound gun

    captain """
    Ah, it sounds like the others have caught something. And they're not far from here.
    """

    """
    But soon after the gunshot, another sound followed.

    A desperate cry for help.

    The captain and I heard it, immediately jumping to our feet.

    We rushed in the direction of the cry.
    """

    call wait_screen_transition()

    $ play_music('danger')

    """
    Soon, we came upon the others.

    Doctor Baldwin is on the ground.

    Standing beside him is Samuel Manning, visibly shaken.
    """

    drunk """
    Oh my God, oh my God.

    It was an accident.

    I can't believe this happened.
    """

    """
    Captain Sinha grabbed him.
    """

    captain """
    What have you done, fool?
    """

    drunk """
    I shot at a rabbit, but missed.

    I didn't mean to hit him.

    I didn't...
    """

    """
    We look down at Daniel Baldwin.

    Next to him are empty vials and a syringe.
    """

    footman """
    He asked me to give him that.

    Then he nodded off right after.
    """

    """
    Captain Sinha sits next to the victim to check his pulse.
    """

    captain """
    It is too late.

    His heart has stopped.

    He is dead.
    """

    $ stop_music()

    pause 2.0

    $ lad_details.saved_variables["day2_saw_accident"] = True

    return