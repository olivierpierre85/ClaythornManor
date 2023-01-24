label lad_day2_evening_billiard_room:

    $ change_room('billiard_room')

    if not lad_details.saved_variables["day2_evening_billiard_room_visited"]:

        $ lad_details.saved_variables["day2_evening_billiard_room_visited"] = True

        """
        As I expected, not a lot of people are there.

        I can only see Captain Sinha sitting on a couch and the butler in the corner.

        Well at least, the bar is still there.
        """

        $ lad_day2_evening_billiard_room_menu = TimedMenu([
            TimedMenuChoice('Talk to Sushil Sinha', 'lad_day2_evening_billiard_room_captain', 20),
            TimedMenuChoice('Talk again to Sushil Sinha', 'lad_day2_evening_billiard_room_captain_2', condition='lad_details.saved_variables["day2_evening_billiard_room_captain_talked"] == True'),
            TimedMenuChoice('Go to the bar to have a drink', 'lad_day2_evening_billiard_room_bar', 10),
            TimedMenuChoice('Have another drink, for the nerves', 'lad_day2_evening_billiard_room_bar_2', 10, condition = 'lad_details.saved_variables["day2_drinks"] == 1'),
            TimedMenuChoice('I think I still need of few more drinks', 'lad_day2_evening_billiard_room_bar_3', 30, condition = 'lad_details.saved_variables["day2_drinks"] == 2'),
            TimedMenuChoice('Oh what the hell, maybe I should just get plastered', 'lad_day2_evening_billiard_room_bar_4', 120, condition = 'lad_details.saved_variables["day2_drinks"] == 3'),
            TimedMenuChoice('Leave the room', 'lad_day2_evening_billiard_room_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ lad_day2_evening_billiard_room_menu.early_exit = False

        """
        You are back in the Billiard Room.
        """

    call run_menu(lad_day2_evening_billiard_room_menu)

    return

label lad_day2_evening_billiard_room_captain_hypothesis_cancel:

    return
    
label lad_day2_evening_billiard_room_captain_hypothesis_doctor:

    captain """
    And what if he was?

    A lot of people are, especially doctors.

    In any case, opium addicts often die of overdose.
    
    Not shot in the chest.
    """

    """
    Okay, I have no answer to that.
    """

    return

label lad_day2_evening_billiard_room_captain_hypothesis_drunk:

    captain """
    Really? 

    He seemed pretty drunk to me.
    """

    lad """
    Yes, in the early morning. And then again before the accident happened.

    But not right before the hunt started.
    """

    captain """
    Well if that is true, breakfast might have sobered him up.

    And then I suppose he drank more during the hunt.
    """

    if lad_details.saved_variables["day2_saw_accident"]:

        captain """
        You were there with him right?

        Did you see him drink?
        """

        lad """
        Well, I think so.

        He was keeping mostly to himself but I did see him drink from his flask.
        """


    return

label lad_day2_evening_billiard_room_captain_hypothesis_broken:

    captain """
    A weird liquid?

    What type of liquid?
    """

    lad """
    A greenish liquid.

    It was coming from his flask.
    """

    captain """
    So?
    """

    lad """
    Well, green is the color of poison. No?

    In any case, it's not the normal colour of alcohol.
    """

    captain """
    Not of any alcohol you know perhaps.

    But I do know multiple liqueurs that have a greenish colour.

    Absinthe, Chartreuse, Creme de menthe,...  and there are probably even more.

    So I wouldn't scream poison next time you see a green drink.
    """

    if not lad_details.saved_variables["day1_drunk"]:

        captain """
        Of course, if you had tasted the drink it would another matter.

        Have you?
        """

        lad """
        No, of course not. I wouldn't risk it.
        """

        captain """
        Then we will have to wait for the experts to analyze it.

        But I bet they won't find anything out the ordinary.
        """

        $ lad_details.saved_variables["day2_evening_taste_from_flask"] = True

    else:
        # TODO ONLY POSSIBLE WAY TO MAKE THE CAPTAIN SUSPICIOUS ??WHAT TO MALE of it now?
        lad """
        But the flask didn't have any of those alcohols.

        I tasted it and it was just whisky.

        I am sure of that.
        """

    return

label lad_day2_evening_billiard_room_captain_2:

    captain """
    Yes mister Harring?

    Do you have anything to add to our last conversation?
    """

    call run_menu(lad_day2_evening_billiard_room_captain_hypothesis_menu)

    return


label lad_day2_evening_billiard_room_captain:

    """
    I take a seat in front of Sushil Sinha.

    If he is disturbed by the events of the day, he doesn't show it.
    """

    captain """
    Good evening Mister Harring.

    It's nice to see someone else not scared out of their wit tonight.

    The reaction of the others is pretty ridiculous to me.
    """

    lad """
    You don't think we should be at least a little worried?
    """

    captain """
    Absolutely not. What happened today were obviously accidents.

    There is no reason to think otherwise.

    And now everyone is placating themselves in their rooms, like some mysterious murderer is going to take them.
    """

    lad """
    You don't think there is a murderer among us then?
    """

    captain """
    Of course there is.
    
    His name is Samuel Manning.

    Once the police come, they will probably charge him with involuntary manslaughter.

    It's most likely he'll be sent to prison for a long time.

    But he won't cause anymore harm tonight. You can be sure of that.
    """

    lad """
    What makes you so sure?

    You must admit that two deaths happening in the same day is quite rare occurrence.
    """

    captain """
    Sadly I'll have to disagree with you.

    It happened to me more times that I could count.

    And I know what you are gonna say. 
    
    We are not at war anymore. It's not the same.

    True. But on the other hand, I don't think it is so improbable.

    I think everyone is overreacting because they are not used to death like I am.

    Once you remove fear from the equation, you'll realize there is nothing abnormal about the events of today.

    Don't you think?

    Or you have tangible evidences to believe otherwise ?
    """

    $ lad_day2_evening_billiard_room_captain_hypothesis_menu = TimedMenu([
        TimedMenuChoice('I have a intuition {{intuition}}', 'TODO', 10, condition="lad_details.is_intuition_unlocked('psychic_poisons')" ),
        TimedMenuChoice('I have a gun, I do what I want {{object}}', 'TODO', 10, condition="lad_details.is_object_unlocked('gun')" ),
        TimedMenuChoice('I believe Daniel Baldwin was an opium addict {{observation}}', 'lad_day2_evening_billiard_room_captain_hypothesis_doctor', 10, condition="current_character.saved_variables['knows_doctor_addict']" ),
        TimedMenuChoice('I saw a strange liquid on the night stand of Thomas Moody {{observation}}', 'lad_day2_evening_billiard_room_captain_hypothesis_broken', 10, condition="lad_details.is_observation_unlocked('green_liquid')" ),
        TimedMenuChoice('I am not sure Samuel Manning was really drunk when the accident occurred', 'lad_day2_evening_billiard_room_captain_hypothesis_drunk', 10 ),
        TimedMenuChoice('I don\'t see any reasons to be suspicious.', 'lad_day2_evening_billiard_room_captain_hypothesis_cancel', keep_alive=True, early_exit = True ),
    ])

    call run_menu(lad_day2_evening_billiard_room_captain_hypothesis_menu)

    lad """
    Ok. I guess there is nothing really suspicious in the end.
    """

    captain """
    Exactly.

    Two sad unrelated accidents is the most simple and logical explanation here.

    And like the famous saying goes, the most simple explanation is usually the best.

    Now if you'll excuse me, I would like to finish my book.
    """

    lad """
    Of course.
    """

    $ lad_details.saved_variables["day2_evening_billiard_room_captain_talked"] = True

    return


label lad_day2_evening_billiard_room_bar:

    """
    There is not much of choice of drinks. So I drink a glass of sherry.
    """

    $ lad_details.saved_variables["day2_drinks"] = lad_details.saved_variables["day2_drinks"] + 1

    return

label lad_day2_evening_billiard_room_bar_2:
    
    """
    With everything that has happened, one drink is probably not enough.

    I should have another one to help me relax.

    So I pour myself another sherry.
    """

    $ lad_details.saved_variables["day2_drinks"] = lad_details.saved_variables["day2_drinks"] + 1

    return

label lad_day2_evening_billiard_room_bar_3:
    
    """
    I can't seem to be able to get rid of my anxiety.

    More drinks is probably the answer.
    """

    pause 2.0
    # TODO sound of drink pouring

    """
    After a few more drinks, the captain turns his head towards me.
    """

    captain """
    Are you ok there?

    You sure you haven't had enough for tonight?

    We may have to be sharp early tomorrow.
    """

    lad """
    Naahhh, I am fine....
    """

    """ 
    Shit, am I slurring?

    Maybe he is right.
    """

    $ lad_details.saved_variables["day2_drinks"] = lad_details.saved_variables["day2_drinks"] + 1

    return

label lad_day2_evening_billiard_room_bar_4:
    
    """
    I ignore the captain judgemental look and head again to the bar.

    Cut me some slack.
    
    These are extraordinary circumstances.

    Beside, one more can't hurt.
    """

    $ lad_details.saved_variables["day2_drunk"] = True
    $ lad_details.saved_variables["day2_poisoned"] = False

    return

label lad_day2_evening_billiard_room_cancel:
    return