label nurse_introduction:

    call change_time(17,30, 'Afternoon', 'Friday', hide_minutes = True, chapter='friday_afternoon')

    call black_screen_transition("", "Rosalind Marsh")

    $ change_room("train_inside")

    play sound train_moving loop

    $ play_music('chill')

    """
    The rhythm of the train tracks usually soothes me. Today, it merely accentuates the pounding in my temples.
    
    I press a handkerchief to my lips. When I pull it away, I check for spots of red. Clean. For now.
    """

    nurse """
    (Keep it together, Rosalind. Just a weekend. A simple weekend in the country.)
    """

    """
    I look at the letter again. "Exceptional Act of Bravery." 
    
    They dug up my service record from the Great War. Or maybe from the Boxer Rebellion. It doesn't matter.
    
    The prize money does. 
    
    Treatment is expensive. The specialized clinics in Switzerland, the experimental tonics... they all require funds I no longer have.
    """

    play sound train_stopping

    $ change_room("train_station")

    pause 2.0

    """
    The cold air of the station hits my lungs like shattered glass. I stifle a cough, straightening my coat.
    
    A man approaches. Uniformed. Efficient.
    """

    footman """
    Miss Marsh? For Claythorn Manor?
    """

    nurse """
    That is correct.
    """

    """
    I hand him my luggage. He takes it without a word. I appreciate the silence. Chatter drains what little energy I have left.
    """

    $ change_room("inside_car")

    """
    The car ride is bumpy. Every jolt sends a dull ache through my joints.
    
    I open my bag, checking my supplies. Vials, pills, bandages. My lifeline.
    
    And... other things. Just in case. One can never be too prepared.
    """

    footman """
    We are almost there, Miss.
    """

    """
    The manor looms ahead. It's grand, imposing. Also isolating.
    
    Perfect for a rest. Or for something else entirely.
    """

    $ stop_music()
    
    play sound thunder loop
    
    $ change_room("manor_exterior")

    """
    I step out. The butler welcomes me. I force a polite smile, though it feels brittle on my face.
    """

    stop sound fadeout 2.0

    pause 2.0

    jump nurse_day1_evening
