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

    $ change_room("train_inside")

    play sound train_moving loop

    $ play_music('chill')

    """
    As I approach my destination, I am reading yet another time the letter that made me come on this trip.
    """

    letter """
    September 5th, [current_year]

    Dear Mister Harring,

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

    But still, there is part of me thinking,

    Maybe I never should have come.
    """

    play sound train_stopping

    $ change_room("train_station")

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
    Very well Sir. Let me assist you with your luggage and you can follow me into the car.
    """

    """
    And like that we were on our way.
    """

    $ change_room("inside_car")

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
    I seem to have made him uneasy. Maybe he's not used to small talk with guests.

    This feels odd, as I'm usually on the other end of this treatment.

    I wonder how well I'll blend in with the other folks at the manor.

    They might be used to this kind of service.

    But then again, maybe not. Maybe Lady Claythorn likes helping people like me.

    We'll see.

    After leaving Aberdeen, we move into the countryside, then into what seems like a vast forest.

    About twenty minutes later, all signs of human life disappear.

    It's nothing but dense woodland as far as the eye can see.

    The isolation makes me feel a bit uneasy, being so far from everywhere else.

    And the look of an approaching storm in the sky only adds to my discomfort.
    """

    $ stop_music()
    
    play sound thunder loop
    
    $ change_room("manor_exterior")

    """
    Eventually, an imposing mansion emerges on the horizon.

    It's bigger than any house I've ever been in.

    A big country house. 

    Everyone who is someone in England used to have one.

    Now I've heard a lot of people can't afford them anymore.

    They are sold, turned into hotels, or even abandoned. Left there to rot.
    
    What a shame.

    As the driver unloads my luggage from the car, I approach the entrance, where a butler opens the door to welcome me.

    I step into the most remarkable hall I've ever set foot in.
    """

    stop sound fadeout 2.0

    pause 2.0

    call change_time(18,10)

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
    Well, it's not like I have multiple changes of clothes anyway. So, I follow him.
    """

    $ change_room('tea_room')

    """
    As I step into the room, the butler loudly introduces me.
    """

    butler """
    Mister TED HARRING.
    """

    """
    Everyone turns their head towards me.
    
    Some people nod in my direction, while others barely acknowledge my presence.

    From afar, the butler provides me with a brief introduction to each guest.
    """

    show captain at truecenter
    butler """ 
    The older man talking is from India, and his name is Sushil Sinha.
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
    After this introduction, he leaves me and goes to stand in the corner of the room.

    Most of the guests are already engaged in conversation.

    However, Amelia Baxter and Samuel Manning are alone.

    They seem more approachable than the rest.
    """
    
    $ time_left = 20
    
    $ current_menu = TimedMenu("lad_introduction", [
        TimedMenuChoice('Talk to Samuel Manning', 'lad_day1_drinks_drunk', 5),
        TimedMenuChoice('Talk to Amelia Baxter', 'lad_day1_drinks_psychic', 0), # keep_alive = True, TODO keep alive to allow more choices if leaving by mistakes?
        ], image_left = "drunk", image_right = "psychic")
    call run_menu(current_menu)

    call change_time(18,30)

    play sound dinner_gong

    """
    What was that? A gong?
    """

    butler """
    Dinner is served. Please, follow me to the dining room.
    """

    $ stop_music()

    jump lad_day1_evening


label lad_day1_drinks_psychic:

    """
    I am approaching the middle-aged woman.
    """

    call lad_day1_drinks_psychic_encounter

    call psychic_generic

    return

# Dialog also in psychic side TODO move into global label?
label lad_day1_drinks_psychic_encounter:

    lad """
    Nice to meet you, Miss Baxter. I am Ted Harring.
    """

    psychic """
    Nice to meet you, Mr. Harring.
    """

    return

label lad_day1_drinks_drunk:

    """
    I am heading towards the older man.

    He holds a glass of whiskey in his hand. His gaze is empty.
    """
    
    lad """
    Hello sir, how are you?
    """

    drunk """
    (Snore...)
    """

    """
    He reeks of booze, and he is deeply asleep. Talking to him is useless.
    """

    return