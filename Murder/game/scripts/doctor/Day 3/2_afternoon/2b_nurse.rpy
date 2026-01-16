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

    # TODO Choice of hiding pr talk to them.
    # But you get seen anyway => So only possible ending.


    jump ending_generic