# ------------------------------------
#               CAPTAIN/NURSE
# ------------------------------------
# Saturday evening - Captain Sinha and Miss Marsh meet in the billiard room.
# Used by:
#   - captain_day2_evening_billiard_room_nurse (linear flow)
#   - nurse_day2_evening_billiard_room_captain_intro
#   - nurse_day2_evening_billiard_room_manning
#   - nurse_day2_evening_billiard_room_captain_key

label common_day2_evening_billiard_room_nurse_captain_intro:

    captain """
    Miss Marsh.

    I thought everyone had retired.
    """

    nurse """
    Not quite yet.

    I am glad you are here captain.

    I would like to talk about something sensitive.

    I hope you don't mind.
    """
    
    captain """
    Not at all.
    """
    nurse """
    Good.

    You see, there are a few things about this weekend that don't make sense to me.
    """

    captain """
    Oh?

    Such as?
    """

    return


label common_day2_evening_billiard_room_nurse_captain_two_deaths_1:

    nurse """
    We've witnessed two deaths in as many days.

    Doesn't it seem strange to you?
    """

    return

label common_day2_evening_billiard_room_nurse_captain_two_deaths_2:

    captain """
    Not really.

    They seem quite natural to me, Miss Marsh.

    Thomas Moody died of injuries he got during the war.

    Even if you thought he was fine, he might have been suffering in silence.

    Some people prefer to hide their distress from the people around them.
    """

    if current_character.text_id == "nurse":

        """
        He looks at me intently as he is saying those words.

        Could it be that he found out about my condition?
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

    if current_character.text_id == "nurse" and nurse_details.threads.is_unlocked('master_key'):

        """
        Especially since I am now in possession of that key.
        """

    return


label common_day2_evening_billiard_room_nurse_captain_key:

    if current_character.text_id == "captain":

        """
        A short pause.

        I do not believe she has finished.
        """

    nurse """
    Do you still have the butler's key with you?
    """

    if current_character.text_id == "captain":

        """
        Now we come to it.

        The key is in my waistcoat pocket.

        I can feel its weight against my ribs.

        I have no intention of telling her so.
        """

    else:

        """
        He sets down his glass and regards me steadily.
        """

    captain """
    Why do you ask?
    """

    nurse """
    Just to reassure myself.

    I won't be able to sleep if I am not absolutely sure that Samuel Manning is properly locked in his room, with no way of escaping.
    """

    if current_character.text_id == "captain":

        """
        A perfectly reasonable answer.

        It is also one that anyone might offer for any number of reasons.
        """

    else:

        """
        He holds my gaze for a moment, then seems to decide the question is reasonable enough.
        """

    captain """
    Of course.

    It is still right here with me.
    """

    if current_character.text_id == "captain":

        """
        I reach into my jacket pocket.

        I let my hand come out empty, and arrange my features into mild surprise.
        """

    else:

        """
        He reaches into his jacket pocket.

        Then stops.

        His hand comes out empty.
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

    return
