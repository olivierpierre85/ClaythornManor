# Map choices for Broken (Thomas Moody), Saturday evening (found_poison path).
#
# A smaller map than Friday's: it is past nine, the house is retiring, and he
# has resolved to stay awake. No livery mechanics tonight - he keeps to the
# guest floors as himself. The billiard room carries the evening's real
# content (Captain Sinha and a sober Mr Manning - see 2_billiard_room.rpy);
# the rest are the generic defaults.
#
# The early exit ("Take up your watch for the night") ends the exploration and
# leads into the night vigil in 1_main.rpy.


label broken_day2_evening_map_menu:
    python:
        broken_day2_evening_map_menu = TimedMenu(
            "broken_day2_evening_map_menu",
            [
            # Ground floor
            TimedMenuChoice(default_room_text('tea_room'), 'broken_day2_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'broken_day2_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'broken_day2_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('manor_garden'), 'broken_day2_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'broken_day2_evening_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('library'), 'broken_day2_evening_library', 10, room='library'),
            # Specific actions
            TimedMenuChoice('Join the others in the billiard room', 'broken_day2_evening_billiard_room', 10, room='billiard_room'),
            TimedMenuChoice('Take up your watch for the night', 'generic_cancel', early_exit=True, room='bedroom_broken'),
        ], is_map = True)

    return


# ------------------------------------
#   GROUND FLOOR
# ------------------------------------
label broken_day2_evening_tea_room:

    call broken_tea_room_default

    return


label broken_day2_evening_dining_room:

    $ change_room('dining_room')

    """
    The table has been cleared, the cloth drawn, the chairs set straight.

    Everything in perfect order, as though the household meant to be judged on it.

    Nothing here but the ghost of an empty chair.
    """

    return


label broken_day2_evening_entrance_hall:

    call broken_entrance_hall_default

    return


label broken_day2_evening_garden:

    $ change_room('manor_garden')

    """
    The night is cold and moonless, and the wood stands like a wall at the edge of the lawn.

    Somewhere beyond it lies a road with a tree across it.

    Nothing to be learned out here but how dark a Scottish night can be.

    I step back inside.
    """

    return


label broken_day2_evening_portrait_gallery:

    call broken_portrait_gallery_default

    return


label broken_day2_evening_library:

    call broken_library_default

    return
