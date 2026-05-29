# --------------------------------------------
#   Captain — Sunday morning, nurse path
#
#   The captain confided in Miss Marsh last night, and she comes for him at
#   first light. After they take stock, he must choose:
#     - Leave at once: they run into Mr Harring and Miss Baxter, take the old
#       motor car together, and are ambushed on the road -> car_ambush ending.
#     - Go to ground: they hide in the butler's attic room and wait the
#       morning out, then come down in the afternoon.
# --------------------------------------------

label captain_day3_morning_nurse:

    $ change_room('bedroom_captain', irisout)

    """
    I sleep poorly, and only in patches.

    The house stays quiet through the night.

    A little before half past eight, I dress and sit on the edge of the bed.

    There is a soft, quick knock at the door.
    """

    play sound door_knock

    nurse """
    Captain. It's me.
    """

    """
    I unlock the door.

    Miss Marsh slips inside without a word and closes it behind her.

    She is pale, but quite collected.
    """

    captain """
    Miss Marsh.

    Are you all right?
    """

    nurse """
    I am, but there is something wrong with the house.
    """

    captain """
    What do you mean?
    """

    nurse """
    There are no staff. No fires lit. No breakfast laid.

    I have walked the dining room, the kitchen, the back corridor.

    Not a soul.
    """

    captain """
    So I was right, something is afoot.

    Have you tried to check some other rooms?
    """

    nurse """
    No, I came straight to you.
    """

    captain """
    A sound choice.
    """

    nurse """
    But what are we going to do now?

    I was thinking we might hide for a while, until we can learn more about what is happening here.

    Maybe it would be better to leave, but I am afraid whoever is behind all of this might spot us.

    And ... then I don't know what they might do.
    """

    """
    I think for a moment.

    If someone in this house means us harm, it might be best to remain hidden.

    On the other hand, we cannot hide forever.

    Two courses lie open to me, and neither is without risk.
    """

    $ time_left = 1
    call run_menu( TimedMenu("captain_day3_morning_nurse_menu", [
        TimedMenuChoice("Slip out of the house now, while it is quiet", 'captain_day3_morning_nurse_leave', early_exit=True),
        TimedMenuChoice("Go to ground and wait the morning out", 'captain_day3_morning_nurse_hide', early_exit=True),
    ]))

    return


# ------------------------------------
#   NURSE PATH — leave at once
#
#   The captain and Miss Marsh try to quit the house early. They run into
#   Mr Harring and Miss Baxter, who will not be left behind, and the four of
#   them take the old motor car. It does not see them clear of the estate.
# ------------------------------------
label captain_day3_morning_nurse_leave:

    captain """
    We are not going to wait to be found.

    We leave now, on foot if we must, and we put this house behind us.
    """

    nurse """
    You are certain?
    """

    captain """
    I am certain of very little this morning.

    But I would sooner take my chances on the road than in a locked room.
    """

    $ change_room('bedrooms_hallway', dissolve)

    """
    We go down together, keeping close to the wall.

    The hall is grey and still.

    I mean to make for the garage and see whether the old car can be made to serve.
    """

    $ change_room('entrance_hall', dissolve)

    """
    We are halfway across the entrance hall when a voice stops us.
    """

    lad """
    Captain! Miss Marsh!
    """

    """
    Ted Harring comes quickly down the stair, Miss Baxter close behind him.

    Relief is plain on both their faces.
    """

    psychic """
    Thank heaven. We thought we were the only ones left.
    """

    lad """
    Where are you going?
    """

    captain """
    Out.

    The staff are gone, the telephone is dead, and Mr Manning is murdered in his bed.

    I do not intend to be next.
    """

    psychic surprised """
    Murdered?
    """

    captain """
    Yes.

    A house like this keeps a motor somewhere. I mean to find it and get it running.

    Miss Marsh and I are leaving.
    """

    lad """
    Then we are coming with you.

    You cannot mean to leave us here.
    """

    """
    I look at the boy, and at Miss Baxter beside him.

    I had meant to travel light and quiet, two and no more.

    But I cannot in conscience shut the door on them.
    """

    captain """
    Very well.

    All four of us, then.

    Quickly, and quietly.
    """

    $ change_room('manor_garden', dissolve)

    """
    The garage gives up an old motor car, left behind when the good one went.

    There is fuel enough in a can on the bench to fill the tank.

    I coax the engine into life on the third try, and we crowd aboard.
    """

    call captain_day3_car_ride_ambush


# ------------------------------------
#   NURSE PATH — go to ground
# ------------------------------------
label captain_day3_morning_nurse_hide:

    captain """
    We should not stay here.

    This room is the first place anyone would look for me.
    """

    nurse """
    Where, then?
    """

    captain """
    The attic.

    I have the butler's master key.

    His room will do.

    No guest has any business being up there, so no one will think to look for us.
    """

    nurse """
    Lead the way, Captain.
    """

    $ change_room('bedrooms_hallway', dissolve)

    """
    I open the door a crack and listen.

    The corridor is empty, and very still.

    I step out, Miss Marsh close behind.

    We move quickly, keeping to the side of the hall, and reach the foot of the attic stair without seeing anyone.
    """

    call change_time(9, 0)

    $ change_room('attic_hallway')

    """
    The boards creak under our weight.

    I take the master key from my pocket and fit it to the butler's door.

    The bolt slides back without protest.
    """

    play sound door_open

    $ change_room("butler_room")

    """
    I usher Miss Marsh inside and close the door behind us.

    I turn the key in the lock.
    """

    play sound door_locked

    captain """
    Sit down, Miss Marsh.

    We are going to be here a little while.
    """

    nurse """
    Thank you.
    """

    """
    She sits on the edge of the narrow bed and folds her hands in her lap.

    A composed woman.

    She has not asked me a single foolish question since she came through my door.
    """

    captain """
    Tell me what you saw, room by room.

    Leave nothing out.
    """

    """
    She does, plainly and in order.

    Empty dining room. Cold range. Back door bolted from the inside.

    No coats taken from the hall. No carriage in the drive.

    Whoever has gone, has gone in a hurry, or has not gone at all.
    """

    call change_time(10, 30)

    """
    We sit in silence for a long while after that.

    Now and again I hear a board ease somewhere below.

    Once, footsteps in the upstairs corridor — slow, deliberate, then gone.

    I keep my hand close to my pocket and say nothing.

    Miss Marsh does the same.

    She has the gift, rare in any company, of being able to sit quite still and quite quiet.
    """

    call change_time(11, 30)

    """
    By late morning, the house has settled into a heavy silence.

    Whatever was moving about earlier seems to have stopped, or gone elsewhere.

    Miss Marsh looks at me.
    """

    nurse """
    What now, Captain?
    """

    captain """
    Now we go down.

    Carefully.

    And we find out what has become of the others.
    """

    return
