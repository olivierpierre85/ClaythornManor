label lad_day2_no_hunt_map_menu:
    python:    
        # -------------------------
        # Saturday, During the Hunt
        # -------------------------        
        lad_day2_no_hunt_map_menu = TimedMenu("lad_day2_no_hunt_map_menu", [
            TimedMenuChoice(default_room_text('storage'), 'lad_day2_no_hunt_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'lad_day2_no_hunt_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'lad_day2_no_hunt_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'lad_day2_no_hunt_butler_room', 10, room='butler_room'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'lad_day2_no_hunt_bedroom_doctor', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'lad_day2_no_hunt_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 'lad_day2_no_hunt_bedroom_psychic', 10, room='bedroom_psychic'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'lad_day2_no_hunt_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'lad_day2_no_hunt_bedroom_drunk', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('library'), 'lad_day2_no_hunt_library', 10, room='library'),
            TimedMenuChoice(default_room_text('billiard_room'), 'lad_day2_no_hunt_billiard_room', 10, room='billiard_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'lad_day2_no_hunt_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'lad_day2_no_hunt_garden', 30, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'lad_day2_no_hunt_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'lad_day2_no_hunt_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('kitchen'), 'lad_day2_no_hunt_kitchen', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'lad_day2_no_hunt_scullery', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'lad_day2_no_hunt_garage', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'lad_day2_no_hunt_gun_room', 10, room='gun_room'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 
                'lad_day2_no_hunt_bedroom_nurse_busy', 
                10, 
                room='bedroom_nurse',
                condition = "lad_details.saved_variables['day2_nohunt_has_visited_tea_room']"
            ),
            TimedMenuChoice(
                default_room_text('bedroom_nurse'),
                'lad_day2_no_hunt_bedroom_nurse',
                15, 
                room='bedroom_nurse',
                condition = "not lad_details.saved_variables['day2_nohunt_has_visited_tea_room']"
            ),
            TimedMenuChoice(
                'Meet the others in the Tea Room', 
                'lad_day2_hunt_tea_room', 
                120, 
                room = 'tea_room',
                keep_alive = True, 
            ),
            TimedMenuChoice(
                'Go back to the Tea Room', 
                'lad_day2_hunt_tea_room_return',  
                room = 'tea_room',
                condition = "lad_details.saved_variables['day2_nohunt_has_visited_tea_room']",
                keep_alive = True, 
            ),
            TimedMenuChoice(
                'Take a nap until the others return', 
                'lad_day2_no_hunt_cancel', 
                240, 
                early_exit = True, 
                room = 'bedroom_lad'
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'lad_day2_bedroom_broken', 
                20, 
                room = 'bedroom_broken',
            )
        ], is_map = True)
    return


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
    # Hide all downstairs choices for the current menu
    # $ lad_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('gun_room'))
    # $ lad_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('garage'))
    # $ lad_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('scullery'))
    # $ lad_details.saved_variables["day2_no_hunt_map_menu"].hide_specific_choice(default_room_text('kitchen'))

    $ all_menus[lad_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('gun_room'))
    $ all_menus[lad_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('garage'))
    $ all_menus[lad_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('scullery'))
    $ all_menus[lad_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))
     
    call lad_downstairs_default

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
label lad_day2_no_hunt_bedroom_try_enter(menu_id, enter_result, enter_duration=5):

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
    
        enter_text = enter_text_list[lad_details.saved_variables['day2_nohunt_bedroom_tries']]
        no_enter_text = no_enter_text_list[lad_details.saved_variables['day2_nohunt_bedroom_tries']]
        
    if lad_details.saved_variables['day2_nohunt_bedroom_tries'] == 0:

        """
        Most people are out for the hunt, so I guess I could try to enter the room anyway.

        But it won't look good if I get caught.

        What should I do?
        """

        $ lad_details.saved_variables['day2_nohunt_bedroom_tries'] += 1

    else:

        """
        There seems to be nobody here as well.
        """

        $ lad_details.saved_variables['day2_nohunt_bedroom_tries'] += 1

    call run_menu(
        TimedMenu(
            id=menu_id,
            choices=[
                TimedMenuChoice(enter_text, enter_result, enter_duration, early_exit=True),
                TimedMenuChoice(no_enter_text, 'lad_day2_no_hunt_default_room_no_enter', enter_duration, early_exit=True),
            ]
        )
    )

    return

label lad_day2_no_hunt_default_room_no_enter:
    
    """
    It's better not to enter this room for now.
    """

    return

label lad_day2_no_hunt_default_room_locked:
    
    """
    I try to push the door open.

    It's locked.
    """

    return

# Psychic
label lad_day2_no_hunt_bedroom_psychic:
    
    call lad_bedroom_default

    call lad_day2_no_hunt_bedroom_try_enter('lad_day2_no_hunt_bedroom_psychic', 'lad_day2_no_hunt_default_room_locked')

    return


# Doctor
label lad_day2_no_hunt_bedroom_doctor:

    call lad_bedroom_default

    call lad_day2_no_hunt_bedroom_try_enter('lad_day2_no_hunt_bedroom_doctor', 'lad_day2_no_hunt_default_room_locked')

    return


# Nurse
label lad_day2_no_hunt_bedroom_nurse:

    call lad_bedroom_default

    call lad_day2_no_hunt_bedroom_try_enter('lad_day2_no_hunt_bedroom_nurse', 'lad_day2_no_hunt_default_room_locked')

    return


# Captain
label lad_day2_no_hunt_bedroom_captain:

    call lad_bedroom_default

    call lad_day2_no_hunt_bedroom_try_enter('lad_day2_no_hunt_bedroom_captain', 'lad_day2_no_hunt_default_room_locked', enter_duration=20)

    return


# Host
label lad_day2_no_hunt_bedroom_host:

    call lad_bedroom_default

    call lad_day2_no_hunt_bedroom_try_enter('lad_day2_no_hunt_bedroom_host', 'lad_day2_no_hunt_default_room_locked')

    return


# Drunk


label lad_day2_no_hunt_bedroom_drunk:

    call lad_bedroom_drunk_default

    call lad_day2_no_hunt_bedroom_try_enter('lad_day2_no_hunt_bedroom_drunk', 'lad_day2_no_hunt_bedroom_drunk_enter', enter_duration=20)

    return


# 
# Attic
# 
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