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

        Hopefully, I can still hold on until the end of the day.
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

    I make my way downstairs for breakfast.
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

    I turn it over.
    """

    if nurse_details.threads.is_unlocked('master_key'):

        """
        Another master key.

        I already hold one. I have no need for a second.

        Though I wonder why this one was left here so openly.

        I set it back down.
        """

    else:

        """
        A master key, by the look of it — the kind a head of household staff would carry.

        The sort that opens every door in the house.
        """

        if nurse_details.saved_variables['visited_attic_butler_room']:

            """
            My mind goes directly to the butler's room — that reinforced cabinet.

            A lock like that does not guard trinkets.

            This key might be exactly what I need.
            """

        else:

            """
            Normally, I would not need such a key. I can open most anything with a hairpin and patience.

            But a butler keeps a household's valuables under proper lock and key — the sort that resists my usual methods.

            His room would be worth a visit.
            """
        
        """
        I slip the key into my coat pocket.
        """

    """
    Above me, floorboards creak.

    I go still.

    Then another creak, further along the upper corridor.

    Someone is up, and moving.

    And they will be coming downstairs before long.

    I cannot afford to be found standing here.

    Every moment I remain is a risk.
    """

    if nurse_details.threads.is_unlocked('silverware_big'):

        """
        I have already taken what I came for.

        The silver is in my bag, along with everything else I gathered this weekend.

        There is nothing left to stay for.
        """
        
    $ time_left = 1
    call run_menu(TimedMenu("nurse_day3_morning_choice_rich", [
        TimedMenuChoice("Go check the butler's room first", 'nurse_day3_morning_attic', early_exit=True, condition="not nurse_details.threads.is_unlocked('silverware_big')"),
        TimedMenuChoice("Get your things from your room and leave", 'nurse_day3_morning_room_nap', early_exit=True, condition="nurse_details.threads.is_unlocked('silverware_big')"),
        TimedMenuChoice("Leave now, without wasting another second!{{intuition}}", 'nurse_day3_morning_leave', early_exit=True, condition="nurse_details.endings.is_unlocked('escape_at_night')"),
    ]))

    return


label nurse_day3_morning_leave:


    """
    An irrational feeling overtakes me.

    I know I should prepare more before attempting the long journey back.

    But a deep-rooted fear prevents me from getting to my room.

    No. I need to leave now — there is no time to waste.
    """

    if nurse_details.threads.is_unlocked('silverware_big'):

        """
        At least I have the valuables I acquired with me in my bag.
        """

    """
    I take my coat from the stand.

    I open the front door and step outside.
    """

    $ change_room("manor_exterior", dissolve)

    """
    The air is cold and sharp, but I scarcely feel it.
    """

    if nurse_details.threads.is_unlocked('silverware_big'):

        """
        My bag is heavy on my shoulder — heavier than it has any right to be.
        """

    """
    I walk quickly down the drive, my heels crunching on the gravel.

    I do not look back.

    There will be no prize. There was never going to be one.

    I have understood that for some time now, and yet I stayed.

    The gate at the end of the drive. Eyes on that, and nothing else.
    """

    $ change_room("forest_road", dissolve)

    #TOO: Maybe not very useful ending? Maybe if you were exhausted you are forced to take a nap ???
    if nurse_details.threads.is_unlocked('day1_exhaustion') or nurse_details.threads.is_unlocked('day2_exhaustion'):

        if nurse_details.threads.is_unlocked('silverware_big'):

            """
            The road stretches ahead, and the bag grows heavier with every step.

            I should drop some of the silver. I know that. But I cannot bring myself to part with it.

            My legs falter beneath the weight — of the bag, of the illness, of everything I have put my body through.
            """

        else:

            """
            The road stretches ahead, quiet and grey beneath the morning cloud.

            I keep walking — or I try to.

            My legs feel heavier with every step.

            I should not have pushed myself so hard these past days.
            """

        play sound woman_cough

        if nurse_details.threads.is_unlocked('silverware_big'):

            """
            The cough takes hold, and this time it does not let go.

            I sink to my knees on the wet road, the bag spilling open beside me.

            All that silver, scattered in the mud.

            What a waste.
            """

        else:

            """
            The cough takes hold, and this time it does not let go.

            I stumble.

            The road swims before my eyes.
            """

        jump nurse_ending_escape_collapse

    """
    The road stretches ahead, quiet and grey beneath the morning cloud.
    """

    if nurse_details.threads.is_unlocked('silverware_big'):

        # No need for pearls now, too complicated
        # if nurse_details.threads.is_unlocked('steal_pearls'):

        """
        But for the first time in a very long while, I am not afraid of what lies at the end of it.

        The silver, the pearls — together, they are worth a good deal more than I dared hope.

        Enough to settle somewhere. Enough to see a proper doctor.

        Enough to hope.
        """

        jump nurse_ending_escape_rich
        
        # else:

        #     """
        #     I run the figures in my head again. The candlesticks, the salver, the spoons.

        #     It is something. But not enough. Not nearly enough.

        #     If only I had taken something else — one more item of real value, and I might have had enough.

        #     That thought will haunt me, I think.
        #     """

        #     jump nurse_ending_escape_poor

    else:

        """
        I keep walking.

        There is nothing behind me worth turning back for.
        """

        jump nurse_ending_escape_poor
