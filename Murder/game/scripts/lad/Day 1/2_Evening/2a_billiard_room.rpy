label lad_day1_evening_billiard_room:

    $ change_room('billiard_room')

    if not lad_details.saved_variables["day1_evening_billiard_room_visited"]:

        $ lad_details.saved_variables["day1_evening_billiard_room_visited"] = True

        """
        Except for Amelia Baxter, everyone I saw at dinner is in this room.

        I recognize Doctor Baldwin, sitting alone on a chair.

        There's also an array of alcohol near the bar.

        The remainder of the guests are clustered together, with Sushil Sinha leading the conversation.

        The butler stands silently in a corner near them.
        """

        $ lad_day1_evening_billiard_room_menu = TimedMenu("lad_day1_evening_billiard_room_menu", [
            TimedMenuChoice('Talk to Daniel Baldwin', 'lad_day1_evening_billiard_room_doctor', 10),
            TimedMenuChoice('Approach the large group of people', 'lad_day1_evening_billiard_room_group', 10),
            TimedMenuChoice('Ask the butler about Amelia\'s room', 'lad_day1_evening_billiard_room_butler', 20, condition = 'not is_unlock_map("bedroom_psychic")'),
            TimedMenuChoice('Go to the bar to have a drink', 'lad_day1_evening_billiard_room_bar_1', 20, linked_choice='lad_day1_evening_billiard_room_bar_2'),
            TimedMenuChoice('Have another drink', 'lad_day1_evening_billiard_room_bar_2', 20, condition = 'lad_details.saved_variables["day1_drinks"] == 1', linked_choice='lad_day1_evening_billiard_room_bar_3'),
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

    $ lad_details.important_choices.unlock('whisky')

    """
    I approach the bar.

    Samuel Manning is there.
    """

    lad """
    Hello sir.
    """

    drunk """
    ...
    """

    """
    The man stares at me but makes no sound.
    """

    broken """
    Don't mind him, he seems to be totally out of it.
    """

    """
    I am startled by the man who approaches me.

    He wears one of those masks I've seen on wounded soldiers from the war.

    There were so badly injured that they have to hide their faces.

    He pretends not to notice my surprise and keeps on talking.
    """

    $ broken_details.description_hidden.unlock('mask') 

    broken """
    He was already asleep when I arrived. It's impressive that he managed to still be here.

    I was seating next to him at dinner and it was impossible to have him say anything coherent.

    He could eat his food though. You could tell he is used to function like this. Poor fellow.

    Anyway, I am Thomas Moody.
    """

    $ drunk_details.description_hidden.unlock('addict') 

    lad """
    Ted Harring, how do you do.
    """

    broken """
    Nice to meet you mister Harring. I guess you came here for a drink.

    The choice is rather restricted I am afraid. There's only Sherry or Port.

    But luckily, I've come prepared.
    """

    """
    Before I could say anything, he reaches into his coat pocket and pulls out a flask.
    
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
    $ lad_details.saved_variables["day1_drinks"] = lad_details.saved_variables["day1_drinks"] + 1

    broken """
    Cheers, Mister Harring. Now if you don't mind, I'll see what this group is talking about.
    """

    """
    He joins the group of people talking.
    """

    return

label lad_day1_evening_billiard_room_group:

    """
    I walk towards the main group in the room.

    Thomas Moody, Rosalind Marsh and Lady Claythorn are listening to the older Indian man.

    Even the butler, who is standing on the corner next to them looks very interested in what is being said.

    I join them.    
    """

    captain """
    Mister Harring.

    I was just telling everyone here a story.

    Where was I?

    Oh Right.
    """

    call common_day1_evening_captain_billiard_room_speech_part_1

    """
    This appears to be a long story. 

    If I stay, I might be stuck here for a while.
    """

    call run_menu(TimedMenu("lad_day1_evening_billiard_room_group", [
            TimedMenuChoice('Continue to listen anyway', 'lad_day1_evening_billiard_room_group_part_2', 120, early_exit = True),
            TimedMenuChoice('I would rather do something else', 'lad_day1_evening_billiard_group_cancel', 5, early_exit = True)
        ])
    )

    return

label lad_day1_evening_billiard_group_cancel:

    """
    I pretend to hear something coming from the other side of the room and quietly leave the group.
    """

    return

label lad_day1_evening_billiard_room_group_part_2:

    call common_day1_evening_captain_billiard_room_speech_part_2

    """
    Wait, that was the original question?

    Why he is living in England?

    That sure took long enough.
    """

    return

label lad_day1_evening_billiard_room_bar_2:

    """
    I really don't feel comfortable here.

    Perhaps another drink will help me relax.

    So, I decide to go back to the bar and pour myself a sherry.
    """

    $ lad_details.saved_variables["day1_drinks"] = lad_details.saved_variables["day1_drinks"] + 1

    return

label lad_day1_evening_billiard_room_bar_3:
    
    """
    Well, I haven't tried the Port wine yet.

    It's probably better than what I'm used to.

    So, I pour myself a glass.

    It's exquisite.

    So good that it would be foolish not to have another one.

    So I do.

    And another...

    And another...
    """

    $ lad_details.important_choices.unlock('day1_drunk')
    # TODO add blur effect if drunk, puke noise... Or just black out 

    return


label lad_day1_evening_billiard_room_doctor:
      
    lad """
    Hello Doctor.
    """

    doctor """
    Mister Harring.
    """

    call doctor_generic

    return

label lad_day1_evening_billiard_room_cancel:
    
    """
    I don't feel like staying in this room.
    """

    return

label lad_day1_evening_billiard_room_butler:

    """
    I approach the butler.
    """

    lad """
    Hello, I was wondering if you could help me.
    """

    butler """
    Of course, Mr. Harring.

    What is it?
    """

    lad """
    I would like to talk to Miss Baxter.

    Do you know where her room is?
    """

    butler """
    I certainly do.

    But I'm not sure that I should tell you.

    That's not very appropriate.
    """

    lad """
    Hmm, well, no, it's nothing like that. 

    I'd just like to finish the conversation we had earlier.

    I'm sure Miss Baxter won't mind.
    """

    butler """
    Well, I suppose it's not a big secret whose rooms are whose.

    So, I might as well tell you.

    She is in the "Elizabeth I" room.
    """

    $ unlock_map('bedroom_psychic')

    lad """
    Thank you.
    """

    return