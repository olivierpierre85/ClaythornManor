# --------------------------------------------
#   Captain
#
#   Sunday - Morning
#
#   08:30 -> 12:00
#
#   Music: mysterious
#
#   Position
#       - House: captain, lad, psychic, nurse, host
#       - Dead : broken, doctor
#       - Confined : drunk (locked in his room)
#
#   Notes :
#       - Branches on confide_in_nurse:
#           - confided: Miss Marsh comes to fetch him, they hide together
#           - otherwise: captain explores the manor alone
#       - In the exploration branch, finding the car with petrol_tin_in_shed
#         unlocks an option to flee alone in the car.
# --------------------------------------------

label captain_day3_morning:

    call change_time(8, 30, 'Morning', 'Sunday', hide_minutes = True, chapter='sunday_morning')

    $ captain_details.add_checkpoint("captain_day3_morning")

    call black_screen_transition("Sushil Sinha", chapters_names[current_chapter])

    $ play_music('mysterious', 2)

    if captain_details.threads.is_unlocked('confide_in_nurse'):

        call captain_day3_morning_nurse

    else:

        call captain_day3_morning_explore


    jump captain_day3_afternoon
