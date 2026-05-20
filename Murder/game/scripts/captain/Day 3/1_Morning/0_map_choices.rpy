# --------------------------------------------
#   Captain — Sunday morning map exploration
#
#   With the staff gone, the basement is finally open to him.
#   The garage holds an old motor car.
#   If he found the petrol tin in the shed on Saturday evening, he can
#   choose to take the car and flee alone.
# --------------------------------------------

label captain_day3_morning_map_menu:
    python:
        captain_day3_morning_map_menu = TimedMenu("captain_day3_morning_map_menu", [
            # First floor
            TimedMenuChoice(default_room_text('library'), 'captain_day3_morning_library', 10, room='library', next_menu='captain_library_menu'),
            TimedMenuChoice(default_room_text('tea_room'), 'captain_day3_morning_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'captain_day3_morning_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'captain_day3_morning_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('billiard_room'), 'captain_day3_morning_billiard_room', 10, room='billiard_room'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'captain_day3_morning_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('manor_garden'), 'captain_day3_morning_garden', 10, room='manor_garden'),
            # Bedrooms
            TimedMenuChoice(default_room_text('bedroom_lad'), 'captain_day3_morning_bedroom_lad', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 'captain_day3_morning_bedroom_psychic', 10, room='bedroom_psychic'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'captain_day3_morning_bedroom_nurse', 10, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'captain_day3_morning_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'captain_day3_morning_bedroom_drunk', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'captain_day3_morning_bedroom_doctor', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_broken'), 'captain_day3_morning_bedroom_broken', 10, room='bedroom_broken'),
            # Attic
            TimedMenuChoice(default_room_text('storage'), 'captain_day3_morning_attic_default', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'captain_day3_morning_attic_default', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'captain_day3_morning_attic_default', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'captain_day3_morning_attic_default', 10, room='butler_room'),
            # Basement — now reachable, no staff
            TimedMenuChoice(default_room_text('kitchen'), 'captain_day3_morning_kitchen', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'captain_day3_morning_scullery', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'captain_day3_morning_garage', 10, room='garage', next_menu='captain_day3_morning_garage_menu'),
            TimedMenuChoice(default_room_text('gun_room'), 'captain_day3_morning_gun_room', 10, room='gun_room'),
            # End
            TimedMenuChoice(
                'Wait for the others in the entrance hall',
                'generic_cancel',
                early_exit = True,
                room = 'entrance_hall',
            ),
        ], is_map = True)

    return


# ------------------------------------
#   BASEMENT — first visit framing
# ------------------------------------
label captain_day3_first_downstairs:

    if not captain_details.saved_variables["day3_morning_downstairs_visited"]:

        $ change_room("basement_stairs")

        """
        I take the stairs to the basement.

        No staff. No voices. No clatter of pans.

        The house has been emptied to its bones.
        """

        $ captain_details.saved_variables["day3_morning_downstairs_visited"] = True

    return


label captain_day3_morning_kitchen:

    call captain_day3_first_downstairs

    $ change_room('kitchen')

    """
    The range is cold.

    No bread has been put out. No water set to boil.

    A breakfast service that was never begun.
    """

    return


label captain_day3_morning_scullery:

    call captain_day3_first_downstairs

    $ change_room('scullery')

    """
    Yesterday's dishes still wait in the sink.

    The staff did not even stop to clear the supper plates before they left.

    Or before they were taken.
    """

    return


label captain_day3_morning_gun_room:

    call captain_day3_first_downstairs

    $ change_room('gun_room')

    if captain_details.saved_variables["day3_morning_gun_room_visited"]:

        """
        I have already been through what is here.

        Nothing more for me.
        """

        return

    $ captain_details.saved_variables["day3_morning_gun_room_visited"] = True

    """
    The hunting rifles stand in their rack along the wall.

    There is a revolver on the bench. I check it: empty.

    The cartridges are not in the room. Whoever cleared the staff out has taken them, or hidden them.

    A loaded gun would be a comfort. An empty one is only a weight.

    I leave them where they are.
    """

    return


label captain_day3_morning_garage:

    call captain_day3_first_downstairs

    $ change_room('garage')

    if captain_details.saved_variables["day3_morning_car_seen"]:

        $ change_room('garage')

        """
        The car still sits where I left it.

        Nothing has changed.
        """

        return

    $ captain_details.saved_variables["day3_morning_car_seen"] = True

    """
    The garage is dim.

    Lady Claythorn's good Rolls Royce is gone.

    In its place, an old motor car of an earlier make. Dusty, but sound under the dust.

    I lift the bonnet. The engine is in order.

    I try the starter. It turns over once and dies.

    The tank is dry.
    """

    $ captain_details.threads.unlock('seen_car')

    if captain_details.threads.is_unlocked('petrol_tin_in_shed'):

        """
        The shed.

        The petrol tin I found last night, set out in the middle of the floor as if waiting to be carried away.

        A full can would more than serve.

        I could go down to the shed, fetch it, fill the tank, and be gone before the house knows I am missing.

        It would be the safe choice for one man.

        It would also leave the others to whatever is happening here.
        """

        call run_menu(TimedMenu("captain_day3_morning_garage_menu", [
            TimedMenuChoice("Fetch the petrol and drive out alone",
                'captain_day3_morning_escape_alone', 0, early_exit=True),
            TimedMenuChoice("Leave the car. The others come first",
                'captain_day3_morning_stay_with_others', 0, early_exit=True),
        ]))

    else:

        """
        Without petrol, the car is a dead weight.

        Lady Claythorn's chauffeur drove us in on Friday. Wherever he is now, he did not leave any fuel behind.

        I close the bonnet and step back.
        """

    return


