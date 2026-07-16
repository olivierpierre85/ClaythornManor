# ------------------------------------
#   BILLIARD ROOM - Saturday night
#
#   Present: Captain Sinha (reading by the lamp, a soda water at his elbow)
#   and Mr Manning (drinking, but holding the line). The ladies and the
#   doctor have gone up, and no staff are anywhere to be seen.
#
#   The important business of the night happens here: convincing the
#   Captain. Three facts gathered around the house each open a question
#   for him (staff_missing, phone_dead, manning_partner). Once all three
#   have been told (day2_evening_captain_facts), Moody decides he can
#   reveal the last part (day2_evening_captain_convinced) and the final
#   question appears: show him the order. Convinced, the Captain proposes
#   the dinner gong, and it is rung straight from that scene
#   (broken_day2_evening_ring_gong) - never from the map.
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
#   CAPTAIN SINHA
# ------------------------------------
label broken_day2_evening_billiard_captain:

    if not broken_details.saved_variables['day2_evening_billiard_captain_approached']:

        $ broken_details.saved_variables['day2_evening_billiard_captain_approached'] = True

        captain """
        Mr Moody. How are you tonight?
        """

        broken """
        I am doing all right, considering, Captain.

        What about you?
        """

        captain """
        I am doing well enough.

        It is true that what happened to Mr Harring is tragic, but these things happen.

        I would not worry about it too much.
        """

        """
        Of course, for him the death of Ted Harring is the only unusual event of this weekend.

        It might be complicated to convince him otherwise.

        But I shouldn't tell him everything at once.

        That could unnerve him.

        Let's proceed carefully.
        """


    else:

        $ broken_captain_night_menu.early_exit = False

    # Convincing the Captain: three facts gathered around the house each
    # open a question (staff_missing, phone_dead, manning_partner). Every
    # question ends by calling the check label: once all three facts have
    # been told, the reveal monologue plays and 'Show him the order'
    # appears - it wins his trust, he proposes the gong, and the gong is
    # rung directly from that scene (no map choice).
    $ broken_captain_night_menu = TimedMenu("broken_captain_night_menu", [
        TimedMenuChoice('Ask what he makes of the fallen tree', 'broken_day2_evening_captain_tree', 10),
        TimedMenuChoice("Ask his opinion of Mr Harring's death", 'broken_day2_evening_captain_harring', 10),
        TimedMenuChoice('Tell him the staff are gone', 'broken_day2_evening_captain_staff', 10, condition = "broken_details.threads.is_unlocked('staff_missing')"),
        TimedMenuChoice('Tell him the telephone is dead', 'broken_day2_evening_captain_phone', 10, condition = "broken_details.threads.is_unlocked('phone_dead')"),
        TimedMenuChoice('Tell him what happened in the wood', 'broken_day2_evening_captain_wood', 10, condition = "broken_details.threads.is_unlocked('manning_partner')"),
        TimedMenuChoice('Show him the order', 'broken_day2_evening_captain_order', 0, early_exit = True, condition = "broken_details.saved_variables['day2_evening_captain_convinced']"),
        TimedMenuChoice('Leave him to his book', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "captain")

    call run_menu(broken_captain_night_menu)

    return


label broken_day2_evening_captain_tree:

    broken """
    What do you make of this business with the road, Captain?

    Don't you think that is strange?
    """

    captain """
    Strange? Far from it.
    
    With the storm we've had yesterday, it was to be expected to have some damage.

    I am just happy that the house was untouched.
    """

    call broken_day2_evening_captain_check_convinced

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

    call broken_day2_evening_captain_check_convinced

    return


# ------------------------------------
#   THE THREE FACTS - convincing the Captain
# ------------------------------------
# One label per fact gathered around the house. Every question in the
# Captain's menu ends by calling the check label: once all three facts
# have been told, the reveal monologue plays once and the 'Show him the
# order' question opens.
label broken_day2_evening_captain_check_convinced:

    if broken_details.saved_variables['day2_evening_captain_facts'] < 3 or broken_details.saved_variables['day2_evening_captain_convinced']:

        return

    $ broken_details.saved_variables['day2_evening_captain_convinced'] = True

    """
    The staff gone. The telephone dead. A letter written to turn one guest against another.

    He has weighed each piece like evidence, and put none of it aside.

    Now I think I can reveal the last part.

    The order that was slipped under my own door.
    """

    return


label broken_day2_evening_captain_staff:

    $ broken_details.saved_variables['day2_evening_captain_facts'] += 1

    broken """
    Captain, I have been below stairs tonight.

    The kitchen fire is out, the attic is locked and silent, and there is not a servant left in this house.

    The gun room has been emptied too. Every rifle we carried this morning is gone.

    I believe the staff are gone, and that they do not mean to come back.
    """

    captain """
    Servants do not desert a good post in the night, Mr Moody.

    They go when they have been warned, or when they have been paid to go.

    And a man who gathers up the guns before a quiet night expects the night to be otherwise.
    """

    call broken_day2_evening_captain_check_convinced

    return


label broken_day2_evening_captain_phone:

    $ broken_details.saved_variables['day2_evening_captain_facts'] += 1

    broken """
    I tried the telephone in the hall, Captain.

    The line is dead. No operator, no exchange, nothing at all.

    Yet at dinner our hostess told us she had telephoned the police station this very evening.
    """

    captain """
    Then either the line has died since dinner, or no call was ever placed.

    Set it beside the tree across the road, Mr Moody.

    A blocked road and a dead wire. That is not misfortune. That is a siege.
    """

    call broken_day2_evening_captain_check_convinced

    return


label broken_day2_evening_captain_wood:

    $ broken_details.saved_variables['day2_evening_captain_facts'] += 1

    """
    I glance at Mr Manning first.

    He answers with a small nod. His story is mine to tell now.
    """

    broken """
    This morning in the wood, Captain, there was very nearly a second death.

    Somebody sent Mr Manning a letter blaming Doctor Baldwin for the loss of his wife.

    It was written to put a rifle in a grieving man's hands, and it all but succeeded.
    """

    drunk """
    It did succeed, sir, in everything but the trigger.

    Mr Moody talked the rifle out of my hands. That is the whole of my part in this weekend.
    """

    captain """
    Then the letter is the crime, gentlemen, not the man who received it.

    A grudge does not find its own way to a house party. Somebody posts it there.

    Whoever gathered us under this roof knew what each of us carried, and meant to set us upon one another.
    """

    call broken_day2_evening_captain_check_convinced

    return


# ------------------------------------
#   THE ORDER - the Captain's trust, his idea, and the gong
# ------------------------------------
# The last question. Showing the order wins the Captain over: he proposes
# the gong, and the gong is rung on the spot (broken_day2_evening_ring_gong,
# 0_map_choices.rpy). Both outer menus are closed on the way out, so the
# night map ends here.
label broken_day2_evening_captain_order:

    """
    I take the order from my pocket and hand it to him.

    An old army order, for the transfer of an officer, slipped under my door.

    And at the foot of it, in a neat staff officer's hand, his own name.
    """

    """
    The Captain reads it once, and then again more slowly.

    For a long moment he says nothing at all.
    """

    captain """
    That is my hand, and my name.

    I must have signed a hundred papers like this one, and thought no more of each than of the weather.
    """

    """
    He lays it flat on his knee, the way a man lays down a card.
    """

    captain """
    Mr Manning was given a letter to make him hate the doctor.

    You were given this, to make you hate me.

    Somebody is loading us like rifles, and pointing us at one another.
    """

    broken """
    That is my belief, Captain.

    And I would rather show it to you than act upon it.
    """

    """
    He closes his book without marking the page, and studies me for a long moment.
    """

    captain """
    I have spent thirty years weighing men, Mr Moody, so I shall tell you plainly what I make of you.

    A great deal about you does not add up.

    But a man who is handed a reason to hate me, and brings it to me instead, is no enemy of mine.

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

    I am on my feet before my nerve can fail me, and I go straight to the dining room.
    """

    # The decision is made here and now: close the billiard and map menus,
    # then ring the gong directly. Unwinding the menus after the return
    # lands back in 1_main at 23:30 with gather_everyone unlocked.
    $ all_menus[broken_day2_evening_billiard_menu.id].early_exit = True
    $ all_menus[broken_details.saved_variables["day2_evening_map_menu"].id].early_exit = True

    call broken_day2_evening_ring_gong

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

    And it is true that for once, he doesn't look drunk.

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
