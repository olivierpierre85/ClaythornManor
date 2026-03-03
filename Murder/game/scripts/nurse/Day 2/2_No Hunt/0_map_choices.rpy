label nurse_day2_no_hunt_map_menu:
    python:
        # -------------------------
        # Saturday, During the Hunt
        # -------------------------        
        nurse_day2_no_hunt_map_menu = TimedMenu("nurse_day2_no_hunt_map_menu", [
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'nurse_day2_no_hunt_downstairs_maid', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'nurse_day2_no_hunt_downstairs_maid', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'nurse_garage_default', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'nurse_gun_room_default', 10, room='gun_room'),
            # first floor
            TimedMenuChoice(default_room_text('billiard_room'), 'nurse_billiard_room_default', 10, room='billiard_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'nurse_dining_room_default', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'nurse_day2_no_hunt_garden', 30, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'nurse_entrance_hall_default', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('library'), 'nurse_library_default', 0, room='library'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'nurse_portrait_gallery_default', 10, room='portrait_gallery'),
            # Bedrooms 
            TimedMenuChoice(default_room_text('bedroom_lad'), 'nurse_day2_no_hunt_bedroom_lad', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'nurse_day2_no_hunt_bedroom_doctor', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'nurse_day2_no_hunt_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'nurse_day2_no_hunt_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'nurse_day2_no_hunt_bedroom_drunk', 10, room='bedroom_drunk'),
            # attic
            TimedMenuChoice(default_room_text('storage'), 'nurse_day2_no_hunt_attic_default', 60, room='storage', condition=attic_default),
            TimedMenuChoice(default_room_text('males_room'), 'nurse_day2_no_hunt_attic_default', 60, room='males_room', condition=attic_default),
            TimedMenuChoice(default_room_text('females_room'), 'nurse_day2_no_hunt_attic_default', 60, room='females_room', condition=attic_default),
            TimedMenuChoice(default_room_text('butler_room'), 'nurse_day2_no_hunt_attic_default', 60, room='butler_room', condition=attic_default),
            
            TimedMenuChoice(default_room_text('storage'), 'nurse_day2_no_hunt_attic_return_too_soon', 10, room='storage', condition=attic_return_too_soon),
            TimedMenuChoice(default_room_text('males_room'), 'nurse_day2_no_hunt_attic_return_too_soon', 10, room='males_room', condition=attic_return_too_soon),
            TimedMenuChoice(default_room_text('females_room'), 'nurse_day2_no_hunt_attic_return_too_soon', 10, room='females_room', condition=attic_return_too_soon),
            TimedMenuChoice(default_room_text('butler_room'), 'nurse_day2_no_hunt_attic_return_too_soon', 10, room='butler_room', condition=attic_return_too_soon),
            
            TimedMenuChoice(default_room_text('bedroom_psychic'), 
                'nurse_day2_no_hunt_bedroom_psychic_busy', 
                10, 
                room='bedroom_psychic',
                condition = condition_saturday_hunt_morning,
            ),
            TimedMenuChoice(
                'Take a rest', 
                'nurse_day2_no_hunt_cancel', 
                60, 
                early_exit = True, 
                room = 'bedroom_nurse',
                condition = condition_saturday_hunt_morning
            ),
            TimedMenuChoice(
                'Wait until the others return', 
                'nurse_day2_no_hunt_cancel', 
                90, 
                early_exit = True, 
                room = 'bedroom_nurse',
                condition = "not " + condition_saturday_hunt_morning
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'nurse_day2_bedroom_broken', 
                20, 
                room = 'bedroom_broken',
            )
        ], 
        is_map = True)
    
    return

# Downstairs
label nurse_day2_no_hunt_downstairs_maid:

    # Hide both kitchen and scullery — they share the same discovery
    $ all_menus[nurse_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))
    $ all_menus[nurse_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('scullery'))

    $ change_room("basement_stairs")

    call nurse_downstairs_approach

    $ change_room("kitchen")

    """
    I almost step inside until I notice one of the maids, alone.
    
    She is busy, likely preparing our luncheon.

    It is better if she does not see me.

    I pull the door to and leave.
    """

    return


# First Floor

label nurse_day2_no_hunt_garden:

    $ change_room('manor_garden')

    """
    The morning air is quite still, and there is a pale brightness to the sky that has been absent since our arrival.

    Not warm, precisely, but a good deal better than yesterday.

    A short walk in the garden can only do one good.

    The paths are a little damp underfoot, but the ground is firm enough.

    I follow the gravel along the low hedgerow, taking my time.

    The house stands behind me, quiet and closed.

    There is something restoring about being outside, away from the corridors and other people's doors.

    I could walk further, but I know better than to encourage that impulse.

    One must not confuse feeling a little better with being well.

    I do a single turn of the garden and return to the entrance.
    """

    return


