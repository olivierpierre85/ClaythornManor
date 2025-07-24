label lad_generic_other_guests:

    call run_menu(current_character.saved_variables["lad_generic_other_guests_menu"])

    return


label lad_generic_other_guests_friday_dinner:

    lad """
    Well, I just arrived.
    
    So I don't really have an opinion on anyone yet.
    """

    return


label lad_generic_other_guests_friday:

    lad """
    I haven't talk a lot to other people yet, except maybe to Miss Baxter.
    """

    doctor """
    And what do you make of her?
    """

    lad """
    I am not sure. 
    
    She seems very nice, but there is something weird about her.

    I don't know how to explain it.
    """

    doctor """
    I see.
    """

    return

