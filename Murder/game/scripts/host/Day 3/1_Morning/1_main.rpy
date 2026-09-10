# --------------------------------------------
#   Host
#
#   Sunday - Morning
#
#   08:00 -> 12:00
#
#   Music: mysterious
#
#   Position
#       - Bedroom Host : host, captain (she confided in him last night)
#       - House        : lad, psychic, nurse
#       - Confined     : drunk, locked in his room
#       - Dead         : broken (Thomas Moody), doctor (Daniel Baldwin)
#       - Gone         : butler and the rest of the staff, in the car since eleven
#
#   Notes :
#       - This chapter is only reachable through the 'trust_captain' branch of
#         Saturday night. Every other Saturday evening path ends in a death.
#       - TODO: waking scene with the Captain, the state of the empty house,
#         and the morning map exploration.
# --------------------------------------------
label host_day3_morning:

    call change_time(8, 00, 'Morning', 'Sunday', hide_minutes = True, chapter = 'sunday_morning')

    $ host_details.add_checkpoint("host_day3_morning")

    call black_screen_transition("Lady Claythorn", chapters_names[current_chapter])

    $ change_room('bedroom_host', irisout)

    $ play_music('mysterious', 2)

    # TODO: waking scene - the house is silent, the staff are gone with the car.

    call host_day3_morning_wake

    # TODO: map exploration of the empty manor.
    #
    #   $ time_left = 150
    #
    #   call run_menu(host_details.saved_variables["day3_morning_map_menu"])

    call change_time(12, 00)

    $ stop_music()

    jump work_in_progress

    # TODO: once Sunday afternoon is written, replace the line above with:
    #
    #   jump host_day3_afternoon


# ------------------------------------
#   Waking with the Captain
# ------------------------------------
label host_day3_morning_wake:

    # TODO: dialogue.

    return
