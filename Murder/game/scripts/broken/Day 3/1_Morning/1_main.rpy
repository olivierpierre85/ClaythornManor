# --------------------------------------------
#   Broken
#
#   Sunday - Morning
#
#   8:30 -> 11:30
#
#   Music: mysterious
#
#   Position
#       - House : Captain, Doctor, Mr Manning, Miss Baxter, Miss Marsh, Broken
#       - Gone  : Lady Claythorn and all the staff (left in the night)
#       - Dead  : Lad (Ted Harring)
#
# --------------------------------------------
label broken_day3_morning:

    $ broken_details.add_checkpoint("broken_day3_morning")

    call change_time(8, 30, 'Morning', 'Sunday', hide_minutes = True, chapter='sunday_morning')

    call black_screen_transition("Thomas Moody", chapters_names[current_chapter])

    $ change_room('bedroom_broken', irisout)

    $ play_music('mysterious', 2)

    # TODO, wake with everyone in the billiard room?
    """
    Dawn comes when I wake up, stiff in my watch chair.
    """


    jump broken_day3_afternoon
