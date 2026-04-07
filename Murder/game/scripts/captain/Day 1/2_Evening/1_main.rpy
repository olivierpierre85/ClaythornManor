# --------------------------------------------
#   Captain
#
#   Friday - Evening
#
#   16:30 -> 23:00
#
#   Music: chill
#
#   Position
#       - Tea Room : Doctor, Broken, Nurse, Drunk
#       - Dinner Room : Everyone
#
#   Notes :
#       - Tea room: meet Doctor, Broken, Nurse
#       - Dinner: Psychic, Broken
#       - Map visit, 90 minutes
#       - Billiard room: tell Boxer story
# --------------------------------------------
label captain_day1_evening:

    call change_time(16, 30, "Evening", "Friday", hide_minutes = True, chapter='friday_evening')

    $ current_character.add_checkpoint("captain_day1_evening")

    call black_screen_transition("Sushil Sinha", chapters_names[current_chapter])

    $ change_room('entrance_hall', dissolve)

    $ play_music('upbeat')

    """
    We arrive at the manor.

    It is an imposing house. Not the grandest I have seen, but respectable.

    The kind of place I should have been invited to years ago.

    I straighten my jacket and step inside.
    """

    call common_day1_evening_second_arrival_part_1

    """
    Manning is already demanding a drink. The man has no shame.

    But at least he draws attention away from me.
    """

    call common_day1_evening_second_arrival_part_2

    """
    Miss Baxter excuses herself to freshen up in her room.

    Good. I have had quite enough of her questions for now.

    The tea room it is.
    """

    $ change_room('tea_room', dissolve)

    call change_time(16, 45)

    """
    Three people are already here.

    Two men in quiet conversation and a woman standing a little apart, sipping tea.

    Time to introduce myself.
    """

    captain """
    Hello there, I am Captain Sushil Sinha.
    """

    broken """
    Nice to meet you, Captain. I am Thomas Moody.
    """

    doctor """
    Doctor Daniel Baldwin.

    How do you do.
    """

    captain """
    Nice to meet you both.
    """

    """
    I notice at once that Mr Moody is wearing a tin mask.

    I have seen many of those. The poor man must have suffered terribly during the war.

    I must be careful not to stare.
    """

    $ broken_details.description_hidden.unlock('mask')

    broken """
    And who is the gentleman over there?
    """

    """
    He is referring to Manning, who has found the drinks tray with remarkable speed.
    """

    captain """
    That would be Samuel Manning.

    I am afraid he had a bit too much to drink.

    But don't worry about him.
    """

    """
    We watch as Manning fills a water glass to the brim with sherry.

    He drinks it in one go, then sits down on the sofa and falls asleep almost immediately.
    """

    captain """
    Well, that should keep him still for a while.
    """

    $ drunk_details.description_hidden.unlock('addict')

    doctor """
    Indeed, it's impressive that...
    """

    """
    The doctor starts to say something, but I cannot afford silences.

    Silences invite questions. Questions lead to lies. And lies must be kept to a minimum.

    Better to fill the air myself.
    """

    captain """
    It reminds me of a fellow I knew back in the Army.

    He was my superior, but I swear I never saw him sober.

    Even in the mornings, he was always still drunk from the day before.
    """

    """
    That part, at least, is true.

    I carry on from there. A story about a drunkard officer in Calcutta.

    Then another about the supply lines in Burma.

    I can tell the doctor has stopped listening after a while, but Mr Moody seems genuinely interested.

    Good. As long as I am the one talking, nobody can ask me anything awkward.
    """

    """
    The woman approaches our group.
    """

    captain """
    Oh, hello Miss ... ?
    """

    nurse """
    Miss Marsh.
    """

    captain """
    How do you do, Miss Marsh. Captain Sushil Sinha.

    I was telling those gentlemen a story about a certain conflict I was involved in.

    But I can change the subject if you prefer.
    """

    nurse """
    No, please, go on. I am quite familiar with wartime stories, having served as a nurse through more than one.
    """

    captain """
    Really? You were a wartime nurse. How interesting.

    Well, where was I?
    """

    broken """
    I believe you were talking about the Anglo-Zanzibar War.
    """

    captain """
    Right.

    That's where I got my first battle scar.

    It's on my back so I won't show it to you, but it was rather dangerous fighting.

    Not like the Great War of course, and not that I can understand your pain.

    But still, a battle wound is a battle wound.
    """

    """
    That particular scar is from falling off a chair in my office in Calcutta.

    But they do not need to know that.

    The Anglo-Zanzibar War. A conflict that lasted barely an hour.

    Not that anyone here is likely to remember that detail.
    """

    $ captain_details.description_hidden.unlock('embellishment')

    """
    I carry on. Miss Marsh listens attentively, though I notice something sharp behind her eyes.

    The doctor, on the other hand, has drifted off entirely. He nods, but his mind is elsewhere.

    Two more guests slip into the room. The butler announces the young man.
    """

    butler """
    Mr Ted Harring!
    """

    """
    He looks out of place. Young, nervous, dressed in clothes that have seen better days.

    I pay him little mind and continue my story.
    """

    $ lad_details.description_hidden.unlock('poor')

    """
    I am in the middle of a rather good tale when the gong interrupts me.
    """

    play sound dinner_gong

    """
    A pity. I was just getting to the best part.
    """

    $ stop_music()

    call change_time(18, 30, 'Dinner', 'Friday')

    $ change_room('dining_room', irisout)

    $ play_music('chill', 2)

    """
    We file into the dining room. Each place is marked with a name card.

    I find mine near the head of the table. A good position.

    Miss Baxter is on my right. Mr Moody sits across from me.
    """

    """
    Then, our host makes her entrance.

    She is younger than I expected. Elegantly dressed, with the quiet confidence of old money.

    She takes her seat at the head of the table.
    """

    call common_day1_evening_host_welcome_speech

    """
    One thousand pounds, shared among seven guests. Roughly one hundred and forty each.

    Not as much as I had hoped, but still a significant sum.

    If used wisely, it could open the right doors.

    The first course is served shortly after.
    """

    $ captain_details.description_hidden.unlock('heroic_act')

    """
    I glance at the people nearest to me.

    Miss Baxter, whom I already spoke with at length during the car ride.

    And Mr Moody, the war veteran.
    """

    call change_time(19, 30)

    $ time_left = 90
    call run_menu(TimedMenu("captain_day1_evening", [
        TimedMenuChoice("Talk to Amelia Baxter", 'captain_day1_dinner_psychic', early_exit=True),
        TimedMenuChoice("Talk to Thomas Moody", 'captain_day1_dinner_broken', early_exit=True),
        TimedMenuChoice("Eat in dignified silence", 'generic_cancel', early_exit=True),
    ], image_left = "psychic", image_right = "broken"))

    call change_time(21, 00)

    """
    The dinner draws to a close.

    Lady Claythorn mentions that drinks will be available in the billiard room for those who wish to continue the evening.

    First, I should like to see my room. I have not yet had the chance to settle in.

    I ask the footman to show me the way.
    """

    $ change_room('bedrooms_hallway', dissolve)

    footman """
    Here you are, Captain.

    You've been assigned the 'George I' room.
    """

    $ unlock_map('bedroom_captain')

    $ change_room('bedroom_captain', dissolve)

    """
    The room is adequate. Not extravagant, but respectable.

    'George I.' An ordinary room named after an ordinary King.

    Still, it is more comfortable than my lodgings in London.

    I unpack quickly and consider my options.
    """

    $ play_music('upbeat')

    call change_time(21, 30)

    $ time_left = 90

    call run_menu(captain_details.saved_variables["day1_evening_map_menu"])

    call change_time(23, 00)

    $ stop_music()

    """
    The hour is late and the house has grown quiet.

    I return to my room.
    """

    $ change_room('bedroom_captain', dissolve)

    """
    I change and prepare for bed with military efficiency.

    As I lie down, I review the evening.

    I have done well. Nobody suspects a thing.

    My stories held their attention, and I avoided any question that might have caught me out.

    Tomorrow, I shall do the same.

    With that thought, I close my eyes.
    """

    $ stop_music()

    jump work_in_progress


