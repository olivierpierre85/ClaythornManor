# Generic Host Dialogs.
# Accessible from :
#                   - Nurse

label host_generic:

    # Reset if previous early exit
    $ current_character.saved_variables["host_generic_menu"].early_exit = False

    call run_menu(current_character.saved_variables["host_generic_menu"])

    return

label host_generic_background_nurse:

    host """
    There is relatively little to say.

    I am Elisabeth Claythorn.

    I should hope that is sufficient.
    """

    return

label host_generic_invite_nurse:

    nurse """
    Why did you invite us here?
    """

    host """
    All in good time, Miss Marsh. 
    
    All in good time.
    """

    return

label host_generic_other_guests_nurse:

    host """
    That is rather insensitive.
    """

    return

label host_generic_manor:

    host """
    It has been in my husband's family for quite some time.

    I have always found it rather quaint.
    """

    return

label host_generic_age:

    host """
    A lady never reveals her age.
    """

    return

label host_generic_room:

    host """
    I am staying in the master suite, naturally.
    """

    return
