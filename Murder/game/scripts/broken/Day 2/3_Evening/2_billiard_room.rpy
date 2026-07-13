# ------------------------------------
#   BILLIARD ROOM - Saturday night (found_poison path)
#
#   Present: Captain Sinha (drinking soda water) and a sober Mr Manning.
#   The ladies and the doctor have retired, and the butler's corner stands
#   empty - the staff are already preparing their departure in the night.
#
#   The Captain's talk seeds Sunday: if the police have not come by morning,
#   he means to walk to the village himself.
# ------------------------------------
label broken_day2_evening_billiard_room:

    $ change_room('billiard_room')

    if not broken_details.saved_variables['day2_evening_billiard_room_visited']:

        $ broken_details.saved_variables['day2_evening_billiard_room_visited'] = True

        """
        The billiard room is a far quieter gathering than it was last night.

        Captain Sinha stands by the fire with a glass of soda water. Mr Manning has taken the chair furthest from the bar, which tells its own story.

        Of the ladies and the doctor there is no sign.

        And for the first time this weekend, the butler's corner stands empty.

        No one is serving. The bottles wait abandoned on the bar.

        A billiard room without a servant in it, in a house like this, is a small wrongness all of its own.
        """

        $ broken_day2_evening_billiard_menu = TimedMenu("broken_day2_evening_billiard_menu", [
            TimedMenuChoice('Join Captain Sinha by the fire', 'broken_day2_evening_billiard_captain', 0, keep_alive = True, next_menu = 'broken_captain_night_menu'),
            TimedMenuChoice('Sit with Mr Manning', 'broken_day2_evening_billiard_drunk', 0, keep_alive = True, next_menu = 'broken_drunk_night_menu'),
            TimedMenuChoice('Leave the room', 'generic_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ broken_day2_evening_billiard_menu.early_exit = False

        """
        I look in on the billiard room again.

        The fire has burned lower, and nobody has fed it.
        """

    call run_menu(broken_day2_evening_billiard_menu)

    return


# ------------------------------------
#   CAPTAIN SINHA (by the fire)
# ------------------------------------
label broken_day2_evening_billiard_captain:

    if not broken_details.saved_variables['day2_evening_billiard_captain_approached']:

        $ broken_details.saved_variables['day2_evening_billiard_captain_approached'] = True

        """
        I cross to the fire.

        Two days ago I could not have stood this close to the man without my hands remembering the rifle.

        Tonight I only want to know what he is made of, because tomorrow may require it.
        """

        captain """
        Mr Moody.

        Not drinking either, I observe.
        """

        broken """
        It seems to be catching, Captain.
        """

    else:

        $ broken_captain_night_menu.early_exit = False

        """
        I return to the Captain's post by the fire.
        """

    $ broken_captain_night_menu = TimedMenu("broken_captain_night_menu", [
        TimedMenuChoice('Ask what he makes of the fallen tree', 'broken_day2_evening_captain_tree', 15),
        TimedMenuChoice("Ask his opinion of Mr Harring's death", 'broken_day2_evening_captain_harring', 15),
        TimedMenuChoice('Sound him out about tomorrow', 'broken_day2_evening_captain_tomorrow', 20),
        TimedMenuChoice('Leave him to the fire', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "captain")

    call run_menu(broken_captain_night_menu)

    return


label broken_day2_evening_captain_tree:

    broken """
    What do you make of this business with the road, Captain?
    """

    captain """
    A tree may fall by chance. I have seen it happen.

    But consider what this one has accomplished.

    No police. No telegraph boy. No tradesman's van. A full day, bought with one trunk of timber.

    If I wished to cut a house such as this one off from the world, I should do precisely what has been done.
    """

    """
    He says it evenly, the way another man would remark on the weather.

    It is the first thing he has said all weekend that I am certain is not a performance.
    """

    return


label broken_day2_evening_captain_harring:

    broken """
    And Mr Harring?

    You heard the doctor. No mark, and no cause.
    """

    captain """
    I have known men die without a mark before, Mr Moody.

    It was rarely nature's doing.
    """

    """
    He looks into the fire for a moment.
    """

    captain """
    A healthy young man does not simply stop in the night.

    I said nothing this morning because there was nothing useful to say.

    But I have not stopped thinking it.
    """

    return


label broken_day2_evening_captain_tomorrow:

    broken """
    And if the police have not come by morning?
    """

    captain """
    Then I do not intend to wait upon them any longer.

    If there is no motor and no telephone, there are still two legs and a road.

    The village cannot be above seven miles. I shall walk it, and bring the constabulary back myself.
    """

    """
    He sets down his glass and looks at me directly.
    """

    captain """
    I would be glad of company, if any man here is fit for the distance.
    """

    broken """
    You may count on mine, Captain.
    """

    """
    So there it is.

    Whatever else tomorrow brings, I shall not have to face it alone.
    """

    return


# ------------------------------------
#   MR MANNING (the chair furthest from the bar)
# ------------------------------------
label broken_day2_evening_billiard_drunk:

    if not broken_details.saved_variables['day2_evening_billiard_drunk_approached']:

        $ broken_details.saved_variables['day2_evening_billiard_drunk_approached'] = True

        """
        Manning sits with his hands folded in his lap, watching the fire as though it might try something.

        He looks up as I draw a chair beside his, and does not look away.

        A day ago he could not hold my eye at all.
        """

        broken """
        You are not drinking, Mr Manning.
        """

        drunk """
        No.

        No, I find I have rather lost the taste for it.
        """

        """
        He glances at the bottles waiting on the bar, the way a man looks at an old enemy.
        """

        drunk """
        Mr Moody. This morning, in the wood.

        What you kept me from...
        """

        broken """
        Was nothing at all, Mr Manning, because nothing at all took place.

        A quiet morning, and poor shooting. We shall leave it there.
        """

        """
        He nods, slowly, and something crosses his face that might, in a better week, have been a smile.
        """

        drunk """
        A quiet morning. Yes.

        Then I shall say only this, sir. If you should ever have need of me, for anything at all, you shall have me sober.
        """

        """
        I have made no friends behind this mask.

        It occurs to me, settling beside him in the firelight, that this ruined old fellow may prove to be the first.
        """

    else:

        $ broken_drunk_night_menu.early_exit = False

        """
        I go back to Mr Manning's corner.
        """

    $ broken_drunk_night_menu = TimedMenu("broken_drunk_night_menu", [
        TimedMenuChoice('Compare the two letters', 'broken_day2_evening_drunk_letters', 20),
        TimedMenuChoice('Ask how he is bearing up', 'broken_day2_evening_drunk_bearing', 15),
        TimedMenuChoice('Leave him be', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_left = "drunk")

    call run_menu(broken_drunk_night_menu)

    return


label broken_day2_evening_drunk_letters:

    broken """
    Mr Manning. The letter you were sent.

    What it said about your wife, about the medicine. Had any of that ever been printed? Spoken of at an inquest? Anything public at all?
    """

    """
    He is quiet a long moment, and when he answers, it is not the drunkard speaking. It is the lawyer.
    """

    drunk """
    No, sir.

    I made certain of that at the time. For her sake.

    What was in that letter was known to three people. One of them is in the ground beside her, and the other two are the doctor and myself.
    """

    broken """
    And mine quoted an army transfer order, number and date, from an autumn seven years gone.

    That is not gossip either. That is a records office.
    """

    drunk """
    Then whoever wrote to us did not overhear our griefs, Mr Moody.

    They went looking for them. Methodically. Long before any invitation was ever sent.
    """

    """
    We sit with that a while, the fire ticking between us.

    This weekend was not arranged in a week. It has been researched, the way I would research a story.

    And I doubt very much the research stopped at the two of us.
    """

    return


label broken_day2_evening_drunk_bearing:

    broken """
    How are you bearing up, Mr Manning? And honestly, if you please.
    """

    drunk """
    Honestly.

    My hands have not been still since noon, and I have counted the bottles on that bar eleven times.
    """

    """
    He gives a small, dry laugh, with no self-pity in it that I can hear.
    """

    drunk """
    I have not been dry two days together since Margaret died.

    It is a poor time to start, with all this going on.

    But then, it is the only time I have.
    """

    broken """
    Then we shall count the bottles together, and leave them where they stand.
    """

    return
