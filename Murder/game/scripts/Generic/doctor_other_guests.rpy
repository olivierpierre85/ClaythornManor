label doctor_generic_other_guests_friday:
    
    doctor """
    Oh, I haven't talked with a lot of people so far.

    I think the only person I have heard talk is Mister Sinha.

    And I really just mean heard. 
    
    Because I don't think I was able to add anything to the conversation.
    """

    $ captain_details.unlock_knowledge('talker') 

    return

label doctor_generic_other_guests_saturday:
    
    doctor """
    I haven't talk in details to anyone yet. 
    
    So I don't really have an opinion on the guests.
    """

    return

label doctor_generic_other_guests:

    if not 'doctor_generic_other_guests_menu' in locals():
        $ doctor_generic_other_guests_menu = TimedMenu([
            TimedMenuChoice('What about Samuel Manning?', 'doctor_generic_drunk', 5),
            TimedMenuChoice('I want to talk about something else.', 'doctor_generic_cancel', 0, keep_alive = True, early_exit = True)
        ], image_right = "doctor")

    call run_menu(doctor_generic_other_guests_menu)

    return

label doctor_generic_drunk:

    doctor """
    Well, I think by now you can tell as well as I that he is a dangerous drunk.

    We better stay away from him.
    """

    return
