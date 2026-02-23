# --------------------------------------------
#   Nurse
#           
#   Friday - Afternoon
#   
#   14:00 -> 16:30
#
#   Music: Chill, upbeat
#
#   Alive: Everyone
#
# --------------------------------------------
label nurse_introduction:

    call change_time(14, 0, 'Arrival', 'Friday', hide_minutes=True, chapter='friday_afternoon')

    call black_screen_transition("", "Rosalind Marsh")

    $ change_room("train_inside", irisout)

    play sound train_moving loop

    $ play_music('chill')

    """
    The letter is on my lap, and I have read it enough times to know it by heart.

    On the surface, it is perfectly composed. Generous, even.

    A weekend at a Scottish manor, an award for distinguished service, a cheque for one thousand pounds.

    On the surface.

    But I know a con when I see one.

    The vague wording. The pressure to attend in person. The promise of money that exists only so long as you show up.

    Someone is gathering people. The question is why.

    The sensible thing would have been to stay home.

    And yet here I am, somewhere in the north of Scotland, watching the countryside blur past the window.

    I fold the letter and slip it back into my bag.

    If there is no prize at the end of this, there will at least be a house full of wealthy guests.

    A weekend is quite enough time to make a trip worth one's while.
    """

    play sound train_stopping

    $ change_room("train_station")

    pause 2.0

    """
    I am one of the first off the train.

    Old habit. It pays to get a good look at things before other people do.

    A young man in livery is waiting near the exit, scanning the passengers as they file past.

    I approach him before he has the chance to approach anyone else.
    """

    nurse """
    Good afternoon. I'm Rosalind Marsh. Are you going to Claythorn Manor?
    """

    footman """
    Yes, ma'am. Lady Claythorn sent me to collect her guests.
    """

    """
    He seems relieved to have found someone.

    A moment later, a middle-aged gentleman steps onto the platform and makes his way towards us with the unhurried confidence of a man who expects things to fall into place.
    """

    doctor """
    Hello. Could you help me? I'm supposed to go to Claythorn Manor.
    """

    footman """
    Of course, sir. Lady Claythorn sent me to pick up her guests.
    """

    doctor """
    Good. Do you know how many were on this train?
    """

    footman """
    I can't say for certain. We'll wait a few minutes to see if anyone else shows up.
    """

    doctor """
    Fine.
    """

    doctor """
    Nice to meet you, Miss Marsh. I'm Doctor Daniel Baldwin.
    """

    nurse """
    Nice to meet you, doctor. Was your trip pleasant?
    """

    doctor """
    It was pleasant, thank you.

    How about you?
    """

    nurse """
    It was fine, thank you. And what...
    """

    """
    I stop.

    Something — someone — catches my eye over the doctor's shoulder.

    A man has appeared farther along the platform.

    He is tall and composed, and most of his face is concealed behind a tin mask.

    I have seen worse, working on the wards. Much worse.

    But I was not expecting it, and the surprise must have shown on my face.

    I collect myself quickly and look away.
    """

    broken """
    Hi, I'm Thomas Moody.

    Lady Claythorn invited me. Maybe you can help?
    """

    """
    Nobody speaks for a moment.

    I am not here to make enemies. Or scenes.
    """

    doctor """
    Hello, Mr Moody. You're with the right people.

    This young man was about to drive us to Claythorn Manor.

    I'm Daniel Baldwin, and this is Rosalind Marsh.

    Nice to meet you.
    """

    """
    We exchange a few brief words, then follow the footman to the car.
    """

    $ change_room("inside_car")

    """
    I take a seat behind the footman, leaving the two men to settle in beside me.

    The doctor attempts conversation, and I do my part — a smile here, a short reply there.

    But my attention keeps drifting.

    Seven guests in total, if the letter is to be believed.

    A doctor. A man disfigured in the war. That is two accounted for.

    I wonder what connects us all. The invitation spoke of bravery.

    Bravery. What a word to use.

    By the time we turn onto a wooded track, the men have both fallen quiet.

    The doctor is watching the road. The soldier stares out of the window.

    Neither of them seems especially at ease.

    I find that interesting.

    Whatever Lady Claythorn has planned, I am not the only one who came here against their better judgement.
    """

    $ stop_music()

    $ change_room("manor_exterior")

    """
    The house comes into view just as the first drops of rain begin to fall.

    It is larger than I expected. And older.

    The kind of house that costs more to maintain than most people earn in a lifetime.

    Someone here has money — or the appearance of it.

    Either way, I intend to leave with a little more than I arrived with.

    I straighten my coat and step out of the car.
    """

    pause 2.0

    jump nurse_day1_evening
