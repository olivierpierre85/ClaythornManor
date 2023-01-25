label day2_breakfast_lad_psychic:

    psychic """
    Hello Mister Harring. How are you ?
    """

    lad """
    Very well thank you.
    """

    psychic """
    I was wondering if everyone was gonna join us on time.
    
    There are still a few people missing.

    For instance, I don't think we will see Mister Manning anytime soon. 

    He was so drunk yesterday that I wouldn't be surprised if he doesn't show up before noon.
    """

    """
    Suddenly, Samuel Manning enters the room.

    He stumbled to the buffet table and picks up a plate, visibly shaking.    
    """

    psychic angry """
    Well, I spoke too soon. Here he is. And in such a state.

    How dreadful.
    """

    # TODO Same for psychic and lad? Change based on current char?
    """
    At the same moment, the butler rushes inside the room.
    
    He goes to Lady Claythorn and whispers something in her ears.

    I can tell that is not good news.

    She looks shocked and worried. 
    
    She stands up and walks in my direction, then stops in front of the doctor.
    """

    host """
    Doctor Baldwin, I am sorry to interrupt your breakfast, but would you mind coming with us?

    We need your assistance.
    """

    """
    Without hesitation, Daniel Baldwin stands up.
    """

    doctor """
    Of course, I'll follow you.
    """

label day2_breakfast_host_death:
    
    """
    Suddenly, Lady Claythorn and the butler are back in the room.
    """

    captain "Lady Claythorn, what is happening ? "

    """
    The lady is visibly distressed.
    """

    host """
    I am sorry to announce such horrible news everyone.

    But it appears Mister Moody passed away in his sleep tonight.
    """

    $ play_music('scary')

    """
    The room became instantly silent.
    """

    captain """
    Do we know what has happened ?
    """

    host """
    Doctor baldwin is examining him right now.

    He will probably tell us more later.
    """

    """
    She then sat down to her chair.

    Everybody looks distressed.
    """

    lad """
    How terrible.
    """

    psychic """
    Yes, such sad news.
    """

    """
    We keep eating slowing in silent for a moment when the doctor enters the room.
    """

    return 

label day2_breakfast_host_death_doctor:

    host -surprised """
    Doctor Baldwin. Can you tell us more about what happened ?
    """

    doctor """
    I can't say anything definitive for now. We need to call the town to ask for an ambulance.
    """

    # TODO quid lines ? broken ? or the host pretends everything is fine so everyone stays here ?
    host """
    Yes of course.

    My butler will do what's necessary.
    """

    doctor """
    Very well.
    """

    """
    We then keep on eating in a sad silence.

    Nobody talks much.
    """

    return