# Bedroom
label nurse_day2_no_hunt_bedroom_try_enter(menu_id, enter_result, enter_duration=5):

    python:
        enter_text_list = [
            "Perhaps I should take a quick look inside.",
            "There is no harm in a brief inspection.",
            "I will just see if anything is out of place."
        ]

        no_enter_text_list = [
            "No, I should not pry.",
            "It is none of my business to be entering other people's rooms.",
            "I had better leave it be."
        ]
    
        # Ensure we don't go out of bounds if the player tries many times
        try_index = min(nurse_details.saved_variables.setdefault('day2_nohunt_bedroom_tries', 0), len(enter_text_list) - 1)
        enter_text = enter_text_list[try_index]
        no_enter_text = no_enter_text_list[try_index]
        
    if nurse_details.saved_variables.get('day2_nohunt_bedroom_tries', 0) == 0:

        """
        With most of the household out shooting, one could easily slip inside unseen.

        Though it would be rather difficult to explain if I were caught.
        """

    else:

        """
        This corridor remains quite deserted as well.
        """

    $ nurse_details.saved_variables['day2_nohunt_bedroom_tries'] = nurse_details.saved_variables.get('day2_nohunt_bedroom_tries', 0) + 1

    call run_menu(
        TimedMenu(
            id=menu_id, 
            choices=[
                TimedMenuChoice(enter_text, enter_result, enter_duration, early_exit=True),
                TimedMenuChoice(no_enter_text, 'nurse_day2_no_hunt_default_room_no_enter', enter_duration, early_exit=True),
            ]
        )
    )

    return

label nurse_day2_no_hunt_default_room_no_enter:
    
    """
    It is best I do not go in there for now.
    """

    return


label nurse_day2_no_hunt_default_room_locked:
    
    """
    I try the handle gently.

    It is securely locked.
    """

    return


# Lad
label nurse_day2_no_hunt_bedroom_lad:

    call nurse_bedroom_default_no_answer

    call nurse_day2_no_hunt_bedroom_try_enter('nurse_day2_no_hunt_bedroom_lad', 'nurse_day2_no_hunt_default_room_locked')

    return


# Doctor
label nurse_day2_no_hunt_bedroom_doctor:

    call nurse_bedroom_default_no_answer

    call nurse_day2_no_hunt_bedroom_try_enter('nurse_day2_no_hunt_bedroom_doctor', 'nurse_day2_no_hunt_default_room_locked')

    return


# Captain
label nurse_day2_no_hunt_bedroom_captain:

    call nurse_bedroom_default_no_answer

    call nurse_day2_no_hunt_bedroom_try_enter('nurse_day2_no_hunt_bedroom_captain', 'nurse_day2_no_hunt_default_room_locked')

    return


# Host
label nurse_day2_no_hunt_bedroom_host:

    call nurse_bedroom_default_no_answer

    call nurse_day2_no_hunt_bedroom_try_enter('nurse_day2_no_hunt_bedroom_host', 'nurse_day2_no_hunt_default_room_locked')

    return


# Drunk
label nurse_day2_no_hunt_bedroom_drunk:

    call nurse_bedroom_default_no_answer

    """
    The door shifts slightly under my touch.

    It appears Mr Manning has left it resting on the latch.
    """

    call nurse_day2_no_hunt_bedroom_try_enter('nurse_day2_no_hunt_bedroom_drunk', 'nurse_day2_no_hunt_bedroom_drunk_enter', enter_duration=20)

    return

label nurse_day2_no_hunt_bedroom_drunk_enter:

    """
    I push the door open quietly, ensuring no one is watching.
    """

    play sound door_open

    $ change_room('bedroom_drunk')

    """
    The room is in a frightful state.

    Clothes are discarded carelessly, and the unmistakable smell of spirits hangs in the air.
    """

    $ unlock_map('bedroom_drunk')

    """
    A brief glance reveals only empty whisky bottles.

    Quite as I suspected. There is nothing of interest for me here.
    """

    return

# Attic
label nurse_day2_no_hunt_attic_default:
        
    $ all_menus[nurse_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[nurse_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[nurse_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[nurse_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('butler_room'))

    call nurse_attic_default

    return


label nurse_day2_no_hunt_attic_return_too_soon:

    $ all_menus[nurse_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[nurse_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[nurse_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[nurse_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('butler_room'))

    call nurse_attic_return_too_soon

    return
