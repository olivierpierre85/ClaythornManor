# Billiard room — Saturday evening
# Captain enters alone. The evening runs 21:00 → 23:00.
# Each "wait" costs 20 minutes; whoever joins him depends on the time slot
# the wait begins in:
#   21:00 – 21:20 → Miss Marsh (nurse)
#   21:20 – 21:40 → Empty — captain reads, no one comes
#   21:40 – 22:00 → Mr Harring (lad), come down looking for reassurance
#   22:00 – 22:20 → Empty — captain reads, no one comes
#   22:20 – 22:40 → Empty — captain reads, no one comes
#   22:40 – 23:00 → Lady Claythorn (host), packed and ready to leave;
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
                'captain_day2_evening_billiard_room_nurse', 20,
                condition="time_left>100"),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_empty_1', 20,
                condition="time_left>80 and time_left<=100"),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_lad', 20,
                condition="time_left>60 and time_left<=80"),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_empty_2', 20,
                condition="time_left>40 and time_left<=60"),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_empty_3', 20,
                condition="time_left>20 and time_left<=40"),
            TimedMenuChoice('Wait and see who comes',
                'captain_day2_evening_billiard_room_host', 20,
                condition="time_left<=20"),
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
#   Empty waits — captain reads, no one comes
# ------------------------------------
label captain_day2_evening_billiard_room_empty_1:

    """
    I turn back to my book and try to settle to it.

    A page or two go by, easily enough.
    """

    call wait_screen_transition

    """
    The fire shifts in the grate, and the clock on the mantel ticks on.

    Whoever I had thought might come, has not.
    """

    return


label captain_day2_evening_billiard_room_empty_2:

    """
    I read on, though the words come more slowly now.
    """

    call wait_screen_transition

    """
    Nothing stirs in the corridor beyond.

    The house has gone properly quiet.
    """

    return


label captain_day2_evening_billiard_room_empty_3:

    """
    I let the book lie open on my knee and watch the fire awhile instead.
    """

    call wait_screen_transition

    """
    Still no one comes.
    """

    return


# ------------------------------------
#   First slot — Miss Marsh (21:00 – 21:20)
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

    She had every excuse to stay in her room, and yet she chose to come down and see who would be here.

    That is interesting to know.
    """ 

    return


# ------------------------------------
#   Second slot — Mr Harring (21:40 – 22:00)
# ------------------------------------
label captain_day2_evening_billiard_room_lad:

    call captain_day2_evening_billiard_room_wait

    """
    Ted Harring eases the door open and casts his eye round the room before stepping in.

    He goes straight to the bar and pours himself a glass of sherry filled to the brim.

    Then he comes towards me.
    """

    lad """
    Captain. Could I have a word?
    """

    """
    He is making a fair show of being at his ease, but it is plain that he is really scared.
    """

    if (captain_details.threads.is_unlocked('captain_host_suspicion_name')
        and captain_details.threads.is_unlocked('captain_host_suspicion_portrait')
        and captain_details.threads.is_unlocked('captain_host_suspicion_shooting')):

        """
        I have a choice to make here.

        I have seen enough oddities in Lady Claythorn's behaviour to truly suspect something is amiss here.

        I could tell Mr Harring what I found.

        He might prove a useful ally for what may come.

        But if I am wrong to trust him, I might have to pay a high price.
        """

        call run_menu(TimedMenu("captain_day2_evening_billiard_room_lad_menu", [
            TimedMenuChoice("Tell him about your doubts",
                'captain_day2_evening_billiard_room_lad_agree', 0, early_exit=True),
            TimedMenuChoice("Keep pretending everything is fine",
                'captain_day2_evening_billiard_room_lad_dismiss', 0, early_exit=True),
        ]))

    else:

        """
        I am worried about what is happening here as well.

        But I can't really tell him that.
        """

        call captain_day2_evening_billiard_room_lad_dismiss

    return


label captain_day2_evening_billiard_room_lad_dismiss:

    """
    No, I must keep my composure, and act as the tough fighter I am supposed to be.

    That is the safest choice.
    """

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
    You look uneasy, Mr Harring.
    """

    lad """
    Well, I think we have every reason to be, don't you think?
    """

    captain """
    I am afraid you are probably right.
    """

    lad """
    So you also think those deaths are suspicious?
    """

    captain """
    I think so, yes.

    But that is not the worst of it.

    I have learnt things about our host that do not sit well with me.
    """

    lad """
    Really? Such as?
    """

    captain """
    I will spare you the details.
    """

    """
    I do not believe he could understand them in any case.
    """

    captain """
    But I am very confident that our host is not Lady Claythorn, but an impostor.
    """

    lad """
    Really? But why ?

    What does this all mean?
    """

    captain """
    I am afraid I do not know more than this, but I think it is good to know.

    This way we can take precautions during the night.
    """

    lad """
    What sort of precaution?
    """

    captain """
    Be on your guard, Mr Harring.

    Wedge a chair beneath your door if you must, and sleep lightly.

    Come the morning we shall see what can be made of it.

    Do you agree?
    """

    lad """
    Right. It is sensible I suppose Captain.

    If you don't mind, I think I'll head up to my room right away then.
    """

    captain """
    A good idea.

    Goodnight, Mr Harring.
    """

    lad """
    Good night, Captain.
    """

    """
    He goes more steadily than he came.

    Whatever else I have done tonight, I have at least not left him to bear his fears alone.
    """

    return


# ------------------------------------
#   Third slot — Lady Claythorn (22:40 – 23:00)
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
