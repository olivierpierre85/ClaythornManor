# --------------------------------------------
#               Amelia Baxter
#           Friday 16:30 Arrival
#
#  Alive: Everyone
# --------------------------------------------
label psychic_day1_arrival:

    $ psychic_details.add_checkpoint("psychic_day1_arrival") 
    
    call black_screen_transition("Amelia Baxter", "Friday")

    $ change_room('great_hall', irisout)
    
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
    What about you miss ... ?
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

    $ time_left = 20

    call lad_generic

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

    jump psychic_day1_dinner


    

