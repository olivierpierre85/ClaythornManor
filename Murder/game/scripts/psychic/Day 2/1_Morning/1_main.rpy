label psychic_day2_morning:

    $ current_character.add_checkpoint("psychic_day2_morning") 

    call black_screen_transition("Amelia Baxter", "Saturday")

    scene psychic_room with irisout
    
    $ change_room('psychic_room')

    call change_time(8,30, 'Morning', 'Saturday', hide_minutes = True)

    """
    Despite the storm that raged all night, I manage to sleep relatively well.

    So I take my time getting ready then I head downstairs to the dining room.
    """

    $ change_room('dining_room')

    call change_time(9,20)

    """
    Some of the guests are already eating.

    I grab a plate a the breakfast buffet, then sat down at the same place at the table than yesterday.

    Captain Sinha is already there but I don't feel like talking with him.

    It is too soon for that.

    After a while, Ted Harring joins me at the table.
    """

    call change_time(9,30)

    call day2_breakfast_lad_psychic

    """
    For some reason, Ted Harring also stands up and follows them.

    I guess I am stuck with Sushil Sinha.
    """

    $ time_left = 30

    call captain_generic

    # $ psychic_day1_evening_menu = TimedMenu([
    #     TimedMenuChoice('Follow them', 'lad_day2_breakfast_follow', 30, early_exit = True ),
    #     TimedMenuChoice('Stay there and finish the most important meal of the day', 'lad_day2_breakfast_eat', early_exit = True)
    # ])
    # call run_menu(psychic_day1_evening_menu)

    # TODO generic captain or eat in silence

    call change_time(10,00)

    call day2_breakfast_host_death

    call day2_breakfast_host_death_doctor

    $ stop_music()


    # TODO
    jump work_in_progress


    