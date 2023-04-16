# Downstairs
label lad_day2_no_hunt_evening_kitchen:
    call lad_day2_no_hunt_downstairs_default
    return

label lad_day2_no_hunt_evening_scullery:
    call lad_day2_no_hunt_downstairs_default
    return

label lad_day2_no_hunt_evening_garage:
    call lad_day2_no_hunt_downstairs_default
    return

label lad_day2_no_hunt_evening_gun_room:
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
label lad_day2_no_hunt_evening_library:
    call lad_library_default
    return

label lad_day2_no_hunt_evening_billiard_room:
    call lad_billiard_room_default
    return

label lad_day2_no_hunt_evening_dining_room:
    call lad_dining_room_default
    return


label lad_day2_no_hunt_evening_garden:
    call lad_garden_default
    return

label lad_day2_no_hunt_evening_entrance_hall:
    call lad_entrance_hall_default
    return

label lad_day2_no_hunt_evening_portrait_gallery:
    call lad_portrait_gallery_default
    return

# Bedroom
label lad_day2_no_hunt_evening_lad_room:
    """
    TODO
    """
    return

label lad_day2_no_hunt_evening_doctor_room:
    """
    TODO
    """
    return

label lad_day2_no_hunt_evening_captain_room:
    """
    TODO
    """
    return

label lad_day2_no_hunt_evening_psychic_room:
    """
    TODO
    """
    return

label lad_day2_no_hunt_evening_host_room:
    """
    TODO
    """
    return

label lad_day2_no_hunt_evening_drunk_room:
    """
    TODO
    """
    return

label lad_day2_no_hunt_evening_broken_room:
    """
    TODO
    """
    return

label lad_day2_no_hunt_evening_nurse_room:
    """
    TODO
    """
    return

# Attic
label lad_day2_no_hunt_evening_storage:
    """
    TODO
    """
    return

label lad_day2_no_hunt_evening_males_room:
    """
    TODO
    """
    return

label lad_day2_no_hunt_evening_females_room:
    """
    TODO
    """
    return

label lad_day2_no_hunt_evening_butler_room:
    """
    TODO
    """
    return