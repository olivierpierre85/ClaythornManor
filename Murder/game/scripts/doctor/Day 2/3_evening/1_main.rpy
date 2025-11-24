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

    $ play_music('sad')

    """
    I am still in shock when we reach the mansion.

    I can scarcely recall what happened in the woods.

    Samuel Manning, bleeding to death whilst I tried to save him.

    The other group, drawn by the noise, rejoining us to witness the horrific scene.

    Once it was clear the poor man was dead, Captain Sinha took charge and had us carry Samuel Manning back to the house.

    I still can hardly believe it.

    I have killed a man.

    I cannot seem to convince myself that it was him or me.

    Yet I must not waste time dwelling on it.

    The others will have questions.

    I must think very carefully about what I am going to say to them.
    """           

    jump work_in_progress

