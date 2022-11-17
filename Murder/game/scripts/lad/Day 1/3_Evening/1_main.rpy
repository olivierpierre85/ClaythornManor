# --------------------------------------------
#               Ted Harring
#           Friday 21:00 Evening
#
#   Alive: Everyone
label lad_day1_evening:

    call change_time(21,00, 'Evening')

    scene hallway

    "He takes me through the grand staircase, on to the first floor."

    footman """
    There you go sir.

    You have the 'William The Conqueror' room.

    I hope it's to your liking.
    """

    call unlock_map('lad_room')

    $ change_room('lad_room')

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

    $ play_music('upbeat')

    $ time_left = 120

    call run_menu(lad_map_menu)

    call change_time(23,00)

    "I am feeling tired. It's probably best if I go to bed now."

    $ change_room('lad_room')

    "NOW WHAT ??? You Notice something on your bed. a letter."

    # TODO play music SCARY

    # SHOW PNG LETTER.

    if lad_day1_poisoned:

        jump lad_ending_day1_poisoned

    else:

        jump lad_day2_morning

label lad_day1_evening_host_room:
    
    scene hallway

    "I knock on the door."

    psychic "Yes ?"

    lad """
    Lady Claythorn, it's Ted Harring.

    I was hoping we could talk?   
    """

    host """
    I am sorry, but it's a very bad time mister Harring.

    Why don't you meet the others in the billiard room?.
    """

    return

label lad_day1_evening_psychic_room:
  
    scene hallway

    "I knock on the door."

    psychic "Yes ? Who is it ?"

    lad "Hi, it's Ted Harring."

    psychic """
    Oh. What do you want mister Harring?
    """
    
    lad """
    I am not sure. But maybe we could continue our conversation from earlier.
    """

    psychic "Oh Mister Harring. I am afraid I was getting ready to bed. We can talk again tomorrow."

    lad "Of course, I am sorry."

    return

label lad_day1_evening_cancel:
    return