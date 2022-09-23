label lad_introduction:
  
    scene train_inside
    # train sound

    """
    As I approach Aberdeen station, I am reading yet another time the letter that made me come on this whole trip.
    """

    letter """
    Congratulation Mister Haring,

    Due to your recent actions, you have been selected as one of the recipients of the \"Exceptional Act of Bravery Award\".

    This award comes with a price money of two thousand pounds.
    
    You'll be receiving the price along with seven other courageous persons. And you will all be enjoying a weekend of leisure at Claythorne Manor.

    All you have to do is be at the Aberdeen Station, around 4PM, and a driver will pick you up to the place.

    Hoping ,.....

    """

    """
    More detailed information follows, but that's about the content of it.

    TODO Happy and surprised

    Well, I couldn't really say no to this amount of money.
    
    So I feel like I didn't have much choice.

    But still, there is part of me thinking:

    Maybe I never should have come.
    
    """

    # Dramatic music, Start of Theme ?
    # PAUSE

    scene train_station
    
    "As I step off the train, a young man approaches me."

    footman "Welcome sir. Are you by any chance, heading to Claythorne Manor ?"

    lad "Yes, as a matter of fact I am."

    "And for proof, I show him the letter that I still had in my hands."
    
    footman "Very well Sir. I can take your luggage and you can follow me into the car."

    "He then grabs my small luggage and load ti into the boot."

    "I enter the car."

    # TODO sound of car closing

    scene inside_car

    """
    I try to relax, in the car.

    After leaving Aberdeen, we are riding more into the country side. Then into what looks like a large forest.

    After a while we can't see any trace of houses or farms.

    I am an uneasy to find it to be so far from every where else.

    And to make matter worse, a look at the sky tells me that a storm is coming. 

    Finally an impressive mansion appears in the horizon.
    """

    scene manor_exterior
    # TODO Scary music (short), plus thunder

    jump lad_day1_arrival