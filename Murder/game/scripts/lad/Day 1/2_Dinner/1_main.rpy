# --------------------------------------------
#               Ted Harring
#           Friday 18:30 Arrival
#
#   Alive: Everyone
label lad_day1_dinner:

    $ change_room('dining_room')
    
    call change_time(18,30, 'Dinner', 'Friday')

    $ play_music('chill')

    """
    Everyone sits at a place with their names on them.

    While I am examining everyone, Lady Claythorn enters the room. 
    
    She takes her place at the table.
    """

    call host_welcome_speech

    """
    After the speech, everyone seems pleased. And a few of the guests started showing their appreciation to the host.
    """

    host """
    Please no need to thank me. The food will be served, enjoy your meal.
    """

    """
    The butler then enters the room, accompany by the footman.
    
    They proceed in serving the first dish and pouring drinks to everyone.
    
    The mood starts to relax, and the sound of different conversations fills the room.

    I turn my attention to the guests next to me.

    I am sitting between Amelia Baxter, and Daniel Baldwin.
    """

    # $ doctor_details.introduce()

    $ time_left = 60

    $ current_menu = TimedMenu([
        TimedMenuChoice('Talk to Daniel Baldwin', 'lad_day1_dinner_doctor'), # SHould they be keep_alive ?
        TimedMenuChoice('Talk to Amelia Baxter', 'lad_day1_dinner_psychic')
    ], image_left = "doctor", image_right = "psychic")
    call run_menu(current_menu)

    stop music fadeout 5.0

    """
    The dinner is ending.

    The host explain that we can continue to discuss and enjoy drinks in the billiard room. Or for those tired by the journey, we can simply go to bed.

    Since I haven't been able to see my room, I better go there first.

    I ask the footman to show me the way.
    """

    stop music fadeout 10.0
    
    jump lad_day1_evening

  
label lad_day1_dinner_psychic:
    
    lad """
    Hi again Miss Baxter.
    """

    psychic """
    Oh Mister Harring. I am glad we can continue our conversation.
    """

    call psychic_generic
    
    return
    

label lad_day1_dinner_doctor:

    lad """
    Hello. I am Ted Harring.
    """

    doctor """
    Hi mister Haring, I am doctor Daniel Baldwin.
    """

    lad """
    Nice to meet you doctor.
    """

    call doctor_generic

    return


