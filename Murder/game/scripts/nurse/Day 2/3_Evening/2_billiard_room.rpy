# Billiard Room - Saturday Evening
label nurse_day2_evening_billiard_room:

    $ change_room("billiard_room")

    if not nurse_details.saved_variables["day2_evening_billiard_room_visited"]:

        $ nurse_details.saved_variables["day2_evening_billiard_room_visited"] = True

        """
        A single lamp burns at the far end of the room.

        Captain Sinha is alone on a chair, reading.

        He turns as I enter, but does not seem surprised to see me.
        """

        $ nurse_day2_evening_billiard_room_menu = TimedMenu("nurse_day2_evening_billiard_room_menu", [
            TimedMenuChoice('Go to the sideboard for a drink', 'nurse_day2_evening_billiard_room_bar', 10),
            TimedMenuChoice('Talk to Captain Sinha', 'nurse_day2_evening_billiard_room_captain_intro', next_menu="nurse_day2_evening_billiard_room_captain_menu"),
            TimedMenuChoice('Leave', 'nurse_day2_evening_billiard_room_leave', 0, keep_alive=True, early_exit=True),
        ])

    else:

        """
        The Captain is still here.

        He glances up as I enter and raises his glass slightly.
        """

        $ nurse_day2_evening_billiard_room_menu.early_exit = False

    call run_menu(nurse_day2_evening_billiard_room_menu)

    call nurse_day2_evening_check_exhaustion

    return


label nurse_day2_evening_billiard_room_bar:

    """
    I take a step towards the sideboard, then stop myself.

    What am I doing?

    No. That is the last thing I need tonight.

    I turn away before the Captain notices.
    """

    return


label nurse_day2_evening_billiard_room_captain_intro:

    captain """
    Miss Marsh.

    I thought everyone had retired.
    """

    nurse """
    Not quite yet.
    """

    captain """
    Nor am I.

    Help yourself to something, if you wish.
    """

    """
    I decline with a small shake of my head.

    He carries his glass to the chairs by the fire.

    After a moment, I follow him.
    """

    captain """
    You look as though something is troubling you, Miss Marsh.
    """

    nurse """
    I confess it is.

    There are things about this weekend that I cannot quite account for.
    """

    captain """
    Oh?

    Such as?
    """

    nurse """
    I am not certain I can put it into words.

    But I cannot help feeling that something here is wrong.
    """

    """
    He watches me for a moment, then nods, once.
    """

    captain """
    Very well, Miss Marsh. Say what is on your mind.
    """

    $ nurse_day2_evening_billiard_room_captain_menu = TimedMenu("nurse_day2_evening_billiard_room_captain_menu", [
        TimedMenuChoice('Something is not right about the staff{{observation}}', 'nurse_day2_evening_billiard_room_staff', 15, condition="nurse_details.threads.is_unlocked('maid_actress') and nurse_details.threads.is_unlocked('footman_belgian')"),
        TimedMenuChoice('I was at the Boxer Rebellion too{{observation}}', 'nurse_day2_evening_billiard_room_boxer', 15, condition="nurse_details.threads.is_unlocked('remember_doctor')", linked_choice="nurse_day2_evening_billiard_room_boxer_2"),
        TimedMenuChoice('About your rank at the Boxer Rebellion{{observation}}', 'nurse_day2_evening_billiard_room_boxer_2', 15, condition="is_linked_choice_hidden('nurse_day2_evening_billiard_room_captain_menu', 'nurse_day2_evening_billiard_room_boxer_2')", linked_choice="nurse_day2_evening_billiard_room_zanzibar_confrontation"),
        TimedMenuChoice('About the Zanzibar War{{observation}}', 'nurse_day2_evening_billiard_room_zanzibar_confrontation', 15, condition="is_linked_choice_hidden('nurse_day2_evening_billiard_room_captain_menu', 'nurse_day2_evening_billiard_room_zanzibar_confrontation') and nurse_details.threads.is_unlocked('captain_lie_zanzibar') and not nurse_details.threads.is_unlocked('captain_fraud')"),
        TimedMenuChoice('Leave', 'nurse_day2_evening_billiard_room_leave', 0, keep_alive=True, early_exit=True),
    ])

    call run_menu(nurse_day2_evening_billiard_room_captain_menu)

    return


