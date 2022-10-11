label lad_day2_morning:

    scene dining_hall

    call change_time(10,00)

    """
    When every one is done eating, Lady Claythorn speaks up.
    """

    host """
    Well, as I told you before, activities were planned for the day.

    This morning those who wished, we were supposed to go on a hunt.

    It's a sad affair that has happened, but it's not a reason to stay here doing nothing.

    So, if nobody disagrees, I propose that we continue according to what was planned.
    """

    """
    A murmur of assent runs through the assembly.
    """

    host """
    Excellent.

    Everything is ready for those who wish to join the hunt. 
    
    I know most of you are probably not accustomed with this type of event.

    That's why our staff can lend you everything you will need, clothes, the guns. And they will also assist you during the whole event.

    But of course, you can decide to just stay here.

    You can relax and enjoy the warmth of the house until the others return.

    """

    """
    A hunt... A real aristocratic hunt.

    That is something to see.

    It's not like I will have this opportunity often.

    And I might not be the only one out of my depth if Lady Claythorn is right. 

    So I won't be embarrassed.

    On the other hand, I have never even held a gun in my life.

    Those older guys may not be gentry, but they've probably learned how to shoot during the war.

    So what should I do ?
    """

    $ lad_day2_morning_menu = TimedMenu([
        TimedMenuChoice('Go on the hunt and risk to embarrass myself, or worse', 'lad_day2_morning_hunt', early_exit = True),
        TimedMenuChoice('Stay here were it\'s cosy', 'lad_day2_morning_nohunt', early_exit = True)
    ])
    $ time_left = 1
    call run_menu(lad_day2_morning_menu)

    jump lad_day2_afternoon

    return

