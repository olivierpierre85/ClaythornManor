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

    $ play_music('chill', 3)

    """
    I wake before the sun has fully cleared the horizon.

    The 'George I' room is silent, its heavy curtains muffling the morning bird-song.

    I lie still for a moment, listening to the house.

    Day two.

    My performance yesterday was adequate. I played the part of the retired officer to perfection.

    Yet I must not grow complacent. A single slip, a misplaced word, and this entire charade collapses.

    I have survived thirty years of Imperial politics. I can survive a weekend in the Highlands.

    I rise and begin my preparations.

    Washing is a brief, cold affair. Dressing is done with practised efficiency.

    Every button fastened. Every crease straightened.

    The mirror shows a man who belongs here. That is all that matters.

    I cannot afford to be late for breakfast. Punctuality is the bedrock of authority.
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
    """

    if captain_details.threads.is_unlocked('captain_host_suspicion_name') and captain_details.threads.is_unlocked('captain_host_suspicion_portrait'):

        """
        My mind, however, is not entirely on my breakfast.

        What I uncovered last night still sits uncomfortably at the back of my thoughts.

        Our gracious hostess is not quite the woman she claims to be.

        I shall have to tread very carefully today.
        """

    call change_time(9, 20)

    """
    Miss Baxter is next to appear.

    She drifts in as though arriving at a reading rather than a breakfast, and helps herself to a small serving.

    She takes her seat a short way from mine and, to my quiet relief, seems in no more hurry to speak than I am.

    Miss Marsh follows a moment later. A nod, a word of greeting, and she settles at the far side of the table with her tea.

    Lastly, Mr Harring slips in with that habitual air of not quite belonging, and seats himself near Miss Baxter.

    She greets him warmly and they fall into conversation at once.
    """

    call change_time(9, 30)

    """
    I have no interest in following their exchange.

    The young man's chatter is no concern of mine, and I take the opportunity to study the others in silence.
    """

    if captain_details.threads.is_unlocked('tell_boxer_story'):

        jump captain_day2_morning_breakfast_death

    else:

        jump captain_day2_morning_breakfast_alive


# --------------------------------------------
#   VERSION A — Moody is found dead
#   (Captain told the Boxer Rebellion story)
# --------------------------------------------
label captain_day2_morning_breakfast_death:

    """
    While I am eating, Samuel Manning makes his entrance.

    Or rather, he stumbles through it.

    His complexion is ashen, his cravat askew, and his hands shake so badly that he drops a spoon twice before finally securing a cup of black coffee.

    He has clearly not recovered from yesterday, and seems to have no intention of doing so today either.

    He drops into the nearest seat without a word to anyone.

    Miss Baxter's expression hardens at the sight of him, though she says nothing.

    A reputable man would at least have the decency to remain in his room until he was fit for company.
    """

    """
    While I am observing Mr Manning, the butler slips into the room and bends to Lady Claythorn's ear.

    Whatever he tells her, it takes all of her breeding to receive it without crying out.

    She rises at once, crosses the room, and stops beside Doctor Baldwin.
    """

    call common_day2_morning_host_to_doctor

    """
    The three of them leave together.

    To my mild surprise, Mr Harring also stands and follows them out, with no apparent invitation and no apparent reason.

    The room settles into an uneasy hush.

    Nobody speaks, though every face bears the same unspoken question.
    """

    psychic -angry """
    Good morning, Mr Sinha.
    """

    captain """
    Miss Baxter.
    """

    psychic """
    An unfortunate way to begin a day.

    What do you suppose has happened?
    """

    captain """
    I could not say, Miss Baxter. The butler was not speaking loudly enough for my benefit.

    Whatever it is, our hostess will no doubt inform us when she feels it appropriate.
    """

    psychic """
    You are very composed, Mr Sinha.
    """

    captain """
    A man who has served in the Empire learns to be composed, Miss Baxter.

    Impatience solves nothing, and makes a poor impression on those around you.
    """

    """
    She inclines her head slightly, and we lapse into silence once more.

    Whatever has passed upstairs, we are not to know for some while yet.
    """

    call change_time(10, 00)

    call common_day2_morning_host_death

    call common_day2_morning_host_death_doctor

    """
    Mr Moody. Dead in his bed.

    Only last night he stood beside me at the fireplace, nodding approvingly at my tale of the Boxer Rebellion.

    A man in reasonable health, so far as I was able to judge.

    The doctor speaks of old war wounds and natural failure, and it is plausible enough.

    Yet something in me refuses to accept it quite so readily.

    I have seen too many men die in ways that were not at all what they first appeared to be.
    """

    $ stop_music()

    call common_day2_morning_host_hunt

    """
    Our hostess is remarkably composed.

    A death beneath one's roof is no small matter, and yet she presses on as though nothing more pressing had occurred than a postponed tea.

    That, in itself, is worth noting.

    For my part, I am in no position to refuse her.

    A man invited for his military record would look strange indeed if he shrank from a morning's shooting.
    """

    call common_day2_morning_hunt_captain_drunk

    """
    A few eyebrows are raised at Mr Manning's answer. He is in no fit state for a country walk, let alone a hunt.

    But nobody says anything aloud, and I see no reason to be the first.
    """

    call common_day2_morning_hunt_psychic

    call common_day2_morning_hunt_nurse

    call common_day2_morning_hunt_lad

    call common_day2_morning_hunt_host_to_doctor

    call doctor_day2_hunt_choice

    call common_day2_morning_hunt_end

    # TODO: continue to captain hunt chapter (not yet written)
    jump work_in_progress


