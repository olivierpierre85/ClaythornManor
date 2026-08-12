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
        I have had what I came for out of that book.

        Elisabeth Claythorn, and a title I was never given.

        There is nothing more here for me tonight.
        """

        return

    """
    A better library than the rest of the house deserves.

    A heavy book lies open on the table, left there for the guests to find, no doubt.

    'A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.'

    And there is a thought I do not much care for.

    Every person at that table knows more about my family than I do.

    I was given a house, a voice, a way of holding a fork, and not one word about the woman I am supposed to be.

    That will not do. An actress who does not know her part is only a woman in a good dress.

    I turn to the index. Clarendon, Claridge, Clark.

    Claythorn.
    """

    call library_book_content

    """
    Elisabeth.

    My name is Elisabeth, and I was born in 1865.

    Which makes me fifty-nine years old, and I have been telling myself all evening that I look my age.

    Then the rest of it, and the rest of it is worse.

    The family name is Claythorn. The title is not.

    They hold a peerage. The Earldom of Kilbraith.

    A peer is addressed by his title and never by his surname. The daughter and heir of the Earl of Kilbraith is not 'Lady Claythorn'.

    She is Lady Kilbraith.

    I have spent the whole evening introducing myself by a name that does not exist.

    And he had me learn the fork.
    """

    $ host_details.description_hidden.unlock('name_age')

    $ host_details.threads.unlock('family_history')

    """
    Very well. Panicking is for the rehearsal room.

    If anyone puts it to me, I let the villagers take the blame. They have called this house Claythorn since before I was born, and in time I simply let it stick.

    It is thin. But said with enough boredom, thin will hold.

    I close the book and set it back exactly as I found it.
    """

    return


# ------------------------------------
#   PORTRAIT GALLERY (the missing face)
# ------------------------------------
label host_portrait_gallery_default:

    $ change_room('portrait_gallery')

    if host_details.threads.is_unlocked('no_portrait'):

        """
        The Claythorns are still there, and I am still not.

        Nothing about that has improved in the last hour.
        """

        return

    """
    A dozen Claythorns in gilt frames, looking down the gallery at me with no expression I would call welcoming.

    Powdered wigs. Stiff collars. A rather fine hunting scene with a heavy-jawed gentleman in the middle of it.

    I look for something of myself in any of those faces, out of habit more than hope, and of course there is nothing.

    I walk the whole length of it twice.

    Then I understand what is wrong with this room.

    There is no portrait of the mistress of the house.

    Every one of these people had themselves painted, and the only one missing is the woman who owns the place.

    All it takes is one guest standing where I am standing, asking which one is you, Lady Claythorn.

    And I have nothing.
    """

    $ host_details.threads.unlock('no_portrait')

    """
    No. I shall have something.

    A portrait was begun in the spring and the man made me look like my own mother, so I sent it back and have not had the heart to sit again.

    That is the sort of thing a woman says about a portrait. Vain, dull, and impossible to check.

    I say it twice under my breath in the empty gallery until it sounds like something I have said before.

    But the butler ought to have thought of this before I did. I shall be having a word with him about it.
    """

    return
