label nurse_day2_evening_map_menu:
    python:
        # -------------------------
        # Saturday Evening
        # -------------------------
        nurse_day2_evening_map_menu = TimedMenu("nurse_day2_evening_map_menu", [
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'nurse_day2_evening_downstairs_maid', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'nurse_day2_evening_downstairs_maid', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'nurse_day2_evening_garage', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'nurse_day2_evening_gun_room', 0, room='gun_room', condition="not nurse_details.threads.is_unlocked('take_gun')"),
            # first floor
            TimedMenuChoice(default_room_text('billiard_room'), 'nurse_day2_evening_billiard_room', 10, room='billiard_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'nurse_day2_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'nurse_day2_evening_garden', 30, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'nurse_day2_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('library'), 'nurse_day2_evening_library', 0, room='library'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'nurse_day2_evening_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('tea_room'), 'nurse_day2_evening_tea_room', 10,  room='tea_room'),
            # Bedrooms 
            TimedMenuChoice(default_room_text('bedroom_lad'), 'nurse_day2_evening_bedroom_lad', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'nurse_day2_evening_bedroom_doctor', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'nurse_day2_evening_bedroom_captain', 0, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'nurse_day2_evening_bedroom_host', 0, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'nurse_day2_evening_bedroom_drunk', 20, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 
                'nurse_day2_evening_bedroom_psychic', 
                10, 
                room='bedroom_psychic'
            ),
            # attic
            TimedMenuChoice(default_room_text('storage'), 'nurse_day2_evening_attic_storage', 0, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'nurse_day2_evening_attic_males_room', 20, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'nurse_day2_evening_attic_females_room', 20, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'nurse_day2_evening_attic_butler_room', 0, room='butler_room'),

            TimedMenuChoice(
                'Go to sleep', 
                'nurse_day2_evening_rest_before_dinner', 
                0, 
                early_exit = True, 
                room = 'bedroom_nurse'
            ),
            TimedMenuChoice(
                'Richard III Bedroom', 
                'nurse_day2_evening_bedroom_broken', 
                20, 
                room = 'bedroom_broken',
            )
        ], 
        is_map = True)

    return


label nurse_day2_evening_downstairs_maid:

    $ all_menus[nurse_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('scullery'))
    $ all_menus[nurse_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))

    $ change_room("kitchen")

    """
    I ease the door open just enough to look inside.

    The kitchen is a hive of activity.

    The staff are busy cleaning after the evening meal.

    I withdraw before anyone notices my presence.
    """

    call nurse_day2_evening_check_exhaustion

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

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_dining_room:

    $ change_room('dining_room')

    """
    The dining room has been cleared.

    Only the large table remains, bare and polished under the cold light.

    There is nothing to keep me here.
    """

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_garden:

    $ change_room('entrance_hall')

    """
    I step towards the door.

    It is dark outside, and the wind has risen again.

    There is nothing to be gained by wandering out there in the cold.

    I turn and go back in.
    """

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_entrance_hall:

    $ change_room('entrance_hall')

    """
    The great hall is very quiet.

    The place where Doctor Baldwin was carried in is no different from any other part of the floor.

    And yet I cannot quite look at it without thinking of him.

    I move on.
    """

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_portrait_gallery:

    $ change_room('portrait_gallery')

    """
    The gallery is lit only by a single lamp at the far end.

    The portraits watch me in silence.
    """

    call nurse_day2_evening_check_exhaustion

    return

# Billiard Room — see 2_billiard_room.rpy


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

    $ change_room("bedrooms_hallway")

    play sound door_knock

    """
    I approach Mr Harring's room and knock gently.

    There is no reply, but I can hear the sound of heavy furniture being dragged across the floorboards.

    It seems he is barricading himself inside.

    Under the circumstances, I suppose I cannot blame him.
    """


    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_default_room_no_enter:
    
    """
    It is best I do not go in there for now.
    """

    return

label nurse_day2_evening_bedroom_captain:

    call nurse_bedroom_default

    """
    Captain Sinha is nowhere to be seen, though I suspect he is not far away.
    """

    if nurse_details.saved_variables.get("visited_bedroom_captain"):

        """
        This corridor remains quite deserted as well.
        """

        call run_menu(
            TimedMenu(
                id="nurse_day2_evening_bedroom_captain_again",
                choices=[
                    TimedMenuChoice("I should take another look just to be certain I missed nothing.", 'nurse_day2_evening_enter_captain_again', 10, early_exit=True),
                    TimedMenuChoice("No, I have already searched here.", 'nurse_day2_evening_default_room_no_enter', 10, early_exit=True),
                ]
            )
        )

    else:

        """
        With most of the household downstairs or retired, one could easily slip inside unseen.

        Though it would be rather difficult to explain if I were caught.
        """

        call run_menu(
            TimedMenu(
                id="nurse_day2_evening_bedroom_captain",
                choices=[
                    TimedMenuChoice("We leave tomorrow. This might be my last chance to search the room.", 'nurse_day2_evening_enter_captain', 10, early_exit=True),
                    TimedMenuChoice("No, if I am caught, I could lose everything before we leave.", 'nurse_day2_evening_default_room_no_enter', 10, early_exit=True),
                ]
            )
        )

    call nurse_day2_evening_check_exhaustion

    return

