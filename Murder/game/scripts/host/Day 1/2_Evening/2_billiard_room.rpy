
label host_day1_evening_billiard_room:

    $ change_room('billiard_room')

    """
    The billiard room is warm, and near enough everyone is in it.

    Miss Marsh stands by the fire, with Mr Moody beside her.

    Mr Harring is standing about at the edge of things, holding his glass as though it might be taken off him.

    Dr Baldwin has found himself a chair.

    Mr Manning has found the bar, which was never in doubt.

    And the butler is in the shadow by the door with his hands folded, missing nothing.

    I head towards Miss Marsh and Mr Moody and strike up a light conversation.

    Soon, I notice Captain Sinha entering the room.

    Talking to him seems the safest option for me.
    """

    call common_day1_evening_billiard_room_captain_invited

    """
    He makes the little show of reluctance that a man makes when he has been waiting all evening to be asked.

    Then he takes up his position by the fireplace and begins.
    """

    call common_day1_evening_captain_billiard_room_speech_part_1

    """
    I let my eyes go round the room while he settles into it.

    I feel it is going to be a long story.

    Good. The less I talk, the better.
    """

    call common_day1_evening_captain_billiard_room_speech_part_2

    """
    He finishes to a small, warm silence.
    """

    host """
    Thank you, Captain. I doubt any of us will forget it.

    Now, if you will excuse me, it has gotten rather late.
    
    I should head back to my room for the night.
    """

    """
    The others follow my lead.
    """

    $ host_details.threads.unlock('stayed_with_guests')

    return
