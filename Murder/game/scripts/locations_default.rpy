
label generic_cancel:
    return

label attic_default:
    scene attic

    """
    The door to the servants stairs is closed.
    """

    return

label downstairs_default:
    scene basement_stairs

    """
    I was on my way to the basement, when someone stops me.
    """

    maid "I am sorry, but downstairs is for staff only." 

    if current_character.text_id == "lad":
        lad "Oh I am sorry, I didn't know."

        $ lad_details.saved_variables["has_met_maid"] = True

    return

label garden_friday:
    $ change_room('great_hall')
    
    """
    I reach the great hall and get ready to open the door. 
    
    But the weather is so bad, only someone crazy would go out now.

    I'd better do something else at the moment.
    """

    return

label garden_default:

    $ change_room('manor_garden')
    
    """
    Beautiful garden.

    But not much to do here.
    """

    return

label garage_default:

    call downstairs_default
    
    # $ change_room('garage')

    # """
    # The garage is now accessible??? Or is???? Maybe not if downstairs.
    # """

    return

label garage_friday:
    
    # Answers different based on the day (first day weather is too bad)
    """
    There is a garage outside.

    But I am not getting out while there is a storm. TODO or can't access
    """

    return

label library_default:
    
    $ change_room('library')
    
    "It's empty"

    "No need to stay here."

    return

label tea_room_default:
    
    $ change_room('tea_room')
    
    "It's empty"

    "No need to stay here."

    return

label dining_room_default:
    
    $ change_room('dining_room')
    
    "It's empty"

    "No need to stay here."

    return

label billiard_room_default:
    
    $ change_room('billiard_room')
    
    "It's empty"

    "No need to stay here."

    return

label bedroom_default:
    
    scene hallway
    
    "I knock on the door."

    play sound door_knock

    "Nobody answers."

    return

label entrance_hall_default:
    
    scene great_hall
    
    """
    Impressive entrance hall
    
    But it's empty.
    """

    return

label portrait_gallery_default:
    
    scene portrait_gallery
    
    """
    Creepy portrait gallery.

    Not much to do here.
    """

    return

# Downstairs
label kitchen_default:
    call downstairs_default
    return

label scullery_default:
    call downstairs_default
    return

label gun_room_default:
    call downstairs_default
    return

# Attic
label storage_default:
    call attic_default
    return

label males_room_default:
    call attic_default
    return

label butler_room_room_default:
    call attic_default
    return

label servant_stairs_1_default:
    call attic_default
    return

label servant_stairs_2_default:
    call attic_default
    return

# All bedrooms
label host_room_default:
    call bedroom_default
    return

label lad_room_default:
    call bedroom_default
    return

label psychic_room_default:
    call bedroom_default
    return

label captain_room_default:
    call bedroom_default
    return

label broken_room_default:
    call bedroom_default
    return

label nurse_room_default:
    call bedroom_default
    return

label doctor_room_default:
    call bedroom_default
    return

label drunk_room_default:
    call bedroom_default
    return