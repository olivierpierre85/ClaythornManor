label lad_day1_drinks:
  
    scene tea_room

    # Introduces EVERYONE !
    """
    As I enter the room, the butler introduces me, almost shouting.
    """

    butler """
    Mister Ted Haring.
    """

    """
    Everyone turns their head to me and nod a hello.

    From a distance, the butler gives me a short introduction of every guests.
    """

    show captain at truecenter
    butler """ 
    The older man talking is from India and his name is Sushil Sinha.
    """
    hide captain

    show nurse at truecenter
    butler """
    He is in conversation with Rosalind Marshman.
    """
    hide nurse

    show doctor at truecenter
    butler """
    And the man with the glasses is Daniel Baldwin.
    """
    hide doctor

    show broken at truecenter
    butler """
    Don't be alarmed by the man in the mask. 
    He is a war veteran named Thomas Moody.
    """
    hide broken

    show drunk at truecenter
    butler """
    The man sitting on the couch, looking rather exhausted is Samuel Manning
. 
    """
    hide drunk

    show psychic at truecenter
    butler """
    The older lady in the corner of the room is Amalia Baxter.
    """
    hide psychic

    lad """
    I don't see our host in the room.
    """

    butler """
    Lady Claythorn is still busy at the moment.

    You'll meet her at dinner.
    """

    """
    After this introduction he leaves me and go stand in the corner of the room.

    Most of the guests are already in conversation.
    
    But Amalia Baxter and Samuel Manning are alone.

    They seem more approachable than the rest.
    """
    
    $ time_left = 30
    $ current_menu = TimedMenu([
        TimedMenuChoice('Talk to Samuel Manning', 'lad_day1_drinks_drunk', 5),
        TimedMenuChoice('Talk to Amalia Baxter', 'lad_day1_drinks_psychic', 5)
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

    lad """
    Nice to meet you miss Baxter. I am Ted Haring.
    """

    psychic """
    Nice to meet you mister Haring.
    """
    
    $ current_character.has_met.add('psychic')

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