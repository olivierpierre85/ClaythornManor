label lad_day1_drinks:
  
    scene tea_room

    """
    I enter the room where I see a few people already in conversation.
    
    But two persons are alone. A middle age man sitting on a couch, and a young woman standing by herself.

    They seem more approachable than the rest.

    """
    
    $ time_left = 30
    $ current_menu = TimedMenu([
        TimedMenuChoice('Talk to the man', 'lad_day1_drinks_drunk', 5),
        TimedMenuChoice('Talk to the woman', 'lad_day1_drinks_psychic', 5)
        ], image_left = "drunk", image_right = "psychic")
    call run_menu(current_menu)

    "Suddenly, the butler comes into the room."

    butler "Dinner is served. Please follow me to the dining room."

    hide butler 

    stop music fadeout 5.0

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

    "He reeks of booze, and is deep asleep. It's useless talking to him."

    return