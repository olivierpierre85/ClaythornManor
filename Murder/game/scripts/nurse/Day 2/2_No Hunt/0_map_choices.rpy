label nurse_day2_no_hunt_map_menu:
    python:
        # -------------------------
        # Saturday, During the Hunt
        # -------------------------        
        nurse_day2_no_hunt_map_menu = TimedMenu("nurse_day2_no_hunt_map_menu", [
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'nurse_day2_no_hunt_downstairs_maid', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'nurse_day2_no_hunt_downstairs_maid', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'nurse_garage_default', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'nurse_gun_room_default', 0, room='gun_room', condition="not nurse_details.threads.is_unlocked('take_gun')"),
            # first floor
            TimedMenuChoice(default_room_text('billiard_room'), 'nurse_billiard_room_default', 10, room='billiard_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'nurse_day2_no_hunt_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'nurse_day2_no_hunt_garden', 30, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'nurse_entrance_hall_default', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('library'), 'nurse_library_default', 0, room='library'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'nurse_portrait_gallery_default', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('tea_room'), 'nurse_tea_room_default', 10,  room='tea_room', condition= "not " + condition_saturday_hunt_morning),
            TimedMenuChoice("Wait for luncheon in the Tea Room", 'nurse_day2_hunt_tea_room_early', 0, early_exit = True,  room='tea_room', condition=condition_saturday_hunt_morning),
            # Bedrooms 
            TimedMenuChoice(default_room_text('bedroom_lad'), 'nurse_day2_no_hunt_bedroom_lad', 0, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'nurse_day2_no_hunt_bedroom_doctor', 0, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'nurse_day2_no_hunt_bedroom_captain', 0, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'nurse_day2_no_hunt_bedroom_host', 0, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'nurse_day2_no_hunt_bedroom_drunk', 20, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 
                'nurse_day2_no_hunt_bedroom_psychic', 
                0, 
                room='bedroom_psychic',
                condition = condition_saturday_hunt_morning,
            ),
            # attic
            TimedMenuChoice(default_room_text('storage'), 'nurse_day2_no_hunt_attic_storage', 0, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'nurse_day2_no_hunt_attic_males_room', 20, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'nurse_day2_no_hunt_attic_females_room', 20, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'nurse_day2_no_hunt_attic_butler_room', 20, room='butler_room'),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 
                'nurse_day2_no_hunt_bedroom_psychic_busy', 
                10, 
                room='bedroom_psychic',
                condition = "not " + condition_saturday_hunt_morning,
            ),
            TimedMenuChoice(
                'Take a rest before lunch', 
                'nurse_day2_no_hunt_rest_before_lunch', 
                0, 
                early_exit = True, 
                room = 'bedroom_nurse',
                condition = condition_saturday_hunt_morning
            ),
            TimedMenuChoice(
                'Wait until the others return', 
                'nurse_day2_no_hunt_cancel', 
                90, 
                early_exit = True, 
                room = 'bedroom_nurse',
                condition = "not " + condition_saturday_hunt_morning
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'nurse_day2_bedroom_broken', 
                20, 
                room = 'bedroom_broken',
            )
        ], 
        is_map = True)
    
    return


label nurse_day2_no_hunt_rest_before_lunch:

    $ change_room("bedroom_nurse")

    """
    I am exhausted.

    A quick nap before luncheon is what I need.
    """

    call wait_screen_transition()

    call change_time(11, 45)

    return


label nurse_day2_hunt_tea_room_early:

    $ change_room("tea_room")

    """
    I do not really have the strength to explore.

    I should just wait for luncheon here.
    """

    $ nurse_details.saved_variables['day2_hunt_tea_room_early'] = True

    return

# Downstairs
label nurse_day2_no_hunt_downstairs_maid:

    # Hide both kitchen and scullery — they share the same discovery
    $ all_menus[nurse_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))
    $ all_menus[nurse_details.saved_variables["day2_no_hunt_map_menu"].id].hide_specific_choice(default_room_text('scullery'))

    $ change_room("basement_stairs")

    call nurse_downstairs_approach

    $ change_room("kitchen")

    """
    I almost step inside until I notice one of the maids, alone.
    
    It is better if she does not see me.

    I pull the door to and leave.
    """

    return


# First Floor
label nurse_day2_no_hunt_dining_room:

    $ change_room('dining_room')

    """
    The dining room is empty.

    The table is not entirely cleared.

    Strange, that should have been done by now.

    Looks like the manor is understaffed.
    """

    return

label nurse_day2_no_hunt_garden:

    $ change_room('manor_garden')

    """
    The sky is a little brighter this morning. Not much, but enough.

    The paths are damp underfoot, and there is a chill still in the air, but it is pleasant to be outside.

    I walk the length of the garden slowly, not pushing myself.

    The house is quiet behind me. It is a relief, for a moment, to be away from it.

    I do not stay long. One circuit, and then back inside.
    """

    return


