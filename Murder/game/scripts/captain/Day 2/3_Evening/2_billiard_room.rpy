# Billiard room — Saturday evening
# Captain enters alone. The evening runs 21:00 → 23:00.
# Each "wait" costs 40 minutes; whoever joins him depends on the time slot
# the wait begins in:
#   21:00 – 21:40 → Miss Marsh (nurse)
#   21:40 – 22:20 → Mr Harring (lad), come down looking for reassurance
#   22:20 – 23:00 → Lady Claythorn (host), packed and ready to leave;
#                   with all three host suspicions, a final chance to accuse her.
# A captain who lingers elsewhere first will simply miss earlier visitors.
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

        $ captain_day2_evening_billiard_room_menu = TimedMenu("captain_day2_evening_billiard_room_menu", [
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_nurse', 40,
                condition="time_left>80"),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_lad', 40,
                condition="time_left>40 and time_left<=80"),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_host', 40,
                condition="time_left<=40"),
            TimedMenuChoice('Pour a glass of sherry',
                'captain_day2_evening_billiard_room_sherry', 10),
            TimedMenuChoice('Leave the room',
                'generic_cancel', 0, keep_alive=True, early_exit=True),
        ])

    else:

        """
        I am back in the billiard room.

        The chairs sit much as I left them.
        """

        $ captain_day2_evening_billiard_room_menu.early_exit = False

    call run_menu(captain_day2_evening_billiard_room_menu)

    return


label captain_day2_evening_billiard_room_sherry:

    """
    I cross to the sideboard and pour a small measure of sherry from one of the decanters.

    The glass is good crystal, the sherry darker than I would have chosen for myself, but it will do.
    """

    return

label captain_day2_evening_billiard_room_wait:

    if captain_details.saved_variables["day2_evening_billiard_encounters"] == 0:

        """
        I take down a book from the shelf and settle into a chair by the fire.
        """

        call wait_screen_transition

    elif captain_details.saved_variables["day2_evening_billiard_encounters"] == 1:

        """
        I turn another page, more for the look of the thing than to read.
        """

        call wait_screen_transition

        """
        After a little while the door opens a second time.
        """

    else:

        """
        It is getting late, yet I feel like I could wait a little more.
        """

        call wait_screen_transition

        """
        The door opens a third time — and stops short.
        """

    $ captain_details.saved_variables["day2_evening_billiard_encounters"] += 1
    
    return

