label psychic_day2_no_hunt_map_menu:
    python:
        # -------------------------
        # Saturday, During the Hunt
        # -------------------------        
        psychic_day2_no_hunt_map_menu = TimedMenu("psychic_day2_no_hunt_map_menu", [
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'psychic_day2_no_hunt_downstairs_default', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'psychic_day2_no_hunt_downstairs_default', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'psychic_day2_no_hunt_downstairs_default', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'psychic_day2_no_hunt_downstairs_default', 10, room='gun_room'),
            # first floor
            TimedMenuChoice(default_room_text('billiard_room'), 'psychic_billiard_room_default', 10, room='billiard_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'psychic_dining_room_default', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'psychic_garden_default', 30, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'psychic_entrance_hall_default', 10, room='entrance_hall'),
            # Bedrooms 
            TimedMenuChoice(default_room_text('bedroom_lad'), 'psychic_day2_no_hunt_bedroom_lad', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'psychic_day2_no_hunt_bedroom_doctor', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'psychic_day2_no_hunt_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'psychic_day2_no_hunt_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'psychic_day2_no_hunt_bedroom_drunk', 10, room='bedroom_drunk'),
            # attic
            TimedMenuChoice(default_room_text('storage'), 'psychic_day2_no_hunt_attic_default', 60, room='storage', condition=attic_default),
            TimedMenuChoice(default_room_text('males_room'), 'psychic_day2_no_hunt_attic_default', 60, room='males_room', condition=attic_default),
            TimedMenuChoice(default_room_text('females_room'), 'psychic_day2_no_hunt_attic_default', 60, room='females_room', condition=attic_default),
            TimedMenuChoice(default_room_text('butler_room'), 'psychic_day2_no_hunt_attic_default', 60, room='butler_room', condition=attic_default),
            
            TimedMenuChoice(default_room_text('storage'), 'psychic_day2_no_hunt_attic_return_too_soon', 10, room='storage', condition=attic_return_too_soon),
            TimedMenuChoice(default_room_text('males_room'), 'psychic_day2_no_hunt_attic_return_too_soon', 10, room='males_room', condition=attic_return_too_soon),
            TimedMenuChoice(default_room_text('females_room'), 'psychic_day2_no_hunt_attic_return_too_soon', 10, room='females_room', condition=attic_return_too_soon),
            TimedMenuChoice(default_room_text('butler_room'), 'psychic_day2_no_hunt_attic_return_too_soon', 10, room='butler_room', condition=attic_return_too_soon),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 
                'psychic_day2_no_hunt_bedroom_nurse_busy', 
                10, 
                room='bedroom_nurse',
                condition = condition_saturday_hunt_morning,
            ),
            TimedMenuChoice(
                "Go check on Rosalind Marsh", 
                'psychic_day2_no_hunt_bedroom_nurse_blood', 
                10, 
                room='bedroom_nurse',
                condition = "not " + condition_saturday_hunt_morning,
            ),
            # TimedMenuChoice(
            #     default_room_text('bedroom_nurse'),
            #     'psychic_day2_no_hunt_bedroom_nurse',
            #     15, 
            #     room='bedroom_nurse',
            #     condition = "not psychic_details.saved_variables['day2_nohunt_has_visited_tea_room']"
            # ),
            # When it was up to you to chose when eating, not anymore
            # TimedMenuChoice(
            #     'Meet Rosalind Marsh in the Tea Room', 
            #     'psychic_day2_hunt_tea_room', 
            #     150, 
            #     room = 'tea_room'
            # ),
            TimedMenuChoice(
                'Wait for Rosalind Marsh in the Tea Room', 
                'generic_cancel', 
                0,
                early_exit = True, 
                room = 'tea_room',
                condition = condition_saturday_hunt_morning
            ),
            TimedMenuChoice(
                'Go back to the Tea Room', 
                'psychic_tea_room_default',  
                10,
                room = 'tea_room',
                condition = "not " + condition_saturday_hunt_morning
            ),
            TimedMenuChoice(
                'Take a nap', 
                'psychic_day2_no_hunt_cancel', 
                60, 
                early_exit = True, 
                room = 'bedroom_psychic',
                condition = condition_saturday_hunt_morning
            ),
            TimedMenuChoice(
                'Wait until the others come back', 
                'psychic_day2_no_hunt_cancel', 
                90, 
                early_exit = True, 
                room = 'bedroom_psychic',
                condition = "not " + condition_saturday_hunt_morning
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'psychic_day2_bedroom_broken', 
                20, 
                room = 'bedroom_broken',
            )
        ] + copy.deepcopy(lord_choices), 
        is_map = True)
    
    return

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
label psychic_day2_no_hunt_bedroom_try_enter(menu_id, enter_result, enter_duration=5):

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
            id=menu_id, 
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

    call psychic_bedroom_default_no_answer

    call psychic_day2_no_hunt_bedroom_try_enter('psychic_day2_no_hunt_bedroom_lad', 'psychic_day2_no_hunt_default_room_locked')

    return


# Doctor
label psychic_day2_no_hunt_bedroom_doctor:

    call psychic_bedroom_default_no_answer

    call psychic_day2_no_hunt_bedroom_try_enter('psychic_day2_no_hunt_bedroom_doctor', 'psychic_day2_no_hunt_default_room_locked')

    return


# Nurse
label psychic_day2_no_hunt_bedroom_nurse:

    call psychic_bedroom_default_no_answer

    call psychic_day2_no_hunt_bedroom_try_enter('psychic_day2_no_hunt_bedroom_nurse', 'psychic_day2_no_hunt_default_room_locked')

    return


# Captain
label psychic_day2_no_hunt_bedroom_captain:

    call psychic_bedroom_default_no_answer

    call psychic_day2_no_hunt_bedroom_try_enter('psychic_day2_no_hunt_bedroom_captain', 'psychic_day2_no_hunt_default_room_locked')

    return


# Host
label psychic_day2_no_hunt_bedroom_host:

    call psychic_bedroom_default_no_answer

    call psychic_day2_no_hunt_bedroom_try_enter('psychic_day2_no_hunt_bedroom_host', 'psychic_day2_no_hunt_default_room_locked')

    return


# Drunk
label psychic_day2_no_hunt_bedroom_drunk:

    call psychic_bedroom_default_no_answer

    """
    The simple push I give to the door opens it.

    I catch a glimpse inside his room from here.

    It is quite untidy.
    """

    call psychic_day2_no_hunt_bedroom_try_enter('psychic_day2_no_hunt_bedroom_drunk', 'psychic_day2_no_hunt_bedroom_drunk_enter', enter_duration=20)

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