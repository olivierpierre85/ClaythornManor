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


label broken_dining_room_default:

    $ change_room('dining_room')

    """
    The staff are clearing the last of the dinner service.

    I have no wish to be underfoot, so I do not linger.
    """

    return


label broken_entrance_hall_default:

    $ change_room('entrance_hall')

    """
    The hall is quiet at this hour.

    Worn carpet, brass wanting polish. A house keeping up appearances on a thinning purse, as I marked when I first came in.

    I take its measure once more and move on.
    """

    return


label broken_portrait_gallery_default:

    $ change_room('portrait_gallery')

    """
    A gallery of Claythorns, generations of them frowning down out of their gilt frames.

    I study the faces out of habit, looking for the likeness that runs down a family line.

    It is the one thing the mask has never stopped me doing.

    There is nothing here that asks a question of me tonight.
    """

    return


label broken_library_default:

    $ change_room('library')

    """
    A decent library, better kept than the rest of the house.

    A heavy book lies open on the table — a dictionary of the landed gentry.

    I know the use of a book like that, even if I am no great reader.

    Another time, perhaps. Tonight I would sooner walk the house than sit and read about it.
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
        A motor car stands under a dust sheet, and the air is thick with petrol and cold iron.

        I draw the sheet back a little.

        An old tourer, well kept, though it has not been run in some time.

        Force of habit has me looking it over — the tyres, the plugs, the state of the engine.

        Whatever else I have set aside for this masquerade, the hands of a mechanic do not forget their trade.

        Still, there is nothing here that speaks to the business that brought me to this house.

        I let the sheet fall and leave it be.
        """

    return


label broken_gun_room_default:

    $ change_room('gun_room')

    """
    The gun room.

    A rack of sporting guns behind glass.

    Locked.

    On a table lies a handgun.

    That could prove useful.

    But ever since the war, I have avoided guns when I can.

    So, I leave it as I found it.
    """

    return
