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
    As I enter, the butler steps forward to greet us.
    """

    call common_day1_evening_doctor_nurse_broken_arrival

    $ change_room('bedrooms_hallway', dissolve)

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

    I was telling those gentlemen a story about a certain conflict I was involved in.

    But I can change the subject if you prefer.
    """

    nurse """
    No, please, go on. I am quite familiar with wartime stories, having served as a nurse through more than one.
    """

    captain """
    Really? You were a wartime nurse. How interesting.

    Well where was I?
    """

    broken """
    I believe you were talking about the Anglo-Zanzibar War.
    """

    captain """
    That's where I got my first battle scar.

    It's on my back so I won't show it to you, but it was rather dangerous fighting.

    Not like the great war of course, and not that I can understand your pain.
    
    But still, a battle wound is a battle wound.
    """

    """
    He's comparing a small scar on his back to the disfigured face of Thomas Moody.

    That's rather insensitive.
    """

    """
    He speaks on at some length about the expedition.

    I listen as best I can.

    Something about the way he talks about the Anglo-Zanzibar War is odd.

    There was something specific about that conflict. Yet, I can't quite place it.

    It is too distant in my memory.

    At some point I notice Doctor Baldwin has gone quiet.

    He nods along, but his eyes are elsewhere.

    I know that look. Something on his mind, and not the conversation in front of him.
    """

    """
    Two more have slipped into the room without my noticing.
    
    A young man and a woman in rather more elaborate dress than the occasion perhaps warrants.

    I have no time to speak to them. The gong sounds from the corridor.
    """

    play sound dinner_gong

    $ stop_music()

    call change_time(18,30, 'Dinner', 'Friday')

    $ change_room('dining_room', irisout)

    $ play_music('chill', 2)

    """
    My place is set at the far end of the table.

    To my distinct dismay, the only person situated next to me is Mr Manning.

    Of all the guests to be seated beside, I must endure the one who can scarcely stand straight.
    """

    call common_day1_evening_host_welcome_speech

    """
    Once the speech concludes, the first course promptly follows.

    Shortly after, the staff circle the table to pour the wine.
    """

    drunk """
    Ah, capital! Fill it up to the very brim, if you please.

    Much obliged.
    """

    """
    It appears the evening will be quite as taxing as I had feared.

    I am conflicted, if I ignore him, I might have to eat in silence, that could appear weird.

    But I don't know that I want to engage with him.

    What to do?
    """

    call change_time(19, 30)

    $ time_left = 90 
    call run_menu(TimedMenu("nurse_day1_evening", [
        TimedMenuChoice("Talk to Samuel Manning", 'nurse_day1_dinner_drunk', early_exit=True),
        TimedMenuChoice("Just keep to yourself", 'generic_cancel', early_exit=True),
    ], image_right = "lad"))

    call change_time(21,00)

    """
    Everyone is finished with dinner. 
    
    There is talk about possible drinks after, but first I have to go to my room.

    Before I get up, I think about the silver.

    It's not first rate, but I might get some money for it.

    Should I pocket it before leaving to my room?
    """

    $ time_left = 1 
    call run_menu(TimedMenu("doctor_day1_evening", [
        TimedMenuChoice("Talk to Ted Harring", 'doctor_day1_dinner_lad', early_exit=True),
        TimedMenuChoice("Just keep to yourself", 'generic_cancel', early_exit=True),
    ], image_right = "lad"))

    call change_time(21,00)

    jump work_in_progress


label nurse_day1_dinner_drunk:

    """
    I can't believe I am doing this.

    But It would feel too rude for me to just ignore him.

    And he might also take it the wrong.

    So I guess I don't have a choice.
    """

    nurse """
    How are you doing Mister Manning?
    """

    drunk """
    Me? Oh very well.

    The wine is first rate, you should take a sip.
    """

    """
    I wet my lips into it.

    It's actually not that great.

    Just passable
    """

    nurse """
    Yes, it's rather good.
    """

    """
    Well, what should we talk about?
    """

    call drunk_generic

    return