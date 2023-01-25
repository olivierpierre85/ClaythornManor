# --------------------------------------------
#   Lad
#           
#   Friday - Arrival/Afternoon
# 
#   18:15 -> 21:00 
#
#   Music: Upbeat
#
#   Position
#       - Tea Room : Everyone else
#       - Host Room : host
#
#   Notes : 
#       - Generic Psychic, 15 minutes
#       - Generic Psychic OR Doctor, 60 minutes
# --------------------------------------------
label lad_day1_afternoon:

    call change_time(18,15, 'Afternoon', 'Friday')
    
    $ current_character.add_checkpoint("lad_day1_afternoon") 
    
    call black_screen_transition("Ted Harring", "Friday Afternoon")

    $ change_room('great_hall', irisout)

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
    
    $ time_left = 15
    
    $ current_menu = TimedMenu([
        TimedMenuChoice('Talk to Samuel Manning', 'lad_day1_drinks_drunk', 5),
        TimedMenuChoice('Talk to Amelia Baxter', 'lad_day1_drinks_psychic', 5), # keep_alive = True, TODO keep alive to allow more choices if leaving by mistakes ?
        ], image_left = "drunk", image_right = "psychic")
    call run_menu(current_menu)

    call change_time(18,30)

    play sound dinner_gong

    """
    What was that? A gong?
    """

    butler """
    Dinner is served. Please follow me to the dining room.
    """

    """
    Oh a gong warns people that dinner is served.

    Rich people live differently that's for sure.
    """

    $ change_room('dining_room')

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

    $ time_left = 60

    $ current_menu = TimedMenu([
        TimedMenuChoice('Talk to Daniel Baldwin', 'lad_day1_afternoon_dinner_doctor'), # SHould they be keep_alive ?
        TimedMenuChoice('Talk to Amelia Baxter', 'lad_day1_afternoon_dinner_psychic')
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


label lad_day1_drinks_psychic:

    """
    I am approaching the middle-aged lady.
    """

    call lad_day1_drinks_psychic_encounter

    call psychic_generic

    return

# Dialog also in psychic side TODO move into global label ?
label lad_day1_drinks_psychic_encounter:

    lad """
    Nice to meet you miss Baxter. I am Ted Haring.
    """

    psychic """
    Nice to meet you mister Haring.
    """

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

label lad_day1_afternoon_dinner_psychic:
    
    lad """
    Hi again Miss Baxter.
    """

    psychic """
    Oh Mister Harring. I am glad we can continue our conversation.
    """

    call psychic_generic
    
    return
    

label lad_day1_afternoon_dinner_doctor:

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