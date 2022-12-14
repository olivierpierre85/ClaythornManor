label lad_day3_stay:

    call change_time(13,00, "Afternoon", "Sunday")

    """
    I don't feel comfortable leaving Amelia Baxter alone in here.

    And in any case, I don't like the idea to be alone with this guy in the forest.

    For whole all know, he very well might be the killer.

    Miss Baxter doesn't seem to trust him anyway.

    So I figure it's best we stay there, and be on our guards.

    If we are lucky, the captain will come back with reinforcements and everything will be fine.
    """

    pause 2.0

    """
    After a while sitting anxiously, Amelia stands up.
    """

    psychic """
    Well, no point in waiting doing nothing.

    We haven't eaten anything since yesterday.

    I could check the kitchen to see if there is anything I could prepare.
    """

    lad """
    Okay, I am coming with you.
    """

    $ change_room('kitchen')

    """
    We looked around to find something.
    """

    psychic """
    There is not much.

    But I think I can manage a light luncheon if you are not picky.
    """

    """
    I take a seat while she prepares the food.

    I offer to help but she declines.

    That's probably for the best.

    It's not like I could do much anyway.
    """

    $ lad_details.unlock_knowledge('cook') 

    $ change_room('dining_room')

    """
    When everything is ready I offer to carry the plates to the dining room.

    I put them on the table at our usuals places.

    Then I excuse myself.
    """

    psychic """
    Where are you going mister Harring?

    It's better that we stick together at all time.
    """

    lad """
    I understand, but there is one thing I need to do alone.

    You see, we haven't left each other company the whole day and...
    """

    psychic """
    Say no more, I understand.

    I guess this was inevitable. 

    I would like to go too actually.

    Let's meet here in a few minutes.
    """

    lad """
    Of course.
    """

    pause 1.0

    scene hallway

    """
    I accompany Miss Baxter to her room.
    """

    psychic """
    That is where we split up.

    We can meet again in the dining room in a few minutes.
    """


    if lad_details.is_intuition_unlocked('psychic_poisons'):

        """
        I see her enter her room but as I was supposed to reach mine, some weird feeling overwhelms me. 

        I don't know what it is but it tells me to not go to my room.

        That I should go back to the dining room, now.

        What should I do?
        """

        $ time_left = 1
        call run_menu( TimedMenu([
            TimedMenuChoice('I am being paranoid. Besides I can\'t hold it any longer', 'lad_day3_afternoon_toilet', early_exit = True ),
            TimedMenuChoice('Go back downstairs', 'lad_day3_afternoon_no_toilet', early_exit = True)
            ])
        )
    else:

        call lad_day3_afternoon_toilet

    return

label lad_day3_afternoon_toilet:

    """
    I see her enter her room then I head to mine.

    As I am walking in the hallway, I am looking frenetically around me.

    It feels like someone could jump from a corner at any moment.

    I better not waste any time.
    """   

    $ change_room('lad_room')

    pause 2.0

    """
    Once I am done, I try to hurry back as fast as I could, almost running down the stairs. 
    """

    $ change_room('dining_room')
    
    """
    But when I came back, Miss Baxter is already seated at the table.

    She was even faster than I was.

    She must be scared too.
    """

    pause 1.0

    """
    I take my place in front of her and we start eating in silence. 
    
    There is not much we want to talk about.

    After I finished my plate, I offer to help her do the dishes.

    Not that it really matters now.

    It's just something more to do while waiting.

    But as soon I stand up, I realize I can't stay on my feet.

    My head is dizzy. 

    I feel that I am about to faint.

    I look to Amelia Baxter.

    She observes me with a blank stare, not surprised by my reaction.
    """

    lad """
    What... did ... you do ... to my food ???
    """

    # psychic """
    # Your food? I did nothing with it.

    # But I taught you might have.

    # So I switched our plates before handing them to you.

    # You see, I never really trusted you Mister Harring.

    # It looks like I was right to do so.
    # """

    """
    I try to keep on talking. But no sound comes out of my mouth.
    
    I fall on the ground.
    """

    play sound body_fall

    $ lad_details.unlock_intuition('psychic_poisons')

    $ lad_day3_ending = "poisoned"

    return

label lad_day3_afternoon_no_toilet:
    
    """
    Instead of going to my room, I go down the stairs and back into the dining room.
    """

    $ change_room('dining_room')

    """
    Then, I try to make sense of what is happening.

    I am putting my trust on a eccentric older lady because I don't think she could hurt me.

    Not directly at least.

    But she could do it in a more subtle way.

    I look at our plates, they look normal to me.

    And I was with her the whole time, so there is no way she could have tampered with.

    At least I think.

    Just to be sure, I could switch them.

    It's probably for nothing, but it's better to be safe than sorry.

    So I trade plates and sat down at my place, waiting for Miss Baxter to return.
    """

    pause 2.0

    """
    She comes back, very soon herself.

    She couldn't have stayed very long in her room.

    But that make sense, she must be terrified.
    """

    pause 1.0

    """
    I take my place in front of her and we start eating in silence. 
    
    There is not much we want to talk about.
    """

    

    $ lad_day3_ending = "survived"

    return