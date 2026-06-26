# Generic, reusable location visits for Broken (Thomas Moody).
# These are the "nothing of consequence here" defaults, called from the map
# menus when a room has no special scene for the current chapter. The day's
# wrappers handle any floor-crossing (livery change) before calling these.

# ------------------------------------
#   GROUND FLOOR
# ------------------------------------
label broken_tea_room_default:

    $ change_room('tea_room')

    """
    The tea room stands empty now, the cups long since cleared away.

    Nothing here keeps me.
    """

    return


label broken_entrance_hall_default:

    $ change_room('entrance_hall')

    """
    The hall is quiet.

    Worn carpet, brass wanting polish. A house keeping up appearances on a thinning purse, as I marked when I first came in.

    I take its measure once more and move on.
    """

    return


label broken_portrait_gallery_default:

    $ change_room('portrait_gallery')

    """
    A gallery of Claythorns, generations of them frowning down out of their gilt frames.

    I study the faces out of habit, looking for the likeness that runs down a family line.

    There is nothing here that asks a question of me tonight.
    """

    return


label broken_library_default:

    $ change_room('library')

    """
    A decent library, better kept than the rest of the house.

    A heavy book lies open on the table — a dictionary of the landed gentry.

    But I don't have the time to read it.
    
    Tonight I have more important things to investigate.
    """

    return


# ------------------------------------
#   SERVANTS' FLOOR
# ------------------------------------
label broken_garage_default:

    $ change_room('garage')

    if broken_details.saved_variables.get("visited_garage"):

        """
        The garage is just as I left it.

        There is nothing more for me here.
        """

    else:

        $ broken_details.saved_variables["visited_garage"] = True

        """
        The air is thick with petrol and cold iron.

        A motor car stands in the middle of the room.

        An old tourer, well kept, though it has not been run in some time.

        Nothing else gets my attention.
        """

    return


label broken_gun_room_default:

    $ change_room('gun_room')

    """
    The gun room.

    There is a rack of sporting guns behind glass, and on a table lies a handgun.

    That could prove useful.

    But if anyone notices me with a gun, that would attract questions I would rather avoid.

    So, I leave it as I found it.
    """

    return
