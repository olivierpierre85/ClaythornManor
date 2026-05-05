# Billiard room — Saturday evening
# Captain enters alone. He may wait up to three times to see who joins him:
#   first wait  → Miss Marsh (nurse)
#   second wait → Miss Baxter (psychic)
#   third wait  → Lady Claythorn (host) — packed and ready to leave; if all
#                three host suspicions are unlocked, a final chance to accuse her.
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
                condition='captain_details.saved_variables["day2_evening_billiard_waited"] == 0'),
            TimedMenuChoice('Wait further to see who else may come',
                'captain_day2_evening_billiard_room_psychic', 40,
                condition='captain_details.saved_variables["day2_evening_billiard_waited"] == 1'),
            TimedMenuChoice('Wait one last time',
                'captain_day2_evening_billiard_room_host', 40,
                condition='captain_details.saved_variables["day2_evening_billiard_waited"] == 2'),
            TimedMenuChoice('Pour a glass of sherry',
                'captain_day2_evening_billiard_room_sherry', 10),
            TimedMenuChoice('Leave the room',
                'generic_cancel', 0, keep_alive = True, early_exit=True),
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


# ------------------------------------
#   First encounter — Miss Marsh
# ------------------------------------
label captain_day2_evening_billiard_room_nurse:

    $ captain_details.saved_variables["day2_evening_billiard_waited"] = 1

    """
    I take down a book from the shelf and settle into a chair by the fire.
    """

    call wait_screen_transition

    """
    A few minutes pass before the door eases open behind me.

    Miss Marsh hesitates a moment in the doorway, then crosses the room with her usual quiet composure.

    Whatever has brought her here, it was not for the company of the decanters.
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
    """

    return


# ------------------------------------
#   Second encounter — Miss Baxter
# ------------------------------------
label captain_day2_evening_billiard_room_psychic:

    $ captain_details.saved_variables["day2_evening_billiard_waited"] = 2

    """
    I turn another page, more for the look of the thing than to read.
    """

    call wait_screen_transition

    """
    The door opens a second time.

    Miss Baxter pauses on the threshold and surveys the room before stepping in.

    She crosses to the sideboard and pours herself a small glass with the air of one who is glad to have something to do with her hands.
    """

    psychic """
    Captain.

    I had thought I should find the room empty.
    """

    captain """
    Miss Baxter.

    Please, sit by the fire if you wish.
    """

    """
    She lowers herself into the chair opposite mine and rests her glass upon her knee.

    Her composure is admirable, but it is composure all the same. The sort one puts on, like a coat.
    """

    psychic """
    A dreadful day, Captain.

    Two of our number gone, and that poor man locked above stairs.
    """

    captain """
    A dreadful day, indeed.
    """

    psychic """
    I confess I do not feel quite easy in my own room tonight.

    I cannot help wondering whether we are as safe as our hostess assures us.
    """

    """
    A careful question, asked very lightly.

    I do not wish to give her more than she has come for.
    """

    captain """
    The doors of this house are solid oak, Miss Baxter.

    And Mr Manning is locked behind one of them.

    I should not lose any sleep on his account.
    """

    psychic """
    No.

    No, I daresay you are right.
    """

    """
    She does not look as though she believes me.

    She finishes her sherry in two small sips and rises.
    """

    psychic """
    Forgive me, Captain. I find I am more tired than I had thought.
    """

    captain """
    Of course. Sleep well, Miss Baxter.
    """

    """
    She inclines her head and withdraws.

    She came down looking for reassurance, and I have given her precious little of it.

    I doubt very much that she will sleep tonight.
    """

    return


# ------------------------------------
#   Third encounter — Lady Claythorn
# ------------------------------------
label captain_day2_evening_billiard_room_host:

    $ captain_details.saved_variables["day2_evening_billiard_waited"] = 3

    """
    I had nearly given up on company for the night.
    """

    call wait_screen_transition

    """
    The door opens once more — and stops short.

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
