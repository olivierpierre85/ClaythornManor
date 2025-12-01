label doctor_day2_evening_exploration:
    
    call change_time(21, 00)

    $ change_room("bedroom_doctor")

    """
    I now find myself faced with several courses of action.

    The most obvious would be to remain here in my room and wait for the morning.

    I could even move some furniture against the door to make certain no one can enter.

    Yet that, too, feels dangerous. There are other ways for someone to reach me.

    The alternative is to attempt to discover who wrote that note to Samuel Manning.

    That is the person I ought to fear.

    Everything points towards Lady Claythorn, yet I cannot be sure.

    If only I could trust at least one other person, I might ask for their assistance.

    It would be safer to investigate in company, but in whom ought I place my trust?

    It would be ideal to have someone implicitly trustworthy, like a judge.

    But everyone here appears suspicious to me.
    """

    if doctor_details.important_choices.is_unlocked('flirt'):

        """
        I might turn to Andrew. After the time we have spent together, I find it hard to picture him as a likely culprit.

        He is probably downstairs with the staff at present, unless he has already retired for the night.
        """

    if doctor_details.observations.is_unlocked('remember_nurse'):

        """
        By good fortune, I already know Nurse Rosalind Marsh. That acquaintance makes me more comfortable about approaching her.
        """
    
    if doctor_details.objects.is_unlocked('book_opium'):
        
        """
        To make matters worse, the symptoms of withdrawal are steadily increasing.

        My hands tremble, and I am sweating more than is reasonable.

        They will only grow worse as the night wears on, which will not be in my favour.
        """

    """
    I feel very much at a crossroads.

    What I decide to do now may mean the difference between life and death.

    So what shall it be?
    """

    $ time_left = 90
    call run_menu(doctor_details.saved_variables["day2_evening_map_menu"])

    return


label doctor_day2_evening_billiard_room:

    $ change_room('billiard_room')

    if not doctor_details.saved_variables["day2_evening_billiard_room_visited"]:

        $ doctor_details.saved_variables["day2_evening_billiard_room_visited"] = True

        """
        Just as I imagined, the room is almost deserted.

        I can see only Captain Sinha seated upon a sofa, and the butler standing discreetly in the corner.

        The bar is still available, but I promised myself to keep a clear head, so I should avoid it.
        """

        # TODO add interaction with the butler
        $ doctor_day2_evening_billiard_room_menu = TimedMenu("doctor_day2_evening_billiard_room_menu", [
            TimedMenuChoice('Talk to Sushil Sinha', 'doctor_day2_evening_billiard_room_captain'),
            TimedMenuChoice('Go to the bar for a drink', 'doctor_day2_evening_billiard_room_bar', 10),
            TimedMenuChoice('Leave the room', 'generic_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ doctor_day2_evening_billiard_room_menu.early_exit = False

        """
        I find myself once more in the billiard room.
        """

    call run_menu(doctor_day2_evening_billiard_room_menu)

    return


label doctor_day2_evening_billiard_room_bar:

    """
    In spite of knowing full well it is a mistake, my steps carry me straight to the bar.

    Before I have quite registered it, I am already pouring myself a glass of sherry.

    The moment I realise what I have done, a wave of shame washes over me.

    Yet now that the glass is in my hand, I cannot simply set it aside.

    I might as well drink it.

    But this will be the last one.
    """

    if doctor_details.objects.is_unlocked('book_opium'):

        """
        At last, I have a chance to free myself from opium entirely.

        I shouldn't exchange one addiction for another.
        """

    return


label doctor_day2_evening_billiard_room_captain:


    """
    I go to Captain Sinha.

    He notices me and puts his book on the table.
    """

    captain """
    Doctor Baldwin, it's nice to see you. 
    
    I fear that most of the other guests are too afraid to get out of their room.
    """

    doctor """
    Really? What should they be afraid of?
    """

    captain """
    Well, nothing of course.

    It's obvious to me that the two sad death of the weekend were both tragic, but unfortunate event.
    """

    doctor """
    But you believe not everyone agrees with you.

    So they are scared, but of what exactly?

    Oh I understand now.

    They are scared of me of course.

    But they acted as if they understood that what happened during the hunt was just an accident.
    """

    captain """
    Oh don't feel too bad Doctor. I am sure they still think that, but they're just being prudent.

    They are not in the habit of being this close to death like you and I.
    """

    doctor """
    Right.
    """

    captain """
    But is there something you wanted to tell me doctor?
    """

    call run_menu(
        TimedMenu("doctor_day2_evening_billiard_room_captain", [
            TimedMenuChoice("Tell him about the letter", 'doctor_day2_evening_billiard_room_captain_letter'),
            TimedMenuChoice("Tell him about Thomas Moody's face", 'doctor_day2_evening_billiard_room_captain_mask', 30 ,condition="doctor_details.observations.is_unlocked('broken_unmasked') and all_menus['doctor_day2_evening_billiard_room_captain'].choices[0].hidden"),
            TimedMenuChoice("Find someone else to confide in", 'doctor_day2_evening_billiard_room_captain_avoid', keep_alive=True, early_exit = True),
        ])
    )

    return


label doctor_day2_evening_billiard_room_captain_letter:

    doctor """
    There is something I need to share with you.

    I haven't been totally honest about what happened during the hunt.

    ...
    """

    captain """
    I admit this is weird, but you must forgive me, it's not enough.
    """

    """
    He is not trusting me.

    I understand, in the end, I am the one who killed Samuel Manning.

    He is not there to defend himself.

    If I really want to convince Sushil Sinha, I need more evidence that something not normal is happening here.
    """

    return

label doctor_day2_evening_billiard_room_captain_mask:

    # TODo: Tell about the mask

    # Captain ask to see the body.
    # You both go to tyhomas moody's room

    # Captain even sees the poison on the nightstand. Doctor didn't see it.

    # ADd choice, he asks if you want to sleep with him you HAVE to say yes. OR you DIE.


    # ADD trust captain unlock, you'll follow the captain around in the morning IF you sleep with him you'll be fine.
    return

label doctor_day2_evening_billiard_room_captain_avoid:

    doctor """
    Not really, I just wanted to see who was there.
    """

    captain """
    All right, then if you don't mind, I was in the middle of a captivating part in my book.
    """

    doctor """
    I'll leave you to it then.
    """

    # """
    # I don't why, but I don't feel like trusting him.

    # If want help, I should seek it somewhere else.
    # """

    return