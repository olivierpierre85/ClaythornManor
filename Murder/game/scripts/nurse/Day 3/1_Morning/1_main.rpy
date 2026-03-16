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
#       - Knows about footman
# --------------------------------------------
label nurse_day3_morning:

    call change_time(8, 30, "Morning", "Sunday", hide_minutes=True, chapter='sunday_morning')

    $ nurse_details.add_checkpoint("nurse_day3_morning")

    call black_screen_transition("Rosalind Marsh", chapters_names[current_chapter])

    $ change_room("bedroom_nurse", irisout)

    $ play_music('mysterious')

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

    """
    Above me, floorboards creak.

    I go still.

    Then another creak, further along the upper corridor.

    Someone is up, and moving.

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

    jump nurse_day3_afternoon


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


label nurse_day3_morning_attic:

    """
    I press myself to the back of the hall as the footsteps grow closer.

    Ted Harring and Amelia Baxter descend the stairs and move through to the dining room without glancing my way.

    I waste no time.

    The service stairs are at the far end of the corridor.

    Up to the attic.
    """

    $ change_room("attic_hallway")

    """
    The attic corridor is narrow and very still.

    Dust on every surface.

    The staff quarters line the passage, their doors all shut.

    No sound from behind any of them.

    The whole house might as well be empty.

    At the far end of the hallway, I find the butler's room.
    """

    $ change_room("butler_room")

    if nurse_details.saved_variables.get('visited_attic_butler_room', False):

        """
        I have been here before.

        The reinforced cabinet stands where it always stood, waiting.
        """

    else:

        $ nurse_details.saved_variables["visited_attic_butler_room"] = True

        call nurse_butler_room_first_visit

    """
    I take the key from my pocket and fit it into the cabinet lock.

    It turns without effort.

    The doors swing open.

    No bearer bonds. But then I never truly believed in those.

    The silver is real though.

    A pair of candlesticks, a salver, a set of heavy serving spoons.

    Not a fortune, by any standard. But it is something.

    That will make this weekend a profitable one, at least.

    I take what will fit without making my bag unmanageable.

    Then I close the cabinet as best I can and step back.

    I ease the bedroom door closed behind me.

    Nobody should have cause to come in here now.

    There is nothing to do but wait.

    I settle on the edge of the narrow bed and fold my hands.

    Somewhere below me, the others are waking, moving through the house, drawing their own conclusions.

    When they look for me, they will find an empty room.

    Good. Let them wonder.

    I shall stay up here until things have quietened, then slip out this afternoon when no one is watching the drive.

    It is not the ideal plan.

    But it is the plan I have, and it will have to do.
    """

    jump nurse_day3_afternoon
