
label downstairs_default:
    scene basement_stairs

    "I was on my way to the basement, when the butler stopped me."

    butler "Excuse me sir, but downstairs is for staff only."

    # TODO GET CURRENT TALKER ..... for default text? or personalized text ?
    # $ default_char = get_char(current_character.text_id)
    if current_character.text_id == "lad":
        lad "Oh I am sorry, I didn't know."

    return

label gun_room_default:
    call change_room('gun_room')
    
    """
    A room filled with guns.

    I better not touch them, I might hurt myself.
    """

    return

label generic_exterior_bad_weather:
    scene great_hall
    """
    I reach the great hall to go out. 
    
    But the weather is so bad I don't think it's a good idea.
    """
    return

label manor_exterior_default:
    # TODO adapt depending on the weather
    call generic_exterior_bad_weather

    return

label forest_default:
    # TODO adapt depending on the weather
    call generic_exterior_bad_weather

    return

label garage_default:
    
    # Answers different based on the day (first day weather is too bad)
    """
    There is a garage outside.

    But I am not getting out while there is a storm.
    """

    return

label tea_room_default:
    
    scene tea_room
    
    "It's empty"

    "No need to stay here."

    return

label billiard_room_default:
    
    scene billiard_room
    
    "It's empty"

    "No need to stay here."

    return

label bedroom_default:
    
    scene hallway
    
    "I knock on the door."

    "Nobody answers."

    return

label lad_library:

    # TODO booleon

    if lad_visited_library:
        """
        I have been there already.

        """
    else:

        scene library
        
        """
        It's a very nice library. But what am I doing here ? I can barely read.

        """

        $ lad_details.add_knowledge('education')

        """
        There is an open book on a small table.

        \"A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.\"

        Yeah, I am not reading that.

        I probably better go elsewhere.

        """
        # TODO add info on BOOK ???

        $ lad_visited_library = True

    return

# Downstairs
label kitchen_default:
    call downstairs_default
    return

label scullery_default:
    call downstairs_default
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