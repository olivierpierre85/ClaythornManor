# Map choices for Doctor, Friday evening
# Downstairs
label doctor_day1_evening_kitchen:
    call doctor_day1_evening_downstairs_default
    return

label doctor_day1_evening_scullery:
    call doctor_day1_evening_downstairs_default
    return

label doctor_day1_evening_garage:
    call doctor_day1_evening_downstairs_default
    return

label doctor_day1_evening_gun_room:
    call doctor_day1_evening_downstairs_default
    return

label doctor_day1_evening_downstairs_default:
        
    call doctor_downstairs_default
    # Hide all downstairs choices for the current menu
    $ doctor_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('gun_room'))
    $ doctor_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('garage'))
    $ doctor_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('scullery'))
    $ doctor_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('kitchen'))
    return


# First Floor
label doctor_day1_evening_library:
    call doctor_library_default
    return

label doctor_day1_evening_tea_room:
    call doctor_tea_room_default
    return

label doctor_day1_evening_dining_room:
    call doctor_dining_room_default
    return

label doctor_day1_evening_garden:

    $ change_room('great_hall')
    
    """
    I reach the great hall and prepare to open the door. 

    However, the weather is so bad that only a madman would venture out now. 

    I'd be better off doing something else at the moment.
    """

    return

label doctor_day1_evening_entrance_hall:
    call doctor_entrance_hall_default
    return

label doctor_day1_evening_portrait_gallery:
    call doctor_portrait_gallery_default
    return

# Closed bedrooms
label doctor_bedroom_stay_away:

    """
    Should I try to enter anyway?

    No, that's probably a bad idea.
    """
    
    return

label doctor_day1_evening_bedroom_doctor:

        # TODO do drugs if you chose to go to your room early
    # => Death

    return

label doctor_day1_evening_bedroom_captain:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_host:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_drunk:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_broken:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_nurse:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

# Attic
label doctor_day1_evening_storage:
    call doctor_storage_default
    return

label doctor_day1_evening_males_room:
    call doctor_males_room_default
    return

label doctor_day1_evening_females_room:
    call doctor_females_room_default
    return

label doctor_day1_evening_butler_room:
    call doctor_butler_room_default
    return