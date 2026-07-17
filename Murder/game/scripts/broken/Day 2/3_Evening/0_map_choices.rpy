# Map choices for Broken (Thomas Moody), Saturday night.

label broken_day2_evening_map_menu:
    python:
        broken_day2_evening_map_menu = TimedMenu(
            "broken_day2_evening_map_menu",
            [
            # Servants' floor (open tonight, and deserted - see header comment)
            map_choice('kitchen', 'broken_day2_evening_kitchen', 10),
            map_choice('scullery', 'broken_day2_evening_scullery', 10),
            map_choice('garage', 'broken_day2_evening_garage', 10),
            map_choice('gun_room', 'broken_day2_evening_gun_room', 10),
            # Ground floor
            map_choice('tea_room', 'broken_day2_evening_tea_room', 10),
            map_choice('dining_room', 'broken_day2_evening_dining_room', 10),
            map_choice('entrance_hall', 'broken_day2_evening_entrance_hall', 10),
            map_choice('manor_garden', 'broken_day2_evening_garden', 10),
            map_choice('servant_stairs', 'broken_day2_evening_servant_stairs', 10),
            map_choice('portrait_gallery', 'broken_day2_evening_portrait_gallery', 10),
            map_choice('library', 'broken_day2_evening_library', 10),
            # Bedrooms (his own room is the retire exit, so it is not listed here)
            map_choice('bedroom_lad', 'broken_day2_evening_bedroom_lad', 10),
            map_choice('bedroom_host', 'broken_day2_evening_bedroom_host', 10),
            map_choice('bedroom_nurse', 'broken_day2_evening_bedroom_nurse', 10),
            map_choice('bedroom_doctor', 'broken_day2_evening_bedroom_doctor', 10),
            map_choice('bedroom_drunk', 'broken_day2_evening_bedroom_drunk', 10),
            map_choice('bedroom_psychic', 'broken_day2_evening_bedroom_psychic', 10),
            map_choice('bedroom_captain', 'broken_day2_evening_bedroom_captain', 10),
            # Attic
            map_choice('storage', 'broken_day2_evening_attic_default', 10),
            map_choice('males_room', 'broken_day2_evening_attic_default', 10),
            map_choice('females_room', 'broken_day2_evening_attic_default', 10),
            map_choice('attic_butler_room', 'broken_day2_evening_attic_default', 10),
            # Specific actions
            # keep_alive: the Captain's questions need facts gathered around
            # the house, so the player must be able to come back here.
            TimedMenuChoice('Look in on the billiard room', 'broken_day2_evening_billiard_room', 20, keep_alive=True, room='billiard_room'),
            TimedMenuChoice('Turn in for the night', 'generic_cancel', early_exit=True, room='bedroom_broken'),
        ], is_map = True)

    return

# ------------------------------------
#   SERVANTS' FLOOR
# ------------------------------------
# Deserted tonight: the staff are nowhere to be found, and each room shows a
# piece of the flight being prepared for four in the morning.
# The kitchen, scullery, gun room and attic each add one mark to the
# day2_evening_staff_oddities count. All four marks are needed to unlock
# staff_missing. The garage carries no clue and stays out of the count.
label broken_day2_evening_kitchen:

    call broken_day2_evening_descend

    $ change_room('kitchen')

    """
    The kitchen is empty, and the fire is not burning.

    There should be someone here, banking the coals for the morning at the very least.

    Nobody has troubled to see to it, which makes preparing breakfast tomorrow a hard task.
    """

    call broken_day2_evening_staff_oddity

    return


label broken_day2_evening_scullery:

    call broken_day2_evening_descend

    $ change_room('scullery')

    """
    The scullery is cold and empty.

    On the sink there are several unwashed pots and pans.

    Nobody bothered to clean the dishes tonight.
    """

    call broken_day2_evening_staff_oddity

    return


label broken_day2_evening_garage:

    call broken_day2_evening_descend

    call broken_garage_default

    return


label broken_day2_evening_gun_room:

    call broken_day2_evening_descend

    $ change_room('gun_room_empty')

    """
    The gun room.

    The rack behind the glass stands empty, nothing left on it but the pegs.

    The butler carried the rifles from the hunt back down here himself when we came in.

    They are not here now.

    Every gun in this house has been gathered up and carried off somewhere.
    """

    call broken_day2_evening_staff_oddity

    return


# One mark per room, in whatever order the player finds them. The reflection
# escalates with the count, and the fourth mark settles the question.
label broken_day2_evening_staff_oddity:

    $ broken_details.saved_variables['day2_evening_staff_oddities'] += 1

    if broken_details.saved_variables['day2_evening_staff_oddities'] == 1:

        """
        That is rather odd.

        But I should not jump to conclusions.
        """

    elif broken_details.saved_variables['day2_evening_staff_oddities'] == 2:

        """
        Another strange thing.

        But there must be a reasonable explanation.

        There usually is.
        """

    elif broken_details.saved_variables['day2_evening_staff_oddities'] == 3:

        """
        That is becoming weirder.

        I am running out of explanations for the staff actions.

        Where could they all be?        
        """

    elif broken_details.saved_variables['day2_evening_staff_oddities'] == 4:

        """
        Now that is concerning.

        That is too many oddities to be an accident.

        Something is happening here, and I can think of only one explanation.

        The staff are gone, and they do not intend to come back.
        """

        $ broken_details.threads.unlock('staff_missing')

    return


