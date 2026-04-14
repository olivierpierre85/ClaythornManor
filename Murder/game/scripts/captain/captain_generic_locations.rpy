# Generic Captain location visits.
# Used for places that can be visited on multiple days with the same options.

label captain_library_default:

    $ change_room('library')

    if captain_details.saved_variables.get("visited_library"):

        if captain_details.threads.is_unlocked('captain_host_suspicion_name'):

            """
            The library is as I left it.

            I have already read what I needed from the genealogy book.

            There is nothing more here for me.
            """

            return

        else:

            """
            The library is as I left it.

            The genealogy book still lies open on the table, waiting.
            """

    else:

        $ captain_details.saved_variables["visited_library"] = True

        """
        A well-stocked library. The kind one would expect in a house like this.

        A book lies open on a table.

        'A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.'

        The eighth edition, printed in 1894.

        I remember dreaming of seeing my name in such a book.

        I know now that it will never happen.
        """

    call run_menu(
        TimedMenu("captain_library_menu", [
            TimedMenuChoice('Look up the Claythorns in the index', 'captain_library_read', 30, early_exit=True),
            TimedMenuChoice('Leave the book be', 'generic_cancel', 10, early_exit=True)
        ])
    )

    return


label captain_library_read:

    """
    I glance through a few pages.

    Let us see if the Claythorns are mentioned.

    I search through the index. Clarendon, Claridge, Clark...

    Claythorn.

    There are several entries. I find the one concerning this manor.
    """

    book """
    Nicholas Claythorn, of Claythorn Manor, 3rd Earl of Kilbraith, .

    Born on June 22, 1813.

    His parents were Nicholas Claythorn, 2nd Earl of Kilbraith, and Agnes Cicely.

    With Mary Kirwan, his wife, he fathered one son and one daughter:

    1. Elisabeth, his heir, born in 1865.

    2. Andrew, born in 1867, died in 1869.

    Lineage...
    """

    """
    I read the entry twice.

    There it is. The family name is Claythorn, but their title is not.

    They hold a peerage — the Earldom of Kilbraith. Their seat is this manor, but the title is quite separate.

    A peer is addressed by his title, not by his surname. The Earl of Kilbraith is styled 'Lord Kilbraith', and his countess, 'Lady Kilbraith'.

    Never 'Lord Claythorn'. Never 'Lady Claythorn'.

    Still, I should not leap to conclusions.

    It is not unheard of for a family to set the formal title aside in daily use. Since the war, I have heard of peers who have grown weary of ceremony.

    Or perhaps it is a local habit. The villagers call her 'Lady Claythorn' after the name of the house, and in time she has simply let it stick.

    And yet, it is something strange enough that I should not dismiss it entirely.
    """

    $ captain_details.threads.unlock('captain_host_suspicion_name')

    """
    I close the book and place it back on the table.

    Interesting. Very interesting indeed.
    """

    return


label captain_portrait_gallery_default:

    $ change_room('portrait_gallery')

    if captain_details.threads.is_unlocked('captain_host_suspicion_portrait'):

        """
        The Claythorn forebears still gaze down from their frames, silent and stern.

        The absence of our host's portrait remains as striking as before.

        There is nothing more the gallery can tell me.
        """

        return

    """
    A gallery of family portraits lines the walls.

    The Claythorn lineage, rendered in oil and gilt frames.

    I study the faces. Old money, passed down through blood.

    There are perhaps a dozen portraits here, spanning several generations.

    Stern-looking gentlemen in powdered wigs. Ladies in elaborate gowns.

    But then something strikes me.

    None of them resemble our host.

    Where is Lady Claythorn?

    If she is the current mistress of this house, her portrait ought to hang here alongside her forebears.

    And yet there is nothing.

    In itself, that doesn't mean much.

    It could be a personal preference, or perhaps she had difficulty persuading a decent artist to come all the way out here.

    Still, I will keep that in mind.
    """

    $ captain_details.threads.unlock('captain_host_suspicion_portrait')

    return
