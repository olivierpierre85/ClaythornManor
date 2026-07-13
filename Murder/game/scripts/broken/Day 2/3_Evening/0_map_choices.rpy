# Map choices for Broken (Thomas Moody), Saturday night.
#
# The same board as Friday night, but the game is different: he is not
# snooping, he is raising the house. Calling at every occupied bedroom
# (most won't answer, some hide) AND warning the Captain and Mr Manning
# in the tea room (2_tea_room.rpy) unlocks gather_everyone - without it
# the manor burns while everyone sleeps (see 1_main.rpy).
#
# Occupied doors that count towards the gathering: doctor, psychic, nurse,
# host. The Captain's and Mr Manning's rooms stand empty (they are in the
# tea room, where the Captain reads and Mr Manning drinks). Ted Harring's
# room holds Ted Harring.
#
# No livery mechanics tonight: the door at the foot of the servant stair is
# locked from the other side, and the attic answers nobody. The entrance
# hall pays off the telephone he resolved to try (the line is dead).
#
# The early exit ("Turn in for the night") ends the exploration and leads
# into the night in 1_main.rpy.


label broken_day2_evening_map_menu:
    python:
        broken_day2_evening_map_menu = TimedMenu(
            "broken_day2_evening_map_menu",
            [
            # Attic
            map_choice('storage', 'broken_day2_evening_attic_default'),
            map_choice('males_room', 'broken_day2_evening_attic_default'),
            map_choice('females_room', 'broken_day2_evening_attic_default'),
            map_choice('attic_butler_room', 'broken_day2_evening_attic_default'),
            # Bedrooms (his own room is the retire exit, so it is not listed here)
            map_choice('bedroom_lad', 'broken_day2_evening_bedroom_lad'),
            map_choice('bedroom_host', 'broken_day2_evening_bedroom_host'),
            map_choice('bedroom_nurse', 'broken_day2_evening_bedroom_nurse'),
            map_choice('bedroom_doctor', 'broken_day2_evening_bedroom_doctor'),
            map_choice('bedroom_drunk', 'broken_day2_evening_bedroom_empty'),
            map_choice('bedroom_psychic', 'broken_day2_evening_bedroom_psychic'),
            map_choice('bedroom_captain', 'broken_day2_evening_bedroom_empty'),
            # Ground floor
            map_choice('tea_room', 'broken_day2_evening_tea_room'),
            map_choice('dining_room', 'broken_day2_evening_dining_room'),
            map_choice('entrance_hall', 'broken_day2_evening_entrance_hall'),
            map_choice('manor_garden', 'broken_day2_evening_garden'),
            map_choice('servant_stairs', 'broken_day2_evening_servant_stairs'),
            map_choice('portrait_gallery', 'broken_day2_evening_portrait_gallery'),
            map_choice('library', 'broken_day2_evening_library'),
            # Specific actions
            TimedMenuChoice('Look in on the billiard room', 'broken_day2_evening_billiard_room', 10, room='billiard_room'),
            TimedMenuChoice('Turn in for the night', 'generic_cancel', early_exit=True, room='bedroom_broken'),
        ], is_map = True)

    return


# ------------------------------------
#   THE GATHERING
# ------------------------------------
# gather_everyone unlocks once the Captain and Mr Manning have agreed to the
# watch (day2_evening_watch_agreed, set in 2_tea_room.rpy) and every occupied
# bedroom door has been called at.
label broken_day2_evening_check_gathered:

    if broken_details.threads.is_unlocked('gather_everyone'):

        return

    python:
        _all_gathered = (
            broken_details.saved_variables['day2_evening_watch_agreed']
            and broken_details.saved_variables['day2_evening_called_doctor']
            and broken_details.saved_variables['day2_evening_called_psychic']
            and broken_details.saved_variables['day2_evening_called_nurse']
            and broken_details.saved_variables['day2_evening_called_host']
        )

    if _all_gathered:

        $ broken_details.threads.unlock('gather_everyone')

        """
        That is every door I can knock upon.

        The Captain and Mr Manning hold the ground floor, the ladies have barred themselves in, and heaven help the doctor, for he would not wake for the last trumpet.

        Whatever comes for us tonight will not find this house asleep.
        """

    return


# ------------------------------------
#   BEDROOMS
# ------------------------------------
label broken_day2_evening_bedroom_doctor:

    $ change_room('bedrooms_hallway')

    if not broken_details.saved_variables['day2_evening_called_doctor']:

        $ broken_details.saved_variables['day2_evening_called_doctor'] = True

        """
        I knock at Doctor Baldwin's door. Nothing.

        I knock harder, hard enough to wake the corridor.

        From within comes a sound like a man swimming up from deep water, a mumble, the creak of a bed. Then nothing again.

        Whatever the doctor takes of an evening, he has taken it.

        No fire bell would rouse him now. His lock will have to stand guard in his stead.
        """

        call broken_day2_evening_check_gathered

    else:

        """
        The doctor's door, and the doctor's silence behind it.

        There is no more to be done for him tonight.
        """

    return


label broken_day2_evening_bedroom_psychic:

    $ change_room('bedrooms_hallway')

    if not broken_details.saved_variables['day2_evening_called_psychic']:

        $ broken_details.saved_variables['day2_evening_called_psychic'] = True

        """
        I knock at Miss Baxter's door, and give my name.

        Her voice comes through the wood at once, wide awake.
        """

        psychic """
        Mr Moody. What a peculiar hour for a social call.

        You needn't explain yourself, I feel the same disquiet in this house that you do. It hangs in every corridor like smoke.

        I shall not open my door tonight, not to you nor to anybody.

        But rest assured, it will be locked, and the chair set under the handle, and should anyone try it I shall scream this house down to its foundations.
        """

        """
        A scream for an alarm bell.

        From her, I believe it. It will do.
        """

        call broken_day2_evening_check_gathered

    else:

        """
        Miss Baxter's door stays shut, as she promised it would.

        I leave her be.
        """

    return


