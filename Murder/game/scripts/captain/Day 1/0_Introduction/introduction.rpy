label captain_introduction:

    $ captain_details.add_checkpoint("captain_introduction") 
    
    call change_time(17,00, 'Evening', 'Friday')

    scene train_inside

    play sound train_moving loop

    $ play_music('chill')

    """
    TODO intro captain
    """

    play sound train_stopping

    scene train_station

    pause 5.0
    
    """
    As soon as the train stops I am on the platform.

    I scan the few people waiting there and quickly notice there is only one servant there.

    If Lady Claythorn is well organized, he must be there for me.

    I reached him before he saw me.
    """

    captain """
    Excuse me young man. 
    
    How you working for Lady Claythorn?
    """

    footman """
    Indeed I am. You must be ...
    """

    captain """
    Sushil Sinha. Retired captain.
    """

    footman """
    Of course. I've been expecting you captain.

    There are a few more people on this train that our also guest of Lady Claythorn...
    """

    captain """
    Of course, I'll wait for them.
    """

    """
    After a while an older lady joins me.

    Then inebriated gentleman erupts from the train at the last minute.

    I am surprised that is also a guest.

    When we reach the car, I quickly sit with the older Lady to avoid an accident.

    Then we left.
    """

    scene inside_car

    """
    The drunk quickly falls asleep.

    So I have only the older lady to make conversation with.

    She asked me a few questions, some of them borderline racist.

    It would be impolite not to ask something in return.
    """

    $ time_left = 30

    call psychic_generic

