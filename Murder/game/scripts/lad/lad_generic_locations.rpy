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

label lad_attic_default:

    $ change_room("attic_hallway")

    if not lad_details.saved_variables['attic_visited']:
        
        """
        I took the stairs to the attic.

        I am not sure I can be there.
        """

        $ lad_details.saved_variables["attic_visited"] = True

    return

label lad_downstairs_default:

    $ change_room("basement_stairs")

    """
    I was on my way to the basement, when someone stops me.
    """

    maid "I am sorry, but downstairs is for staff only." 

    lad "Oh I am sorry, I didn't know."

    $ lad_details.saved_variables["has_met_maid"] = True

    $ lad_details.saved_variables["psychic_generic_other_guests_saturday_morning_ask"] = True

    return

label lad_garden_default:

    $ change_room('manor_garden')
    
    """
    Beautiful garden.

    But not much to do here.
    """

    return

label lad_garage_default:

    call lad_downstairs_default

    return


label lad_library_default:
    
    $ change_room('library')
    
    "It's empty"

    "No need to stay here."

    return

label lad_tea_room_default:
    
    $ change_room('tea_room')
    
    "It's empty"

    "No need to stay here."

    return

label lad_dining_room_default:
    
    $ change_room('dining_room')
    
    "It's empty"

    "No need to stay here."

    return

label lad_billiard_room_default:
    
    $ change_room('billiard_room')
    
    "It's empty"

    "No need to stay here."

    return

label lad_bedroom_default:
    
    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on the door.

    Nobody answers.
    """

    return

label lad_entrance_hall_default:
    
    scene great_hall
    
    """
    Impressive entrance hall
    
    But it's empty.
    """

    return

label lad_portrait_gallery_default:
    
    scene portrait_gallery
    
    """
    That's a creepy portrait gallery.

    I don't recognize anyone, so I guess these are people from the Claythorn family.
    """

    return

# Downstairs
label lad_kitchen_default:
    call lad_downstairs_default
    return

label lad_scullery_default:
    call lad_downstairs_default
    return

label lad_gun_room_default:
    call lad_downstairs_default
    return

# Attic
label lad_storage_default:

    call lad_attic_default

    """
    I try to open the attic storage room but it's closed.
    """
    
    return

label lad_females_room_default:

    call lad_attic_default

    """
    I try to open the room but it's closed.
    """

    return

label lad_males_room_default:

    call lad_attic_default

    """
    I try to open the room but it's closed.
    """

    return

label lad_butler_room_default:
    
    call lad_attic_default

    """
    I try to open the room but it's closed.
    """

    return