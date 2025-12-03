label psychic_day2_evening_map_menu:
    python:
        # -------------------------
        # Saturday Evening
        # ------------------------- 
        psychic_day2_evening_map_menu = TimedMenu("psychic_day2_evening_map_menu", [
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'psychic_day2_evening_downstairs_default', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'psychic_day2_evening_downstairs_default', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'psychic_day2_evening_downstairs_default', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'psychic_day2_evening_downstairs_default', 10, room='gun_room'),
            # first floor
            TimedMenuChoice(default_room_text('tea_room'), 'psychic_tea_room_default', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'psychic_dining_room_default', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'psychic_day2_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'psychic_entrance_hall_default', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('library'), 'psychic_library_default', 10, room='library'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'psychic_portrait_gallery_default', 10, room='portrait_gallery'),   
            # Bedrooms 
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'psychic_day2_evening_bedroom_doctor', 20, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'psychic_day2_evening_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'psychic_day2_evening_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'psychic_day2_evening_bedroom_drunk', 10, room='bedroom_drunk'),
            # attic
            TimedMenuChoice(default_room_text('storage'), 'psychic_day2_evening_attic_default', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'psychic_day2_evening_attic_default', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'psychic_day2_evening_attic_default', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'psychic_day2_evening_attic_default', 10, room='butler_room'),
            # TimedMenuChoice(default_room_text('storage'), 'psychic_day2_evening_attic_default', 10, room='storage', condition=attic_default),
            # TimedMenuChoice(default_room_text('males_room'), 'psychic_day2_evening_attic_default', 10, room='males_room', condition=attic_default),
            # TimedMenuChoice(default_room_text('females_room'), 'psychic_day2_evening_attic_default', 10, room='females_room', condition=attic_default),
            # TimedMenuChoice(default_room_text('butler_room'), 'psychic_day2_evening_attic_default', 10, room='butler_room', condition=attic_default),
            # TimedMenuChoice(default_room_text('storage'), 'psychic_day2_evening_attic_return_too_soon', 10, room='storage', condition=attic_return_too_soon),
            # TimedMenuChoice(default_room_text('males_room'), 'psychic_day2_evening_attic_return_too_soon', 10, room='males_room', condition=attic_return_too_soon),
            # TimedMenuChoice(default_room_text('females_room'), 'psychic_day2_evening_attic_return_too_soon', 10, room='females_room', condition=attic_return_too_soon),
            # TimedMenuChoice(default_room_text('butler_room'), 'psychic_day2_evening_attic_return_too_soon', 10, room='butler_room', condition=attic_return_too_soon),
            # TOO late to approach Ted Harring, only chance during the simple menu before dinner
            # TimedMenuChoice(
            #     default_room_text('bedroom_lad'), 
            #     'psychic_day2_evening_lad_discussion', 
            #     20, 
            #     room='bedroom_lad',
            #     condition = "not psychic_details.threads.is_unlocked('visit_lad')"
            # ),
            TimedMenuChoice(
                default_room_text('bedroom_lad'), 
                'psychic_day2_evening_bedroom_lad', 
                20, 
                room='bedroom_lad',
            ),
            TimedMenuChoice(
                'Check if there is someone in the Billiard Room', 
                'psychic_day2_evening_billiard_room', 
                0, 
                room = 'billiard_room',
                keep_alive = True, 
            ),
            TimedMenuChoice(
                default_room_text('bedroom_nurse'),
                'psychic_day2_evening_bedroom_nurse_gone',
                0, 
                room='bedroom_nurse',
            ),
            TimedMenuChoice(
                'Wait in your room for Ted Harring', 
                'psychic_day2_evening_cancel', 
                0, 
                early_exit = True, 
                room = 'bedroom_psychic',
                condition = "psychic_details.threads.is_unlocked('visit_lad')"
            ),
            TimedMenuChoice(
                'Wait in your room', 
                'psychic_day2_evening_cancel', 
                0, 
                early_exit = True, 
                room = 'bedroom_psychic',
                condition = "not psychic_details.threads.is_unlocked('visit_lad')"
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'psychic_day2_bedroom_broken', 
                20, 
                room = 'bedroom_broken',
                condition = "psychic_details.saved_variables['day2_has_seen_bedroom_broken'] == False"
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'psychic_day2_bedroom_broken_already_see', 
                20, 
                room = 'bedroom_broken',
                condition = "psychic_details.saved_variables['day2_has_seen_bedroom_broken'] == True and not all_menus['psychic_day2_evening_map_menu'].choices[25].hidden" #Check that previous choice hasn't been made, allow to avoid going twice to the same room
            )
        ],
        # ] + copy.deepcopy(lord_choices), # It's too late for the lord now, because I need to let psychic try the butler room
        is_map = True)

    return

# Downstairs
label psychic_day2_evening_downstairs_default:

    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('gun_room'))
    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('garage'))
    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('scullery'))
    $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))

    call psychic_downstairs_default

    return


