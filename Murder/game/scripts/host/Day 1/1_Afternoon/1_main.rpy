# --------------------------------------------
#   Host
#           
#   Friday - Afternoon
#   
#   14:00 -> 16:30
#
#   Music: Elegant, slightly mysterious
#
#   Alive: Everyone
#
# --------------------------------------------
label host_introduction:

    call change_time(10, 0, 'Arrival', 'Friday', hide_minutes=True, chapter='friday_afternoon')

    call black_screen_transition("", "Lady Claythorn")

    $ change_room("manor_exterior", irisout)

    # play sound car_engine_stop

    # $ play_music('elegant')

    butler """
    Al right, from now on you are the lady of this place. Don't forget it.
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

    You see, in this kind of environment, the staff is more scrutinize that than the host.

    That's a rule.

    As the Lady of the house, you can do almost anything.

    At worst you'll be labelled "eccentric".

    But to maintain the illusion, the staff can't afford a mistake.

    That's why I have to be in charge of them.

    Besides, a butler must always be a man.
    """

    host """
    Right.
    """

    butler """
    But let's go in, the rest of our staff arrived yesterday to prepare the house.

    Now it's time to explain what's expected of them.
    """

    """
    The "Staff", are actually all actors, some with very little domestic experience, if any.

    But I've been assured that the guests we are receiving won't be accustomed to all this.

    None of them is from a standing important enough so that they should notice little mistakes with the service.

    Still, that would an incredible feat if the weekend goes as planned.
    """

    # $ stop_music()

    jump host_day1_evening
