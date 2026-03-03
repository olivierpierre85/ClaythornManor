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

    call run_menu(TimedMenu("nurse_lockpick_default_" + search_label, [
        TimedMenuChoice("Pick the lock and go in.", search_label, 10, early_exit=True, keep_alive=True),
        TimedMenuChoice("No. Leave it.", 'generic_cancel', early_exit=True, keep_alive=True),
    ]))

    return

# Possible searches for treasure => Only after day 2 (during the hunt there is nobody)

label nurse_search_captain_default:

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


label nurse_search_host_default:

    $ change_room("bedroom_host")

    """
    The room is larger than mine, dressed in pale silks and heavy curtains.

    This is unquestionably the lady of the house's own chamber.

    I look quickly through the dressing table.

    A jet brooch, a few hairpins, a string of garnets in a velvet case.

    They catch my eye for a moment.
    """

    $ unlock_map('bedroom_host')

    call run_menu(TimedMenu("nurse_search_host_choice_default", [
        TimedMenuChoice("Take the garnets.", 'nurse_take_garnets', 5, early_exit=True),
        TimedMenuChoice("Leave them. It's not worth the risk.", 'generic_cancel', early_exit=True),
    ]))

    return


label nurse_take_garnets:

    """
    Not first-rate, but they will fetch something.

    I slip the case into my bag and close the drawer as I found it.
    """

    $ nurse_details.threads.unlock('steal_garnets')

    return


label nurse_search_lad_default:

    $ change_room("bedrooms_hallway")

    """
    There isn't much in here.

    A jacket thrown over the chair, a battered holdall on the floor.

    There is nothing here worth taking.

    A young man travelling light and spending freely is unlikely to be carrying anything of value.
    """

    return


label nurse_search_broken_default:

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


label nurse_search_doctor_default:

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
        It looks exactly the same as before.

        No need to search any further.
        """

    else:

        $ nurse_details.saved_variables["visited_garage"] = True

        $ change_room("garage")

        """
        I reach the garage, making sure I should not encounter anyone.

        It is a cold, oil-smelling place.

        There is an old car; it does not look as though it is working any more.

        Tools hang neatly along one wall, and a bicycle leans against another.

        Nothing here that is of any use to me.
        """

    return


label nurse_gun_room_default:

    if nurse_details.saved_variables.get("visited_gun_room"):

        $ change_room("gun_room")

        if nurse_details.threads.is_unlocked('take_gun'):

            """
            There is nothing new in here.

            I search a bit more for bullets, but still cannot find any.

            So there is no reason to stay here.
            """

            return

        else:

            """
            The rows of weapons remain exactly as they were.

            The small pistols are still available if I so desire.
            """

    else:

        $ nurse_details.saved_variables["visited_gun_room"] = True

        $ change_room("gun_room")

        """
        The gun room.
        
        I am confident that I should not be here, so I made sure no one noticed me.

        Shotguns and hunting rifles line three walls, arranged on open racks.

        The smell of gun oil is sharp.

        Everything is laid out as though ready for use — nothing locked away.

        There are even a few small handguns lying on a table.

        It looks like something I could use.
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

    It is not loaded.

    And I have not seen any bullets lying about.

    Nevertheless, it could prove useful.

    I slip it into my bag.

    Nobody will notice. Not for a while, at any rate.
    """

    $ nurse_details.threads.unlock('take_gun')

    return


label nurse_tea_room_default:

    $ change_room('tea_room')

    """
    The room is quite empty.

    The teapot has gone cold.

    There is nothing to keep me here.
    """

    return


label nurse_entrance_hall_default:

    $ change_room('entrance_hall')

    """
    The great hall is quiet.

    The chandelier has been turned down low.

    I stand beneath it for a moment, listening.

    The house settles around me.

    There is something watchful about the place at this hour.
    """

    return


label nurse_downstairs_approach:

    """
    I move quietly through the back passage.

    Years of moving through dark passages in hospitals and large houses have taught me how to remain unseen.

    I reach the kitchen door and ease it open an inch.
    """

    return


label nurse_library_default:

    if nurse_details.saved_variables.get("visited_library"):

        $ change_room("library")

        if nurse_details.threads.is_unlocked('captain_zanzibar'):

            """
            There is nothing more for me to find here.

            I already know what I need to know about Zanzibar.
            """

            return

        else:

            """
            The library remains as it was.

            The volumes of "A History of the British Army" are still on the shelf.
            """

    else:

        $ nurse_details.saved_variables["visited_library"] = True

        $ change_room("library")

        """
        A well-appointed library.

        "A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain" lies open on a table.

        I cast my eye along the shelves.

        Mostly heraldry, county histories, and bound journals.

        Nothing worth taking — far too heavy, and of no particular value.

        I am about to leave when a title catches my attention.

        "A History of the British Army" — Fortescue.

        Fourteen volumes.

        I have seen this set before, in the officers' mess at Netley.

        The Captain mentioned Zanzibar at some point, I remember.

        Something in the way he spoke of it nagged at me, though I could not quite place it at the time.

        I could try to learn more about that conflict, though it may take some time.
        """

    if not nurse_details.threads.is_unlocked('captain_zanzibar'):
        call run_menu(TimedMenu("nurse_library_choice", [
            TimedMenuChoice("Look it up. It may be useful.", 'nurse_library_war_book', 30, early_exit=True),
            TimedMenuChoice("Leave it. I am too tired for reading.", 'generic_cancel', 20, early_exit=True),
        ]))

    return


label nurse_library_war_book:

    """
    I take down the volume covering the latter campaigns in India and East Africa.

    I find the index and look up Zanzibar.

    A single page.

    The engagement lasted thirty-eight minutes.

    The shortest war in recorded history, apparently.

    The British bombardment was overwhelming.

    Casualties on the British side were minimal — one man, lightly wounded.

    If what the Captain said is true, he would be the only injured soldier from the entire war.

    That seems most unlikely.

    He may well have invented the whole story — but to what end?
    """

    $ nurse_details.threads.unlock('captain_zanzibar')

    return


label nurse_portrait_gallery_default:

    if nurse_details.saved_variables.get("visited_portrait_gallery"):

        $ change_room('portrait_gallery')

        """
        The portraits remain as they were, their silent judgement unchanged.

        There is nothing here for me.
        """

    else:

        $ nurse_details.saved_variables["visited_portrait_gallery"] = True

        $ change_room('portrait_gallery')

        """
        The gallery is lit by a single gas lamp.

        The Claythorn ancestors gaze down from their frames with an air of collective disapproval.

        I feel rather as though I am being assessed.

        I do not linger.
        """

    return