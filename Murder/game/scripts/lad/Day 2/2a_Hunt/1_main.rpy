label lad_day2_hunt:
    call black_screen_transition("The Lad - The Hunt") # Good ?
    scene gun_room

    play music upbeat_02 fadein 10.0

    """
    Well I don't know if it's my best idea.

    But I guess I didn't feel it was right stay behind with the ladies.

    """

    #     I wonder what it says about me I wonder.
    # TODO easter egg only if it's the first choice

    butler """
    So it's your first hunt mister Harring ?
    """
 
    lad """
    Yes indeed. I don't even know how to use a rifle.
    """

    butler """
    Don't worry sir. A footman will follow you and will reload the gun for you.
    
    All you have to do is point at you target when you encountered something, and pull the trigger.
    """

    lad """
    All right, that sounds easy enough. Will everyone have a footman as well ?
    """

    butler """
    No just you. I will be with Lady Claythorn and the others insisted they didn't need help.
    """

    lad """
    I see. And what kind of animal are we hunting today ?
    """

    butler """
    I think we will encounter wild birds mostly. But we might also run into some deers or wild pigs.
    """

    lad """
    Aren't those dangerous ?
    """

    butler """
    Not if you don't get too close to them. And again you won't be alone, so there is no reason be scared.
    """
    lad """
    I am not scared, just curious.
    """

    butler """
    Right. Anyway, you can pick up this gun and wear the clothes I lay down on the table.

    Come join the others outside when you are ready.
    """

    lad """
    Perfect, thanks.
    """

    """
    I am trying the clothes before me. They fit perfectly.

    Well, if something happens to me, at least I'll look good.

    I'll go outside meet the others.
    """

    scene manor_garden

    """
    I join the others in the garden.

    They all look quite comfortable in in their hunting clothes.

    There is Doctor Baldwin, the old Indian man, Lady Claythorn and her staff.

    And even the drunk guy is here.

    Wait what ?!

    He has a gun on hand. That can't be safe.

    I approach the Butler.
    """

    lad """
    Is it okay for him to have a gun ? He looked a bit drunk this morning.
    """

    butler """
    I was afraid of that at first too. But I just talked to him and I can assure you that he is perfectly fine.

    He may have been a bit off because of yesterday, but the breakfast and the events of this morning must have sober him up.
    """

    lad """
    Ok, if you are sure.
    """

    """
    Still, I better stay away from him.

    The butler then addresses the whole group.
    """

    butler """
    Good, now that everybody is ready, I propose that we split into two groups.

    It will be easier to spot game this way.

    """

    # TODO more explanation about the program, where to meet again....


    """
    People agree and the Indian man ask to join our host.

    The drunk man insists on going with the doctor, who agrees.

    I am the odd one out.

    Which group should I join ?
    """

    $ lad_day2_hunt_menu = TimedMenu([
        TimedMenuChoice('The Doctor and the Drunk', 'lad_day2_hunt_accident', early_exit = True ),
        TimedMenuChoice('The Lady and the Indian Man', 'lad_day2_hunt_fine', early_exit = True)
    ], image_left = "drunk", image_left_2 = "doctor", image_right = "host", image_right_2 = "captain")
    $ time_left = 1
    call run_menu(lad_day2_hunt_menu)

    # TODO go back to mansion


    return