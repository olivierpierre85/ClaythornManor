label lad_introduction:
  
    scene train_inside
    play sound train_moving

    """
    As I approach Aberdeen station, I am reading yet another time the letter that made me come on this whole trip.
    """

    letter """

    September 5th, 1924

    Mister Haring,

    I am pleased to announce that you have been selected as one of the recipients of the \"Exceptional Act of Bravery Award\".

    You'll be receiving the price, along with seven other courageous persons, at a reception organized in your honor. 
    
    As a thank you, a weekend of leisure at Claythorne Manor as been planned for all of you to enjoy.

    After which, a price money of two thousand pounds will be handed to you.
    
    It is mandatory to be present in person in order to receive this prize.  

    All you have to do is be at the Aberdeen Station, on the 13th of October around 4PM, where someone will drive you to the manor.

    Hoping ,.....

    """

    """
    More thanks and information follows, but that's about the content of it.

    I couldn't really believe it at first. I don't think I am that deserving. 
    At least no more than hundreds of guys in this country.

    But in the end, no matter the reason, I can't possibly say no to this amount of money.
    
    So I feel like I didn't have much choice.

    But still, there is part of me thinking:

    Maybe I never should have come.
    
    """

    # TODO THEME ANIMATION AND SONG
    # Dramatic music, Start of Theme ?
    # PAUSE

    scene train_station
    
    "As I step off the train, a young man approaches me."

    footman "Welcome sir. Are you by any chance, heading to Claythorne Manor ?"

    lad "Yes, as a matter of fact I am."

    "As proof, I show him the letter that I still had in my hands."
    
    footman "Very well Sir. I can take your luggage and you can follow me into the car."

    "He then grabs my small luggage and load it into the boot of the car."

    # TODO sound of car closing

    scene inside_car

    """
    I try to relax, in the car.

    After leaving Aberdeen, we are riding more into the country side. Then into what looks like a large forest.

    After a while we can't see any trace of houses or farms.

    I am an uneasy to find it to be so far from every where else.

    And to make matter worse, a look at the sky tells me that a storm is coming. 

    Finally an impressive mansion appears in the horizon.

    TODO DESCRIBE THE MANOR
    """

    scene manor_exterior
    # TODO Scary music (short), plus thunder

    jump lad_day1_arrival