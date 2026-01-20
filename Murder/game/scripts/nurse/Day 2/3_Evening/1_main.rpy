label nurse_day2_evening:

    call change_time(19,00, 'Evening', 'Saturday', chapter='saturday_evening')

    $ change_room("living_room")

    """
    The hunters return. Loud, dirty, and smelling of gunpowder.
    
    I retreat to the corner, observing.
    """
    
    # Simple evening progression
    
    call change_time(20,00)

    $ change_room("dining_room")

    """
    Dinner again. The atmosphere is tense.
    """

    if nurse_details.threads.is_unlocked('stole_item'):
        """
        I touch the silver spoon in my pocket. A secret talisman.
        """

    """
    I decline the brandy. Alcohol and my condition do not mix.
    """

    nurse """
    I will retire early again. Goodnight, everyone.
    """

    jump nurse_day3_morning
