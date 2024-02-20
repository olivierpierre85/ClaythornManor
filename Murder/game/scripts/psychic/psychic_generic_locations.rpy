label psychic_downstairs_default:

    $ change_room("basement_stairs")

    """
    The basement is where the domestic staff work.
    
    I definitely shouldn't go down there, it's not my place.
    """

    return

label psychic_library_default:

    $ change_room('library') 
    
    """
    Here is an impressive library.

    "A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain." is open on a table.

    But I don't feel like reading now.
    """

    $ psychic_details.saved_variables["library_visited"] = True

    return

label psychic_tea_room_default:
    
    $ change_room('tea_room')
    
    """
    There's no one here.

    There's no reason to linger.
    """

    return

label psychic_dining_room_default:
    
    $ change_room('dining_room')
    
    """
    The dining area is currently unoccupied.

    I shouldn't stay here.
    """

    return

label psychic_entrance_hall_default:
    
    $ change_room("great_hall")
    
    """
    A very nice great hall.
    
    But it is totally empty.
    """

    return

label psychic_portrait_gallery_default:
    
    $ change_room("portrait_gallery")

    if not psychic_details.saved_variables["portrait_gallery_visited"]:
    
        """
        There are quite a few impressive portraits here.

        However, no one else is present.
        """

        $ psychic_details.saved_variables["portrait_gallery_visited"] = True
    
    else:

        """
        The paintings remain unchanged.
        """

        # TODO: Or did they change? 

    return


label psychic_bedroom_default:
    
    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on the door, waiting for a response.

    There's silence. No one replies.
    """

    return

# Attic
label psychic_attic_default:

    $ change_room("attic_hallway")

    """
    I climbed the stairs to the attic.

    The room is filled with darkness.

    I don't think I should explore this place any further.
    
    For now at least.
    """

    return

# TODO maybe won't ever be used? Find what to do with attic
# label psychic_storage_default:

#     call psychic_attic_default

#     """
#     I try to open the attic storage room, but it's closed.
#     """
    
#     return

# label psychic_females_room_default:

#     call psychic_attic_default

#     """
#     I try to open the room, but it's closed.
#     """

#     return

# label psychic_males_room_default:

#     call psychic_attic_default

#     """
#     I try to open the room, but it's closed.
#     """

#     return

# label psychic_butler_room_default:
    
#     call psychic_attic_default

#     """
#     I try to open the room, but it's closed.
#     """

#     return