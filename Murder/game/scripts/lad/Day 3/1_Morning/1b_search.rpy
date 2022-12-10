# LAST DAY we can search EVERYWHERE
# FOR special rooms not visited before, KEEP THEM or not ?
# FIRST lets forget all special room

label lad_day3_morning_garden:

    $ change_room('manor_garden')
    
    """
    We go out into the garden to check.

    But there is no trace of anyone.

    Lady Claythorn car is not there either.
    """

    return

label lad_day3_morning_kitchen:

    $ change_room('kitchen')

    if lad_day2_believe_psychic:
        psychic """
        You see.

        There is no one here.

        Even though breakfast should be ready soon.
        """

        lad """
        Ok I admit that is very strange indeed.
        """

    #TODO LOOK AROUND and Might find poison is choice ?????
    
    return

label lad_day3_morning_gun_room:

    $ change_room('gun_room')

    lad """
    Nobody is here.
    """

    psychic """
    No indeed.

    But it might be useful to get a weapon for protection you don't think?
    """

    """
    Well, I don't have a lot of experience with guns.

    It might be a bad idea.

    But on the other hand, I don't know what we might encounter here.
    """

    call run_menu(TimedMenu([
        TimedMenuChoice('Sure, I need a gun. It doesn\'t matter I don\'know how to use it', 'lad_day3_take_gun',early_exit=True),
        TimedMenuChoice('I would rather not. I could hurt myself.', 'lad_day3_no_gun', early_exit=True), 
    ]))

    return

label lad_day3_take_gun:

    lad """
    You are right.

    We better get something to defend ourselves.
    """

    """
    Hunting rifles are a bit too large.

    But I spot a revolver that fits my pocket.
    """

    lad """
    Alright, I'll take this with me.

    But there are no bullets in it.
    """

    psychic """
    Sometimes, bullets are being kept separated from the guns.

    It makes it less likely to have an accident.
    """

    lad """
    Where could they be then?
    """

    psychic """
    No idea.

    But even empty, the gun can still scare away someone.
    """

    """
    I guess.

    But it's not very reassuring.
    """

    return

label lad_day3_no_gun:

    lad """
    No I don't think so.

    We might end up hurting ourselves.
    """

    psychic """
    Alright, if that is what you want.
    """

    return

label lad_day3_morning_scullery:

    $ change_room('scullery')

    """
    Wait, what the hell is a scullery?
    """

    lad """
    Do you know what room this is?
    """

    psychic """
    The scullery.

    That's mainly where they wash the dishes.

    If you look down the sink full, there are a lot of dirty dishes.
    
    It seems nobody cleaned after supper yesterday.
    """

    return


label lad_day3_morning_garage:

    $ change_room('garage')

    """
    The garage.

    That's where lady Claythorn car should be.

    But instead there is only parts of other cars and an old model in a shabby state.
    """

    lad """
    Do you come here in this car?
    """

    psychic """
    No, of course not.
    
    Lady Claythorn's chauffeur drove us here in a Rolls Royce.

    Not in this old thing.
    """

    lad """
    Yeah me too.
    """

    lad """
    But if everyone has left, we might need it if we want to leave too.
    """

    psychic """
    Right. But do you know how to drive that?

    Because I sure can't.
    """

    $ psychic_details.add_knowledge('drive')

    lad """
    Not really, no.

    I never learn how to drive.
    """

    """
    It's not like I could afford a car anyway.
    """

    $ lad_details.add_knowledge('drive')

    $ lad_day3_seen_car = True

    return