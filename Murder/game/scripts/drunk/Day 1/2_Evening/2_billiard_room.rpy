# ------------------------------------
#   BILLIARD ROOM (ends the map)
#   He drinks until he falls asleep, and wakes alone.
#   -> raided_bar + port, or the bottles left on the bar
#
#   What the others see of him here:
#       - at the bar, slumped against the counter (captain, broken, host)
#       - Moody tipping the last of the whisky into his flask beside him, then
#         offering it to Harring (common_day1_evening_moody_offers_harring_flask)
#       - Harring to Miss Baxter: "Don't mind Mr Manning" (psychic)
#       - the Captain's story by the fire
#         (common_day1_evening_captain_billiard_room_speech_part_1 / _part_2)
# ------------------------------------
label drunk_day1_evening_billiard_room:

    $ change_room('billiard_room')

    $ drunk_details.saved_variables["day1_evening_billiard_room_visited"] = True

    # TODO add dialogs
    #   - The party. He makes straight for the bar
    #   - If he put the bottle down (no day1_drink), he only plays the drunk from here

    call run_menu(TimedMenu("drunk_day1_evening_billiard_room_menu", [
        TimedMenuChoice("Pour yourself a drink", 'drunk_day1_evening_billiard_room_bar_1', 20),
        TimedMenuChoice("Pour yourself another", 'drunk_day1_evening_billiard_room_bar_2', 20, condition="is_choice_hidden('drunk_day1_evening_billiard_room_menu', 'drunk_day1_evening_billiard_room_bar_1')"),
        TimedMenuChoice("One more, and that will be the last", 'drunk_day1_evening_billiard_room_bar_3', 20, condition="is_choice_hidden('drunk_day1_evening_billiard_room_menu', 'drunk_day1_evening_billiard_room_bar_2')"),
        TimedMenuChoice("Listen to Captain Sinha's story", 'drunk_day1_evening_billiard_room_captain', 30),
        TimedMenuChoice("Close your eyes for a moment", 'generic_cancel', early_exit=True),
    ]))

    $ stop_music()

    call wait_screen_transition()

    call change_time(23, 45)

    # TODO add dialogs
    #   - He wakes in the empty room. The fire is low, the bottles still on the bar

    $ time_left = 1

    call run_menu(TimedMenu("drunk_day1_evening_menu_bar", [
        TimedMenuChoice("Take every bottle worth the name up to your room", 'drunk_day1_evening_raid_bar', early_exit=True),
        TimedMenuChoice("Leave them on the bar", 'drunk_day1_evening_leave_bar', early_exit=True),
    ]))

    return


# ------------------------------------
#   THE BAR (every glass counts, see day1_drinks in drunk_config.rpy)
# ------------------------------------
label drunk_day1_evening_billiard_room_bar_1:

    $ drunk_details.saved_variables["day1_drinks"] += 1

    # TODO add dialogs

    return


label drunk_day1_evening_billiard_room_bar_2:

    $ drunk_details.saved_variables["day1_drinks"] += 1

    # TODO add dialogs

    return


label drunk_day1_evening_billiard_room_bar_3:

    $ drunk_details.saved_variables["day1_drinks"] += 1

    # TODO add dialogs

    return


label drunk_day1_evening_billiard_room_captain:

    # TODO add dialogs
    #   - The Captain's war story, from the bar

    return


# ------------------------------------
#   WAKING ALONE
# ------------------------------------
label drunk_day1_evening_raid_bar:

    $ drunk_details.threads.unlock('raided_bar')

    $ drunk_details.objects.unlock('port')

    # TODO add dialogs
    #   - Every bottle worth the name, the port among them, carried up the stairs

    return


label drunk_day1_evening_leave_bar:

    # TODO add dialogs

    return
