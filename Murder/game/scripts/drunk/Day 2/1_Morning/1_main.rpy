# --------------------------------------------
#   Drunk
#
#   Saturday - Morning
#
#   07:30 -> 10:45
#
#   Music: mysterious in the room, scary for the announcement, upbeat for the hunt
#
#   Position
#       - Bedroom Drunk : drunk
#       - Dining Room : Everyone but Thomas Moody, found dead in his bed
#       - Gun Room : the men, taking their rifles
#
# --------------------------------------------
label drunk_day2_morning:

    call change_time(7, 30, 'Morning', 'Saturday', hide_minutes = True, chapter='saturday_morning')

    $ drunk_details.add_checkpoint("drunk_day2_morning")

    call black_screen_transition("Samuel Manning", chapters_names[current_chapter])

    $ change_room('bedroom_drunk', irisout)

    $ play_music('mysterious', 2)

    if drunk_details.threads.is_unlocked('day1_drink'):

        call drunk_day2_morning_hungover

    else:

        call drunk_day2_morning_clear

    # TODO add dialogs

    jump drunk_day2_hunt


# ------------------------------------
#   He drank. He remembers nothing, and the letter is new.
# ------------------------------------
label drunk_day2_morning_hungover:

    show layer master at drunk_wobble_layer
    $ drunk_mode = True

    # TODO add dialogs

    return


# ------------------------------------
#   He did not drink. First clear morning in five years.
#   -> watered_flask, or not
# ------------------------------------
label drunk_day2_morning_clear:

    $ drunk_mode = False

    # TODO add dialogs

    $ time_left = 1
    call run_menu(TimedMenu("drunk_day2_morning_menu_flask", [
        TimedMenuChoice('Fill it with water, and a finger of whisky for the smell', 'drunk_day2_morning_flask_water', early_exit=True),
        TimedMenuChoice('Fill it with whisky. One day will not hurt', 'drunk_day2_morning_flask_whisky', early_exit=True),
    ]))

    return


label drunk_day2_morning_flask_water:

    $ drunk_details.threads.unlock('watered_flask')

    # TODO add dialogs

    return


label drunk_day2_morning_flask_whisky:

    # TODO add dialogs

    return
