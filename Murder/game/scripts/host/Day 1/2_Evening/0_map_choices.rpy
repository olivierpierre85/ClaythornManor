# Map choices for the Host (Lady Claythorn), Friday evening
#
# She is the only guest in this house who is supposed to own it, which turns
# the usual rules inside out:
#   - Below stairs is hers by right, so the servants' floor needs no disguise.
#     It is the one place she can hear her own people speak, if they will.
#   - The guest bedrooms are barred to her by common sense, exactly as they are
#     to Thomas Moody. A hostess caught coming out of a guest's room is finished.
#   - The attic is locked and the butler holds the key, which is the whole
#     problem with this weekend in miniature.
#   - The billiard room is not a curiosity but a duty. Sitting up with them
#     unlocks stayed_with_guests, and skipping it costs her a mark against the
#     performance at the debrief.
#
# Budget: 120 units. A look into an empty room costs the usual 10, the rooms
# with something in them 20, the library 30 (she reads the whole entry), and
# the billiard room 40, because she cannot sit down with them and leave again
# after five minutes.

label host_day1_evening_map_menu:
    python:
        host_day1_evening_map_menu = TimedMenu(
            "host_day1_evening_map_menu",
            [
            # Attic
            map_choice('storage', 'host_day1_evening_attic_default', 10),
            map_choice('males_room', 'host_day1_evening_attic_default', 10),
            map_choice('females_room', 'host_day1_evening_attic_default', 10),
            map_choice('attic_butler_room', 'host_day1_evening_attic_default', 10),
            # Bedrooms (her own room is the retire exit, so it is not listed here)
            map_choice('bedroom_lad', 'host_day1_evening_bedroom_avoid', 10),
            map_choice('bedroom_broken', 'host_day1_evening_bedroom_avoid', 10),
            map_choice('bedroom_nurse', 'host_day1_evening_bedroom_avoid', 10),
            map_choice('bedroom_doctor', 'host_day1_evening_bedroom_avoid', 10),
            map_choice('bedroom_drunk', 'host_day1_evening_bedroom_avoid', 10),
            map_choice('bedroom_psychic', 'host_day1_evening_bedroom_avoid', 10),
            map_choice('bedroom_captain', 'host_day1_evening_bedroom_avoid', 10),
            # Ground floor
            map_choice('tea_room', 'host_day1_evening_tea_room', 10),
            map_choice('dining_room', 'host_day1_evening_dining_room', 10),
            map_choice('manor_garden', 'host_day1_evening_garden', 10),
            map_choice('entrance_hall', 'host_day1_evening_entrance_hall', 10),
            map_choice('servant_stairs', 'host_day1_evening_servant_stairs', 10),
            map_choice('portrait_gallery', 'host_day1_evening_portrait_gallery', 20),
            map_choice('library', 'host_day1_evening_library', 30),
            # Servants' floor
            map_choice('kitchen', 'host_day1_evening_kitchen', 20),
            map_choice('scullery', 'host_day1_evening_scullery', 20),
            map_choice('garage', 'host_day1_evening_garage', 10),
            map_choice('gun_room', 'host_day1_evening_gun_room', 10),
            # Specific actions
            TimedMenuChoice('Sit up with your guests in the billiard room', 'host_day1_evening_billiard_room', 40, room='billiard_room'),
            TimedMenuChoice('Retire for the night', 'generic_cancel', early_exit=True, room='bedroom_host'),
        ], is_map = True)

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


label host_day1_evening_dining_room:

    $ change_room('dining_room')

    """
    The table has already being cleared.
    
    It looks goods considering the small number of staff.
    """

    return


label host_day1_evening_entrance_hall:

    $ change_room('entrance_hall')

    """
    The hall, empty, with the lamps turned low.

    I notice the carpet has worn thin along the line a footman would walk, and the brass could do with attention.

    Not what one would expect from a well kept house.

    Hopefully, nobody will think too much of it.
    """

    return


