# Generic psychic Dialogs.
# Accessible from :
#                   - The lad
#                   - The Captain? TODO not sure

# ?TODO add extra choices possibilities?
label lad_generic:
    
    # Reset if previous early exit
    $ current_character.saved_variables["lad_generic_menu"].early_exit = False
    $ print(current_character.saved_variables["lad_generic_menu"].is_valid())
    call run_menu(current_character.saved_variables["lad_generic_menu"])
    $ print("exit run")
    return


label lad_generic_weather_friday:

    psychic """
    Well, it is not very original to ask about such things when meeting someone new.

    But it is true that is not your average rain. It looks more like a dangerous storm to me.

    And since we are basically in the middle of nowhere, that's reason enough to be a little nervous I suppose.
    """

    return

label lad_generic_weather_saturday:

    return

label lad_generic_weather_sunday:

    return

label lad_generic_room_friday:

    lad """
    I don't know, I haven't been to my room yet.

    I just arrived, I didn't realize I would be the last one here.
    """

    return

label lad_generic_room_psychic:

    lad """
    Oh I am in the \"William the Conqueror\" Bedroom.
    """

    psychic """
    An impressive king, better than mine.
    """

    lad """
    What do you mean?
    """

    """
    I have the \"George III\" Bedroom.

    A strange name as he is not one of our most famous king.

    I wonder why they named a room after him.
    """

    lad """
    And William the Conqueror is better?
    """

    """
    He is serious?

    Hasn't he heard of \"William the Conqueror\"?
    """

    psychic """
    Well, he was a French Duke who was able to take the throne of England from very powerful men.

    That's not nothing.

    On the other hands, he was sometimes also called the Bastard King.

    So make that what you want.
    """

    $ unlock_map('lad_room')

    return


label lad_generic_age_psychic:

    lad """
    I am 22 years old.
    """

    psychic """
    Really, I would I have pegged him older than that.

    I guess it's his rugged look.

    Life is not easy for the working class.
    """

    return
    

label lad_generic_heroic_act:

    lad """
    

    """

    return

label lad_generic_manor:
    
    lad """
    It's very nice.

    A bit far out of town I think.

    But I suppose some people like the isolation.
    """

    return

label lad_generic_cancel:

    return