
# Generic Broken Dialogs.
# Accessible from :
#                   - Doctor (Friday tea room, the plain labels below)
label broken_generic:

    # Reset if previous early exit
    $ current_character.saved_variables["broken_generic_menu"].early_exit = False

    call run_menu(current_character.saved_variables["broken_generic_menu"])
    
    return


label broken_generic_doctor_improprieties:

    # The possibilities that the doctor can be a bit rude

    if doctor_details.saved_variables['broken_offended'] == 0:

        """
        Well, I was not very polite here. 
        
        I should watch what I am saying, shouldn't I?
        """

    elif doctor_details.saved_variables['broken_offended'] == 1:

        """
        Blast it, I did it again. I really ought to be more careful.
        """

    elif doctor_details.saved_variables['broken_offended'] == 2:

        """
        I cannot believe I was rude again.

        I must sound like an absolute tosser to him now.
        """

        $ doctor_details.threads.unlock('broken_offended')

    $ doctor_details.saved_variables['broken_offended'] += 1
    
    return


label broken_generic_other_guests_friday:

    broken """
    The other guests? You mean Miss Marsh, I presume?
    """

    doctor """
    Well, yes, of course. She is the only one we have met so far.
    """

    broken """
    Right.

    I am not sure. She was very quiet during our journey.

    But being alone with men around her must have made her uneasy.
    """

    call run_menu( TimedMenu("broken_generic_other_guests_friday_offense", [
        TimedMenuChoice("Yes, it must be that", 'broken_generic_other_guests_friday_not_offended', 10, early_exit=True),
        TimedMenuChoice("I can think of another reason she was uneasy", 'broken_generic_other_guests_friday_offended', 10, early_exit=True),
        ])
    )

    return


label broken_generic_other_guests_friday_offended:

    doctor """
    Well, or it might be your... your...
    """

    broken """
    My what?
    """

    doctor """
    No, nothing.
    """

    """
    He may not say anything, but he understands very well what I meant.
    """

    call broken_generic_doctor_improprieties

    return


label broken_generic_other_guests_friday_not_offended:

    broken """
    Of course, what else could that be.
    """

    return


label broken_generic_weather_friday:

    broken """
    It is not the ideal weather, but there is no reason to lose sleep over it, is there?
    """

    return


label broken_generic_background:

    broken """
    There is not much to say, I am afraid.

    The Army was my trade, and the Army had done with me in 'seventeen.

    I have kept no other since. There is a pension, and it is enough.
    """

    $ broken_details.description_hidden.unlock('job')

    call run_menu( TimedMenu("broken_generic_background_offense", [
        TimedMenuChoice("And you have not worked since?", 'broken_generic_background_offended_1', 0, early_exit=True, next_menu="broken_generic_background_offended_1" ),
        TimedMenuChoice("That's a very noble profession", 'broken_generic_background_not_offended', 10, early_exit=True),
        ])
    )

    return

label broken_generic_background_not_offended:

    broken """
    Thank you.

    It was not saving lives, but I was good at it.
    """

    return


label broken_generic_background_offended_1:

    broken """
    Not since, no. I was a famous actor before, you understand.

    Sadly I can't do that anymore.
    """

    call run_menu( TimedMenu("broken_generic_background_offended_1", [
        TimedMenuChoice("Wait? Really?", 'broken_generic_background_offended_2', 10, early_exit=True),
        TimedMenuChoice("Just laugh and say nothing", 'generic_cancel', 10, early_exit=True),
        ])
    )

    return


label broken_generic_background_offended_2:

    broken """
    No, of course not.

    I was obviously joking.
    """

    """
    Then he gives me a weird look.
    """

    call broken_generic_doctor_improprieties

    return
    

label broken_generic_heroic_act_intro:

    broken """
    Well, I suppose it is related to what I did in the war.

    But there were a lot of heroic acts that happened at that time.

    I am not sure mine was particularly exceptional.

    I suppose I am here for a different reason.
    """

    return


label broken_generic_heroic_act:

    call broken_generic_heroic_act_intro

    call run_menu( TimedMenu("broken_generic_heroic_act_offended", [
        TimedMenuChoice("What do you mean?", 'broken_generic_heroic_act_offended', 20, early_exit=True),
        TimedMenuChoice("Nod, but don't engage", 'generic_cancel', 20, early_exit=True),
        ])
    )

    return


