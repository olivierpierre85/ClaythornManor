# Billiard room — Saturday evening — third slot (22:40 – 23:00)
# Lady Claythorn is packed and ready to leave. Branch chosen by the top-level
# menu in 2_billiard_room.rpy:
#   - with_suspicions: captain has all three host suspicions and may confront her
#   - no_suspicions: she slips past on a thin excuse
label captain_day2_evening_billiard_room_host_intro:

    call captain_day2_evening_billiard_room_wait

    """
    Lady Claythorn pauses on the threshold, and the sight of me brings her up at once.

    For an instant her face is quite undefended.

    She wears her travelling coat, buttoned to the throat.

    She had not expected to find anyone in this room.
    """

    host """
    Captain.

    I... did not realise anyone was still up.
    """

    captain """
    Evidently.
    """

    host """
    Forgive me. I came down to fetch my book.

    I find I cannot sleep without something to read.
    """

    """
    A thin excuse, but a hostess in her own house may name her reason as she likes.

    The coat is not so easily explained.

    A travelling coat, buttoned for the road at near eleven o'clock.

    A woman seeking a book for her bedside does not come for it dressed for travel.
    """

    return


label captain_day2_evening_billiard_room_host_with_suspicions:

    call captain_day2_evening_billiard_room_host_intro

    """
    And here, plainly, is what I have been waiting for the whole evening.

    Her name is not her own.

    Her portrait is nowhere to be found in the gallery.

    She cannot shoot, nor keep a proper table.

    And now she stands before me in a travelling coat at near eleven o'clock, with two of her guests dead beneath her roof.

    If I am to put it to her, it must be now.
    """

    call run_menu(TimedMenu("captain_day2_evening_billiard_room_host_menu", [
        TimedMenuChoice("Confront her with what I know",
            'captain_day2_evening_billiard_room_host_accuse', 20, early_exit=True),
        TimedMenuChoice("Let her go and say nothing",
            'captain_day2_evening_billiard_room_host_silent', 20, early_exit=True),
    ]))

    return


label captain_day2_evening_billiard_room_host_no_suspicions:

    call captain_day2_evening_billiard_room_host_intro

    """
    I should ask her why she is dressed that way.
    
    Especially since it is not the only suspicious thing I have discovered about her.

    But I feel I still do not have proof enough to confront a lady in her own house.

    To press her now, on what I have, would be a discourtesy of the worst kind.
    """

    """
    I rise, and hold out the book she came for.
    """

    captain """
    Your book, my lady.
    """

    host """
    Oh — keep it, Captain, please. I would not dream of disturbing your evening.

    I shall do well enough without.
    """

    captain """
    I would not hear of it, my lady. You came down for it, and it is yours.

    I must insist.
    """

    """
    She hesitates a moment longer than I should have expected, then takes the book from my hand.
    """

    host """
    You are very kind.
    """

    captain """
    Not at all. Good night, my lady.
    """

    """
    She gives the smallest of nods, and is gone before I have settled back in my chair.

    The door clicks shut.

    I have the uncomfortable feeling that my manners have prevented me from doing something I should have done.

    But it is too late now.
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
    At this hour, with your coat buttoned for the road, yes.

    There is no portrait of you in the gallery upstairs. Not one.

    You are styled Lady Claythorn, and yet Claythorn is the name of the house, not of any title I have ever heard of.

    On the hunt this morning, you handled a rifle as no shooting woman would.

    And tonight, with two of your guests dead beneath your roof, you stand dressed for the door.
    """

    """
    She is very still.

    For a long moment she does not answer at all.

    Then she draws a slow breath, and meets my eye.
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
    She turns toward the door.
    """

    host """
    I should sit by the fire if I were you, Captain.

    Finish your book.

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

    A travelling coat and a startled face are not enough to set against a hostess in her own house, not at near eleven o'clock, not with the only other witnesses asleep upstairs.

    She murmurs a goodnight and goes without another word.

    Whatever I might have asked her, the moment is past.
    """

    return
