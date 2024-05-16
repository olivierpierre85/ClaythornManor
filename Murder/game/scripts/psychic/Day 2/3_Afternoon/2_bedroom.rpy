label psychic_day2_afternoon_bedroom:
    
    $ change_room('bedroom_psychic', dissolve)

    call change_time(18, 00)

    """
    I returned to my room to change and clear my head.
    
    It seems like I still have a little bit of time before dinner.

    I guess I could just rest for a bit,

    or take the opportunity to have a private chat with someone.

    I don't think it would be wise to approach Captain Sinha,

    nor Lady Claythorn.

    However, I don't believe I am taking too much of a risk by talking with Rosalind Marsh or Ted Harring.
    """

    $ time_left = 99 # TODO, change with option in menu? 
    call run_menu(TimedMenu("psychic_day2_afternoon_bedroom", [
            TimedMenuChoice('Try to talk to Rosalind Marsh', 'psychic_day2_afternoon_bedroom_nurse_busy', 10, early_exit=True),
            TimedMenuChoice('Try to talk to Ted Harring', 'psychic_day2_afternoon_lad_discussion', 30, early_exit=True),
            TimedMenuChoice('Just have a quick nap instead', 'psychic_day2_afternoon_cancel', 30, early_exit=True),
            # Talk with host anyway??? Intuition things are not going according to plan.
        ])
    )

    return


label psychic_day2_afternoon_lad_discussion:

    $ change_room("bedrooms_hallway")

    call common_day2_afternoon_lad_psychic_discussion

    return


label psychic_day2_afternoon_bedroom_nurse_busy:
    
    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on Rosalind Marsh's door.
    """

    nurse """
    Yes? Who is there?
    """

    psychic """
    It's Amelia Baxter.

    I was hoping we could talk a bit.
    """

    nurse """
    Oh, Mrs. Baxter, I'm actually not ready yet.

    Can it wait until dinner?
    """

    play sound woman_cough

    """
    She coughs abruptly, a sound that seems to carry a painful echo.
    """

    pause 1.0

    nurse """
    Sorry about that. 
    """

    psychic """
    Are you alright?
    """

    nurse """
    Yes, it's nothing, really.
    
    I am just a bit under the weather.
    """

    """
    She takes out her handkerchief and brings it to her mouth.

    Then, she tries to quickly put it back in her pocket.

    But I still caught a glimpse of a trace of blood on it.

    She's worse than she wants to show.
    """

    $ nurse_details.description_hidden.unlock('sick')

    nurse """
    Well, I should go now.
    """

    """
    She is obviously not comfortable with the situation.

    I shouldn't press her.
    """

    psychic """
    Of course, sorry for bothering you.
    """
    
    return


label psychic_day2_afternoon_cancel:

    $ change_room('bedroom_psychic')

    """
    That's about all I can manage right now.

    I should rest for a bit.
    """

    call wait_screen_transition()

    return

