# --------------------------------------------
#                Psychic 
#
#           Friday 18:30 Dinner
#
#             Alive: Everyone
# --------------------------------------------
label psychic_day1_dinner:

    $ change_room('dining_room')
    
    call change_time(18,30, 'Dinner', 'Friday')

    $ play_music('chill')

    """
    I sit down at the place with my name on it.

    Then, a lady enters the room.

    She is wearing expensive clothing.
    """

    call host_welcome_speech

    """
    Well said.

    I join in clapping with the rest of the guests.
    """

    host """
    Please no need to thank me. The food will be served, enjoy your meal.
    """

    """
    The food arrives right after the speech.

    Perfect timing here.
    """

    pause 1

    """
    It looks like I already know the persons next to me.
    
    On my left is Mister Sinha.
    
    And Ted Haring is on my right.
    """


    $ time_left = 60

    $ current_menu = TimedMenu([
        TimedMenuChoice('Talk to Sushil Sinha', 'psychic_day1_dinner_captain'), # SHould they be keep_alive?
        TimedMenuChoice('Talk to Ted Harring', 'psychic_day1_dinner_lad')
    ], image_left = "captain", image_right = "lad")

    call run_menu(current_menu)

    $ stop_music()

    """
    The dinner is over.

    The host gave us the opportunity to meet again for drinks. 
    
    But I don't know, this was quite a long day.
    
    Maybe I should just go to bed.

    In any case, I should retire to my room first.
    """

    $ stop_music(10)
    
    jump psychic_day1_evening

  
label psychic_day1_dinner_lad:
    
    lad """
    Hi again Miss Baxter.
    """

    psychic """
    Oh Mister Harring. I am glad we can continue our conversation.
    """

    call lad_generic
    
    return
    

label psychic_day1_dinner_captain:

    """
    Maybe I was too quick to judge him.

    I should try to talk to him again.
    """

    call captain_generic

    return


