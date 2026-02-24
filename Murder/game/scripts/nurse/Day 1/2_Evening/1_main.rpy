# --------------------------------------------
#   Nurse
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
#       - Generic Broken, lad
# --------------------------------------------
label nurse_day1_evening:

    call change_time(14, 45, "Evening", "Friday", hide_minutes = True, chapter='friday_evening')

    $ current_character.add_checkpoint("nurse_day1_evening") 

    call black_screen_transition("Rosalind Marsh", chapters_names[current_chapter])

    $ change_room('entrance_hall', dissolve)

    $ play_music('upbeat')

    """
    As we enter the room, the butler comes to greet us.
    """

    call common_day1_evening_doctor_nurse_broken_arrival

    """
    The butler shows Doctor Baldwin and Thomas Moody rooms, then we reach mine.
    """

    butler """
    Miss Marsh, you'll stay in the "Queen Alexandra Room".
    """

    """
    He opens the door to a spacious, well-appointed room.
    """

    $ change_room('bedroom_nurse', dissolve)

    butler """
    Let me know if I can do anything for you.
    """

    nurse """
    Very well, thank you.
    """

    """
    The journey has taken rather more out of me than I'd care to admit.

    I'll rest before dinner.
    """

    call wait_screen_transition()

    call change_time(16,30)

    """
    I wake up a bit rested — enough to get through dinner.

    I should go downstairs to meet the others.
    """

    $ change_room('tea_room', dissolve)

    call change_time(16,45)

    """
    The tea room is quieter than I expected.

    Doctor Baldwin and Thomas Moody are deep in some hushed exchange.

    I pour myself a tea and keep my distance.
    """

    """
    Two men enter together, though they couldn't look less alike.

    One is an Indian gentleman in military dress, upright and composed.

    The other is older — rumpled jacket, unsteady on his feet.
    """

    """
    The soldier crosses to Doctor Baldwin without hesitation.

    The older man drifts toward me.
    """

    drunk """
    Ah! Samuel Manning, at your... at your service.
    """

    """
    He extends a hand, misses mine by several inches, and beams at me regardless.
    """

    nurse """
    How do you do, Mr Manning.
    """

    """
    I made my excuses before he could finish his next sentence.

    The soldier is still with Baldwin and Moody.

    He seems the sort who finishes what he starts.

    I position myself nearby and wait.
    """

    captain """
    Oh, hello Miss ... ?
    """
    
    nurse """
    Miss Marsh.
    """

    captain """
    Nice to meet you, Miss Marsh. Captain Sushil Sinha.

    I was telling those gentlemen a story about 
    """

    nurse """
    Please, go on.
    """

    captain """
    Very well, so where was I?
    """



    """
    He spoke for some time after that — something about the regiment, a posting in Calcutta, a colonel whose name I didn't catch.

    I listened as best I could.

    It was perfectly pleasant if one didn't try to follow the thread.
    """

    """
    At some point I noticed Doctor Baldwin had gone quiet.

    He was nodding along, but his eyes were elsewhere.

    I know that look. Something on his mind, and not the conversation in front of him.
    """

    """
    Two more had slipped into the room without my noticing — a young man with the restless energy of someone who'd rather be outside, and a woman in rather more elaborate dress than the occasion perhaps warranted.

    I didn't introduce myself.

    I wasn't ready for more of that just yet.
    """

    """
    What a peculiar assortment of people.

    Lady Claythorn has eclectic taste in guests, I'll give her that.
    """

    """
    I finish my tea as the gong sounds from the corridor.

    Good. Dinner, at least, requires no conversation I haven't already rehearsed.
    """

    jump work_in_progress