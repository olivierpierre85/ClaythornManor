# --------------------------------------------
#   Drunk
#
#   Friday - Evening
#
#   18:30 -> 23:00
#
#   Music: chill at dinner, upbeat for the billiard room, scary for the letter
#
#   Position
#       - Dining Room : Everyone (he sits on Lady Claythorn's left, Miss Marsh
#         below him, the boy across the table)
#       - Billiard Room : the party, after dinner
#       - Bedroom Drunk : the letter
#
# --------------------------------------------
label drunk_day1_evening:

    call change_time(18, 30, 'Dinner', 'Friday', hide_minutes=True, chapter='friday_evening')

    $ drunk_details.add_checkpoint("drunk_day1_evening")

    call black_screen_transition("Samuel Manning", chapters_names[current_chapter])

    $ drunk_mode = True

    $ change_room('tea_room', irisout)

    show layer master at drunk_wobble_layer

    play sound dinner_gong

    # TODO add dialogs

    call drunk_day1_dinner_sole

    # TODO add dialogs

    call drunk_day1_dinner_glimpses

    # TODO add dialogs

    $ time_left = 1
    call run_menu(TimedMenu("drunk_day1_evening_menu_after_dinner", [
        TimedMenuChoice('Get to the billiard room before the others do', 'drunk_day1_evening_billiard_room', early_exit=True),
        TimedMenuChoice('Go straight up to your room', 'drunk_day1_evening_go_up', early_exit=True),
    ]))

    call drunk_day1_evening_letter

    jump drunk_day2_morning


# ------------------------------------
#   The sole. The one clear thing in the evening.
# ------------------------------------
label drunk_day1_dinner_sole:

    # TODO add dialogs

    return


# ------------------------------------
#   The rest of dinner. Things half seen, filed without knowing it.
#   Every one of them comes back on Saturday night.
# ------------------------------------
label drunk_day1_dinner_glimpses:

    call change_time(19, 30)

    # TODO add dialogs

    return


# ------------------------------------
#   BILLIARD ROOM. He takes everything worth the name.
#   -> raided_bar, port
# ------------------------------------
label drunk_day1_evening_billiard_room:

    $ change_room('billiard_room')

    $ play_music('upbeat')

    # TODO add dialogs

    $ drunk_details.threads.unlock('raided_bar')
    $ drunk_details.objects.unlock('port')

    # TODO add dialogs

    return


# ------------------------------------
#   Straight up. Nothing taken.
# ------------------------------------
label drunk_day1_evening_go_up:

    $ change_room('bedrooms_hallway')

    $ play_music('upbeat')

    # TODO add dialogs

    return


# ------------------------------------
#   THE LETTER
# ------------------------------------
label drunk_day1_evening_letter:

    call change_time(21, 30)

    $ change_room('bedroom_drunk', dissolve)

    # TODO add dialogs

    $ time_left = 1
    call run_menu(TimedMenu("drunk_day1_evening_menu_letter", [
        TimedMenuChoice('Drink until it goes away', 'drunk_day1_evening_letter_drink', early_exit=True),
        TimedMenuChoice('Put the bottle down, and think{{intuition}}', 'drunk_day1_evening_letter_sober', early_exit=True, condition="drunk_details.endings.is_unlocked('despair')"),
    ]))

    return


# ------------------------------------
#   He drinks. -> day1_drink
# ------------------------------------
label drunk_day1_evening_letter_drink:

    $ drunk_details.threads.unlock('day1_drink')

    # TODO add dialogs

    return


# ------------------------------------
#   He does not. The letter did what a night's sleep never does.
# ------------------------------------
label drunk_day1_evening_letter_sober:

    # TODO add dialogs

    return
