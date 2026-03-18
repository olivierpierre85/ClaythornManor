# --------------------------------------------
#   Nurse
#
#   Sunday - Morning
#
#   8:30 -> 12:00
#
#   Music: mysterious
#
#   Position
#       - House: lad, captain, psychic, doctor, nurse
#       - Dead : broken, drunk
#       -? : Host
#
#   Notes :
#       - No more maps
#   Useful Threads:
# --------------------------------------------
label nurse_day3_morning:

    call change_time(8, 30, "Morning", "Sunday", hide_minutes=True, chapter='sunday_morning')

    $ nurse_details.add_checkpoint("nurse_day3_morning")

    call black_screen_transition("Rosalind Marsh", chapters_names[current_chapter])

    $ change_room("bedroom_nurse", irisout)

    $ play_music('mysterious', 2)

    if nurse_details.threads.is_unlocked('day1_exhaustion') or nurse_details.threads.is_unlocked('day2_exhaustion'):

        play sound woman_cough

        """
        I wake already spent.

        A cough finds me before I am properly conscious, which is its usual way.

        I press the handkerchief to my lips and wait for it to pass.

        More blood this morning.

        I fold the cloth away and sit on the edge of the bed until my head clears.

        I have been pushing myself too hard.

        I knew it, and I did it regardless.

        That will not do. Not today.

        Today, of all mornings, I need to think clearly.
        """

    else:

        """
        I wake to silence.

        Not the ordinary silence of a sleeping house — something stiller than that.

        I lie for a moment, listening.

        Nothing moves below.

        I sit up.
        """

    """
    I wash and dress methodically.

    Whatever this morning holds, it is better faced upright and properly buttoned.

    I head down to have breakfast.
    """

    call change_time(8, 45)

    $ change_room("dining_room", dissolve)

    """
    The dining room is empty.

    Not merely quiet — empty in a way that stops me in the doorway.

    The grates are cold. No breakfast has been laid. The table stands exactly as it was left after last night's dinner.

    Not a maid, not a footman. Not a sound from the kitchen.

    I walk to the window and look out at the grounds.

    Nobody there either.

    Something is wrong.

    And perhaps I have known it, in some quieter part of my mind, since the moment I read that letter on the train.

    There is no prize here. There never was.

    Whatever this weekend is truly about, it has moved well beyond the point of pretending otherwise.

    I should have acted sooner.

    I may be running out of time.
    """

    $ change_room("entrance_hall", dissolve)

    """
    I cross to the entrance hall and look about.

    No one.

    I stand in the middle of the room.

    Then something catches my eye.

    On the small side table beside the front door, placed neatly — deliberately, I think — is a key on a plain chain.

    I pick it up.

    It is small and well-worn, with the heft of something often used.
    """

    if nurse_details.saved_variables.get('visited_attic_butler_room', False):

        """
        I turn it over.

        A master key, by the look of it — the kind a head of household staff would carry.

        I think of the reinforced cabinet in the butler's room.

        The silver gleaming behind the glass.

        I could not get at it before.

        I rather think I could now.
        """

    else:

        """
        I turn it over.

        It has the look of a household master key — well-used, heavier than it appears.

        The sort that opens every room in a house this size.

        A butler of this standing would keep his own cabinet somewhere.

        Most of them do.

        Somewhere in his bedroom, most likely.
        """

    call nurse_day3_morning_creak

    if nurse_details.threads.is_unlocked('silverware_big'):


        jump nurse_day3_morning_leave_rich

    """
    And they will be coming downstairs before long.

    I slip the key into my coat pocket.

    I cannot afford to be found standing here.

    Yet I am not certain it is wise to use it.

    Every moment I remain is a risk.

    Perhaps the wisest course is simply to go.
    """

    $ time_left = 1
    call run_menu(TimedMenu("nurse_day3_morning_choice", [
        TimedMenuChoice("Leave now, while there is still time", 'nurse_day3_morning_leave', early_exit=True),
        TimedMenuChoice("Go check the butler's room first", 'nurse_day3_morning_attic', early_exit=True),
    ]))


    return


label nurse_day3_morning_leave:

    """
    I take my coat from the stand.

    I do not hesitate.

    I open the front door and step outside.
    """

    $ change_room("manor_exterior", dissolve)

    """
    The air is cold and wet, the drive still damp from the night.

    I walk quickly, without looking back at the house.

    There will be no prize. There was never going to be one.

    I have understood that for some time now, and yet I stayed.

    The gate at the end of the drive. Eyes on that, and nothing else.
    """

    $ change_room("forest_road", dissolve)

    """
    The road stretches ahead, quiet and grey beneath the morning cloud.

    I keep walking.

    There is nothing behind me worth turning back for.
    """

    jump nurse_ending_escape_poor


label nurse_day3_morning_leave_rich:

    """
    I look at the key on the table.

    I do not need it. I have already taken what I came for.

    The silver is in my bag, along with everything else I gathered this weekend.

    There is nothing left to wait for.
        
    I take my coat from the stand.

    I do not hesitate.

    I open the front door and step outside.
    """

    $ change_room("manor_exterior", dissolve)

    """
    The air is cold and sharp, but I scarcely feel it.

    My bag is heavy on my shoulder — heavier than it has any right to be.

    I walk quickly down the drive, my heels crunching on the gravel.

    I do not look back.
    """

    $ change_room("forest_road", dissolve)

    """
    The road stretches ahead, quiet and grey beneath the morning cloud.

    But for the first time in a very long while, I am not afraid of what lies at the end of it.

    I have enough now. Enough to settle somewhere. Enough to see a proper doctor.

    Enough to hope.
    """

    jump nurse_ending_escape_rich


label nurse_day3_morning_creak:

    """
    Above me, floorboards creak.

    I go still.

    Then another creak, further along the upper corridor.

    Someone is up, and moving.
    """

    return
