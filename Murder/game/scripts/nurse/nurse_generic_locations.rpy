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