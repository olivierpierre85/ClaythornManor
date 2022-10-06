
label downstairs_default:
    scene basement_stairs

    butler "Excuse me sir, but downstairs is for staff only."

    # TODO GET CURRENT TALKER ..... for default text? or personalized text ?
    # $ default_char = get_char(current_character.text_id)
    if current_character.text_id == "lad":
        lad "Oh I am sorry, I didn't know."

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

    "No need to stay here"

    return

label bedroom_default:
    
    scene hallway
    
    "I knock on the door."

    "Nobody answers."

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