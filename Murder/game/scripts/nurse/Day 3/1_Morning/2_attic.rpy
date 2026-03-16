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
