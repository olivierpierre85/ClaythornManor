label lad_day2_evening:
    call black_screen_transition("Day 2 - Evening") # Good ?
    scene dining_hall # with irisout

    call change_time(18,30)

    call change_floor(1)

    """
    When I enter the dining room, the mood is rather gloom.
    
    There is a lot fewer people than yesterday.

    Daniel Baldwin and Thomas Moody seats are empty.

    And Samuel Manning is not there either. 

    Captain Sinha thought it was better to lock him in his room.

    The poor guy didn't even object.

    I take my usual seat, with only Amalia Baxter next to me now.
    """

    host """
    Now that everyone is here. I want to say how sorry I am for what happened today.

    It's not how I imagine this week-end would be.

    I don't think any of us want more entertainment at this point.

    So tomorrow morning, you'll receive your rewards.
    
    Then we will wait until the police arrives.

    You'll be free to go back home as soon as the officers will say so.

    In the meantime, enjoy your meal.

    Afterwards, drinks will be available in the billiard room like yesterday. 
    """

    """
    The food arrives right after the speech.

    But none of us have much of an appetite.
    """

    psychic """
    So Mister Harring, did you put some though on what we talked about earlier.

    """

    # Answers depending on what he found in the house




    return