# ------------------------------------
#   First slot — Miss Marsh (21:00 – 21:40)
# ------------------------------------
label captain_day2_evening_billiard_room_nurse:

    call captain_day2_evening_billiard_room_wait

    """
    A few minutes pass before the door eases open behind me.

    Rosalind Marsh hesitates a moment in the doorway, then crosses the room with her usual quiet composure.
    """

    call common_day2_evening_billiard_room_nurse_captain_intro

    call common_day2_evening_billiard_room_nurse_captain_two_deaths

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
    
    I wonder what made a middle-aged nurse risk coming downstairs tonight.

    She had every excuses to stay in her room and yet she decided to check on who would be there.

    That is interesting to know.
    """ 

    return


# ------------------------------------
#   Second slot — Mr Harring (21:40 – 22:20)
# ------------------------------------
label captain_day2_evening_billiard_room_lad:

    call captain_day2_evening_billiard_room_wait

    """
    Ted Harring eases the door open and casts his eye round the room before stepping in.

    He crosses to the chair opposite mine with a careful, studied air, and seats himself.
    """

    lad """
    Captain. Could I have a word?
    """

    """
    He has come down here for a reason.

    He is making a fair show of being at his ease, but it is plainly costing him something.

    The question is whether I mean to give him what he came for, or send him back upstairs none the wiser.
    """

    if (captain_details.threads.is_unlocked('captain_host_suspicion_name')
        and captain_details.threads.is_unlocked('captain_host_suspicion_portrait')
        and captain_details.threads.is_unlocked('captain_host_suspicion_shooting')):

        call run_menu(TimedMenu("captain_day2_evening_billiard_room_lad_menu", [
            TimedMenuChoice("Tell him he is right to be uneasy",
                'captain_day2_evening_billiard_room_lad_agree', 0, early_exit=True),
            TimedMenuChoice("Hold the line — nothing is amiss",
                'captain_day2_evening_billiard_room_lad_dismiss', 0, early_exit=True),
        ]))

    else:

        call captain_day2_evening_billiard_room_lad_dismiss

    return


label captain_day2_evening_billiard_room_lad_dismiss:

    call common_day2_evening_billiard_room_lad_captain_dismiss

    """
    He looks at me a moment longer than is comfortable.

    Whatever he came for, he is not going to get it from me tonight.
    """

    call common_day2_evening_billiard_room_lad_captain_close

    """
    He drains his glass and withdraws without another word.

    A young man can be told a great many things, if one is firm about it.

    Whether it does him any good is another matter.
    """

    return


label captain_day2_evening_billiard_room_lad_agree:

    captain """
    You are right to be uneasy, Mr Harring.

    I have been turning the day over in my own mind, and the more I do, the less it sits well with me.
    """

    lad """
    So you do think there's something behind it?
    """

    captain """
    I think there is rather more behind it than any of us can yet account for.

    But it is gone eleven of the clock, and the house is shut up for the night.

    Whatever has been set in motion here, we shall not unpick it now.
    """

    lad """
    Then what should we do?
    """

    captain """
    Be on your guard, Mr Harring.

    Wedge a chair beneath your door if you must, and sleep lightly.

    There is precious little more to be done at this hour.

    Come the morning we shall see what can be made of it.
    """

    lad """
    Right. Goodnight then, Captain.
    """

    captain """
    Goodnight, Mr Harring.
    """

    """
    He goes more steadily than he came.

    Whatever else I have done tonight, I have at least not left the lad to bear his fears alone.
    """

    return


# ------------------------------------
#   Third slot — Lady Claythorn (22:20 – 23:00)
# ------------------------------------
label captain_day2_evening_billiard_room_host:

    call captain_day2_evening_billiard_room_wait

    """
    Lady Claythorn is on the threshold, and the sight of me has brought her up at once.

    For an instant her face is quite undefended.

    Her travelling coat is buttoned to the throat. A small leather case stands at her feet.

    She had not expected to find anyone in this room.
    """

    host """
    Captain.

    I... did not realise anyone was still up.
    """

    captain """
    Evidently.
    """

    """
    She recovers herself with admirable speed, but the case at her feet is not so easily concealed.

    Wherever she had thought to be at this hour, it was not in the manor.
    """

    if (captain_details.threads.is_unlocked('captain_host_suspicion_name')
        and captain_details.threads.is_unlocked('captain_host_suspicion_portrait')
        and captain_details.threads.is_unlocked('captain_host_suspicion_shooting')):

        """
        And here, plainly, is what I have been waiting for the whole evening.

        Her name is not her own.

        Her portrait is nowhere to be found in the gallery.

        She cannot shoot, nor keep a proper table.

        And now she stands before me, packed and bound for the door at near eleven of the clock, with two of her guests dead beneath her roof.

        If I am to put it to her, it must be now.
        """

        call run_menu(TimedMenu("captain_day2_evening_billiard_room_host_menu", [
            TimedMenuChoice("Confront her with what I know",
                'captain_day2_evening_billiard_room_host_accuse', 0, early_exit=True),
            TimedMenuChoice("Let her go and say nothing",
                'captain_day2_evening_billiard_room_host_silent', 0, early_exit=True),
        ]))

    else:

        host """
        I had thought to take a turn outside before retiring.

        The air has been so close in the house all day.
        """

        captain """
        Of course, Lady Claythorn.
        """

        """
        It is a poor lie, told with a packed case at her feet.

        But I have not enough in hand to challenge her on it.

        She gathers up her case and is gone before I have set down my book.
        """


    return


label captain_day2_evening_billiard_room_host_accuse:

    captain """
    Forgive me, my lady. Before you go, there is a matter I should put to you.
    """

    host """
    At this hour, Captain?
    """

    captain """
    At this hour, with your case at your feet, yes.

    There is no portrait of you in the gallery upstairs. Not one.

    You are styled Lady Claythorn, and yet Claythorn is the name of the house, not of any title I have ever heard of.

    On the hunt this morning you handled a rifle as no shooting woman would.

    And tonight, with two of your guests dead beneath your roof, you are dressed for the road.
    """

    """
    She is very still.

    For a long moment she does not answer at all.

    Then she sets the case down again, very deliberately, and meets my eye.
    """

    host """
    You are an observant man, Captain.

    Rather more observant than was wanted here.
    """

    captain """
    Who are you, my lady?
    """

    host """
    No one in particular.

    A woman who was paid handsomely to play a part for a weekend, and who now finds the part has run rather beyond her contract.
    """

    captain """
    Paid by whom?
    """

    host """
    That, Captain, I am not going to tell you.

    And I would advise you very strongly not to press the question further tonight.
    """

    """
    She lifts her case once more.
    """

    host """
    I should sit by the fire if I were you, Captain. Finish your book.

    Whatever has been arranged for this house, it is not arranged for you.

    Not yet.
    """

    """
    She withdraws without another word, and the door clicks shut behind her.

    A confession of sorts, even if she did not name a name.

    I have not stopped her. I doubt very much I could have.

    But I have had it from her own mouth that she is not what she has claimed to be.

    That, at least, is something to take into the morning.
    """

    return


label captain_day2_evening_billiard_room_host_silent:

    """
    I let her go.

    A packed case and a startled face are not enough to set against a hostess in her own house, not at near eleven at night, not with the only other witnesses asleep upstairs.

    She gathers the case and goes without another word.

    Whatever I might have asked her, the moment is past.
    """

    return
