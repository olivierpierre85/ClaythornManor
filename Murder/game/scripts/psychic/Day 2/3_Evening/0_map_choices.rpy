# Downstairs
label psychic_day2_evening_downstairs_default:

    # Hide all downstairs choices for the current menu
    # $ psychic_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('gun_room'))
    # $ psychic_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('garage'))
    # $ psychic_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('scullery'))
    # $ psychic_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('kitchen'))

    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('gun_room'))
    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('garage'))
    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('scullery'))
    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))

    call psychic_downstairs_default

    return


label psychic_day2_evening_garden:

    # TODO replace by garden at night and dark contemplation ?

    $ change_room('great_hall')
    
    """
    I reach the large hall and prepare to open the door.

    The weather has improved, but it is pitch dark outside.
    
    What possessed me? There is no reason to go out now.
    """

    return

# First Floor

# Bedroom
label psychic_day2_evening_bedroom_try_enter(enter_result, enter_duration=10):

    python:
        enter_text_list = [
            "Let's go in. What's the worst that could happen?",
            "It won't hurt to give it a try. Let's go in and find out.",
            "Let's enter and see what happens. It can't be that bad.",
            "What's the harm in entering? Let's go!",
            "Come on, let's go inside. What could go wrong?",
            "Shall we enter? It's not like you'd be in any danger anyway."
        ]

        no_enter_text_list = [
            "I definitely shouldn't enter. That would be reckless!",
            "I shouldn't go in. That's too dangerous!",
            "I'd better not enter. It could be risky.",
            "That's a bad idea. I shouldn't go inside.",
            "I don't want to take unnecessary risks. I shouldn't go in.",
            "It's not worth the danger. I'm not going in."
        ]
    
        enter_text = enter_text_list[psychic_details.saved_variables['day2_evening_bedroom_tries']]
        no_enter_text = no_enter_text_list[psychic_details.saved_variables['day2_evening_bedroom_tries']]
        
    if psychic_details.saved_variables['day2_evening_bedroom_tries'] == 0:

        """
        Should I try to enter anyway?
        """

        $ psychic_details.saved_variables['day2_evening_bedroom_tries'] += 1

    else:

        """
        There seems to be nobody here as well.
        """

        $ psychic_details.saved_variables['day2_evening_bedroom_tries'] += 1

    call run_menu(
        TimedMenu(
            id="psychic_day2_evening_bedroom_try_enter" + enter_result, 
            choices=[
                TimedMenuChoice(enter_text, enter_result, enter_duration, early_exit=True),
                TimedMenuChoice(no_enter_text, 'psychic_day2_evening_default_room_no_enter', enter_duration, early_exit=True),
            ]
        )
    )

    return

label psychic_day2_evening_default_room_no_enter:
    
    """
    It's better not to enter this room for now.
    """

    return

label psychic_day2_evening_default_room_locked:
    
    """
    I try to push the door open.

    It's locked.
    """

    return


# Lad - ???
label psychic_day2_evening_bedroom_lad:

    call psychic_bedroom_default

    call psychic_day2_evening_bedroom_try_enter('psychic_day2_evening_default_room_locked')

    return


# Doctor - Dead
label psychic_day2_evening_bedroom_doctor:

    """
    The door stands slightly ajar.

    I notice faint traces of blood on the floor.

    Cautiously, I step inside and see Doctor Baldwin's body.
    """

    $ change_room('bedroom_doctor')

    """
    He is lying peacefully in his bed.

    Unsure what I could do here, I decide to leave.
    """

    $ unlock_map('bedroom_doctor')
    # TODO: Add possibility to snoop?

    return




# Captain - In the billiard room
label psychic_day2_evening_bedroom_captain:

    call psychic_bedroom_default

    call psychic_day2_evening_bedroom_try_enter('psychic_day2_evening_default_room_locked')

    return

# Host - Preparing to leave
label psychic_day2_evening_bedroom_host:

    call psychic_bedroom_default

    call psychic_day2_evening_bedroom_try_enter('psychic_day2_evening_default_room_locked')

    return

# Broken (if already seen in the afternoon)
label psychic_day2_bedroom_broken_already_see:

    $ change_room("bedrooms_hallway")

    """
    I stand once again in front of Thomas Moody's room.

    I do not know what compelled me to come here again.

    I try to open the door, but I can't. The memory of his dead body is still too fresh in my mind.

    I'd better go somewhere else.
    """

    return


# Drunk
label psychic_day2_evening_bedroom_drunk:

    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on the door.
    """

    drunk """
    Grrr, Mrrrr, Errrr
    """

    """
    I recognise Samuel Manning's voice, and it's clear he is too drunk to be coherent. 
    
    Since the door is locked, I decide not to interfere.
    """

    $ unlock_map('bedroom_drunk')

    return

# Attic
label psychic_day2_evening_attic_default:

    # Hide all downstairs choices for the current menu
    # $ psychic_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('storage'))
    # $ psychic_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('males_room'))
    # $ psychic_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('females_room'))
    # $ psychic_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('butler_room'))
        
    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('butler_room'))

    call psychic_attic_default

    return


label psychic_day2_evening_attic_return_too_soon:

    # Hide all upstairs choices for the current menu
    # $ psychic_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('storage'))
    # $ psychic_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('males_room'))
    # $ psychic_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('females_room'))
    # $ psychic_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('butler_room'))

    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('butler_room'))

    call psychic_attic_return_too_soon


    return