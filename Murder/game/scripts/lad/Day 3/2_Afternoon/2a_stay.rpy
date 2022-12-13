label lad_day3_stay:

    call change_time(13,00, "Escape", "Sunday")

    """
    I don't feel comfortable leaving Amelia Baxter alone in here.

    And in any case, I don't think I can trust to follow this guy in the forest.

    For whole all know, he very well might be the killer.

    Miss Baxter seems to think it anyway.

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

    I would like to go to actually.

    Let's meet here in a few minutes.
    """

    lad """
    Of course.
    """

    $ change_room('lad_room')

    """
    I proceed to go back to room and back as fast as I could.

    I looked frenetically around me while doing so. Checking every corner.

    When I came back, Miss Baxter is already seated at the table.
    """

    $ change_room('dining_room')
    
    lad """
    I take my place in front of her and we start eating in silence. 
    
    There is not much we want to talk about.

    After I finished my plate, I want to stand to help her do the dishes.

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

    $ lad_day3_poisoned = True
    # TODO special action (SWITCH PLATES) to unlock TRUE ending first part=> Am I the baddy ?

    return