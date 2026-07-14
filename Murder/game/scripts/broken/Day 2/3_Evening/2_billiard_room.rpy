# ------------------------------------
#   BILLIARD ROOM - Saturday night
#
#   Present: Captain Sinha (reading by the lamp, a soda water at his elbow)
#   and Mr Manning (drinking, but holding the line). The ladies and the
#   doctor have gone up, and no staff are anywhere to be seen.
#
#   The important business of the night happens here: laying his fears
#   before the pair of them and proposing the watch
#   (broken_day2_evening_propose_watch -> day2_evening_watch_agreed, one of
#   the two conditions of gather_everyone).
#
#   The Captain's talk also seeds Sunday: if the police have not come by
#   morning, he means to walk to the village himself.
# ------------------------------------
label broken_day2_evening_billiard_room_scene:

    $ change_room('billiard_room')

    if not broken_details.saved_variables['day2_evening_billiard_room_visited']:

        $ broken_details.saved_variables['day2_evening_billiard_room_visited'] = True

        """
        Drinks in the billiard room, our hostess said, and here is what remains of the promise.

        Captain Sinha sits in the good light with a book open on his knee and a glass of soda water at his elbow.

        Mr Manning has the chair nearest the bar, and a glass of something that is not soda water stands guard beside him.

        No butler, no footman. The two of them have poured for themselves like men in a railway waiting room.
        """

    else:

        # Reset menu
        $ broken_day2_evening_billiard_menu.early_exit = False

        """
        I look in on the billiard room again.

        The Captain has not turned many pages. Mr Manning's glass is no emptier than it was.
        """

    $ broken_day2_evening_billiard_menu = TimedMenu("broken_day2_evening_billiard_menu", [
        TimedMenuChoice('Join Captain Sinha and his book', 'broken_day2_evening_billiard_captain', 0, keep_alive = True, next_menu = 'broken_captain_night_menu'),
        TimedMenuChoice('Sit with Mr Manning', 'broken_day2_evening_billiard_drunk', 0, keep_alive = True, next_menu = 'broken_drunk_night_menu'),
        TimedMenuChoice('Lay your fears before them and propose a watch', 'broken_day2_evening_propose_watch', 20, keep_alive = True, condition = "not broken_details.saved_variables['day2_evening_watch_agreed']"),
        TimedMenuChoice('Leave the room', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ])

    call run_menu(broken_day2_evening_billiard_menu)

    return


# ------------------------------------
#   THE WATCH PROPOSAL
# ------------------------------------
label broken_day2_evening_propose_watch:

    $ broken_details.saved_variables['day2_evening_watch_agreed'] = True

    """
    I draw a chair between the two of them, and I do not dress it up.

    Ted Harring dead without a mark. The letters. The staff packing in the dark, the telephone, the tree across the road.

    And my belief, plainly stated, that someone under this roof does not intend all of us to see Monday.
    """

    captain """
    You are proposing a watch.
    """

    broken """
    I am proposing that nobody in this house spends tonight alone and asleep at the same time.

    Watches in turn, on the landing, where every door can be seen.

    And the ladies and the doctor warned to lock themselves in.
    """

    """
    The Captain closes his book without marking the page.
    """

    captain """
    In Burma we called it a stand-to, and I have never once regretted ordering it.

    Mr Manning and I shall take the first watch together.

    Come down when you have knocked on your doors, Mr Moody, and we shall divide the night.
    """

    drunk """
    I'll stand mine sober, sir.

    That much I can still promise a man.
    """

    """
    He pushes the glass away as he says it, a whole arm's length, and looks rather surprised at his own hand.

    Two of them. Now for the rest of the house.
    """

    call broken_day2_evening_check_gathered

    return


# ------------------------------------
#   CAPTAIN SINHA (the good light)
# ------------------------------------
label broken_day2_evening_billiard_captain:

    if not broken_details.saved_variables['day2_evening_billiard_captain_approached']:

        $ broken_details.saved_variables['day2_evening_billiard_captain_approached'] = True

        """
        I cross to the lamp.

        Two days ago I could not have stood this close to the man without my hands remembering the rifle.

        Tonight I only want to know what he is made of, because tonight may require it.
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
        I return to the Captain's post by the lamp.
        """

    $ broken_captain_night_menu = TimedMenu("broken_captain_night_menu", [
        TimedMenuChoice('Ask what he makes of the fallen tree', 'broken_day2_evening_captain_tree', 15),
        TimedMenuChoice("Ask his opinion of Mr Harring's death", 'broken_day2_evening_captain_harring', 15),
        TimedMenuChoice('Sound him out about tomorrow', 'broken_day2_evening_captain_tomorrow', 20),
        TimedMenuChoice('Leave him to his book', 'generic_cancel', 0, keep_alive = True, early_exit = True)
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
    He looks into the lamplight for a moment.
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
#   MR MANNING (the chair nearest the bar)
# ------------------------------------
label broken_day2_evening_billiard_drunk:

    if not broken_details.saved_variables['day2_evening_billiard_drunk_approached']:

        $ broken_details.saved_variables['day2_evening_billiard_drunk_approached'] = True

        """
        Manning watches the fire as though it might try something, one hand curled round his glass.

        He looks up as I draw a chair beside his, and does not look away.

        A day ago he could not hold my eye at all.
        """

        broken """
        You are drinking again, Mr Manning.
        """

        drunk """
        Only enough to keep my hands still, sir.

        I have been counting my way down this one glass for two hours, and I am still winning.
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

        Then I shall say only this, sir. If you should ever have need of me, for anything at all, you shall have me.

        And as near sober as I can manage.
        """

        """
        I have made no friends behind this mask.

        It occurs to me, settling beside him in the lamplight, that this ruined old fellow may prove to be the first.
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

    My hands have not been still since noon, and this is the first glass of a day that would ordinarily have cost me a bottle.
    """

    """
    He gives a small, dry laugh, with no self-pity in it that I can hear.
    """

    drunk """
    I have not been dry two days together since Margaret died.

    It is a poor time to make promises, with all this going on.

    But a smaller glass tonight than last night, and a smaller one again tomorrow.

    A lawyer knows better than to swear to more than he can prove.
    """

    broken """
    Then we shall prove it one evening at a time, Mr Manning, and leave the bottles where they stand.
    """

    return
