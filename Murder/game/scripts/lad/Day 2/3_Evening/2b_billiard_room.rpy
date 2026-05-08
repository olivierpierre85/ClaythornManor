label lad_day2_evening_billiard_room:

    $ change_room('billiard_room')

    if not lad_details.saved_variables["day2_evening_billiard_room_visited"]:

        $ lad_details.saved_variables["day2_evening_billiard_room_visited"] = True

        """
        Just as I expected, there aren't many people here.

        I can only see Captain Sinha sitting on a sofa and the butler in the corner.

        At least the bar is still there.
        """

        # TODO add interaction with the butler
        $ lad_day2_evening_billiard_room_menu = TimedMenu("lad_day2_evening_billiard_room_menu", [
            TimedMenuChoice('Talk to Sushil Sinha', 'lad_day2_evening_billiard_room_captain', next_menu="lad_day2_evening_billiard_room_captain_hypothesis_menu"),
            TimedMenuChoice('Talk to Sushil Sinha again', 'lad_day2_evening_billiard_room_captain_2', condition='lad_details.saved_variables["day2_evening_billiard_room_captain_talked"]', next_menu="lad_day2_evening_billiard_room_captain_hypothesis_menu", keep_alive = True),
            TimedMenuChoice('Go to the bar for a drink', 'lad_day2_evening_billiard_room_bar', 10, linked_choice ="lad_day2_evening_billiard_room_bar_2"),
            TimedMenuChoice('Have another drink to calm the nerves', 'lad_day2_evening_billiard_room_bar_2', 10, condition = 'lad_details.saved_variables["day2_drinks"] == 1', linked_choice ="lad_day2_evening_billiard_room_bar_3"),
            TimedMenuChoice('Maybe a few more drinks would help', 'lad_day2_evening_billiard_room_bar_3', 30, condition = 'lad_details.saved_variables["day2_drinks"] == 2', linked_choice ="lad_day2_evening_billiard_room_bar_4"),
            TimedMenuChoice('Don\'t listen to him, just get plastered', 'lad_day2_evening_billiard_room_bar_4', 120, condition = 'lad_details.saved_variables["day2_drinks"] == 3'),
            TimedMenuChoice('Leave the room', 'generic_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ lad_day2_evening_billiard_room_menu.early_exit = False

        """
        I am back in the billiard room.
        """

    call run_menu(lad_day2_evening_billiard_room_menu)

    return


label lad_day2_evening_billiard_room_captain_hypothesis_cancel:
    

    return
    

label lad_day2_evening_billiard_room_captain_hypothesis_doctor:

    lad """
    I found this in Daniel Baldwin's room.
    """

    """
    You show him the vial.
    """

    captain """
    Is that a bottle of laudanum?
    """

    lad """
    Yes, there were nearly a dozen like this in Daniel Baldwin's room.
    
    Far more than he would have needed for medical purposes.
    """

    captain """
    All right, but what do you make of that?
    """

    lad """
    I think it's obvious he had an opium addiction.
    """

    captain """
    Possibly, but what if he did?

    Many people are addicted — especially doctors.

    Regardless, opium addicts often die of an overdose, not from a gunshot to the chest.
    """

    """
    Well, I've no response to that.
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

    if current_character.text_id=="lad" and lad_details.threads.is_unlocked('hunt_doctor_drunk'):

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

    So I wouldn't shout "poison" every time you see a green drink.
    """

    if not lad_details.threads.is_unlocked('whisky'):

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
        # TODO what is that??????
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
    Yes, Mr Harring?

    Do you have anything to add to our last conversation?
    """

    call run_menu(lad_day2_evening_billiard_room_captain_hypothesis_menu)

    return


label lad_day2_evening_billiard_room_captain:

    """
    I take a seat opposite Sushil Sinha.

    If he's disturbed by the events of the day, he doesn't show it.
    """

    call common_day2_evening_billiard_room_lad_captain_dismiss

    $ lad_day2_evening_billiard_room_captain_hypothesis_menu = TimedMenu("lad_day2_evening_billiard_room_captain_hypothesis_menu", [
        TimedMenuChoice('Reveal Daniel Baldwin\'s opium addiction{{observation}}', 'lad_day2_evening_billiard_room_captain_hypothesis_doctor', 10, condition="lad_details.threads.is_unlocked('laudanum')"),
        TimedMenuChoice('Point out the strange liquid on Thomas Moody\'s room{{observation}}', 'lad_day2_evening_billiard_room_captain_hypothesis_broken', 10, condition="lad_details.threads.is_unlocked('green_liquid')"),
        TimedMenuChoice('Show the letter found in Samuel\'s Manning room{{object}}', 'lad_day2_evening_billiard_room_captain_hypothesis_drunk_letter', 10, condition="lad_details.threads.is_unlocked('burned_letter')"),
        TimedMenuChoice('Question Samuel Manning\'s state of inebriation at the time of the accident', 'lad_day2_evening_billiard_room_captain_hypothesis_drunk', 10),
        # TODO: If you have ALL the suspicions, you can convince the captain something strange is afoot. Need to decide next steps.
        TimedMenuChoice('Accept you don\'t have any real suspicions', 'lad_day2_evening_billiard_room_captain_hypothesis_cancel', keep_alive=True, early_exit=True),
    ])
    call run_menu(lad_day2_evening_billiard_room_captain_hypothesis_menu)

    call common_day2_evening_billiard_room_lad_captain_close

    $ lad_details.saved_variables["day2_evening_billiard_room_captain_talked"] = True

    return


label lad_day2_evening_billiard_room_bar:

    """
    There isn't a wide variety of drinks, so I take a glass of sherry.
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
    I ignore the captain's disapproving look and head back to the bar.

    Cut me some slack.

    These are extraordinary circumstances.

    Besides, one more can't hurt.
    """

    $ lad_details.threads.unlock('day2_drunk')

    show layer master at drunk_wobble_layer
    $ drunk_mode = True

    return
