# --------------------------------------------
#   Doctor
#           
#   Friday - Afternoon
#   
#   14:00 -> 14:45
#
#   Music: Chill, upbeat
#
#   Alive: Everyone
#
#   Notes : 
#       - 
# --------------------------------------------
label doctor_introduction:

    call change_time(14, 00, 'Arrival', 'Friday', hide_minutes=True)

    call black_screen_transition("Daniel Baldwin", "Friday Afternoon")

    $ change_room("train_inside")

    play sound train_moving loop

    $ play_music('chill')

    """
    Anxiety hits me harder than usual.

    I haven't been away this long in years. It feels off, but there's no turning back.

    Not with so much money at stake.

    I'll manage. I always do.

    My gaze lands on the bag. I pause. The thought crosses my mind—it could help. It always does. 
    
    But it's a mistake, and I know it.

    I don't want to start wrong. Not this time. Something tells me I'll need my wits about me all weekend.

    I think it through, weigh it all, and still reach for the bag.
    """

    play sound train_stopping

    """
    As I head to the bathroom, the train begins to slow.

    Too late now.
    """

    $ change_room("train_station")

    pause 2.0

    """
    I gather my things and leave the train.
    """

    pause 1.0

    """
    Stepping off, I look for my driver.

    The train is empty enough that I quickly spot the only person fitting the bill at the station.
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

    """
    It isn't long before a woman approaches us.
    """

    nurse """
    Hi, I'm Rosalind Marsh. Are you going to Claythorn Manor?
    """

    footman """
    Yes, ma'am. This gentleman will come with us.
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
    She stops suddenly, surprised, a bit scared.

    Her gaze fixes on something behind me.

    I turn quickly.
    """

    broken """
    Hi, I'm Thomas Moody.

    Lady Claythorn invited me. Maybe you can help?
    """

    """
    It takes a moment before anyone can respond.

    We are all shocked by the mask covering most of his face.

    A "broken face" from the war.

    It's not the first one I've seen, but I'm still not used to it.

    Apparently, neither are the people next to me.
    """

    doctor """
    Hello, Mr. Moody. You're with the right people.

    This young man was about to drive us to Claythorn Manor.

    I'm Daniel Baldwin, and this is Rosalind Marsh.

    Nice to meet you.
    """

    """
    We exchange a few pleasantries, then go to the car and begin our journey to Claythorn Manor.
    """

    $ change_room("inside_car")

    """
    I am seated at the front of the car.

    I tried to keep the conversation going for a while, but it fizzled out rather quickly.

    Rosalind Marsh seems to be more of the quiet type, and besides, she still seems uneasy about being seated with the former soldier.

    She keeps looking out of the window, avoiding his gaze as much as possible.

    Thomas Moody doesn't seem to mind. He must be accustomed to this kind of treatment. 

    In any case, he remains silent. I don't know if it's out of compassion for Miss Marsh or if that's just his nature.

    So after a while, we all retreated into a silent contemplation of the landscape.

    I glance behind me every now and then to check on the others, when I notice the driver looking at me.

    When he realises I can see him, he quickly turns back to stare at the road.

    Am I imagining things, or is he blushing? 
    """

    $ stop_music()
    
    $ change_room("manor_exterior")

    """
    It looks like we've reached our destination right on time to avoid a storm.

    The sky is getting dark but it's not raining yet.

    Claythorn Manor is impressive enough.

    I better try to relax now.
    """

    pause 2.0

    jump doctor_day1_evening
