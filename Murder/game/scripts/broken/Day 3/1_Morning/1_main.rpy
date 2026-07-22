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

    $ change_room('billiard_room', irisout)

    $ play_music('mysterious', 2)

    """
    Dawn comes when I wake up, stiff in my watch chair.
    """

    ## TODO more talk, still empty, get ready for a walk, get some food for the trip
    ## Then a long walk. Picnic along the road

    ## Add something about Samuel Manning masks?.
    ## where to put the intuition? AT THE split thing !! 
    # Before intuition, convince to send only captain sinha and broken.
    # They get shot by a volley of hunting rifles.

    # After intuition, you insist very very much not to go because...
    # you think you there might a killer in this shit.
    # There maybe the choice to show your true face => Arrested by CAPTAIN, then left then dies with the rest of them (burn in you room, attache to the bed.) 
    # Keep your identity intact, convince them by telling WHOEVER doesn't aggre is suspicious or some shit. So everyone walks, women complain, it takes a shit long of time, but you get out
    # Or the opposite. The psychic will say she saw part of your face while sleeping
    # but if you manage to reach the police station ! Almost everybody makes it but ted harring. The suspicious thing

    jump broken_day3_afternoon
