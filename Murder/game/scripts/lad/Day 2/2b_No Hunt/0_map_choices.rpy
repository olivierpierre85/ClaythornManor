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
            id="lad_day2_no_hunt_bedroom_try_enter" + enter_result, 
            [
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

label lad_day2_no_hunt_doctor_room_enter:
    # May knows whose room it is so lock it to avoid weird dialog for now
    call lad_day2_no_hunt_default_room_locked

    return

# Nurse
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

    call lad_day2_no_hunt_bedroom_try_enter('lad_day2_no_hunt_captain_room_enter', enter_duration=20)

    return

# Host
label lad_day2_no_hunt_host_room:

    call lad_bedroom_default

    call lad_day2_no_hunt_bedroom_try_enter('lad_day2_no_hunt_host_room_enter')

    return

label lad_day2_no_hunt_host_room_enter:
    
    call lad_day2_no_hunt_default_room_locked

    return

# Drunk
label lad_day2_no_hunt_drunk_room:

    call lad_bedroom_default

    """
    After knocking, the door slightly opens.

    It was not even closed.
    """

    call lad_day2_no_hunt_bedroom_try_enter('lad_day2_no_hunt_drunk_room_enter', enter_duration=20)

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