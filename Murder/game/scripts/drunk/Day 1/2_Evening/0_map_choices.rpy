# Map choices for the Drunk (Samuel Manning), Friday evening
#
# After the letter, before the billiard room. Going to the billiard room ends
# the map: he drinks there until he falls asleep (2_billiard_room.rpy).
# His own room is the retire exit, so it is not listed here.

label drunk_day1_evening_map_menu:
    python:
        drunk_day1_evening_map_menu = TimedMenu(
            "drunk_day1_evening_map_menu",
            [
            # Servants' floor
            map_choice('kitchen', 'drunk_day1_evening_kitchen', 20),
            map_choice('scullery', 'drunk_day1_evening_scullery', 10),
            map_choice('garage', 'drunk_day1_evening_garage', 10),
            map_choice('gun_room', 'drunk_day1_evening_gun_room', 10),
            # Ground floor
            map_choice('tea_room', 'drunk_day1_evening_tea_room', 10),
            map_choice('dining_room', 'drunk_day1_evening_dining_room', 10),
            map_choice('manor_garden', 'drunk_day1_evening_garden', 10),
            map_choice('entrance_hall', 'drunk_day1_evening_entrance_hall', 10),
            map_choice('servant_stairs', 'drunk_day1_evening_servant_stairs', 10),
            map_choice('portrait_gallery', 'drunk_day1_evening_portrait_gallery', 10),
            map_choice('library', 'drunk_day1_evening_library', 20),
            # Bedrooms
            map_choice('bedroom_lad', 'drunk_day1_evening_bedroom_avoid'),
            map_choice('bedroom_host', 'drunk_day1_evening_bedroom_avoid'),
            map_choice('bedroom_broken', 'drunk_day1_evening_bedroom_avoid'),
            map_choice('bedroom_nurse', 'drunk_day1_evening_bedroom_avoid'),
            map_choice('bedroom_doctor', 'drunk_day1_evening_bedroom_avoid'),
            map_choice('bedroom_psychic', 'drunk_day1_evening_bedroom_avoid'),
            map_choice('bedroom_captain', 'drunk_day1_evening_bedroom_avoid'),
            # Attic
            map_choice('storage', 'drunk_day1_evening_attic_default'),
            map_choice('males_room', 'drunk_day1_evening_attic_default'),
            map_choice('females_room', 'drunk_day1_evening_attic_default'),
            map_choice('attic_butler_room', 'drunk_day1_evening_attic_default'),
            # Specific actions
            TimedMenuChoice('Go to the billiard room for a drink', 'drunk_day1_evening_billiard_room', 0, early_exit=True, room='billiard_room'),
            TimedMenuChoice('Retire for the night', 'generic_cancel', early_exit=True, room='bedroom_drunk'),
        ], is_map = True)

    return


# ------------------------------------
#   DOWNSTAIRS
# ------------------------------------
label drunk_day1_evening_go_downstairs:

    if drunk_details.saved_variables['day1_evening_downstairs_visited']:

        return

    $ change_room('basement_stairs')

    # TODO add dialogs
    #   - First time below stairs

    $ drunk_details.saved_variables['day1_evening_downstairs_visited'] = True

    return


label drunk_day1_evening_kitchen:

    call drunk_day1_evening_go_downstairs

    $ change_room('kitchen')

    # TODO add dialogs
    #   - The maid alone with the dinner pots (host_day1_evening_kitchen)

    return


label drunk_day1_evening_scullery:

    call drunk_day1_evening_go_downstairs

    $ change_room('scullery')

    # TODO add dialogs
    #   - The rat poison on the shelf, cork out, half-empty (host_day1_evening_scullery)

    return


label drunk_day1_evening_garage:

    call drunk_day1_evening_go_downstairs

    $ change_room('garage')

    # TODO add dialogs

    return


label drunk_day1_evening_gun_room:

    call drunk_day1_evening_go_downstairs

    $ change_room('gun_room')

    # TODO add dialogs
    #   - Sporting guns behind glass, a handgun on the table (host_day1_evening_gun_room)

    return


# ------------------------------------
#   GROUND FLOOR
# ------------------------------------
label drunk_day1_evening_tea_room:

    $ change_room('tea_room')

    # TODO add dialogs
    #   - Already put straight, the glasses gone (host_day1_evening_tea_room). The couch he slept on

    return


label drunk_day1_evening_dining_room:

    $ change_room('dining_room')

    # TODO add dialogs
    #   - The staff clearing the last of the dinner service

    return


label drunk_day1_evening_garden:

    $ change_room('manor_garden')

    # TODO add dialogs
    #   - Rain, and the wind getting up

    return


label drunk_day1_evening_entrance_hall:

    $ change_room('entrance_hall')

    # TODO add dialogs

    return


label drunk_day1_evening_servant_stairs:

    $ change_room('servant_stairs')

    # TODO add dialogs
    #   - A footman's livery on its peg (broken_day1_evening_servant_stairs)

    return


label drunk_day1_evening_portrait_gallery:

    $ change_room('portrait_gallery')

    # TODO add dialogs

    return


label drunk_day1_evening_library:

    $ change_room('library')

    # TODO add dialogs
    #   - The genealogy left open at Claythorn (host_day1_evening_library)

    return


# ------------------------------------
#   BEDROOMS
# ------------------------------------
label drunk_day1_evening_bedroom_avoid:

    $ change_room('bedrooms_hallway')

    # TODO add dialogs

    # Block all bedrooms on the first refusal
    $ all_menus[drunk_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_lad'))
    $ all_menus[drunk_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_host'))
    $ all_menus[drunk_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_broken'))
    $ all_menus[drunk_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_nurse'))
    $ all_menus[drunk_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_doctor'))
    $ all_menus[drunk_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_psychic'))
    $ all_menus[drunk_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_captain'))

    return


# ------------------------------------
#   ATTIC (locked)
# ------------------------------------
label drunk_day1_evening_attic_default:

    $ all_menus[drunk_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[drunk_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[drunk_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[drunk_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('attic_butler_room'))

    $ change_room("attic_hallway")

    # TODO add dialogs
    #   - Every door locked (play sound door_locked)

    return
