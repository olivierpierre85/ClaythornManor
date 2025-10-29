label doctor_day1_evening_bedroom_drunk_enter:

    $ change_room("bedroom_drunk")

    """
    I step into the room.

    It is a dreadful mess.

    The bottles of whisky, some already emptied, give me a fair idea whose room this is.

    There is no doubt that Samuel Manning sleeps here.
    """
    
    $ unlock_map("bedroom_drunk")

    $ play_music("mysterious")

    """
    I glance around, uncertain what I am hoping to find, when I notice a letter upon the desk.

    I take it up.

    The first part is written in a fine, elegant hand.
    """

    call drunk_letter_first_part

    """
    What on earth does this mean?

    Who could have written such a thing?

    Still, what troubles me most is the second part — barely legible, clearly added later by Samuel Manning himself.
    """

    call drunk_letter_second_part

    """
    My legs feel weak.

    I sit on the edge of the bed, struggling to make sense of it all.

    Someone in this house means me harm.

    And they are trying to use Samuel Manning to hurt me.

    I try to remember him, but I cannot say for certain that I ever treated his wife.

    That does not mean the accusation is false. It is entirely possible I did, and have simply forgotten.

    It must be someone who knows me well, yet I do not recall recognising anyone so far.

    Then again, I have not been paying much attention.

    But what should I do now?

    The prudent choice would be to leave this place at once.

    Yet to explain my departure, I might have to reveal what I found here — and that could prove troublesome.

    I cannot afford to lose the prize money either; heaven knows I need it.

    Besides, it could simply be a cruel joke, or some wretched misunderstanding.

    What should I do now?
    """

    call run_menu( 
        TimedMenu("doctor_day1_evening_bedroom_drunk_enter", [
            TimedMenuChoice("Do not risk your life — leave this place", "doctor_day1_evening_bedroom_drunk_leave_manor", 20, early_exit=True),
            TimedMenuChoice("Do not risk losing the money — stay", "doctor_day1_evening_bedroom_drunk_stay", early_exit=True),
        ])
    )

    return


label doctor_day1_evening_bedroom_drunk_leave_manor:

    """
    Why am I even considering staying here.

    I should leave now, and warn everyone about this.

    I believe that they should all be gathered in the billiard room.
    """

    $ change_room("billiard_room") 
    
    """
    Indeed I find most people here gathered around Captain Sinha.

    I interrupt him.
    """

    doctor """
    Sorry Captain, but I have something that I think you should see.
    """

    """
    I hand the letter to him.
    """

    # TODO jump to ending
    return


label doctor_day1_evening_bedroom_drunk_stay:

    """
    I do not believe I am in any great danger.

    I shall stay, though I must be cautious from now on.

    Especially around Samuel Manning.

    And I should try to discover who could have written this wretched letter.
    """

    $ doctor_details.objects.unlock("drunk_letter")

    $ play_music("PREVIOUS")

    return
