# --------------------------------------------
#   Doctor
#           
#   Friday - Evening
# 
#   14:45 -> 23:00
#
#   Music: chill
#
#   Position
#       - Dinner Room : Everyone
#
#   Notes : 
#       - Map visit, 90 minutes
#       - Generic Broken
# --------------------------------------------
label doctor_day1_evening:
    
    call change_time(14, 45, "Evening", "Friday", hide_minutes = True, chapter='friday_evening')

    $ current_character.add_checkpoint("doctor_day1_evening") 

    call black_screen_transition("Daniel Baldwin", chapters_names[current_chapter])

    $ change_room('great_hall', dissolve)

    $ play_music('upbeat')

    """
    We all reach the hall together, leaving the driver to look after our luggage.
    """

    butler """
    Welcome everyone.

    You are the first guest to arrive for this week-end event.

    It's a bit early, so it may take a while before others arrive. In the meantime, let me show you to your rooms.

    You can rest there a bit, there will be drinks later in the tea room.
    """

    doctor """
    Perfect, when should we meet later?
    """

    butler """
    Around four I believe.
    """

    """
    I quickly check my pocket watch.

    That would leave me at least one hour of solitude in my room.
    
    That's perfect.
    """
    
    butler """
    If you don't have any more questions, please follow me upstairs.
    """

    $ change_room('bedroom_doctor', dissolve)

    """
    The butler shows me to my room first.

    I quickly settle in and wait for five minutes for the driver to bring my bag back.

    Now I can finally relax.
    """

    call wait_screen_transition()

    call change_time(15,30)

    play sound door_knock

    footman """
    Doctor Baldwin, the tea room has been set for drinks.

    You can come down if you are ready.
    """

    doctor """
    Very, very well.

    I will be there soon.

    Thank you.
    """

    """
    I am not sure how long I've been out.

    It's better if I hurry downstairs so I do not appear suspicious.
    """

    pause 1.0

    $ change_room('tea_room', dissolve)

    call change_time(15,40)

    """
    Well, it looks like I am the first one. 

    There was no reason to rush.
    """

    butler """
    Doctor Baldwin, would you like a glass of sherry?
    """

    doctor """
    Sure why not, thank you.
    """

    """ 
    As the butler hands me my drink, Thomas Moody enters the room.
    """

    broken """
    Doctor Baldwin, I suppose we are the first ones.
    """
    
    doctor """
    It seems like it.
    """

    $ time_left = 50

    call broken_generic

    if doctor_details.important_choices.is_unlocked('broken_offended'):
        # The Broken is offended, he won't talk to you anymore
        broken """
        Excuse me, I have something to do.
        """

        """
        He goes back to the bar and starts to talk to the butler, leaving me alone in a corner.

        Well that will teach me.
        """

    call change_time(16,30)

    """
    After a while, Miss Marsh enters the room.

    She is followed by a Indian man in an army uniform and an older gentleman.

    They must have just arrived from the station.

    The older man goes straight to the tray with drinks. 
    
    He walks in an unsure fashion, almost bumping into the butler who swiftly avoids him.

    The military man walks towards me.
    """

    captain """
    Hello there, I am Captain Sushil Sinha.
    """

    if doctor_details.important_choices.is_unlocked('broken_offended'):

        """
        As he sees the new guests coming in, Thomas Moody joins me back to greet them.
        """

    broken """
    Nice to meet you captain, I am Thomas Moody.
    """

    doctor """
    Doctor Daniel Baldwin.

    How do you do.
    """

    captain """
    Nice to meet you both.
    """

    broken """
    And who is the gentleman over there?
    """

    captain """
    That would be Samuel Manning.

    I am afraid he had a bit too much to drink.

    But don't worry about him.
    """

    """
    We all glance at him from afar as he fills a water glass to the brim with sherry.

    He then proceeds to chug it in one sip.

    After that, he sits down on the sofa next to him and immediately falls asleep.
    """

    captain """
    Well, that should keep him still for a while.
    """

    doctor """
    Indeed, it's impressive that  ...
    """

    captain """
    It reminds me of a guy I knew back in the Army.

    He was my superior but I swear I never saw him sober.

    Even in the morning he always was still drunk from the day before.

    And...
    """

    """
    He proceeds to tell a tedious story about its time in the military.

    I try to concentrate on what he is saying but I can't focus. 

    So I just nod in agreement and wonder when I will be able to go quietly back to my room.    
    """

    play sound dinner_gong

    """
    I am brutally awoken from my daydreaming by the dinner gong.

    I barely even notice what has happened over the past few hours.

    Everyone is heading towards the dining area, so I go with them.
    """

    $ stop_music()

    call change_time(18,30, 'Dinner', 'Friday')

    $ change_room('dining_room', irisout)

    $ play_music('chill')


    """
    My place is at the end of the table.

    That is better because I don't feel like talking too much.

    Then, the host finally joins us.
    """

    call common_day1_evening_host_welcome_speech

    """
    This speech is quickly followed by the first course.
    """

    pause 1

    """
    I look who I have on my side, it's a young man I didn't even notice before.
    """

    jump work_in_progress