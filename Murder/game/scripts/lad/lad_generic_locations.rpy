label lad_library:

    $ change_room('library') 
    
    """
    It's a very nice library. But what am I doing here? I can barely read.
    """

    $ lad_details.unlock_knowledge('education')

    """
    There is an open book on a small table.

    \"A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.\"

    Yeah, I am not reading that.

    I probably better go look elsewhere.
    """
    # TODO add info on BOOK???

    $ lad_details.saved_variables["library_visited"] = True

    return

label lad_library_visited:

    $ change_room('library')

    """
    There is nothing different from last time I was in there.
    """

    return

label attic_default:

    $ change_room("attic_hallway")

    if not lad_details.saved_variables['attic_visited']:
        
        """
        I took the stairs to the attic.

        I am not sure I can't be there.
        """

        $ lad_details.saved_variables["attic_visited"] = True

    return

label downstairs_default:

    $ change_room("basement_stairs")

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
    
    $ change_room("bedrooms_hallway")
    
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
    That's a creepy portrait gallery.

    I don't recognize anyone, so I guess these are people from the Claythorn family.
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

    """
    I try to open the attic storage room but it's closed.
    """
    
    return

label females_room_default:

    call attic_default

    """
    I try to open the room but it's closed.
    """

    return

label males_room_default:

    call attic_default

    """
    I try to open the room but it's closed.
    """

    return

label butler_room_default:
    
    call attic_default

    """
    I try to open the room but it's closed.
    """

    return

# label servant_stairs_1_default:
#     call attic_default
#     return

# label servant_stairs_2_default:
#     call attic_default
#     return

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