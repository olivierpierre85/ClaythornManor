# --------------------------------------------
#   Psychic
#           
#   Friday - Afternoon
#   
#   15:30 -> 18:30
#
#   Music: Chill, upbeat
#
#   Alive: Everyone
#
#   Notes : 
#       - Generic Lad, 15 minutes
# --------------------------------------------
label psychic_introduction:

    call change_time(15, 30, 'Arrival', 'Friday', hide_minutes=True)

    call black_screen_transition("Amelia Baxter", "Friday Afternoon")

    scene train_inside with irisout 

    play sound train_moving loop

    $ play_music('chill')

    """
    This invitation really isn't well-written.

    Vague instructions on how to reach the manor.

    Little information about who has been invited.

    I guess it wouldn't be surprising if most of the participants didn't come.

    I can't help feeling nervous about the whole thing.

    Well, it's too late to back down now.

    We'll see what happens.
    """

    play sound train_stopping

    scene train_station

    pause 5.0
    
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

    scene inside_car

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
    
    scene manor_exterior

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

    However, the storm that has befallen us gives it a somewhat sinister look.

    Nevertheless, its appearance reassures me.

    Such a house shows that its owner must be incredibly wealthy.

    Now I can finally relax.

    Everything will be fine from now on.
    """

    pause 1.0

    """
    The three of us walk towards the entrance while the driver takes care of our luggage.

    Samuel Manning woke up when the car stopped. He looks somewhat better than earlier.

    When we reach the main door, a butler greets us.
    """

    stop sound

    $ change_room('great_hall', dissolve)
    
    call change_time(16,30, 'Arrival', 'Friday')

    $ play_music('upbeat')

    butler """
    Good afternoon, everyone, and welcome to Claythorn Manor.

    I'm sorry that Lady Claythorn can't greet you herself.

    She is still busy preparing for tonight.

    In the meantime, you can enjoy some drinks in the tea room.

    Or, if you wish to change, I can show you to your room right now.
    """

    drunk """
    I'm good, but I could use a drink.

    Which way is the tea room?
    """

    """
    Amazing. He looked passed-out drunk in the car.
    
    How could he possibly want another drink now?
    """

    butler """
    Very well, sir. You'll find the tea room through the door on your left.

    Other guests who arrived earlier are already settled there.

    You can join them.
    """

    captain """
    I'll come with you.
    """

    butler """
    What about you, Miss ...?
    """

    psychic """
    Miss Baxter.

    I think I'll freshen up in my room first.

    It's been a very long trip.
    """

    butler """
    Of course, please follow me upstairs.
    """

    $ change_room("bedrooms_hallway")

    butler """
    Here we are, Miss.

    The "George III Bedroom."

    I hope it's to your liking.
    """

    $ unlock_map('psychic_room')

    $ change_room('psychic_room')

    """
    He opens my room and lets me in.
    
    At the same time, the driver arrives with my luggage.

    He leaves them there and then excuses himself.
    """

    butler """
    Well, it looks like you're all set.

    Please join us in the dining room when you're ready.
    """

    """
    I nod and take a look at my room.

    It's a bit worn out but still looks great.

    I should be comfortable here.
    """
    
    pause 1.0

    """
    When I'm ready, I head downstairs to the tea room.
    """

    $ change_room("tea_room")

    call change_time(18,15, 'Arrival', 'Friday')

    butler """
    Miss Baxter.

    Almost everyone is here now.
    """

    """
    He quickly introduces me to the people I haven't met yet.
    """

    butler """
    Please make yourself at home.

    Now, if you'll excuse me, I hear the car is back with the last guest.
    """

    """
    He leaves me on my own.

    I glance around the room.

    Almost everyone is gathered around Sushil Sinha.

    He's in the midst of what sounds like another tedious story.

    I'm not eager to listen to that again.

    On a chair, Samuel Manning is sitting alone with a glass in his hand.

    I can't believe it.

    He's asleep again.

    Well, I guess I have no choice but to join the larger group.

    But before I could move, the butler returns.
    """

    butler """
    Mister TED HARRING.
    """

    """
    The butler nearly shouts the name of the new guest.

    He's a good-looking young man, but he looks unsure.

    You can tell that he's not in his natural element here.

    I smile at him and, after some hesitation, comes towards me.
    """

    call lad_day1_drinks_psychic_encounter

    $ time_left = 15

    call lad_generic

    play sound dinner_gong

    butler """
    Dinner is served. Please follow me to the dining room.
    """

    $ stop_music()

    jump psychic_day1_evening
