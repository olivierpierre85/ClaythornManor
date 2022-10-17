label lad_introduction:
  
    scene train_inside

    #TODO longer introduction? sound?
    """
    As I approach my destination, I am reading yet another time the letter that made me come on this trip.
    """

    letter """

    September 5th, [current_year]

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

    # $ host_details.introduce()

    play sound train_moving

    play music danger_01

    # TODO THEME ANIMATION AND SONG
    # Dramatic music, Start of Theme ?
    # end with 
    # PAUSE
    pause 5.0

    stop music
    scene train_station
    
    "As I step off the train, a man approaches me."

    footman "Welcome sir. Are you by any chance, heading to Claythorn Manor ?"

    lad "Yes, as a matter of fact I am."

    "As proof, I hand him the letter that I still had in my hands."
    
    footman "Very well Sir. I can take your luggage and you can follow me into the car."

    "And like that we were on our way."

    scene inside_car

    lad """ 
    So you are lady Claythorn's driver ?
    """

    footman """
    Yes, I mean,.. no.
    I am actually her footman. But I also drive people when necessary.
    """

    lad """
    Oh. So there is no driver at Claythorn Manor ?
    """

    footman """
    Well, ... not that I know of sir.

    But I am sorry, I must concentrate on the road ahead. Lady Claythorn doesn't like it when I am distracted.
    """

    lad "Of course, I am sorry."

    footman "No need for apologies Sir."

    """
    Hum, it looks like I have made him uneasy. Maybe he is not supposed to make small talk with guests.

    I feel weird because I'm not used to be treated like. It is usually more the other way around.

    I wonder if I'll manage to blend in with the other folks at the manor.

    They might be more accustomed to this kind of treatment.

    But on the other hand maybe not. Maybe Lady Claythorn gets a kick of helping people like me.

    We'll see.

    After leaving Aberdeen, we are riding into the country side. Then into what looks like a large forest.

    About twenty minutes later, there is no trace of human life at all.

    There is only woods so far as I can see.

    I am a little an uneasy to find it to be so far from every where else.

    And to make matter worse, a look at the sky tells me that a storm is coming. 
    """

    jump lad_day1_arrival