# Introduction for hero
label lad_day1_arrival:

    play sound thunder loop
    scene manor_exterior

    """
    Finally an impressive mansion appears in the horizon.

    It's bigger than any of the houses I've seen in London. 

    A big country house. 

    Everyone who is someone in England used to have one.

    Now I've heard a lot of people can't afford them anymore.

    They are sold, turned into hotels, or even abandoned. Left there to rot.

    While I can barely afford to pay rent for my miserable place.
    
    What a shame.

    While the driver is unloading my bag from the car, I walk towards the entrance, where a butler opens the door to greet me.

    I walk into the most impressive hall I ever been in.
    
    """

    stop sound

    scene great_hall
    
    call change_time(17,30)

    butler """

    Good afternoon Sir.

    """

    lad "Hello, I am Ted Harring, I was invited by Lady Claythorn."

    $ lad_details.introduce()

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

    jump lad_day1_drinks