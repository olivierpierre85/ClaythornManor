# Generic Host Dialogs.
# Accessible from :
#                   - Nurse
#                   - Broken

label host_generic:

    # Reset if previous early exit
    $ current_character.saved_variables["host_generic_menu"].early_exit = False

    call run_menu(current_character.saved_variables["host_generic_menu"])

    return


label host_generic_weather:

    host """
    A mixture of rain and good weather.

    That is actually as good as it gets for the region, I am afraid.

    One must learn to appreciate the mist as much as the sun.
    """

    return


label host_generic_background:
    
    host """
    There isn't much to say.
    
    I have been the mistress of this estate since my late father passed away.

    That would have been nearly ten years ago.

    I now manage the domain as well as I can.

    But I don't really like to talk about myself.
    """

    return


label host_generic_background_nurse:

    call host_generic_background

    """
    That's peculiar, the gentry usually love to talk about themselves.

    But she could just be a little shy.
    """

    return

label host_generic_invite_nurse:

    host """
    Everything was explained in the letter, was it not?
    """

    nurse """
    True, but it didn't mention the reasons for this very selfless act.
    """

    host """
    One does not think reasons are necessary to thank people who did exceptional things.

    Such as yourself.

    What a great sacrifice you have made, giving most of your life for the welfare of others.

    It is my great pleasure to give you something in return, since I have been blessed myself.
    """

    nurse """
    That's very generous.

    So you've been doing that often?
    """

    host """
    Well, no, that is the first time I am giving away this prize.

    But I might do for other people in the future of course.
    """

    return

label host_generic_other_guests_nurse:

    host """
    A group of people of great value.

    But we shouldn't talk about them behind their backs.

    That is improper.
    """

    return


label host_generic_manor:

    host """
    This "place" has been in my family for quite some time.

    I have always found it rather quaint.

    It is a trifle too large for me and my staff, I am afraid.

    But I can't really give it up, it's my legacy.
    """

    return


label host_generic_age_nurse:

    host surprised """
    I beg your pardon? You want to know my age?
    """

    nurse """
    Oh, it's just that you look so young.

    And managing such a large estate must be difficult for a young lady.
    """

    host -surprised """
    I am not as young as I might look.

    And I manage it quite well, thank you.
    """

    return


label host_generic_room:

    host """
    The master bedroom is named after Henry IV.

    Why, I am not sure exactly.
    """

    return


# ------------------------------------
#               BROKEN
# ------------------------------------
label host_generic_background_broken:

    call host_generic_background

    """
    She turns the talk aside as neatly as a card sharp turning a trick.

    Mistress here since her father passed, she says. Nearly ten years.

    And yet she cannot be far past thirty.

    The sums do not quite tally.

    Either she came to it remarkably young, or that is not the whole of the story.
    """

    return


label host_generic_invite_broken:

    broken """
    Forgive my curiosity, but the letter never quite explained why you settled upon us in particular.

    A thousand pounds apiece is no small sum.
    """

    host """
    Is generosity so very suspect, Mr Moody?

    Each of you performed an act of rare courage. One felt such things ought to be honoured.
    """

    broken """
    Of course. It is only that such open-handedness is rare these days.
    """

    host """
    Then let us call it an indulgence.

    I have the means, and few enough occasions to put them to good use, out here.
    """

    """
    The means.

    That is the very thing her family no longer has, if my enquiries are to be trusted.

    She answers without a flicker, smooth as glass.

    Too smooth, perhaps. Either she is telling the truth, or she has rehearsed the lie until it fits like a glove.
    """

    return


label host_generic_other_guests_broken:

    host """
    A remarkable assembly, every one of them.

    But it would be improper of me to discuss my guests behind their backs.
    """

    """
    A careful answer. She gives nothing away.

    Then again, neither do I.
    """

    return
