# --------------------------------------------
#   Captain — Sunday morning, nurse path
#
#   The captain confided in Miss Marsh last night.
#   She comes for him at first light, and they go to ground in the butler's
#   room in the attic to wait the morning out.
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
    I am.

    But the house is not.
    """

    captain """
    Explain.
    """

    nurse """
    There are no staff. No fires lit. No breakfast laid.

    I have walked the dining room, the kitchen, the back corridor.

    Not a soul.
    """

    captain """
    And Lady Claythorn?
    """

    nurse """
    Her door is locked.

    She does not answer.
    """

    """
    So it begins.

    Whatever is at the heart of this house, it has moved in the night.
    """

    captain """
    What of Miss Baxter and Mr Harring?
    """

    nurse """
    I have not knocked on their doors.

    I came straight to you.
    """

    captain """
    A sound choice.
    """

    """
    I think for a moment.

    The two of us alone in the corridors, looking for a fight, would be a poor plan.

    Better to get out of sight, take stock, and decide on a course before we are found.
    """

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
