# Map choices for Captain, Friday evening
label captain_day1_evening_map_menu:
    python:
        captain_day1_evening_map_menu = TimedMenu(
            "captain_day1_evening_map_menu",
            [
            # Attic
            TimedMenuChoice(default_room_text('storage'), 'captain_day1_evening_attic_default', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'captain_day1_evening_attic_default', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'captain_day1_evening_attic_default', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'captain_day1_evening_attic_default', 10, room='butler_room'),
            # Bedrooms
            TimedMenuChoice(default_room_text('bedroom_lad'), 'captain_day1_evening_bedroom_closed', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'captain_day1_evening_bedroom_closed', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_broken'), 'captain_day1_evening_bedroom_closed', 10, room='bedroom_broken'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'captain_day1_evening_bedroom_closed', 10, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'captain_day1_evening_bedroom_closed', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'captain_day1_evening_bedroom_drunk', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 'captain_day1_evening_bedroom_psychic', 10, room='bedroom_psychic'),
            # First floor
            TimedMenuChoice(default_room_text('tea_room'), 'captain_day1_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'captain_day1_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'captain_day1_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'captain_day1_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'captain_day1_evening_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('library'), 'captain_day1_evening_library', 10, room='library'),
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'captain_day1_evening_downstairs_default', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'captain_day1_evening_downstairs_default', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'captain_day1_evening_downstairs_default', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'captain_day1_evening_downstairs_default', 10, room='gun_room'),
            # Specific actions
            TimedMenuChoice(
                'Meet the others in the billiard room',
                'captain_day1_evening_billiard_room',
                0,
                room = 'billiard_room',
                next_menu = 'captain_day1_evening_billiard_room_menu'
            ),
            TimedMenuChoice(
                'Retire for the night',
                'generic_cancel',
                early_exit = True,
                room = 'bedroom_captain'
            )
        ], is_map = True)

    return


# ------------------------------------
#   DOWNSTAIRS
# ------------------------------------
label captain_day1_evening_downstairs_default:

    $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('gun_room'))
    $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('garage'))
    $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('scullery'))
    $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))

    $ change_room("basement_stairs")

    """
    I head down the stairs to the service area.

    A footman steps forward before I reach the bottom.
    """

    footman """
    Good evening, sir. I'm afraid guests aren't permitted beyond this point.
    """

    captain """
    Of course. My apologies.
    """

    """
    Rules are rules. I of all people understand that.

    I turn back without argument.
    """

    return


# ------------------------------------
#   FIRST FLOOR
# ------------------------------------
label captain_day1_evening_tea_room:

    $ change_room('tea_room')

    """
    The tea room is deserted now. Nothing of interest here.
    """

    return


label captain_day1_evening_dining_room:

    $ change_room('dining_room')

    """
    The staff are clearing away the last of the dinner service.

    No reason to linger.
    """

    return


label captain_day1_evening_garden:

    $ change_room('entrance_hall')

    """
    I consider stepping outside, but the weather has worsened considerably.

    A storm is gathering. I can hear the wind picking up against the windows.

    Not a night for a stroll.
    """

    return


label captain_day1_evening_entrance_hall:

    $ change_room('entrance_hall')

    """
    The entrance hall is quiet at this hour.

    It is a fine space. The kind of hall that speaks of generations.

    I take a moment to study the architecture, then move on.
    """

    return


label captain_day1_evening_portrait_gallery:

    $ change_room('portrait_gallery')

    """
    A gallery of family portraits lines the walls.

    The Claythorn lineage, rendered in oil and gilt frames.

    I study the faces. Old money, passed down through blood.

    I wonder what my mother would have thought of this place.

    She would have wanted me to belong here.
    """

    return


label captain_day1_evening_library:

    $ change_room('library')

    """
    A well-stocked library. The kind one would expect in a house like this.

    A book lies open on the desk.

    'A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.'

    I glance through a few pages, but my name would never appear in such a volume.

    I close it and move on.
    """

    return


# ------------------------------------
#   ATTIC
# ------------------------------------
label captain_day1_evening_attic_default:

    $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('butler_room'))

    $ change_room("attic_hallway")

    """
    The servants' quarters. Narrow stairs, plain walls.

    I know this part of a house well enough. It is where people like the staff live.

    And, in some ways, it is where people like me were expected to stay.

    There is nothing for me up here. I go back down.
    """

    return


# ------------------------------------
#   BEDROOMS
# ------------------------------------
label captain_day1_evening_bedroom_closed:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    captain """
    Hello?
    """

    """
    No answer.

    It would be improper to enter someone's room uninvited.

    That is not how a gentleman conducts himself.
    """

    return


label captain_day1_evening_bedroom_drunk:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    captain """
    Mr Manning?
    """

    play sound door_open

    """
    The door swings open at my knock. It was not even latched.

    The smell is appalling.

    I close the door and walk away.

    Whatever is in there is not my concern.
    """

    return


label captain_day1_evening_bedroom_psychic:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    captain """
    Miss Baxter? Are you there?
    """

    psychic """
    Yes? Who is it?
    """

    captain """
    Captain Sinha. I was wondering if you might care for a conversation.
    """

    psychic """
    That is kind of you, Captain. But I am rather tired.

    We can speak again tomorrow.
    """

    captain """
    Of course. Good night.
    """

    $ unlock_map('bedroom_psychic')

    return
