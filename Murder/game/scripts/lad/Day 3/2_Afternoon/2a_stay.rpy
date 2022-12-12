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

    But I found TODO FOOD victorian food.
    """

    """
    I take a seat while she prepares the food.

    I offered to help her but she declines.

    That's probably for the best.

    It's not like I could do much anyway.
    """

    $ lad_details.add_knowledge('cook') 

    """
    When everything is ready we take our plates to the dining room.
    """

    $ change_room('dining_room')

    # TODO SWITCH PLATE? HOW INTERACTION WITH CHOICE 
    lad """
    We start to eat in silence. There is not much more we want to talk about.

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
    psychic """
    Your food? I did nothing with it.

    But I taught you might have.

    So I switched our plates before handing them to you.

    You see, I never really trusted you Mister Harring.

    It looks like I was right to do so.
    """

    """
    I try to answer, but nothings comes out of my mouth.
    
    I fall onto the ground.
    """

    #TODO sound falling sound

    $ current_character.intuitions.add('psychic_poisons')

    $ lad_day3_poisoned = True
    # TODO special action (find the poison) to unlock TRUE ending first part=> Am I the baddy ?

    return