label nurse_day2_evening_billiard_room_staff:

    nurse """
    The staff here.

    Have you taken much notice of them, Captain?
    """

    captain """
    In what sense?
    """

    """
    I should be careful here, I can't really say I went searching their rooms.
    """

    nurse """
    The footman.

    There is something in the way he speaks.

    A vowel here, a cadence there — not quite English.

    I noticed it this afternoon and could not entirely set it aside.
    """

    captain """
    A foreign-born man in service is hardly remarkable, Miss Marsh.

    Half the footmen in London came over from the continent at one point or another.
    """

    nurse """
    And the maid.

    I have the strangest feeling I have seen her before somewhere.

    Not here.

    In London, perhaps.

    A theatre, I think.

    There is something too precise about her — her movements, her expressions.
    """

    captain """
    You think you once saw a housemaid on stage.
    """

    """
    He does not say it unkindly, but he does not say it with conviction either.
    """

    captain """
    An accent and a familiar face are not evidence of anything, Miss Marsh.

    People land where they can, and do what they must.

    I would not read too much into it.
    """

    """
    He is not wrong.

    But I am not entirely satisfied either.
    """

    return


label nurse_day2_evening_billiard_room_boxer:

    nurse """
    Yesterday you told a story about the Boxer Rebellion.
    """

    captain """
    Yes, I might have. What of it?
    """

    nurse """
    I was there too, you know.

    As a nurse, attached to the field hospital at Tientsin before the column set out for Peking.
    """

    """
    He pauses.

    This surprises him.
    """

    captain """
    Were you indeed?

    That is a remarkable coincidence.
    """

    nurse """
    There is more.

    Daniel Baldwin was there too.

    He was a young doctor at the time — I am almost certain of it.

    When you spoke of your campaign on Friday evening, it all came back to me.
    """

    """
    He is quiet for a moment.
    """

    captain """
    Baldwin.

    Yes.

    I might remember a doctor by that name.

    But I never made the connection, it's no like we were in the same circles.

    This is very strange.
    """

    nurse """
    I have been wondering if anyone else here might have been present.

    Thomas Moody, perhaps?
    """

    captain """
    Moody.

    It is not impossible, I suppose.

    Though I could not say with any certainty.

    It would be difficult to recognise him with his mask on.
    """

    nurse """
    What about Ted Harring?
    """

    captain """
    No.

    Far too young.

    He would have been a boy.
    """

    nurse """
    Lady Claythorn? Samuel Manning? Mrs Baxter?
    """

    captain """
    I honestly do not remember.

    It was a long time ago, and there were a great many people passing through those camps.

    I would not stake much on absence of memory.
    """

    """
    He sets down his glass.
    """

    captain """
    Three guests at this table who were all in China at the same time.

    It is strange, I grant you that.

    But it is not completely impossible.

    And with terrible things that happened this week-end, I will concede that something is not quite right.

    I'll be on my guards from now on, and I suggest you do the same.
    """

    $ nurse_details.threads.unlock('boxer_rebellion_1')

    return


label nurse_day2_evening_billiard_room_boxer_2:

    nurse """
    There is something I have been meaning to raise with you, Captain.

    About your rank at the time of the Boxer Rebellion.
    """

    """
    A stillness settles over him.
    """

    captain """
    Go on.
    """

    nurse """
    I was there, as I said.

    And I can tell you with some confidence that Indian officers did not hold the rank of captain at that time.

    Not officially.

    I would have known.
    """

    """
    He does not flinch.

    But he does not answer immediately either.
    """

    captain """
    You are not wrong.

    I was never officially a captain.

    The law at the time made quite sure of that — whatever one's ability, whatever one's service, whatever one's devotion to the Crown.

    I earned that rank. I was denied it.

    So yes, I took it for myself.

    The rest of my account is true.
    """

    """
    He meets my eyes.

    There is no shame in it — or if there is, he has long since made his peace with it.
    """

    nurse """
    I see.
    """

    """
    A lie, even a comprehensible one, is still a lie.

    But I say nothing more.

    Not yet.
    """

    $ nurse_details.threads.unlock('boxer_rebellion_2')

    return


