label lad_day2_evening_map_menu:
    python:   
        # -------------------------
        # Saturday, Evening
        # -------------------------
        lad_day2_evening_map_menu = TimedMenu("lad_day2_evening_map_menu", [
            TimedMenuChoice(default_room_text('storage'), 'lad_day2_evening_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'lad_day2_evening_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'lad_day2_evening_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'lad_day2_evening_butler_room', 10, room='butler_room'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'lad_day2_evening_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'lad_day2_evening_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'lad_day2_evening_bedroom_drunk', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'lad_day2_evening_bedroom_nurse', 10, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('library'), 'lad_day2_evening_library', 10, room='library'),
            TimedMenuChoice(default_room_text('tea_room'), 'lad_day2_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'lad_day2_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'lad_day2_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'lad_day2_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'lad_day2_evening_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('kitchen'), 'lad_day2_evening_kitchen', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'lad_day2_evening_scullery', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'lad_day2_evening_garage', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'lad_day2_evening_gun_room', 10, room='gun_room'),
            TimedMenuChoice(
                default_room_text('bedroom_doctor'), 
                'lad_day2_bedroom_doctor', 
                20, 
                room = 'bedroom_doctor',
            ),
            TimedMenuChoice(
                'Go to sleep and hope for the best.', 
                'lad_day2_evening_sleep',
                early_exit = True, 
                room = 'bedroom_lad',
            ),
            TimedMenuChoice(
                'Have a talk with Amelia Baxter', 
                'lad_day2_evening_bedroom_psychic',
                0,
                room = 'bedroom_psychic',
            ),
            TimedMenuChoice(
                'Check if there is someone in the Billiard Room', 
                'lad_day2_evening_billiard_room', 
                0, 
                room = 'billiard_room',
                keep_alive = True, 
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'lad_day2_bedroom_broken', 
                20, 
                room = 'bedroom_broken',
                condition="not lad_details.observations.is_unlocked('green_liquid')"
            ),
            # If you've already seen the liquid, you can still visit but for nothing
            TimedMenuChoice(
                'Richard III Bedroom', 
                'lad_day2_bedroom_broken_back', 
                10, 
                room = 'bedroom_broken',
                condition="lad_details.observations.is_unlocked('green_liquid') and not all_menus['lad_day2_evening_map_menu'].choices[22].hidden"
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'lad_day2_bedroom_broken_back_for_drink', 
                10, 
                room = 'bedroom_broken',
                condition = 'lad_details.saved_variables["day2_evening_taste_from_flask"]'
            ),
        ], is_map = True)     

    return

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

    # Hide all downstairs choices for the current menu
    # $ lad_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('gun_room'))
    # $ lad_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('garage'))
    # $ lad_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('scullery'))
    # $ lad_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('kitchen'))

    $ all_menus[lad_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('gun_room'))
    $ all_menus[lad_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('garage'))
    $ all_menus[lad_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('scullery'))
    $ all_menus[lad_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))
     
    call lad_downstairs_default

    return


# First Floor
label lad_day2_evening_library:
    call lad_library_default
    return

label lad_day2_evening_dining_room:
    call lad_dining_room_default
    return

label lad_day2_evening_garden:

    $ change_room('great_hall')

    """
    I open the door to go to the garden.

    But after a quick glance outside, I realize it's pitch black.

    I don't think I'll be able to do anything there at this hour.
    """
    return

label lad_day2_evening_entrance_hall:
    call lad_entrance_hall_default
    return

label lad_day2_evening_portrait_gallery:
    call lad_portrait_gallery_default
    return

label lad_day2_evening_tea_room:
    call lad_tea_room_default
    return

# Bedrooms
label lad_bedroom_stay_away_day2:

    """
    Should I try to enter anyway?

    No, that's probably a bad idea.

    Everyone is in the house now, so it would be too risky.
    """
    
    return

# Nurse
label lad_day2_evening_bedroom_nurse:

    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on the door.

    A low voice answers.
    """

    nurse """
    Yes? What is it?
    """
    
    $ unlock_map('bedroom_nurse')

    lad """
    Miss Marsh, it's Ted Harring.

    I was wondering if we could talk.
    """

    nurse """
    It's incredibly late, Mr Harring.

    Can't it wait until the morning?
    """

    lad """
    Yes, of course, sorry for disturbing you.
    """

    return

# Captain
label lad_day2_evening_bedroom_captain:
    # In the billiard room
    call lad_bedroom_default

    call lad_bedroom_stay_away_day2

    return

# Host
label lad_day2_evening_bedroom_host:
    # Preparing to leave
    call lad_bedroom_default

    call lad_bedroom_stay_away_day2

    return

# Drunk
label lad_day2_evening_bedroom_drunk:

    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on the door.
    """

    drunk """
    Grrr, Mrrrr, Errrr
    """

    """
    I can hear Samuel Manning's voice, but it's incoherent and he's mostly just moaning.

    It's pretty clear that he's blind drunk.

    I know the door is locked, so there' i's no point trying to enter.
    """

    $ unlock_map('bedroom_drunk')

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
