label lad_day2_evening_billiard_room:

    $ change_room('billiard_room')

    if not lad_details.saved_variables["day2_evening_billiard_room_visited"]:

        $ lad_details.saved_variables["day2_evening_billiard_room_visited"] = True

        """
        Just as I expected, there aren't many people here.

        I can only spot Captain Sinha sitting on a couch and the butler in the corner.

        At least the bar is still there.
        """

        # TODO add interaction with the butler
        $ lad_day2_evening_billiard_room_menu = TimedMenu("lad_day2_evening_billiard_room_menu", [
            TimedMenuChoice('Talk to Sushil Sinha', 'lad_day2_evening_billiard_room_captain', 20),
            TimedMenuChoice('Talk to Sushil Sinha again', 'lad_day2_evening_billiard_room_captain_2', condition='lad_details.saved_variables["day2_evening_billiard_room_captain_talked"] == True'),
            TimedMenuChoice('Go to the bar for a drink', 'lad_day2_evening_billiard_room_bar', 10),
            TimedMenuChoice('Have another drink to calm the nerves', 'lad_day2_evening_billiard_room_bar_2', 10, condition = 'lad_details.saved_variables["day2_drinks"] == 1'),
            TimedMenuChoice('Maybe a few more drinks would help', 'lad_day2_evening_billiard_room_bar_3', 30, condition = 'lad_details.saved_variables["day2_drinks"] == 2'),
            TimedMenuChoice('Don\'t listen to him, just get plastered', 'lad_day2_evening_billiard_room_bar_4', 120, condition = 'lad_details.saved_variables["day2_drinks"] == 3'),
            TimedMenuChoice('Leave the room', 'generic_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ lad_day2_evening_billiard_room_menu.early_exit = False

        """
        I am back in the Billiard Room.
        """

    call run_menu(lad_day2_evening_billiard_room_menu)

    return

label lad_day2_evening_billiard_room_captain_hypothesis_cancel:
    

    return
    
label lad_day2_evening_billiard_room_captain_hypothesis_doctor:

    lad """
    I believe Daniel Baldwin had an opium addiction.
    """

    captain """
    And what if he was?

    Many people are, especially doctors.

    Regardless, opium addicts often die of an overdose.
    
    Not from a gunshot to the chest.
    """

    """
    Well, I don't have a response to that.
    """

    return

label lad_day2_evening_billiard_room_captain_hypothesis_drunk:

    lad """
    I doubt that Samuel Manning was truly drunk at the time of the accident.
    """

    captain """
    Really? 

    He seemed quite drunk to me.
    """

    lad """
    Yes, early in the morning. And then again before the accident.

    But not right before the hunt began.
    """

    captain """
    If that's true, maybe breakfast sobered him up.

    And I assume he had more drinks during the hunt.
    """

    if lad_details.saved_variables["day2_saw_accident"]:

        captain """
        You were with him, weren't you?

        Did you see him drink?
        """

        lad """
        I believe so.

        He mostly kept to himself, but I did see him sip from his flask.
        """

        captain """
        Well, there you have it, then.
        """
    
    lad """
    I suppose so.
    """

    return

label lad_day2_evening_billiard_room_captain_hypothesis_drunk_letter:

    lad """
    I suspect Samuel Manning had a motive to harm Daniel Baldwin.
    """

    captain """
    Really? What makes you think that?
    """

    lad """
    I found this piece of paper in Samuel Manning's room while you all were hunting.
    """

    captain """
    Why on earth were you in his room?

    You know what, never mind.

    I don't want to know.

    Show me the paper.
    """

    """
    I hand the letter to him.
    """

    captain """
    It's hard to make out the words here. What do you think it means?
    """

    lad """
    I'm not entirely sure, but it might be a threat or blackmail, or...
    """

    captain """
    Or it could mean nothing.

    You can interpret those words in countless ways.

    For instance:
    """

    letter """
    The dogs treated you gently.

    The horse recovered swiftly.

    Do what you love.

    The bird sang.

    Cats don't hesitate.
    """

    lad """
    It's definitely not that!
    """

    captain """
    Probably not, but you can't be certain, can you?

    I'm afraid this doesn't help us much.
    """

    """
    Maybe not.

    But what about this poem though?

    Did he just improvise it on the spot?
    """

    #TODO: Way with words for Sushil sinha?
    return

label lad_day2_evening_billiard_room_captain_hypothesis_broken:

    lad """
    I noticed a weird liquid on Thomas Moody\'s nightstand.
    """

    captain """
    A weird liquid?

    What kind of liquid?
    """

    lad """
    It was greenish and oozing from his flask.
    """

    captain """
    So?
    """

    lad """
    Well, green often indicates poison, right?

    At least, it's not a typical color for alcohol.
    """

    captain """
    Maybe not for any alcohol you're familiar with.

    I know of several liqueurs that have a greenish hue.

    Absinthe, Chartreuse, Creme de menthe,... and there are likely more.

    So I wouldn't shout "poison" the next time you see a green drink.
    """

    if not lad_details.saved_variables["day1_drunk"]:

        captain """
        Of course, if you had tasted the drink, it would be a different story.

        Did you try it?
        """

        lad """
        No, of course not. I wouldn't risk it.
        """

        captain """
        Then we'll need to wait for the experts to analyze it.

        But I bet they won't find anything unusual.
        """

        $ lad_details.saved_variables["day2_evening_taste_from_flask"] = True

    else:
        # TODO ONLY POSSIBLE WAY TO MAKE THE CAPTAIN SUSPICIOUS??WHAT TO MAKE OF IT NOW?
        lad """
        But the flask didn't contain any of those alcohols.

        I tasted it, and it was just whisky.

        I'm certain of that.
        """

    return

label lad_day2_evening_billiard_room_captain_2:

    captain """
    Yes, Mister Harring?

    Do you have anything to add to our last conversation?
    """

    call run_menu(lad_day2_evening_billiard_room_captain_hypothesis_menu)

    return

label lad_day2_evening_billiard_room_captain:

    """
    I take a seat opposite Sushil Sinha.

    If he's disturbed by the events of the day, he doesn't show it.
    """

    captain """
    Good evening, Mister Harring.

    It's nice to see someone else who isn't scared out of their wits tonight.

    The reaction of the others seems quite ridiculous to me.
    """

    lad """
    You don't think we should be at least a bit worried?
    """

    captain """
    Absolutely not. What happened today was obviously accidental.

    There's no reason to think otherwise.

    And now everyone is holed up in their rooms, as if some mysterious murderer is out to get them.
    """

    lad """
    So you don't believe there's a murderer among us?
    """

    captain """
    Of course, there is.
    
    His name is Samuel Manning.

    Once the police arrive, they'll probably charge him with involuntary manslaughter.

    He's likely to be sent to prison for a long time.

    But he won't cause any more harm tonight. Of that, you can be certain.
    """

    lad """
    What makes you so sure?

    You must admit, two deaths in a single day is quite an uncommon occurrence.
    """

    captain """
    Sadly, I'll have to disagree with you.

    It has happened to me more times than I can count.

    And I know what you're going to say. 
    
    We're not at war anymore. It's not the same.

    True. But on the other hand, I don't believe it's that improbable.

    I think everyone is overreacting because they're not accustomed to death like I am.

    Once you remove fear from the equation, you'll realize there's nothing abnormal about today's events.

    Don't you agree?

    Or do you have tangible evidence to believe otherwise?
    """

    $ lad_day2_evening_billiard_room_captain_hypothesis_menu = TimedMenu("lad_day2_evening_billiard_room_captain_hypothesis_menu", [
        TimedMenuChoice('Reveal Daniel Baldwin\'s opium addiction{{observation}}', 'lad_day2_evening_billiard_room_captain_hypothesis_doctor', 10, condition="current_character.saved_variables['knows_doctor_addict']"),
        TimedMenuChoice('Point out the strange liquid on Thomas Moody\'s room{{observation}}', 'lad_day2_evening_billiard_room_captain_hypothesis_broken', 10, condition="lad_details.observations.is_unlocked('green_liquid')"),
        TimedMenuChoice('Accuse Samuel Manning of having a motive to harm Daniel Baldwin', 'lad_day2_evening_billiard_room_captain_hypothesis_drunk_letter', 10, condition="lad_details.objects.is_unlocked('burned_letter')"),
        TimedMenuChoice('Question Samuel Manning\'s state of inebriation at the time of the accident', 'lad_day2_evening_billiard_room_captain_hypothesis_drunk', 10),
        # TODO: If you have ALL the suspicions, you can convince the captain something strange is afoot. Need to decide next steps.
        TimedMenuChoice('Accept you don\'t have any real suspicions', 'lad_day2_evening_billiard_room_captain_hypothesis_cancel', keep_alive=True, early_exit=True),
    ])
    # $ lad_day2_evening_billiard_room_captain_hypothesis_menu = TimedMenu("lad_day2_evening_billiard_room_captain_hypothesis_menu", [
    #     TimedMenuChoice('I believe Daniel Baldwin had an opium addiction {{observation}}', 'lad_day2_evening_billiard_room_captain_hypothesis_doctor', 10, condition="current_character.saved_variables['knows_doctor_addict']" ),
    #     TimedMenuChoice('I noticed a strange liquid on Thomas Moody\'s nightstand {{observation}}', 'lad_day2_evening_billiard_room_captain_hypothesis_broken', 10, condition="lad_details.observations.is_unlocked('green_liquid')" ),
    #     TimedMenuChoice('I suspect Samuel Manning had a motive to harm Daniel Baldwin', 'lad_day2_evening_billiard_room_captain_hypothesis_drunk_letter', 10,  condition="lad_details.objects.is_unlocked('burned_letter')"  ),
    #     TimedMenuChoice('I doubt that Samuel Manning was truly inebriated at the time of the accident', 'lad_day2_evening_billiard_room_captain_hypothesis_drunk', 10 ),
    #     # TODO: If you have ALL the suspicions, you can convince the captain something strange is afoot. Need to decide next steps.
    #     TimedMenuChoice('I don\'t see any reasons to be suspicious.', 'lad_day2_evening_billiard_room_captain_hypothesis_cancel', keep_alive=True, early_exit = True ),
    # ])

    call run_menu(lad_day2_evening_billiard_room_captain_hypothesis_menu)

    lad """
    Okay. Maybe there isn't anything particularly suspicious after all.
    """

    captain """
    Precisely.

    Two unfortunate, unrelated accidents is the simplest and most logical explanation here.

    As the famous saying goes, the simplest explanation is usually the best.

    Now, if you'll excuse me, I'd like to finish my book.
    """

    lad """
    Of course.
    """

    $ lad_details.saved_variables["day2_evening_billiard_room_captain_talked"] = True

    return

label lad_day2_evening_billiard_room_bar:

    """
    There isn't a wide variety of drinks. So, I have a glass of sherry.
    """

    $ lad_details.saved_variables["day2_drinks"] += 1

    return

label lad_day2_evening_billiard_room_bar_2:
    
    """
    Given everything that's happened, one drink probably isn't enough.

    I should have another to help me relax.

    So, I pour myself another glass of sherry.
    """

    $ lad_details.saved_variables["day2_drinks"] += 1

    return

label lad_day2_evening_billiard_room_bar_3:
    
    """
    I can't seem to shake off my anxiety.

    More drinks might be the answer.
    """

    pause 2.0
    # TODO sound of drink pouring

    """
    After a few more drinks, the captain turns his head toward me.
    """

    captain """
    Are you okay over there?

    Are you sure you haven't had enough for tonight?

    We might need to be sharp early tomorrow.
    """

    lad """
    Nahhh, I'm fine...
    """

    """ 
    Damn, am I slurring?

    Maybe he's right.
    """

    $ lad_details.saved_variables["day2_drinks"] += 1

    return

label lad_day2_evening_billiard_room_bar_4:
    
    """
    I ignore the captain's judgmental look and head back to the bar.

    Cut me some slack.

    These are extraordinary circumstances.

    Besides, one more can't hurt.
    """

    $ lad_details.saved_variables["day2_drunk"] = True
    $ lad_details.saved_variables["day2_poisoned"] = False

    return
