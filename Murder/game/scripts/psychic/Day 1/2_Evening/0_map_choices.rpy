# Map choices for PSYCHIC, Friday evening
# Downstairs
label psychic_day1_evening_downstairs_default:
    # Hide all downstairs choices for the current menu
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
    I reach the large hall and prepare to open the door.

    But the weather is dreadful, so it would be madness to go out now.

    It makes more sense to do something else for the time being.
    """

    return

# Closed bedrooms
label psychic_bedroom_stay_away:

    """
    I do not think it would be wise to simply enter someone's room like that.

    They might return at any moment.
    """
    
    return

label psychic_day1_evening_default_bedroom:
    call psychic_bedroom_default_no_answer
    call psychic_bedroom_stay_away
    return

# Attic
label psychic_day1_evening_attic_default:
        
    # Hide all upstairs choices for the current menu
    $ all_menus[psychic_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[psychic_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[psychic_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[psychic_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('butler_room'))

    call psychic_attic_default

    return


label psychic_day2_no_hunt_attic_return_too_soon:

    # Hide all upstairs choices for the current menu
    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[psychic_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('butler_room'))

    call psychic_attic_return_too_soon

    return