# Billiard room — Saturday evening — second slot (21:40 – 22:00)
# Mr Harring comes down looking for reassurance. Branch chosen by the
# top-level menu in 2_billiard_room.rpy:
#   - with_suspicions: captain may confide his doubts about the host
#   - no_suspicions: captain keeps up the soldierly front
label captain_day2_evening_billiard_room_lad_intro:

    call captain_day2_evening_billiard_room_wait

    """
    Ted Harring eases the door open and casts his eye round the room before stepping in.

    He goes straight to the bar and pours himself a glass of sherry filled to the brim.

    Then he comes towards me.
    """

    lad """
    Captain, could I have a word?
    """

    """
    He is making a fair show of being at his ease, but it is plain that he is quite frightened.
    """

    return


label captain_day2_evening_billiard_room_lad_with_suspicions:

    call captain_day2_evening_billiard_room_lad_intro

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

    return


label captain_day2_evening_billiard_room_lad_no_suspicions:

    call captain_day2_evening_billiard_room_lad_intro

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
    """

    call lad_day2_evening_billiard_room_captain_hypothesis_drunk

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
    So you also think these deaths are suspicious?
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
    Really? But why?

    What does this all mean?
    """

    captain """
    I am afraid I do not know more than this, but it is as well to be informed.

    In this way, we can take precautions during the night.
    """

    lad """
    What sort of precaution?
    """

    captain """
    Keep your wits about you tonight, Mr Harring.

    Turn the key in your door, and sleep with one ear open.

    If you hear anything queer, do not go after it alone — come and fetch me first.

    We shall wait until daylight, and take stock then.

    Are we agreed?
    """

    lad """
    Right.

    It is sensible, I suppose, Captain.

    If you don't mind, I think I'll head up to my room straight away, then.
    """

    captain """
    A good idea.

    Good night, Mr Harring.
    """

    lad """
    Good night, Captain.
    """

    """
    He goes more steadily than he came.

    Whatever else I have done tonight, I have at least not left him to bear his fears alone.
    """

    $ captain_details.threads.unlock('confide_in_lad')

    return