# --------------------------------------------
#   VERSION B — Moody arrives alive
#   (Captain refused to tell the Boxer story)
# --------------------------------------------
label captain_day2_morning_breakfast_alive:

    """
    While I am eating, Samuel Manning makes his entrance.

    Or rather, he stumbles through it.

    His complexion is ashen, his cravat askew, and his hands shake so badly that he drops a spoon twice before finally securing a cup of black coffee.

    He has clearly not recovered from yesterday, and seems to have no intention of doing so today either.

    He drops into the nearest seat without a word to anyone.

    Miss Baxter's expression hardens at the sight of him, though she says nothing.
    """

    """
    Mr Moody appears a moment later, his mask in place and his step as measured as ever.

    He pauses at the threshold, surveys the room with his usual unreadable courtesy, and helps himself to a light plate.

    He then takes a seat near the middle of the table.
    """

    broken """
    Good morning to you all.

    I trust the storm did not trouble anyone too greatly.
    """

    host """
    Good morning, Mr Moody. We were beginning to wonder whether we should see you at all.
    """

    broken """
    A little later than I intended, I am afraid. Old habits from the convalescent home die hard.
    """

    """
    A polite murmur of sympathy runs around the table.

    The breakfast settles into a decorous rhythm at last.

    A remark on the weather here, a brief comment upon last night's dinner there.

    Nothing of any consequence, which is precisely as it should be.
    """

    if captain_details.threads.is_unlocked('captain_garden_shed_locked'):

        """
        I permit myself a moment to consider what I found yesterday.

        The garden shed, its door firmly locked. An odd detail to dwell upon in a house this remote.

        Perhaps it means nothing. Perhaps it means a good deal.
        """

    broken """
    Captain Sinha, if I may say so, I was rather hoping to hear one of your stories last night.

    Miss Marsh spoke so warmly of them. It seemed a pity you were indisposed.
    """

    """
    The table turns, politely, in my direction.

    An awkward moment. I feel Miss Marsh's eyes upon me, and I know perfectly well what she is thinking.

    A man invited for his military record who will not tell a single war story is a man with something to conceal.

    I must answer carefully.
    """

    captain """
    You are very kind, Mr Moody.

    The journey had left me in no humour for performance. I trust I shall make amends in due course.
    """

    broken """
    I shall hold you to it, Captain.
    """

    """
    A faint smile from behind the mask, and he returns to his plate.

    Miss Marsh does not smile. She looks at me a moment longer than is necessary, then at her tea, and says nothing at all.

    I shall have to manage her carefully.
    """

    psychic -angry """
    Mr Sinha, you have been very quiet this morning.
    """

    captain """
    A man is not obliged to speak merely because others expect him to, Miss Baxter.

    I find a little silence does the digestion a world of good.
    """

    psychic """
    How very practical.
    """

    """
    She says it with a thin smile that does not quite reach her eyes.

    She has not forgiven me for last night's dinner, it seems.
    """

    call change_time(10, 00)

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

    And a morning in the open air will do me no harm at all.
    """

    call common_day2_morning_hunt_captain_drunk

    """
    A few eyebrows are raised at Mr Manning's answer. He is in no fit state for a country walk, let alone a hunt.

    But nobody says anything aloud, and I see no reason to be the first.
    """

    call common_day2_morning_hunt_psychic

    call common_day2_morning_hunt_nurse

    call common_day2_morning_hunt_lad

    host """
    Very good. And you, Mr Moody? Are you well enough to join us?
    """

    broken """
    I shall come as well, if I may.

    A little fresh air would be most welcome.
    """

    call common_day2_morning_hunt_host_to_doctor

    call doctor_day2_hunt_choice

    call common_day2_morning_hunt_end

    # TODO: continue to captain hunt chapter (not yet written)
    jump work_in_progress
