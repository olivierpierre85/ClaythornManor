# Downstairs
label lad_day2_evening_kitchen:
    call lad_day2_evening_downstairs_default
    return

label lad_day2_evening_scullery:
    call lad_day2_evening_downstairs_default
    return

label lad_day2_evening_garage:
    call lad_day2_evening_downstairs_default
    return

label lad_day2_evening_gun_room:
    call lad_day2_evening_downstairs_default
    return

label lad_day2_evening_downstairs_default:
    call lad_downstairs_default
    # Hide all downstairs choices for the current menu
    $ lad_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('gun_room'))
    $ lad_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('garage'))
    $ lad_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('scullery'))
    $ lad_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('kitchen'))
    return


# First Floor
label lad_day2_evening_library:
    call lad_library_default
    return

# label lad_day2_evening_billiard_room:
#     call lad_billiard_room_default
#     return

label lad_day2_evening_dining_room:
    call lad_dining_room_default
    return

label lad_day2_evening_garden:
    call lad_garden_default
    return

label lad_day2_evening_entrance_hall:
    call lad_entrance_hall_default
    return

label lad_day2_evening_portrait_gallery:
    call lad_portrait_gallery_default
    return

# Bedroom
label lad_day2_evening_bedroom_try_enter(enter_result, enter_duration=5):

    python:
        enter_text_list = [
            "Let's go in, what's the worst that could happen?",
            "It won't hurt to give it a try. Let's go in and find out.",
            "Let's enter and see what happens, it can't be that bad.",
            "What's the harm in entering? Let's go!",
            "Come on, let's go inside. What's the worst that could go wrong?",
            "Shall we enter? What's the worst that could occur?"
        ]

        no_enter_text_list= [
            "I definitely shouldn't enter, that would be reckless!",
            "I shouldn't go in, that's too dangerous!",
            "I'd better not enter, it could be risky.",
            "That's a bad idea, I shouldn't go inside.",
            "I don't want to take unnecessary risks, I shouldn't go in.",
            "It's not worth the danger, I'm not going in."
        ]
    
        enter_text = enter_text_list[lad_details.saved_variables['day2_nohunt_bedroom_tries']]
        no_enter_text = no_enter_text_list[lad_details.saved_variables['day2_nohunt_bedroom_tries']]
        
    if lad_details.saved_variables['day2_nohunt_bedroom_tries'] == 0:

        """
        Most people are out for the hunt, so I guess I could try to enter the room anyway.

        But it won't look good if I am caught.

        Why should I do?
        """

        $ lad_details.saved_variables['day2_nohunt_bedroom_tries'] += 1

    else:

        """
        There seems to be nobody here as well.
        """

        $ lad_details.saved_variables['day2_nohunt_bedroom_tries'] += 1

    call run_menu(
        TimedMenu([
            TimedMenuChoice(enter_text, enter_result, enter_duration, early_exit = True),
            TimedMenuChoice(no_enter_text, 'lad_day2_evening_default_room_no_enter', enter_duration, early_exit = True),
        ])
    )

    return

label lad_day2_evening_default_room_no_enter:
    
    """
    It's better not to enter this room for now.
    """

    return

label lad_day2_evening_default_room_locked:
    
    """
    I try to push the door opened.

    It's locked.
    """

    return

# Psychic
# label lad_day2_evening_psychic_room:
    
#     call lad_bedroom_default

#     call lad_day2_evening_bedroom_try_enter('lad_day2_evening_psychic_room_enter')

#     return

label lad_day2_evening_psychic_room_enter:
    # May knows whose room it is so lock it to avoid weird dialog for now
    call lad_day2_evening_default_room_locked

    return

# Doctor
label lad_day2_evening_doctor_room:

    call lad_bedroom_default

    call lad_day2_evening_bedroom_try_enter('lad_day2_evening_doctor_room_enter')

    return

# Nurse
label lad_day2_evening_doctor_room_enter:
    # May knows whose room it is so lock it to avoid weird dialog for now
    call lad_day2_evening_default_room_locked

    return

label lad_day2_evening_nurse_room:

    call lad_bedroom_default

    call lad_day2_evening_bedroom_try_enter('lad_day2_evening_nurse_room_enter')

    return

label lad_day2_evening_nurse_room_enter:

    call lad_day2_evening_default_room_locked

    return

# Captain
label lad_day2_evening_captain_room:

    call lad_bedroom_default

    call lad_day2_evening_bedroom_try_enter('lad_day2_evening_captain_room_enter', enter_duration=20)

    return

# Host
label lad_day2_evening_host_room:

    call lad_bedroom_default

    call lad_day2_evening_bedroom_try_enter('lad_day2_evening_host_room_enter')

    return

label lad_day2_evening_host_room_enter:
    
    call lad_day2_evening_default_room_locked

    return

# Drunk
label lad_day2_evening_drunk_room:

    call lad_bedroom_default

    """
    After knocking, the door slightly opens.

    It was not even closed.
    """

    call lad_day2_evening_bedroom_try_enter('lad_day2_evening_drunk_room_enter', enter_duration=20)

    return


# 
# Attic
# 
label lad_day2_evening_storage:
    call lad_storage_default
    return

label lad_day2_evening_males_room:
    call lad_males_room_default
    return

label lad_day2_evening_females_room:
    call lad_females_room_default
    return

label lad_day2_evening_butler_room:
    call lad_butler_room_default
    return