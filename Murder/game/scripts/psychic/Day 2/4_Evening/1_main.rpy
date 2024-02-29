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

    jump work_in_progress

