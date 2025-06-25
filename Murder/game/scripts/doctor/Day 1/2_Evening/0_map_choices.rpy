# Map choices for Doctor, Friday evening
# Downstairs
label doctor_day1_evening_kitchen:
    call doctor_day1_evening_downstairs_default
    return

label doctor_day1_evening_scullery:
    call doctor_day1_evening_downstairs_default
    return

label doctor_day1_evening_garage:
    call doctor_day1_evening_downstairs_default
    return

label doctor_day1_evening_gun_room:
    call doctor_day1_evening_downstairs_default
    return

label doctor_day1_evening_downstairs_default:
        
    call doctor_downstairs_day1
    # Hide all downstairs choices for the current menu
    $ doctor_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('gun_room'))
    $ doctor_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('garage'))
    $ doctor_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('scullery'))
    $ doctor_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('kitchen'))
    return


label doctor_downstairs_day1:

    $ change_room("basement_stairs")

    """
    I ought to have a look downstairs. Might be something of interest there.
    """

    footman """
    Good evening, sir. I'm afraid guests aren't permitted beyond this point.
    """

    """
    I offer him my warmest smile.
    """

    doctor """
    I do apologise. I'm only having a quick look. Could you make an exception?

    I promise I won't be long.
    """

    footman """
    If it were up to me, I'd gladly say yes.

    But Lady Claythorn was quite clear with her instructions.

    I'm sure you understand.

    Please don't take it personally.
    """

    """
    He says it with a warm smile of his own.

    His eyes say sorry, but there's something else there, too.

    I wonder if...
    """

    call run_menu(
        TimedMenu("doctor_has_try_sneaking_downstairs", [
            TimedMenuChoice("Try flirting with him", 'doctor_downstairs_flirt', 15, early_exit=True),
            TimedMenuChoice("No, he clearly won't change his mind", 'doctor_downstairs_apologize', 15, early_exit=True),
        ])
    )

    return


label doctor_downstairs_flirt:

    doctor """
    That's a shame, but I do understand. Orders are orders.

    Still, I was rather hoping you'd show me around.

    There are a few things I wouldn't mind chatting to you about.
    """

    footman """
    I'm a bit tied up at the moment.

    But I could make time later, if you'd still like to talk.
    """

    doctor """
    I'd like that very much.

    Where shall we meet?
    """

    footman """
    Hard to say when I'll be free.

    But I could pop by your room once I've a moment—if you don't mind.
    """

    """
    Well, that was rather forward.

    I glance around to check we're alone.
    
    We are.
    """

    doctor """
    That sounds perfect.

    I'll see you later, then.
    """

    $ doctor_details.important_choices.unlock('flirt')

    return


label doctor_downstairs_apologize:

    doctor """ 
    Quite right.

    I'll be off, then.

    Good evening.
    """

    footman """
    Good evening, sir.
    """

    return


# First Floor
label doctor_day1_evening_library:
    call doctor_library_default
    return

label doctor_day1_evening_tea_room:
    call doctor_tea_room_default
    return

label doctor_day1_evening_dining_room:
    call doctor_dining_room_default
    return

label doctor_day1_evening_garden:

    $ change_room('great_hall')
    
    # """
    # I reach the great hall and prepare to open the door. 

    # However, the weather is so bad that only a madman would venture out now. 

    # I'd be better off doing something else at the moment.
    # """

    return


label doctor_day1_evening_entrance_hall:
    call doctor_entrance_hall_default
    return

label doctor_day1_evening_portrait_gallery:
    call doctor_portrait_gallery_default
    return

# Closed bedrooms
label doctor_bedroom_stay_away:

    """
    Should I try to enter anyway?

    No, that's probably a bad idea.
    """
    
    return

label doctor_day1_evening_bedroom_doctor:

        # TODO do drugs if you chose to go to your room early
    # => Death

    return

label doctor_day1_evening_bedroom_captain:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_host:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_drunk:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_broken:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_nurse:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

# Attic
label doctor_day1_evening_storage:
    call doctor_storage_default
    return

label doctor_day1_evening_males_room:
    call doctor_males_room_default
    return

label doctor_day1_evening_females_room:
    call doctor_females_room_default
    return

label doctor_day1_evening_butler_room:
    call doctor_butler_room_default
    return