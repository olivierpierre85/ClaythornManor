label captain_introduction:

    $ captain_details.add_checkpoint("captain_introduction") 
    
    call change_time(17,00, 'Evening', 'Friday', hide_minutes = True)

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
    As soon as the train stops, I am on the platform.

    I scan the few people waiting there and quickly notice there is only one servant there.

    If Lady Claythorn is well-organized, he must be there for me.

    I reached him before he saw me.
    """

    captain """
    Excuse me, young man. 
    
    Are you working for Lady Claythorn?
    """

    footman """
    Indeed, I am. You must be ...
    """

    captain """
    Sushil Sinha. Retired captain.
    """

    footman """
    Of course, I've been expecting you, captain.

    There are a few more people on this train who are also guests of Lady Claythorn...
    """

    captain """
    Of course, I'll wait for them.
    """

    """
    After a while, an older lady named Amelia Baxter joins us.

    Then, an inebriated gentleman erupts from the train at the last minute.

    I am surprised that he is also a guest.

    When we reach the car, I quickly sit with Miss Baxter.
    """

    scene inside_car

    """
    The drunk quickly falls asleep.

    So, I have only the older lady to make conversation with.

    She asked me a few questions. Some of them have a tinge of racism to them.

    Sadly, it's something I am too familiar with, so I say nothing.

    No matter how I feel, I have learned it's better to stay polite.

    But to avoid another inappropriate question, I decide to monopolize the conversation while we stay in the car.

    Let's see how she likes being forced to listen to something she doesn't want to.
    """

    jump work_in_progress


