label nurse_day3_morning_stay:

    """
    I press myself to the back of the hall as the footsteps grow closer.

    Ted Harring and Amelia Baxter descend the stairs and move through to the dining room without glancing my way.

    I waste no time.

    The service stairs are at the far end of the corridor.
    """

    return


label nurse_day3_morning_room_nap:

    call nurse_day3_morning_stay
    
    call nurse_day3_morning_room_grab_belongings
    
label nurse_day3_morning_attic:

    call nurse_day3_morning_stay

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

    I ease the bedroom door closed behind me, and return to my room discretely.
    """

    $ nurse_details.objects.unlock('silverware_big')

    jump nurse_day3_morning_room_grab_belongings


label nurse_day3_morning_room_grab_belongings:

    $ change_room("bedroom_nurse", dissolve)

    """
    I gather my few belongings, lock the door, and get ready to leave.

    My legs are weak. My chest aches.

    If I attempt the walk to the village now, I will not make it. I know that.

    I need to rest. Just a short nap before I make the journey.

    I settle on the edge of the narrow bed and fold my hands.

    I lie fully clothed upon the bed.

    I close my eyes.
    """

    jump nurse_day3_afternoon

    return
