label captain_introduction:

    $ captain_details.add_checkpoint("captain_introduction") 
    
    call change_time(17, 00, 'Evening', 'Friday', hide_minutes = True)

    $ change_room("train_inside")

    play sound train_moving loop

    $ play_music('chill')

    """
    I don't like it.

    I don't like it one bit.

    I am committing fraud, that's the only way to put it.

    I don't understand where Lady Claythorn got the idea of this "heroic action" of mine.

    She most certainly mistook me for another Indian soldier.

    God knows it wouldn't be the first time.

    Yet, her invitation was so vague it could still apply to me.

    I look at it again, mostly trying to convince myself.
    """

    letter """
    "... as a thank you for all the lives you saved during the war, I would ..."
    """

    """
    Yet, I am sure I saved lives...

    ... technically.

    Many soldiers died because they didn't receive their rations on time.

    Or because they didn't have the proper winter clothing.

    But I know that can't be what she meant.

    Well, it's too late now.

    I don't have any choice but to act the part.
    
    I should be forthright, authoritative, and act as if I am used to leading dozens of men to their deaths.

    How hard could that be?
    """

    play sound train_stopping

    $ change_room("train_station")

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

    $ change_room("inside_car")

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


