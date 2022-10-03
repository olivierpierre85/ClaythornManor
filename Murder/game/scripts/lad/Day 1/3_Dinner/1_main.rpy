# Introduction for hero
label lad_day1_dinner:

    call change_time(18,30)

    scene dining_hall

    """
    Everyone sits at a place with their names on them.

    You turn your attention to the group of people seated a the table, and count eight persons.

    While you are examining everyone, an older lady enters the room. She takes her place at the center of the table.

    """

    call host_welcome_speech

    "After the speech, everyone seems pleased. And a few of the guests started showing their appreciation to the host"

    host "Please no need to thank me. The food will be served, enjoy your meal."

    play music upbeat_02

    """
    The butler then enters the room, accompany by the footman.
    
    They proceed in serving the first dish and pouring drinks to everyone.
    
    The mood starts to relax, and the sound of different conversations fills the room.

    You then turn your attention to the guests next to you.

    You are sitting between Amalia Baxter, and a middle aged man wearing glasses.

    It's name card reads 'Doctor Daniel Baldwin'
    """

    $ doctor_details.introduce()

    $ time_left = 60

    $ current_menu = TimedMenu([
        TimedMenuChoice('Talk to Daniel Baldwin', 'lad_day1_dinner_doctor'),
        TimedMenuChoice('Talk to Amalia Baxter', 'lad_day1_dinner_psychic')
    ], image_left = "doctor", image_right = "psychic")
    call run_menu(current_menu)

    stop music fadeout 5.0

    """
    The dinner is ending.

    The host explain that we can continue to discuss and enjoy drinks in the billiard room. Or for those tired by the journey, we can simply go to bed.

    Since I haven't been able to see my room, I better go there first.

    I ask the footman to show me the way.
    """

    jump lad_day1_evening

  
label lad_day1_dinner_psychic:

    call psychic_generic
    
    return
    

label lad_day1_dinner_doctor:

    call doctor_generic

    return


