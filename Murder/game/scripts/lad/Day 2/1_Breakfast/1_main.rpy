label lad_day2_breakfast:

    call black_screen_transition("The Lad - Day 2")

    scene bedroom_lad with irisout

    call change_time(9,00)

    "You slept through the night."

    if (lad_day1_drinks > 2):
        "You have a bad hangover. But you'll power through."
    
    "After getting ready, you leave your room to have breakfast."

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

    $ time_left = 30

    $ lad_day1_evening_menu = TimedMenu([
        TimedMenuChoice('Follow them', 'lad_day2_breakfast_follow', 30, condition = 'lad_day2_breakfast_eat == False'),
        TimedMenuChoice('Stay there and finish breakfast', 'lad_day2_breakfast_eat', condition = 'lad_day2_breakfast_follow == False')
    ])

    call run_menu(lad_day1_evening_menu)

    if lad_day2_breakfast_follow:

        "As we entered the dining room again. The host explains briefly what has happened"

    else:

        "TODO Full sumary of what Happened in FOLLOW O"

    jump lad_day2_luncheon



label lad_day2_breakfast_eat:

    $ lad_day2_breakfast_eat = True

    psychic -angry "I wonder what this is about."

    lad "Me too, and I have a bad feeling about it."

    call psychic_generic
    
    return

    