label broken_day2_evening_bedroom_nurse:

    $ change_room('bedrooms_hallway')

    if not broken_details.saved_variables['day2_evening_called_nurse']:

        $ broken_details.saved_variables['day2_evening_called_nurse'] = True

        """
        I knock at Miss Marsh's door.

        Silence. But it is the wrong kind of silence, the held-breath kind, with a floorboard settling where somebody has just stopped moving.

        She is hiding.

        I put my mouth near the jamb and keep my voice low. My name, and my fear plainly stated, and what I mean to do about it.

        A long moment. Then the bolt slides, and her voice comes through the gap of the door.
        """

        nurse """
        Forgive me, Mr Moody. After this morning I did not know whose knock to trust.

        I shall bar the door and keep the candle burning, and I am a light sleeper.

        If I hear anything at all, the whole house will hear me next.
        """

        """
        Practical and precise. I would expect nothing else of her.
        """

        call broken_day2_evening_check_gathered

    else:

        """
        A thin line of candlelight shows beneath Miss Marsh's door, as she said it would.

        She is keeping her word.
        """

    return


label broken_day2_evening_bedroom_host:

    $ change_room('bedrooms_hallway')

    if not broken_details.saved_variables['day2_evening_called_host']:

        $ broken_details.saved_variables['day2_evening_called_host'] = True

        """
        A line of light shows beneath Lady Claythorn's door, and behind it, small sounds of movement.

        I knock.

        The light goes out mid-knock. The movement stops.

        I knock again, and give my name, and the silence only deepens.

        She is standing in the dark on the other side of that door, waiting for me to leave.

        Very well. Let her hear that the house is awake, at least.

        That is warning enough for a woman who needs none.
        """

        call broken_day2_evening_check_gathered

    else:

        """
        Lady Claythorn's door, dark and silent.

        She heard me the first time.
        """

    return


# The Captain's and Mr Manning's doors - both men are still downstairs.
label broken_day2_evening_bedroom_empty:

    $ change_room('bedrooms_hallway')

    """
    I knock. No light beneath the door, and no answer.

    He is not up here.

    Whoever I mean to find tonight, I must look downstairs first.
    """

    return


label broken_day2_evening_bedroom_lad:

    $ change_room('bedrooms_hallway')

    """
    Ted Harring's door.

    Behind it he is lying where we carried him, past all warning and all watches.

    I stand a moment with my knuckles an inch from the wood, feeling a fool.

    Rest easy, Mr Harring. This is for the ones you left behind.
    """

    return


# ------------------------------------
#   ATTIC
# ------------------------------------
label broken_day2_evening_attic_default:

    $ all_menus[broken_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[broken_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[broken_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[broken_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('attic_butler_room'))

    """
    From the attic stair comes the scrape of something heavy being dragged, and low voices, and not one line of light under any door.

    I knock. The dragging stops.

    Nobody answers, and the voices do not start again until I am halfway back down the stair.

    The staff are awake at this hour, and busy, and want no witnesses to it.

    That is an answer of its own.
    """

    return


# ------------------------------------
#   GROUND FLOOR
# ------------------------------------
label broken_day2_evening_tea_room:

    # The evening's real content: Captain Sinha reads, Mr Manning drinks.
    call broken_day2_evening_tea_room_scene

    return


label broken_day2_evening_dining_room:

    $ change_room('dining_room')

    """
    The table has been cleared, the cloth drawn, the chairs set straight.

    Everything in perfect order, as though the household meant to be judged on it.

    Nothing here but the ghost of an empty chair.
    """

    return


label broken_day2_evening_entrance_hall:

    $ change_room('entrance_hall')

    if not broken_details.saved_variables['day2_evening_phone_tried']:

        $ broken_details.saved_variables['day2_evening_phone_tried'] = True

        """
        The hall stands empty, and the telephone waits on its table by the stair.

        I lift the receiver and hold it to my ear.

        Nothing.

        No operator, no crackle from the exchange. A dead silence, like a shell held to the ear.

        Yet our hostess telephoned the police station this very evening, or so she told us at dinner.

        Either the line has died since, or no call was ever placed.

        I set the receiver back on its cradle.

        The house is cut off, and somebody has wished it so.
        """

    else:

        """
        I try the telephone once more.

        The line is as dead as before.
        """

    return


label broken_day2_evening_garden:

    $ change_room('manor_garden')

    """
    The night is cold and moonless, and the wood stands like a wall at the edge of the lawn.

    Somewhere beyond it lies a road with a tree across it.

    Nothing to be learned out here but how dark a Scottish night can be.

    I step back inside.
    """

    return


label broken_day2_evening_servant_stairs:

    $ change_room('servant_stairs')

    """
    The livery hangs on its peg where I left it, but tonight it can do nothing for me.

    The door at the foot of the stair is locked from the other side.

    Through it, faintly, come footsteps and the corded creak of trunks being moved.

    The servants' floor is awake, and it has locked the house out.
    """

    return


label broken_day2_evening_portrait_gallery:

    call broken_portrait_gallery_default

    return


label broken_day2_evening_library:

    call broken_library_default

    return


label broken_day2_evening_billiard_room:

    $ change_room('billiard_room')

    """
    Drinks in the billiard room, our hostess said, as there were yesterday.

    But the room is empty. No butler at his corner, no glasses set out, the bottles abandoned on the bar.

    The fire is dying in the grate and nobody has fed it.

    A billiard room without a servant in it, in a house like this, is a small wrongness all of its own.
    """

    return
