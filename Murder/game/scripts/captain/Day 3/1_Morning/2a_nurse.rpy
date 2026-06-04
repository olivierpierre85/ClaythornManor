# --------------------------------------------
#   Captain — Sunday morning, nurse path
#
#   The captain confided in Miss Marsh last night, and she comes for him at
#   first light. After they take stock, he is offered a choice that is really
#   no choice at all:
#     - Leave at once: Miss Marsh cannot face the road on foot and admits she
#       is unwell, so the captain yields and they go to ground after all.
#     - Go to ground: they hide in the butler's attic room directly.
#   Either way they wait the morning out and come down in the afternoon.
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

    Have you checked any of the other rooms?
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
        TimedMenuChoice("Do not waste time, leave the house now", 'captain_day3_morning_nurse_leave', early_exit=True),
        TimedMenuChoice("Go to attic and wait the morning out", 'captain_day3_morning_nurse_hide', early_exit=True),
    ]))

    return


# ------------------------------------
#   NURSE PATH — leave at once (a false choice)
#
#   Miss Marsh cannot face the road on foot and admits she is unwell, though
#   she will not say how badly. The captain yields and they go to ground after
#   all, falling through to the hide sequence.
# ------------------------------------
label captain_day3_morning_nurse_leave:

    captain """
    I have no wish to wait here to be found.

    I would put this house behind me now, while it is quiet.
    """

    nurse """
    On foot, Captain?
    """

    captain """
    I am afraid yes.

    I do not see another way.

    Lady Claythorn and her staff most likely left with the motor car.

    It is a fairly long walk to the town, but it is still early, I am sure we can make it.
    """

    nurse """
    Oh, I am sure you could, Captain.

    Sadly I can't.
    """

    """
    She says it quietly, and I see now what I had been too preoccupied to mark before.

    The pallor that is not only fear.

    The careful way she holds herself.
    """

    nurse """
    I am not a healthy woman, Captain.

    There is a good chance my body will not hold for such a long journey.
    """

    captain """
    I see.
    """

    """
    I think her condition might be worse than her quiet behaviour shows.

    But if she does not want to tell me more, I will not press her.
    """

    captain """
    All right, we can stay at the manor a bit longer until things settle down.
    """

    nurse """
    Thank you, Captain.
    """

    jump captain_day3_morning_nurse_hide


# ------------------------------------
#   NURSE PATH — go to ground
# ------------------------------------
label captain_day3_morning_nurse_hide:

    captain """
    We should not stay here.

    This room is the first place anyone would look for me.
    """

    nurse """
    You are right.

    I believe the attic is the best place to hide.

    It should be empty now.
    """

    captain """
    The attic, good idea.

    I have the butler's master key.

    So we can hide in his room and lock the door.
    """

    nurse """
    Perfect.

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

    """
    She sits on the edge of the narrow bed and folds her hands in her lap.
    """

    call change_time(10, 30)

    """
    We sit in silence for a long while after that.

    Then, I hear a board ease somewhere below.

    Once, footsteps in the upstairs corridor — slow, deliberate, then gone.
    """

    captain """
    Somebody is downstairs.
    """

    nurse """
    It could be one of the others.
    """

    captain """
    It could be, but I do not know whether they are friend or foe.

    It is probably better to wait for them to leave.
    """

    nurse """
    You are probably right.
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
    Well, I have tried to find the best way to act now.
    """

    nurse """
    And?
    """

    captain """
    I believe the safer bet is for me to leave.

    Even if I have to do it on foot.

    You could stay safely here, I am sure I can make it before the end of the day.
    """

    nurse """
    I see.

    If I am being honest I do not like this captain, it feels extremely dangerous for me.
    """

    captain """
    I know and I am sorry, but I still believe it is our best chance.

    And if it can ease your mind, you can take this pistol.

    I try to always keep it on me, one never knows when one might need protection.

    Do you know how to use one?
    """

    nurse """
    I can manage, I believe.

    But I really wish I won't have to use it.
    """

    captain """
    You probably won't, just stay here, close the door and do not open to anybody.

    It is safe to say that everyone is a suspect at this point.
    """

    nurse """
    All right, I think I can manage that.

    Thank you captain.
    """

    captain """
    Good luck Miss Marsh.
    """

    $ change_room('entrance_hall', dissolve)

    """
    I do not waste time and go down fast to the entrance hall.

    It is still empty, so I make it outside.
    """

    call change_time(12, 00)

    $ change_room('forest_road', dissolve)

    """
    I took only my coat and what will fit in its pockets.

    The drive gives way to a rough road, and the road to open country between the trees.
    """

    $ play_music('danger')

    """
    I keep a solid pace for the better part of an hour.

    Then, somewhere behind me, I hear an engine.
    """

    play sound car_driving fadein 4 loop

    """
    A motor car, coming up the road at my back.

    For a moment I let myself hope it is help, sent on ahead of the others.

    I raise a hand and step to the verge to let it pass.

    It does not slow.

    If anything it gathers speed, and it holds straight for me.
    """

    """
    I throw myself towards the trees.

    But the road is wide open, and a man on foot is no match for a motor.

    The car corrects as I move, and the wheels come with me.
    """

    play sound body_fall

    jump captain_ending_run_over
