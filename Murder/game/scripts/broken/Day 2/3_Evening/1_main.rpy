# --------------------------------------------
#   Broken
#
#   Saturday - Evening (after the hunt)
#
#   15:00 -> 23:00
#
#   Music: chill, mysterious, sad, scary
#
#   Position
#       - House : Lady Claythorn, Captain, Doctor, Mr Manning, Miss Baxter, Miss Marsh, Broken (+ staff)
#       - Dead  : Lad (Ted Harring)
# --------------------------------------------
label broken_day2_evening:

    $ broken_details.add_checkpoint("broken_day2_evening")

    call change_time(15, 00, 'Evening', 'Saturday', chapter='saturday_evening')

    call black_screen_transition("Thomas Moody", chapters_names[current_chapter])

    $ play_music('chill', 2)

    $ change_room('entrance_hall', dissolve)

    """
    We come back to the manor, exhausted and and quiet.

    The butler takes our rifle back to the gun room.

    He looks distraught for some reason.

    Miss Baxter and Miss Marsh are in the hall to meet us.
    """

    psychic """
    Welcome back, how was the hunt?
    """

    captain """
    We had a nice day out in the woods, but sadly we are coming back empty handed.
    """

    host """
    These things happen captain.
    
    No need to worry, we didn't rely on this hunt for our dinner tonight.
    """

    captain """
    Of course, I did not want to imply we were, I am sure the dinner will be lovely.
    """

    broken """
    By the way, has the police arrived yet?
    """

    nurse """
    No, nobody came yet.

    But they should arrive soon.
    """

    host """
    I am sure they will.
    
    In the meantime, we can all take the opportunity to go get change.

    We can rejoin for dinner at the usual time.
    """

    $ change_room('bedroom_broken', dissolve)

    call change_time(17, 00)

    """
    I return to my room to change, and take the opportunity of the alone time to think.

    I am still not sure what is happening here.

    All I know is that this whole event is a lie, but cannot figure what it's ultimate goal.

    But the letters left for Thomas and Samuel Manning leave no doubt.

    We are all in danger here. 

    Maybe I should stop treating this like a story, and run while I still have the time.

    I really hope the police will arrive soon, and put an end to this madness.

    The police.
    
    A though occurs to me, am I really sure they will come?

    The host didn't seem surprised they were not there yet.

    But I would assume that when a unnatural death is reported, they would come at once.

    And I know that Lady Claythorn is lying and hiding something.

    She is obviously very suspicious here, I shouldn't trust whatever she said.

    So maybe I should check myself. 
    
    The phone is the entrance hall, I should try it as soon as I have the opportunity.

    I sit on my bed, and try to think of what I should do.
    """

    call change_time(18, 30)

    play sound dinner_gong

    """
    I am still deep in my thoughts when the gong rings.
    """


    $ change_room('dining_room', irisout)

    $ play_music('sad', 2)

    """
    We all take our usual seats around the dining table.

    I glance at Ted Harring empty chair, and think it could have been worse had not intervene with Samuel Manning.

    Lady Claythorn rises to address us.
    """

    host """
    Now that everyone is here, I want to express my deepest regret for what happened this morning.

    This isn't how I imagined our weekend.

    Neverthless, I hope you enjoyed today's activities.

    Tomorrow, if the weather allows it, a game of croquet will be held in the garden, followed by an outdoor lunch.

    Afterwards, you'll receive your rewards, then you will be free to return home.

    For now, enjoy your dinner.

    Drinks will be available in the billiard room afterwards, as they were yesterday.
    """

    broken """
    Excuse me Lady Claythorn, if I may, can I ask if you received news from the police?
    """

    host """
    Right, we phoned to the police station moments ago.

    I am afraid they won't be coming today.
    """

    captain """
    What!? Why not?
    """

    host """
    They were on their way but encountered a huge tree blocking the road.
    
    They couldn't get past it.
    
    They said they'll be back tomorrow with assistance.

    But you should not worry, I am sure everything will be sorted tomorrow morning.
    """

    """
    The police won't come, as I feared.

    One more reason to be cautious today.

    The dinner comes quickly after that.

    Everyone is rather quiet and I do not feel like talking either.

    But if I keep quiet, it could be seen as rude, or even suspicious.
    """

    call change_time(19, 30)

    $ time_left = 90

    call run_menu(TimedMenu("broken_day2_evening_menu_dinner", [
        TimedMenuChoice("Speak to Lady Claythorn", 'broken_day2_dinner_host', early_exit=True),
        TimedMenuChoice("Keep my own counsel", 'generic_cancel', early_exit=True),
    ], image_right = "host"))

    call change_time(21, 00)

    """
    The dinner ends as quietly as it began.

    Lady Claythorn wishes us each a good night, and the party rises from the table without ceremony.
    """

    if broken_details.threads.is_unlocked('found_poison'):

        jump broken_day2_evening_stay_awake

    jump broken_day2_evening_retire


