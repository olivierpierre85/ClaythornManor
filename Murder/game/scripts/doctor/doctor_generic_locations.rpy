# Downstairs
# label doctor_kitchen_default:
#     call doctor_downstairs_default
#     return

# label doctor_scullery_default:
#     call doctor_downstairs_default
#     return

# label doctor_gun_room_default:
#     call doctor_downstairs_default
#     return

# label doctor_garage_default:
#     call doctor_downstairs_default
#     return

#First floor
label doctor_tea_room_default:
    
    $ change_room('tea_room')
    
    """
    There is not a soul in here and nothing to do at the moment.

    No need to stay any longer.
    """

    return


label doctor_library_default:
    # TODO change to day2? or adapt if needed
    $ change_room('library')

    """
    That is a well-furnished library.

    But with everything that has happened, I do not feel like reading today.
    """

    return


label doctor_portrait_gallery_default:

    $ change_room("portrait_gallery")

    """
    This is clearly where the Claythorn family display their portraits.

    It's rather odd to have so many crammed into such a small room.

    It gives the place quite an eerie atmosphere.

    I don't feel comfortable lingering here too long.
    """

    return


label doctor_garden_default:

    $ change_room('manor_garden')

    # """
    # A beautiful garden.

    # I wandered in it for a while, enjoying a relaxing walk.

    # But I didn't find anything of interest.
    # """

    return


label doctor_dining_room_default:
    
    $ change_room('dining_room')
    
    """
    The dining room.

    No need to linger, nobody will come back here until tomorrow.
    """

    return


label doctor_billiard_room_default:
    
    $ change_room('billiard_room')
    
    # """
    # It's empty.

    # No need to stay here.
    # """

    return


label doctor_entrance_hall_default:
    
    $ change_room("great_hall")
    
    """
    I feel compelled to take another look at this entrance hall.

    It is quite magnificent.
    
    I take in the view for a few minutes.

    Nobody comes.
    """

    return


# First Floor 
label doctor_bedroom_default:
    
    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    doctor """
    Hello, is anyone there?
    """

    """
    There is no answer.
    """

    return

# Attic
label doctor_storage_default:

    call doctor_attic_default

    # """
    # I try to open the attic storage room, but it's closed.
    # """
    
    return


label doctor_females_room_default:

    call doctor_attic_default

    # """
    # I try to open the room, but it's closed.
    # """

    return

label doctor_males_room_default:

    call doctor_attic_default

    # """
    # I try to open the room, but it's closed.
    # """

    return

label doctor_butler_room_default:
    
    call doctor_attic_default

    # """
    # I try to open the room, but it's closed.
    # """

    return



label doctor_attic_default:

    $ change_room("attic_hallway")

    # if not doctor_details.saved_variables['attic_visited']:

    #     """
    #     I took the stairs to the attic.

    #     I'm not sure if I should be here.
    #     """

    #     $ doctor_details.saved_variables["attic_visited"] = True

    return

