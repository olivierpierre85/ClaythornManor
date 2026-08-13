# Map choices for the Host (Lady Claythorn), Friday evening

label host_day1_evening_map_menu:
    python:
        host_day1_evening_map_menu = TimedMenu(
            "host_day1_evening_map_menu",
            [   
            # Servants' floor
            map_choice('kitchen', 'host_day1_evening_kitchen', 20),
            map_choice('scullery', 'host_day1_evening_scullery', 20),
            map_choice('garage', 'host_day1_evening_garage', 10),
            map_choice('gun_room', 'host_day1_evening_gun_room', 10),        
            # Ground floor
            map_choice('tea_room', 'host_day1_evening_tea_room', 10),
            map_choice('dining_room', 'host_dining_room_default', 10),
            map_choice('manor_garden', 'host_day1_evening_garden', 10),
            map_choice('entrance_hall', 'host_entrance_hall_default', 10),
            map_choice('servant_stairs', 'host_servant_stairs_default', 10),
            map_choice('portrait_gallery', 'host_portrait_gallery_default', 20),
            map_choice('library', 'host_library_default', 30),
            # Bedrooms (her own room is the retire exit, so it is not listed here)
            map_choice('bedroom_lad', 'host_day1_evening_bedroom_avoid', 10),
            map_choice('bedroom_broken', 'host_day1_evening_bedroom_avoid', 10),
            map_choice('bedroom_nurse', 'host_day1_evening_bedroom_avoid', 10),
            map_choice('bedroom_doctor', 'host_day1_evening_bedroom_avoid', 10),
            map_choice('bedroom_drunk', 'host_day1_evening_bedroom_avoid', 10),
            map_choice('bedroom_psychic', 'host_day1_evening_bedroom_avoid', 10),
            map_choice('bedroom_captain', 'host_day1_evening_bedroom_avoid', 10),
            # Attic
            map_choice('storage', 'host_day1_evening_attic_default', 10),
            map_choice('males_room', 'host_day1_evening_attic_default', 10),
            map_choice('females_room', 'host_day1_evening_attic_default', 10),
            map_choice('attic_butler_room', 'host_day1_evening_attic_default', 10),
            # Specific actions
            TimedMenuChoice('Sit up with your guests in the billiard room', 'host_day1_evening_billiard_room', 90, room='billiard_room'),
            TimedMenuChoice('Retire for the night', 'generic_cancel', early_exit=True, room='bedroom_host'),
        ], is_map = True)

    return


# ------------------------------------
#   DOWNSTAIRS
# ------------------------------------
label host_day1_evening_go_downstairs:

    if host_details.threads.is_unlocked('go_downstairs'):

        return

    $ change_room('servant_stairs')

    """
    I look at the narrow stair down.

    It should lead to the servants' quarters.

    A lady should not go there. 
    
    She should ring, and wait for the servants to come up to her.

    But curiosity is too strong, and I go down anyway.
    """

    $ host_details.threads.unlock('go_downstairs')

    return


label host_day1_evening_kitchen:

    call host_day1_evening_go_downstairs

    $ change_room('kitchen')

    """
    I reach the most important room below stairs, the kitchen.
    
    The girl is there alone, sorting the pots and pans used for dinner.

    I wonder how she managed to prepare an entire dinner.

    She notices me.
    """

    maid """
    Ma'am, I do not think you should be here.
    """

    host """
    I know, but I wanted to check on you.

    And how are you managing so far?
    """

    maid """
    Everything went well, ma'am. We all pitched in for dinner.

    And we will probably spend the night clearing it all up, but we will manage.
    """

    host """
    Very well, I will not disturb you then.

    Good night.
    """

    maid """
    Good night, m'lady.
    """

    return


label host_day1_evening_scullery:

    call host_day1_evening_go_downstairs

    $ change_room('scullery')

    """
    The scullery is empty and cold, and smells of soda and wet stone.

    I take a quick look about the room.

    On the shelf above the sink stands a bottle with its cork out.

    Rat poison. 
    
    And it is half-empty.

    In itself, it is not unusual. 
    
    Old houses have rats.

    Except that this one was shut up until yesterday, and will be again at the end of this weekend.

    Why would anyone bother getting rid of rats for a mere couple of days?

    I leave without a good answer.
    """

    $ host_details.threads.unlock('found_poison')

    return


# ------------------------------------
#   GARAGE
# ------------------------------------
label host_day1_evening_garage:

    call host_day1_evening_go_downstairs

    $ change_room('garage')

    """
    Petrol and cold iron, and a different car from the one we came up in.

    An old tourer, well kept.

    It does not look as though it will start.

    Nothing for me here.
    """

    return

label host_day1_evening_gun_room:

    call host_day1_evening_go_downstairs

    $ change_room('gun_room')

    """
    Sporting guns behind glass, and a handgun lying out on the table.

    It reminds me of a Chekhov's play I once saw.

    I am not sure why.

    Better leave it there.
    """

    return


# ------------------------------------
#   GROUND FLOOR
# ------------------------------------
label host_day1_evening_tea_room:

    $ change_room('tea_room')

    """
    The tea room has been put straight already. 
    
    Cushions plumped, glasses gone, not a ring left on the wood.
    """

    return


label host_day1_evening_garden:

    $ change_room('manor_garden')

    """
    Rain, and a wind coming up through the trees.

    I stand in the doorway long enough to feel the cold on my face.

    I will not be able to go further without ruining my dress.

    So I go back inside before anyone sees the lady of the house standing in the wet.
    """

    return


# ------------------------------------
#   BEDROOMS
# ------------------------------------
label host_day1_evening_bedroom_avoid:

    $ change_room('bedrooms_hallway')

    """
    I have my hand on the door before the sense of it catches up with me.

    No.

    There is nothing in that room worth what it would cost me.

    A guest found on the wrong landing is an eccentric. The lady of the house coming out of a guest's bedroom is a story that reaches the village by Monday.

    And if there is one thing this house cannot afford, it is a story it did not write itself.
    """

    # Block all bedrooms on the first refusal
    $ all_menus[host_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_lad'))
    $ all_menus[host_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_broken'))
    $ all_menus[host_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_nurse'))
    $ all_menus[host_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_doctor'))
    $ all_menus[host_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_drunk'))
    $ all_menus[host_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_psychic'))
    $ all_menus[host_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_captain'))

    return


# ------------------------------------
#   ATTIC (locked, and not her key)
# ------------------------------------
label host_day1_evening_attic_default:

    $ all_menus[host_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[host_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[host_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[host_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('attic_butler_room'))

    $ change_room("attic_hallway")

    """
    I climb the stairs, even though I probably should not.

    I try to open the door.
    """

    play sound door_locked

    """
    Locked, of course.

    And I do not have the key.

    Only he does.

    Out of curiosity, I try another door, then a third, then the last.

    All of them closed.

    I stand on the stair a moment longer than I need to, and then I go back down.
    """

    $ host_details.saved_variables['day1_evening_attic_tried'] = True

    return
