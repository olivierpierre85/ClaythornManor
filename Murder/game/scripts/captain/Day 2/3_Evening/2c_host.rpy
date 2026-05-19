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
    That is possible explanation, but why is she wearing a coat then?

    A woman seeking a book for her bedside does not come for it dressed for travel.
    """

    return


label captain_day2_evening_billiard_room_host_with_suspicions:

    call captain_day2_evening_billiard_room_host_intro

    """
    And here, plainly, is what I have been waiting for the whole evening.

    I have learned enough about her to know she is not who she claims to be.

    And now she stands before me in a travelling coat at near eleven o'clock, with two of her guests dead beneath her roof.

    If I am to put it to her, it must be now.
    """

    call run_menu(TimedMenu("captain_day2_evening_billiard_room_host_menu", [
        TimedMenuChoice("Confront her",
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

    call captain_day2_evening_billiard_room_host_silent

    return


label captain_day2_evening_billiard_room_host_accuse:

    $ play_music('danger', 2)

    captain """
    Forgive me, my lady, there is a matter I should put to you.
    """

    host """
    At this hour, Captain?
    """

    captain """
    At this hour, yes.

    But do not worry, I will make it quick.

    There is no portrait of you in the gallery upstairs. Not one.

    You are styled Lady Claythorn, and yet Claythorn is the name of the house, not of any title I have ever heard of.

    On the hunt this morning, you handled a rifle as no real Lady would.

    And tonight, with two of your guests dead beneath your roof, you stand dressed for the door.
    """

    """
    She is very still.

    For a long moment she does not answer at all.

    Then she draws a slow breath, and meets my eye.
    """

    host """
    I don't know what you mean by that, Captain, but I am rather tired, so I will retire now.

    Hopefully you will have recovered your senses in the morning.
    """

    """
    She turns toward the door.
    """

    captain """
    Not so fast.
    """

    """
    I step between her and the doorway, and take her by the arm.

    The grip is firmer than I had intended, but my patience is at an end.
    """

    host -scared """
    Captain! What on earth do you think you are doing?

    Stop this instant!
    """

    """
    She wants to look outraged, but she is visibly scared.
    """

    captain """
    I am truly sorry, I do not want to harm you.

    But I need to know what is happening here.

    Who are you? 

    What is this all about?
    """

    """
    Her gaze is panicked, but for a second I notice she sees something behind me.

    But I do not have the time to turn to see what it is.
    """

    play sound bludgeon

    """
    The blow tears across my temple.

    The room tilts, and the carpet rises to meet me.

    Somewhere very far off, the lady is screaming.
    """

    host -scared """
    Stop! You're going to kill him!
    """

    """
    I turn towards my attacker and see the butler looking down on me.

    In his hand is a poker, snatched from the fire.

    He raises it above his head, then brings it down quickly towards me.
    """

    play sound bludgeon

    jump captain_ending_bludgeoned


label captain_day2_evening_billiard_room_host_silent:

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
