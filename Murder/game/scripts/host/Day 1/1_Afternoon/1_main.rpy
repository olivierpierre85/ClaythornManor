# --------------------------------------------
#   Host
#           
#   Friday - Afternoon
#   
#   10:00 -> 16:30
#
#   Music: Elegant, slightly mysterious
#
#   Alive: Everyone
#
# --------------------------------------------
label host_introduction:

    call change_time(10, 0, 'Arrival', 'Friday', hide_minutes=True, chapter='friday_afternoon')

    call black_screen_transition("", "Lady Claythorn")

    $ play_music('chill')

    $ change_room("train_inside_second")

    """
    The journey from London is finally coming to a close.

    After the train, I was picked up.

    I can spot the Manor from afar.

    I wonder what I have set myself into.
    """

    $ change_room("train_station", irisout)

    """
    I have barely stepped out of the coach when he approaches me.
    """

    butler """
    Good, you made it on time.

    Please come this way.
    """

    """
    Without ceremony, he guides me inside a car.
    """

    $ change_room("car_interior", irisout)

    butler """
    All right, from now on you are the lady of this place. Don't forget it.
    """

    host """
    I don't understand why you can't be the lord.

    You will clearly be better at it than I.
    """

    butler """
    You mean because I am the better actor?
    """

    host """
    I didn't say that.

    And you are not.

    But I know you are familiar with that type of house.
    """

    butler """
    Right, I was a footman when I was younger, a very long time ago.

    But that's precisely why I should be the butler.

    You see, in this kind of environment, the staff are scrutinised more than the host.

    That's a rule.

    As the Lady of the house, you can do almost anything.

    At worst you'll be labelled "eccentric".

    But to maintain the illusion, the staff can't afford a mistake.

    That's why I have to be in charge of them.

    Besides, a butler must always be a man.
    """

    host """
    Right. But I've been assured that the guests we are receiving won't be accustomed to all this.

    None of them is from a standing important enough so that they should notice little mistakes with the service.
    """

    butler """
    Maybe so, but the rest of our staff are all actors too.
    
    They have very little domestic experience, if any.

    So we shouldn't take any chances. 
    """

    $ change_room("manor_exterior", irisout)

    """
    We stay silent for the rest of the journey, until finally, I can spot the Manor from afar.

    This is becoming real now.
    
    I feel a knot inside my stomach and wonder what I have set myself into.
    """
    
    butler """
    Alright, the others are already there to prepare the house.
    
    Let us not waste any time.
    """

    $ change_room("entrance_hall")

    """
    Two other people are gathered in the entrance hall.

    A young man, rather dashing, and a girl that looks that she can't be more than 18 years old.
    """

    host """
    Is that everyone?
    """

    butler """
    I am afraid so, it would have been dangerous to bring more people in.
    """

    host """
    Is that enough for a house this size?
    """

    butler """
    Normally no, but for the weekend we will have to make this work.
    """ 

    jump host_day1_evening
