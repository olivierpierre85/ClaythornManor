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
            TimedMenuChoice(default_room_text('gun_room'), 'nurse_day1_evening_gun_room', 20, room='gun_room'),
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

    Years of night shifts have taught me how to be unobtrusive in other people's houses.

    I reach the kitchen door and ease it open an inch.

    The room is full — staff moving back and forth, voices overlapping, the clatter of pots.

    No chance of doing anything useful in there tonight.

    The scullery will be just the same, connected as it is to the kitchen.

    I pull the door to and leave without anyone having noticed me.
    """

    return


label nurse_day1_evening_garage:

    $ all_menus[nurse_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('garage'))

    $ change_room("basement_stairs")

    """
    I take the back passage, keeping close to the wall.
    """

    $ change_room("garage")

    """
    It is a cold, oil-smelling place.

    A motor car sits under a dust sheet.

    Tools hang neatly along one wall, and a bicycle leans against another.

    Nothing here that is of any use to me.
    """

    return


label nurse_day1_evening_gun_room:

    $ all_menus[nurse_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('gun_room'))

    $ change_room("basement_stairs")

    """
    I take the servants' corridor without stopping.
    """

    $ change_room("gun_room")

    """
    Glass cases line three walls, each holding shotguns and hunting rifles in neat rows.

    The smell of gun oil is sharp.

    A row of keys hangs on a hook beside the door — presumably for the cabinets.

    I try one.

    It turns.
    """

    call run_menu(TimedMenu("nurse_day1_evening_gun_room_choice", [
        TimedMenuChoice("Take a pistol", 'nurse_day1_evening_take_gun', 10, early_exit=True),
        TimedMenuChoice("Leave it. Too dangerous to carry.", 'generic_cancel', early_exit=True),
    ]))

    return


label nurse_day1_evening_take_gun:

    """
    My hand closes around the grip of a small revolver.

    It is loaded.

    I slip it into my bag and close the cabinet again, hanging the key back on its hook.

    Nobody will notice — not tonight, at any rate.
    """

    $ nurse_details.threads.unlock('has_gun')

    return


# First Floor
label nurse_day1_evening_library:

    $ change_room('library')

    """
    A well-appointed library.

    I cast my eye along the shelves.

    Mostly heraldry, county histories, and bound journals.

    Nothing worth taking — far too heavy, and of no particular value.

    I am about to leave when a title catches my attention.

    "The Anglo-Zanzibar War — A Brief Account."

    The Captain mentioned Zanzibar this afternoon.

    Something in the way he spoke of it nagged at me, though I could not place it at the time.
    """

    call run_menu(TimedMenu("nurse_library_default", [
        TimedMenuChoice("Read the account. It may be useful.", 'nurse_day1_evening_library_zanzibar', 30, early_exit=True),
        TimedMenuChoice("Leave it. I am too tired for reading tonight.", 'generic_cancel', early_exit=True),
    ]))

    return


label nurse_day1_evening_library_zanzibar:

    call wait_screen_transition()

    """
    I sit down and read.

    The war lasted thirty-eight minutes.

    The shortest war in recorded history.

    The British bombardment was swift and overwhelming.

    There were British casualties.

    Very few, but there were some.

    Why would the Captain speak of it as though he had seen hard fighting?

    Unless he wished to appear more battle-hardened than he truly was.

    Or perhaps, he was there for a different reason entirely.
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
label nurse_day1_evening_bedroom_drunk:

    call nurse_bedroom_default

    play sound door_open

    """
    My knocking nudges the door open a little.

    The smell that reaches me from inside is enough.

    Spirits, and something stale beneath it.

    I have attended enough patients in this condition to know better than to enter.
    """

    call run_menu(TimedMenu("nurse_day1_evening_bedroom_drunk", [
        TimedMenuChoice("Go in. He may need medical attention.", 'nurse_day1_evening_bedroom_drunk_enter', 0, next_menu="nurse_day1_evening_bedroom_drunk", early_exit=True),
        TimedMenuChoice("Close the door and leave.", 'nurse_day1_evening_bedroom_drunk_leave', early_exit=True),
    ]))

    return


label nurse_day1_evening_bedroom_drunk_enter:

    """
    I push the door open.

    Mr Manning is sprawled across the armchair, still dressed.

    He is breathing — noisily, and with great conviction.

    He is not in any danger.

    I tuck a blanket around him out of habit, collect his glass from the floor before it is knocked over, and leave quietly.
    """

    $ nurse_details.threads.unlock('checked_drunk')

    return


label nurse_day1_evening_bedroom_drunk_leave:

    """
    I pull the door to and let him be.

    It is not my responsibility.
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


label nurse_bedroom_stay_away:

    """
    I raise my hand to knock, then think better of it.

    These are private rooms.

    I have no business here.
    """

    return


label nurse_day1_evening_bedroom_captain:
    call nurse_bedroom_default
    call nurse_bedroom_stay_away
    return

label nurse_day1_evening_bedroom_host:
    call nurse_bedroom_default
    call nurse_bedroom_stay_away
    return

label nurse_day1_evening_bedroom_lad:
    call nurse_bedroom_default
    call nurse_bedroom_stay_away
    return

label nurse_day1_evening_bedroom_broken:
    call nurse_bedroom_default
    call nurse_bedroom_stay_away
    return

label nurse_day1_evening_bedroom_doctor:
    call nurse_bedroom_default
    call nurse_bedroom_stay_away
    return


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


# Attic
label nurse_day1_evening_storage:
    call nurse_attic_default
    call nurse_attic_closed
    return

label nurse_day1_evening_males_room:
    call nurse_attic_default
    call nurse_attic_closed
    return

label nurse_day1_evening_females_room:
    call nurse_attic_default
    call nurse_attic_closed
    return

label nurse_day1_evening_butler_room:
    call nurse_attic_default
    call nurse_attic_closed
    return


label nurse_attic_default:

    $ change_room("attic_hallway")

    """
    The attic staircase is narrow and the floorboards announce every step.

    I stop.

    A woman wandering uninvited through the servants' quarters would not go unremarked.
    """

    return


label nurse_attic_closed:

    play sound door_locked

    """
    The door is locked, in any case.

    I ought not to have come up here at all.
    """

    return


# Billiard room
label nurse_day1_evening_billiard_room:

    $ change_room('billiard_room')

    """
    A haze of pipe smoke hangs over the room.

    Captain Sinha is holding court near the fireplace.

    A small audience has gathered — the Captain's voice carries, and his stories have the weight of a man who expects to be listened to.

    I find a chair near the window, a little apart from the group.

    I am content to observe.

    Ted Harring is there too, hovering at the edge of the circle.

    He catches my eye and nods.

    I nod back, and look away.

    I don't stay long.
    """

    return