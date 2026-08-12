
# Generic Broken Dialogs.
# Accessible from :
#                   - Doctor (Friday tea room, the plain labels below)
#                   - The Host (Friday dinner, via the _host variants below)
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


# ---------------------------------------------------------------------------
# HOST (Lady Claythorn) variants
# Moody is seated on her right at the Friday dinner, and he is the one man at
# that table who was raised below stairs. Every answer he gives her is also a
# reminder that he can read this house better than she can.
# She cannot ask a guest why he was invited - she is supposed to have invited
# him - so that question is dressed up as a hostess asking for the tale itself.
# ---------------------------------------------------------------------------

label broken_generic_background_host:

    broken """
    There is very little to tell, I am afraid.

    I soldiered for twenty years, and there has been a pension in Liverpool since.
    """

    host """
    And before that?
    """

    broken """
    Before that I was in service, my lady.

    Boot boy, then footman, in a house not unlike this one. Then I enlisted.
    """

    $ broken_details.description_hidden.unlock('job')

    $ broken_details.description_hidden.unlock('city')

    $ broken_details.description_hidden.unlock('background')

    """
    Well.

    That explains a great deal.

    He has stood at the wall through a hundred dinners exactly like this one, and there is not a thing I do at this table that he has not watched a real one do first.

    Of all the people to seat on my right.
    """

    host """
    Then you must tell me if my staff go wrong. You will see it long before I do.
    """

    broken """
    They have gone wrong twice already.

    But since you are good enough to ask, my lady, I shall say nothing about either.
    """

    """
    He says it lightly, as a joke against my footmen.

    I laugh, because it is expected, and because the alternative is to ask him which two things, and I cannot possibly ask him which two things.
    """

    return


label broken_generic_heroic_act_host:

    """
    I know what those letters said. I do not know what any of them believe they said.
    """

    host """
    I should like to hear it from you rather than off a sheet of paper, Mr Moody.

    In your own words. What is it that brought you to my table?
    """

    call broken_generic_heroic_act_intro

    host """
    A different reason.
    """

    broken """
    Only that a man with a face like mine is remembered for what he did, my lady, and a man with an ordinary one is not.

    There were braver things done that week than anything I managed. Nobody has written to those fellows.
    """

    $ broken_details.description_hidden.unlock('heroic_act')

    """
    He has just told me he does not believe the reason he was given.

    And he has told it to the woman who is supposed to have written it, in the mildest voice in the room, and then gone back to his plate.

    I have worked with actors who feed you a line to see what you will do with it.

    That is what that was.
    """

    return


label broken_generic_manor_host:

    broken """
    It is a decent-sized house, my lady.

    Built for a landowner with money rather than for a title, if you will forgive me. It is not large enough for a Duke or an Earl.

    Squires, I should have guessed. Baronets at the most.
    """

    host """
    You are very nearly rude, Mr Moody.
    """

    broken """
    I am very nearly right, though. There is a third possibility, of course.

    Industrialists who bought the land and had the word "Lady" painted on the gate afterwards.

    That would be quite outrageous, if that were the case.
    """

    """
    Squires. Baronets. Or a name somebody bought.

    I do not know which of those I am supposed to be. Nobody has ever told me, because nobody thought a woman playing a part would need it.
    """

    host """
    And where does an old soldier learn to price a house from the soup?
    """

    broken """
    In service, my lady. I was raised in one of these.

    One learns to read a place the way other men read a newspaper.
    """

    $ broken_details.description_hidden.unlock('background')

    """
    He was in service. In a house of this sort, at a table of this sort, run by a woman of this sort.

    He is not making conversation. He is telling me he can read this house, and watching to see whether that troubles me.
    """

    return


label broken_generic_age_host:

    call broken_generic_age_intro

    host """
    Forgive me. That was a rude question, and I asked it anyway.
    """

    broken """
    It was an honest one. I would sooner have those.
    """

    $ broken_details.description_hidden.unlock('age')

    """
    Forty-seven, and the half of the face I can see is a great deal older than that.

    Whatever was done to him was done to a young man.
    """

    return


label broken_generic_room_host:

    call broken_generic_room_intro

    host """
    Nobody knows much about him, Mr Moody. That is rather the point of him.
    """

    broken """
    Then I am in excellent company, my lady.
    """

    """
    And there I sit, having asked a guest which of my own bedrooms I put him in.

    He answered as though it were the most natural question in the world.

    A man who lets a mistake go by as smoothly as that has noticed it. They always have.
    """

    return


label broken_generic_other_guests_friday_dinner_host:

    broken """
    A remarkable table, my lady.

    A doctor, a nurse, a soldier, a barrister, a young man who has not taken his eyes off the silver, and a lady in a good deal of jewellery who I am told reads palms.

    Not one of them had met another before this afternoon.
    """

    host """
    That is rather the charm of it.
    """

    broken """
    Of course.

    Though I confess I keep looking for the thread that joins them, and I cannot find it.

    You would know it better than anybody. What made you settle on these seven?
    """

    """
    Nothing made me settle on anything. I was handed a list of names and told to learn them by Friday.
    """

    host """
    Merit, Mr Moody. Nothing half so interesting as a thread.
    """

    broken """
    A pity. A thread would have made the better story.
    """

    """
    That is the same question he asked me over the fish, in a different coat.

    He has counted the table, and he has worked out that not one of us belongs at it.
    """

    return

