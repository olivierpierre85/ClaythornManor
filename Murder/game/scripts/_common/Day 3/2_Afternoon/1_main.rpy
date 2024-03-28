label common_day3_afternoon_lad_psychic_captain_discussion:

    captain """
    I believe I've looked absolutely everywhere now.

    There is no trace of anyone.

    I also tried to use the telephone, and it's not working.

    Thus, there is no way for us to call for help.

    The way I see it now, we don't have many options left.
    
    I believe we must leave this place.

    The longer we stay, the more at risk we are.
    """

    psychic """
    But... shouldn't we wait for the police?

    They were expected today. They could arrive any moment.
    """

    captain """
    I wouldn't count on it.

    From what I gather, there's no evidence that the police were called yesterday.
    """

    psychic """
    But Miss Claythorn said...

    She said...
    """

    if current_character.text_id == "lad":
        """
        She stops mid-sentence, realising the implication.
        """
    else:
        pause 1.0

    psychic """
    I see, you believe she never called.

    That the police have no idea about what's happened here.

    That she lied to us.
    """

    captain """
    That's the most logical explanation.

    No one was around when the phone calls were supposedly made.

    So, there's no way to verify if they actually happened.
    """

    lad """
    But why?

    Why would anyone do this?

    I don't understand what's happening.
    """

    captain """
    Neither do I.

    I've thought about it, and I have no clue why we were all invited here.

    I'm certain it wasn't to give us any money.

    In any case, all I know is we need to leave as soon as possible.
    """

    psychic """
    But how?

    The nearest town is miles away.

    I can't walk that far. 

    And even if I could, I'm not prepared for such a journey.
    """

    """
    Captain Sinha and I consider this for a moment.
    """

    captain """
    You might be right.

    It would be a long walk, and the weather might turn at any moment.

    We could get caught in another storm.

    It's probably unsafe for you to join us.
    """

    psychic surprised """
    But you're not going to leave me here alone, are you?

    What would become of me?
    """

    captain """
    We could lock you in a room.

    Though, that's far from ideal.

    Perhaps one of us should stay with you.
    """

    psychic """
    Yes!

    Mister Harring can stay with me, right?

    The two of us should be safe until you return with help.
    """

    captain """
    That seems to be the wisest choice.

    What do you think, Mister Harring?
    """

    pause 1.0

    return
