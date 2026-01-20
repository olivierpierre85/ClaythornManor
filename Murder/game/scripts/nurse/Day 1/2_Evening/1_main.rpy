label nurse_day1_evening:

    call change_time(19,30, 'Evening', 'Friday', chapter='friday_evening')

    $ change_room("dining_room")
    
    # Run the map menu before dinner starts, simulating arrival/evening time
    call nurse_day1_evening_map_menu

    $ change_room("dining_room")
    $ play_music('jazz')

    """
    Dinner is served. The guests are a motley crew.
    
    I sit next to a young man—Ted Harring, 'The Lad'. He looks out of place. Nervous.
    
    Across from me is Captain Sinha. Alert, watchful. A military man.
    
    And Dr. Arbuthnot. I recognize the look in his eyes. He's analyzing everyone. Colleagues can be the most dangerous observers.
    """

    # Choice: Steal something
    menu:
        "Notice a silver spoon near your plate."
        
        "Slip it into your sleeve":
            $ nurse_init_variables["stole_item"] = True
            """
            With a practiced flick of the wrist, the spoon vanishes into my sleeve. 
            
            The weight is comforting against my skin. Small victories.
            """
        
        "Leave it be":
            $ nurse_init_variables["stole_item"] = False
            """
            I resist the urge. Too risky on the first night.
            """

    """
    The conversation flows around me. I contribute only when necessary.
    
    "Oh, yes, the weather is dreadful."
    "The soup is delicious."
    
    My focus is elsewhere. I am scanning for... vulnerabilities.
    """

    $ change_room("living_room")

    """
    We move to the living room for drinks.
    
    I ask for tea. The caffeine isn't good for me, but it warms my hands.
    
    Mr. Manning—the drunk—is already loud.
    
    And the Psychic, Amelia Baxter, is making a show of 'feeling vibrations'.
    """

    # Choice: Drug someone
    menu:
        "The host, Thomas Moody, seems very agitated."

        "Slip a mild sedative into his drink":
            $ nurse_init_variables["drugged_guest"] = True
            """
            While he turns to speak to the maid, I lean over. A tiny pinch of powder from my ring.
            
            It will help him sleep. He needs it. I am doing him a favor.
            """
            
        "Do nothing":
            $ nurse_init_variables["drugged_guest"] = False
            """
            Not my place. Let him differ.
            """

    """
    Sudden exhaustion hits me like a physical blow. My chest tightens.
    
    I need to lie down. Now.
    """

    nurse """
    If you will excuse me, the journey has tired me out. I must retire.
    """

    $ change_room("bedroom_nurse")
    
    """
    Safe in my room. I lock the door.
    
    I take my own medicine. Bitter, but necessary.
    
    Tomorrow is another day.
    """

    jump nurse_day2_morning
