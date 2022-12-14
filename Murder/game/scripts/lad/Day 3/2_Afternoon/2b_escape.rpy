label lad_day3_escape:

    $ change_room('manor_garden')

    call change_time(13,00, "Afternoon", "Sunday")

    # TODO captain asks about the gun room. Tell him you have it or not ?

    """
    It may be dangerous but I still prefer going with the Captain than staying in the manor.

    I feel like there is too much risk that the killer is still there.

    So we got ready and then got out in the garden.
    """

    captain """
    I don't think it's gonna be an easy walk.

    The roads must still be muddy, and if I recall well, the trip to the next house must be at least 10 miles.
    
    Maybe more.

    So it's not a gonna be picnic.
    """

    """
    And like that, he started to move towards the exit gate.
    """

    scene forest_road

    if lad_details.is_object_unlocked('gun') :

        """
        We have walked for about a hour when he stops.
        """

        lad """
        Is something wrong?
        """

        captain """
        I don't know, you tell me.
        """

        play music danger_01 fadein 2.0

        """
        I then get a gun from his back pocket and points it at me.
        """

        # TODO play music scary
        lad surprised """
        What the hell ?!
        """

        captain """
        Oh don't look so surprised.

        You don't really think I would have just let you get away so easily.
        """

        play sound gun

        $ lad_day3_ending = "gun_downed"

            # FOLLOWS TWO a gun shots, but the captain is dead too, but the killer was behind the forest and kills the captains 
    
    # TODO IF you took a gun from the gun room ! The captain will see it and wrestle you for IT
    # ?TODO find a way to load it? If it is loaded?
    # ENDING DEATH

    # IF you didn't take any gun, you'll finally reach a police station.
    # Long ending, they go back to the manor and everyone is dead
    # ENDING MIXED YOU SURVIVED GREAT, but everyone but the captain is dead.


    return