label nurse_day2_evening_billiard_room_zanzibar_confrontation:

    nurse """
    You spoke of the Anglo-Zanzibar War on Friday.

    Dangerous fighting.

    Wounds earned in the press of battle.
    """

    captain """
    What of it?
    """

    nurse """
    I have since looked it up.

    The entire engagement lasted less than an hour.

    British naval artillery. No real resistance to speak of.

    The fighting you described does not quite correspond to the historical record.
    """

    """
    He does not flinch.

    If anything, he straightens slightly.
    """

    captain """
    No, perhaps it does not.

    But I was there, Miss Marsh.

    And I was wounded.
    """

    nurse """
    Wounded.

    In an engagement that lasted forty-five minutes.
    """

    captain """
    Precisely.

    Which rather proves my point.

    The bombardment was brief, yes.

    But buildings do not care how long a battle lasts before they fall on you.

    I may well have been one of the only men on that shore to sustain a serious injury that day.

    Perhaps the only one.
    """

    """
    He is not confessing.

    He is retreating into a smaller, more defensible position — and doing it with some composure.
    """

    nurse """
    And the rank?

    The command?
    """

    captain """
    I have already spoken to you about that.

    What more is there to add?
    """

    """
    He turns back towards the fire.

    The conversation, in his estimation, is over.

    But something he said lingers.
    """

    $ nurse_day2_evening_billiard_room_zanzibar_final_menu = TimedMenu("nurse_day2_evening_billiard_room_zanzibar_final_menu", [
        TimedMenuChoice('I understand. There was no need to lie.', 'nurse_day2_evening_billiard_room_captain_end_good', 30, early_exit=True),
        TimedMenuChoice('You are a fraud. I shall tell the staff.', 'nurse_day2_evening_billiard_room_captain_end_bad', 30, early_exit=True),
    ])

    call run_menu(nurse_day2_evening_billiard_room_zanzibar_final_menu)


label nurse_day2_evening_billiard_room_captain_end_good:

    """
    He looks at me for a long moment.

    Then something gives way.
    """

    captain """
    The campaigns, yes, those were real.

    But the rank, the command, the prestige —

    fabricated, every word.
    """

    """
    He presses his hands together.
    """

    captain """
    And the battles themselves.

    I was there, you understand.

    But behind the lines.

    Always behind the lines.

    Logistics. Supply routes. Dispatches.

    I never once saw what you saw.

    Never saw what the soldiers saw.

    It is rather difficult to make a heroic story out of a supply depot.
    """

    """
    He does not look ashamed.

    Only tired.
    """

    captain """
    It was not vanity, Miss Marsh.

    Or not only vanity.

    When I came to London, no one looked at me.

    I was not a hero to them.

    I was simply something they did not recognise.

    The stories gave me a way in.

    Not because I was extraordinary.

    Simply in the hope of a better life.
    """

    """
    The fire has burned low.

    Neither of us speaks for a time.
    """

    nurse """
    I believe you.
    """

    """
    It is not forgiveness.

    But it is the truth, as far as I can give it.
    """

    $ nurse_details.threads.unlock('captain_fraud')

    return


label nurse_day2_evening_billiard_room_captain_end_bad:

    """
    Something changes in his expression.
    """

    captain """
    You would not dare.
    """

    nurse """
    Watch me.
    """

    """
    He rises from the chair.

    I do not step back.

    The room contracts around us — two people who know too much, in a house where knowing too much is dangerous.

    And then my chest seizes.
    """

    """
    The cough comes from nowhere.

    Or from everywhere.

    It comes the way it always comes when I have pushed too far — sudden, total, unstoppable.
    """

    """
    I hear the Captain's voice, urgent, panicked, close.

    I cannot make out the words.

    The lamp. The carpet. The fire.

    And then nothing.
    """

    jump nurse_ending_billiard_room_death

    return


label nurse_day2_evening_billiard_room_leave:

    """
    I have nothing more to say tonight.
    """

    captain """
    Good night, Miss Marsh.
    """

    nurse """
    Good night.
    """

    return
