# --------------------------------------------
#   Drunk
#
#   Sunday - Morning
#
#   08:00 -> 12:00
#
#   Music: scary for the door, mysterious after
#
#   Position
#       - Bedroom Drunk : drunk, playing dead
#       - House : lad, psychic, captain (searching)
#       - Dead  : broken, doctor
#       - Gone  : butler and the staff, since the night
#
# --------------------------------------------
label drunk_day3_morning:

    call change_time(8, 00, 'Morning', 'Sunday', hide_minutes = True, chapter = 'sunday_morning')

    $ drunk_details.add_checkpoint("drunk_day3_morning")

    call black_screen_transition("Samuel Manning", chapters_names[current_chapter])

    $ drunk_mode = False

    scene black_background

    $ play_music('scary', 3)

    # TODO add dialogs

    jump drunk_day3_afternoon
