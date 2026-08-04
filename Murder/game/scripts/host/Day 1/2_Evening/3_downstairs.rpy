# Servants' floor (downstairs) for the Host (Lady Claythorn), Friday evening.
#
# She goes down for the reason nobody would guess: she wants five minutes with
# her own kind. What she finds is that the butler has drilled them so hard they
# will not come out of character even below stairs, which tells her more about
# him than anything he has said to her face.
#
#   - Kitchen:  the girl and the footman, both playing servants at a woman who
#               is playing their mistress. She learns what the staff are.
#   - Scullery: an open bottle of rat poison on the shelf (found_poison).
#   - Garage and gun room: nothing that concerns her tonight.

# ------------------------------------
#   KITCHEN (her own people)
# ------------------------------------
label host_day1_evening_kitchen:

    $ change_room('kitchen')

    if host_details.saved_variables['day1_evening_staff_seen']:

        """
        The kitchen again, and the same careful faces.

        There is nothing more for me down here.
        """

        return

    $ host_details.saved_variables['day1_evening_staff_seen'] = True

    """
    The stair down is narrow and smells of soap and coal.

    A lady does not go below stairs. A lady rings.

    But I have spent seven hours being looked at, and I should like five minutes among people who know exactly what I am.

    The range is still breathing out its heat. The girl is at the sink with her sleeves pushed up, and the footman is polishing something that does not need polishing.

    They both stand as I come in.

    Both of them. Properly. Without being told.
    """

    host """
    Please, sit down.

    There is nobody here but us.
    """

    """
    The footman glances at the door to the passage before he answers me, which is answer enough.
    """

    footman """
    We would rather stand, my lady. If it is all the same.
    """

    """
    My lady.

    Down here, with the door shut, and a dishcloth in his hand.
    """

    host """
    You needn't do that when there is no one to hear it.
    """

    maid """
    We were told, ma'am.

    From the moment we came through the gate to the moment we are through it again. No names, no letting up, not even to each other.

    He said a house is like a stage with no wings. There is nowhere to stand where you are not on.
    """

    """
    That is not a bad note, as notes go. I have had worse from better-paid men.

    And it is being obeyed, which is the part that unsettles me.

    I have worked with companies who could not hold a curtain call together, and this pair have not dropped a stitch in seven hours.
    """

    host """
    And are you managing? Truthfully.
    """

    maid """
    The plates are heavier than I thought, ma'am.

    I dropped nothing.
    """

    """
    Eighteen, if she is a day. She has the flat vowels of somewhere north of here and a rep company's way of standing with her weight on one hip, which she has almost trained out of herself.

    The footman is better. The footman is very good indeed. He is enjoying himself, and enjoying yourself is the thing that gets an actor caught.
    """

    footman """
    We shall manage, my lady. It is three days.

    And the money is the money.
    """

    """
    The money is the money.

    That is what I said to myself in a cold room in London when the letter came, and it sounded just as thin then.

    Whoever cooked that dinner is not in this room, and I do not ask where she is, because a woman who owns a house knows who cooks in it.

    So I say something dull about the fires, and I take my five minutes and leave with none of the comfort I came down for.
    """

    return


# ------------------------------------
#   SCULLERY (the bottle nobody will own)
# ------------------------------------
label host_day1_evening_scullery:

    $ change_room('scullery')

    if host_details.threads.is_unlocked('found_poison'):

        """
        The scullery, and the bottle still on its shelf where I left it.

        I have no better idea now than I had an hour ago about who put it there.
        """

        return

    """
    The scullery is cold, and smells of soda and wet stone.

    It is empty, which suits me. I want a moment where nobody is looking at me at all.

    I get it, and then I make the mistake of looking about the room.

    On the shelf above the sink, between the soap and the blacking, stands a bottle with its cork out.

    Rat poison. The label is not shy about it, and there is a good deal less in it than there should be.

    Left open. On an open shelf. Above the sink where the plates are washed.
    """

    $ host_details.threads.unlock('found_poison')

    """
    I do not touch it.

    There will be a reason. Old houses have rats, and this one has stood empty long enough to have a great many of them.

    Except that this house was shut up until this week, and a bottle half gone is a bottle somebody has been using.

    Which means one of us.

    I look at it a moment longer than is good for me, and I leave it precisely where it stands, cork out, the way I found it.

    Because if I move it, whoever put it there will know that somebody saw.

    And then I go back up the stairs rather faster than I came down them.
    """

    return


# ------------------------------------
#   GARAGE
# ------------------------------------
label host_day1_evening_garage:

    $ change_room('garage')

    """
    Petrol and cold iron, and the car we came up in standing quiet in the middle of it all.

    An old tourer, well kept.

    I sat in the back of that this morning being told who I was, and I could sit in the front of it now and be in the village by midnight.

    Nothing stopping me but a thousand pounds and my own good name, and I have never had much of the second.

    I put my hand flat on the bonnet, which is cold, and I go back inside.
    """

    return


# ------------------------------------
#   GUN ROOM
# ------------------------------------
label host_day1_evening_gun_room:

    $ change_room('gun_room')

    """
    Sporting guns behind glass, and a handgun lying out on the table as though somebody had been called away in the middle of cleaning it.

    Tomorrow there is to be a shoot, and I am expected to know one end of a gun from the other.

    I have handled a prop revolver in the second act of a thing at the Adelphi, and I do not believe that will carry me very far.

    Better not to be found down here fingering the firearms the night before.

    I leave them where they are.
    """

    return
