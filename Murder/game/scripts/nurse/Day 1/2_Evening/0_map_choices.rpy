# Map choices for Nurse, Friday evening
label nurse_day1_evening_map_menu:
    python:        
        # Map choices
        nurse_day1_evening_map_menu = TimedMenu(
            "nurse_day1_evening_map_menu", 
            [
            # Default values
            TimedMenuChoice(default_room_text('storage'), 'nurse_day1_evening_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'nurse_day1_evening_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'nurse_day1_evening_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'nurse_day1_evening_butler_room', 10, room='butler_room'),
            #bedroom
            TimedMenuChoice(default_room_text('bedroom_lad'), 'nurse_day1_evening_bedroom_lad', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'nurse_day1_evening_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'nurse_day1_evening_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_broken'), 'nurse_day1_evening_bedroom_broken', 10, room='bedroom_broken'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'nurse_day1_evening_bedroom_doctor', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('tea_room'), 'nurse_day1_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'nurse_day1_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'nurse_day1_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'nurse_day1_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'nurse_day1_evening_portrait_gallery', 10, room='portrait_gallery'),
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'nurse_day1_evening_downstairs_crowded', 0, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'nurse_day1_evening_downstairs_crowded', 0, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'nurse_day1_evening_garage', 20, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'nurse_day1_evening_gun_room', 0, room='gun_room'),
            # Specific actions
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'nurse_day1_evening_bedroom_drunk', 10, room='bedroom_drunk', next_menu="nurse_day1_evening_bedroom_drunk"),
            TimedMenuChoice(default_room_text('library'), 'nurse_day1_evening_library', 0, next_menu="nurse_library_default", room='library'),
            TimedMenuChoice(
                default_room_text('bedroom_psychic'), 
                'nurse_day1_evening_bedroom_psychic', 
                10, 
                room = 'bedroom_psychic'
            ),
            TimedMenuChoice(
                'Meet the others in the billiard room', 
                'nurse_day1_evening_billiard_room', 
                0,
                room = 'billiard_room',
                next_menu = 'nurse_day1_evening_billiard_room_menu'
            ), 
            TimedMenuChoice(
                'Go rest for the night', 
                'generic_cancel', 
                early_exit = True, 
                room = 'bedroom_nurse'
            )
        ], is_map = True)
    
    return


label nurse_day1_evening_downstairs_crowded:

    # Hide both kitchen and scullery — they share the same discovery
    $ all_menus[nurse_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))
    $ all_menus[nurse_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('scullery'))

    $ change_room("basement_stairs")

    """
    I move quietly through the back passage.

    Years of night moving in the dark in large house taught me how to stay hidden.

    I reach the kitchen door and ease it open an inch.
    """

    $ change_room("kitchen")

    """
    I almost go in until I notice some of the staff. 
    
    They are busy cleaning today's meal.

    No chance of doing anything useful in there tonight.

    The scullery will be just the same, connected as it is to the kitchen.

    I pull the door to and leave without anyone having noticed me.
    """

    return


label nurse_day1_evening_garage:

    $ change_room("garage")

    """
    I reach the garage, making sure I wouldn't encounter anyone.

    It is a cold, oil-smelling place.

    There is an old car, it doesn't look like it's working anymore.

    Tools hang neatly along one wall, and a bicycle leans against another.

    Nothing here that is of any use to me.
    """

    return


label nurse_day1_evening_gun_room:

    $ change_room("gun_room")

    """
    The gun room.
    
    I am confident that I shouldn't be here, so I made sure no one notices me.

    Shotguns and hunting rifles line three walls, arranged on open racks.

    The smell of gun oil is sharp.

    Everything is laid out as though ready for use — nothing locked away.
    """

    call run_menu(TimedMenu("nurse_day1_evening_gun_room_choice", [
        TimedMenuChoice("Take a pistol", 'nurse_day1_evening_take_gun', 20, early_exit=True),
        TimedMenuChoice("Leave it. Too dangerous to carry.", 'generic_cancel', 20, early_exit=True),
    ]))

    return


label nurse_day1_evening_take_gun:

    """
    My hand closes around the grip of a small revolver.

    It is loaded.

    I slip it into my bag.

    Nobody will notice — not tonight, at any rate.
    """

    $ nurse_details.threads.unlock('take_gun')

    return


