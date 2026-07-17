# ------------------------------------
#   BILLIARD ROOM - Saturday night
#
#   Present: Captain Sinha (reading by the lamp, a soda water at his elbow)
#   and Mr Manning (drinking, but holding the line). The ladies and the
#   doctor have gone up, and no staff are anywhere to be seen.
#
#   The important business of the night happens here: convincing the
#   Captain. Three facts gathered around the house each open a question
#   for him (staff_missing, phone_dead, drunk_partner). Once all three
#   have been told (day2_evening_captain_facts), Moody decides he can
#   reveal the last part (captain_convinced thread) and the final
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
    # open a question (staff_missing, phone_dead, drunk_partner). Every
    # question ends by calling the check label: once all three facts have
    # been told, the reveal monologue plays and 'Show him the order'
    # appears - it wins his trust, he proposes the gong, and the gong is
    # rung directly from that scene (no map choice).
    $ broken_captain_night_menu = TimedMenu("broken_captain_night_menu", [
        TimedMenuChoice('Ask what he makes of the fallen tree', 'broken_day2_evening_captain_tree', 10),
        TimedMenuChoice("Ask his opinion of Mr Harring's death", 'broken_day2_evening_captain_harring', 10),
        TimedMenuChoice('Tell him the staff are gone', 'broken_day2_evening_captain_staff', 10, condition = "broken_details.threads.is_unlocked('staff_missing')"),
        TimedMenuChoice('Tell him the telephone is dead', 'broken_day2_evening_captain_phone', 10, condition = "broken_details.threads.is_unlocked('phone_dead')"),
        TimedMenuChoice('Show him the order', 'broken_day2_evening_captain_order', 0, early_exit = True, condition = "broken_details.threads.is_unlocked('captain_convinced') and broken_details.threads.is_unlocked('drunk_partner')"),
        TimedMenuChoice('Leave him to his book', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "captain")

    call run_menu(broken_captain_night_menu)

    return


label broken_day2_evening_captain_tree:

    broken """
    What do you make of this business with the road, Captain?

    A tree preventing the police from coming, don't you think that is strange?
    """

    captain """
    Strange? Far from it.
    
    With the storm we've had yesterday, some damage was to be expected.

    I am just happy that the house was untouched.
    """

    return


label broken_day2_evening_captain_harring:

    broken """
    You are really not surprised by Ted Harring's death.

    Healthy young men do not just die in their sleep.

    You heard the doctor. No mark, and no cause.
    """

    captain """
    I admit it is unusual, but not unheard of.

    Sadly, I have seen people not much older than Mr Harring dying the same way.

    Of overdose, heart attacks, or other failing of the body.

    Death comes sometimes out of the blue.
    
    And not just in the battlefield Mr Moody.

    It is good to keep that in mind.
    """

    return


# ------------------------------------
#   THE THREE FACTS - convincing the Captain
# ------------------------------------
# One label per fact gathered around the house. Every question in the
# Captain's menu ends by calling the check label: once all three facts
# have been told, the reveal monologue plays once and the 'Show him the
# order' question opens.
label broken_day2_evening_captain_check_convinced:

    if broken_details.saved_variables['day2_evening_captain_facts'] < 2:

        return

    $ broken_details.threads.unlock('captain_convinced')

    """
    The staff gone. The telephone dead. 
    
    I don't know if that was enough to raise some suspicion.

    I hope so, because if not, he might not believe me when I tell him the full story.
    """

    if broken_details.threads.is_unlocked('drunk_partner'):

        """
        Samuel Manning will go with what I say, so I can ask the question now.
        """

    else:

        """
        One last thing before I reveal the whole story.

        I should see if Samuel Manning will go along with it.
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
    Is that so?

    They could be just sleeping, couldn't they?
    """

    broken """
    I thought so at first, but I made such noise in the attic that it is very unlikely nobody heard me.
    """

    captain """
    Strange, but there could be a logical explanation.

    For instance, maybe they had to go to the city for some errands.
    """

    broken """
    In the middle of the night?
    """

    captain """
    Right, that would be uncommon indeed.

    But I am sure they will be back tomorrow.
    """

    broken """
    I wouldn't be so sure of it.
    """

    captain """
    Well, I guess we will see, won't we.
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
    And you assume what? That the phone was cut intentionally?
    """

    broken """
    Well, it is rather strange isn't it?
    """

    captain """
    Not that much.

    You are aware there was a storm, it might have damaged the line.

    Or maybe there is a problem with the operator.

    Sadly, those rural lines are rarely reliable.
    """

    broken """
    Right, of course.

    But the timing is the reason for my suspicions.

    A call was supposedly made, then a few moments later it is not working.

    I find it hard to believe.
    """

    captain """
    Well, I admit it is a big coincidence.

    But not really a cause for alarm either.
    """

    call broken_day2_evening_captain_check_convinced

    return

# ------------------------------------
#   Captain 
# ------------------------------------
label broken_day2_evening_captain_order:

    broken """
    Captain, there is something you must know.
    """

    """
    I glance at Mr Manning first.

    He answers with a small nod.
    """

    broken """
    This morning in the wood, Captain, you did not realise it, but there was very nearly two more deaths.
    """

    """
    At this, he shows a little surprise.
    """

    captain """
    Two more deaths?
    
    What do you mean by that?
    """

    broken """
    Well, somebody left Mr Manning a letter blaming Doctor Baldwin for the loss of his wife.

    It was written to put a rifle in a grieving man's hands, and hope he would arm the doctor, without incriminating themselves.
    """

    """
    He pauses for a second, then turns to Samuel Manning.
    """

    captain """
    Mr Manning, is that true?
    """

    drunk """
    Well, it is.

    I don't know that I would really have hurt the doctor, but god knows I wanted to.

    If it wasn't for Mr Moody, I can't say what would have happened.
    """

    captain """
    Really, well if this is true, I guess Doctor Baldwin owes a lot of gratitude to you, Mr Moody.
    """

    drunk """
    It is true, I swear!

    I can't show you the letter, I burnt it, you see, and...
    """

    captain """
    It is alright Mr Manning.

    Let's say I believe you.

    But, Mr Moody, how did you learn of Mr Manning's plan?
    """

    broken """
    I was suspicious of Mr Manning for a simple reason.

    I received a letter myself.
    """

    """
    I take the order from my pocket and hand it to him.

    The Captain reads it once, and then again more slowly.

    For a long moment he says nothing at all.
    """

    captain """
    I see, that is clever.

    I suppose this order was meant to turn you against me.

    But I can assure you it is obviously a fake.

    It looks nothing like the one I used.

    But I assumed you came to the same conclusion.

    Otherwise I could have been another victim.

    That is what you are implying Mr Moody is it not?

    Mr Manning was given a letter to make him hate the doctor.

    You were given this, to make you hate me.

    The goal was to have two more deaths this weekend.
    """

    broken """
    Yes, that is my belief, Captain.
    """

    """
    He closes his book without marking the page, and studies me for a long moment.
    """

    captain """
    Tell me, Mr Moody, why would I trust you.

    You may have fabricated this whole story.
    """

    broken """
    I suppose, but to what end?

    I have nothing to gain here.
    """

    captain """
    Maybe not.

    But this situation is surreal.

    I do not know what to make of it.
    """

    broken """
    I understand.

    If you'll allow me, I'll try to explain how I see things.
    """

    captain """
    Please, do.
    """

    drunk """
    Yes, what on earth do you think is happening this weekend?
    """

    broken """
    Very well, let me tell you something about myself first.

    I am not a car mechanic like I let some people believe.

    I am a journalist, and I made a bit of research before coming here.
    """

    captain """
    A journalist, but why didn't you say so?
    """

    broken """
    Because it is better not to attract attention when conducting an investigation.

    If I had declared myself a journalist, I am sure that would have made some people reluctant to talk to me.
    """

    """
    That should be enough of an explanation for now.

    No need for the full story just yet.
    """

    captain """
    Right, so all this time you were investigating us. Interesting.

    What have you found then?
    """

    broken """
    Quite a few things.

    But I realise now it is better I share them with everyone.

    I just needed to trust a couple of people before I do.

    Can I count on you, Captain?
    """

    captain """
    You can.

    And you must know, I carry a pistol on me.
    """

    broken """
    Good, I have no idea what kind of resistance we will encounter here.

    Now we should gather the rest of the guests.
    """

    captain """
    Indeed, then take my advice.

    Do not waste time going from door to door.

    There is a simple way to alert everyone in case of an emergency in a house like this one.

    You ring the dinner gong.

    Nobody sleeps through a gong. The whole house will come down, and you will say your piece once, to everyone at the same time.
    """

    """
    The gong.

    Simple, loud, and impossible to ignore.
    """

    broken """
    Good idea, Captain.

    Let's all go to the dining room then.
    """

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

    $ broken_details.threads.unlock('drunk_partner')

    return
