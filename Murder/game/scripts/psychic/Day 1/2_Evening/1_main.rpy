# --------------------------------------------
#   Psychic
#           
#   Friday - Evening
#   
#   18:30 -> 23:00
#
#   Music: chill
#
#   Alive: Everyone
#
#   Notes
#       - Generic Lad, Captain: 60 minutes
#       - Map menu: 120 minutes
# --------------------------------------------
label psychic_day1_evening:

    call change_time(18,30, 'Dinner', 'Friday')

    $ current_character.add_checkpoint("psychic_day1_evening") 

    call black_screen_transition("Amelia Baxter", "Friday Evening")

    $ change_room('dining_room', irisout)

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
        TimedMenuChoice('Talk to Sushil Sinha', 'psychic_day1_dinner_captain'),
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

    pause 2.0

    call change_time(21,00, 'Evening', 'Friday')

    $ change_room('psychic_room', dissolve)

    """
    Well, I am comfortably settled.

    What should I do now?
    """

    $ play_music('upbeat')

    $ time_left = 120
    
    call run_menu(psychic_details.saved_variables["map_menu"])

    call change_time(23,00)

    $ stop_music()

    """
    It's been a long day.

    I can't stay up any longer.

    It's time to go to bed.
    """

    $ change_room('psychic_room')

    jump psychic_day2_morning
        

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