label doctor_day3_afternoon_nurse:

    $ change_room("butler_room")

    nurse """
    I believe it has been long enough.

    We should head back downstairs, and see where the others have settled.
    """

    """
    We climb down from the attic and reach the top of the main staircase.
    """

    $ change_room("entrance_hall")

    """
    From there, we can hear voices coming from the tea room.

    We go down and linger by the doorway, careful not to be seen.

    We try to make out what they are saying.
    """

    """
    We cannot catch every word, but the gist is clear.

    Captain Sinha intends to leave on his own.

    Ted Harring and Amelia Baxter will wait for him to return with help.
    """

    nurse """
    I think they are coming.

    Quickly.
    """

    """
    She darts towards the library to hide.

    I follow her at once.
    """

    $ change_room("library", fade)

    nurse """
    Good.

    We should be safe in here, for the moment.
    """

    doctor """
    Very well.

    But what do we do next?

    From what we heard, they are no closer to understanding what is happening than we are.

    It may be safe to speak with them, do you not agree?
    """

    nurse """
    I am not sure.

    One of them could be lying to the others.

    Mostly, I am frightened of Captain Sinha.

    I do not think the other two are as dangerous.

    We should at least wait for him to leave.

    After that, I do not know.

    We could remain hidden, and see whether the police come.

    Or we could try to speak to them.

    What do you think?
    """

    $ time_left = 1
    call run_menu(TimedMenu("doctor_day3_afternoon_nurse", [
        TimedMenuChoice("Speak to them, they look harmless", "doctor_day3_afternoon_nurse_talk", 0, early_exit=True),
        TimedMenuChoice("Stay hidden, they look dangerous", "doctor_day3_afternoon_nurse_hide", 0, early_exit=True),
    ]))

    # Now in the kitchen, they prepare dinner like the lad

    call doctor_day3_afternoon_nurse_kitchen

    jump doctor_ending_poisoned


label doctor_day3_afternoon_nurse_talk:

    doctor """
    I think we should speak to them.

    We can wait for Captain Sinha to leave, if you would prefer.
    """

    nurse """
    All right.

    Let us wait a little.
    """

    call wait_screen_transition

    call change_time(12, 30)

    """
    We do not have to wait long.

    A few minutes later, we hear the Captain say his goodbyes.

    Then the front door closes.
    """

    play sound door_close

    nurse """
    Right.

    He has left.

    We can safely approach the others now.
    """

    """
    We slip out of the library and cross the hall.
    """

    $ change_room("entrance_hall", dissolve)

    """
    Ted Harring and Amelia Baxter are still there.

    They look startled to see us.
    """

    psychic """
    Doctor?

    And Miss Marsh?

    Where have you been?
    """

    lad """
    You two gave us a fright.

    Thought you'd done a runner like the others.
    """

    nurse """
    We have been searching the house.

    We did not find anything useful.

    We heard the front door close, so we came at once.

    Has someone just left?
    """

    psychic """
    Yes, Captain Sinha.

    He has gone to fetch help.

    He says he can make it alone, and that we should not all risk ourselves on the road.

    So we shall wait for him here.
    """

    nurse """
    That seems sensible.

    Then we shall wait with you.
    """

    psychic """
    All right.

    In the meantime, none of us has eaten properly in hours.

    Since we have little else to do, we ought to prepare something.

    That would at least keep us occupied until the police arrive.
    """

    nurse """
    I agree.

    We should go and see what is in the kitchen.
    """

    psychic """
    Good idea.

    Let's go.
    """


    return


# TODO Other ending of fork to poisoned ending?
label doctor_day3_afternoon_nurse_hide:

    doctor """
    I believe we should remain hidden for the moment.

    Not out of cowardice, but out of prudence.

    There is no point in taking unnecessary risks.

    From what I understand, Captain Sinha is gonna go find help.

    We can wait hidden until he returns, that's probably the safest course.
    """

    nurse """
    Great, I was hoping you would say that.

    We just have to find a safe spot and wait there. 
    """

    jump work_in_progress


# TODO REWRITE
label doctor_day3_afternoon_nurse_kitchen:

    $ change_room("kitchen", dissolve)

    call change_time(12,30)

    """
    The kitchen is cold, but not abandoned.

    A few pots still sit where they were left.

    A loaf of bread rests beneath a cloth, as if someone meant to return.
    """

    nurse """
    There should be enough here for a simple meal.

    Bread, some cheese, and perhaps soup if the range still works.

    We do not need a feast.

    Just enough to keep our strength.
    """

    lad """
    If there's bread, I'm in.

    If there's cheese, I'm in twice.
    """

    psychic """
    Please do not make jokes.

    Not now.
    """

    lad """
    I'm not joking.

    I'm coping.
    """

    doctor """
    That is understandable.

    Let us be efficient.

    Rosalind, you know this place better than any of us.

    If you can direct us, we will make this quick.
    """

    nurse """
    All right.

    Ted, fetch plates and whatever cutlery you can find.

    Amelia, fill the kettle if the tap still runs.

    Doctor, help me check the larder.
    """

    """
    We set to work.

    For a few minutes, the simple tasks dull the edge of fear.

    Yet even here, with our hands busy, I cannot shake the thought that the manor is listening.
    """

    return
