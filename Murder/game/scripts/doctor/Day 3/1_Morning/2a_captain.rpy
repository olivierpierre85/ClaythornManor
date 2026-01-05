label doctor_day3_morning_captain:

    $ change_room('bedroom_captain', irisout)

    # Wake up in Captain's room. You follow him exploring but find NOTHING, until you find LAD and psychic => YOU leave with captain !!!!!!

    # """
    # Captain path? Following him, discuss suspects, leave as soon as possible.

    # Meet the others PSYCHIC + LAD =>

    # Copy paste other dialogs until choice to GET out or STAY?

    #     IF STAY, the nurse doesn't show up, you die poisoned anyway?

    #     IF leave you ESCAPE???????

    # ALSO learn about the Boxer's rebellion !! Help for possible unlocking!!!! => Notice that the nurse was unstable back then? Maybe too suspicious
    # """

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

    Room after room yields nothing and We were starting to lose hope.

    But as we were going down the stairs to the entrance hall, we heard a faint discussion coming.
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

    We were starting to feel like we were in a ghost house.
    """

    psychic """
    We feel the same. You're the first person we've encountered today as well.
    """

    #Discussion, about where to go next, conclusion that we have seen every room but Miss Marsh

    # THey all go together, as there are no reason to suspect foul play. 
    # BUT the captain doesn't have a key now so they 


    # He leaves and is free? USE the car if you see the key in ANDREW's ROOM ?

    return
