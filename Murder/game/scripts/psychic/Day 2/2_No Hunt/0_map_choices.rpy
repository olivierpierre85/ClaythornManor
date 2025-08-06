# Downstairs
label psychic_day2_no_hunt_downstairs_default:

    # Hide all downstairs choices for the current menu
    # $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('gun_room'))
    # $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('garage'))
    # $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('scullery'))
    # $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('kitchen'))

    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('gun_room'))
    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('garage'))
    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('scullery'))
    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))

    call psychic_downstairs_default

    return


# First Floor

# Bedroom
label psychic_day2_no_hunt_bedroom_try_enter(enter_result, enter_duration=5):

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
    
        enter_text = enter_text_list[psychic_details.saved_variables['day2_nohunt_bedroom_tries']]
        no_enter_text = no_enter_text_list[psychic_details.saved_variables['day2_nohunt_bedroom_tries']]
        
    if psychic_details.saved_variables['day2_nohunt_bedroom_tries'] == 0:

        """
        Most people are out for the hunt, so I suppose I could try to enter the room anyway.

        But it would not look good if I were caught.

        What should I do?
        """

        $ psychic_details.saved_variables['day2_nohunt_bedroom_tries'] += 1

    else:

        """
        There seems to be nobody here as well.
        """

        $ psychic_details.saved_variables['day2_nohunt_bedroom_tries'] += 1

    call run_menu(
        TimedMenu(
            id="psychic_day2_no_hunt_bedroom_try_enter" + enter_result, 
            choices=[
                TimedMenuChoice(enter_text, enter_result, enter_duration, early_exit=True),
                TimedMenuChoice(no_enter_text, 'psychic_day2_no_hunt_default_room_no_enter', enter_duration, early_exit=True),
            ]
        )
    )

    return

label psychic_day2_no_hunt_default_room_no_enter:
    
    """
    It is better not to enter this room for now.
    """

    return

label psychic_day2_no_hunt_default_room_locked:
    
    """
    I try to push the door open.

    The door is locked.
    """

    return


# Lad
label psychic_day2_no_hunt_bedroom_lad:

    call psychic_bedroom_default

    call psychic_day2_no_hunt_bedroom_try_enter('psychic_day2_no_hunt_default_room_locked')

    return


# Doctor
label psychic_day2_no_hunt_bedroom_doctor:

    call psychic_bedroom_default

    call psychic_day2_no_hunt_bedroom_try_enter('psychic_day2_no_hunt_default_room_locked')

    return


# Nurse
label psychic_day2_no_hunt_bedroom_nurse:

    call psychic_bedroom_default

    call psychic_day2_no_hunt_bedroom_try_enter('psychic_day2_no_hunt_default_room_locked')

    return


# Captain
label psychic_day2_no_hunt_bedroom_captain:

    call psychic_bedroom_default

    call psychic_day2_no_hunt_bedroom_try_enter('psychic_day2_no_hunt_default_room_locked')

    return

# Host
label psychic_day2_no_hunt_bedroom_host:

    call psychic_bedroom_default

    call psychic_day2_no_hunt_bedroom_try_enter('psychic_day2_no_hunt_default_room_locked')

    return

# Drunk
label psychic_day2_no_hunt_bedroom_drunk:

    call psychic_bedroom_default

    """
    The simple push I give to the door opens it.

    I catch a glimpse inside his room from here.

    It is quite untidy.
    """

    call psychic_day2_no_hunt_bedroom_try_enter('psychic_day2_no_hunt_bedroom_drunk_enter', enter_duration=20)

    return

# Attic
label psychic_day2_no_hunt_attic_default:
        
    # Hide all choices for the current menu
    # $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('storage'))
    # $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('males_room'))
    # $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('females_room'))
    # $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('butler_room'))

    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('butler_room'))

    call psychic_attic_default

    return