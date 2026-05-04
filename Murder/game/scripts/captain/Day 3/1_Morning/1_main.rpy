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
# --------------------------------------------

label captain_day3_morning:

    call change_time(8, 30, 'Morning', 'Sunday', hide_minutes = True, chapter='sunday_morning')

    $ captain_details.add_checkpoint("captain_day3_morning")

    call black_screen_transition("Sushil Sinha", chapters_names[current_chapter])

    jump work_in_progress
