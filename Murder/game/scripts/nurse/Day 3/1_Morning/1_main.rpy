# --------------------------------------------
#   Nurse
#           
#   Sunday - Morning
# 
#   8:30 -> 12:00
#
#   Music: mysterious
#
#   Position
#       - House: lad, captain, psychic, doctor, nurse
#       - Dead : broken, drunk
#       -? : Host
#
#   Notes : 
#       - No more maps
#   Useful Threads:
#       - Knows about footman
# --------------------------------------------
label nurse_day3_morning:

    call change_time(8, 30, "Morning", "Sunday", hide_minutes=True, chapter='sunday_morning')

    $ nurse_details.add_checkpoint("nurse_day3_morning") 

    call black_screen_transition("Rosalind Marsh", chapters_names[current_chapter])

    $ change_room("bedroom_nurse", irisout)

    $ play_music('mysterious')

    """
    I wake before the sun has fully conquered the Scottish mist.

    My chest feels heavy, a dull ache that has become my constant companion.

    I lie still for a moment, listening to the silence of the manor.

    It is a heavy, expectant silence.

    The events of the past two days weigh upon me like a physical burden.
    """


    jump work_in_progress
