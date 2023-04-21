# Downstairs
label lad_day2_no_hunt_kitchen:
    call lad_day2_no_hunt_downstairs_default
    return

label lad_day2_no_hunt_scullery:
    call lad_day2_no_hunt_downstairs_default
    return

label lad_day2_no_hunt_garage:
    call lad_day2_no_hunt_downstairs_default
    return

label lad_day2_no_hunt_gun_room:
    call lad_day2_no_hunt_downstairs_default
    return

label lad_day2_no_hunt_downstairs_default:
    call lad_downstairs_default
    # Hide all downstairs choices for the current menu
    $ lad_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('gun_room'))
    $ lad_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('garage'))
    $ lad_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('scullery'))
    $ lad_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('kitchen'))
    return


# First Floor
label lad_day2_no_hunt_library:
    call lad_library_default
    return

label lad_day2_no_hunt_billiard_room:
    call lad_billiard_room_default
    return

label lad_day2_no_hunt_dining_room:
    call lad_dining_room_default
    return

label lad_day2_no_hunt_garden:
    call lad_garden_default
    return

label lad_day2_no_hunt_entrance_hall:
    call lad_entrance_hall_default
    return

label lad_day2_no_hunt_portrait_gallery:
    call lad_portrait_gallery_default
    return

# Bedroom
label lad_day2_no_hunt_bedroom_try_enter(enter_result, enter_duration=5):
        
    """
    Most people are out for the hunt, so I guess I could try to enter the room anyway.

    But it won't look good if I am caught.

    Why should I do?
    """

    call run_menu(
        TimedMenu([
            TimedMenuChoice('Let\'s go in, what\'s the worst that could happen?', enter_result, enter_duration, early_exit = True),
            TimedMenuChoice('I definitely shouldn\'t enter, that would be reckless!', 'lad_day2_no_hunt_default_room_no_enter', 5, early_exit = True),
        ])
    )

    return

label lad_day2_no_hunt_default_room_no_enter:
    
    """
    It's better not to enter this room for now.
    """

    return

label lad_day2_no_hunt_default_room_locked:
    
    """
    I try to push the door opened.

    It's locked.
    """

    return

# Psychic
label lad_day2_no_hunt_psychic_room:
    
    call lad_bedroom_default

    call lad_day2_no_hunt_bedroom_try_enter('lad_day2_no_hunt_psychic_room_enter')

    return

label lad_day2_no_hunt_psychic_room_enter:
    # May knows whose room it is so lock it to avoid weird dialog for now
    call lad_day2_no_hunt_default_room_locked

    return

# Doctor
label lad_day2_no_hunt_doctor_room:

    call lad_bedroom_default

    call lad_day2_no_hunt_bedroom_try_enter('lad_day2_no_hunt_doctor_room_enter')

    return

# Nurse
label lad_day2_no_hunt_doctor_room_enter:
    # May knows whose room it is so lock it to avoid weird dialog for now
    call lad_day2_no_hunt_default_room_locked

    return

label lad_day2_no_hunt_nurse_room:

    call lad_bedroom_default

    call lad_day2_no_hunt_bedroom_try_enter('lad_day2_no_hunt_nurse_room_enter')

    return

label lad_day2_no_hunt_nurse_room_enter:

    call lad_day2_no_hunt_default_room_locked

    return

# Captain
label lad_day2_no_hunt_captain_room:
    call lad_bedroom_default
    return

# Host
label lad_day2_no_hunt_host_room:
    call lad_bedroom_default
    return

# Drunk
label lad_day2_no_hunt_drunk_room:
    call lad_bedroom_default
    return


# Attic
label lad_day2_no_hunt_storage:
    call lad_storage_default
    return

label lad_day2_no_hunt_males_room:
    call lad_males_room_default
    return

label lad_day2_no_hunt_females_room:
    call lad_females_room_default
    return

label lad_day2_no_hunt_butler_room:
    call lad_butler_room_default
    return