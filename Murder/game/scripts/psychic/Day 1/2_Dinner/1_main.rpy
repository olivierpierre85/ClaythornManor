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

    Then, an elegant lady enters the room.
    """

    call host_welcome_speech

    """
    Well said.
    """

    host """ TODO
    Please no need to thank me. The food will be served, enjoy your meal.
    """

    """TODO
    The butler then enters the room, accompany by the footman.
    
    They proceed in serving the first dish and pouring drinks to everyone.
    
    The mood starts to relax, and the sound of different conversations fills the room.

    I turn my attention to the guests next to me.

    I am sitting between Amelia Baxter, and Daniel Baldwin.
    """


    # $ time_left = 60

    # $ current_menu = TimedMenu([
    #     TimedMenuChoice('Talk to Sushil Sinha', 'psychic_day1_dinner_captain'), # SHould they be keep_alive ?
    #     TimedMenuChoice('Talk to Amelia Baxter', 'psychic_day1_dinner_lad')
    # ], image_left = "doctor", image_right = "psychic")
    # call run_menu(current_menu)

    stop music fadeout 5.0

    """ TODO
    The dinner is ending.

    The host explain that we can continue to discuss and enjoy drinks in the billiard room. Or for those tired by the journey, we can simply go to bed.

    Since I haven't been able to see my room, I better go there first.

    I ask the footman to show me the way.
    """

    stop music fadeout 10.0
    
    jump lad_day1_evening

  
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

    captain """ TODO more
    Miss Baxter.
    """

    psychic """
    Mister Sinha.
    """

    call captain_generic

    return


