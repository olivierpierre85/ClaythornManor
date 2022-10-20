label lad_day2_afternoon_bedroom:
    scene bedroom_lad

    call change_time(16,00)

    """
    So we carried Doctor Baldwin to his room and lay him down on his bed.

    Afterwards, I retreated to my room to change my clothes.

    They were stained with blood.

    As I was preparing to go downstairs again, someone knock on my door
    """

    play sound door_knock

    psychic """
    Mister Harring, can I come in ?
    """

    """
    Amalia Baxter... What does she want ?
    """

    # TODO CHoice of letting her in or not ?
    lad """
    Come on in Mrs Baxter. The door is open.
    """

    play sound door_open

    psychic """
    I am sorry to intrude, but I think it's important that we talked.
    """



    

    return