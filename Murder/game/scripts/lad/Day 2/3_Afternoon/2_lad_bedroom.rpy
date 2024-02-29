label lad_day2_afternoon_bedroom:
    
    $ change_room('lad_room')

    call change_time(18,00)

    """
    So, I retreated to my room to fetch clean clothes.

    I also took the opportunity to have a bath.

    As I was preparing to go downstairs again, someone knocked on my door.
    """

    call common_day2_afternoon_lad_psychic_discussion

    if not lad_details.saved_variables['knows_psychic_room']:

        psychic """
        I'm in the "Elizabeth I" room.
        """

        $ unlock_map('psychic_room')

        $ lad_details.saved_variables['knows_psychic_room'] = True # TODO add automatic function in unlock map

    return
