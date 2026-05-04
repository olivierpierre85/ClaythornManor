# Billiard room — Saturday evening
# Captain enters alone and waits to see who, if anyone, will join him.
label captain_day2_evening_billiard_room:

    $ change_room('billiard_room')

    if not captain_details.saved_variables["day2_evening_billiard_room_visited"]:

        $ captain_details.saved_variables["day2_evening_billiard_room_visited"] = True

        """
        The billiard room is lit much as it was last night, but the warmth of the place has gone out of it.

        The decanters stand untouched on the side.

        The glasses have been laid out in expectation of a company that has chosen not to come.

        I am quite alone.
        """

        call run_menu(TimedMenu("captain_day2_evening_billiard_room_menu", [
            TimedMenuChoice('Wait and see who comes', 'captain_day2_evening_billiard_room_wait', 0, early_exit=True),
            TimedMenuChoice('Pour a glass of sherry', 'captain_day2_evening_billiard_room_sherry', 0, early_exit=True),
            TimedMenuChoice('Leave the room', 'generic_cancel', 0, early_exit=True),
        ]))

    else:

        """
        I am back in the billiard room.

        The chairs sit much as I left them.
        """

    return


label captain_day2_evening_billiard_room_wait:

    """
    I take down a book from the shelf and settle into a chair by the fire.

    A man waiting in a public room with no occupation is conspicuous.

    A man with a book, far less so.
    """

    call captain_day2_evening_billiard_room_nurse

    return


label captain_day2_evening_billiard_room_sherry:

    """
    I cross to the sideboard and pour a small measure of sherry from one of the decanters.

    The glass is good crystal, the sherry darker than I would have chosen for myself, but it will do.

    I take down a book from the shelf as I pass and settle into a chair by the fire.
    """

    call captain_day2_evening_billiard_room_nurse

    return


label captain_day2_evening_billiard_room_nurse:

    """
    A few minutes pass before the door eases open behind me.

    Miss Marsh hesitates a moment in the doorway, then crosses the room with her usual quiet composure.

    She has spent most of the evening at the hostess's elbow.

    Whatever has brought her here, it was not for the company of the decanters.
    """

    captain """
    Miss Marsh.

    I thought everyone had retired.
    """

    nurse """
    Not quite yet.

    There are a few things about this weekend that don't make sense to me.
    """

    captain """
    Oh?

    Such as?
    """

    nurse """
    We've witnessed two deaths in as many days.

    Doesn't it seem strange to you?
    """

    """
    A direct question, asked very simply.

    A man with nothing to hide would dismiss it without a second thought.

    So I shall do precisely that.
    """

    captain """
    Not really.

    They seem quite natural to me, Miss Marsh.

    Thomas Moody died of injuries he got during the war.

    Even if you thought he was fine, he might have been suffering in silence.

    Some people prefer to hide their distress from the people around them.
    """

    nurse """
    But for Doctor Baldwin?
    """

    captain """
    A dreadful accident, Miss Marsh.

    Manning was drunk and careless with a firearm.

    Sadly, this type of tragic event is not rare at all.

    Although some people treat it as a light form of entertainment, a hunt is a dangerous business.
    """

    nurse """
    Perhaps you are right.

    Still, I confess I am uneasy knowing Samuel Manning is just upstairs.

    A few steps from my own room.

    Are we sure he cannot get out?
    """

    captain """
    Quite sure.

    I locked the door myself, with the key the butler gave me.

    The doors in this house are solid oak.

    He is going nowhere.
    """

    nurse """
    That is reassuring.
    """

    """
    A short pause.

    I do not believe she has finished.
    """

    nurse """
    Do you still have the butler's key with you?
    """

    """
    Now we come to it.

    The key is in my waistcoat pocket.

    I can feel its weight against my ribs.

    I have no intention of telling her so.
    """

    captain """
    Why do you ask?
    """

    nurse """
    Just to reassure myself.

    I won't be able to sleep if I am not absolutely sure that Samuel Manning is properly locked in his room, with no way of escaping.
    """

    """
    A perfectly reasonable answer.

    It is also one that anyone might offer for any number of reasons.
    """

    captain """
    Of course.

    It is still right here with me.
    """

    """
    I reach into my jacket pocket.

    I let my hand come out empty, and arrange my features into mild surprise.
    """

    captain """
    Blast.

    I had it earlier, but it is in my hunting coat.

    Upstairs, in my room.

    I changed for dinner and left it in the pocket.
    """

    nurse """
    I see.
    """

    captain """
    You shouldn't worry.

    I locked my room with my own key.

    It is safe there.
    """

    nurse """
    Good.
    """

    """
    She regards me a moment longer than I should like.

    She did not believe a word of it.

    But she knows better than to press me on it tonight.
    """

    nurse """
    Good night, Captain.
    """

    captain """
    Good night, Miss Marsh.
    """

    """
    She withdraws as quietly as she came.

    The door clicks shut behind her, and the room is mine again.

    Whatever questions she came in with, she has gone away with most of them.

    But not all.
    """

    return
