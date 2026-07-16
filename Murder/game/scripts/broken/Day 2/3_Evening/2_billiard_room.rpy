# ------------------------------------
#   BILLIARD ROOM - Saturday night
#
#   Present: Captain Sinha (reading by the lamp, a soda water at his elbow)
#   and Mr Manning (drinking, but holding the line). The ladies and the
#   doctor have gone up, and no staff are anywhere to be seen.
#
#   The important business of the night happens here: laying his fears
#   before the pair of them (broken_day2_evening_lay_fears). The Captain
#   decides to trust Moody and offers the idea of the night: ring the
#   dinner gong to bring the whole house down at once
#   (day2_evening_gong_idea -> the gong choice on the night map).
#
#   The Captain's talk also seeds Sunday: if the police have not come by
#   morning, he means to walk to the village himself.
# ------------------------------------
label broken_day2_evening_billiard_room_scene:

    $ change_room('billiard_room')

    if not broken_details.saved_variables['day2_evening_billiard_room_visited']:

        $ broken_details.saved_variables['day2_evening_billiard_room_visited'] = True

        """
        I head to the billiard room, where our hostess said, there would be drinks.

        Only two other guests have come here.

        Captain Sinha sits in the good light with a book open on his knee and a glass of soda water at his elbow.

        Mr Manning has the chair nearest the bar, with a glass of something that is not soda water.

        No butler, no footman, only the three of us.
        
        Good.

        Here are two men I think I can reasonably trust.

        I could convince them that something has to be done tonight.

        But how to make them trust me?
        """

    else:

        # Reset menu
        $ broken_day2_evening_billiard_menu.early_exit = False

        """
        I look in on the billiard room again.

        Captain Sinha and Samuel Manning are still there.
        """

    $ broken_day2_evening_billiard_menu = TimedMenu("broken_day2_evening_billiard_menu", [
        TimedMenuChoice('Join Captain Sinha', 'broken_day2_evening_billiard_captain', 0, keep_alive = True, next_menu = 'broken_captain_night_menu'),
        TimedMenuChoice('Sit with Mr Manning', 'broken_day2_evening_billiard_drunk', 10),
        TimedMenuChoice('Leave the room', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ])

    call run_menu(broken_day2_evening_billiard_menu)

    return


# ------------------------------------
#   LAYING THE FEARS - the Captain's idea
# ------------------------------------
label broken_day2_evening_lay_fears:

    $ broken_details.saved_variables['day2_evening_gong_idea'] = True

    """
    I draw a chair between the two of them, and I do not dress it up.

    Ted Harring dead without a mark. The letters. The staff packing in the dark, the telephone, the tree across the road.

    And my belief, plainly stated, that someone under this roof does not intend all of us to see Monday.
    """

    """
    The Captain closes his book without marking the page, and studies me for a long moment.
    """

    captain """
    I have spent thirty years weighing men, Mr Moody, so I shall tell you plainly what I make of you.

    A great deal about you does not add up.

    But you are not lying about this. That much I can see.

    So I will trust you, and act on what you say.
    """

    drunk """
    That makes two of us, sir.
    """

    captain """
    Then take my advice.

    If every soul in this house is in danger, you do not carry that news from door to door.

    You ring the dinner gong.

    Nobody sleeps through a gong. The whole house will come down, and you will say your piece once, to everyone at the same time.
    """

    """
    The gong.

    Simple, loud, and impossible to ignore.

    It stands in the dining room, and nothing prevents me from walking in there and striking it.

    All that remains is to decide whether I dare.
    """

    return


# ------------------------------------
#   CAPTAIN SINHA (the good light)
# ------------------------------------
label broken_day2_evening_billiard_captain:

    if not broken_details.saved_variables['day2_evening_billiard_captain_approached']:

        $ broken_details.saved_variables['day2_evening_billiard_captain_approached'] = True

        captain """
        Mr Moody. How are you tonight?
        """

        broken """
        Fine, Captain.
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

    broken """
    You are drinking again, Mr Manning.
    """

    drunk """
    Only enough to keep my hands still, sir.

    The events of today have shaken me rather badly.
    """

    """
    I can understand that.

    And it is true that he looks more exhausted than drunk.

    That is good.
    """

    drunk """
    Mr Moody. This morning, in the wood.

    What you kept me from...
    """

    broken """
    No need to talk about it, Mr Manning.

    The real question is what we are going to do now.
    """

    drunk """
    Right.

    Whatever you want to do, I'll follow.

    I owe you that much.
    """

    broken """
    Perfect.

    I am still not sure what our course of action should be, but it is good to know you are on my side.

    I shall keep that in mind.
    """

    """
    Well, that went well enough.

    But I would feel more secure if I could rely on more people than just the two of us.
    """

    $ broken_details.threads.unlock('manning_partner')

    return
