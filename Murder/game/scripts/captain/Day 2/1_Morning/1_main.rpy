# --------------------------------------------
#   Captain
#
#   Saturday - Morning
#
#   08:30 -> 11:00
#
#   Music: chill
#
#   Position
#       - Dining Room : Everyone
#
#   Notes :
#       - Branches on tell_boxer_story:
#           - told   : Thomas Moody is found dead (common death/hunt flow)
#           - refused: Thomas Moody arrives alive after Samuel Manning, normal breakfast
# --------------------------------------------

label captain_day2_morning:

    call change_time(8, 30, 'Morning', 'Saturday', hide_minutes = True, chapter='saturday_morning')

    $ captain_details.add_checkpoint("captain_day2_morning")

    call black_screen_transition("Sushil Sinha", chapters_names[current_chapter])

    $ change_room("bedroom_captain", irisout)

    $ play_music('mysterious', 2)

    """
    I wake before the sun has fully cleared the horizon.

    The room is silent, its heavy curtains muffling the morning bird-song.

    I lie still for a moment, listening to the house.

    Day two.

    The letter still lies on the bedside table where I left it last night.

    Four words, unsigned. 
    
    I turned them over a hundred times before sleep finally found me, and I am no nearer an answer this morning than I was then.

    Someone beneath this roof knows I am not the hero I claim to be.
    """

    if captain_details.threads.is_unlocked('captain_host_suspicion_name') and captain_details.threads.is_unlocked('captain_host_suspicion_portrait'):

        """
        And the letter is not the only matter that weighs upon me.

        Nor is our gracious hostess quite who she pretends to be.

        That adds a layer of risk to everything.
        """

    """
    Whatever is at play here, I must be extremely careful.

    I rise and begin my preparations.

    Washing is a brief, cold affair. Dressing is done with practised efficiency.

    Every button fastened. Every crease straightened.

    The mirror shows a man who belongs here. That is all that matters.

    Now, it is time for breakfast.
    """

    call change_time(8, 45)

    $ change_room('dining_room', dissolve)

    """
    I enter the dining room.

    The table is set, and the smell of coffee and fried bread fills the air.

    I am the first guest to arrive. That suits me.

    I help myself to a modest plate at the buffet and take the same seat I occupied last night.

    A few minutes alone, before the others descend, are always welcome.
    """

    call change_time(9, 00)

    """
    Doctor Baldwin is the first to join me.

    He offers a silent nod from across the room, which I return in kind.

    He helps himself to a plate and eats without a word.

    A sensible man. He has already understood that the morning is not for chatter.

    My mind, however, is not entirely on my breakfast.

    What I uncovered last night still sits uncomfortably at the back of my thoughts.

    I shall have to be extremely careful today, especially around Thomas Moody.
    """

    call change_time(9, 20)

    """
    Miss Baxter is next to appear.

    She drifts in and helps herself to a small serving.

    She takes her seat next to mine and, to my quiet relief, seems in no more hurry to speak than I am.

    Miss Marsh follows a moment later. A nod, a word of greeting, and she settles at the far side of the table with her tea.

    Lastly, Mr Harring slips in with an air of not quite belonging, and seats himself near Miss Baxter.

    I have no interest in following their exchange, so I keep eating in silence.

    While I am eating, Samuel Manning makes his entrance.

    Or rather, he stumbles through it.

    His complexion is ashen, his cravat askew, and his hands shake so badly that he drops a spoon twice before finally securing a cup of black coffee.

    He has clearly not recovered from yesterday.

    He drops into the nearest seat without a word to anyone.

    Miss Baxter's expression hardens at the sight of him, though she says nothing.
    """

    if captain_details.threads.is_unlocked('tell_boxer_story'):

        call captain_day2_morning_breakfast_death

    else:

        call captain_day2_morning_breakfast_alive

    """
    So I readily accept the invitation to join in this afternoon exercise.

    All the other men accept as well, but the ladies will remain behind.
    """

    jump captain_day2_hunt


# --------------------------------------------
#   VERSION A — Moody is found dead
#   (Captain told the Boxer Rebellion story)
# --------------------------------------------
label captain_day2_morning_breakfast_death:

    """
    While I am observing Mr Manning, the butler slips into the room and bends to Lady Claythorn's ear.

    Whatever he tells her, it takes all of her breeding to receive it without crying out.

    She rises at once, crosses the room, and stops beside Doctor Baldwin.
    """

    call common_day2_morning_host_to_doctor

    """
    The three of them leave together.

    To my surprise, Mr Harring also stands and follows them out, with no apparent reason.

    The room settles into silence.

    Nobody speaks, though every face bears the same unspoken question.

    After a moment, Miss Baxter realises she can't ignore me forever.
    """

    call common_day2_morning_captain_psychic_greeting

    """
    She then proceeds to ask me various questions.

    I try to fill the time with the most detailed stories I can. I do not reciprocate her questions.
    """

    call change_time(10, 00)

    call common_day2_morning_host_death

    call common_day2_morning_host_death_doctor

    """
    Mr Moody. Dead in his bed.

    The doctor speaks of old war wounds and natural failure, and it is plausible enough.

    Yet something in me refuses to accept it quite so readily.

    The letter comes back to me at once.

    Someone under this roof sent it. And now, barely twelve hours later, a man is dead.

    That is not a coincidence I am prepared to dismiss.
    """

    if captain_details.threads.is_unlocked('captain_host_suspicion_name') and captain_details.threads.is_unlocked('captain_host_suspicion_portrait'):

        """
        The hostess is not what she presents herself to be, either.

        A letter, a false identity, a dead man. Three things beneath the same roof.

        Doubt creeps into my mind. Maybe I should not have stayed.

        But I feel I am in too deep to turn back now.
        """

    $ stop_music()

    call common_day2_morning_host_hunt

    """
    Our hostess is remarkably composed.

    A death beneath one's roof is no small matter, and yet she carries on as though nothing more serious had occurred than a postponed tea.

    That, in itself, is worth noting.

    For my part, I am in no position to refuse her.

    A man invited for his military record would look strange indeed if he shrank from a morning's shooting.
    """

    return


# --------------------------------------------
#   VERSION B — Moody arrives alive
#   (Captain didn't tell the Boxer story)
# --------------------------------------------
label captain_day2_morning_breakfast_alive:

    """
    Mr Moody appears a moment later.
    """

    pause 1.0

    """
    He pauses at the threshold and surveys the room before heading to the buffet.
    
    There, he helps himself to a light plate.

    He then takes the seat in front of me and starts engaging with our hostess.

    I look at him for a few seconds.

    His presence makes me uneasy.

    Even if I have no proof, I still suspect he is responsible for the letter.

    Before he can notice my staring, I turn my head to the side.

    Miss Baxter is still talking with Ted Harring, which leaves me with no one to talk to.

    That suits me well enough.
    """

    call change_time(10, 00)

    call wait_screen_transition()

    """
    As the plates are gradually cleared, Lady Claythorn rises and addresses the table.
    """

    $ play_music('upbeat', 2)

    host """
    Well, if everyone has finished, I should like to remind you that activities were planned for today.

    This morning, those who wish to are to join a hunt.

    Our staff will lend you everything you need, clothes, guns, and their assistance throughout the event.

    Of course, if you would rather remain indoors by the fire, that is perfectly welcome too.
    """

    """
    A hunt. Yes, I remember it being mentioned.

    I can scarcely refuse without drawing attention to myself.

    And a morning in the open air will do me good.
    """

    return
