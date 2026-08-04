# Billiard room, Friday evening, from the head of the room rather than the door.
#
# The same gathering the Captain and Thomas Moody attend, seen by the woman who
# is supposed to be giving it. She calls Sinha over, Miss Marsh asks for a
# story, and the Boxer Rebellion carries the rest of the evening for her.
# Sitting up with them unlocks stayed_with_guests. Never coming at all is what
# costs her a mark at the end of the chapter (see 1_main.rpy).

label host_day1_evening_billiard_room:

    $ change_room('billiard_room')

    if host_details.saved_variables['day1_evening_billiard_room_visited']:

        """
        I look in on them again.

        The fire has been made up, the glasses are full, and nobody wants anything from me but my presence.

        I can do presence.
        """

        return

    $ host_details.saved_variables['day1_evening_billiard_room_visited'] = True

    """
    The billiard room is warm, and near enough everyone is in it.

    Miss Marsh has taken the chair by the fire and Mr Moody the one beside her. Mr Harring is standing about at the edge of things, holding his glass as though it might be taken off him.

    Dr Baldwin has found a corner and a bottle. Mr Manning has found the bar, which was never in doubt.

    And the butler is in the shadow by the door with his hands folded, missing nothing.

    I take the seat they leave for me, and the room arranges itself around it.

    That is the part nobody warns you about. They give you the best chair without thinking, and you have to take it without thinking too.

    Captain Sinha comes in last.
    """

    call common_day1_evening_billiard_room_captain_invited

    """
    He makes the little show of reluctance that a man makes when he has been waiting all evening to be asked.

    Then he takes up his position by the fireplace, and I mean position.

    Feet apart, weight back, the glass held where his hands can be seen.

    Whoever taught him did a thorough job.
    """

    call common_day1_evening_captain_billiard_room_speech_part_1

    """
    I let my eyes go round the room while he settles into it.

    Miss Marsh is watching him rather harder than the story requires. Mr Moody has not moved at all.

    Mr Manning is at the bar with his back to the whole performance, and I find I am no longer certain he is not listening to every word.

    Then I put my chin on my hand and give the captain my whole face, because that is what I am for tonight.
    """

    call common_day1_evening_captain_billiard_room_speech_part_2

    """
    He finishes to a small, warm silence, which is the only applause a room like this gives.

    It was well told. That is what strikes me.

    Not well remembered. Well told.

    The pauses fall in the same places a good speech puts them, and the awful parts come exactly where an audience is ready for them.

    Every man tells his war twice, I suppose. The second time it has become a piece.
    """

    host """
    Thank you, Captain. I doubt any of us will forget it.
    """

    """
    The evening loosens after that. Somebody proposes billiards, somebody else pours, and for the best part of an hour I am nothing more than a woman being agreeable in a warm room.

    It is the easiest work I have ever been paid for, and it frightens me more than the speech did.

    Because I can feel how much I like it.

    I catch the butler's eye once, in the shadow by the door.

    There is a great deal I should like to ask him, and not one of it can be asked here.
    """

    $ host_details.threads.unlock('stayed_with_guests')

    return
