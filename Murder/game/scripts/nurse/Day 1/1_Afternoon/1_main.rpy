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
#   Notes: 
#       - Nurse arrives on same train as Doctor and Broken
#       - We see her perspective: casing the manor, hiding illness
#       - Establishes her as thief with terminal disease
#
# --------------------------------------------
label nurse_introduction:

    call change_time(14, 0, 'Arrival', 'Friday', hide_minutes=True, chapter='friday_afternoon')

    call black_screen_transition("", "Rosalind Marsh")

    $ change_room("train_inside", irisout)

    play sound train_moving loop

    $ play_music('chill')

    """
    The invitation promised a thousand pounds in bearer bonds.

    That's more than I'd make in years of honest work.

    Honest. What a funny word.

    I've been taking things that don't belong to me since before the Great War. 
    
    The army taught me discipline, timing, patience. 
    
    It also taught me that no one suspects the nurse.
    """

    pause 1.0

    """
    I cough into my handkerchief. Just a small one this time.

    I check the cloth. No blood. Not yet.

    The doctors say I have months. Maybe a year if I'm lucky.

    Lucky. Another funny word.

    Claythorn Manor is my retirement plan. One last score before this body gives out.

    A grand estate full of wealthy fools and valuable antiques.

    It's perfect.
    """

    play sound train_stopping

    $ change_room("train_station")

    pause 2.0

    """
    The train slows. I gather my modest luggage and step onto the platform.

    A young man in livery stands waiting. The footman, presumably.

    Good. The staff structure tells me a lot about a household.

    Footman means money. Money means opportunity.

    But I'm not alone.
    """

    pause 1.0

    """
    A man with spectacles approaches the footman first.

    He has the bearing of someone educated, but his suit is slightly worn at the elbows.

    Professional class. Doctor, perhaps. Or a solicitor.

    Either way, not my target. They never have the good pieces.
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

    """
    Doctor. I was right. 

    I know that look in his eyes. The slight tremor in his hands as he adjusts his bag.

    Withdrawal. Opioids, if I had to guess. I've seen it before.

    We share some things in common, then. We both have secrets we'd rather keep hidden.
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
    Movement behind the doctor catches my eye.

    I stop mid-sentence.

    A figure approaches. A man. But his face...

    My stomach turns. Not from disgust—from recognition.
    """

    broken """
    Hi, I'm Thomas Moody.

    Lady Claythorn invited me. Maybe you can help?
    """

    """
    A tin mask covers most of his face. What's visible beneath is scarred tissue.

    I've seen a hundred faces like his in the field hospitals. 
    
    The shrapnel wounds, the burns, the reconstructions that never quite worked.

    This war never stops taking.
    """

    nurse """
    Of course. We're all going to the same place.

    Nice to meet you, Mr Moody.
    """

    """
    I try to sound casual, warm even.

    But something about him unsettles me beyond his appearance.

    The eyes behind that mask are watchful. Calculating.

    I should know. Mine are the same.
    """

    $ change_room("inside_car")

    """
    We settle into the car for the journey.

    I choose a seat in the back, near the window.

    The best position to observe without being observed.

    The doctor attempts polite conversation, but it dies quickly.
    """

    pause 1.0

    """
    The masked man—Moody—sits quietly across from me.

    He hasn't said a word since his introduction.

    I find myself glancing at him, trying to read what little I can see of his expression.

    Each time, those eyes are already watching me.
    """

    """
    I turn to the window instead.

    The countryside rolls past. Fields give way to forest.

    Dense, isolated. No nearby villages.

    Perfect for privacy.

    Or for making sure no one hears you scream.

    A morbid thought. But then, I am dying. I'm allowed a few.
    """

    pause 1.0

    """
    A coughing fit seizes me without warning.

    I press my handkerchief to my mouth, trying to muffle it.

    The doctor glances back with professional interest.
    """

    doctor """
    Are you alright, Miss Marsh?
    """

    nurse """
    Fine, thank you. Just the dust from the journey.
    """

    """
    He nods, but I catch him watching me a moment longer than necessary.

    Doctors. Always looking for symptoms.

    I fold my handkerchief quickly, hiding the red spots from view.

    Not yet. Not where anyone can see.
    """

    $ stop_music()
    
    play sound thunder loop

    $ change_room("manor_exterior")

    """
    The manor emerges from the tree line like a beast waking from slumber.

    Georgian architecture. Four stories, at least. Dozens of rooms.

    The storm clouds gathering overhead only add to its imposing figure.

    My heart beats faster, but not from fear.

    Anticipation.
    """

    pause 1.0

    """
    I study the exterior as we approach.

    The main entrance, yes, but also the service door on the east side.

    The windows on the ground floor—older locks, easier to force if needed.

    The ivy climbing the walls—potential access to the upper floors.

    Force of habit.
    """

    pause 1.0

    """
    The footman helps us out of the car as the first drops of rain begin to fall.

    I take a deep breath.

    This is it.

    Three days. One manor. One last chance.

    Let's see what Lady Claythorn is really made of.
    """

    stop sound fadeout 2.0

    pause 2.0

    jump nurse_day1_evening
