# --------------------------------------------
#   Doctor
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
label doctor_day3_morning:

    call change_time(8, 30, "Morning", "Sunday", hide_minutes=True, chapter='sunday_morning')

    $ lad_details.add_checkpoint("doctor_day3_morning") 

    call black_screen_transition("Daniel Baldwin", chapters_names[current_chapter])

    $ play_music('mysterious')

    if doctor_details.threads.is_unlocked('trust_captain'):

        call doctor_day3_morning_captain

    elif doctor_details.threads.is_unlocked('trust_nurse'):

        call doctor_day3_morning_nurse

    jump work_in_progress
    

