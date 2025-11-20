# --------------------------------------------
#   Doctor
#           
#   Saturday - Evening
# 
#   15h -> 23h
#
#   Music: sad
#
#   Position
#       - House: Everyone else
#       - Dead : broken, DRUNK
#
#   Notes : 
#       - Team with nurse?
#       - Map 120 minutes
# --------------------------------------------
label doctor_day2_evening:

    call change_time(15,00, 'Evening', 'Saturday', chapter='saturday_evening')

    $ doctor_details.add_checkpoint("doctor_day2_evening") 
    
    call black_screen_transition("Daniel Baldwin", chapters_names[current_chapter])

    $ change_room("great_hall", irisout)

    """
    Everything happened so quickly it is all a blur.

    After the shouting and crying in the woods, Captain Sinha took charge.

    He had us carry the doctor on a makeshift stretcher back to the house.

    It took some time, but we eventually reached the mansion.
    """        

    $ play_music('sad')

    jump work_in_progress
