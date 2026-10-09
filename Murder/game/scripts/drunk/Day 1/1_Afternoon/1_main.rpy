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
    Sir, excuse me, can I see your ticket please?
    """

    drunk """
    hum, sorry what?

    Where am I ?
    """

    inspector """
    We are in Scotland now.

    We just passed Dundee a few moments ago.
    """

    drunk """
    In Scotland, right, of course.
    """

    inspector """
    May I see your ticket now Sir please?
    """

    drunk """
    My ticket?

    Yes yes,

    It is in my pocket I think.

    Ah there is is.

    Here you are.
    """

    inspector """
    Thank you.

    I see you are getting off at aberdeen, it is the next stop.

    We should arrive there soon, so be ready.
    """

    drunk """
    Yes, thank you sir.
    """

    """
    Ready? To step off a train?

    Even I can manage that, no worries about it.

    I look around me and notice I am alone in the compartment.

    Good.

    My hand reach into my jacket and grasp my flask.

    I still have a bit of time before arriving, it will be fine.

    I put the flask to my lisp, then back in my pocket.
    """

    play sound train_stopping

    call wait_screen_transition()

    """
    Wait are we there already?

    I grab my bag and rush out the door.
    """

    $ change_room("train_station")

    #   Platform (psychic_introduction, captain_introduction)
    #       - Sinha is first off and finds the footman, then Baxter joins them.
    #       - The footman asks after "a Mr Manning". Neither of them has met him, so they wait for the train to empty.
    #       - As the train is about to leave, he stumbles out of a door, almost falling
    #         ("an inebriated gentleman erupts from the train at the last minute").
    #       - The three of them are the only ones left on the platform. He walks over, looking uncertain.
    #       - footman: "Hello, sir. Are you going to Claythorn Manor?" / drunk: "I am indeed."
    #       - The footman announces about an hour's drive to the manor.
    #       - He does not recognise Amelia Baxter (that only comes back on Sunday, 'lost_case').
    #
    #   ~16:00 Car (inside_car) (psychic_introduction, captain_introduction)
    #       - Sinha joins Baxter in the back ("better to let Mr Manning sit in front"),
    #         so he rides up front beside the footman, who is driving.
    #       - He tries to make small talk with the driver, but his speech is incoherent.
    #         The driver ignores him and keeps his eyes on the road.
    #       - When he realises no one wishes to talk to him, he takes a sip from his flask
    #         and falls asleep at once. The driver sighs with relief.
    #       - Behind him, Sinha says he has had one too many, then monopolises the
    #         conversation with Baxter for the rest of the drive.
    #
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
