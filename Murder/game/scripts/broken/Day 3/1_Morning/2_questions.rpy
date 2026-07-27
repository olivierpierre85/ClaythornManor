
# ------------------------------------
#   THE QUESTIONS
#
#   Good discussions points can save Moody
# ------------------------------------
label broken_day3_morning_question_boxer:

    $ broken_details.saved_variables['day3_morning_good_questions'] += 1

    broken """
    Doctor, I remember you told me you served in the Boxer Rebellion.

    Was that correct?
    """

    doctor """
    It was.

    That was my first post as a field surgeon.
    """

    """
    It is dangerous to speak as Thomas here, for I do not know the details of his part in that conflict.

    But I must, if I am to prove my point.
    """

    broken """
    Quite.

    That struck me as odd, you see, because I fought in that war as well.
    """

    doctor """
    Really? Why did you not say so before?
    """

    broken """
    I do not like to dwell on the past much.

    But now I feel this could be relevant.
    """

    captain """
    It is indeed, for I was there myself.

    I was ...
    """

    #TODO: OTHER music? or sound

    nurse """
    Good heavens!

    So was I.
    """

    """
    A pause followed that declaration.

    Everyone realises now that it cannot be a coincidence anymore.
    """

    captain """
    You were, Miss Marsh?
    """

    nurse """
    Yes, as a very young nurse.
    """

    captain """
    That is extraordinary.

    Such a coincidence...
    """

    broken """
    Captain, it is clear this is no longer a coincidence.

    Four of us served in a relatively small conflict, decades ago.

    It is very likely the reason we have been gathered here.
    """

    doctor """
    What do you mean?

    What could have happened there?
    """

    broken """
    I do not know, but if we can find out, we might begin to understand what is happening here.

    First, it is important to know whether anyone else was with us in China at that time.

    Mr Manning?
    """

    drunk """
    Yes?

    I am sorry, what is it?
    """

    broken """
    We were wondering whether you fought in China, or were there at all, during the Boxer Rebellion.
    """

    drunk """
    China? No, I have never been there.

    And certainly not during any rebellion.

    I should remember that.
    """

    psychic """
    Nor I.

    I have never so much as left these shores.
    """

    return


label broken_day3_morning_question_culprit:

    $ broken_details.saved_variables['day3_morning_good_questions'] += 1

    broken """
    I also have another theory I would like to share with you.
    """

    # When everyone is suspicious of the others: AMELIA BAXTER turns the suspicion towards him, and now you have to show you face or not. then DEATH, if not, people do not believe you more
        # TimedMenuChoice("Take off the mask and show them your true face", 'broken_day3_morning_show_face', 0, early_exit=True),


    return


label broken_day3_morning_question_letters:

    $ broken_details.saved_variables['day3_morning_good_questions'] += 1

    # TODO NOTHING new is learned, we cover this before

    return


# WEAK question - the poison proves nothing except that Moody has been
# carrying a bottle of it about since Friday. It hands Miss Marsh a stick to
# beat him with, and sets up the arrest if he later takes off the mask.
label broken_day3_morning_question_poison:

    broken """
    There is something none of you have seen.
    """

    """
    I take the bottle from my coat and set it down on the billiard table.

    The label is plain enough, and so is the skull printed above it.
    """

    broken """
    I took this from the scullery on Friday night.

    Doctor, I believe Ted Harring was poisoned.
    """

    """
    Doctor Baldwin picks the bottle up, turns it about, and hands it back to me with something close to pity.
    """

    doctor """
    Arsenic, Mr Moody.

    Had that young man swallowed this, he would have died on his knees, and the whole floor would have heard about it for hours.

    He was quiet, and he was cold, and there was not a mark upon him.

    I examined him myself.
    """

    nurse """
    And how long have you been carrying it about, Mr Moody?
    """

    broken """
    Since Friday.

    For safe keeping.
    """

    nurse """
    Quite.
    """

    """
    Ten minutes gone, and I have put a bottle of poison in Miss Marsh's mind with my own name attached to it.

    That was not clever.
    """

    return