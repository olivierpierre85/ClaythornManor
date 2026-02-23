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
    He opens the door to a very elegant room.
    """

    $ change_room('bedroom_nurse', dissolve)

    butler """
    Let me know if I can do anything for you.
    """

    nurse """
    Very well, thank you.
    """

    """
    Well, the trip was exhausting.

    If I don't want to exert myself, I'd better get some rest before going downstairs.

    I set up my luggage and get into bed.
    """

    call wait_screen_transition()

    call change_time(16,30)

    """
    I wake up a bit rested — enough to get through dinner.

    I should go downstairs to meet the others.
    """

    $ change_room('tea_room', dissolve)

    call change_time(16,45)

    jump work_in_progress