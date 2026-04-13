# --------------------------------------------
#   Captain
#           
#   Saturday - Morning
#   
#   09:00 -> 11:00
#
#   Music: chill
#
#   Position
#       - Dining Room : Everyone 
#
#   Notes : 
#       - 
# --------------------------------------------

label captain_day2_morning:

    call change_time(9, 00, 'Morning', 'Saturday', hide_minutes = True, chapter='saturday_morning')

    $ captain_details.add_checkpoint("captain_day2_morning")

    call black_screen_transition("Sushil Sinha", chapters_names[current_chapter])

    $ change_room("bedroom_captain", irisout)

    $ play_music('chill', 3)

    """
    I wake before the sun has fully cleared the horizon.

    The 'George I' room is silent, its heavy curtains muffling the morning bird-song.

    I lie still for a moment, listening to the house.

    Day two.

    My performance yesterday was adequate. I played the part of the retired officer to perfection.

    Yet I must not grow complacent. A single slip, a misplaced word, and this entire charade collapses.

    I have survived thirty years of Imperial politics. I can survive a weekend in the Highlands.

    I rise and begin my preparations.

    Washing is a brief, cold affair. Dressing is done with practised efficiency.

    Every button fastened. Every crease straightened.

    The mirror shows a man who belongs here. That is all that matters.

    I cannot afford to be late for breakfast. Punctuality is the bedrock of authority.
    """

    call change_time(9, 15)

    $ change_room('dining_room', dissolve)

    """
    I enter the dining room.

    The table is set, and the smell of coffee and fried bread fills the air.

    It is time to resume the act.
    """

    jump work_in_progress
