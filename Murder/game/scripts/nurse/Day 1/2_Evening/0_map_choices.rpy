# Map choices for Nurse, Friday evening
label nurse_day1_evening_map_menu:
    python:        
        # Map choices
        nurse_day1_evening_map_menu = TimedMenu(
            "nurse_day1_evening_map_menu", 
            [
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'nurse_day1_evening_downstairs_crowded', 20, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'nurse_day1_evening_downstairs_crowded', 20, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'nurse_day1_evening_garage', 20, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'nurse_day1_evening_gun_room', 0, room='gun_room'),
            # First floor
            TimedMenuChoice(default_room_text('tea_room'), 'nurse_day1_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'nurse_day1_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'nurse_day1_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'nurse_day1_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'nurse_day1_evening_portrait_gallery', 10, room='portrait_gallery'),
            #bedroom
            TimedMenuChoice(default_room_text('bedroom_lad'), 'nurse_day1_evening_bedroom_lad', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'nurse_day1_evening_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'nurse_day1_evening_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_broken'), 'nurse_day1_evening_bedroom_broken', 10, room='bedroom_broken'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'nurse_day1_evening_bedroom_doctor', 10, room='bedroom_doctor'),

            # attic
            TimedMenuChoice(default_room_text('storage'), 'nurse_day1_evening_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'nurse_day1_evening_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'nurse_day1_evening_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'nurse_day1_evening_butler_room', 10, room='butler_room'),
            # Specific actions
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'nurse_day1_evening_bedroom_drunk', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('library'), 'nurse_day1_evening_library', 0, room='library'),
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

    call nurse_downstairs_approach

    $ change_room("kitchen")

    """
    I almost go in until I notice some of the staff. 
    
    They are busy cleaning today's meal.

    No chance of doing anything useful in there tonight.

    The scullery will be just the same, connected as it is to the kitchen.

    I pull the door to and leave without anyone having noticed me.
    """

    call nurse_day1_evening_check_exhaustion

    return


# First Floor
label nurse_day1_evening_dining_room:

    $ change_room('dining_room')

    """
    The dining room is deserted.

    The staff are clearing away the last of the dishes.

    I receive a faintly puzzled look from the footman.

    I offer no explanation and withdraw.
    """

    call nurse_day1_evening_check_exhaustion

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

    call nurse_day1_evening_check_exhaustion

    return




# First Floor — Bedrooms
label nurse_day1_evening_bedroom_too_dangerous:

    """
    No answer.
    """

    if not nurse_details.saved_variables["bedroom_too_dangerous_seen"]:

        $ nurse_details.saved_variables["bedroom_too_dangerous_seen"] = True

        """
        I could try my skills to enter anyway.

        But that seems far too dangerous to try anything, with the house still so full of people.
        """
        
    """    
    There must be better places to explore for now.
    """

    call nurse_day1_evening_check_exhaustion

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

    call nurse_day1_evening_check_exhaustion

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

    call nurse_day1_evening_check_exhaustion

    return


label nurse_day1_evening_bedroom_captain:
    call nurse_bedroom_default
    call nurse_day1_evening_bedroom_too_dangerous
    call nurse_day1_evening_check_exhaustion
    return

label nurse_day1_evening_bedroom_host:
    call nurse_bedroom_default
    call nurse_day1_evening_bedroom_too_dangerous
    call nurse_day1_evening_check_exhaustion
    return

label nurse_day1_evening_bedroom_lad:
    call nurse_bedroom_default
    call nurse_day1_evening_bedroom_too_dangerous
    call nurse_day1_evening_check_exhaustion
    return

label nurse_day1_evening_bedroom_broken:
    call nurse_bedroom_default
    call nurse_day1_evening_bedroom_too_dangerous
    call nurse_day1_evening_check_exhaustion
    return

label nurse_day1_evening_bedroom_doctor:
    call nurse_bedroom_default
    call nurse_day1_evening_bedroom_too_dangerous
    call nurse_day1_evening_check_exhaustion
    return


# ATTIC
label nurse_day1_evening_storage:
    call nurse_attic_default
    call nurse_attic_too_dangerous
    call nurse_day1_evening_check_exhaustion
    return

label nurse_day1_evening_males_room:
    call nurse_attic_default
    call nurse_attic_too_dangerous
    call nurse_day1_evening_check_exhaustion
    return

label nurse_day1_evening_females_room:
    call nurse_attic_default
    call nurse_attic_too_dangerous
    call nurse_day1_evening_check_exhaustion
    return

label nurse_day1_evening_butler_room:
    call nurse_attic_default
    call nurse_attic_too_dangerous
    call nurse_day1_evening_check_exhaustion
    return


label nurse_day1_evening_garage:

    call nurse_garage_default

    call nurse_day1_evening_check_exhaustion

    return


label nurse_day1_evening_gun_room:

    call nurse_gun_room_default

    call nurse_day1_evening_check_exhaustion

    return


label nurse_day1_evening_tea_room:

    call nurse_tea_room_default

    call nurse_day1_evening_check_exhaustion

    return


label nurse_day1_evening_entrance_hall:

    call nurse_entrance_hall_default

    call nurse_day1_evening_check_exhaustion

    return


label nurse_day1_evening_portrait_gallery:

    call nurse_portrait_gallery_default

    call nurse_day1_evening_check_exhaustion

    return


label nurse_day1_evening_library:

    call nurse_library_default

    call nurse_day1_evening_check_exhaustion

    return


label nurse_attic_default:

    $ change_room("attic_hallway")

    $ all_menus[nurse_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[nurse_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[nurse_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[nurse_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('butler_room'))

    """
    The attic staircase is narrow and the floorboards announce every step.

    I stop.

    A woman wandering uninvited through the servants' quarters would not go unremarked.
    """

    return


label nurse_attic_too_dangerous:

    """
    I ought not to have come up here at all.

    This is not the right moment to venture around here.
    """

    return


label nurse_day1_evening_check_exhaustion:

    if (time_left < 30) and not nurse_details.saved_variables["day1_evening_exhaustion_triggered"]:

        $ nurse_details.saved_variables["day1_evening_exhaustion_triggered"] = True

        """
        A wave of tiredness washes over me quite suddenly.

        The journey here took more out of me than I thought.

        If I push myself much further tonight, I shall pay for it.
        """

    return