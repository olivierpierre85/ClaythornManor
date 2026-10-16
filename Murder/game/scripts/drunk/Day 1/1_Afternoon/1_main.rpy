# --------------------------------------------
#   Drunk
#
#   Friday - Afternoon
#
#   15:45 -> 16:45
#
#   Music: chill
#
#   Alive: Everyone
#
# --------------------------------------------
label drunk_introduction:

    call change_time(15, 45, 'Arrival', 'Friday', hide_minutes=True, chapter='friday_afternoon')

    $ drunk_details.add_checkpoint("drunk_introduction")

    call black_screen_transition("", "Samuel Manning")

    $ change_room("train_inside_second", irisout)

    $ set_drunk_mode(1) 

    play sound train_moving loop

    $ play_music('chill')

    inspector """
    Excuse me, sir. May I see your ticket, please?
    """

    drunk """
    Hm, sorry, what?

    Where am I?
    """

    inspector """
    We are in Scotland now.

    We passed Dundee a few moments ago.
    """

    drunk """
    In Scotland, right, of course.
    """

    inspector """
    May I see your ticket now, please, sir?
    """

    drunk """
    My ticket?

    Yes, yes.

    It is in my pocket, I think.

    Ah, there it is.

    Here you are.
    """

    inspector """
    Thank you.

    I see you are getting off at Aberdeen. It is the next stop.

    We should arrive there soon, so be ready.
    """

    drunk """
    Yes, thank you, sir.
    """

    """
    Ready? To step off a train?

    Even I can manage that, surely.

    I look around me and notice I am alone in the compartment.

    Good.

    My hand reaches into my jacket and grasps my flask.

    I still have a little time before we arrive.

    Without even thinking about it, I put the flask to my lips.
    """

    stop sound

    call wait_screen_transition()

    """
    Wait, are we there already?

    I grab my bag and rush out of the door.

    I almost fall onto the platform, but manage to keep my footing.

    The platform is already emptying.

    There is a group of people still waiting, so I go to them.
    """

    $ change_room("train_station")

    call common_day1_afternoon_station_drunk

    """
    I look at my fellow travellers.

    A middle-aged lady and an Indian fellow.

    They keep talking amongst themselves and let me sit in the front.

    I happily oblige.
    """

    $ change_room("inside_car")

    drunk """
    So, it looks like a storm is coming our way.
    """

    """
    The driver gives me a strange look.
    """

    drunk """
    Do not worry. I am sure we will be there before the worst of it is upon us.

    But please, tell me about this place we are going to.
    """

    footman """
    I am really sorry, sir.

    I should focus on the road.
    """

    drunk """
    Right.
    """

    """
    This man is not the talking type, it seems.

    I glance at the back seat, but the other passengers avoid my gaze.

    Well, there is not much to do for the next hour.

    So be it, then.
    """

    call wait_screen_transition()

    call change_time(16,15, 'Evening', 'Friday')

    # Arrival to manor
    $ stop_music(3)
    
    play sound thunder loop
    
    $ change_room("manor_exterior_storm")
    
    """
    I am woken by thunder.

    In front of me stands Claythorn Manor, even more impressive than I imagined.

    Well, the weekend should be comfortable, at least.

    The car pulls up in the driveway.

    I grab my luggage and head to the entrance.
    """

    jump drunk_day1_evening
