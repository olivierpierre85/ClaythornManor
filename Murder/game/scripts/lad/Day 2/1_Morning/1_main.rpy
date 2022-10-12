label lad_day2_morning:

    call black_screen_transition("The Lad - Day 2")

    scene bedroom_lad with irisout

    call change_time(9,00)

    """
    I slept through the night. 
    
    The storm from yesterday has passed and the weather is clearer now.

    """


    if (lad_day1_drinks > 2):
        "Hee, I have a bad hangover this morning. Why did I drink that much ?"
    
    "After getting ready, I leave my room to have breakfast."

    scene dining_hall

    """
    Most of the guests are already in the dining room.

    There is a breakfast buffet. So I fix myself a plate. Eggs, bacon, bread,... with no particular logic.

    I have know idea if it is what I am supposed to do.

    So I take my seat at the same place than yesterday trying not to be noticed.

    Daniel Baldwin and Amalia Baxter are already there.

    """

    psychic """
    Hello Mister Harring. How are you ?
    """

    lad "Very well thank you."

    psychic """
    I was wondering if everyone was gonna join us on time.
    
    There are still a few people missing.

    For instance, I don't know if you noticed the drunk man yesterday. 

    He was so drunk that I wouldn't be surprised if we don't see him before noon.
    """

    "I nod. Not sure what to say."

    if 'broken' in current_character.has_met:

        "I check around the room."

        lad """

        I don\'t see the man with a mask either.

        I talked to him yesterday and he seemed fine to me.
        """
    
    """
    As I begin to eat, the drunk man from yesterday enters the room.

    He stumbled to the buffet table and picks up a plate, visibly shaking.    
    """

    psychic angry """
    Well, I spoke too soon. Here he is. And in such state.

    What a shame.
    """

    """
    At the same moment, the butler rushes inside the room.
    
    He goes to Lady Claythorn and whispers something in her ears.

    I can tell that is not good news.

    She looks shocked and worried. Then stands up and walks in my direction.

    She stops in front a the doctor.
    """

    host """

    Doctor Baldwin, I am sorry to interrupt you breakfast, but would you mind coming with us ?

    We need your assistance.
    """

    """
    Without hesitation, Daniel Baldwin stands up.
    """

    doctor """
    Of course, I'll follow you.
    """

    """
    Everything is happening fast. What should I do ?
    """

    
    $ lad_day1_evening_menu = TimedMenu([
        TimedMenuChoice('Follow them', 'lad_day2_breakfast_follow', 30, early_exit = True ),
        TimedMenuChoice('Stay there and finish breakfast', 'lad_day2_breakfast_eat', early_exit = True)
    ])
    $ time_left = 30
    call run_menu(lad_day1_evening_menu)

    call change_time(9,30)

    if lad_day2_breakfast_follow:

        """
        As we entered the dining room again, the host just finished explaining the situation.

        She has regained her composure when she sees the doctor.
        """

    else:

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

        play music scary_01

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

        I turn over to Amalia Baxter.
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

    Nobody dares to speak much.
    """

    jump lad_day2_morning_breakfast_over



label lad_day2_breakfast_eat:

    psychic -angry "I wonder what this is about."

    lad "Me too, and I have a bad feeling about it."

    call psychic_generic(skip_intro = True)
    
    return

    