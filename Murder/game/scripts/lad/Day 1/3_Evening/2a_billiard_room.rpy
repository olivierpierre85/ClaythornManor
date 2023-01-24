label lad_day1_evening_billiard_room:

    $ change_room('billiard_room')

    if not lad_details.saved_variables["day1_evening_billiard_room_visited"]:

        $ lad_details.saved_variables["day1_evening_billiard_room_visited"] = True

        """
        Almost everyone I saw at dinner is here.

        Except for Amelia Baxter.

        I recognize Doctor Baldwin sitting on a chair alone.

        There is also a choice of alcohol near the bar.

        The rest of the guests are grouped together. Sushil Sinha is leading the conversation.

        And the butler is silent in a corner near them.
        """

        $ lad_day1_evening_billiard_room_menu = TimedMenu([
            TimedMenuChoice('Talk to Daniel Baldwin', 'lad_day1_evening_billiard_room_doctor', 50),
            TimedMenuChoice('Approach the large group of people', 'lad_day1_evening_billiard_room_group', 10),
            # TimedMenuChoice('Ask the butler about Amelia\'s room', 'lad_day1_evening_billiard_room_butler', 20),
            # TimedMenuChoice('Ask the butler about our Lady Claythorn room', 'lad_day1_evening_billiard_room_butler', 20),
            TimedMenuChoice('Go to the bar to have a drink', 'lad_day1_evening_billiard_room_bar_1', 20),
            TimedMenuChoice('Have another drink', 'lad_day1_evening_billiard_room_bar_2', 20, condition = 'lad_details.saved_variables["day1_drinks"] == 1'),
            TimedMenuChoice('Maybe one last drink', 'lad_day1_evening_billiard_room_bar_3', 120, condition = 'lad_details.saved_variables["day1_drinks"] == 2'),
            TimedMenuChoice('Leave the room', 'lad_day1_evening_billiard_room_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ lad_day1_evening_billiard_room_menu.early_exit = False

        """
        I am back in the Billiard Room.
        """

    call run_menu(lad_day1_evening_billiard_room_menu)

    return


label lad_day1_evening_billiard_room_bar_1:

    "I approach the bar."

    "Samuel Manning is there."

    lad "Hello sir."

    drunk "..."

    "The man stares at me but makes no sound."

    broken "Don't mind him, he seems to be totally out of it."

    """
    I am startled by the man who approaches me.

    He wears one of those masks I've seen on wounded soldiers from the war.

    There were so badly injured that they have to hide their faces.

    He pretends not to notice my surprise and keeps on talking.
    """

    $ broken_details.unlock_knowledge('mask') 

    broken """
    He was already asleep when I arrived. It's impressive that he managed to still be here.

    I was seating next to him at dinner and it was impossible to have him say anything coherent.

    He could eat his food though. You could tell he is used to function like this. Poor fellow.

    Anyway, I am Thomas Moody.
    """

    $ drunk_details.unlock_knowledge('addict') 

    lad "Ted Harring, how do you do."

    broken """
    Nice to meet you mister Harring. I guess you came here for a drink.

    The choice is rather restricted I am afraid. There's only Sherry or Port.

    But luckily, I've come prepared.
    """

    """
    Before I could say anything. He reaches down his coat pocket and took a flask out. 
    
    Then he starts pouring me a glass of what looks like whisky.
    """

    broken """
    You'll probably enjoy this more.
    """

    "Well, I can't really say no to that."

    lad """
    Thanks. Cheers.
    """

    #TODO if needed for the story about drunk and puking ADD here that the drunk asks for a drink
    $ lad_details.saved_variables["day1_poisoned"] = True
    $ lad_details.saved_variables["day1_drinks"] = lad_details.saved_variables["day1_drinks"] + 1

    broken """
    Cheers Mister Harring. Now if you don't mind, I'll see what this group is talking about.
    """

    """
    He joins the group of people talking.
    """

    return

label lad_day1_evening_billiard_room_group:

    """
    I walk to the main group in the room.

    Thomas Moody, Rosalind Marsh and Lady Claythorn are listening to the older indian man.

    Even the butler, who is standing on the corner next to them looks very interested in what is being said.

    I join them.    
    """

    captain """
    Mister Haring.

    I was just telling everyone here a story.

    Where was I ?

    Oh Right.
    """

    call captain_billiard_room_speech_part_1

    """
    This appears to be a long story. 

    If I stay I might be stuck here for a while.
    """

    call run_menu(TimedMenu([
            TimedMenuChoice('Continue to listen anyway', 'lad_day1_evening_billiard_room_group_part_2', 120, early_exit = True),
            TimedMenuChoice('I would rather do something else', 'lad_day1_evening_billiard_group_cancel', 5, early_exit = True)
        ])
    )

    return

label lad_day1_evening_billiard_group_cancel:

    """
    I pretend I hear something coming from the other side of the room and leave the group quietly.
    """

    return

label lad_day1_evening_billiard_room_group_part_2:

    call captain_billiard_room_speech_part_2

    """
    Wait, that was the original question ?

    Why he is living in England ?

    It took long enough.
    """

    return

label lad_day1_evening_billiard_room_bar_2:
    """
    I really don't feel comfortable here.

    Perhaps another drink will help me relax.

    So I decide to go back to the bar and pour myself a sherry.
    """

    $ lad_details.saved_variables["day1_drinks"] = lad_details.saved_variables["day1_drinks"] + 1

    return

label lad_day1_evening_billiard_room_bar_3:
    
    """
    Well, I haven't tried the Port yet.

    It's probably better then what I am used to.

    So I pour myself one.

    It's exquisite.

    So good that it would be stupid not the drink another one.

    So I did.

    And another, ...

    And an other, ...
    """

    $ lad_details.saved_variables["day1_poisoned"] = False
    $ lad_details.saved_variables["day1_drunk"] = True
    # TODO add blur effect if drunk, puke noise... Or just black out 

    return


label lad_day1_evening_billiard_room_doctor:
      
    lad """
    Hello Doctor.
    """

    doctor """
    Mister Haring.
    """

    call doctor_generic

    return

label lad_day1_evening_billiard_room_cancel:
    
    "You don't feel like staying in this room and leave"

    scene hallway

    return