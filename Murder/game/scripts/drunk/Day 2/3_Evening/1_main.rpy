# --------------------------------------------
#   Drunk
#
#   Saturday - Evening
#
#   15:00 -> 23:30
#
#   Music: sad for the return, mysterious for the room, danger for the night
#
#   Position
#       - House    : host, captain, lad, psychic, nurse, butler
#       - Confined : drunk, locked in his room
#       - Dead     : broken (Thomas Moody), doctor (Daniel Baldwin)
#
# --------------------------------------------
label drunk_day2_evening:

    call change_time(15, 00, 'Evening', 'Saturday', hide_minutes=True, chapter='saturday_evening')

    $ drunk_details.add_checkpoint("drunk_day2_evening")

    call black_screen_transition("Samuel Manning", chapters_names[current_chapter])

    $ drunk_mode = False

    $ change_room('entrance_hall', irisout)

    $ play_music('sad', 2)

    # TODO add dialogs

    call drunk_day2_evening_accusation

    call drunk_day2_evening_telephone

    call drunk_day2_evening_confined

    # ------------------------------------
    #   The room. The long think.
    # ------------------------------------

    # TODO add dialogs

    call drunk_day2_evening_think_loop

    # ------------------------------------
    #   The choice. What a man does with a locked door.
    # ------------------------------------

    # TODO add dialogs

    $ time_left = 1
    call run_menu(TimedMenu("drunk_day2_evening_menu_choice", [
        TimedMenuChoice('Play dead. Port for blood, a razor for the edge', 'drunk_day2_evening_play_dead', early_exit=True, condition="drunk_details.threads.is_unlocked('understood') and drunk_details.objects.is_unlocked('port')"),
        TimedMenuChoice('Hammer on the door and warn the whole house', 'drunk_day2_evening_confront', early_exit=True, condition="drunk_details.threads.is_unlocked('understood')"),
        TimedMenuChoice('Accept it, and drink', 'drunk_day2_evening_drink', early_exit=True),
    ]))

    return


# ------------------------------------
#   The accusation in the hall
# ------------------------------------
label drunk_day2_evening_accusation:

    # TODO add dialogs

    return


# ------------------------------------
#   The telephone call, watched
# ------------------------------------
label drunk_day2_evening_telephone:

    # TODO add dialogs

    return


# ------------------------------------
#   Confined. The Captain walks him up.
# ------------------------------------
label drunk_day2_evening_confined:

    # TODO add dialogs

    return


# ------------------------------------
#   The think loop
# ------------------------------------
label drunk_day2_evening_think_loop:

    $ current_character.saved_variables["day2_evening_think_menu"].early_exit = False

    $ time_left = TIME_MAX
    call run_menu(current_character.saved_variables["day2_evening_think_menu"])

    call drunk_day2_evening_think_conclusion

    return


# The three topics that make the picture whole are the letter, the telephone
# call and the butler. Think through all three and 'understood' unlocks.
label drunk_day2_evening_think_conclusion:

    python:
        _topics = drunk_details.saved_variables["day2_evening_topics"]
        _key = {"letter", "telephone", "butler"}
        _has_all = _key.issubset(set(_topics))

    if _has_all and not drunk_details.threads.is_unlocked('understood'):

        $ drunk_details.threads.unlock('understood')

        # TODO add dialogs

    return


# ------------------------------------
#   The topics
# ------------------------------------
label drunk_day2_evening_think_letter:

    $ drunk_details.saved_variables["day2_evening_topics"].append("letter")

    # TODO add dialogs

    return


label drunk_day2_evening_think_moody:

    # TODO add dialogs

    return


label drunk_day2_evening_think_telephone:

    $ drunk_details.saved_variables["day2_evening_topics"].append("telephone")

    if not drunk_details.observations.is_unlocked('phone_call'):
        $ drunk_details.observations.unlock('phone_call')

    # TODO add dialogs

    return


label drunk_day2_evening_think_butler:

    $ drunk_details.saved_variables["day2_evening_topics"].append("butler")

    if not drunk_details.observations.is_unlocked('butler_face'):
        $ drunk_details.observations.unlock('butler_face')

    # TODO add dialogs

    return


label drunk_day2_evening_think_psychic:

    # TODO add dialogs

    return


label drunk_day2_evening_think_self:

    # TODO add dialogs

    return
