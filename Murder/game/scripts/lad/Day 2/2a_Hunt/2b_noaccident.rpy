label lad_day2_hunt_noaccident:

    scene forest
    call change_time(12,30, 'Hunt', 'Saturday')

    """
    Following our hostess was probably the safest course.

    The only problem is that she and Sushil Sinha are both in their element.

    While I am clearly not.

    They already shot a few rabbits and a pheasant.

    Out of pity, they also try to help me shoot a beautiful deer that came on to my path.

    But their guidance was unsuccessful. I only managed to scare the animal away.
    """

    captain """
    Poor luck Mr Harring. I am sure you'll get the next one.
    """

    lad """
    Thank you, but I don't think I am made for this. I think I missed it by a couple of feet.
    """

    captain """
    Don't worry, it's just that you lack the practice.

    But it's just as well. You wouldn't want to have served in the war.

    It's was the bloodiest thing. Nothing compare to the previous conflicts I was in.
    """

    lad """
    You fought in many other wars?
    """

    captain """
    Of course, I started my career in India and fought my first battle during the war with Burma.

    I've also been involved in the Chinese rebellion. Then ...
    """
    # TODO little difference if you have listened to the speech

    $ captain_details.add_knowledge('wars')

    """
    Those talks about war must have made Lady Claythorn uneasy, because she suddenly interrupts us.
    """

    host """
    Well, I think it's time for luncheon. How do you feel about settling here for our picnic ?
    """

    captain """
    Yes it's a perfect spot.
    """

    """
    So we started preparing the picnic.

    But we didn't have time to eat, that we heard a shot not far from us.
    """

    stop music fadeout 3.0

    play sound gun

    captain """
    Ah, the others must have caught something. And they are not far from us.
    """

    """
    But the shot was followed soon by something else.

    A cry for help.

    The captain heard it too, and jump on his feet.

    I stood up and we ran in the direction of the cry.
    """

    play music danger_01 fadein 5.0

    """
    We quickly reached the others.

    Doctor Baldwin was lying down on the floor.

    Next to him was Samuel Manning, shaking.
    """

    drunk """
    Oh my god, oh my god.

    It was an accident.

    I don't know how it could have happened.
    """

    """
    We examined the doctor.

    It is too late.

    He has bled to death.
    """

    stop music fadeout 5.0

    pause 2.0

    $ lad_day2_saw_accident = True

    return