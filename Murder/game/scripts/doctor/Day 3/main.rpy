# --------------------------------------------
#   Doctor
#           
#   Sunday - Morning
# 
#   7:30 / 9:30 -> 12:00
#
#   Music: mysterious
#
#   Position
#       - House: lad, captain, psychic, doctor
#       - Dead : broken, drunk, ?????
#       -? : Host, nurse
#
#   Notes : 
#       - Map 90, 150 minutes
# --------------------------------------------
label doctor_day3_morning:

    call change_time(9, 30, "Morning", "Sunday", hide_minutes=True, chapter='sunday_morning')

    $ lad_details.add_checkpoint("doctor_day3_morning") 

    call black_screen_transition("Daniel Baldwin", chapters_names[current_chapter])

    $ play_music('mysterious')

    if doctor_details.threads.is_unlocked('trust_captain'):

        call doctor_day3_morning_captain

    elif doctor_details.threads.is_unlocked('trust_nurse'):

        call doctor_day3_morning_nurse

    jump work_in_progress


label doctor_day3_morning_captain:

    $ change_room('bedroom_captain', irisout)

    """
    Captain path? Following him, discuss suspects, leave as soon as possible.

    Escape?

    ALSO learn about the Boxer's rebellion !! Help for possible unlocking!!!!
    """

    return
    


label doctor_day3_morning_nurse:

    $ change_room('bedroom_nurse', irisout)

    """
    TODO, nurse path?

    What is nurse path? follow the nurse, then pop up to the death dinner with Lad and psychic?

    Then Die eating poison like others.

    BUT what have we discover? LEARN MORE ABOUT NURSE => Maybe add something to unlock HER? => So the psychic ALONE IS NOT ENOUGH!!
    """

    return
    
# TODO, multiple starts possible
# Wake up in NURSE's ROOM. You hide with here while observing the rest of the gang, you notice she is stealy (helps to unlock her later?) ???
# Wake up in Captain's room. You follow him exploring but find NOTHING, until you find LAD and psychic => YOU leave with captain !!!!!!