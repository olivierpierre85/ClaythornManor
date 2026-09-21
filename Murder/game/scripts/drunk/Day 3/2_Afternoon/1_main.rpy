# --------------------------------------------
#   Drunk
#
#   Sunday - Afternoon
#
#   12:00 -> Ending
#
#   Music: mysterious, danger for the table, scary for the butler
#
#   Position
#       - Service passage : drunk, hidden
#       - Kitchen / Dining Room : lad, psychic, nurse
#       - Dead : broken, doctor
#       - Gone, then back : butler
#
# --------------------------------------------
label drunk_day3_afternoon:

    call change_time(12, 00, 'Afternoon', 'Sunday', hide_minutes = True, chapter = 'sunday_afternoon')

    $ drunk_details.add_checkpoint("drunk_day3_afternoon")

    call black_screen_transition("Samuel Manning", chapters_names[current_chapter])

    $ change_room('basement_stairs', irisout)

    $ play_music('mysterious', 2)

    # TODO add dialogs

    $ time_left = 1
    call run_menu(TimedMenu("drunk_day3_afternoon_menu_plates", [
        TimedMenuChoice('Slip in and put the plates back where they were', 'drunk_day3_afternoon_swap', early_exit=True),
        TimedMenuChoice('Stay in the hatch. It is not your business. It never was', 'drunk_day3_afternoon_watch', early_exit=True),
    ]))

    return


# ------------------------------------
#   He puts them back. -> swapped_back, the boy lives
# ------------------------------------
label drunk_day3_afternoon_swap:

    $ drunk_details.threads.unlock('swapped_back')

    $ change_room('dining_room')

    # TODO add dialogs

    call drunk_day3_afternoon_recognition

    call drunk_day3_afternoon_butler_returns

    jump drunk_ending_survived


# ------------------------------------
#   He does nothing. -> the boy dies
# ------------------------------------
label drunk_day3_afternoon_watch:

    # TODO add dialogs

    call drunk_day3_afternoon_recognition

    call drunk_day3_afternoon_butler_returns_found

    jump drunk_ending_found_out


# ------------------------------------
#   He recognises Miss Baxter. -> lost_case
# ------------------------------------
label drunk_day3_afternoon_recognition:

    $ play_music('sad', 2)

    # TODO add dialogs

    return


# ------------------------------------
#   The butler returns, and Manning has the wit to be gone. (survived)
# ------------------------------------
label drunk_day3_afternoon_butler_returns:

    # TODO add dialogs

    return


# ------------------------------------
#   The butler returns, and Manning is still at the hatch. (found_out)
# ------------------------------------
label drunk_day3_afternoon_butler_returns_found:

    # TODO add dialogs

    return
