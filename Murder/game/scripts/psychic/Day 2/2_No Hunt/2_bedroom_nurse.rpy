label psychic_day2_no_hunt_bedroom_nurse_blood:
    
    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on Rosalind Marsh's door.
    """

    nurse """
    Yes? Who is there?
    """

    psychic """
    It's me again.

    I wanted to see how you were doing.
    """

    """
    She slightly opens the door but stays inside.
    """

    nurse """
    Oh, Mrs. Baxter, I'm actually not feeling well.

    Can it wait?
    """

    play sound woman_cough

    """
    She coughs abruptly, a sound that seems to echo painfully.
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

    She is worse than she wishes to show.
    """

    nurse """
    Well, I should go now.
    """

    """
    She is obviously not comfortable with the situation.

    I shouldn't press her right now.

    But perhaps we could talk about it later.
    """

    $ psychic_details.observations.unlock('nurse_blood')

    psychic """
    Of course, sorry for bothering you.
    """

    # OLDER dialogs when this discussion happened in the late afternoon
    # $ change_room('bedroom_psychic')

    # """
    # I return to my room to rest.

    # But very quickly, the gong rings.
    # """

    # call change_time(18,30)

    # play sound dinner_gong

    # """
    # I guess I'd better join the others downstairs.
    # """    
    
    return
