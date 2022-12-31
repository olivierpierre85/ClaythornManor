label lad_day2_evening:
    $ lad_details.add_checkpoint("lad_day2_evening") 
    
    # call black_screen_transition("Day 2 - Evening") # Good ?
    $ change_room('dining_room') 

    call change_time(18,30, "Evening", "Saturday")

    """
    When I enter the room, the mood is rather gloom.

    Daniel Baldwin and Thomas Moody seats are empty.

    And Samuel Manning is not there either. 

    I take my usual seat, with only Amelia Baxter next to me now.
    """

    host """
    Now that everyone is here. I want to say how sorry I am for what happened today.

    It's not how I imagine this week-end would be.

    I don't think any of us want more entertainment at this point.

    So tomorrow morning, you'll receive your rewards.
    
    Then we will wait until the police arrives.

    You'll be free to go back home as soon as the officers will say so.

    In the meantime, enjoy your meal.

    Afterwards, drinks will be available in the billiard room like yesterday. 
    """

    """
    The food arrives right after the speech.

    But none of us have much of an appetite.
    """

    lad """
    Miss Baxter, I don't see Samuel Manning here.

    Do you know where he is ?
    """

    psychic """
    Locked in his room, that's where he is.
    """

    lad """
    Really, how come ?
    """

    psychic """
    While you were away, we had a heated discussion of what to do with him.

    Some were to attach him to a chair, other to let him be free.
    
    In the end, Captain Sinha thought it was better to lock him in his room.

    At least he didn't object.

    He is there now. 

    It was agreed that his dinner will be served there.
    """    

    """
    Alright. That's one fewer thing to be concerned about I guess.

    None of us has much will to make small talk.

    So we eat in silence.

    When dinner is over, most people retreat to their room.

    I doubt a lot of them will want to discuss over drinks now.

    What will I do ?
    """

    play music sad_01 fadein 5.0 # TODO music

    call change_time(21,00)

    $ time_left = 90

    call run_menu(lad_map_menu)

    call change_time(22,30)

    stop music fadeout 5.0

    if lad_day2_drunk:

        """
        Gee, I am not thinking straight.

        I rush to my room.
        """

        $ change_room('lad_room')

        """
        I quickly reach the toilet and puke all I have been drinking.

        I better go to bed now.
        """

        if lad_day1_drunk:
            """
            Alright, two days in a row.

            What does it say about me?
            """

            $ lad_details.unlock_knowledge('poor_drinker') 

            # TODO achievement. DRUNK OR CHEATED DEATH IF drank poison

        """
        I fell asleep as soon as I lay on my bed.
        """
    
    else:

        """
        I am tired of wandering inside this house.

        Beside, with all that happened today, I am exhausted.

        I should go back to my room.
        """

        $ change_room('lad_room')

        """
        Before trying to sleep, I better move the some furniture in front of the door.

        It's better to be careful.
        """

        play sound moving_furniture
        
        pause 2.0

        """
        Ok, that should do it.

        I can rest peacefully now.
        """

    jump lad_day3_morning

label lad_day2_evening_sleep:

    return

label lad_day2_broken_room_back:

    $ change_room('broken_room')

    """ 
    My conversation with Sushil made me think.

    Maybe I should try to drink from the flask.

    At least I would now for sure if something is not right.

    I reach for the flask next to the nightstand.

    It's empty now.

    All of its contents is lying on the nightstand, and some on the floor.

    I could lick some of it.

    But even I am not so low class as this.

    I will just wait for the experts to have an answer.
    """    

    return



label lad_day2_doctor_room:

    $ change_room('doctor_room') 

    """
    I didn't have the time earlier to take a good look at the room.

    It feels a little weird being in here, but I might as well look for something useful.

    I search his personal effects when I stubble into his medication suitcase.

    There is nothing out of the ordinary in there.

    A stethoscope, bandages, a few bottle of medications,...

    There is one in particular that he has more that the others. 
    
    Laudanum is written on the label.

    He has almost a dozen of those bottles.

    Laudanum... , I heard that before.
    
    It's opium.

    Looks like the doctor wasn't using it only on patients.
    """

    $ doctor_details.unlock_knowledge('addict') 

    """
    Just in case, I might as well take a few for myself.
    """

    # TODO is the lad a thief ? likely ADD HERE
    # TODO add LAUDANUM IN THE OBJECTS LIST?

    return
    