# ------------------------------------
#   BEDROOMS
# ------------------------------------
label broken_day2_evening_bedroom_doctor:

    $ change_room('bedrooms_hallway')

    play sound door_knock

    """
    I knock at Doctor Baldwin's door. Nothing.
    """

    play sound door_knock

    """
    I knock a second time, harder.

    From within comes a mumble, the creak of a bed.

    Doctor Baldwin is there, but he won't come out.
    """

    return


label broken_day2_evening_bedroom_psychic:

    $ change_room('bedrooms_hallway')

    play sound door_knock

    """
    I knock at Miss Baxter's door, and give my name.

    But she is not answering.
    """

    return


label broken_day2_evening_bedroom_nurse:

    $ change_room('bedrooms_hallway')

    play sound door_knock

    """
    I knock at Miss Marsh's door.

    No answer.

    But I can't blame her if she wants to be alone tonight.
    """

    return


label broken_day2_evening_bedroom_host:

    $ change_room('bedrooms_hallway')

    play sound door_knock

    """
    I knock.

    No answer.

    It is probably best.

    Confronting Lady Claythorn alone, and at this hour, might have been a bad idea.
    """

    return


label broken_day2_evening_bedroom_captain:

    $ change_room('bedrooms_hallway')

    play sound door_knock

    """
    I knock. 
    
    No light beneath the door, and no answer.
    """

    return

label broken_day2_evening_bedroom_drunk:

    $ change_room('bedrooms_hallway')

    play sound door_knock

    """
    I knock.

    The door is not closed, so my touch is enough to open it.

    From the hallway I glance into a room in a poor state.

    There is nobody inside.

    I do not go in. I do not want to be caught in someone else's room.
    """

    return


label broken_day2_evening_bedroom_lad:

    $ change_room("bedroom_lad")

    """
    I enter Ted Harring's room.

    His body is still on the bed, with bedsheets covering his face.

    I don't know what possessed me to come here.

    It is not as if I could learn anything from a dead man.

    I prepare to turn back when I spot something peculiar.

    A single rose has been laid next to him.

    Somebody has been grieving strongly enough to want to show their affection.

    But nobody in this house is supposed to have known him.

    How peculiar.
    """

    return


# ------------------------------------
#   ATTIC
# ------------------------------------
label broken_day2_evening_attic_default:

    $ all_menus[broken_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[broken_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[broken_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[broken_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('attic_butler_room'))

    $ change_room('attic_hallway')

    """
    I climb the attic stair and knock.
    """

    play sound door_knock

    """
    No answer, no light beneath it, and everything up here is quiet. 

    I try the handle.
    """

    play sound door_locked

    """
    Closed, and it will not open.

    I go along the corridor, knocking and trying every other door in turn.
    """

    play sound door_locked

    """
    Closed, all of them, and the same silence behind each.

    Either the staff sleep like the dead, or there is nobody up here at all.
    """

    call broken_day2_evening_staff_oddity

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

    Everything in perfect order.

    No reason to linger.
    """

    return


label broken_day2_evening_entrance_hall:

    $ change_room('entrance_hall')

    """
    The hall stands empty.
    
    I find the telephone, its on a table behind the stair.

    I lift the receiver and hold it to my ear.

    Nothing.

    No operator, no crackle from the exchange. 
    
    A dead silence.

    Yet our hostess telephoned the police station this very evening, or so she told us at dinner.

    Either the line has died since, or no call was ever placed.

    I set the receiver back on its cradle.
    """

    $ broken_details.threads.unlock('phone_dead')

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


label broken_day2_evening_servant_stairs:

    $ change_room('servant_stairs')

    """
    The footman livery is still there where I left it.
    """

    if not broken_details.saved_variables['day2_evening_no_pretence']:

        call broken_day2_evening_no_pretence

    """
    I stand at the head of the stair and listen.

    Nothing comes up from below. No footsteps, no voices, not so much as a clatter of pans.
    """


    return


# The reflection that ends the disguise. Fired once, from the servant stair or
# from the first room below stairs, whichever the player reaches first.
label broken_day2_evening_no_pretence:

    $ broken_details.saved_variables['day2_evening_no_pretence'] = True

    """
    Last night I would not have set foot below stairs without a disguise.

    Tonight I do not think it is still necessary.
    
    This whole weekend has become too dangerous to waste any more time.
    """

    return


# Going below stairs: the first crossing plays the no-pretence reflection in
# the stairwell on the way down. After that it costs nothing.
label broken_day2_evening_descend:

    if not broken_details.saved_variables['day2_evening_no_pretence']:

        $ change_room("basement_stairs")

        call broken_day2_evening_no_pretence

    return


label broken_day2_evening_portrait_gallery:

    call broken_portrait_gallery_default

    return


label broken_day2_evening_library:

    call broken_library_default

    return


label broken_day2_evening_billiard_room:

    # The evening's real content: Captain Sinha reads, Mr Manning drinks.
    call broken_day2_evening_billiard_room_scene

    return
