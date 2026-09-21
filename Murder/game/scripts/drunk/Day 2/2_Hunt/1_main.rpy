# --------------------------------------------
#   Drunk
#
#   Saturday - The Hunt
#
#   11:00 -> 15:00
#
#   Music: upbeat for the lawn, chill for the grove, danger for the shot
#
#   Position
#       - North field   : host, captain, butler
#       - Western grove : doctor, drunk, lad, footman
#       - House         : nurse, psychic
#       - Dead          : broken (Thomas Moody)
#
# --------------------------------------------
label drunk_day2_hunt:

    call change_time(11, 00, 'The Hunt', 'Saturday', chapter='saturday_afternoon')

    $ drunk_details.add_checkpoint("drunk_day2_hunt")

    call black_screen_transition("Samuel Manning", chapters_names[current_chapter])

    if drunk_details.threads.is_unlocked('watered_flask'):
        $ drunk_mode = False
    else:
        $ drunk_mode = True

    $ change_room('manor_garden', irisout)

    if not drunk_details.threads.is_unlocked('watered_flask'):
        show layer master at drunk_wobble_layer

    $ play_music('upbeat')

    # TODO add dialogs

    if drunk_details.threads.is_unlocked('watered_flask'):

        call drunk_day2_hunt_morning_clear

    else:

        call drunk_day2_hunt_morning_drunk

    # TODO add dialogs

    if drunk_details.threads.is_unlocked('watered_flask'):

        call drunk_day2_hunt_afternoon_clear

    else:

        call drunk_day2_hunt_afternoon_drunk

    return


# ------------------------------------
#   The morning, sober and pretending
# ------------------------------------
label drunk_day2_hunt_morning_clear:

    # TODO add dialogs

    return


# ------------------------------------
#   The morning, drunk
# ------------------------------------
label drunk_day2_hunt_morning_drunk:

    # TODO add dialogs

    return


# ------------------------------------
#   The afternoon, sober. The doctor's back, and the choice.
# ------------------------------------
label drunk_day2_hunt_afternoon_clear:

    # TODO add dialogs

    $ time_left = 1
    call run_menu(TimedMenu("drunk_day2_hunt_menu_rabbit", [
        TimedMenuChoice('Raise the rifle and fire', 'drunk_day2_hunt_fire', early_exit=True),
        TimedMenuChoice('Lower the rifle', 'drunk_day2_hunt_lower', early_exit=True),
    ]))

    return


# ------------------------------------
#   He fires. -> shot_doctor, and the weekend goes on.
# ------------------------------------
label drunk_day2_hunt_fire:

    $ drunk_details.threads.unlock('shot_doctor')

    # TODO add dialogs

    jump drunk_day2_evening


# ------------------------------------
#   He lowers the rifle. -> spared
# ------------------------------------
label drunk_day2_hunt_lower:

    # TODO add dialogs

    jump drunk_ending_spared


# ------------------------------------
#   The afternoon, drunk. The rabbit is real. -> despair
# ------------------------------------
label drunk_day2_hunt_afternoon_drunk:

    # TODO add dialogs

    jump drunk_ending_despair
