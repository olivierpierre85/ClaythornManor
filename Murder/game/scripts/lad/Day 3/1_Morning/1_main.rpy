label lad_day3_morning:
    
    call black_screen_transition("Ted Harring", "Sunday")

    $ change_room('lad_room', irisout)

    if lad_day2_believe_psychic:
        call change_time(7,00, "Morning", "Sunday")
        # You talked to and believed psychic
        # So she came to wake you at dawn
    else:
        # Otherwise, you'll have less time to explore
        call change_time(8,00, "Morning", "Sunday")

    play sound door_knock
    
    """
    I woke up suddenly with the sound of someone knocking frantically at the door.
    """

    play sound door_knock

    if lad_day2_drunk:
            """
            My head hurts like crazy.

            Oh my god, I wish I could sleep more.
            """    

    psychic """
    Mister Harring are you there ?
    """
    
    if lad_day2_believe_psychic:

        """
        Miss Baxter ?

        Right, we agreed to wake each other up.

        I just didn't think it would be that early.
        """

        lad """
        I am coming !
        """

        """
        I dress up in a hurry and open the door.

        Amalia Baxter enters, visibly nervous.
        """

        psychic """
        I believe I was right yesterday.

        Something strange is happening.
        """

        lad """
        What do you mean?
        """

        psychic """
        I didn't run into any staff members on my way here.

        At this hour, they should be busy with the fires, the cleaning, setting up breakfast.

        But I saw nor heard anything.

        It's quite as a cemetery in here.
        """

        lad """
        Are you sure it's not normal.?

        It's still very early.
        """

        psychic """
        I don't think so.

        I woke at this hour yesterday and the house was teeming with life.

        Something is amiss I am telling you.
        """

        lad """
        Okay, if you say so.

        We better look into it then.
        """

        

    else:
        """
        Miss Baxter again ?

        What is it now ?
        """

        lad """
        I am coming !
        """

        """
        I dress up in a hurry and open the door.
        """

        lad """
        Miss Baxter, is everything alright?
        """

        psychic """
        I don't know.

        I think something weird happening.
        """

        """
        I woke early as usual and tried to get a cup of tea before breakfast.

        But no one is there.
        """

        lad """
        What do you mean ?
        """

        psychic """
        That the staff is gone, all of them.

        I tried the kitchen, outside, the whole place even.

        I didn't see anybody.
        """

        lad """
        Can't they be still asleep ?
        """

        psychic """
        Oh Mister Harring, that's impossible.

        They are supposed to be awake since dawn to get the house ready for the day.

        They couldn't have just slept in.

        I also went to check on misses Claythorn and she doesn't answer.
        """

        lad """
        Don't worry, I am sure it's not so bad.
        """

        psychic """
        I don't know.

        But I don't want to keep on searching alone.

        Would please accompany me to check on the others ?
        """

        lad """
        Well, I am awake now so why not.

        If that can appease you.
        """

        """
        We decide it's better we check again every room together.

        So first we go to ...
        """
        
    # TODO test every room before it's over
    
    if lad_day2_believe_psychic:
        $ time_left = 120
    else:
        $ time_left = 60

    call run_menu(lad_map_menu)

    call change_time(9,00)

    # TODO force one choice to go downstairs ?
    call run_menu(TimedMenu([
        TimedMenuChoice(default_room_text('host_room'), 'lad_day3_morning_host_room', 20, room = 'host_room'),
        TimedMenuChoice(default_room_text('drunk_room'), 'lad_day3_morning_drunk_room', 20, room = 'drunk_room'),
        TimedMenuChoice(default_room_text('captain_room'), 'lad_day3_morning_captain_room', 20, room = 'captain_room'),
        TimedMenuChoice(default_room_text('gun_room'), 'lad_day3_morning_gun_room', 20, room = 'gun_room'),
        TimedMenuChoice('Go wait for Sushil', 'lad_day3_morning_give_up', early_exit = True, room = 'tea_room', condition = "lad_day3_morning_captain_found"),
    ], is_map = True))

    $ change_room('tea_room')

    """
    I don't think we'll find something now.

    So we settled in the tea room to wait for the captain.
    """

    captain """
    That's unbelievable, but it looks like we are the three remaining living souls in this place.
    """

    # TODO add call with telephone ? Room with a telephone ?

    # TODO the captain saw a car in the garage BUT it's out of gas, AND he can't find the keys, so we'll need to walk

    $ lad_day3_escape_menu = TimedMenu([
        TimedMenuChoice('Stay here with Amelia', 'lad_day3_stay', early_exit = True ),
        TimedMenuChoice('Follow Sushil', 'lad_day3_escape', early_exit = True)
    ], image_left = "psychic",  image_right = "captain")
    $ time_left = 1
    call run_menu(lad_day3_escape_menu)

    # TODO handle possible endings
    # TODO add switch on the 
    # TODO more logic in ending names
    if lad_day3_gun_downed:
        jump lad_gun_downed_ending
    elif lad_day3_poisoned:
        jump lad_ending_day3_poisoned


    return

