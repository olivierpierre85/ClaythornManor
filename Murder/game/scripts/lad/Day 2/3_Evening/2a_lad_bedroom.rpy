label lad_day2_evening_bedroom:
    
    $ change_room('bedroom_lad')

    call change_time(18,00)

    """
    So I retreat to my room to fetch clean clothes.

    I also take the opportunity to have a bath.

    As I am preparing to go downstairs again, someone knocks on my door.
    """

    call common_day2_evening_lad_psychic_discussion_0

    if not lad_details.saved_variables['knows_bedroom_psychic']:

        psychic """
        I'm in the "Elizabeth I" room.
        """

        $ unlock_map('bedroom_psychic')

        $ lad_details.saved_variables['knows_bedroom_psychic'] = True # TODO add automatic function in unlock map

    return
