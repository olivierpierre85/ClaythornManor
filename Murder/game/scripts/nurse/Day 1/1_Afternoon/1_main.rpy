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
    """

    play sound woman_cough

    """
    The cough comes without warning, as it always does.

    I press my handkerchief to my mouth and wait for it to pass.

    There is blood. Not much for now. That at least is bit reassuring, but I know that won't last.

    I fold the handkerchief away before anyone can notice.

    The doctor gave me his assessment three months ago, in that careful, measured tone they all use when they have nothing reassuring to say.

    Consumption. The word sits in my chest like the cold does now.

    He said rest. Fresh air. A sanatorium, if at all possible.

    A sanatorium.

    Do they imagine money simply appears?

    I cannot afford to rest. Not yet. But I cannot afford to run myself into the ground either.

    A fine line to walk, and I intend to walk it carefully.

    So in the end, I had no choice to come this weekend, no matter the risks.

    If there is no prize at the end of this, I could at least "find" things of value there.

    A weekend is quite enough time to make a trip worth one's while.
    """

    play sound train_stopping

    $ change_room("train_station")

    pause 2.0

    """
    As I step off the train, I scan the platform out of habit.

    Near the exit, a young man in livery is already in conversation with a gentleman who must have been first off.

    I make my way towards them.
    """

    call common_day1_afternoon_station_doctor_nurse

    $ change_room("inside_car")

    """
    I take a seat behind the footman, leaving the two men to settle in beside me.

    The doctor attempts conversation, and I do my part — a smile here, a short reply there.

    But my attention keeps drifting.

    Seven guests in total, if the letter is to be believed.

    A doctor. A man disfigured in the war. That is two accounted for.

    I wonder what connects us all.

    By the time we turn onto a wooded track, the men have both fallen quiet.

    The doctor is watching the road. The soldier stares out of the window.

    Neither of them seems especially at ease.

    I feel a tightness in my chest and breathe through it slowly.

    A full weekend on my feet. I shall have to be disciplined about it.
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

    jump nurse_day1_evening
