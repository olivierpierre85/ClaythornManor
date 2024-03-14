# --------------------------------------------
#   Psychic
#           
#   Saturday - Evening
# 
#   18:30 -> 23h
#
#   Music: sad
#
#   Position
#       - House: Everyone else
#       - Dead : broken, doctor
#
#   Notes : 
#       -  
# --------------------------------------------
label psychic_day2_evening:

    call change_time(18,30, "Evening", "Saturday")

    $ psychic_details.add_checkpoint("psychic_day2_evening") 

    call black_screen_transition("Amelia Baxter", "Saturday Evening")

    $ change_room("dining_room", irisout)
    
    $ play_music('sad', 3)


    """
    As I step into the room, a somber ambiance surrounds me.

    The chairs where Daniel Baldwin and Thomas Moody usually sit are vacant.

    Samuel Manning is not here either, obviously.

    I settle into my familiar spot, with Ted Harring on my right.

    Lady Claythorn stands up to speak.
    """

    call common_day2_evening_dinner

    call change_time(21,00)

    """
    We ate in silence.

    After dinner, most retired to their rooms.

    I wouldn't think many would join for a drink afterwards.

    I probably should wait in my room for Ted Harring. 

    But I could also take advantage that the Manor is almost empty.

    What will I do?
    """


    $ time_left = 60

    call run_menu(psychic_details.saved_variables["day2_evening_map_menu"])

    call change_time(22,00)

    """
    No need to wander the house further.

    I should get back to my room.
    """

    $ change_room('psychic_room', dissolve)

    pause 2.0

    """
    After a little while, someone knocks on my door.
    """

    # call TOdo

    jump work_in_progress

