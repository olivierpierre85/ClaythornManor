# Map choices for PSYCHIC, Friday evening
label psychic_day1_evening_map_menu:
    python:
        psychic_day1_evening_map_menu= TimedMenu("psychic_day1_evening_map_menu", [
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'psychic_day1_evening_downstairs_default', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'psychic_day1_evening_downstairs_default', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'psychic_day1_evening_downstairs_default', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'psychic_day1_evening_downstairs_default', 10, room='gun_room'),
            # first floor
            TimedMenuChoice(default_room_text('tea_room'), 'psychic_tea_room_default', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'psychic_dining_room_default', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'psychic_day1_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'psychic_entrance_hall_default', 10, room='entrance_hall'),
            # TimedMenuChoice(default_room_text('portrait_gallery'), 'psychic_day1_evening_portrait_gallery', 10, room='portrait_gallery'),
            #Bedrooms
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'psychic_day1_evening_default_bedroom', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'psychic_day1_evening_default_bedroom', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'psychic_day1_evening_default_bedroom', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'psychic_day1_evening_bedroom_drunk', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_broken'), 'psychic_day1_evening_default_bedroom', 10, room='bedroom_broken'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'psychic_day1_evening_default_bedroom', 10, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('bedroom_lad'), 'psychic_day1_evening_default_bedroom', 10, room='bedroom_lad'),
            # attic
            TimedMenuChoice(default_room_text('storage'), 'psychic_day1_evening_attic_default', 60, room='storage', condition=attic_default),
            TimedMenuChoice(default_room_text('males_room'), 'psychic_day1_evening_attic_default', 60, room='males_room', condition=attic_default),
            TimedMenuChoice(default_room_text('females_room'), 'psychic_day1_evening_attic_default', 60, room='females_room', condition=attic_default),
            TimedMenuChoice(default_room_text('butler_room'), 'psychic_day1_evening_attic_default', 60, room='butler_room', condition=attic_default),

            # Specific actions
            TimedMenuChoice(
                'Go to bed', 
                'generic_cancel', 
                room = 'bedroom_psychic', 
                early_exit = True
            ),
            TimedMenuChoice(
                'Meet the others in the billiard room', 
                'psychic_day1_evening_billiard_room', 
                0, 
                keep_alive = True, 
                room = 'billiard_room'
            ),
        ] + copy.deepcopy(lord_choices)
        , is_map = True)


    return

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

    $ change_room('entrance_hall')
    
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

label psychic_day1_evening_bedroom_drunk:

    call psychic_bedroom_default_no_answer

    call psychic_bedroom_stay_away

    """
    On the other hand, I notice that the door to this room is not properly closed.  

    I feel tempted to go in, yet I cannot. It would be too dangerous, for now.  
    """

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
