label lad_library_default:

    $ change_room('library') 

    if not lad_details.saved_variables["library_visited"]:
    
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
    
    else:

        """
        There is nothing different from last time I was in there.

        No reason to look further.
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

    if lad_details.saved_variables["has_try_sneaking_downstairs"] == 0:

        """
        I was on my way to the basement, when a young maid stops me.
        """

        maid """
        Hello Sir, can I help you?
        """ 

        lad """
        Oh, don't mind me. I'm just taking a walk around.
        """

        maid """
        I'm sorry, but the basement is for staff only. 
        
        However, there are plenty of rooms upstairs that you can visit.
        """

        lad """
        Of course, thank you.
        """

        # TODO add maid character menu????? TO say what????

        $ lad_details.saved_variables["has_met_maid"] = True

        $ lad_details.saved_variables["has_try_sneaking_downstairs"] = 1

    elif lad_details.saved_variables["has_try_sneaking_downstairs"] == 1: 
        
        maid """
        You again Sir? As i already told you, I am afraid you are not allowed to be here.
        """ 

        lad """
        Of course, I was just lost. I am terribly sorry.
        """

        maid """
        It's alright, don't worry about it sir.
        """

        """
        I better be careful. If I am caught here a third time, it will start to really look suspicious.
        """

        $ lad_details.saved_variables["has_try_sneaking_downstairs"] = 2

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

label lad_tea_room_default:
    
    $ change_room('tea_room')
    
    """
    There is nobody here.

    No need to stay any longer.
    """

    return

label lad_dining_room_default:
    
    $ change_room('dining_room')
    
    """
    The dining room is empty at the moment.
    
    I shouldn't stay here.
    """

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
    
    $ change_room("great_hall")
    
    """
    It's certainly an impressive entrance hall.
    
    Nobody is here.
    """

    return

label lad_portrait_gallery_default:
    
    $ change_room("portrait_gallery")

    if not lad_details.saved_variables["portrait_gallery_visited"]:
    
        """
        That's a creepy portrait gallery.

        I don't recognize anyone, so I guess these are people from the Claythorn family.
        """

        # TODO possibility to zoom on specific members ?

        $ lad_details.saved_variables["portrait_gallery_visited"] = True
    
    else:

        """
        Nothing new here.

        It still gives me a weird creepy feeling.
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