label nurse_day3_morning:

    call change_time(9, 30, "Morning", "Sunday", hide_minutes=True, chapter='sunday_morning')

    $ nurse_details.add_checkpoint("nurse_day3_morning") 

    call black_screen_transition("Rosalind Marsh")

    $ change_room('bedroom_nurse', irisout)
    
    """
    I am awake before the knock.
    
    Silence. Heavy, oppressive silence.
    """

    play sound door_knock

    psychic """
    Miss Marsh? Are you in there?
    """

    nurse """
    Yes, Miss Baxter. A moment.
    """

    """
    I open the door. She looks terrified.
    """

    psychic """
    They are gone. The staff. And I think... I think others are not waking up.
    """

    nurse """
    Show me.
    """

    $ play_music('mysterious', 2)

    call nurse_day3_morning_map_menu

    $ change_room('tea_room', dissolve)
    
    """
    We gather in the tea room. Captain Sinha joins us.
    
    Three survivors. And a house full of corpses.
    """

    jump nurse_day3_afternoon
