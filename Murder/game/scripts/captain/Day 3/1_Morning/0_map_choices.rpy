# --------------------------------------------
#   Captain — Sunday morning map exploration
#
#   With the staff gone, the basement is finally open to him.
#   The garage holds an old motor car.
#   The garden gives a second chance at the petrol: with the staff gone he
#   can let himself into the locked shed with the master key and take the
#   tin, even if he missed it on Saturday evening (sets petrol_tin_in_shed).
#   The car and petrol together open the flight options in the afternoon.
# --------------------------------------------

label captain_day3_morning_map_menu:
    python:
        captain_day3_morning_map_menu = TimedMenu("captain_day3_morning_map_menu", [
            # First floor
            TimedMenuChoice(default_room_text('library'), 'captain_day3_morning_library', 10, room='library'),
            TimedMenuChoice(default_room_text('tea_room'), 'captain_day3_morning_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'captain_day3_morning_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'captain_day3_morning_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('billiard_room'), 'captain_day3_morning_billiard_room', 10, room='billiard_room'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'captain_day3_morning_entrance_hall', 0, room='entrance_hall', early_exit=True),
            TimedMenuChoice(default_room_text('manor_garden'), 'captain_day3_morning_garden', 10, room='manor_garden'),
            # Bedrooms
            TimedMenuChoice(default_room_text('bedroom_captain'), 'captain_day3_morning_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_lad'), 'captain_day3_morning_bedroom_lad', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 'captain_day3_morning_bedroom_psychic', 10, room='bedroom_psychic'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'captain_day3_morning_bedroom_nurse', 10, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'captain_day3_morning_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'captain_day3_morning_bedroom_drunk', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'captain_day3_morning_bedroom_doctor', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_broken'), 'captain_day3_morning_bedroom_broken', 10, room='bedroom_broken'),
            # Attic — same rooms as the night before (state carries over)
            TimedMenuChoice(default_room_text('storage'), 'captain_attic_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'captain_attic_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'captain_attic_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'captain_attic_butler_room', 10, room='butler_room'),
            # Basement — now reachable, no staff
            TimedMenuChoice(default_room_text('kitchen'), 'captain_day3_morning_kitchen', 10, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'captain_day3_morning_scullery', 10, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'captain_day3_morning_garage', 10, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'captain_day3_morning_gun_room', 10, room='gun_room'),
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

    No matter, I still have mine in my pocket.

    I leave them where they are.
    """

    return


label captain_day3_morning_garage:

    call captain_day3_first_downstairs

    $ change_room('garage')

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

        I found petrol there, a full can.

        That is more than enough to leave this place.

        But first I should know what has become of the others.

        I close the bonnet and leave the car as it stands.
        """

    else:

        """
        Without petrol, the car is a dead weight.

        Lady Claythorn's chauffeur drove us in on Friday. Wherever he is now, he did not leave any fuel behind.

        I close the bonnet and step back.
        """

    return


# ------------------------------------
#   FIRST FLOOR
# ------------------------------------
label captain_day3_morning_library:

    $ change_room('library')

    if captain_details.threads.is_unlocked('captain_host_suspicion_name'):

        """
        The genealogy book still lies open on the table.

        I have already read what I needed from it.
        """

        return

    """
    The genealogy book lies open on the table, where I left it.

    But I do not have time to sit and read it through.

    Not now. Not with the staff vanished and the house emptied around me.

    I leave the book where it lies.
    """

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

    It is the heart of the house, so I linger a little to see if I can hear something.
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

    Lady Claythorn's good motor car is gone, and the chauffeur with it.

    A thin mist hangs over the gravel and the wet grass.
    """

    if captain_details.threads.is_unlocked('petrol_tin_in_shed'):

        """
        The shed at the end of the garden probably still holds the petrol tin I found on Saturday night.

        No need to check there again.
        """

        return

    """
    With the staff gone, there is no longer anyone to keep me out of any corner of this place.

    I walk down to the squat timber outbuilding at the end of the garden.
    """

    # TODO add this image
    $ change_room('toolshed_outside_day')

    """
    The door is locked.

    But the master key is in my pocket, and there is no one left to answer for it.
    """

    play sound door_open

    $ change_room('toolshed')

    call captain_garden_shed_inside

    return


# ------------------------------------
#   BEDROOMS
# ------------------------------------
label captain_day3_morning_bedroom_default_intro:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    return


# Spoken only the first time the captain lets himself into someone's private
# room, whether the door was locked or simply unanswered. Every later room is
# entered without comment.
label captain_day3_morning_privacy_resolve:

    if not captain_details.saved_variables["day3_morning_privacy_explained"]:

        """
        Yesterday I would have left it at that and respected their privacy.

        Today, with the staff vanished and a man lying murdered down the corridor, I will not.
        """

        $ captain_details.saved_variables["day3_morning_privacy_explained"] = True

    return


label captain_day3_morning_bedroom_captain:

    $ change_room('bedroom_captain')

    """
    My own room, just as I left it.

    I cannot say why my feet have carried me back here.

    There is no time to nap, and no inclination for it either.

    The bed can wait. I have a house to search.
    """

    return


label captain_day3_morning_bedroom_lad:

    call captain_day3_morning_bedroom_default_intro

    captain """
    Mr Harring?
    """

    """
    No answer.
    """

    call captain_day3_morning_privacy_resolve

    """
    I try the handle. The door is not locked.
    """

    $ change_room("bedroom_lad")

    """
    The room is empty.

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
    """

    call captain_day3_morning_privacy_resolve

    """
    I try the handle. The door is not locked, and swings open.
    """

    $ change_room("bedroom_psychic")

    """
    The room is empty.

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
    """

    $ captain_details.saved_variables["day3_morning_nurse_checked"] = True

    call captain_day3_morning_privacy_resolve

    """
    I try the handle. The door is locked.

    I fit the key and turn it.
    """

    play sound door_open

    $ change_room("bedroom_nurse")

    """
    The room is empty.

    The bed is made and has not been slept in.

    Miss Marsh is not here, and nothing in these four walls tells me where she has gone.

    I take note of it, lock the door behind me, and step back out.
    """

    return


label captain_day3_morning_bedroom_host:

    call captain_day3_morning_bedroom_default_intro

    captain """
    Lady Claythorn?
    """

    """
    No answer.
    """

    call captain_day3_morning_privacy_resolve

    """
    I try the handle. The door is locked.

    I fit the key.
    """

    play sound door_open

    $ change_room("bedroom_host")

    """
    The wardrobe stands open, clothes scattered on the floor.

    Whoever calls herself Lady Claythorn has gone in a hurry.
    """

    return


label captain_day3_morning_bedroom_drunk:

    call captain_day3_morning_bedroom_default_intro

    captain """
    Mr Manning?
    """

    """
    No reply.
    """

    $ captain_details.saved_variables["day3_morning_drunk_checked"] = True

    call captain_day3_morning_privacy_resolve

    """
    I try the handle. The door is locked.

    I unlock it with the master key and step inside.
    """

    $ change_room("bedroom_drunk")

    $ play_music('scary', fadeout_val=1)

    """
    Manning lies in his bed, the sheets soaked through and dark. 

    I approach the bed.    
    
    His throat has been cut.

    I jump back in horror.

    I thought I had seen death enough to be hardened to it. 

    But this turns my stomach. 
    
    A man killed in his bed, not given the chance to lift a hand.

    Shivers run through my body and guilt overwhelms me.

    I was the one who shut him in to keep the peace.
    
    That made him easy prey for whoever is behind this horrific weekend.

    Tears start running down my face and my hands begin to shake.

    It takes me a moment to steady myself.

    It is good I am alone to witness this. If anyone had been with me, they would have seen right through my act. 

    I step back into the corridor.
    """

    $ play_music('PREVIOUS')

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
