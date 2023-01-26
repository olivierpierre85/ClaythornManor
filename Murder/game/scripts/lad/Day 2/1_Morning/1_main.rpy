# --------------------------------------------
#   Lad
#           
#   Saturday - Morning
# 
#   9:00 -> 11:00
#
#   Music: chill
#
#   Position
#       - Dinner Room : Everyone else
#       - Dead : Broken
#   
#   Notes : 
#       - Generic Psychic, 25 minutes
# --------------------------------------------
label lad_day2_morning:

    call change_time(9,00, 'Morning', 'Saturday', hide_minutes = True)

    $ lad_details.add_checkpoint("lad_day2_morning") 

    call black_screen_transition("Ted Harring", "Saturday")

    scene lad_room with irisout
    
    $ change_room('lad_room')

    $ play_music('upbeat', 3)

    """
    I slept through the night. 
    
    The storm from yesterday has passed and the weather is clearer now.
    """


    if lad_details.saved_variables["day1_drunk"] :
        
        """
        Oh my god my head hurts.

        Why did I drink so much yesterday?
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

    """
    Everything is happening fast. What should I do?
    """

    $ time_left = 30

    $ lad_day1_evening_menu = TimedMenu([
        TimedMenuChoice('Follow them', 'lad_day2_breakfast_follow', 30, early_exit = True ),
        TimedMenuChoice('Stay there and finish the most important meal of the day', 'lad_day2_breakfast_eat', 5, early_exit = True)
    ])
    
    call run_menu(lad_day1_evening_menu)

    call change_time(10,00)

    if lad_details.saved_variables["day2_breakfast_follow"]:

        """
        As we entered the dining room again, the host just finished explaining the situation.

        She has regained her composure when she sees the doctor.
        """

    else:

        $ stop_music()

        call day2_breakfast_host_death

    call day2_breakfast_host_death_doctor    

    """
    When every one is done eating, Lady Claythorn speaks up.
    """

    $ stop_music()

    call host_broken_death_speech

    """
    A hunt... A real aristocratic hunt.

    That is something to see.

    It's not like I will have this opportunity often.

    And I might not be the only one out of my depth if Lady Claythorn is right. 

    So I shouldn't be embarrassed.

    On the other hand, I have never even held a gun in my life.

    Those older guys may not be gentry, but they've probably learned how to shoot during the war.

    So what should I do?
    """

    $ time_left = TIME_MAX # Trick to avoid problems, todo, find a better way

    $ lad_day2_morning_menu = TimedMenu([
        TimedMenuChoice('Go on the hunt and risk to embarrass yourself, or worse', 'lad_day2_hunt', early_exit = True),
        TimedMenuChoice('Stay here where it\'s cosy', 'lad_day2_no_hunt', early_exit = True)
    ])
    
    call run_menu(lad_day2_morning_menu)

    jump lad_day2_afternoon


label lad_day2_breakfast_eat:

    psychic """
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

    