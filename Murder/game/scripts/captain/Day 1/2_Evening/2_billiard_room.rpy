# Billiard room
label captain_day1_evening_billiard_room:

    $ change_room('billiard_room')

    if not captain_details.saved_variables["day1_evening_billiard_room_visited"]:

        $ captain_details.saved_variables["day1_evening_billiard_room_visited"] = True

        """
        The billiard room is warm and well lit.

        Most of the guests have gathered here.

        Lady Claythorn is in conversation with Miss Marsh and Thomas Moody.

        Ted Harring hovers near them, looking as uncomfortable as ever.

        Daniel Baldwin sits alone in a chair, nursing a glass.

        And Manning is at the bar. Naturally.

        As I enter, a few heads turn my way.

        I recognise that look. They are bored and waiting for any kind of distraction.
        """

        $ captain_day1_evening_billiard_room_menu = TimedMenu("captain_day1_evening_billiard_room_menu", [
            TimedMenuChoice('Approach the large group', 'captain_day1_evening_billiard_room_story', 60),
            TimedMenuChoice('Have a drink at the bar', 'captain_day1_evening_billiard_room_bar', 10),
            TimedMenuChoice('Talk to Dr Baldwin', 'captain_day1_evening_billiard_room_baldwin', 10),
            TimedMenuChoice('Leave the room', 'generic_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ captain_day1_evening_billiard_room_menu.early_exit = False

        """
        I am back in the billiard room.
        """

    call run_menu(captain_day1_evening_billiard_room_menu)

    return


label captain_day1_evening_billiard_room_story:

    """
    I make my way towards Lady Claythorn and the others.
    """

    host """
    Captain Sinha. Do come and join us.
    """

    captain """
    Thank you, Lady Claythorn.
    """

    nurse """
    Captain, you must tell us one of your stories.

    Mr Moody was just saying what a fine storyteller you are.
    """

    """
    My old standby rises to the tip of my tongue. The Boxer Rebellion.

    I have told that tale a hundred times. It almost feels like a memory of my own.

    Yet, a single misplaced detail in front of the wrong listener could unravel the whole pretence.

    On the other hand, refusing outright might invite suspicion.
    """

    call run_menu(TimedMenu("captain_day1_evening_billiard_room_story_menu", [
        TimedMenuChoice('Tell the story of the Boxer Rebellion', 'captain_day1_evening_billiard_room_story_tell', 0, early_exit=True),
        TimedMenuChoice('Decline the request', 'captain_day1_evening_billiard_room_story_refuse', 0, early_exit=True),
    ]))

    return


label captain_day1_evening_billiard_room_story_tell:

    captain """
    How kind of him.

    Well, if you insist.
    """

    """
    I take a position near the fireplace and begin.

    This is my best story.

    I have told it so many times that it almost feels true.

    I speak of the Boxer Rebellion. The Eight-Nation Alliance. The march on Beijing.

    I give them the full account.

    Everyone is listening. Even the doctor has looked up from his glass.

    Good.

    The truth is, during the Boxer Rebellion, I was a supply officer stationed behind the lines.

    I never saw a single Boxer. I never fired a single shot.

    But I have read enough accounts of the expedition to describe it as though I were there.

    And over the years, the story has become so polished that even I sometimes forget the reality.

    I finish the story and pause, letting the silence settle.

    Miss Marsh is studying me. There is something in her expression that I do not quite like.

    But the rest of the room seems satisfied.

    Mr Moody nods approvingly. Lady Claythorn offers a polite smile.

    It is a good story. That is what matters.
    """

    $ captain_details.threads.unlock('tell_boxer_story')

    return


label captain_day1_evening_billiard_room_story_refuse:

    captain """
    You are most kind, Miss Marsh. But I fear I must disappoint you this evening.

    The journey has left me no strength for a performance.

    Perhaps another time.
    """

    """
    The silence that follows is a fraction too long.

    Lady Claythorn's smile thins. Mr Moody's face slips into open disappointment.

    My refusal has made everyone uneasy.

    A man invited for his military exploits who refuses to tell a war story is a man with something to conceal.

    Maybe I made a mistake.
    
    I should take myself out of sight before I make it any worse.
    """

    captain """
    Forgive me. I believe I shall retire to my room now.
    """

    """
    I incline my head politely and withdraw from the group, conscious that everyone in the room is following me to the door.
    """

    # Set the previous menu to early exit
    $ captain_day1_evening_billiard_room_menu.early_exit = True

    return


label captain_day1_evening_billiard_room_bar:

    """
    I make my way to the bar.

    Manning is there, slumped against the counter.

    I pour myself a small measure of port and stand apart from him.

    There is nothing to be gained from associating with a drunkard.
    """

    return


label captain_day1_evening_billiard_room_baldwin:

    """
    I approach Baldwin.

    He looks up. His eyes are flat.
    """

    doctor """
    Captain Sinha, how are you?
    """

    captain """
    I am fine, Doctor.

    What about you?
    """

    doctor """
    A little tired if I am being honest.

    The journey has exhausted me.
    """

    """
    Yes, the journey was long. But I can tell that is not entirely what is causing Dr Baldwin's tiredness.

    But no need to say anything.
    """

    captain """
    Very well, I'll leave you alone then.

    Have a good night.
    """

    doctor """
    You too.
    """

    return
