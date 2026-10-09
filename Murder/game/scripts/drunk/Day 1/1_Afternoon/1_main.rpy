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

    $ drunk_mode = True

    $ change_room("train_inside_second", irisout)

    show layer master at drunk_wobble_layer

    play sound train_moving loop

    $ play_music('chill')


    #   15:45 Train, third-class carriage
    #       - Baxter and Sinha travel first class, so they never see him on board.
    #       - Still aboard when the train pulls into the station (Aberdeen, per the lad's invitation).

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

    I hesitate for a second.

    Maybe I should keep my wits about me a little while longer.

    But the dark thoughts resurface.

    Anxiety steps in again.

    I put the flask to my lips.

    I still have a little time before we arrive. It will be fine.
    """

    stop sound

    call wait_screen_transition()

    """
    Wait, are we there already?

    I grab my bag and rush out the door.

    I almost fall on the platform, but manage to keep standing.

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

    footman """
    Yes, I do not like it.

    I am not used to driving in such weather.
    """

    drunk """
    Do not worry. I am sure we will be there before the worst of it is upon us.

    But please, tell me about this place we are going to.
    """

    footman """
    Claythorn Manor.

    A grand place, with a rich history.
    """

    drunk """
    Really? What kind of history?
    """

    footman """
    Oh, there is a lot to say.

    But I am sorry, I should focus on the road.

    Lady Claythorn will be happy to tell you all about her house, I am certain.
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

    #   16:15 Manor exterior, storm (psychic_introduction)
    #       - He wakes up when the car stops, looking somewhat better than before.
    #       - The three of them walk to the door while the driver sees to the luggage.
    #       - The butler greets them at the main door.
    #
    #   16:30 Entrance hall (common_day1_evening_second_arrival_part_1 / _part_2, called from captain_day1_evening)
    #       - Butler: Lady Claythorn is busy, drinks are served in the tea room, or he can show them to their rooms.
    #       - drunk: "I'm good, but I could use a drink. Which way is the tea room?"
    #       - The butler points to the tea room on the left. Sinha goes with him, Baxter goes up to freshen up.
    #
    #   After the arrival (for reference)
    #       - 16:45 Tea room: he rushes to the drinks tray, then drifts over to Rosalind Marsh
    #         ("Ah! Samuel Manning, at your... at your service."), misses her hand,
    #         and she makes her excuses. Baldwin, Moody and Sinha talk apart. (nurse/captain_day1_evening)
    #       - 18:15 On the sofa, "rather exhausted", when the butler introduces him to Ted Harring (lad_day1_evening).
    #       - 18:30 drunk_day1_evening opens in the tea room on the dinner gong.
    #
    #   Notes
    #       - Hidden infos this chapter must reveal (unlock_chapters ('drunk', 'friday_afternoon')):
    #         status, age, addict, job, heroic_act.
    #       - 'lie' (feigning drunkenness) only unlocks on Saturday morning, so the sleep
    #         in the car should not be explained as an act yet.
    #       - next_tasks.md: the train is a mess, the story jumps from one place to the next
    #         until he collapses in the tea room.
    # --------------------------------------------

    # TRain arrival

    jump drunk_day1_evening
