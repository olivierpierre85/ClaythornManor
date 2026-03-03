label nurse_bedroom_default:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    nurse """
    Hello? Is anyone there?
    """

    """
    No answer.
    """

    return

label nurse_bedroom_lockpick_choice(search_label):

    if not nurse_details.saved_variables["lockpick_seen"]:

        $ nurse_details.saved_variables["lockpick_seen"] = True

        """
        The door is locked.

        It would take very little effort to open it.

        In my years of nursing, one becomes acquainted with all manner of locks — on medicine cabinets, ward doors, supply rooms.

        This is nothing remarkable.
        """

    call run_menu(TimedMenu("nurse_day1_evening_lockpick_" + search_label, [
        TimedMenuChoice("Pick the lock and go in.", search_label, 10, early_exit=True, keep_alive=True),
        TimedMenuChoice("No. Leave it.", 'generic_cancel', early_exit=True, keep_alive=True),
    ]))

    return

# Possible searches for treasure => Only after day 2 (during the hunt there is nobody)

label nurse_day1_evening_search_captain:

    $ change_room("bedrooms_hallway")

    play sound door_locked

    """
    The room is neat to the point of severity.

    A coat hangs straight on its hook.

    A leather case sits unpacked on the stand, its straps buckled precisely.

    Nothing is left in reach.

    Military discipline of this kind belongs to one man in this house.

    And whatever the Captain values, he keeps it close to his person.
    """

    $ unlock_map('bedroom_captain')

    return


label nurse_day1_evening_search_host:

    $ change_room("bedroom_host")

    """
    The room is larger than mine, dressed in pale silks and heavy curtains.

    This is unquestionably the lady of the house's own chamber.

    I look quickly through the dressing table.

    A jet brooch, a few hairpins, a string of garnets in a velvet case.

    They catch my eye for a moment.
    """

    $ unlock_map('bedroom_host')

    call run_menu(TimedMenu("nurse_day1_evening_search_host_choice", [
        TimedMenuChoice("Take the garnets.", 'nurse_day1_evening_take_garnets', 5, early_exit=True),
        TimedMenuChoice("Leave them. It's not worth the risk.", 'generic_cancel', early_exit=True),
    ]))

    return


label nurse_day1_evening_take_garnets:

    """
    Not first rate, but they will fetch something.

    I slip the case into my bag and close the drawer as I found it.
    """

    $ nurse_details.threads.unlock('steal_garnets')

    return


label nurse_day1_evening_search_lad:

    $ change_room("bedrooms_hallway")

    """
    There isn't much in here.

    A jacket thrown over the chair, a battered holdall on the floor.

    There is nothing here worth taking.

    A young man travelling light and spending freely is unlikely to be carrying anything of value.
    """

    return


label nurse_day1_evening_search_broken:

    $ change_room("bedrooms_hallway")

    """
    I push the door open.

    It is dark inside, and quieter than it ought to be.

    The room has a stillness to it that gives me pause.

    Nothing on the dressing table.

    A small case under the bed, locked.

    I close the door softly and leave.
    """

    return


label nurse_day1_evening_search_doctor:

    $ change_room("bedrooms_hallway")

    """
    A doctor's bag sits open on the small writing desk.

    Instruments, a bottle of laudanum, a notebook with the clasp shut.

    There is no mistaking whose room this is.

    I know better than to disturb another's bag.

    Partly professional courtesy.

    Partly because there is nothing in there I could make use of.
    """

    $ unlock_map('bedroom_doctor')

    return

label nurse_garage_default:

    if nurse_details.saved_variables.get("visited_garage"):

        $ change_room("garage")

        """
        I have already seen everything there was to see here.
        """

    else:

        $ nurse_details.saved_variables["visited_garage"] = True

        $ change_room("garage")

        """
        I reach the garage, making sure I wouldn't encounter anyone.

        It is a cold, oil-smelling place.

        There is an old car, it doesn't look like it's working anymore.

        Tools hang neatly along one wall, and a bicycle leans against another.

        Nothing here that is of any use to me.
        """

    return


label nurse_gun_room_default:

    if nurse_details.saved_variables.get("visited_gun_room"):

        $ change_room("gun_room")

        if nurse_details.threads.is_unlocked('take_gun'):

            """
            I have already seen everything there was to see here.
            """

            return

        else:

            """
            The rows of weapons remain exactly as they were.
            """

    else:

        $ nurse_details.saved_variables["visited_gun_room"] = True

        $ change_room("gun_room")

        """
        The gun room.
        
        I am confident that I shouldn't be here, so I made sure no one notices me.

        Shotguns and hunting rifles line three walls, arranged on open racks.

        The smell of gun oil is sharp.

        Everything is laid out as though ready for use — nothing locked away.
        """

    if not nurse_details.threads.is_unlocked('take_gun'):
        call run_menu(TimedMenu("nurse_gun_room_choice", [
            TimedMenuChoice("Take a pistol", 'nurse_take_gun', 20, early_exit=True),
            TimedMenuChoice("Leave it. Too dangerous to carry.", 'generic_cancel', 20, early_exit=True),
        ]))

    return


label nurse_take_gun:

    """
    My hand closes around the grip of a small revolver.

    It is loaded.

    I slip it into my bag.

    Nobody will notice. Not for a while, at any rate.
    """

    $ nurse_details.threads.unlock('take_gun')

    return


label nurse_downstairs_approach:

    """
    I move quietly through the back passage.

    Years of moving through dark passages in hospitals and large houses have taught me how to remain unseen.

    I reach the kitchen door and ease it open an inch.
    """

    return