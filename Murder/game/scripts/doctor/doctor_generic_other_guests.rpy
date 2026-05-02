label doctor_generic_other_guests:

    call run_menu(current_character.saved_variables["doctor_generic_other_guests_menu"])

    return

label doctor_generic_other_guests_friday:
    
    doctor """
    Oh, I haven't talked to many people so far.

    I think the only person I've heard speak is Mr Sinha.

    And by "heard," I really just mean heard.
    
    Because I don't think I was able to contribute anything to the conversation.
    """

    if current_character.text_id == "psychic": 

        """
        Yes, I can understand that feeling.
        """

    $ captain_details.description_hidden.unlock('talker') 

    return

label doctor_generic_other_guests_saturday:
    
    doctor """
    I haven't spoken in detail with anyone yet.
    
    So, I don't really have an opinion on the guests.
    """

    return

label doctor_generic_drunk:

    doctor """
    Well, I think by now you can tell as well as I can that he is a dangerous drunk.

    We'd better stay away from him.
    """

    return
