# --------------------------------------------
#   Host
#
#   Saturday - The Hunt
#
#   11:00 -> 15:00
#
#   Music: upbeat for the shoot, danger when the doctor is shot
#
#   Position
#       - House, Tea room : nurse, psychic
#       - North field     : host, captain, butler
#       - Western grove   : doctor, drunk, lad, footman
#       - Dead            : broken (Thomas Moody), then the doctor
#
#   Notes :
#       - The same morning as captain_day2_hunt_moody_dead, seen from her side.
#       - Shared beats (the pairing, the north field, the accident) must be
#         extracted into _common as they are written here.
# --------------------------------------------
label host_day2_hunt:

    call change_time(11, 00, 'The Hunt', 'Saturday', chapter='saturday_afternoon')

    $ current_character.add_checkpoint("host_day2_hunt")

    call black_screen_transition("Lady Claythorn", chapters_names[current_chapter])

    $ change_room('bedroom_host', irisout)

    $ play_music('upbeat', 1)

    # TODO: She changes into the tweeds laid out for her. A man is dead upstairs
    #       and she is dressing for sport, which is exactly what she was hired to do.

    $ change_room('gun_room')

    # TODO: The butler hands her a rifle. A word between the two of them while
    #       nobody is listening, he assures her that Mr Moody's death is an
    #       unfortunate accident and that nobody could have foreseen it.
    # TODO: If found_poison is unlocked, she does not believe a word of it, and
    #       he knows she does not.

    $ change_room('manor_garden')

    # TODO: The party gathers on the lawn. Every line she has is the butler's.

    call common_day2_hunt_butler_groups

    # TODO: The pairing. Captain Sinha asks to accompany her, Mr Manning attaches
    #       himself to the doctor, and Mr Harring goes where he is put.
    #       Extract the shared lines from captain_day2_hunt into _common.

    call change_time(11, 45)

    $ change_room('forest_edge')

    # TODO: The north field. She shoots wide and blames the light, which fools
    #       nobody, least of all a soldier.
    # TODO: But the Captain misses a rabbit sitting still at twenty paces and
    #       blames the lead. She is not the only one acting a part today.
    # TODO: Menu candidate - the suspicious thing of the day (see docs/next_tasks.md).
    #       Needs a thread, and a clue in the captain's or the lad's path to prevent it.

    call change_time(12, 30)

    $ change_room('forest_clearing', dissolve)

    # TODO: Luncheon. The butler leaves them to look in on the other party, and she
    #       is alone with a guest who is plainly working up to a question.
    # TODO: Small talk that gives nothing away. The confrontation with the Captain
    #       belongs to the evening, at the manor.

    call change_time(13, 30)

    $ change_room('forest_edge', dissolve)

    # TODO: Two shots from the western grove, close together, and then a cry.

    $ play_music('danger', 2)

    $ change_room('forest_grove')

    # TODO: Doctor Baldwin dead in the fern. Her second body of the day, and this
    #       one was no more planned than the first.
    # TODO: She is of no use whatsoever and says so. The Captain takes charge of
    #       the stretcher, which suits her, since she has nothing to give.
    # TODO: The slow walk back through the ferns, and the thing she cannot say
    #       aloud: two dead in a house opened by a gentleman she has never met.

    jump work_in_progress