# --------------------------------------------
#   FOUND THE POISON - he refuses to sleep and presses on
# --------------------------------------------
label broken_day2_evening_stay_awake:

    $ play_music('mysterious', 2)

    """
    The others drift towards the stairs and the billiard room, and I stand a moment in the hall with my hand on the banister.

    I am tired to the bone, and a bed has rarely argued its case so well.

    But the bottle sits in my coat like a stone.

    Harring drank in this house, and slept in this house, and did not wake.

    Whoever left that poison on a shelf has had a full day to find a new use for it, and here we all are, being wished a good night and sent up to our beds.

    No.

    Tonight I do not sleep.

    There is a man in the billiard room who has lost his taste for drink, a staff below stairs hired for one weekend only, and questions enough between them to keep me up until dawn.

    Time to go to work.
    """

    $ change_room('entrance_hall')

    call change_time(21, 30)

    $ time_left = 90

    call run_menu(broken_details.saved_variables["day2_evening_map_menu"])

    call change_time(23, 00)

    $ stop_music()

    """
    The house has gone quiet around me, room by room.

    I have seen what there is to see for one night, and the hardest part of it still lies ahead.

    Staying awake until morning.
    """

    $ change_room('bedroom_broken', dissolve)

    $ play_music('mysterious', 2)

    """
    I go up to my room at last, and I do not undress.

    I set the chair where it commands the door, stand the poison bottle on the table where I can see it, and turn the lamp down low.

    The house settles around me, board by board.

    I have sat up all night for a story before. Never for my life.
    """

    call wait_screen_transition()

    """
    Some time past four, when the dark is at its thickest, I hear it.

    Not a footstep. An engine.

    I put out the lamp and go to the window.

    Below, on the drive, the motor car rolls away from the house with its lamps unlit, the gravel crackling soft under its wheels.

    It does not hurry.

    I watch its shape sink into the black of the trees, and I cannot see who is inside.

    But no household slips away from its own guests in the dead of night, lamps out, unless the next part of the programme is one it would rather not be present for.

    Morning cannot come quickly enough.
    """

    jump broken_day3_morning


# --------------------------------------------
#   NO POISON - he retires, and the manor burns in the night
# --------------------------------------------
label broken_day2_evening_retire:

    """
    The others drift towards the stairs and the billiard room, and I stand a moment in the hall, weighing the evening.

    Something in me does not care for any of it. The road, the letters, the empty chair at dinner.

    But it is a feeling only, with nothing solid beneath it, and I have been carrying another man's face since Friday.

    I am wrung dry.

    The police come tomorrow. Whatever I mean to do about any of it, I shall do it better for a night's sleep.
    """

    $ change_room('bedroom_broken', dissolve)

    call change_time(22, 30)

    $ stop_music()

    """
    I lock my door, and take off the mask, and the face underneath it is more tired than the one on top.

    The wine has made my limbs heavy and my thoughts slow.

    Sleep takes me before I have finished deciding to allow it.
    """

    call wait_screen_transition()

    $ play_music('scary')

    play sound fire loop

    """
    Somewhere very far away, glass breaks.

    I swim up towards waking and do not reach it.

    The room is warm. The dark has a taste to it now, thick and bitter.

    Smoke.

    My body understands before my mind does, but my arms are lead, and the door is a mile away across the carpet.

    The last thing I know is the line of light beneath it. Bright, and orange, and moving.
    """

    jump broken_ending_burned


# ------------------------------------
#   DINNER SCENES
# ------------------------------------
label broken_day2_dinner_host:

    broken """
    You have kept a steady hand on the house today, Lady Claythorn.

    It cannot have been an easy day to preside over.
    """

    host """
    You are kind to say so, Mr Moody.

    A hostess is not permitted a difficult day. She may only have busy ones.
    """

    broken """
    Well said.

    Then I hope you will forgive me for adding to it with a little conversation.
    """

    host """
    That part of it, Mr Moody, is no burden at all.
    """

    call host_generic

    return
