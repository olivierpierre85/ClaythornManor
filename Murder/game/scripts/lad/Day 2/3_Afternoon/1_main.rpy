label lad_day2_afternoon:
    call black_screen_transition("Day 2 - Evening???.") # Good ?
    scene great_hall with irisout

    call change_time(15,00)
    
    if lad_day2_hunt:
        """
        The rest happened feels like a blur for me.

        After the screaming and crying in the woods, Captain Sinha took charge.

        He made us transported the Doctor on a makeshift stretcher.
 
        It took a while but we finally reached the mansion.
        """
    else:
        """
        I can see the hunting partying entering the house.

        Amalia and Rosalind were already there, near the entrance.

        Lady Claythorn enters first, visibly shocked.

        Then the butler and footman followed suit.

        They are dragging someone on a makeshift stretcher.
        """

    # TODO play dramatic music
    psychic surprised """
    Oh my God ! What Happened !?

    Is that Doctor Baldwin. Is he injured ?

    Oh no ? Is he dead ?
    """

    captain """
    I am sorry dear, I am afraid that he is.
    """

    if lad_day2_hunt:
        """
        We explained what happened.
        """
    else:
        "TODO explain in details"

    captain """
    Well it's a another reason for an ambulance to come.

    Has anyone from the city arrived here yet ?
    """

    nurse """
    I am afraid not.

    We are still waiting for them.
    """

    captain """
    We better tell them to hurry up then.

    Lady Claythorn where is your phone ?
    """

    host """
    It's in the TODO

    But don't worry I'll take care of it myself.
    """

    """
    She leaves the group with the butler on her trail.
    """




    return