# ------------------------------------
#   DINNER SCENES
# ------------------------------------
label captain_day1_dinner_psychic:

    captain """
    Miss Baxter. We meet again.
    """

    psychic """
    Indeed, Mr Sinha. I trust the tea room was more entertaining than our car ride?
    """

    captain """
    I hope I was not too tedious in the car. I do tend to go on.
    """

    psychic """
    You were thorough, I will say that much.
    """

    """
    I cannot tell whether she is being kind or cutting.

    Either way, I had better be more measured this time.
    """

    psychic """
    Tell me, Captain. What brings a man of your standing to a place like this?
    """

    captain """
    The letter, naturally. Lady Claythorn was generous enough to invite me.

    As recognition of my years of service.
    """

    psychic """
    Your years of service. Yes, you mentioned that. Several times, in fact.
    """

    """
    She is sharper than I gave her credit for.

    I had better not overplay my hand with this one.
    """

    captain """
    And you, Miss Baxter? I confess I did most of the talking earlier.

    I should like to hear about you.
    """

    psychic """
    How very gracious of you. Perhaps another time.

    The food is getting cold.
    """

    """
    She returns to her plate with a polite smile.

    I have not learnt much about her, but she has learnt rather too much about me.

    I must be more careful.
    """

    return


label captain_day1_dinner_broken:

    captain """
    Mr Moody. I hope you are enjoying the dinner.
    """

    broken """
    It is very fine, Captain. I am not used to such extravagance.
    """

    captain """
    Nor I, if I am honest.

    Tell me, were you in the war?
    """

    broken """
    I was. France, mostly.
    """

    """
    He does not elaborate. The mask speaks for itself.

    I know better than to press a man on his wounds.

    But a shared experience, even an exaggerated one, can build trust.
    """

    captain """
    I saw action myself. Nothing compared to what you must have endured, of course.

    But war leaves its mark on all of us.
    """

    broken """
    That it does, Captain.
    """

    """
    He nods slowly and returns to his meal.

    A man of few words. I respect that.

    In truth, I envy it.
    """

    return
