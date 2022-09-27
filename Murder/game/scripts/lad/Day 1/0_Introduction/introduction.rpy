label lad_introduction:
  
    scene train_inside

    """
    As I approach my destination, I am reading yet another time the letter that made me come on this trip.
    """

    letter """

    September 5th, 1924

    Dear Mister Haring,

    I am pleased to announce that you have been selected as one of the recipients of the \"Exceptional Act of Bravery Award\".

    You'll be receiving the prize, along with seven other courageous persons, at a reception organized in your honor. 
    
    As a thank you, a weekend of leisure at Claythorn Manor as been planned for all of you to enjoy.

    After which, a prize money of one thousand pounds will be handed to you.
    
    Please note that your presence is mandatory in order to receive the prize.  

    All you have to do is be at the Aberdeen Station, on the 13th of October around 4PM, where someone will drive you to the manor.

    Hoping ,.....

    """

    """
    More thanks and information follows, but that's about the content of it.

    It is signed by Lady Claythorn. 
    
    I've never heard of her.

    I couldn't really believe it at first. 
    
    I don't think I am that deserving. At least no more than hundreds of guys in this country.

    But in the end, no matter the reason, I can't possibly say no to this amount of money.
    
    So I feel like I didn't have much choice.

    But still, there is part of me thinking:

    Maybe I never should have come.
    
    """

    play sound train_moving # arrival?

    play music intro

    # TODO THEME ANIMATION AND SONG
    # Dramatic music, Start of Theme ?
    # end with 
    # PAUSE
    pause 5.0

    stop music
    scene train_station
    
    "As I step off the train, a young man approaches me."

    footman "Welcome sir. Are you by any chance, heading to Claythorn Manor ?"

    lad "Yes, as a matter of fact I am."

    "As proof, I hand the letter that I still had in my hands to him ."
    
    footman "Very well Sir. I can take your luggage and you can follow me into the car."

    "And like that we were on our way."

    # play sound car_start not great ?
    scene inside_car

    # TODO add real conversation ???? Yes if too short....
    """
    After leaving Aberdeen, we are riding into the country side. Then into what looks like a large forest.

    About twenty minutes later, there is no trace of human life at all.

    There is only woods so far as I can see.

    I am a little an uneasy to find it to be so far from every where else.

    And to make matter worse, a look at the sky tells me that a storm is coming. 

    I tried to talk to the driver. He tells me he is a footman for Lady Claythorn. 
    
    But I can't get anymore from him. Maybe he is not supposed to make small talk with guests.

    I feel weird because I'm not used to be treated like. It is usually more the other way around.

    I wonder if I'll manage to blend in with the other folks at the manor.

    They might be more accustomed to this kind of treatment.

    But on the other hand maybe not. Maybe Lady Claythorn gets a kick of helping people like me.

    We'll see.
    """

    jump lad_day1_arrival