label psychic_day2_evening_garden:

    # TODO replace by garden at night and dark contemplation ?

    $ change_room('great_hall')
    
    """
    I reach the large hall and prepare to open the door.

    The weather has improved, but it is pitch dark outside.
    
    What possessed me? There is no reason to go out now.
    """

    return

# First Floor

# Bedroom
label psychic_day2_evening_bedroom_try_enter(menu_id, enter_result, enter_duration=10):

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
    
        enter_text = enter_text_list[psychic_details.saved_variables['day2_evening_bedroom_tries']]
        no_enter_text = no_enter_text_list[psychic_details.saved_variables['day2_evening_bedroom_tries']]
        
    if psychic_details.saved_variables['day2_evening_bedroom_tries'] == 0:

        """
        Should I try to enter anyway?
        """

        $ psychic_details.saved_variables['day2_evening_bedroom_tries'] += 1

    else:

        """
        There seems to be nobody here as well.
        """

        $ psychic_details.saved_variables['day2_evening_bedroom_tries'] += 1

    call run_menu(
        TimedMenu(
            id=menu_id,
            choices=[
                TimedMenuChoice(enter_text, enter_result, enter_duration, early_exit=True),
                TimedMenuChoice(no_enter_text, 'psychic_day2_evening_default_room_no_enter', enter_duration, early_exit=True),
            ]
        )
    )

    return

label psychic_day2_evening_default_room_no_enter:
    
    """
    It's better not to enter this room for now.
    """

    return

label psychic_day2_evening_default_room_locked:
    
    """
    I try to push the door open.

    It's locked.
    """

    return

# Lad - ???  (uses the calling label as the menu id)
label psychic_day2_evening_bedroom_lad:

    call psychic_bedroom_default_no_answer

    call psychic_day2_evening_bedroom_try_enter('psychic_day2_evening_bedroom_lad', 'psychic_day2_evening_default_room_locked')

    """
    Where could Ted Harring be anyway?
    """

    return


# Doctor - Dead
label psychic_day2_evening_bedroom_doctor:

    """
    The door stands slightly ajar.

    I notice faint traces of blood on the floor.

    Cautiously, I step inside and see Doctor Baldwin's body.
    """

    $ change_room('bedroom_doctor')

    """
    He is lying peacefully in his bed.

    Unsure what I could do here, I decide to leave.
    """

    $ unlock_map('bedroom_doctor')
    # TODO: Add possibility to snoop?

    return


# Captain - In the billiard room
label psychic_day2_evening_bedroom_captain:

    call psychic_bedroom_default_no_answer

    call psychic_day2_evening_bedroom_try_enter('psychic_day2_evening_bedroom_captain', 'psychic_day2_evening_default_room_locked')

    return


# Host - Preparing to leave
label psychic_day2_evening_bedroom_host:

    call psychic_bedroom_default_no_answer

    call psychic_day2_evening_bedroom_try_enter('psychic_day2_evening_bedroom_host', 'psychic_day2_evening_default_room_locked')

    return


# Broken (if already seen in the afternoon)
label psychic_day2_bedroom_broken_already_see:

    $ change_room("bedrooms_hallway")

    """
    I stand once again in front of Thomas Moody's room.

    I do not know what compelled me to come here again.

    I try to open the door, but I can't. The memory of his dead body is still too fresh in my mind.

    I'd better go somewhere else.
    """

    return


# Drunk
label psychic_day2_evening_bedroom_drunk:

    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on the door.
    """

    drunk """
    Grrr, Mrrrr, Errrr
    """

    """
    I recognise Samuel Manning's voice, and it's clear he is too drunk to be coherent. 
    
    Since the door is locked, I decide not to interfere.
    """

    $ unlock_map('bedroom_drunk')

    return

# Attic - Too late for lord Now => 
label psychic_day2_evening_attic_default:

    $ change_room("attic_hallway")

    if not psychic_details.saved_variables["day2_evening_attic_visited"]:

        $ psychic_details.saved_variables["day2_evening_attic_visited"] = True

        if psychic_details.threads.is_unlocked('visited_attic'):

            """
            I am back in the attic.

            But it seems there is nobody now.

            Maybe it's too late.
            """

        else:

            """
            I climb the stairs to the attic and arrive in a dimly lit hallway.

            There are multiple doors, most of them lie in darkness.
            """
        
    else:

        """
        I am back in the attic.
        """

    """
    When I find the right room, I try to open it.
    """

    play sound door_locked

    """
    It's locked.

    And I couldn't force it open myself, obviously.
    """

    return


# label psychic_day2_evening_attic_return_too_soon:

#     # Hide all upstairs choices for the current menu
#     $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
#     $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
#     $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
#     $ all_menus[psychic_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('butler_room'))

#     call psychic_attic_return_too_soon

#     return