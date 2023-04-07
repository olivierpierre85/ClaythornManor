# Map choices for LAD, Friday evening
# Downstairs
label lad_day1_evening_kitchen:
    call lad_downstairs_default
    return

label lad_day1_evening_scullery:
    call lad_downstairs_default
    return

label lad_day1_evening_garage:
    call lad_downstairs_default
    return

label lad_day1_evening_gun_room:
    call lad_downstairs_default
    return


# First Floor
label lad_day1_evening_tea_room:
    call lad_tea_room_default
    return

label lad_day1_evening_dining_room:
    call lad_dining_room_default
    return

label lad_day1_evening_garden:

    $ change_room('great_hall')
    
    """
    I reach the great hall and get ready to open the door. 
    
    But the weather is so bad, only someone crazy would go out now.

    I'd better do something else at the moment.
    """

    return

label lad_day1_evening_entrance_hall:
    call lad_entrance_hall_default
    return

label lad_day1_evening_portrait_gallery:
    call lad_portrait_gallery_default
    return

# Closed bedrooms
label lad_day1_evening_doctor_room:
    call lad_bedroom_default
    return

label lad_day1_evening_captain_room:
    call lad_bedroom_default
    return

label lad_day1_evening_host_room:
    call lad_bedroom_default
    return

label lad_day1_evening_drunk_room:
    call lad_bedroom_default
    return

label lad_day1_evening_broken_room:
    call lad_bedroom_default
    return

label lad_day1_evening_nurse_room:
    call lad_bedroom_default
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