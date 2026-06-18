label lad_day1_evening_billiard_room:

    $ change_room('billiard_room')

    if not lad_details.saved_variables["day1_evening_billiard_room_visited"]:

        $ lad_details.saved_variables["day1_evening_billiard_room_visited"] = True

        """
        Except for Amelia Baxter, everyone from dinner is in this room.

        I recognise Dr Baldwin sitting alone in a chair.

        There's also an array of alcohol near the bar.

        The rest of the guests are clustered together, with Sushil Sinha leading the conversation.

        The butler stands silently in a corner near them.
        """

        $ lad_day1_evening_billiard_room_menu = TimedMenu("lad_day1_evening_billiard_room_menu", [
            TimedMenuChoice('Talk to Daniel Baldwin', 'lad_day1_evening_billiard_room_doctor', 0, next_menu='doctor_generic_menu_lad'),
            TimedMenuChoice('Approach the large group of people', 'lad_day1_evening_billiard_room_group', 0, next_menu='lad_day1_evening_billiard_room_group'),
            TimedMenuChoice('Go to the bar to have a drink', 'lad_day1_evening_billiard_room_bar_1', 20, linked_choice='lad_day1_evening_billiard_room_bar_2'),
            TimedMenuChoice('Have another drink', 'lad_day1_evening_billiard_room_bar_2', 20, condition = 'lad_details.saved_variables["day1_drinks"] == 1', linked_choice='lad_day1_evening_billiard_room_bar_3'),
            TimedMenuChoice('Maybe one last drink', 'lad_day1_evening_billiard_room_bar_3', 120, condition = 'lad_details.saved_variables["day1_drinks"] == 2'),
            TimedMenuChoice('Leave the room', 'lad_day1_evening_billiard_room_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ lad_day1_evening_billiard_room_menu.early_exit = False

        """
        I am back in the billiard room.
        """

    call run_menu(lad_day1_evening_billiard_room_menu)

    return


label lad_day1_evening_billiard_room_bar_1:

    $ lad_details.threads.unlock('whisky')

    """
    I approach the bar.

    Samuel Manning is there.
    """

    call common_day1_evening_moody_offers_harring_flask

    #TODO if needed for the story about drunk and puking ADD here that the drunk asks for a drink
    $ lad_details.saved_variables["day1_drinks"] = lad_details.saved_variables["day1_drinks"] + 1

    return

label lad_day1_evening_billiard_room_group:

    """
    I walk towards the main group in the room.

    Thomas Moody, Rosalind Marsh and Lady Claythorn are listening to the older Indian man.

    Even the butler, who is standing in the corner next to them, looks very interested in what is being said.

    I join them.    
    """

    captain """
    Mr Harring.

    I was just telling everyone here a story.

    Where was I?

    Oh, right.
    """

    call common_day1_evening_captain_billiard_room_speech_part_1

    """
    This appears to be a long story. 

    If I stay, I might be stuck here for a while.
    """

    call run_menu(TimedMenu("lad_day1_evening_billiard_room_group", [
            TimedMenuChoice('Continue to listen anyway', 'lad_day1_evening_billiard_room_group_part_2', 60, early_exit = True),
            TimedMenuChoice('I would rather do something else', 'lad_day1_evening_billiard_group_cancel', 10, early_exit = True)
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

    Why is he living in England?

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
    """

    """
    So I do.

    And another...

    And another...
    """

    
    show layer master at drunk_wobble_layer
    $ drunk_mode = True

    $ lad_details.threads.unlock('day1_drunk')
    # TODO add blur effect if drunk, puke noise... Or just black out 

    return


label lad_day1_evening_billiard_room_doctor:
      
    lad """
    Hello Doctor.
    """

    doctor """
    Mr Harring.
    """

    call doctor_generic

    return

label lad_day1_evening_billiard_room_cancel:

    """
    I don't feel like staying in this room.
    """

    return