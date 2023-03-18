# --------------------------------------------
#   Doctor
#           
#   Friday - Afternoon
#   
#   14:00 -> 18:30
#
#   Music: Chill, upbeat
#
#   Alive: Everyone
#
#   Notes : 
#       - 
# --------------------------------------------
label doctor_introduction:

    call change_time(14,00, 'Arrival', 'Friday', hide_minutes = True)

    call black_screen_transition("Daniel Baldwin", "Friday Afternoon")

    scene train_inside with irisout 

    play sound train_moving loop

    $ play_music('chill')

    # """
    # I am nervous.

    # More than usual.

    # It's been a while since I've left for this long.

    # I wish I could avoid it but of course I can't.

    # The money promised is too enticing.

    # But it's going to be a challenge.

    # I glance towards of my bag and ponder for a few seconds.

    # I could take the edge of now.

    # But it's a bad idea, I know that.

    # I don't want to make a bad impression.

    # Also I have the feeling I might need to be fully alert this weekend.

    # I know all of this.

    # But in spite of it all, I find myself grabbing my bag and heading to the bathroom.
    # """
    
    # Revised GPT-4 version
    """
    I feel anxious.

    More than I usually do.

    It has been some time since I've been away for this long.

    I wish I could avoid it, but of course, I can't.

    The money offered is too tempting.

    Yet, it's going to be a struggle.

    My gaze shifts to my bag, and I hesitate for a moment.

    I could take the edge off now.

    But it's a terrible idea, and I'm well aware of that.

    I don't want to leave a poor impression.

    Besides, I have a feeling I'll need to be fully alert this weekend.

    I'm conscious of all this.

    Yet, despite it all, I find myself grabbing my bag and heading to the bathroom.
    """

    play sound train_stopping

    """
    The train is stopping.

    Too late for that now.
    """

    scene train_station

    pause 5.0
    
    """
    I gather my things and leave the train.
    """

    pause 1.0

    """
    TODO meet nurse and Broken
    """

    scene inside_car


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

    scene hallway

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


    

