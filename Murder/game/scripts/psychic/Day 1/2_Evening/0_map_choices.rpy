# Map choices for PSYCHIC, Friday evening
# Downstairs
label psychic_day1_evening_downstairs_default:

    # Hide all downstairs choices for the current menu
    # $ psychic_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('gun_room'))
    # $ psychic_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('garage'))
    # $ psychic_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('scullery'))
    # $ psychic_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('kitchen'))

    $ all_menus[psychic_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('gun_room'))
    $ all_menus[psychic_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('garage'))
    $ all_menus[psychic_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('scullery'))
    $ all_menus[psychic_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))


    call psychic_downstairs_default

    return


# First Floor

label psychic_day1_evening_garden:

    $ change_room('great_hall')
    
    """
    I get to the large hall and get ready to open the door.

    But the weather's awful, so it'd be crazy to go out now.

    It makes more sense to do something else right now.
    """

    return

# Closed bedrooms
label psychic_bedroom_stay_away:

    """
    I don't think it would be wise to just enter someone's room like that.

    They might come back at any moment.
    """
    
    return

label psychic_day1_evening_default_bedroom:
    call psychic_bedroom_default
    call psychic_bedroom_stay_away
    return

# Attic
label psychic_day1_evening_attic_default:
        
    # Hide all upstairs choices for the current menu
    # $ psychic_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('storage'))
    # $ psychic_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('males_room'))
    # $ psychic_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('females_room'))
    # $ psychic_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('butler_room'))

    $ all_menus[psychic_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[psychic_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[psychic_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[psychic_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('butler_room'))

    call psychic_attic_default

    return


label psychic_day2_no_hunt_attic_return_too_soon:

    # Hide all upstairs choices for the current menu
    # $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('storage'))
    # $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('males_room'))
    # $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('females_room'))
    # $ psychic_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('butler_room'))

    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('butler_room'))

    call psychic_attic_return_too_soon

    return