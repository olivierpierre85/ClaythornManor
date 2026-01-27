label doctor_day3_afternoon_nurse:

    $ change_room("butler_room")

    nurse """
    I believe it has been long enough.

    We should head back downstairs, and see where the others have settled.
    """

    """
    We climb down from the attic and reach the top of the main staircase.
    """

    $ change_room('entrance_hall', dissolve)

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

    call doctor_day3_afternoon_nurse_kitchen

    jump doctor_ending_poisoned


label doctor_day3_afternoon_nurse_wait_captain_leave:

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

    play sound door_shut

    return


label doctor_day3_afternoon_nurse_talk:

    doctor """
    I think we should speak to them.

    We can wait for Captain Sinha to leave, if you would prefer.
    """

    call doctor_day3_afternoon_nurse_wait_captain_leave

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

    return


# TODO Other ending of fork to poisoned ending?
label doctor_day3_afternoon_nurse_hide:

    doctor """
    I believe we should remain hidden for the moment.

    Not out of cowardice, but out of prudence.

    There is no point in taking unnecessary risks.

    From what I understand, Captain Sinha is going to find help.

    We can stay concealed until he returns.

    That is probably the safest course.
    """

    nurse """
    Good.

    I was hoping you would say that.

    We just have to find a safe spot and wait there.

    But first, let us be certain Captain Sinha has gone.
    """

    doctor """
    Very well.
    """

    call doctor_day3_afternoon_nurse_wait_captain_leave

    nurse """
    Right.

    He has left.
    """

    doctor """
    All right.

    Let us go then.
    """

    """
    I step out of the library, thinking the entrance hall will be empty.
    """

    nurse """
    Doctor, wait,...
    """

    $ change_room("entrance_hall")

    """
    But of course Ted Harring and Amelia Baxter are still there, lingering by the front door.

    Bloody hell, what a fool I am.

    Too late to back out now.

    I shall simply have to make the best of it.
    """

    return


label doctor_day3_afternoon_nurse_kitchen:

    $ change_room("kitchen", dissolve)

    call change_time(12, 30)

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

    doctor """
    Very well.

    What can I do to help?
    """

    psychic """
    I think Rosalind and I can manage, Doctor.

    Perhaps you could set the table?
    """

    doctor """
    Certainly.

    I shall do that.
    """

    psychic """
    And maybe Mr Harring can go with you?
    """

    lad """
    Yeah, alright.

    I'll tag along, Doctor.
    """

    $ change_room("dining_room", dissolve)

    call change_time(14, 00)

    """
    Ted Harring and I set the table, then he excuses himself.

    I linger a moment, looking at the place where we have eaten for three days.

    It feels oddly grand for just the four of us.

    I cannot help thinking of my own home, and my own table.

    Soon enough, the two ladies join us with our makeshift lunch.

    Ted Harring returns a moment later.
    """

    psychic """
    There you are.

    It is not much, but it will see us through the day.
    """

    doctor """
    It looks excellent.

    Thank you.
    """

    """
    We sit and begin to eat at once.

    I believe we are all famished.

    For a time, we eat without speaking.
    """

    call wait_screen_transition

    call change_time(15, 0)

    """
    Halfway through my bread, an odd taste blooms at the back of my tongue.

    Bitter.

    Metallic.

    I pause, chewing more slowly.

    My stomach tightens as if a fist has closed around it.

    I set my knife down carefully, as though the smallest sound might split my skull.

    The room seems to tilt, ever so slightly.

    No.

    Not the room.

    It is me.
    """

    doctor """
    Forgive me.

    I feel quite unwell.
    """

    lad """
    What?

    Doctor, you alright?
    """

    nurse """
    Doctor?

    Daniel, what is it?
    """

    """
    Heat rushes through my chest, then drains away at once.

    My hands have gone cold.

    The edges of my vision darken, as if someone is drawing curtains.

    I try to stand.

    My legs do not answer properly.

    The chair scrapes.

    The sound is far too loud.

    I reach for the table, but my fingers miss the edge.
    """

    lad """
    Careful!

    Doctor!
    """

    """
    The floor rises to meet me.

    My shoulder strikes first, then my cheek.

    Voices rush in, muffled and distant, as though I am submerged.

    The ceiling swims.

    Then the light folds in on itself.
    """

    return

