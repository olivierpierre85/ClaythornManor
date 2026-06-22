# Servants' floor (downstairs) for Broken (Thomas Moody), Friday evening.
#
# These rooms are only reachable once the footman's livery has been found in the
# servant stair (found_livery). The map menu in 0_map_choices.rpy gates them and
# handles the livery change on the way down (broken_descend_if_needed).
#
# Two of them carry the evening's real consequences:
#   - Scullery: an open bottle of rat poison, left in plain sight. He may take it
#     (found_poison) or leave it.
#   - Kitchen:  he dodges a footman, then finds the maid alone. He may slip out,
#     or — only if he has caught the host lying at dinner (host_lies) — risk a
#     word with her. She tells him what the butler really is, and the butler sees
#     that he never wakes (broken_ending_day1_throat_cut).

# ------------------------------------
#   SERVANTS' FLOOR (found_livery required)
# ------------------------------------
label broken_day1_evening_downstairs_refused:

    # Trying the servants' floor once greys it all (day1_evening_downstairs_refused)
    # until the livery is found. He is turned back, so no descend/ascend here.
    $ change_room('basement_stairs')

    """
    The stair runs down to the kitchens and the servants' hall.

    A guest who shows his face below is noticed at once, and remembered.

    Not as I am, at any rate. If I mean to go down there, I shall need some way to pass unremarked.
    """

    $ broken_details.saved_variables['day1_evening_downstairs_refused'] = True

    return


# ------------------------------------
#   SCULLERY (the rat poison)
# ------------------------------------
label broken_day1_evening_scullery:

    call broken_descend_if_needed

    $ change_room('scullery')

    """
    I manage to pass unnoticed through the kitchen to reach the scullery.

    It is cold and smells of soda and wet stone.

    No one is about. I have it to myself.

    On the shelf above the sink a bottle stands uncorked, and quite impossible to miss.

    The label leaves no room for doubt. 
    
    Rat poison, and a fair measure of it already gone.

    Left open, in plain sight, in a house full of guests.

    Carelessness, perhaps. Or something a good deal worse.
    """

    call run_menu(TimedMenu("broken_day1_evening_scullery_poison_menu", [
        TimedMenuChoice('Take the bottle with you', 'broken_day1_evening_scullery_take_poison', 0, early_exit=True),
        TimedMenuChoice('Leave it where it stands', 'broken_day1_evening_scullery_leave_poison', 0, early_exit=True),
    ]))

    return


label broken_day1_evening_scullery_take_poison:

    """
    There is probably a very good reason for it to be there.

    Still, I would rather have it where I can keep an eye on it.

    I slip the bottle inside my coat.
    """

    $ broken_details.threads.unlock('found_poison')

    return


label broken_day1_evening_scullery_leave_poison:

    """
    No. I see no reason to take that bottle with me.

    I leave it exactly where it stands, and leave the room.
    """

    return


# ------------------------------------
#   KITCHEN (the footman, then the maid)
#   Talking to the maid is fatal — see broken_ending_day1_throat_cut, triggered
#   at the close of the evening in 1_main.rpy via the talked_to_maid thread.
# ------------------------------------
label broken_day1_evening_kitchen:

    call broken_descend_if_needed



    $ change_room('kitchen')

    """
    I enter the kitchen and stop dead.

    A footman is coming out, a laden tray balanced on one hand.

    I press back against the wall and let him pass, near enough to touch.

    My heart is going hard against my ribs.

    He does not appear to see me.

    The livery will fool a man at a distance, or one in a hurry.

    But close to, with a moment to look, any of the real staff would know in a heartbeat that I am none of theirs.

    I must be very cautious down here.

    The kitchen is all but empty, winding down for the night.

    The great range still breathes out its heat.

    A young maid stands at the sink with her back to me, scouring the last of the pots and pans.

    She has not heard me come in.
    """

    if not broken_details.threads.is_unlocked('host_lies'):

        """
        But she would see at once that I do not belong here.
        
        And I have no reason to trouble her.

        I slip out the way I came, before she ever knows I was there.
        """

        return

    """
    It would be risky to talk to her.

    She would probably see right away I am an impostor.

    But she could also help me understand why Lady Claythorn is lying to us.
    """

    call run_menu(TimedMenu("broken_day1_evening_kitchen_menu", [
        TimedMenuChoice('Ask her a few questions', 'broken_day1_evening_kitchen_maid', 0, early_exit=True),
        TimedMenuChoice('Leave her be', 'broken_day1_evening_kitchen_leave', 0, early_exit=True),
    ]))

    return


label broken_day1_evening_kitchen_leave:

    """
    No, it is better if she doesn't see me.

    I slip out the way I came, before she ever knows I was there.
    """

    return


label broken_day1_evening_kitchen_maid:

    """
    I step closer and clear my throat, softly, so as not to startle her.
    """

    broken """
    A long night of it, by the look of things.
    """

    """
    She turns, clearly surprised.
    """

    maid """
    I am sorry, but who are you?
    """

    """
    Alright, now is the time to see if I can bluff my way here.
    """

    broken """
    Forgive me.

    I am only taken on for the weekend, to lend a hand.

    I was sent for in a hurry, and told precious little of what goes on.
    """

    maid """
    Well, we all are.

    The manor stood empty before this, you know.

    If it is guidance you are after, find the butler.

    He is the only one who truly knows what is going on here.
    """

    """
    Empty before this?

    So the place has been prepared for this weekend, especially for us. How curious.
    """

    broken """
    This is rather unusual.

    If this place was empty before, why re-open it for this weekend?
    """

    maid """
    I could not say, exactly.

    There is some manner of surprise in store for the guests, I think.

    So, of course, share none of this with them.

    But ask the butler.

    He will tell you more than I can.    
    """

    """
    A surprise prepared for us. What does it all mean?

    I want to ask more questions, but to do so would appear too suspicious.

    I leave her to her pots and make my way back up, turning it all over in my mind.
    """

    $ broken_details.threads.unlock('talked_to_maid')

    return


# ------------------------------------
#   GARAGE
# ------------------------------------
label broken_day1_evening_garage:

    call broken_descend_if_needed

    call broken_garage_default

    return


# ------------------------------------
#   GUN ROOM
# ------------------------------------
label broken_day1_evening_gun_room:

    call broken_descend_if_needed

    call broken_gun_room_default

    return
