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
        TimedMenuChoice("Speak to them in the tea room", "doctor_day3_afternoon_nurse_talk", 0, early_exit=True),
        TimedMenuChoice("Stay hidden and move carefully", "doctor_day3_afternoon_nurse_hide", 0, early_exit=True),
    ]))

    return

# TODO rewrite
label doctor_day3_afternoon_nurse_talk:

    doctor """
    I think we should speak to them.

    We can wait for Captain Sinha to leave if you prefer.
    """

    nurse """
    All right.

    Let's wait a bit.
    """

    call wait_screen_transition

    call change_time(12,30)

    """
    We don't have to wait for long, a few minutes later we hear captain say goodbye.

    Then the main entrance closed.
    """

    play sound door_close

    nurse """
    Right he left, we can safely approach the other now.
    """
    
    """
    So we slip out of the library and cross the hall.
    """

    $ change_room("entrance_hall", dissolve)

    """
    Ted Harring and Amelia Baxter are still there.

    They look surprised to see us.
    """

    psychic """
    Doctor?

    And Miss Marsh?

    Where have you been?
    """

    lad """
    You two gave us a fright.

    We thought you'd vanished like the others.
    """

    doctor """
    We have been searching.

    Coudln't find anything thouh

    We needed a moment to speak privately, and to consider our next steps.

    I understand Captain Sinha has decided to leave the manor.
    """

    psychic """
    He has.

    He says he can make it alone, and that we should not all risk ourselves on the road.
    """



    nurse """
    There is another matter.

    We have not eaten properly in hours.

    If we are to keep our wits, we should prepare something.
    """

    psychic """
    Yes, good idea.
    
    We could whip something up.

    That would at leas keep us occupied until the police arrives.
    """

    """
    We all head downstairs.
    """

    jump doctor_day3_afternoon_nurse_kitchen

# TODO rewrite
label doctor_day3_afternoon_nurse_hide:

    doctor """
    I believe we should remain hidden for the moment.

    Not out of cowardice, but out of prudence.

    If Captain Sinha is leaving, it is best we let him go.

    Then we can decide how to deal with the others.
    """

    nurse """
    I was hoping you would say that.

    Come on.

    I know a way to move without being noticed.
    """

    """
    We wait in the library, listening.

    Footsteps cross the hall.

    A door opens, then shuts.

    After a long minute, the house grows quieter.
    """

    nurse """
    That will be him.

    Now.

    We go downstairs, softly.

    If we are lucky, they will stay in the tea room.
    """

    """
    We slip out of the library and move along the corridor.

    The manor feels even larger when we walk in silence.

    Every creak sounds like an accusation.
    """

    $ change_room("entrance_hall", dissolve)

    """
    As we pass the foot of the stairs, a voice calls out, sharp and sudden.
    """

    psychic """
    Doctor?

    Nurse?

    Is that you?
    """

    """
    I freeze.

    Rosalind does too.

    Amelia Baxter stands in the doorway of the tea room, staring straight at us.
    """

    lad """
    You can't just sneak about like that.

    You nearly gave us heart failure.
    """

    doctor """
    Miss Baxter.

    Mr Harring.

    Forgive us.

    We were attempting to move quietly, so as not to draw attention.

    This house does not reward noise.
    """

    psychic """
    Quietly.

    Yes.

    I imagine it does not.

    Were you listening to us?
    """

    nurse """
    We heard voices.

    We did not know who it was.

    We hid out of caution, not malice.
    """

    lad """
    Fair enough.

    I can't blame you for that.

    This place is cursed.
    """

    doctor """
    Captain Sinha has gone, has he not?
    """

    psychic """
    He has.

    He left only a moment ago.

    He told us to wait here, and to be ready when he returns.

    I do not know whether to believe he will.
    """

    nurse """
    Then we should make ourselves useful while we wait.

    We need food.

    And we need water.

    We cannot keep going on nerves alone.
    """

    lad """
    Thank you.

    Someone sensible at last.

    I'm starving.
    """

    doctor """
    The kitchen seems the obvious choice.

    It is central enough, and it will give us something to do.

    Idleness will only invite panic.
    """

    psychic """
    All right.

    But we stay together.

    No more disappearing.
    """

    """
    We fall into an uneasy group, still wary, but no longer scattered.

    Then we make for the kitchen, with careful steps and watchful eyes.
    """
    
    jump doctor_day3_afternoon_nurse_kitchen


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
