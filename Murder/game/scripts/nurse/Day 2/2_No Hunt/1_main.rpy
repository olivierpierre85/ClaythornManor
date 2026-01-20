label nurse_day2_no_hunt:

    call change_time(14,00, 'Afternoon', 'Saturday', hide_minutes = True, chapter='saturday_afternoon_no_hunt')

    $ change_room("living_room")

    """
    Silence descends on the manor as the hunters depart.
    
    The air feels lighter. Or maybe it's just the absence of testosterone.
    """

    call nurse_day2_no_hunt_map_menu

    """
    I end up in the living room.
    
    Dr. Arbuthnot is here too. He didn't go hunting either.
    """

    doctor """
    Miss Marsh. You look... pale. Are you quite alright?
    """

    nurse """
    I am fine, Doctor. Just a bit of fatigue.
    
    (He notices everything. Dangerous.)
    """

    """
    We talk shop for a while. He is knowledgeable, I'll give him that.
    """

    jump nurse_day2_evening
