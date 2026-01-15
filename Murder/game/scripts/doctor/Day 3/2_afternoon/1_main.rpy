# --------------------------------------------
#   Doctor
#           
#   Sunday - Afternoon
# 
#   12:00 -> Ending
#
#   Music: mysterious
#
#   Position
#       - House: lad, captain, psychic, doctor
#       - Dead : broken,  drunk
#       -? : Host, nurse
#
#   Notes : 
#       - 
# --------------------------------------------
label doctor_day3_afternoon:

    call change_time(12,00, "Afternoon", "Sunday", chapter='sunday_afternoon')
    
    $ doctor_details.add_checkpoint("doctor_day3_afternoon") 

    call black_screen_transition("Daniel Baldwin", chapters_names[current_chapter])

    $ play_music('mysterious')

    if doctor_details.threads.is_unlocked('trust_captain'):

        call doctor_day3_afternoon_captain

    elif doctor_details.threads.is_unlocked('trust_nurse'):

        call doctor_day3_afternoon_nurse

    return
