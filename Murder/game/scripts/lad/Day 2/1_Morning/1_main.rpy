label lad_day2_morning:

    $ lad_details.add_checkpoint("lad_day2_morning") 

    call black_screen_transition("Ted Harring", "Saturday")

    scene lad_room with irisout
    
    $ change_room('lad_room')

    call change_time(9,00, 'Morning', 'Saturday', hide_minutes = True)

    """
    I slept through the night. 
    
    The storm from yesterday has passed and the weather is clearer now.
    """


    if lad_details.saved_variables["day1_drunk"] :
        """
        Oh my god my head hurts.

        Why did I drink so much yesterday ?
        """
    
    """
    After getting ready, I leave my room to have breakfast.
    """

    call change_time(9,30)

    $ change_room('dining_room')

    """
    Most of the guests are already in the dining room.

    There is a breakfast buffet. So I fix myself a plate: Eggs, bacon, bread,... with no particular logic.

    I have know idea if it is what I am supposed to do.

    So I take my seat at the same place than yesterday trying not to be noticed.

    Daniel Baldwin and Amelia Baxter are already there.
    """

    call day2_breakfast_lad_psychic

    # """
    # I nod. Not sure what to say.
    # """

    # if lad_details.saved_variables["day1_drinks"] > 0:

    #     "I look around the room."

    #     lad """
    #     I don\'t see the man with the mask either, Thomas Moody.

    #     I talked to him yesterday and he seemed fine to me.
    #     """

    """
    Everything is happening fast. What should I do ?
    """
    
    $ lad_day1_evening_menu = TimedMenu([
        TimedMenuChoice('Follow them', 'lad_day2_breakfast_follow', 30, early_exit = True ),
        TimedMenuChoice('Stay there and finish the most important meal of the day', 'lad_day2_breakfast_eat', early_exit = True)
    ])
    $ time_left = 30
    call run_menu(lad_day1_evening_menu)

    call change_time(10,00)

    if lad_details.saved_variables["day2_breakfast_follow"]:

        """
        As we entered the dining room again, the host just finished explaining the situation.

        She has regained her composure when she sees the doctor.
        """

    else:

        call day2_breakfast_host_death

    call day2_breakfast_host_death_doctor

    stop music fadeout 5.0

    jump lad_day2_morning_breakfast_over


label lad_day2_breakfast_eat:

    psychic -angry """
    I wonder what this is about.
    """

    lad """
    Me too.I have a bad feeling about it.
    """

    psychic """
    Well no reason to worry now.

    We just have to wait and see.
    """

    """
    That's right.

    We should probably talk about something else.
    """

    call psychic_generic()
    
    return

    