label nurse_day2_hunt_tea_room:

    $ change_room("tea_room")

    call change_time(12, 0)

    if nurse_details.saved_variables.get('day2_hunt_tea_room_early', False):

        """
        Amelia Baxter comes a bit later.

        She is composed as ever when she arrives.

        She takes the chair across from me.
        """

    else:

        """
        Mrs Baxter is already seated when I arrive, composed as ever.

        I take the chair across from her.
        """

    psychic """
    Miss Marsh, how are you?
    """

    nurse """
    Fine, thank you.
    """

    psychic """
    It seems we have not yet had a proper chance to talk, have we?
    """

    nurse """
    Indeed.
    """

    call psychic_generic

    """
    A member of the household staff steps in quietly.
    """

    maid """
    Excuse me for interrupting, but do you ladies need some lunch?
    """

    nurse """
    That would be lovely, thank you.
    """

    pause 1.0

    """
    She returns shortly with some plates.

    We eat and exchange pleasantries.
    """

    pause 1.0

    """
    When we have finished, I set my napkin aside.

    I have been feeling out of sorts all morning, and the feeling has not quite left me.
    """

    play sound woman_cough

    """
    A cough escapes me, sharper than I expected.
    """

    nurse """
    I am feeling rather poorly, I am afraid.

    I think I shall retire to my room for a short while.

    Would you mind being left on your own?
    """

    psychic """
    Not at all, please don't concern yourself.

    There is more than enough here to occupy me.
    """

    """
    I leave her to it and make my way back upstairs.

    A brief rest should do me good before the hunting party returns.
    """

    return
