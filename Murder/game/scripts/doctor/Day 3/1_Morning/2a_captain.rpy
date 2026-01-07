label doctor_day3_morning_captain:

    $ change_room('bedroom_captain', irisout)

    captain """
    Doctor Baldwin.

    Doctor Baldwin, are you awake?
    """

    """
    I slowly open my eyes to find Captain Sinha standing over me.
    """

    doctor """
    Yes, Captain.

    I am awake.
    """

    captain """
    I apologise for the intrusion, Doctor, but it is already well past eight o'clock.

    I believe we should leave the room without delay.
    """

    doctor """
    Very well.

    Give me a moment.
    """

    captain """
    Of course.
    """

    """
    A quick glance at Sushil Sinha tells me he is perfectly prepared.

    I do not know when he woke up, but he must have been waiting for quite some time.
    """

    if doctor_details.threads.is_unlocked('book_opium'):

        """
        In contrast, I must look a terrible sight.

        I have been sweating all night, my body aching for a dose of laudanum.

        Fortunately, I was not in my own room, or I might have relapsed.

        I can only hope that today will be easier.
        """

    captain """
    I suggest we go to the dining room first.

    We should see who is already awake.
    """

    doctor """
    That seems reasonable.
    """

    """
    I make myself as presentable as I can, and we set off together.
    """

    call change_time(9, 0)

    $ change_room('dining_room', dissolve)

    captain """
    This is odd.

    There is no one here.
    """

    doctor """
    And breakfast has not been laid out either.
    """

    captain """
    Which is unusual, considering the hour.
    """

    doctor """
    Indeed.

    Perhaps we should look elsewhere.
    """

    captain """
    I agree.

    The kitchen would be the logical next stop.
    """

    doctor """
    Let us go.
    """

    call change_time(9, 15)

    $ change_room('kitchen', dissolve)

    captain """
    It is completely silent.

    That is not normal.

    Something is very wrong.

    We should proceed with caution and search the house for the others.
    """

    doctor """
    I was thinking the same.
    """

    call change_time(11, 30)

    $ change_room('entrance_hall', dissolve)

    """
    We search the manor methodically for some time.

    Room after room yields nothing, and we begin to lose hope.

    Then, as we descend the stairs to the entrance hall, we hear the faint sound of voices below.
    """

    captain """
    Is anyone here?
    """

    lad """
    Captain Sinha, is that you?
    """

    """
    We look down and spot Ted Harring and Amelia Baxter.
    """

    captain """
    At last, living, breathing souls.

    We were beginning to feel as though we were wandering a ghost house.
    """

    psychic """
    We feel the same.

    You are the first people we have encountered all morning.

    I cannot understand where everyone else could have gone.
    """

    captain """
    Nor can we.
    """

    doctor """
    There is one place we have not checked.

    Miss Marsh's room.
    """

    psychic """
    I knocked earlier.

    There was no answer.

    I tried to enter, but it was locked.
    """

    captain """
    Yes, we received no answer as well.

    I think it is time we check anyway.
    """

    call change_time(11, 40)

    $ change_room('hallway', dissolve)

    """
    We all stand in front of Miss Marsh's room.

    Captain Sinha tests the handle.
    """

    play sound door_locked

    captain """
    Locked.
    """

    captain """
    Miss Marsh?

    Are you inside?
    """

    """
    There is no reply.
    """

    captain """
    Doctor, Mister Harring,

    I believe if the three of us shove together, the door will give way.
    """

    psychic """
    Are you sure it is wise to do this?
    """

    captain """
    I am afraid that under the circumstances, we have no other choice.
    """

    psychic """
    Very well.
    """

    captain """
    Lads, on my command.

    One.

    Two.

    Three.
    """

    play sound door_shut

    """
    The lock gives way and the door swings open.

    We all enter the room.
    """

    $ change_room('bedroom_nurse')

    captain """
    There is nobody here.
    """

    lad """
    So she just vanished?

    Along with half the house?
    """

    captain """
    It would appear so.
    """

    """
    A heavy silence settles over us.
    """

    captain """
    I do not understand what is happening.

    We need to discuss this.
    """

    psychic """
    Of course.

    Perhaps we should settle somewhere more comfortable, like the tea room?
    """

    captain """
    A good idea.
    """

    jump doctor_day3_afternoon

