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
    $ lad_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('gun_room'))
    $ lad_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('garage'))
    $ lad_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('scullery'))
    $ lad_details.saved_variables["day2_evening_map_menu"].hide_specific_choice(default_room_text('kitchen'))

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
    It's incredibly late, Mister Harring.

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

    I know that the door is closed, so there's no point in trying to enter.
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
