label lad_day3_stay:
    """
    I don't feel comfortable leaving Amelia Baxter alone in here.

    After all we don't know that there is no killer left in the building.

    And in any case, I don't think I can trust to follow this guy in the forest.

    If Amelia's feeling is correct, he very well might be the killer.

    So I figure it's best we stay there, and be on our guards.

    If we are lucky, the captain will come back with reinforcements and everything will be fine.

    After a while sitting anxiously, Amelia stands up.
    """

    psychic """
    Well, no point in waiting doing nothing.

    We haven't eaten anything since this morning.

    I could check the kitchen to see if there is anything I could prepare.
    """

    lad """
    Okay, I am coming with you.
    """

    call change_room('kitchen')

    """
    I take a seat while she prepares the food.

    I offered to help her but she declines.

    That's probably for the best.
    """

    # TODO Unlock NOT a cook for the lad ???

    """
    When everything is ready we take our plates to the dining room.
    """

    call change_room('dining_hall')

    lad """
    We start to eat in silence, there is not much more we want to talk about.

    After I finished my plate, I want to stand to help Amelia Baxter do the dishes.

    Not that it really matter now.

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

    """
    That's the last thing I can say before I fall on the ground.
    """

    $ current_character.intuitions.add('psychic_poisons')

    $ lad_day3_poisoned = True
    # TODO special action (find the poison) to unlock TRUE ending first part=> Am I the baddy ?

    # Other ending, you get poisoned because the psychic knows the killer is still there in the house
    # A voice is guiding her

    return