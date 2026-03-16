# --------------------------------------------
#   Nurse
#
#   Sunday - Afternoon
#
#   12:00 -> Ending
#
#   Music: mysterious
#
#   Position
#       - House: lad, captain, psychic, doctor
#       - Attic: nurse (hiding)
#       - Dead : broken, drunk
#       -? : Host
#
#   Notes :
#       - Nurse is hiding in the butler's room with stolen silver
#       - She waits for the drive to clear before attempting to leave
#       - Captain leaves the manor to get help (heard from attic)
#       - She slips out once the drive is quiet
# --------------------------------------------
label nurse_day3_afternoon:

    call change_time(12, 00, "Afternoon", "Sunday", hide_minutes=True, chapter='sunday_afternoon')

    $ nurse_details.add_checkpoint("nurse_day3_afternoon")

    call black_screen_transition("Rosalind Marsh", chapters_names[current_chapter])

    $ change_room("butler_room", irisout)

    $ play_music('mysterious')

    # TODO: Nurse reflects on waiting — time is passing, she hears movement below

    call wait_screen_transition()

    call change_time(13, 00)

    # TODO: She hears the front door open and close — the captain leaving

    $ change_room("attic_hallway", dissolve)

    # TODO: She moves carefully along the attic corridor and listens

    $ change_room("entrance_hall", dissolve)

    # TODO: She checks the entrance hall — it is empty, the drive quiet

    $ change_room("manor_exterior", dissolve)

    # TODO: She steps outside and considers the road ahead

    if nurse_details.threads.is_unlocked('steal_cutlery_1') or nurse_details.threads.is_unlocked('steal_cutlery_2') or nurse_details.saved_variables.get('visited_attic_butler_room', False):

        # TODO: She reflects on what she is carrying — worth the risk

        jump nurse_ending_escape_rich

    else:

        jump nurse_ending_escape_poor