label captain_day3_morning_escape_alone:

    """
    Decision made.

    I close the bonnet, fetch the master key from my pocket, and slip out through the side door.

    The garden lies under a thin mist.

    The shed is where I left it last night.
    """

    # TODO: write the actual escape sequence and ending (captain survives alone).
    # For now, route to the placeholder so the rest of the chapter keeps building.
    jump work_in_progress


label captain_day3_morning_stay_with_others:

    captain """
    No.

    Not yet.
    """

    """
    I will not take the only way out of this house before I know what has become of the rest of them.

    I close the bonnet and step back.
    """

    return


# ------------------------------------
#   FIRST FLOOR
# ------------------------------------
label captain_day3_morning_library:

    call captain_library_default

    return


label captain_day3_morning_portrait_gallery:

    call captain_portrait_gallery_default

    return


label captain_day3_morning_tea_room:

    $ change_room('tea_room')

    """
    The fire is dead in the grate.

    No tea has been laid. No one has been in this room since last night.
    """

    return


label captain_day3_morning_dining_room:

    $ change_room('dining_room')

    """
    The table is bare.

    No breakfast service.

    The room has been left exactly as the butler closed it down after dinner.
    """

    return


label captain_day3_morning_entrance_hall:

    $ change_room('entrance_hall')

    """
    The hall is empty.

    The front door is shut, but not bolted.

    Whoever came or went last night did so without making any noise of it.
    """

    return


label captain_day3_morning_billiard_room:

    $ change_room('billiard_room')

    """
    The decanters stand on the side, untouched.

    Last night's glasses have not been cleared.

    The staff did not get round to this room before they vanished.
    """

    return


label captain_day3_morning_garden:

    $ change_room('manor_garden')

    """
    The drive is empty.

    No cars. No carts. No tracks fresh on the gravel.

    Whoever has gone, has gone on foot, or some hours ago.

    A thin mist hangs in the trees. The air is cold.

    I do not linger.
    """

    return


# ------------------------------------
#   BEDROOMS
# ------------------------------------
label captain_day3_morning_bedroom_default_intro:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    return


label captain_day3_morning_bedroom_lad:

    call captain_day3_morning_bedroom_default_intro

    captain """
    Mr Harring?
    """

    """
    No answer.

    I try the handle. The door is not locked. The room is empty, the bed made.

    Wherever the boy is, he is not in his quarters.
    """

    return


label captain_day3_morning_bedroom_psychic:

    call captain_day3_morning_bedroom_default_intro

    captain """
    Miss Baxter?
    """

    """
    No reply.

    I try the handle. The door opens on an empty room.

    The bed has been slept in, but Miss Baxter is gone.
    """

    return


label captain_day3_morning_bedroom_nurse:

    call captain_day3_morning_bedroom_default_intro

    captain """
    Miss Marsh?
    """

    """
    Silence.

    The door is locked.

    I have the master key in my pocket, but I do not use it yet.

    If she is in there and means to stay hidden, that is her choice.

    If she is not in there, the room can wait.
    """

    return


label captain_day3_morning_bedroom_host:

    call captain_day3_morning_bedroom_default_intro

    captain """
    Lady Claythorn?
    """

    """
    No answer.

    The door is locked.

    I fit the master key. The wardrobe stands open, clothes scattered on the floor.

    Whoever calls herself Lady Claythorn has gone in a hurry.
    """

    return


label captain_day3_morning_bedroom_drunk:

    call captain_day3_morning_bedroom_default_intro

    if captain_details.saved_variables["day3_morning_drunk_checked"]:

        """
        I have already been through Mr Manning's room.

        There is nothing more I can do for him.
        """

        return

    $ captain_details.saved_variables["day3_morning_drunk_checked"] = True

    captain """
    Mr Manning?
    """

    """
    No reply.

    I unlock the door with the master key and step inside.
    """

    $ change_room("bedroom_drunk")

    $ play_music('scary', fadeout_val=1)

    """
    Manning lies in his bed, sheets soaked through.

    His throat has been cut.

    He has been dead for hours.

    Someone came through this door in the night, and Manning, drunk as he was, never woke.
    """

    captain """
    God rest you.
    """

    """
    I draw the sheet up over him and step back into the corridor.

    Whoever did this had a key.

    I had thought I was the only one with one, but evidently I was wrong.
    """

    $ play_music('mysterious', 2)

    return


label captain_day3_morning_bedroom_doctor:

    $ change_room("bedroom_doctor")

    """
    Doctor Baldwin still lies where we left him yesterday.

    The blanket has not been moved.

    Whoever has been about the house in the night, they did not trouble him.
    """

    return


label captain_day3_morning_bedroom_broken:

    $ change_room("bedroom_broken")

    """
    Mr Moody's room is as it was yesterday.

    The bed has been straightened around him. His effects, set in order.

    The house has tidied its dead with the same calm hand it tidies everything else.
    """

    return


# ------------------------------------
#   ATTIC
# ------------------------------------
label captain_day3_morning_attic_default:

    $ change_room("attic_hallway")

    """
    The attic is much as I left it last night.

    I have already seen what is up here.

    There is nothing more for me in these rooms.
    """

    return
