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
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'captain_day1_evening_bedroom_closed', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 'captain_day1_evening_bedroom_psychic', 10, room='bedroom_psychic'),
            # First floor
            TimedMenuChoice(default_room_text('tea_room'), 'captain_day1_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'captain_day1_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'captain_day1_evening_garden', 30, room='manor_garden'),
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

    """
    The service area is downstairs. I have no reason to venture there.

    A proper gentleman does not intrude upon the domestic quarters.

    If I were seen poking around the kitchen on the first evening, it would invite exactly the sort of suspicion I am trying to avoid.
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
    I look through the window. The rain is coming down hard now.

    A storm is gathering. I can hear the wind picking up against the glass.

    Most people would turn back at this point.

    But I have marched through monsoons. A bit of rain is hardly cause for concern.
    """

    $ change_room('manor_garden')

    """
    I step outside.

    The air is cold and the rain is heavier than it looked from indoors.

    Within moments, my jacket is soaked through.

    I walk a short distance around the house.

    Nothing remarkable in the dark.

    A garden, a gravel path, what appears to be an outbuilding further on.

    But I am soaking wet and the cold is beginning to bite.

    In these conditions, there is no point in staying any longer.
    """

    $ change_room('bedroom_captain')

    """
    I return inside and head straight to my room to change.

    A foolish exercise, perhaps, but at least I have a better understanding of the estate.
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

    There are perhaps a dozen portraits here, spanning several generations.

    Stern-looking gentlemen in powdered wigs. Ladies in elaborate gowns.

    But then something strikes me.

    None of them resemble our host.

    Where is Lady Claythorn?

    If she is the current mistress of this house, her portrait ought to hang here alongside her forebears.

    And yet there is nothing.

    In itself, that doesn't mean much.

    It could be a personal preference, or perhaps she had difficulty persuading a decent artist to come all the way out here.

    Still, I will keep that in mind.
    """

    $ captain_details.threads.unlock('captain_host_suspicion_portrait')

    return


label captain_day1_evening_library:

    $ change_room('library')

    """
    A well-stocked library. The kind one would expect in a house like this.

    A book lies open on a table.

    'A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.'

    The eighth edition, printed in 1894.

    I remember dreaming of seeing my name in such a book.

    I know now that it will never happen.
    """

    call run_menu(
        TimedMenu("captain_day1_evening_library_menu", [
            TimedMenuChoice('Look up the Claythorns in the index', 'captain_day1_evening_library_read', early_exit=True),
            TimedMenuChoice('Leave the book be', 'generic_cancel', early_exit=True)
        ])
    )

    return


label captain_day1_evening_library_read:

    """
    I glance through a few pages.

    Let us see if the Claythorns are mentioned.

    I search through the index. Clarendon, Claridge, Clark...

    Claythorn.

    There are several entries. I find the one concerning this manor.
    """

    book """
    Nicholas Claythorn, of Claythorn Manor, 3rd Earl of Kilbraith, .

    Born on June 22, 1813.

    His parents were Nicholas Claythorn, 2nd Earl of Kilbraith, and Agnes Cicely.

    With Mary Kirwan, his wife, he fathered one son and one daughter:

    1. Elisabeth, his heir, born in 1865.

    2. Andrew, born in 1867, died in 1869.

    Lineage...
    """

    """
    I read the entry twice.

    There it is. The family name is Claythorn, but their title is not.

    They hold a peerage — the Earldom of Kilbraith. Their seat is this manor, but the title is quite separate.

    A peer is addressed by his title, not by his surname. The Earl of Kilbraith is styled 'Lord Kilbraith', and his countess, 'Lady Kilbraith'.

    Never 'Lord Claythorn'. Never 'Lady Claythorn'.

    Still, I should not leap to conclusions.

    It is not unheard of for a family to set the formal title aside in daily use. Since the war, I have heard of peers who have grown weary of ceremony.

    Or perhaps it is a local habit. The villagers call her 'Lady Claythorn' after the name of the house, and in time she has simply let it stick.

    And yet, it is something strange enough that I should not dismiss it entirely.
    """

    $ captain_details.threads.unlock('captain_host_suspicion_name')

    """
    I close the book and place it back on the table.

    Interesting. Very interesting indeed.
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

    """
    The servants' quarters are upstairs. I have no business going there.

    A guest does not wander into the staff's private rooms. It would be a serious breach of propriety.

    Whatever is up there is none of my concern.
    """

    return


# ------------------------------------
#   BEDROOMS
# ------------------------------------
label captain_day1_evening_bedroom_closed:

    $ captain_details.saved_variables["day1_evening_bedroom_refusals"] += 1

    if captain_details.saved_variables["day1_evening_bedroom_refusals"] == 1:

        $ change_room("bedrooms_hallway")
        
        """
        I pause outside the door.

        No. It would be improper to enter someone's room uninvited.

        That is not how a gentleman conducts himself.
        """

    elif captain_details.saved_variables["day1_evening_bedroom_refusals"] == 2:

        """
        I consider it for a moment, then think better of it.

        A man does not go rummaging through another person's private quarters. Not on the first evening.

        I should keep the bedrooms out of my mind entirely.
        """

        # Block all other bedrooms after 2 refusals
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_lad'))
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_host'))
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_broken'))
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_nurse'))
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_doctor'))
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_drunk'))
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_psychic'))

    return


label captain_day1_evening_bedroom_psychic:

    $ captain_details.saved_variables["day1_evening_bedroom_refusals"] += 1

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

    if captain_details.saved_variables["day1_evening_bedroom_refusals"] >= 2:
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_lad'))
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_host'))
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_broken'))
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_nurse'))
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_doctor'))
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_drunk'))
        $ all_menus[captain_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_psychic'))

    return
