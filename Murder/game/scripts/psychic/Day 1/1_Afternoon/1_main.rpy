# --------------------------------------------
#   Psychic
#           
#   Friday - Afternoon
#   
#   15:30 -> 16:30
#
#   Music: Chill, upbeat
#
#   Alive: Everyone
#
# --------------------------------------------
label psychic_introduction:

    call change_time(15, 30, 'Arrival', 'Friday', hide_minutes=True, chapter='friday_afternoon')

    call black_screen_transition("", "Amelia Baxter")

    $ change_room("train_inside", irisout)

    play sound train_moving loop

    $ play_music('chill')

    """
    This invitation really isn't well written.

    Vague instructions on how to reach the manor.

    There's little information about who has been invited.

    I suppose it wouldn't be surprising if some of the participants did not show up.

    I cannot help feeling nervous about the whole thing.

    Well, it's too late to turn back now.

    We shall see what happens.
    """

    play sound train_stopping

    $ change_room("train_station")

    pause 2.0
    
    """
    I step off the train and look around me.
    """

    pause 1.0

    """
    On the platform, I spot a young man in a footman's livery.

    He is talking to a tanned man with a serious expression.

    I walk towards them.
    """

    psychic """
    Excuse me, gentlemen. I'm heading to Claythorn Manor and was wondering if you could assist me.
    """

    footman """
    Yes, of course. You must be Amelia Baxter.
    """

    psychic """
    That's correct.
    """

    footman """
    Perfect. I work for Lady Claythorn and have been instructed to take you to the manor.
    
    The gentleman here is also coming with us.
    """

    captain """
    Nice to meet you, Miss Baxter.
    """

    """
    He takes my hand and kisses it lightly.

    At least here's someone with manners.
    """

    psychic """
    How do you do, Mister ...
    """

    captain """
    Sinha, Sushil Sinha.
    """

    psychic """
    Ah.
    
    Nice to meet you too, Mr. Sinha.
    """

    footman """
    I believe there's still someone on this train who is supposed to accompany us.

    A Mr. Manning.

    Have either of you met him by any chance?
    """

    captain """
    I don't think so.
    """

    psychic """
    Me neither.
    """

    footman """
    Alright, maybe he missed it. 
    
    Let us wait a few minutes to be sure everyone has left this train, then we can move on.
    """

    """
    As the train prepares to leave the station, I see someone stumbling out of a door, almost falling.

    Since we're the only people left on the platform, he walks towards us, looking uncertain.
    """

    footman """
    Hello, sir. Are you going to Claythorn Manor?
    """

    drunk """ 
    I am indeed.
    """

    footman """
    Perfect, that should be everyone.
    
    You can follow me to the car, and we'll be on our way.

    It will take about an hour to reach the manor.
    """

    $ change_room("inside_car")

    """
    I take a seat in the back.

    Sushil Sinha joins me.
    """

    captain """
    I hope you don't mind my sitting with you.

    I think it's better to let Mr. Manning sit in front.
    """

    psychic """
    Of course not.
    """

    """
    I understand all too well what he means.

    Samuel Manning seems quite out of sorts.

    He attempts to make small talk with the driver, but his speech is incoherent.

    The poor fellow does his best to ignore him and focus on the road.

    When he realises no one wishes to talk to him, Samuel Manning takes a sip from a flask and immediately falls asleep in his seat.

    The driver sighs with relief.
    """

    captain """
    Well, he's certainly had one too many.

    I hope he can sleep it off.

    It would be embarrassing for our host to greet him in this state.
    """

    psychic """
    You are certainly right.

    I would rather discuss something else, if you do not mind.
    """

    captain """
    Not at all.
    """

    $ time_left = 1 
    call run_menu( TimedMenu("psychic_captain_origin_1", [
        TimedMenuChoice('Where are you from?', 'captain_generic_origin_psychic_1', early_exit=True),
        ], image_right = "captain")
    )

    call change_time(16,00)

    $ time_left = 1 
    call run_menu( TimedMenu("psychic_captain_origin_2", [
        TimedMenuChoice('I mean, where are you "Really" from?', 'captain_generic_origin_psychic_2', early_exit=True),
        ], image_right = "captain")
    )

    call change_time(16,15, 'Evening', 'Friday')

    # Arrival to manor
    $ stop_music(3)
    
    play sound thunder loop
    
    $ change_room("manor_exterior")

    """
    After what seems an eternity, the manor appears on the horizon.

    That finally puts an end to Captain Sinha's monologue.
    """

    captain """
    Ah, it looks like we're arriving at our destination.

    What a magnificent home.
    """

    """
    He's right, it is beautiful.

    However, the storm lends it a somewhat sinister aspect.

    Nevertheless, its appearance reassures me somewhat.

    Such a house suggests its owner must be incredibly wealthy.

    Everything ought to be fine from now on.
    """

    pause 1.0

    """
    The three of us walk towards the entrance while the driver attends to our luggage.

    Samuel Manning wakes up when the car stops. He looks somewhat better than before.

    When we reach the main door, a butler greets us.
    """

    stop sound

    
    jump psychic_day1_evening
