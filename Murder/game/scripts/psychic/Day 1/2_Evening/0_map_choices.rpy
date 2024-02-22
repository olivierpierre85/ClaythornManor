# Map choices for PSYCHIC, Friday evening
# Downstairs
label psychic_day1_evening_kitchen:
    call psychic_day1_evening_downstairs_default
    return

label psychic_day1_evening_scullery:
    call psychic_day1_evening_downstairs_default
    return

label psychic_day1_evening_garage:
    call psychic_day1_evening_downstairs_default
    return

label psychic_day1_evening_gun_room:
    call psychic_day1_evening_downstairs_default
    return

label psychic_day1_evening_downstairs_default:
        
    call psychic_downstairs_default
    # Hide all downstairs choices for the current menu
    $ psychic_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('gun_room'))
    $ psychic_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('garage'))
    $ psychic_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('scullery'))
    $ psychic_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('kitchen'))
    return


# First Floor
label psychic_day1_evening_library:
    call psychic_library_default
    return

label psychic_day1_evening_tea_room:
    call psychic_tea_room_default
    return

label psychic_day1_evening_dining_room:
    call psychic_dining_room_default
    return

label psychic_day1_evening_garden:

    $ change_room('great_hall')
    
    """
    I get to the large hall and get ready to open the door.

    But the weather's awful, so it'd be crazy to go out now.

    It makes more sense to do something else right now.
    """

    return

label psychic_day1_evening_entrance_hall:
    call psychic_entrance_hall_default
    return

label psychic_day1_evening_portrait_gallery:
    call psychic_portrait_gallery_default
    return

# Closed bedrooms
label psychic_bedroom_stay_away:

    """
    I don't think it would be wise to just enter someone's room like that.

    They might come back at any moment.
    """
    
    return

label psychic_day1_evening_lad_room:
    call psychic_bedroom_default
    call psychic_bedroom_stay_away
    return

label psychic_day1_evening_doctor_room:
    call psychic_bedroom_default
    call psychic_bedroom_stay_away
    return

label psychic_day1_evening_captain_room:
    call psychic_bedroom_default
    call psychic_bedroom_stay_away
    return

label psychic_day1_evening_host_room:
    call psychic_bedroom_default
    call psychic_bedroom_stay_away
    return

label psychic_day1_evening_drunk_room:
    call psychic_bedroom_default
    call psychic_bedroom_stay_away
    return

label psychic_day1_evening_broken_room:
    call psychic_bedroom_default
    call psychic_bedroom_stay_away
    return

label psychic_day1_evening_nurse_room:
    call psychic_bedroom_default
    call psychic_bedroom_stay_away
    return

# Attic
label psychic_day2_no_hunt_storage:
    call psychic_day2_no_hunt_attic_default
    return

label psychic_day2_no_hunt_males_room:
    call psychic_day2_no_hunt_attic_default
    return

label psychic_day2_no_hunt_females_room:
    call psychic_day2_no_hunt_attic_default
    return

label psychic_day2_no_hunt_butler_room:
    call psychic_day2_no_hunt_attic_default
    return

label psychic_day2_no_hunt_attic_default:
        
    call psychic_attic_default
    # Hide all downstairs choices for the current menu
    $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('storage'))
    $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('males_room'))
    $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('females_room'))
    $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('butler_room'))
    return