label host_day1_evening_garden:

    $ change_room('manor_garden')

    """
    Rain, and a wind coming up through the trees.

    I stand in the doorway long enough to feel the cold on my face.

    It gives me the boost I did not know I needed.

    Then I go back inside before anyone sees the lady of the house standing in the wet.
    """

    return


label host_day1_evening_servant_stairs:

    $ change_room('servant_stairs')

    """
    The narrow stair the staff use, with a footman's livery hanging on its peg.

    There is nothing for me to do here.
    """

    return


# ------------------------------------
#   LIBRARY (who she is supposed to be)
# ------------------------------------
label host_day1_evening_library:

    $ change_room('library')

    if host_details.threads.is_unlocked('family_history'):

        """
        I have had what I came for out of that book.

        Elisabeth Claythorn, and a title I was never given.

        There is nothing more here for me tonight.
        """

        return

    """
    A better library than the rest of the house deserves.

    A heavy book lies open on the table, left there for the guests to find, no doubt.

    'A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.'

    And there is a thought I do not much care for.

    Every person at that table knows more about my family than I do.

    I was given a house, a voice, a way of holding a fork, and not one word about the woman I am supposed to be.

    That will not do. An actress who does not know her part is only a woman in a good dress.

    I turn to the index. Clarendon, Claridge, Clark.

    Claythorn.
    """

    call library_book_content

    """
    Elisabeth.

    My name is Elisabeth, and I was born in 1865.

    Which makes me fifty-nine years old, and I have been telling myself all evening that I look my age.

    Then the rest of it, and the rest of it is worse.

    The family name is Claythorn. The title is not.

    They hold a peerage. The Earldom of Kilbraith.

    A peer is addressed by his title and never by his surname. The daughter and heir of the Earl of Kilbraith is not 'Lady Claythorn'.

    She is Lady Kilbraith.

    I have spent the whole evening introducing myself by a name that does not exist.

    And he had me learn the fork.
    """

    $ host_details.description_hidden.unlock('name_age')

    $ host_details.threads.unlock('family_history')

    """
    Very well. Panicking is for the rehearsal room.

    If anyone puts it to me, I let the villagers take the blame. They have called this house Claythorn since before I was born, and in time I simply let it stick.

    It is thin. But said with enough boredom, thin will hold.

    I close the book and set it back exactly as I found it.
    """

    return


# ------------------------------------
#   PORTRAIT GALLERY (the missing face)
# ------------------------------------
label host_day1_evening_portrait_gallery:

    $ change_room('portrait_gallery')

    if host_details.threads.is_unlocked('no_portrait'):

        """
        The Claythorns are still there, and I am still not.

        Nothing about that has improved in the last hour.
        """

        return

    """
    A dozen Claythorns in gilt frames, looking down the gallery at me with no expression I would call welcoming.

    Powdered wigs. Stiff collars. A rather fine hunting scene with a heavy-jawed gentleman in the middle of it.

    I look for something of myself in any of those faces, out of habit more than hope, and of course there is nothing.

    I walk the whole length of it twice.

    Then I understand what is wrong with this room.

    There is no portrait of the mistress of the house.

    Every one of these people had themselves painted, and the only one missing is the woman who owns the place.

    All it takes is one guest standing where I am standing, asking which one is you, Lady Claythorn.

    And I have nothing.
    """

    $ host_details.threads.unlock('no_portrait')

    """
    No. I shall have something.

    A portrait was begun in the spring and the man made me look like my own mother, so I sent it back and have not had the heart to sit again.

    That is the sort of thing a woman says about a portrait. Vain, dull, and impossible to check.

    I say it twice under my breath in the empty gallery until it sounds like something I have said before.

    But the butler ought to have thought of this before I did. I shall be having a word with him about it.
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
    The attic stair, and the door at the top of it locked.

    I try it twice, which is once more than there was any point in trying it.

    Every room in this house is mine, and I do not have the key to that one.

    Only he does.

    I stand on the stair a moment longer than I need to, and then I go back down.
    """

    $ host_details.saved_variables['day1_evening_attic_tried'] = True

    return
