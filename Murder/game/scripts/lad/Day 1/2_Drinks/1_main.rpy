label lad_day1_drinks:
  
    scene tea_room

    play music "audio/music/Upbeat.mp3"

    """
    I look around the room and see multiple persons already engage in conversation.
    
    But two persons are sitting alone. A middle age man sitting on a couch, and a young woman.

    They seem more approachable than the rest.

    """

    $ time_left = 30
    $ current_menu = TimedMenu([
        TimedMenuChoice('Talk To the man', 'lad_day1_drinks_drunk', 10),
        TimedMenuChoice('Talk To the woman', 'lad_day1_drinks_psychic')
        ], image_left = "drunk", image_right = "psychic")
    call run_menu(current_menu)
    $ current_menu = None

    "You would like to keep talking, but you are interrupted by the butler entering the room."

    show butler at truecenter

    butler "Dinner is served. Please follow me to the dining room."

    hide butler 

    "Everyone moves to the dining room"

    stop music

    jump lad_day1_dinner


label lad_day1_drinks_psychic:

    """
    I am approaching the middle-aged lady.
    """

    call psychic_generic

    return

label lad_day1_drinks_drunk:

    """
    I am heading toward the older man.

    He has a glass of whisky on hand. His gaze is empty.
    
    """
    
    lad "Hello sir, how are you ?"

    drunk "(Snore...)"

    "It's seems hopeless to talk to him."

    return