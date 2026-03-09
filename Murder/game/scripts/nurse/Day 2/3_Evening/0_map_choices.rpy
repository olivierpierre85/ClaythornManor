label nurse_day2_evening_map_menu:
    python:
        # -------------------------
        # Saturday Evening
        # -------------------------
        nurse_day2_evening_map_menu = TimedMenu("nurse_day2_evening_map_menu", [
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'nurse_day2_evening_downstairs_maid', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'nurse_day2_evening_downstairs_maid', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'nurse_garage_default', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'nurse_gun_room_default', 0, room='gun_room', condition="not nurse_details.threads.is_unlocked('take_gun')"),
            # first floor
            TimedMenuChoice(default_room_text('billiard_room'), 'nurse_billiard_room_default', 10, room='billiard_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'nurse_day2_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'nurse_day2_evening_garden', 30, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'nurse_entrance_hall_default', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('library'), 'nurse_library_default', 0, room='library'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'nurse_portrait_gallery_default', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('tea_room'), 'nurse_tea_room_default', 10,  room='tea_room', condition= "not " + condition_saturday_hunt_morning),
            TimedMenuChoice("Wait for luncheon in the Tea Room", 'nurse_day2_hunt_tea_room_early', 0, early_exit = True,  room='tea_room', condition=condition_saturday_hunt_morning),
            # Bedrooms 
            TimedMenuChoice(default_room_text('bedroom_lad'), 'nurse_day2_evening_bedroom_lad', 0, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'nurse_day2_evening_bedroom_doctor', 0, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'nurse_day2_evening_bedroom_captain', 0, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'nurse_day2_evening_bedroom_host', 0, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'nurse_day2_evening_bedroom_drunk', 20, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 
                'nurse_day2_evening_bedroom_psychic_busy', 
                0, 
                room='bedroom_psychic',
                condition = condition_saturday_hunt_morning,
            ),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 
                'nurse_day2_evening_bedroom_psychic_risk', 
                10, 
                room='bedroom_psychic',
                condition = "not " + condition_saturday_hunt_morning,
            ),
            # attic
            TimedMenuChoice(default_room_text('storage'), 'nurse_attic_storage', 0, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'nurse_attic_males_room', 20, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'nurse_attic_females_room', 20, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'nurse_attic_butler_room', 0, room='butler_room'),

            TimedMenuChoice(
                'Take a rest before lunch', 
                'nurse_day2_evening_rest_before_lunch', 
                0, 
                early_exit = True, 
                room = 'bedroom_nurse',
                condition = condition_saturday_hunt_morning
            ),
            TimedMenuChoice(
                'Wait until the others return', 
                'nurse_day2_evening_cancel', 
                90, 
                early_exit = True, 
                room = 'bedroom_nurse',
                condition = "not " + condition_saturday_hunt_morning
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'nurse_search_broken_default', 
                20, 
                room = 'bedroom_broken',
            )
        ], 
        is_map = True)

    return


label nurse_day2_evening_downstairs_default:

    $ all_menus[nurse_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('gun_room'))
    $ all_menus[nurse_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('garage'))
    $ all_menus[nurse_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('scullery'))
    $ all_menus[nurse_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))

    $ change_room("basement_stairs")

    """
    I approach the back stairs.

    A maid is there, quietly clearing up.

    She gives me a polite but firm look.

    Lady Claythorn's instructions, no doubt.

    I withdraw without making a scene.
    """

    return


# First Floor
label nurse_day2_evening_tea_room:

    $ change_room('tea_room')

    """
    The room is empty.

    The fire has burned low.

    I sit for a moment but find no comfort in it.

    I shall try elsewhere.
    """

    return


label nurse_day2_evening_dining_room:

    $ change_room('dining_room')

    """
    The dining room has been cleared.

    Only the large table remains, bare and polished under the cold light.

    There is nothing to keep me here.
    """

    return


label nurse_day2_evening_garden:

    $ change_room('entrance_hall')

    """
    I step towards the door.

    It is dark outside, and the wind has risen again.

    There is nothing to be gained by wandering out there in the cold.

    I turn and go back in.
    """

    return


