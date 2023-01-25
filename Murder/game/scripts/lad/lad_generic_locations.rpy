label lad_library:

    $ change_room('library') 
    
    """
    It's a very nice library. But what am I doing here? I can barely read.
    """

    $ lad_details.unlock_knowledge('education')

    """
    There is an open book on a small table.

    \"A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.\"

    Yeah, I am not reading that.

    I probably better go look elsewhere.
    """
    # TODO add info on BOOK???

    $ lad_details.saved_variables["library_visited"] = True

    return

label lad_library_visited:

    $ change_room('library')

    """
    There is nothing different from last time I was in there.
    """

    return
