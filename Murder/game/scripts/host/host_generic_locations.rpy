# Generic Host location visits.
# Used for places that can be visited on multiple days with the same options.

label host_dining_room_default:

    $ change_room('dining_room')

    """
    The table has already been cleared.

    It looks good, considering the small number of staff.
    """

    return


label host_entrance_hall_default:

    $ change_room('entrance_hall')

    """
    The hall, empty, with the lamps turned low.

    I notice the carpet has worn thin along the line a footman would walk, and the brass could do with attention.

    Not what one would expect from a well kept house.

    Hopefully, nobody will think too much of it.
    """

    return


label host_servant_stairs_default:

    $ change_room('servant_stairs')

    """
    The narrow stair the staff use, with a footman's livery hanging on its peg.

    There is nothing for me to do here.
    """

    return

label host_library_default:

    $ change_room('library')

    if host_details.threads.is_unlocked('family_history'):

        """
        I have learned all I needed from the book on the table.

        There is nothing more for me here.
        """

        return

    """
    A better library than I expected.

    A heavy book lies open on the table.

    I assume it is the one left out for me, so that I might learn about this place.

    'A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.'

    I turn to the index. Clarendon, Claridge, Clark.

    Claythorn.
    """

    call library_book_content

    """
    Elisabeth.

    My name is Elisabeth, and I was born in 1865.

    Which makes me fifty-nine years old, and I have been telling myself all evening that I look my age.

    Then, something strange.

    The family name is Claythorn. The title is not.

    They hold a peerage. The Earldom of Kilbraith.

    The daughter and heir of the Earl of Kilbraith is not 'Lady Claythorn'.

    She is Lady Kilbraith.

    That is a small mistake. Still, I should be prepared if anyone else makes the same realisation I did.

    I think of a few explanations and land on one that should satisfy anyone who asks.

    But I doubt that will happen.

    I close the book and leave the room.
    """

    $ host_details.threads.unlock('family_history')

    return


label host_portrait_gallery_default:

    $ change_room('portrait_gallery')

    if host_details.threads.is_unlocked('no_portrait'):

        """
        The portraits are still there, and not one of them wears my face.

        Nothing about that has changed.
        """

        return

    """
    A dozen Claythorns in gilt frames, looking down the gallery.

    Many generations of people who have lived and died at Claythorn Manor.

    Then a sudden realisation dawns on me.

    There is no portrait of me, the supposed mistress of the house.

    Not impossible in itself, but I should think of a good excuse.

    If somebody asks me about it, I ought to be ready.
    """

    $ host_details.threads.unlock('no_portrait')

    return