label nurse_day2_evening_enter_captain:
    call nurse_bedroom_lockpick_choice('nurse_search_captain_default')
    return

label nurse_day2_evening_enter_captain_again:
    call nurse_bedroom_lockpick_choice('nurse_search_captain_again')
    return

label nurse_day2_evening_bedroom_host:

    call nurse_bedroom_default

    """
    It is highly unusual for Lady Claythorn to be absent from her room at this hour.
    """

    if nurse_details.saved_variables.get("visited_bedroom_host"):

        """
        This corridor remains quite deserted as well.
        """

        call run_menu(
            TimedMenu(
                id="nurse_day2_evening_bedroom_host_again",
                choices=[
                    TimedMenuChoice("Perhaps I missed a hidden drawer earlier.", 'nurse_day2_evening_enter_host_again', 10, early_exit=True),
                    TimedMenuChoice("I have already seen what I need to see.", 'nurse_day2_evening_default_room_no_enter', 10, early_exit=True),
                ]
            )
        )

    else:

        """
        With most of the household downstairs or retired, one could easily slip inside unseen.

        Though it would be rather difficult to explain if I were caught.
        """

        call run_menu(
            TimedMenu(
                id="nurse_day2_evening_bedroom_host",
                choices=[
                    TimedMenuChoice("We leave tomorrow. This might be my last chance to search the room.", 'nurse_day2_evening_enter_host', 10, early_exit=True),
                    TimedMenuChoice("No, if I am caught, I could lose everything before we leave.", 'nurse_day2_evening_default_room_no_enter', 10, early_exit=True),
                ]
            )
        )

    call nurse_day2_evening_check_exhaustion

    return

label nurse_day2_evening_enter_host:
    call nurse_bedroom_lockpick_choice('nurse_search_host_default')
    return

label nurse_day2_evening_enter_host_again:
    call nurse_bedroom_lockpick_choice('nurse_search_host_again')
    return


label nurse_day2_evening_bedroom_doctor:

    $ change_room("bedroom_doctor")

    """
    The door to Doctor Baldwin's room stands open.

    I step inside, and the stillness of the room is immediate.

    He lies on the bed, just as they left him after the tragedy.

    It feels wrong to be here, in the presence of a colleague who has met such a sudden end.

    There is nothing a nurse can do for him now.

    I shall leave him to his rest.
    """

    $ unlock_map('bedroom_doctor')

    call nurse_day2_evening_check_exhaustion

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
    Oh, Miss Marsh. You are very kind to ask.

    But I am quite exhausted, if I am perfectly honest.

    I really just wish to sleep now.
    """

    nurse """
    Of course.

    I shall not keep you. We shall both feel better in the morning.
    """

    psychic """
    Indeed.

    Good night, Miss Marsh.
    """

    nurse """
    Good night.
    """

    $ unlock_map('bedroom_psychic')

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_bedroom_drunk:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    """
    I stand at Samuel Manning's door. I try the handle, but it is locked from the inside.

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

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_bedroom_broken:

    call nurse_search_broken_default

    call nurse_day2_evening_check_exhaustion

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

    call nurse_day2_evening_check_exhaustion

    return


# Cancel / Sleep
label nurse_day2_evening_rest_before_dinner:

    $ change_room("bedroom_nurse")

    """
    I am quite exhausted.

    The events of the day have taken their toll.

    I shall lie down for a moment before the evening meal is served.
    """

    call wait_screen_transition()

    call change_time(19, 30)

    return


label nurse_day2_evening_cancel:

    """
    I shall wait in my room until I am needed.
    """

    return
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


label nurse_day2_evening_garage:

    call nurse_garage_default

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_gun_room:

    call nurse_gun_room_default

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_library:

    call nurse_library_default

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_attic_storage:

    call nurse_attic_storage

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_attic_males_room:

    call nurse_attic_males_room

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_attic_females_room:

    call nurse_attic_females_room

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_attic_butler_room:

    call nurse_attic_butler_room

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_check_exhaustion:


    if (time_left < 40  and nurse_details.threads.is_unlocked('day1_exhaustion')) and not nurse_details.saved_variables["day2_evening_exhaustion_triggered"]:

        $ nurse_details.saved_variables["day2_evening_exhaustion_triggered"] = True

        play sound woman_cough

        """
        A cough comes to me, a strong one.

        I reach for my handkerchief to cover my mouth.
        """

        play sound woman_cough

        """
        It is followed by a second.

        It should not come as a surprise; I haven't rested as much as I ought to.

        The only sane thing to do now is to go to bed.

        If I don't, God knows what could happen.
        """

    return
