label doctor_day2_evening_males_room_default:

    call doctor_attic_default
    
    play sound door_knock

    """
    I could just barge in, but I prefer to knock just in case.
    """

    footman """
    Who is it?
    """

    return


label doctor_day2_evening_males_room_do_no_enter:

    call doctor_day2_evening_males_room_default

    doctor """
    It is Doctor Baldwin.
    """

    footman """
    Oh.

    What can I do for you, doctor?
    """

    doctor """
    Well... I am not entirely sure.

    I was merely exploring, and wondered what was in the attic.
    """

    footman """
    I do not think you are supposed to be here, doctor.

    This is the servants quarters.

    I was about to go to bed myself, as I have to be up early tomorrow.
    """

    doctor """
    Of course, my apologies for disturbing you.

    Good night.
    """

    footman """
    Goodnight, sir.
    """

    """
    Well, that was rather embarrassing.

    That is what happens when one wanders about a house without a clear purpose, I suppose.
    """

    return


label doctor_day2_evening_males_room_enter:

    call doctor_day2_evening_males_room_default
        
    """
    I answer in a whisper.
    """

    doctor """
    Andrew, it is me, Daniel.
    """

    footman """
    Doctor?

    You should not be here.

    Tonight is not the best time, with... everything that has happened.
    """

    doctor """
    I am well aware.

    But I sincerely hope you do not hold me responsible for today's accident.
    """

    """
    He pauses for a second before answering.
    """
    
    footman """
    No, of course not.

    I am sure it was only a terrible mistake.
    """

    """
    There is a pause, then the soft sound of the bolt sliding back.

    The door opens just enough for me to slip inside.

    He closes it carefully behind me.

    Words quickly become unnecessary.

    In a moment we are both on his bed, our clothes discarded on the floor.
    """

    call wait_screen_transition()

    """
    When it is over, reality returns far too quickly.
    """

    footman """
    I think you should go back to your room now.
    """

    doctor """
    Already?

    I was hoping to stay here for the night.
    """

    footman """
    I do not think that would be prudent.

    People might see you in the morning.
    """

    doctor """
    I could rise early and leave before anyone is awake.
    """

    footman """
    I am not certain you could.

    Servants are usually up when you would still think it the middle of the night.

    I would rather not take that risk.

    Besides, in only a few hours I have an errand to run.
    """

    doctor """
    So early?

    Why on earth do you have to do that?
    """

    footman """
    I am sorry, I cannot say.

    It is an order from Lady Claythorn.
    """

    """
    I glance towards the small window.

    The wind has picked up, and distant thunder rolls across the moor.
    """

    doctor """
    It does look as though it may rain again.

    You will catch your death if you stay outside too long.
    """

    footman """
    Do not worry, I shall be taking the car.

    And besides, I am not made out of sugar.
    """

    """
    The expression strikes me as oddly familiar, and somewhat out of place.
    """

    doctor """
    That is a curious turn of phrase.

    And yesterday, I recall you mentioning something about whipping cats.

    That was even more peculiar.

    Where did you learn such expressions?
    """

    footman """
    Hm.

    You have truly never heard them before?

    I suppose I got them from my grandmother.

    We are from the North, near Sunderland.

    People there have rather strange sayings, you know.
    """

    doctor """
    I am aware of that.

    I have family from that region myself.

    Yet I have never heard those expressions.
    """

    """
    He looks embarrassed.
    """

    footman """
    Well.

    I might as well tell you.

    There is no point in keeping this for myself.

    I am not British.

    I was brought here as a young teen, so you would not hear it in my accent.

    But those are French expressions my parents used often.

    I suppose I translated them without realising they might not exist in the King's English.
    """

    doctor """
    You are French?

    How interesting.

    But why keep it a secret?
    """

    footman """
    I am not bloody French.

    People always assume that.

    I am Belgian, from a French speaking family.
    """

    doctor """
    I see.

    My apologies.

    Still, why hide it?
    """

    footman """
    Because I am not meant to be here.

    My parents were war refugees.

    They worked in a weapons factory during the war, in a small northern village called Birtley.

    When the war ended, we were supposed to return to Belgium.
    """

    footman """
    But I had spent my teenage years here.

    I did not want to go back.

    I was seventeen, and I was in love.

    I could not bear to leave him behind.

    So I pretended to be British.

    My English was good enough not to raise suspicion.

    Ever since, I have hidden my true identity.

    That is why I became an actor.

    And...
    """

    """
    He stops short.

    That is information I was not meant to hear.
    """

    doctor """
    You are an actor?

    Then what are you doing here, in the middle of the woods?

    There cannot be many roles for you in a place like this.
    """

    footman """
    No, of course not.

    But one must earn a living.

    Acting is not a secure profession.

    I take odd jobs when I must.

    I was never meant to stay in this manor for long.

    Just long enough to get back on my feet.

    But it is late now.

    I have spoken far too much about myself.

    I need my rest for tomorrow.

    You should go now, Doctor.

    Before we are both discovered.
    """

    """
    The dismissal is abrupt.

    Nevertheless, I nod reluctantly.
    """

    doctor """
    If you insist, I shall be on my way.
    """

    """
    I dress in silence.

    Then he opens the door just enough for me to slip back into the corridor.

    The bolt slides shut behind me.
    """

    $ doctor_details.threads.unlock('footman_actor')

    return