# First Floor
label nurse_day1_evening_library:

    $ change_room('library')

    """
    A well-appointed library.

    "A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain." lies open on a table.

    I cast my eye along the shelves.

    Mostly heraldry, county histories, and bound journals.

    Nothing worth taking — far too heavy, and of no particular value.

    I am about to leave when a title catches my attention.

    "A History of the British Army" — Fortescue.

    Fourteen volumes.

    I have seen this set before, in the officers' mess at Netley.

    The Captain mentioned Zanzibar at some point I remember.

    Something in the way he spoke of it nagged at me, though I could not quite place it at the time.

    I could try to learn more about that conflict, though it may take some time.
    """

    call run_menu(TimedMenu("nurse_library_default", [
        TimedMenuChoice("Look it up. It may be useful.", 'nurse_day1_evening_library_war_book', 30, early_exit=True),
        TimedMenuChoice("Leave it. I am too tired for reading tonight.", 'generic_cancel', 20, early_exit=True),
    ]))

    return


label nurse_day1_evening_library_war_book:

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


label nurse_day1_evening_tea_room:

    $ change_room('tea_room')

    """
    The room is quite empty.

    The teapot has gone cold.

    There is nothing to keep me here.
    """

    return


label nurse_day1_evening_dining_room:

    $ change_room('dining_room')

    """
    The dining room is deserted.

    The staff are clearing away the last of the dishes.

    I receive a faintly puzzled look from the footman.

    I offer no explanation and withdraw.
    """

    return


label nurse_day1_evening_garden:

    $ change_room('entrance_hall')

    """
    I step towards the front door.

    A draught finds its way under the frame.

    The weather has worsened considerably since this afternoon.

    I am not well enough to be wandering about in the cold and the dark.

    I turn back.
    """

    return


label nurse_day1_evening_entrance_hall:

    $ change_room('entrance_hall')

    """
    The great hall is quiet.

    The chandelier has been turned down low.

    I stand beneath it for a moment, listening.

    The house settles around me.

    There is something watchful about the place at this hour.
    """

    return


label nurse_day1_evening_portrait_gallery:

    $ change_room('portrait_gallery')

    """
    The gallery is lit by a single gas lamp.

    The Claythorn ancestors gaze down from their frames with an air of collective disapproval.

    I feel rather as though I am being assessed.

    I do not linger.
    """

    return


# First Floor — Bedrooms
label nurse_day1_evening_bedroom_too_dangerous:

    """
    No answer.

    Far too dangerous to try anything now, with the house still so full of people.
    """

    return


label nurse_day1_evening_bedroom_drunk:

    call nurse_bedroom_default

    play sound door_open

    """
    My knocking nudges the door open a little.

    The smell that reaches me from inside is enough.

    Spirits, and something stale beneath it.

    I know better than to enter.
    """
    
    return


label nurse_day1_evening_bedroom_psychic:

    call nurse_bedroom_default

    psychic """
    Yes? Who is there, please?
    """

    nurse """
    Miss Marsh.
    """

    psychic """
    Oh, Miss Marsh. I am rather tired, I'm afraid.

    Could we speak tomorrow?
    """

    nurse """
    Of course. I shan't disturb you.

    Good night.
    """

    $ unlock_map('bedroom_psychic')

    return


label nurse_day1_evening_bedroom_captain:
    call nurse_bedroom_default
    call nurse_day1_evening_bedroom_too_dangerous
    return

label nurse_day1_evening_bedroom_host:
    call nurse_bedroom_default
    call nurse_day1_evening_bedroom_too_dangerous
    return

label nurse_day1_evening_bedroom_lad:
    call nurse_bedroom_default
    call nurse_day1_evening_bedroom_too_dangerous
    return

label nurse_day1_evening_bedroom_broken:
    call nurse_bedroom_default
    call nurse_day1_evening_bedroom_too_dangerous
    return

label nurse_day1_evening_bedroom_doctor:
    call nurse_bedroom_default
    call nurse_day1_evening_bedroom_too_dangerous
    return


# ATTIC
label nurse_day1_evening_storage:
    call nurse_attic_default
    call nurse_attic_too_dangerous
    return

label nurse_day1_evening_males_room:
    call nurse_attic_default
    call nurse_attic_too_dangerous
    return

label nurse_day1_evening_females_room:
    call nurse_attic_default
    call nurse_attic_too_dangerous
    return

label nurse_day1_evening_butler_room:
    call nurse_attic_default
    call nurse_attic_too_dangerous
    return


label nurse_attic_default:

    $ change_room("attic_hallway")

    """
    The attic staircase is narrow and the floorboards announce every step.

    I stop.

    A woman wandering uninvited through the servants' quarters would not go unremarked.
    """

    return


label nurse_attic_too_dangerous:

    play sound door_locked

    """
    The door is locked, in any case.

    I ought not to have come up here at all.

    This is not the right moment to venture here.
    """

    return