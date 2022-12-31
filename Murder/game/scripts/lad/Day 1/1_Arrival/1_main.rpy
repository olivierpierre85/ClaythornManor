# --------------------------------------------
#               Ted Harring
#           Friday 18:10 Arrival
#
#   Alive: Everyone
label lad_day1_arrival:

    $ lad_details.add_checkpoint("lad_day1_arrival") 
    
    call black_screen_transition("Ted Harring", "Friday")

    $ change_room('great_hall', irisout)
    
    call change_time(18,10, 'Arrival', 'Friday')

    $ play_music('upbeat')

    butler """
    Good afternoon Sir.
    """

    lad "Hello, I am Ted Harring, I was invited by Lady Claythorn."

    butler """
    Yes, of course Mr Harring.

    Welcome to Claythorn Manor.

    I am afraid you won't have time to change right now. 

    Everyone is already there, and dinner will be ready very soon.

    So if you follow me into the tea room, you can join the rest of the party for some drinks.
    """

    """
    Well it's not like I have multiple change of clothes anyway. So I follow him.
    """

    $ change_room('tea_room')

    # Introduces EVERYONE !
    """
    As I enter the room, the butler introduces me, almost shouting.
    """

    butler """
    Mister TED HARRING.
    """

    """
    Everyone turns their head to me. 
    
    Some nods at me, others barely acknowledge me.

    From a distance, the butler gives me a short introduction of every guest.
    """

    show captain at truecenter
    butler """ 
    The older man talking is from India and his name is Sushil Sinha.
    """
    hide captain

    show nurse at truecenter
    butler """
    He is in conversation with Rosalind Marsh...
    """
    hide nurse

    show doctor at truecenter
    butler """
    .. and with Daniel Baldwin. The man with the glasses.
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
    The man sitting on the couch, looking rather exhausted is Samuel Manning.
    """
    hide drunk

    show psychic at truecenter
    butler """
    The older lady in the corner of the room is Amelia Baxter.
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
    
    But Amelia Baxter and Samuel Manning are alone.

    They seem more approachable than the rest.
    """
    
    $ time_left = 30 
    
    $ current_menu = TimedMenu([
        TimedMenuChoice('Talk to Samuel Manning', 'lad_day1_drinks_drunk', 5),
        TimedMenuChoice('Talk to Amelia Baxter', 'lad_day1_drinks_psychic', 5), # keep_alive = True, TODO keep alive to allow more choices if leaving by mistakes ?
        ], image_left = "drunk", image_right = "psychic")
    call run_menu(current_menu)

    play sound dinner_gong

    """
    A gong rings. 

    What is that ?

    Then the butler comes into the room.
    """

    butler """
    Dinner is served. Please follow me to the dining room.
    """

    """
    Oh ok. The gong warns people that dinner is served.

    Rich people live differently that's for sure.
    """

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
