label lad_day1_evening:

    call change_time(21,00)

    scene hallway

    "He takes me through the grand staircase, on to the first floor."

    call change_floor(2)

    footman """
    There you go sir.

    You have the 'William The Conqueror' room.

    I hope it's to your liking.
    """

    call unlock_map('lad_room')

    scene bedroom_lad

    """
    I enter the bedroom. 
    
    It's bigger than my apartment. And more luxurious than I could have dreamed of.
    """

    lad "That will do great, thank you."

    """
    The footman exits the room.

    I look around me in disbelief.
    
    After a while I unpack my small luggage.

    Well that didn't take long. So what do I do now ?

    """

    $ time_left = 120

    $ lad_day1_evening_menu = TimedMenu([
        TimedMenuChoice('Go knock on the the door of Amalia Baxter', 'lad_day1_evening_psychic_room', 55, room = 'psychic_room'),
        TimedMenuChoice('Meet the others in the billiard room', 'lad_day1_evening_billiard_room', 0, keep_alive = True, room = 'billiard_room'),
        TimedMenuChoice('Library', 'lad_day1_evening_library', 40, room = 'library'),
        TimedMenuChoice('Go to sleep', 'lad_day1_evening_cancel', early_exit = True, room = 'lad_room')
    ], is_map = True)

    call run_menu(lad_day1_evening_menu)

    call change_time(23,00)

    "I am feeling tired. It's probably best if I go to bed now."

    scene bedroom_lad

    "NOW WHAT ??? You Notice something on your bed. a letter."

    # TODO play music SCARY

    # SHOW PNG LETTER.

    if lad_day1_poisoned:

        jump lad_ending_day1_poisoned

    else:

        jump lad_day2_breakfast


label lad_day1_evening_library:

    scene library
    
    """
    It's a very nice library. But what am I doing here ? I can barely read.

    """

    $ lad_details.add_knowledge('education')

    """
    There is an open book on a small table.

    \"A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.\"

    Yeah, I am not reading that.

    I probably better go elsewhere.

    """
    # TODO add info on BOOK ???

    return

label lad_day1_evening_psychic_room:
  
    scene hallway

    "I knock on the door."

    psychic "Yes ? Who is it ?"

    lad "Hi, it's Ted Harring. I thought we could continue our conversation from earlier."

    psychic "Oh Mister Harring. I am afraid I was getting ready to bed. We can talk again tomorrow."

    lad "Of course, I am sorry."

    return

label lad_day1_evening_cancel:
    return