label nurse_day2_evening_entrance_hall:

    $ change_room('entrance_hall')

    """
    The great hall is very quiet.

    The place where Doctor Baldwin was carried in is no different from any other part of the floor.

    And yet I cannot quite look at it without thinking of him.

    I move on.
    """

    return


label nurse_day2_evening_portrait_gallery:

    $ change_room('portrait_gallery')

    """
    The gallery is lit only by a single lamp at the far end.

    The portraits watch me in silence.

    I am in no mood for them tonight.
    """

    return





# Billiard Room
label nurse_day2_evening_billiard_room:

    $ change_room("billiard_room")

    """
    The billiard room.

    I can hear voices inside.

    I push open the door far enough to see.
    """

    # TODO: add meaningful billiard room interactions

    return


label nurse_day2_evening_billiard_room_menu:
    python:
        nurse_day2_evening_billiard_room_menu = TimedMenu("nurse_day2_evening_billiard_room_menu", [
            TimedMenuChoice(
                'Leave the billiard room',
                'generic_cancel',
                0,
                early_exit = True,
                room = 'billiard_room'
            ),
        ])

    return


# Bedrooms
label nurse_day2_evening_bedroom_closed:

    if not nurse_details.saved_variables["day2_evening_bedroom_closed"]:

        $ nurse_details.saved_variables["day2_evening_bedroom_closed"] = True

        """
        I knock quietly.

        There is no answer.

        The house is still on edge after today's events.

        It is no great surprise that people are keeping their doors shut.

        I shall not press the matter.
        """

    else:

        """
        Still no answer.

        I shall not disturb them again.
        """

    return


label nurse_day2_evening_bedroom_lad:

    call nurse_bedroom_default
    call nurse_day2_evening_bedroom_closed

    return


label nurse_day2_evening_bedroom_captain:

    call nurse_bedroom_default
    call nurse_day2_evening_bedroom_closed

    return


label nurse_day2_evening_bedroom_host:

    call nurse_bedroom_default
    call nurse_day2_evening_bedroom_closed

    return


label nurse_day2_evening_bedroom_psychic:

    call nurse_bedroom_default

    psychic """
    Yes? Who is there?
    """

    nurse """
    Miss Marsh.

    I only wished to enquire whether you were quite all right.
    """

    psychic """
    Oh, Miss Marsh. How very kind.

    I am as well as can be expected, under the circumstances.

    It has been a dreadful day.
    """

    nurse """
    It has.

    Try to get some rest. We shall both feel better in the morning.
    """

    psychic """
    Yes.

    Good night, Miss Marsh.
    """

    nurse """
    Good night.
    """

    $ unlock_map('bedroom_psychic')

    return


label nurse_day2_evening_bedroom_drunk:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    """
    I stand at Samuel Manning's door.

    I can hear him moving about on the other side. Restless, or perhaps delirious.
    """

    drunk """
    Hmm... urrh...
    """

    """
    I tap again, gently.

    He is quite beyond rational conversation.

    I step back.

    There is nothing to be done for him tonight.
    """

    $ unlock_map('bedroom_drunk')

    return


label nurse_day2_evening_bedroom_broken:

    $ change_room("bedrooms_hallway")

    """
    I stop outside Thomas Moody's room.

    I have stood outside enough rooms like this over the years to know what a closed door can mean.

    I do not linger.
    """

    return


# Attic
label nurse_day2_evening_attic_default:

    $ all_menus[nurse_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[nurse_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[nurse_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[nurse_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('butler_room'))

    $ change_room("attic_hallway")

    """
    The attic corridor.

    A faint light shows under one of the doors.

    I have no proper reason to be up here at this hour.

    I had better go back down.
    """

    return


# Cancel / Sleep
label nurse_day2_evening_sleep:

    $ change_room("bedroom_nurse", dissolve)

    """
    There is nothing more for me to do tonight.

    I lock my door and sit on the edge of the bed for a moment.

    The events of the day turn over in my mind.

    I am tired.

    I close my eyes and let the darkness come.
    """

    call wait_screen_transition()

    return