# Bedroom
label nurse_day2_no_hunt_bedroom_try_enter(menu_id, enter_result, enter_duration=5, do_not_enter_duration=10):

    python:
        enter_text_list = [
            "This is my chance. I should search the room before anyone returns.",
            "I must be quick. There may be something worth taking in there.",
            "I cannot afford to hesitate. I go in."
        ]

        no_enter_text_list = [
            "Not now. The timing is not right.",
            "Too risky. If someone were to come along, I could not explain myself.",
            "I step back. I will find another opportunity."
        ]
    
        # Ensure we don't go out of bounds if the player tries many times
        try_index = min(nurse_details.saved_variables.setdefault('day2_nohunt_bedroom_tries', 0), len(enter_text_list) - 1)
        enter_text = enter_text_list[try_index]
        no_enter_text = no_enter_text_list[try_index]
        
    if nurse_details.saved_variables.get('day2_nohunt_bedroom_tries', 0) == 0:

        """
        With most of the household out hunting, one could easily slip inside unseen.

        Though it would be rather difficult to explain if I were caught.
        """

    else:

        """
        This corridor remains quite deserted as well.
        """

    $ nurse_details.saved_variables['day2_nohunt_bedroom_tries'] = nurse_details.saved_variables.get('day2_nohunt_bedroom_tries', 0) + 1

    call run_menu(
        TimedMenu(
            id=menu_id, 
            choices=[
                TimedMenuChoice(enter_text, enter_result, enter_duration, early_exit=True),
                TimedMenuChoice(no_enter_text, 'nurse_day2_no_hunt_default_room_no_enter', do_not_enter_duration, early_exit=True),
            ]
        )
    )

    return

label nurse_day2_no_hunt_default_room_no_enter:
    
    """
    It is best I do not go in there for now.
    """

    return


label nurse_day2_no_hunt_default_room_locked:
    
    """
    I try the handle gently.

    It is securely locked.
    """

    return

label nurse_day2_no_hunt_enter_psychic:
    call nurse_bedroom_lockpick_choice('nurse_search_psychic_default')
    return

label nurse_day2_no_hunt_enter_lad:
    call nurse_bedroom_lockpick_choice('nurse_search_lad_default')
    return

label nurse_day2_no_hunt_enter_doctor:
    call nurse_bedroom_lockpick_choice('nurse_search_doctor_default')
    return

label nurse_day2_no_hunt_enter_captain:
    call nurse_bedroom_lockpick_choice('nurse_search_captain_default')
    return

label nurse_day2_no_hunt_enter_host:
    call nurse_bedroom_lockpick_choice('nurse_search_host_default')
    return


# Psychic
label nurse_day2_no_hunt_bedroom_psychic:

    call nurse_bedroom_default

    """
    Amelia Baxter is not there. This could be my best opportunity to have a look inside her room.

    But she is nearby. It will not look well if she returns and finds me here.

    It is a considerable risk.
    """

    call nurse_day2_no_hunt_bedroom_try_enter('nurse_day2_no_hunt_bedroom_psychic', 'nurse_day2_no_hunt_enter_psychic')

    return

# Lad
label nurse_day2_no_hunt_bedroom_lad:

    call nurse_bedroom_default

    call nurse_day2_no_hunt_bedroom_try_enter('nurse_day2_no_hunt_bedroom_lad', 'nurse_day2_no_hunt_enter_lad')

    return


# Doctor
label nurse_day2_no_hunt_bedroom_doctor:

    call nurse_bedroom_default

    call nurse_day2_no_hunt_bedroom_try_enter('nurse_day2_no_hunt_bedroom_doctor', 'nurse_day2_no_hunt_enter_doctor')

    return


# Captain
label nurse_day2_no_hunt_bedroom_captain:

    call nurse_bedroom_default

    call nurse_day2_no_hunt_bedroom_try_enter('nurse_day2_no_hunt_bedroom_captain', 'nurse_day2_no_hunt_enter_captain')

    return


# Host
label nurse_day2_no_hunt_bedroom_host:

    call nurse_bedroom_default

    call nurse_day2_no_hunt_bedroom_try_enter('nurse_day2_no_hunt_bedroom_host', 'nurse_day2_no_hunt_enter_host')

    return


# Drunk
label nurse_day2_no_hunt_bedroom_drunk:

    call nurse_bedroom_default

    """
    The door shifts slightly under my touch.

    It appears Mr Manning has left it resting on the latch.

    Since he is not coming back yet, I could take a quick look.

    I push the door open quietly, ensuring no one is watching.
    """

    play sound door_open

    $ change_room('bedroom_drunk')

    """
    The room is in a frightful state.

    Clothes are discarded carelessly, and the unmistakable smell of spirits hangs in the air.
    """

    $ unlock_map('bedroom_drunk')

    """
    A brief glance reveals only empty whisky bottles.

    Quite as I suspected. There is nothing of value for me here.
    """

    return

