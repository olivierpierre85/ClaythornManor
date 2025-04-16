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
    This invitation really isn't well-written.

    Vague instructions on how to reach the manor.

    Little information about who has been invited.

    I guess it wouldn't be surprising if some of the participants didn't show up.

    I can't help feeling nervous about the whole thing.

    Well, it's too late to back down now.

    We'll see what happens.
    """

    play sound train_stopping

    $ change_room("train_station")

    pause 2.0
    
    """
    I step off the train and look around me.
    """

    pause 1.0

    """
    On the platform, I spot a young man in footman's livery.

    He is talking to a tanned man with a serious look.

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

    Here's someone with manners, at least.
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
    
    Let's wait a few minutes to be sure everyone has left this train, then we can move on.
    """

    """
    As the train prepares to leave the station, I see someone stumbling out of a door, almost falling.

    Since we're the only people left on the platform, he walks towards us, looking uncertain.
    """

    footman """
    Hello, sir. Are you Mr. Manning?
    """

    drunk """ 
    I am indeed.
    """

    footman """
    Perfect, that's everyone who was supposed to be on this train.
    
    You can follow me to the car, and we'll be on our way.

    It should take about an hour to reach the manor.
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

    Samuel Manning seems out of it.

    He tries to make small talk with the driver, but his speech is incoherent.

    The poor lad does his best to ignore him and focus on the road.

    When he realizes no one wants to talk to him, Samuel Manning takes a sip from a flask and immediately falls asleep in his seat.

    The driver sighs in relief.
    """

    captain """
    Well, he's certainly had one too many.

    I hope he can sleep it off.

    It would be embarrassing for our host to greet him in this state.
    """

    psychic """
    You're certainly right.

    I'd rather discuss something else, if you don't mind.
    """

    captain """
    Not at all.
    """

    $ time_left = 6

    call captain_generic

    call change_time(16,15, 'Evening', 'Friday')

    # Arrival to manor
    $ stop_music(3)
    
    play sound thunder loop
    
    $ change_room("manor_exterior")

    """
    After what seems like an eternity, the manor appears on the horizon.

    That finally puts an end to Captain Sinha's speech.
    """

    captain """
    Ah, it looks like we're arriving at our destination.

    What a magnificent home.
    """

    """
    He's right, it is beautiful.

    However, the storm gives it a somewhat sinister look.

    Nevertheless, its appearance reassures me.

    Such a house shows that its owner must be incredibly wealthy.

    Everything should be fine from now on.
    """

    pause 1.0

    """
    The three of us walk towards the entrance while the driver takes care of our luggage.

    Samuel Manning woke up when the car stopped. He looks somewhat better than earlier.

    When we reach the main door, a butler greets us.
    """

    stop sound

    
    jump psychic_day1_evening
