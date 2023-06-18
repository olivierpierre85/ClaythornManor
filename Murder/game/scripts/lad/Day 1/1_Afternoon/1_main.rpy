# --------------------------------------------
#   Lad
#           
#   Friday - Afternoon
#   
#   17:30 -> 18:30
#
#   Music: Chill
#
#   Alive: Everyone
#
#   Notes : 
#       - Generic Psychic, 15 minutes
# --------------------------------------------
label lad_introduction:

    call black_screen_transition("Ted Harring", "Friday Afternoon")

    call change_time(17,30, 'Afternoon', 'Friday', hide_minutes = True)

    scene train_inside

    play sound train_moving loop

    $ play_music('chill')

    """
    As I approach my destination, I am reading yet another time the letter that made me come on this trip.
    """

    letter """
    September 5th, [current_year]

    Dear Mister Haring,

    I am pleased to announce that you have been selected as one of the recipients of the \"Exceptional Act of Bravery Award\".

    You'll be receiving the prize, along with seven other courageous persons, at a reception organized in your honor. 
    
    As a thank you, a weekend of leisure at Claythorn Manor as been planned for all of you to enjoy.

    After which, a prize money of one thousand pounds in bearers bond will be handed to you.
    
    Please note that your presence is mandatory in order to receive the prize.

    All you have to do is be at the Aberdeen Station, on the 13th of October around 4PM, where someone will drive you to the manor.

    Hoping ,.....
    """

    """
    More thanks and information follows, but that's about the content of it.

    It is signed by Lady Claythorn. 
    
    I've never heard of her.

    I couldn't really believe it at first. 
    
    I don't think I am that deserving. At least no more than hundreds of guys in this country.

    But in the end, no matter the reason, I can't possibly say no to this amount of money.
    
    So I feel like I didn't have much choice.

    But still, there is part of me thinking:

    Maybe I never should have come.
    """

    # TODO intro screen, song ...

    play sound train_stopping

    scene train_station

    pause 5.0
    
    """
    As I step off the train, a man approaches me.
    """

    footman """
    Welcome sir. Are you by any chance, heading to Claythorn Manor?
    """

    lad """
    Yes, as a matter of fact I am.
    """

    """
    As proof, I hand him the letter that I still had in my hands.
    """
    
    footman """
    Very well Sir. I can take your luggage and you can follow me into the car.
    """

    """
    And like that we were on our way.
    """

    scene inside_car

    lad """ 
    So you are lady Claythorn's driver?
    """

    footman """
    Yes, I mean,.. no.

    I am actually her footman. I also drive people when necessary.
    """

    lad """
    Oh. The driver must be busy because of all the people coming I guess.

    Do you know how many people were invited this weekend?
    """

    footman """
    Well, ... I am not sure sir. Half a dozen at least I believe.

    But I am sorry, I must concentrate on the road ahead. Lady Claythorn doesn't like it when I am distracted.
    """

    lad """
    Of course, I am sorry.
    """

    footman """
    No need for apologies Sir.
    """

    """
    Hum, it looks like I have made him uneasy. Maybe he is not supposed to make small talk with guests.

    I feel weird because I'm not used to be treated like. It is usually more the other way around.

    I wonder if I'll manage to blend in with the other folks at the manor.

    They might be more accustomed to this kind of treatment.

    But on the other hand maybe not. Maybe Lady Claythorn gets a kick of helping people like me.

    We'll see.

    After leaving Aberdeen, we are riding into the country side. Then into what looks like a large forest.

    About twenty minutes later, there is no trace of human life at all.

    There is only woods so far as I can see.

    I am a little an uneasy to find it to be so far from every where else.

    And to make matter worse, a look at the sky tells me that a storm is coming. 
    """

    $ stop_music()
    
    play sound thunder loop
    
    scene manor_exterior

    """
    Finally an impressive mansion appears in the horizon.

    It's bigger than any of the houses I've ever see. 

    A big country house. 

    Everyone who is someone in England used to have one.

    Now I've heard a lot of people can't afford them anymore.

    They are sold, turned into hotels, or even abandoned. Left there to rot.
    
    What a shame.

    While the driver is unloading my bag from the car, I walk towards the entrance, where a butler opens the door to greet me.

    I walk into the most impressive hall I ever been in.
    """

    stop sound

    pause 2.0

    call change_time(18,15)

    $ change_room('great_hall', dissolve)

    $ play_music('upbeat')

    butler """
    Welcome Sir.
    """

    lad """
    Hello, I am Ted Harring, I was invited by Lady Claythorn.
    """

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
    
    $ current_menu = TimedMenu("lad_introduction", [
        TimedMenuChoice('Talk to Samuel Manning', 'lad_day1_drinks_drunk', 5),
        TimedMenuChoice('Talk to Amelia Baxter', 'lad_day1_drinks_psychic', 5), # keep_alive = True, TODO keep alive to allow more choices if leaving by mistakes?
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

    $ stop_music()

    jump lad_day1_evening


label lad_day1_drinks_psychic:

    """
    I am approaching the middle-aged lady.
    """

    call lad_day1_drinks_psychic_encounter

    call psychic_generic

    return

# Dialog also in psychic side TODO move into global label?
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
    
    lad "Hello sir, how are you?"

    drunk "(Snore...)"

    "He reeks of booze, and is deep asleep. It's useless talking to him."

    return