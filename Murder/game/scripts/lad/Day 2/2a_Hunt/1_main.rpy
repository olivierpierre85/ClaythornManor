# --------------------------------------------
#   Lad
#           
#   Saturday - The Hunt
# 
#   11:00 -> 15:00
#
#   Music: upbeat
#
#   Position
#       - House, Tea room : nurse, psychic 
#       - Forest : host, captain, lad, doctor, drunk
#       - Dead : Broken
#
#   Notes : 
#       - Generic doctor, 30 minutes
# --------------------------------------------
label lad_day2_hunt:

    $ lad_details.important_choices.unlock('hunt')

    $ current_character.add_checkpoint("lad_day2_hunt") 

    call change_time(11,00, 'Hunt', 'Saturday')

    call black_screen_transition("Ted Harring", "The Hunt") # Good? TODO check consistency with no hunt
    
    scene gun_room

    $ play_music('upbeat', 1, fadein_val=10.0)

    $ lad_details.saved_variables["day2_hunt"] = True

    """
    Well, I don't know if this is my best idea.

    But I guess it didn't feel right to stay behind with the ladies.
    """

    # TODO achievement,  Hunt like a man

    butler """
    So, this is your first hunt, Mister Harring?
    """

    lad """
    Yes. I must admit that I don't even know how to use a rifle.
    """

    butler """
    Not to worry, sir. A footman will follow you and will reload the gun for you.

    All you have to do is point at your target when you encounter something and pull the trigger.
    """

    lad """
    All right, that sounds easy enough. Will everyone have a footman as well?
    """

    butler """
    It will be just you, I believe. I will be with Lady Claythorn, and the others insisted they didn't need help.
    """

    """
    Of course. So, I'll be the weak link today. Great.
    """

    lad """
    I see. And what kind of animal are we hunting today?
    """

    butler """
    I think we will mostly encounter wild birds. But we might also run into some rabbits or even deer.
    """

    lad """
    Aren't those dangerous?
    """

    butler """
    Not if you don't get too close to them. And again, you won't be alone, so there's no reason to be scared.
    """

    lad """
    I am not scared, just curious.
    """

    butler """
    Right.

    Anyway, you can pick up this gun and wear the clothes I laid out on the table.

    Join the others outside when you're ready.
    """

    lad """
    Perfect, thanks.
    """

    """
    I try on the clothes before me. They fit perfectly.

    If something happens to me, at least I'll look good.
    """

    $ change_room('manor_garden')

    """
    I join the others in the garden.

    They all look quite comfortable in their hunting clothes.

    There's Doctor Baldwin, Sushil Sinha, Lady Claythorn and her staff.

    And even Samuel Manning is here.

    Wait, what?!

    How on earth was he allowed to come with us?

    I approach the butler.
    """

    lad """
    Is it okay for Mister Manning to have a gun? He seemed a bit drunk this morning.
    """

    butler """
    I was concerned about that at first too. But I just spoke to him, and I can assure you he's perfectly fine.

    He might have been a bit off because of yesterday, but the breakfast and the events of this morning must have sobered him up.
    """

    lad """
    Ok, if you're sure.
    """

    """
    Still, I'd better stay away from him.

    The butler then addresses everyone.
    """

    butler """
    Good, now that everyone is ready, I propose we split into two groups.

    It will be easier to spot game that way.
    """

    """
    People agree, and Sushil Sinha asks to partner with our host.

    The drunk man insists on going with the doctor, who accepts.

    I am the odd one out.

    Which group should I join?
    """

    $ lad_day2_hunt_menu = TimedMenu("lad_day2_hunt_menu", [
        TimedMenuChoice('Daniel Baldwin and Samuel Manning', 'lad_day2_hunt_accident', early_exit = True ),
        TimedMenuChoice('Lady Claythorn and Sushil Sinha', 'lad_day2_hunt_noaccident', early_exit = True)
    ], image_left = "drunk", image_left_2 = "doctor", image_right = "host", image_right_2 = "captain")
    $ time_left = 1
    call run_menu(lad_day2_hunt_menu)

    jump lad_day2_afternoon

    return