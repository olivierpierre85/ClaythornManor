# --------------------------------------------
#   Lad
#           
#   Friday - Afternoon
#   
#   17:30 -> 18:10
#
#   Music: Chill
#
#   Alive: Everyone
#
#   Notes : 
#       
# --------------------------------------------

label lad_introduction:

    call change_time(17,30, 'Afternoon', 'Friday', hide_minutes = True, chapter='friday_afternoon')

    call black_screen_transition("", "Ted Harring")

    $ change_room("train_inside")

    play sound train_moving loop

    $ play_music('chill')

    """
    As I approach my destination, I read the letter that has brought me on this trip for the tenth time.
    """

    letter """
    5th September, [current_year]

    Dear Mister Harring,

    I am pleased to announce that you have been selected as one of the recipients of the "Exceptional Act of Bravery Award".

    You'll be receiving the prize, along with six other courageous individuals, at a reception organised in your honour. 
    
    As a thank you, a weekend of leisure at Claythorn Manor has been planned for all of you to enjoy.

    After which, a prize money of one thousand pounds in bearer's bond will be handed to you.
    
    Please note that your presence is mandatory in order to receive the prize.

    All you have to do is be at Aberdeen Station, on the 13th of October around 4PM, where someone will drive you to the manor.

    Hoping ,.....
    """

    """
    More information follows, but that's about the content of it.

    It is signed by "Lady Claythorn". 
    
    I've never heard of her.

    I couldn't really believe it at first. 
    
    I don't think I am that deserving. At least no more than hundreds of other guys in this country.

    But no matter the reason, I can't possibly say no to this amount of money.
    
    So I feel as if I do not have much choice.

    But still, there is part of me thinking,

    Maybe I never should have come.
    """

    play sound train_stopping

    $ change_room("train_station")

    pause 2.0
    
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
    As proof, I hand him the letter that I still have in my hand.
    """
    
    footman """
    Very well Sir. Let me assist you with your luggage and you can follow me into the car.
    """

    """
    And just like that, we are on our way.
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

    Do you know how many people have been invited this weekend?
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

    After we leave Aberdeen, we move into the countryside, then into what seems like a vast forest.

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

    Everyone who was anyone in England used to have one.

    Now I've heard a lot of people can't afford them anymore.

    They are sold, turned into hotels, or even abandoned. Left there to rot.
    
    What a shame.

    As the driver unloads my luggage from the car, I approach the entrance, where a butler opens the door to welcome me.

    I step into the most remarkable hall I've ever set foot in.
    """

    stop sound fadeout 2.0

    pause 2.0

    jump lad_day1_evening