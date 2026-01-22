label psychic_downstairs_default:

    $ change_room("basement_stairs")

    """
    The basement is where the domestic staff work.
    
    I definitely shouldn't go down there, it's not my place.
    """

    return

label psychic_library_intro:

    $ change_room('library') 
    
    """
    Here is an impressive library.

    "A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain." is open on a table.
    """

    return

label psychic_library_default:

    call psychic_library_intro

    """
    But I don't feel like reading now.
    """

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


label psychic_billiard_room_default:
    
    $ change_room('billiard_room')
    
    """
    The billiard room is empty right now.

    I should leave.
    """

    return


label psychic_garden_default:

    $ change_room('manor_garden')
    
    """
    A lovely garden.

    I took a peaceful stroll through it.

    Still, I notice nothing out of the ordinary.
    """

    return


label psychic_entrance_hall_default:
    
    $ change_room("entrance_hall")
    
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


label psychic_bedroom_default_no_answer:
    
    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on the door, waiting for a response.

    There's silence. No one replies.
    """

    return

