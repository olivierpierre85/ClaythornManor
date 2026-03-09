# Generic Host Dialogs.
# Accessible from :
#                   - Nurse

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
    True, but it didn't mention the reasons for this very generous act.
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
