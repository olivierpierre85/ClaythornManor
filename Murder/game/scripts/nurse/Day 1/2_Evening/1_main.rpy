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
    As we enter, the butler steps forward to greet us.
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
    I make my excuses before he can finish his next sentence.

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

    I was telling those gentlemen a story about .....
    """

    nurse """
    No, please, go on. I am familiar with wartime stories, as I worked myself through more than one.
    """

    captain """
    Really? You were a wartime nurse. How interesting.

    Well where was I?
    """

    broken """
    I believe you were talking about the Suakin Expedition.
    """

    captain """
    That's where I got my first battle scar.

    It's on my back so I won't show it to you, but it was rather dangerous fighting.

    Not like the great war of course, and not that I can understand you pain.
    
    But still, a battle wound is a battle wound.
    """

    """
    He's comparing a small scar on his back to the disfigured face of Thomas Moody.

    That's rather insensitive.

    """

    """
    He speaks on at some length about the expedition.

    I listen as best I can.

    Something about the way he talks about the Suakin Expedition is odd.

    Yet, I can't quite place it.

    That story is too old in my mind.

    At some point I notice Doctor Baldwin has gone quiet.

    He nods along, but his eyes are elsewhere.

    I know that look. Something on his mind, and not the conversation in front of him.
    """

    """
    Two more have slipped into the room without my noticing — a young man with the restless energy of someone who'd rather be outside, and a woman in rather more elaborate dress than the occasion perhaps warrants.

    I have no time to speak to them. The gong sounds from the corridor.
    """

    play sound dinner_gong

    jump work_in_progress