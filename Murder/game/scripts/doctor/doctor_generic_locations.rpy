label doctor_library_default:
    # TODO change to day2? or adapt if needed
    $ change_room('library')

    """
    That is a well-furnished library.

    But with everything that has happened, I do not feel like reading today.
    """

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

# label doctor_downstairs_default:


label doctor_garden_default:

    $ change_room('manor_garden')

    # """
    # A beautiful garden.

    # I wandered in it for a while, enjoying a relaxing walk.

    # But I didn't find anything of interest.
    # """

    return


label doctor_tea_room_default:
    
    $ change_room('tea_room')
    
    """
    There is not a soul in here and nothing to do at the moment.

    No need to stay any longer.
    """

    return


label doctor_dining_room_default:
    
    $ change_room('dining_room')
    
    # """
    # The dining room is empty at the moment.
    
    # I shouldn't stay here.
    # """

    return

label doctor_billiard_room_default:
    
    $ change_room('billiard_room')
    
    # """
    # It's empty.

    # No need to stay here.
    # """

    return

label doctor_bedroom_default:


    return

label doctor_entrance_hall_default:
    
    $ change_room("great_hall")
    
    # """
    # It's certainly an impressive entrance hall.
    
    # Nobody is here.
    # """

    return

label doctor_portrait_gallery_default:
    
    $ change_room("portrait_gallery")

    # if not doctor_details.saved_variables["portrait_gallery_visited"]:
    
    #     """
    #     That's a creepy portrait gallery.

    #     I don't recognize anyone, so I guess these are people from the Claythorn family.
    #     """

    #     # TODO: Possibility to zoom in on specific members?

    #     $ doctor_details.saved_variables["portrait_gallery_visited"] = True
    
    # else:

    #     """
    #     Nothing new here.

    #     It still gives me a weird, creepy feeling.
    #     """

    return

# Downstairs
label doctor_kitchen_default:
    call doctor_downstairs_default
    return

label doctor_scullery_default:
    call doctor_downstairs_default
    return

label doctor_gun_room_default:
    call doctor_downstairs_default
    return

label doctor_garage_default:
    call doctor_downstairs_default
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
