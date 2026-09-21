# --------------------------------------------
#   Drunk
#
#   Friday - Afternoon
#
#   15:45 -> 16:45
#
#   Music: chill
#
#   Alive: Everyone
#
# --------------------------------------------
label drunk_introduction:

    call change_time(15, 45, 'Arrival', 'Friday', hide_minutes=True, chapter='friday_afternoon')

    $ drunk_details.add_checkpoint("drunk_introduction")

    call black_screen_transition("", "Samuel Manning")

    $ drunk_mode = True

    $ change_room("train_inside_second", irisout)

    show layer master at drunk_wobble_layer

    play sound train_moving loop

    $ play_music('chill')

    # TODO add dialogs

    jump drunk_day1_evening