label lad_day3_morning_give_up:

    return

label lad_day3_morning_gun_room:

    $ change_room('gun_room')

    """
    A room filled with guns.

    Normally I wouldn't touch them.

    But I think because of the circumstances, I think I can make an exception.

    I look around and find a small handgun.

    It's not loaded but it might deter someone to attack me.

    So I take it.
    """

    # TODO add handgun to tools?

    return


label lad_day3_morning_captain_room:

    scene hallway

    play sound door_knock

    lad """
    Is there someone in there ?
    """

    captain """
    Yes, what is it ?
    """

    $ unlock_map('captain_room')

    lad """
    It's Ted Harring. I am here with Amelia Baxter.

    We would like to talk to you.
    """

    captain """
    Alright come on in.
    """

    $ change_room('captain_room')

    """
    We enter the bedroom.

    It is very tidy.

    The captain is already dressed.

    He was reading a book sitting on a chair.

    As we enter, he stands up, looking surprised.
    """

    captain """
    Well, I was not expecting visitors this early.
    
    What can I do for you ?
    """

    # TODO add if depending on the number of rooms already visited, specially the host room
    psychic """
    We believe something strange is going on.

    This morning, you and mister Harring are the only persons I encountered so far.

    We don't seem to find any of the servants, nor any other guests so far.
    """

    captain """
    Now that you mention it, nobody came to tend the fire this morning.

    It's rather unusual.

    But I don't think it is that concerning. There probably is very going explanation.
    """

    lad """
    We hope so too. 

    But just in case, we where looking inside the manor for someone to explain us what's happening.
    """

    captain """
    I understand. I can come with you if you want.
    """

    psychic """
    Thank you but,... maybe,... maybe it's best if we split up.

    We could cover more ground this way.
    """

    """
    Amelia seemed nervous when she answered.
    """

    captain """
    Good thinking. I'll look on my own, and we can meet later.

    Maybe in the tea room ?
    """

    psychic """
    That sounds perfect.

    See you then.
    """

    $ lad_day3_morning_captain_found = True

    return 

label lad_day3_morning_host_room:

    scene hallway

    play sound door_knock

    psychic """
    This is Lady Claythorn Room.
    """

    $ unlock_map('host_room')

    lad """
    Miss Claythorn ?

    Are you there ?
    """

    """
    There is no response.
    """

    # psychic """
    # I told you she was not there.
    # """

    """
    Then, she put her on hand on the clutch.

    The door opens.
    """

    lad surprised """
    What are you doing ? 

    We can't enter like that !
    """

    """
    But it's too late. She's already rushed inside.

    I have no choice but to follow her.
    """

    $ change_room('host_room')

    """
    It's empty.

    The wardrobe is wide open. There are some clothes on the floor.
    """

    psychic """
    It looks like she left in a hurry.
    """

    """
    We looked for a clue of what happened but found nothing.
    """

    psychic """
    Well, she either have left, or she is still hiding somewhere in the manor.

    There is no need to dwell here any longer.
    """
    
    return 

label lad_day3_morning_drunk_room:

    scene hallway

    # TODO without captain, not possible,
    if not lad_day3_morning_captain_found:
        """
        Samuel Manning room.

        It's closed.

        The captain has the key.
        """
    else:
        captain """
        Move aside, I am gonna open it.
        """

        $ change_room('drunk_room')

    return

label lad_day3_morning_psychic_room:

    $ change_room('psychic_room')

    psychic """
    What are you doing in my room?

    You don't think someone is hiding here?
    """

    lad """
    Probably not, but it's better to be thorough.
    """

    """
    But she is right.

    There is nothing or nobody here.
    """
    