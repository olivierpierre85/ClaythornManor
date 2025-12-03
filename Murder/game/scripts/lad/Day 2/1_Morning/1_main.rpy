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

    call change_time(9,00, 'Morning', 'Saturday', hide_minutes = True, chapter='saturday_morning')

    $ lad_details.add_checkpoint("lad_day2_morning") 

    call black_screen_transition("Ted Harring", chapters_names[current_chapter])

    $ change_room("bedroom_lad", irisout)
    
    $ change_room('bedroom_lad')

    $ play_music('upbeat', 3)

    """
    I slept through the night. 
    
    The storm from yesterday has passed and the weather is clearer now.
    """

    if lad_details.threads.is_unlocked('day1_drunk'):
        
        """
        Oh my God, my head is pounding.

        Why on earth did I drink so much yesterday?
        """
    
    """
    After getting ready, I leave my room to have breakfast.
    """

    call change_time(9,30)

    $ change_room('dining_room')

    """
    Most of the guests are already seated in the dining room.

    There is a breakfast buffet set out. 
    
    I help myself to eggs, bacon, bread and a few other things, not really following any particular order.

    I have no idea if this is what I'm supposed to do.

    I quietly take the same seat I occupied yesterday, hoping to go unnoticed.

    Daniel Baldwin and Amelia Baxter are already present.
    """

    call common_day2_morning_lad_psychic

    """
    Everything is happening fast. What should I do?
    """

    $ time_left = 30
    call run_menu(
        TimedMenu("lad_day2_morning_follow", [
            TimedMenuChoice('Follow them', 'common_day2_breakfast_follow_doctor_lad_host', 30, early_exit = True ),
            TimedMenuChoice('Stay there and finish the most important meal of the day', 'lad_day2_breakfast_eat', 5, early_exit = True)
        ])
    )

    call change_time(10,00)

    if lad_details.saved_variables["day2_breakfast_follow"]:

        $ change_room('dining_room')

        """
        As we returned to the dining room, our hostess had just finished explaining the situation.

        She seemed to regain her composure upon seeing the doctor.
        """

    else:

        $ stop_music()

        call common_day2_morning_host_death

    call common_day2_morning_host_death_doctor    

    """
    When everyone is done eating, Lady Claythorn speaks up.
    """

    $ stop_music()

    call common_day2_morning_host_hunt

    """
    A hunt... A proper aristocratic hunt.

    Now that's something to witness.

    It's not as if I'll get this opportunity often.

    And I might not be the only one feeling out of place, especially if Lady Claythorn is correct.

    So there's no need for embarrassment.

    However, I have never so much as held a gun in my life.

    Those older men might not be of the gentry, but they likely learned to shoot during the war.

    What should I do?
    """

    $ time_left = TIME_MAX # Trick to avoid problems, todo, find a better way
    
    call run_menu(
        TimedMenu("lad_day2_morning_hunt", [
            TimedMenuChoice('Go on the hunt and risk to embarrass yourself, or worse', 'lad_day2_hunt_choice', early_exit = True),
            TimedMenuChoice('Stay here where it\'s cosy', 'lad_day2_no_hunt_choice', early_exit = True)
        ])
    )

    return

# tWO jumps instead of calling the label from the menu so the menu IS resetted to 0
# If not doing that, the rest of the game will happen Inside the menu above
label lad_day2_hunt_choice:

    $ lad_details.threads.unlock('hunt')

    jump lad_day2_hunt

label lad_day2_no_hunt_choice:

    jump lad_day2_no_hunt

label lad_day2_breakfast_eat:

    psychic -angry """
    I wonder what this is about.
    """

    lad """
    Me too. I have a bad feeling about it.
    """

    psychic """
    Well, there's no reason to worry now.

    We'll just have to wait and see.
    """

    lad """
    You're right.

    We should probably talk about something else.
    """

    call psychic_generic()
    
    return

    