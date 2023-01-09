label psychic_introduction:

    $ psychic_details.add_checkpoint("psychic_introduction") 
    
    call change_time(17,00, 'Evening', 'Friday')

    scene train_inside

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
    Yes of course. You must be Miss Baxter.
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