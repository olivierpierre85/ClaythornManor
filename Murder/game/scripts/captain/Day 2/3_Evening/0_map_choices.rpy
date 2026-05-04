# Map choices for Captain, Saturday evening
label captain_day2_evening_map_menu:
    python:
        captain_day2_evening_map_menu = TimedMenu(
            "captain_day2_evening_map_menu",
            [
            # Attic — now reachable: he is suspicious and has the master key
            TimedMenuChoice(default_room_text('storage'), 'captain_day2_evening_attic_storage', 0, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'captain_day2_evening_attic_males_room', 20, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'captain_day2_evening_attic_females_room', 20, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'captain_day2_evening_attic_butler_room', 0, room='butler_room'),
            # Bedrooms
            TimedMenuChoice(default_room_text('bedroom_lad'), 'captain_day2_evening_bedroom_lad', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'captain_day2_evening_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_broken'), 'captain_day2_evening_bedroom_broken', 10, room='bedroom_broken'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'captain_day2_evening_bedroom_nurse', 10, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'captain_day2_evening_bedroom_doctor', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'captain_day2_evening_bedroom_drunk', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 'captain_day2_evening_bedroom_psychic', 10, room='bedroom_psychic'),
            # First floor
            TimedMenuChoice(default_room_text('tea_room'), 'captain_day2_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'captain_day2_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'captain_day2_evening_garden', 0, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'captain_day2_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'captain_portrait_gallery_default', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('library'), 'captain_library_default', 0, room='library'),
            # Downstairs — staff still working there, captain stays out
            TimedMenuChoice(default_room_text('kitchen'), 'captain_day2_evening_downstairs_default', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'captain_day2_evening_downstairs_default', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'captain_day2_evening_downstairs_default', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'captain_day2_evening_downstairs_default', 10, room='gun_room'),
            # Specific actions
            TimedMenuChoice(
                'Look in on the billiard room',
                'captain_day2_evening_billiard_room',
                0,
                room = 'billiard_room',
                keep_alive=True,
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
label captain_day2_evening_downstairs_default:

    $ all_menus[captain_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('gun_room'))
    $ all_menus[captain_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('garage'))
    $ all_menus[captain_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('scullery'))
    $ all_menus[captain_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))

    """
    The staff are still about their work down there.

    Master key or not, I can think of no plausible errand that would carry a guest into the kitchens at this hour.

    Better to leave the lower floor alone.
    """

    return


# ------------------------------------
#   FIRST FLOOR
# ------------------------------------
label captain_day2_evening_tea_room:

    $ change_room('tea_room')

    """
    The tea room is empty and the fire has burned low.

    Nothing to be learned here.
    """

    return


label captain_day2_evening_dining_room:

    $ change_room('dining_room')

    """
    The table has been cleared.

    Only the polished wood remains, reflecting the lamps.

    No reason to linger.
    """

    return


label captain_day2_evening_entrance_hall:

    $ change_room('entrance_hall')

    """
    The hall is quiet.

    The same flagstones where we laid Doctor Baldwin a few hours ago.

    But nothing of interest.
    """

    return


# ------------------------------------
#   GARDEN AND SHED
# ------------------------------------
label captain_day2_evening_garden:

    $ change_room('entrance_hall')

    if not captain_details.objects.is_unlocked('lantern'):

        """
        I look out through the window.

        The night is utterly black, and a thick mist is rolling in across the lawn.

        Without a light, a man would lose himself between the house and the hedge.

        I shall not stumble about out there blind.
        """

        return

    if captain_details.saved_variables["day2_evening_shed_visited"]:

        """
        I have seen all I needed to see out there.

        No reason to brave the cold a second time.
        """

        return

    $ captain_details.saved_variables["day2_evening_garden_visited"] = True

    $ change_room('manor_garden')

    """
    I draw the side door closed behind me and light the lantern.

    The pool of light picks out the gravel path, the wet grass beyond, the dark mass of the hedge.

    I make my way around to the outbuilding I found yesterday.
    """

    call run_menu(TimedMenu("captain_day2_evening_garden_menu", [
        TimedMenuChoice("Try the shed door with the master key", 'captain_day2_evening_shed', 30, early_exit=True),
        TimedMenuChoice("Better not linger out here", 'generic_cancel', 10, early_exit=True),
    ]))

    $ change_room('bedroom_captain')

    """
    I slip back inside and brush the damp from my coat.

    No one seems to have marked my absence.
    """

    return


label captain_day2_evening_shed:

    $ captain_details.saved_variables["day2_evening_shed_visited"] = True

    """
    I fit the master key to the lock. It does not turn at first.

    A patient adjustment, and the bolt slides clear.

    The door creaks open on a small, low-roofed space smelling strongly of oil and old timber.
    """

    play sound door_unlock # TODO confirm sound exists

    """
    The lantern's glow picks out a workbench, a coil of rope, a tarpaulin folded against one wall.

    And, set rather neatly in the middle of the floor, a metal petrol tin.

    I unscrew the cap and lower my nose to it for a moment. Petrol, and a great deal of it.

    A full can, that could be useful.

    I search a little further but found nothing of interest, so I step out of this shed.

    I lock the door behind me as carefully as I opened it.
    """

    $ captain_details.threads.unlock('petrol_tin_in_shed')

    return


# ------------------------------------
#   ATTIC
# ------------------------------------
label captain_day2_evening_attic_default:

    $ change_room("attic_hallway")

    if not captain_details.saved_variables["day2_evening_attic_visited"]:

        $ captain_details.saved_variables["day2_evening_attic_visited"] = True

        """
        I climb the narrow stair to the attic.

        The boards creak under my weight. The air up here is closer, smelling of dust and old wood.

        A short corridor runs the length of the house, doors on either side.

        It is not a place a guest has any business being in.

        But after what happen today, I am not above breaking some rules if that means I can understand better what is happening today.

        I fit the master key to the door. 
        """

        play sound door_unlock

        """
        The bolt slides back without protest.

        A single key for the whole house. If it opens this one, it will open all the others up here just as readily.
        """

    return


label captain_day2_evening_attic_storage:

    call captain_day2_evening_attic_default

    if captain_details.objects.is_unlocked('lantern'):

        $ change_room("attic_storage_room")

        """
        Nothing more for me here. I have what I came for.
        """

        return

    $ change_room("attic_storage_room")

    """
    The storage room is crammed with the leavings of decades.

    Trunks stacked three deep, dust-sheeted furniture, boxes that have not been opened in a generation.

    I work my way along the shelves nearest the door, where the more recent items seem to live.

    Tins of paint. A pair of oil lamps. A small case of candles.

    And, set on its side beneath a folded oilcloth, a storm lantern.

    I lift it from the shelf. The reservoir is half full, the wick recently trimmed.

    A well-kept piece, in an attic full of old leavings. Someone in this house has been keeping it ready.

    That, by itself, is interesting.

    I take it up. It will be wanted before the night is out.
    """

    $ captain_details.objects.unlock('lantern')

    return


label captain_day2_evening_attic_males_room:

    call captain_day2_evening_attic_default

    if captain_details.saved_variables["visited_attic_males_room"]:

        $ change_room("attic_males_room")

        """
        I have already gone through this room.

        Nothing more here.
        """

        return

    $ captain_details.saved_variables["visited_attic_males_room"] = True

    $ change_room("attic_males_room")

    """
    Two beds, a chest of drawers, a peg for each man's coat.

    I work the drawers quickly. Folded shirts, a penknife, a few coins. Nothing of note.

    Then, at the back of the bottom drawer, beneath the linen, a folded sheet of paper.

    A letter from a London theatre company. Politely worded, but a rejection all the same.

    'We regret to inform you that the role has been filled. We wish you every success in your future endeavours.'

    An actor. Playing at being a footman.

    A curious choice of employment for a man with that ambition. And rather further from a stage than one would expect.

    I fold the letter back exactly as I found it.
    """

    $ captain_details.threads.unlock('footman_actor_letter')

    return


label captain_day2_evening_attic_females_room:

    call captain_day2_evening_attic_default

    if captain_details.saved_variables["visited_attic_females_room"]:

        $ change_room("attic_females_room")

        """
        I have already searched this room.

        Nothing more for me here.
        """

        return

    $ captain_details.saved_variables["visited_attic_females_room"] = True

    $ change_room("attic_females_room")

    """
    A small, spare room. Two narrow beds, a washstand, a single trunk between them.

    On the shelf above one of the beds, a few keepsakes — a dog-eared London playbill, another from a touring company.

    Tucked behind them, a faded photograph.

    A young woman in stage dress, posed beside a man I do not recognise. Smiling broadly for the camera.

    The maid who has been waiting on us all weekend.

    Or, more likely, the actress who has been playing at it.

    Two players in the same household, so far from any theatre worth the name.

    That is no coincidence at all.

    I replace the photograph and step back out.
    """

    $ captain_details.threads.unlock('maid_actress_photo')

    return


label captain_day2_evening_attic_butler_room:

    call captain_day2_evening_attic_default

    $ change_room("butler_room")

    if captain_details.saved_variables["visited_attic_butler_room"]:

        """
        The reinforced cabinet still stands against the far wall.

        I have already seen what is inside.
        """

        return

    $ captain_details.saved_variables["visited_attic_butler_room"] = True

    """
    The room itself is plain enough. A narrow bed, a washstand, a single chair.

    A head servant's quarters, and not a thing out of place.

    But against the far wall stands a heavy reinforced cabinet, glass-panelled, the household silver visible behind it.

    The lock is a modern one, and a good one.

    I take the master key from my pocket and try it.

    It turns without complaint.

    Inside: candlesticks, a salver, several sets of heavy plate. The honest wealth of the house, locked behind a butler's door rather than the master's.

    Curious. In a properly run household this would all be in the strong room downstairs, under the mistress's hand.

    I close the cabinet, lock it again, and step back.

    Whoever is truly running this house, it is not Lady Claythorn.
    """

    # TODO consider an observation thread for this realisation

    return


# ------------------------------------
#   BEDROOMS
# ------------------------------------
label captain_day2_evening_bedroom_default_intro:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    captain """
    Hello? Is anyone there?
    """

    return


label captain_day2_evening_bedroom_lad:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    """
    There is no reply.

    Only the sound of heavy furniture being dragged across the floor on the other side.

    Mr Harring is barricading himself in.

    I cannot say I blame the lad.
    """

    return


label captain_day2_evening_bedroom_psychic:

    call captain_day2_evening_bedroom_default_intro

    psychic """
    Yes? Who is it?
    """

    captain """
    Captain Sinha. Forgive me, Miss Baxter.

    I only wished to know whether you were quite all right.
    """

    psychic """
    You are kind, Captain. But I am very tired.

    Would you mind very much if we spoke in the morning?
    """

    captain """
    Of course not. Sleep well, Miss Baxter.
    """

    return


label captain_day2_evening_bedroom_nurse:

    call captain_day2_evening_bedroom_default_intro

    """
    No reply.

    Either Miss Marsh is already asleep, or she is not in her room at all.
    """

    return


label captain_day2_evening_bedroom_host:

    call captain_day2_evening_bedroom_default_intro

    """
    No answer.

    The lady of the house, it seems, has not yet retired — or does not wish to be disturbed if she has.
    """

    return


label captain_day2_evening_bedroom_doctor:

    $ change_room("bedroom_doctor")

    """
    Doctor Baldwin lies upon the bed exactly as we left him this afternoon.

    The blanket I drew over him has not been disturbed.

    There is nothing more I can do for the man.

    I close the door quietly behind me.
    """

    return


label captain_day2_evening_bedroom_broken:

    $ change_room("bedroom_broken")

    """
    Mr Moody's room sits much as it must have done since this morning.

    The bed has been straightened. His effects have been arranged with a tidy hand.

    I leave the room as I found it.
    """

    return


label captain_day2_evening_bedroom_drunk:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    drunk """
    Mmf... go 'way...
    """

    """
    Mr Manning is still locked in, and very much the worse for the day's drinking.

    The key in my pocket would let me through that door at any moment.

    Tonight, however, he is more use to me where he is.
    """

    return
