# Map choices for LAD, Friday evening
label lad_day1_evening_map_menu:
    python:    
        lad_day1_evening_map_menu = TimedMenu(
            "lad_day1_evening_map_menu", 
            [
            # Default values
            TimedMenuChoice(default_room_text('storage'), 'lad_day1_evening_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'lad_day1_evening_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'lad_day1_evening_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'lad_day1_evening_butler_room', 10, room='butler_room'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'lad_day1_evening_bedroom_doctor', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'lad_day1_evening_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'lad_day1_evening_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'lad_day1_evening_bedroom_drunk', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_broken'), 'lad_day1_evening_bedroom_broken', 10, room='bedroom_broken'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'lad_day1_evening_bedroom_nurse', 10, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('library'), 'lad_day1_evening_library', 10, room='library'),
            TimedMenuChoice(default_room_text('tea_room'), 'lad_day1_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'lad_day1_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'lad_day1_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'lad_day1_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'lad_day1_evening_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('kitchen'), 'lad_day1_evening_kitchen', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'lad_day1_evening_scullery', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'lad_day1_evening_garage', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'lad_day1_evening_gun_room', 10, room='gun_room'),
            # Specific actions
            TimedMenuChoice(
                default_room_text('bedroom_psychic'), 
                'lad_day1_evening_bedroom_psychic', 
                10, 
                room = 'bedroom_psychic'
            ),
            TimedMenuChoice(
                'Meet the others in the billiard room', 
                'lad_day1_evening_billiard_room', 
                0, 
                keep_alive = True, 
                room = 'billiard_room',
                next_menu = 'lad_day1_evening_billiard_room_menu'
            ),
            TimedMenuChoice(
                'Go to sleep', 
                'generic_cancel', 
                early_exit = True, 
                room = 'bedroom_lad'
            )
        ], is_map = True)
    return

# Downstairs
label lad_day1_evening_kitchen:
    call lad_day1_evening_downstairs_default
    return

label lad_day1_evening_scullery:
    call lad_day1_evening_downstairs_default
    return

label lad_day1_evening_garage:
    call lad_day1_evening_downstairs_default
    return

label lad_day1_evening_gun_room:
    call lad_day1_evening_downstairs_default
    return

label lad_day1_evening_downstairs_default:

    # Hide all downstairs choices for the current menu
    # $ lad_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('gun_room'))
    # $ lad_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('garage'))
    # $ lad_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('scullery'))
    # $ lad_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('kitchen'))

    $ all_menus[lad_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('gun_room'))
    $ all_menus[lad_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('garage'))
    $ all_menus[lad_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('scullery'))
    $ all_menus[lad_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))
        
    call lad_downstairs_default

    return


# First Floor
label lad_day1_evening_library:
    call lad_library_default
    return

label lad_day1_evening_tea_room:
    call lad_tea_room_default
    return

label lad_day1_evening_dining_room:
    call lad_dining_room_default
    return

label lad_day1_evening_garden:

    $ change_room('great_hall')
    
    """
    I reach the great hall and prepare to open the door. 

    However, the weather is so bad that only a madman would venture out now. 

    I'd be better off doing something else at the moment.
    """

    return

label lad_day1_evening_entrance_hall:
    call lad_entrance_hall_default
    return

label lad_day1_evening_portrait_gallery:
    call lad_portrait_gallery_default
    return

# Closed bedrooms
label lad_bedroom_stay_away:

    """
    Should I try to enter anyway?

    No, that's probably a bad idea.
    """
    
    return

label lad_day1_evening_bedroom_doctor:
    call lad_bedroom_default
    call lad_bedroom_stay_away
    return

label lad_day1_evening_bedroom_captain:
    call lad_bedroom_default
    call lad_bedroom_stay_away
    return

label lad_day1_evening_bedroom_host:
    call lad_bedroom_default
    call lad_bedroom_stay_away
    return

label lad_day1_evening_bedroom_drunk:
    call lad_bedroom_default
    call lad_bedroom_stay_away
    return

label lad_day1_evening_bedroom_broken:
    call lad_bedroom_default
    call lad_bedroom_stay_away
    return

label lad_day1_evening_bedroom_nurse:
    call lad_bedroom_default
    call lad_bedroom_stay_away
    return

# Attic
label lad_day1_evening_storage:
    call lad_storage_default
    return

label lad_day1_evening_males_room:
    call lad_males_room_default
    return

label lad_day1_evening_females_room:
    call lad_females_room_default
    return

label lad_day1_evening_butler_room:
    call lad_butler_room_default
    return