label broken_generic_heroic_act_offended:
    
    """
    He looks at me with a blank stare.
    """

    broken """
    Is it not obvious?

    My ... "condition" makes my actions more memorable than others'.

    But I really do not want to talk about it.
    """

    doctor """
    No, of course.
    """

    $ broken_details.description_hidden.unlock('heroic_act')

    call broken_generic_doctor_improprieties
    
    return


label broken_generic_manor:

    broken """
    It is a decent-sized house.

    Probably originally for a wealthy local landowner.

    Though it is not large enough for an important aristocrat like a Duke or an Earl.

    I do not know much about this Lady Claythorn, but her family are probably squires or baronets.

    Unless they are just wealthy industrialists and they added the "Lady" to lend some prestige to their name.

    That would be quite outrageous if that were the case.
    """

    doctor """
    Really? I would not have thought of that.

    Where did you learn all of this?
    """

    broken """
    Because I was raised in a house a bit like this one.

    I started as a bootboy when I was a wee lad, but quickly rose in rank to become a footman.

    Then I took the King's shilling, and everything changed.
    """

    $ broken_details.description_hidden.unlock('background')

    call run_menu( TimedMenu("broken_generic_manor_offense", [
        TimedMenuChoice("You were glad to be out of service, I imagine", 'broken_generic_manor_offended', 20, early_exit=True),
        TimedMenuChoice("The army suited you better, then", 'broken_generic_manor_not_offended', 20, early_exit=True),
        ])
    )

    return


label broken_generic_manor_offended:

    doctor """
    I understand. It must have seemed a small sort of life for a young man.

    Handing round the soup while other men did something with themselves.
    """

    broken """
    Not really.

    I do not think there is anything wrong with being a servant.

    I was good at it, and I liked it well enough.

    I even hoped to be a butler someday.

    And I had the one thing they cannot train into you.

    A footman has to be tall, you see.

    I am not sure why, but it is a matter of pride for them to have the tallest servants possible.

    It is all part of us being seen as part of the "image" of their property.

    So the post was mine for as long as I wanted it.

    But I found I wanted to be looked at rather less, and to see rather more.

    So I enlisted, and I stayed enlisted for twenty years.
    """

    doctor """
    I am sorry, I did not mean to offend you.
    """

    broken """
    It is all right.
    """

    call broken_generic_doctor_improprieties

    """
    In any case, I realise now he is the tallest man in the room.

    Only the footman seems to be about the same height as he is.
    """

    $ broken_details.description_hidden.unlock('tall') 

    return


label broken_generic_manor_not_offended:

    broken """
    It suited me for twenty years.

    Whether that is quite the same thing, I have never decided.
    """

    return


label broken_generic_age_intro:

    broken """
    47 years old.

    I know it is hard to guess, considering.
    """

    return


label broken_generic_age:

    call broken_generic_age_intro

    doctor """
    I am sorry, I did not want to imply anything.
    """

    broken """
    Do not worry about it.
    """
    
    $ broken_details.description_hidden.unlock('age') 

    call broken_generic_doctor_improprieties
    
    return


label broken_generic_room_intro:

    broken """
    My room is named "Richard the Third".

    I must admit I do not know much about him.
    """

    $ unlock_map('bedroom_broken')

    return


label broken_generic_room:

    call broken_generic_room_intro

    call run_menu( TimedMenu("broken_generic_room_offense", [
        TimedMenuChoice("Me neither", 'generic_cancel', 10, early_exit=True),
        TimedMenuChoice("I saw a Shakespeare's play about him", 'broken_generic_room_offended', 10, early_exit=True),
        ])
    )
    
    return


label broken_generic_room_offended:

    broken """
    Really? What did you learn about him?
    """

    doctor """
    From what I remember, Shakespeare paints him as a man twisted both in body and in soul. 

    The most impressive thing about the play was how the actor managed to convey Richard's deformity. 

    His crooked posture, the twisted arm, the limp — all brought vividly to life upon the stage. 

    It left no doubt in one's mind that he was meant to be both pitied and feared.
    """

    """
    I see Thomas Moody's gaze harden and quickly stop talking.

    I didn't realise who I was talking to.
    """

    call broken_generic_doctor_improprieties

    return
