# Billiard room — Saturday evening — first slot (21:00 – 21:20)
# Miss Marsh comes down. Branch chosen by the top-level menu in
# 2_billiard_room.rpy:
#   - with_suspicions: captain may confide his doubts about the host
#   - no_suspicions: captain has no firm evidence, dismisses the line of talk
label captain_day2_evening_billiard_room_nurse_intro:

    call captain_day2_evening_billiard_room_wait

    """
    A few minutes pass before the door eases open behind me.

    Rosalind Marsh hesitates for a moment in the doorway, then crosses the room with her usual quiet composure.
    """

    call common_day2_evening_billiard_room_nurse_captain_intro

    call common_day2_evening_billiard_room_nurse_captain_two_deaths_1

    """
    A direct question, asked very simply.
    """

    return


label captain_day2_evening_billiard_room_nurse_with_suspicions:

    call captain_day2_evening_billiard_room_nurse_intro

    """
    I have a choice to make here.

    Miss Marsh does not strike me as someone who could harm someone with purpose.

    I could share with her what I have come to suspect of our hostess.

    She might prove an ally, should I need one later.

    But if I have misread her, the price for trusting her could be very high indeed.
    """

    call run_menu(TimedMenu("captain_day2_evening_billiard_room_nurse_menu", [
        TimedMenuChoice("Tell her about your doubts",
            'captain_day2_evening_billiard_room_nurse_agree', 0, early_exit=True),
        TimedMenuChoice("Keep pretending everything is fine",
            'captain_day2_evening_billiard_room_nurse_dismiss', 0, early_exit=True),
    ]))

    return


label captain_day2_evening_billiard_room_nurse_no_suspicions:

    call captain_day2_evening_billiard_room_nurse_intro

    """
    I am uneasy at what is unfolding here as well.

    But I do not have enough tangible evidence to prove it.

    So the safest course is to pretend everything is fine.
    """

    call captain_day2_evening_billiard_room_nurse_dismiss

    return


label captain_day2_evening_billiard_room_nurse_dismiss:


    call common_day2_evening_billiard_room_nurse_captain_two_deaths_2

    """
    She regards me a moment longer than I should like.
    """

    nurse """
    Well, in that case, I am quite tired.

    I should retire.

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


label captain_day2_evening_billiard_room_nurse_agree:

    captain """
    Indeed, Miss Marsh, it does seem strange to me too.

    As a matter of fact, I do not believe these deaths to be entirely accidental.

    The reason is that I have come to doubt our hostess is who she claims to be.
    """

    nurse """
    Lady Claythorn?
    """

    captain """
    Precisely.

    There is no portrait of her in the gallery upstairs.

    The name itself does not stand to scrutiny — Claythorn is the house, not a title.

    And on the hunt this morning she handled a rifle as no shooting woman ever would.

    I cannot say what lies behind it, but the lady before us is not who she says she is.
    """

    """
    She does not protest.

    If anything, she seems to settle, as though I have only confirmed something she had been weighing on her own.
    """

    nurse """
    Thank you for telling me, Captain.
    """

    captain """
    Be on your guard tonight, Miss Marsh.

    Wedge a chair beneath your door if you must, and sleep lightly.

    Come the morning, we shall see what is to be made of it.
    """

    nurse """
    I shall, Captain.

    Good night to you.
    """

    captain """
    Good night, Miss Marsh.
    """

    """
    She withdraws with a measured tread, and the door clicks gently shut behind her.

    Whether I have done well to confide in her, only the morning will tell.
    """

    $ captain_details.threads.unlock('confide_in_nurse')

    return