# Attic
label nurse_day2_no_hunt_attic_approach:

    
    $ change_room("attic_hallway")

    if not nurse_details.saved_variables.get("day2_no_hunt_attic_visited", False):

        $ nurse_details.saved_variables["day2_no_hunt_attic_visited"] = True

        """
        The attic staircase creaks with every step.

        Up here, the air is close and smells of dust and old timber.

        The corridor runs the length of the house, doors on either side.

        With the servants all occupied below, there is no one to question what I am doing up here.
        """

    """
    The door is locked.
    """

    if not nurse_details.saved_variables["lockpick_seen"]:

        $ nurse_details.saved_variables["lockpick_seen"] = True

        """
        It would take very little effort to open it.

        In my years of nursing, one becomes acquainted with all manner of locks — on medicine cabinets, ward doors, supply rooms.

        This is nothing remarkable.
        """

    else:

        """
        But I easily make my way inside.
        """

    return


label nurse_day2_no_hunt_attic_females_room:

    call nurse_day2_no_hunt_attic_approach

    $ change_room("females_room")

    """
    It is a small, spare space — two narrow beds, a washstand, a single trunk between them.

    On the shelf above one of the beds, a small collection of things: a dog-eared playbill from a London theatre, another from a touring company. A faded photograph is tucked behind them.
    """

    """
    I take the photograph down.

    A young woman in stage dress, posed with a man I do not recognise.

    She is smiling broadly.

    I would not have expected it of any of the maids here. One of them has a past she has not spoken of.
    """

    """
    I replace everything as it was and step back out.
    """

    return


label nurse_day2_no_hunt_attic_butler_room:

    call nurse_day2_no_hunt_attic_approach

    $ change_room("butler_room")

    """
    The adjoining pantry door stands ajar.
    """

    play sound door_open

    """
    Inside: a polished cabinet of household silver, a rack of decanted wine, a locked case that can only hold valuables of some kind.

    This is the nerve centre of the house's wealth.

    Whatever the butler knows — or suspects — he keeps it well-guarded.

    There is too much here to search quickly, and I dare not disturb anything.

    I make a note of it and withdraw.
    """

    return


label nurse_day2_no_hunt_attic_males_room:

    call nurse_day2_no_hunt_attic_approach

    $ change_room("males_room")

    """
    Two beds, a chest of drawers, a peg for each man's jacket.

    I check the drawers quickly — folded shirts, a penknife, a few coins.
    """

    """
    Tucked at the very back of the bottom drawer, I find it.

    A passport. Belgian.

    I open it carefully.

    The photograph inside shows a man I do not recognise, though the name on the document is that of one of the footmen.

    It may mean nothing. Or it may mean rather a great deal.

    I close it and replace it exactly as I found it.
    """

    return


label nurse_day2_no_hunt_attic_storage:

    call nurse_day2_no_hunt_attic_approach

    $ change_room("storage")

    """
    The storage room is vast.

    Trunks stacked three deep, old furniture draped in dust sheets, boxes of every shape and size.

    I barely know where to begin.
    """

    call run_menu(
        TimedMenu(
            id='nurse_day2_no_hunt_attic_storage_search',
            choices=[
                TimedMenuChoice('Search the trunks along the far wall', 'nurse_day2_no_hunt_attic_storage_trunks', 30),
                TimedMenuChoice('Look through the old furniture', 'nurse_day2_no_hunt_attic_storage_furniture', 30),
                TimedMenuChoice('Check the shelves near the door', 'nurse_day2_no_hunt_attic_storage_shelves', 30),
                TimedMenuChoice('Give up. This will take all day.', 'nurse_day2_no_hunt_attic_storage_give_up', 10, early_exit=True),
            ]
        )
    )

    return


label nurse_day2_no_hunt_attic_storage_trunks:

    """
    The trunks are packed tightly and most of them are locked.

    I manage to open one — old curtains, heavy and mildewed.

    Another: crockery wrapped in cloth.

    I move on.
    """

    return


label nurse_day2_no_hunt_attic_storage_furniture:

    """
    I lift a dust sheet from what turns out to be an old escritoire.

    The drawers are empty save for a few dried-up pen nibs and a folded invoice from eighteen ninety.

    Nothing useful.
    """

    return


label nurse_day2_no_hunt_attic_storage_shelves:

    """
    The shelves near the door hold rows of old tins and jars, most unlabelled.

    I move some aside — and then I stop.

    Behind a row of old paint tins, stacked neatly and deliberately out of sight:
    """

    """
    Bullets.

    A good number of them. Military calibre, by the look of it.

    Someone has gone to some trouble to hide these.

    I stand very still for a moment.

    Then I replace the tins exactly as they were, and leave the room as quietly as I came.
    """

    return


label nurse_day2_no_hunt_attic_storage_give_up:

    """
    I have been in here long enough.

    There is too much to search properly, and I am beginning to feel uneasy.

    I leave without having found anything of note.
    """

    return
