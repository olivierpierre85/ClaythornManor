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
    The letter rests upon my lap.

    On the surface, it is perfectly composed. Generous, even.

    A weekend at a Scottish manor, an award for distinguished service, prize money of one thousand pounds.

    But dig a little deeper, and one notices something is not quite right.

    The vague wording. The pressure to attend in person. The promise of money that exists only provided one makes an appearance.

    Everything in this letter seems to be a rather elaborate ploy to gather people in an isolated place. 
    
    The question is why.

    The sensible thing would have been to remain at home.
    
    Yet here I am, travelling somewhere in Scotland, watching the countryside blur past the carriage window.

    I fold the letter and slip it back into my handbag.
    """

    play sound woman_cough

    """
    The cough comes without warning, much as it always does.

    I press my handkerchief to my mouth and wait for the fit to pass.

    There is blood. Not much for now. That at least is mildly reassuring, though I know it shall not last.

    I fold the handkerchief away before anyone can notice.

    The doctor gave me his assessment three months ago, in that careful, measured tone they all adopt when they have nothing comforting to say.

    Consumption. The word sits heavy in my chest, much like the cold does now.

    He prescribed rest. Fresh air. A sanatorium, if at all possible.

    A sanatorium.

    I cannot afford that sort of luxury. 
    
    But I cannot afford to do nothing, either.

    So in the end, I had little choice but to attend this weekend, regardless of the risks.

    If there is no prize at the end of this, I will have to 'find' things of value myself.

    One way or another, I shall make this weekend worthwhile.
    """

    play sound train_stopping

    $ change_room("train_station")

    pause 2.0

    """
    As I step off the train, I scan the platform.

    Near the exit, a young man in livery is already in conversation with a gentleman.

    I make my way towards them.
    """

    call common_day1_afternoon_station_doctor_nurse

    $ change_room("inside_car")

    """
    I take a seat behind the footman, leaving the two men to settle in beside me.

    The doctor attempts conversation, and I do my part — a polite smile here, a short reply there.

    But my attention keeps drifting.

    Seven guests in total, if the letter is to be believed.

    A doctor. A man disfigured in the war. That is two accounted for.

    I wonder what links us all together.

    By the time we turn onto a wooded track, the men have both fallen quiet.

    The doctor is watching the road. The soldier stares blankly out of the window.

    Neither of them seems especially at ease.

    I feel a familiar tightness in my chest and breathe through it slowly.

    A full weekend on my feet. I shall have to be rather careful about it.

    If I exert myself, my health will be at risk.

    But if I stay in my bed most of the time, then why come at all?

    It is a fine line to walk, and I must be cautious about it.
    """

    $ stop_music()

    $ change_room("manor_exterior")

    """
    The house comes into view just as the first drops of rain begin to fall.

    It is larger than I had expected. And older.

    The sort of house that costs more to maintain than most people earn in a lifetime.

    Someone here has money — or at least the appearance of it.

    I should have no trouble leaving with a little more than I arrived with.

    I straighten my coat and step out of the motorcar.
    """

    jump nurse_day1_evening
