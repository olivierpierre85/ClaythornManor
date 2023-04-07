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

    call change_time(15,30, 'Arrival', 'Friday', hide_minutes = True)

    call black_screen_transition("Amelia Baxter", "Friday Afternoon")

    scene train_inside with irisout 

    play sound train_moving loop

    $ play_music('chill')

    """
    I still can't believe I had to book the train ticket myself.

    This invitation is really not what I would have expected.

    Vague indications on how to reach the manor.

    Not much information about the participants.

    I wouldn't be surprised if there was nobody at the train station.

    It could be just an elaborate prank.

    And with my luck, there won't be an other train until tomorrow.

    So I will have to spend the night here.

    What a waste of time that would be.

    Well, we'll see.
    """

    play sound train_stopping

    scene train_station

    pause 5.0
    
    """
    I step of the train and try to look for someone who could help me.
    """

    pause 1.0

    """
    On the platform, I spot a young man in a footman livery.

    He is talking to a tanned man with a serious look.

    I walk towards them.
    """

    psychic """
    Excuse me gentlemen. I am heading to Claythorn Manor, and I was wondering if you could help me.
    """

    footman """
    Yes of course. You must be Amelia Baxter.
    """

    psychic """
    That's correct.
    """

    footman """
    Perfect. I work for Lady Claythorn and I have been instructed to take you to the manor.
    
    The gentleman here is also coming with us.
    """

    captain """
    Nice to meet you miss Baxter.
    """

    """
    He takes my hand and kiss it lightly.

    Here's someone with manner at least.
    """

    psychic """
    How do you do mister ...
    """

    captain """
    Sinha, Sushil Sinha.
    """

    psychic """
    Oh.
    
    Nice to meet you too mister... sir.
    """

    footman """
    I believe there is still someone on this train who should accompany us.

    A mister Manning.

    You haven't met him by any chance?
    """

    captain """
    I don't think so.
    """

    psychic """
    Me neither.
    """

    footman """
    Alright, maybe he missed it. 
    
    Let's wait a few minutes to be sure everyone has left this train, then  we can move on.
    """

    """
    As the train was ready to leave the station, I saw someone stumbling through a door, almost falling.

    Since we are the only persons left on the platform, he walks towards us, unsure. 
    """

    footman """
    Hello sir. Are you Mister Manning?
    """

    drunk """ 
    I am indeed.
    """

    footman """
    Perfect, that's everyone who was supposed to be on this train.
    
    You can follow me to the car and we will be on our way.

    It should be about an hour to reach the manor.
    """

    scene inside_car

    """
    I took a seat on the back.

    Sushil Sinha joins me.
    """

    captain """
    I hope you don't mind if I seat with you.

    I think it is better to let mister Manning sitting in front.
    """

    psychic """
    Of course.
    """

    """
    I understand too well what he means.

    Samuel Manning seems to be out of it.

    He tries to make small talk with the driver, but his speech is incoherent.

    The poor lad tries his best to ignore him and to focus on the road.

    When he realizes nobody wants to talk with him, Samuel Manning took a sip of a flask and instantly falls asleep on his seat.

    The driver sigh in relief.
    """

    captain """
    Well, he certainly had one too many.

    I hope he can sleep it off.

    It would be shameful if our host greets him in this state.
    """

    psychic """
    You are certainly right.

    But enough about him.

    I would rather talk about something else if you don't mind.
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
    After what seems to be an eternity, a impressive manor appears on the horizon.

    That finally put an end to Captain Sinha speech.
    """

    captain """
    Oh, it looks like we are arriving at our destination.

    What a magnificent home.
    """


    """
    He is right, it it beautiful.

    But the storm that has fallen upon us gave it something of a sinister look.

    Nevertheless, it's appearance reassures me.

    With such a house, our host has to be someone really wealthy.

    Now I can finally relax. Everything will be fine here.
    """

    pause 1.0

    """
    The three of us walked towards the entrance while the drive takes care our luggage.

    Samuel Manning woke when the car stopped. He looks a tad better than earlier.

    When we reach the main door, a butler greets us.
    """

    stop sound


    $ change_room('great_hall', dissolve)
    
    call change_time(16,30, 'Arrival', 'Friday')

    $ play_music('upbeat')

    butler """
    Good afternoon everyone and welcome to Claythorn Manor.

    I am sorry that Lady Claythorn can't greet you herself.

    She is still busy getting ready for tonight.

    In the meantime, you can enjoy some drinks in the tea room.

    Or, if you wish to change, I can show you to your room right now.
    """

    drunk """
    I am good. But I could use a drink.

    Which way is the tea room?
    """

    """
    Amazing, he looked passed out drunk in the car.
    
    How can he possibly want another drink now?
    """

    butler """
    Very well mister, you'll find the tea room on the door to your left.

    Other guests who arrived earlier are already settled there.

    You can join them.
    """

    captain """
    I'll come with you.
    """

    butler """
    What about you miss ...?
    """

    psychic """
    Miss Baxter.

    I think I'll refresh a bit in my room first.

    It has been a very long trip.
    """

    butler """
    Of course, please follow me upstairs.
    """

    $ change_room("bedrooms_hallway")

    butler """
    Here we are Miss.

    The \"George III Bedroom\".

    I hope it is to your liking.
    """

    $ unlock_map('psychic_room')

    $ change_room('psychic_room')

    """
    He opens my room and lets me in.
    
    At the same time, the driver arrives with my luggage.

    He leaves them there then excuse himself.
    """

    butler """
    Well it looks like you are all set.

    Please join us in the dining room when you are ready.
    """

    """
    I nod and take a look at my room.

    It's a bit worn out but still looks great.

    I should be fine there.
    """
    pause 1.0

    """
    When I am ready, I head downstairs for the tea room.
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

    Now if you'll excuse me, I heard the car is back with the last guest.
    """

    """
    He leaves me on my own.

    I take a look around the room.

    Almost everyone is gathered around Sushil Sinha.

    He is in the middle of what sounds like another tedious story.

    I am not eager to listen to that again.

    On a chair Samuel Manning is sitting alone with a glass on his hand.

    I can't believe it.

    He is asleep again.

    Well, I guess I have no choice but to join the large group.

    But before I could move the butler is back.
    """

    butler """
    Mister TED HARRING.
    """

    """
    The butler almost shouted the new guest name.

    A good looking young man.

    He looks unsure.

    You can tell by his clothes alone that he is not in his natural element here.

    After some hesitation, he comes towards me.
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


    

