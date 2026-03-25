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
            TimedMenuChoice('Leave', 'generic_cancel', 0, keep_alive=True, early_exit=True),
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
    I am not certain how I can put it into words.

    But I cannot help feeling that something here is wrong.
    """

    """
    He watches me for a moment, then nods, once.
    """

    captain """
    Very well, Miss Marsh. Say what is on your mind.
    """

    $ nurse_day2_evening_billiard_room_captain_menu = TimedMenu("nurse_day2_evening_billiard_room_captain_menu", [
        TimedMenuChoice('Something is not right about the staff{{observation}}', 'nurse_day2_evening_billiard_room_staff', 20, condition="nurse_details.threads.is_unlocked('maid_actress') and nurse_details.threads.is_unlocked('footman_actor')", linked_choice="nurse_day2_evening_billiard_room_confront_butler"),
        TimedMenuChoice('Insist we confront the butler{{intuition}}', 'nurse_day2_evening_billiard_room_confront_butler', 20, condition="is_linked_choice_hidden('nurse_day2_evening_billiard_room_captain_menu', 'nurse_day2_evening_billiard_room_confront_butler') and nurse_details.endings.is_unlocked('escape_at_night') and nurse_details.threads.is_unlocked('take_gun') and nurse_details.threads.is_unlocked('find_bullets')"),
        TimedMenuChoice('Insist we confront the butler{{intuition}}', 'nurse_day2_evening_billiard_room_confront_butler_without_bullets', 20, condition="is_linked_choice_hidden('nurse_day2_evening_billiard_room_captain_menu', 'nurse_day2_evening_billiard_room_confront_butler') and nurse_details.endings.is_unlocked('escape_at_night') and nurse_details.threads.is_unlocked('take_gun') and not nurse_details.threads.is_unlocked('find_bullets')"),
        TimedMenuChoice('I was at the Boxer Rebellion too{{observation}}', 'nurse_day2_evening_billiard_room_boxer', 20, condition="nurse_details.threads.is_unlocked('remember_doctor')", linked_choice="nurse_day2_evening_billiard_room_boxer_2"),
        TimedMenuChoice('About your rank at the Boxer Rebellion{{observation}}', 'nurse_day2_evening_billiard_room_boxer_2', 20, condition="is_linked_choice_hidden('nurse_day2_evening_billiard_room_captain_menu', 'nurse_day2_evening_billiard_room_boxer_2')", linked_choice="nurse_day2_evening_billiard_room_zanzibar_confrontation"),
        TimedMenuChoice('About the Zanzibar War{{observation}}', 'nurse_day2_evening_billiard_room_zanzibar_confrontation', 20, condition="is_linked_choice_hidden('nurse_day2_evening_billiard_room_captain_menu', 'nurse_day2_evening_billiard_room_zanzibar_confrontation') and nurse_details.threads.is_unlocked('captain_lie_zanzibar') and not nurse_details.threads.is_unlocked('captain_lie_boxer')"),
        TimedMenuChoice('Ask about Mr Manning', 'nurse_day2_evening_billiard_room_manning', 20),
        TimedMenuChoice("You don't have anything else to say to him", 'generic_cancel', 0, keep_alive=True, early_exit=True),
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
    I should be careful here. I cannot very well say I went searching their rooms.
    """

    nurse """
    The maid.

    I have seen her before. Not here.

    In London, in a play at the theatre.

    She is dressed differently of course, but I am certain that it is her.
    """

    captain """
    You think you saw a housemaid on stage.
    """

    nurse """
    I do not think it. I know it.

    And that is not all.

    The footman. I have seen him on stage as well.

    A different production, but I am quite sure of it.
    """

    captain """
    You attend a great deal of theatre, Miss Marsh.
    """

    nurse """
    I do, as it happens.

    And I know what I saw.

    Two actors, both employed as servants in the same country house.

    That cannot be a coincidence.
    """

    """
    He is quiet for a moment.

    Then, to my surprise, he does not dismiss it.
    """

    captain """
    No.

    No, I rather think it cannot.

    In London that would perhaps be possible.

    But not here.
    """

    nurse """
    Exactly.
    """

    captain """
    But to be sure, we should check if there is something strange with the only other person on staff I have seen this weekend.
    """

    nurse """
    You mean the butler.
    """

    captain """
    Precisely.

    If we could find that he too is not a career servant, that would confirm our suspicions, and we could confront Lady Claythorn about it.
    """

    nurse """
    Good idea, but how could we make him confess?
    """

    captain """
    That's a good question.

    We cannot simply march up to the man and demand an explanation.

    If there is something amiss, he is not going to confess over a polite enquiry.
    """

    nurse """
    Then perhaps we should try a less polite one.
    """

    """
    He looks at me sharply.
    """

    captain """
    That would be unwise.

    And more than a little dangerous.

    Besides, if you want a man like that to talk, you would need to properly frighten him.

    And I do not have anything that would do the trick.

    At least not here with me.

    So it's better not to think of it.
    """

    """
    He turns back to the fire, signalling the matter closed.

    But something in his voice tells me he is more unsettled than he lets on.
    """

    return

label nurse_day2_evening_billiard_room_confront_butler_intro:

    nurse """
    Captain, about the butler.
    """

    captain """
    Miss Marsh, I thought we had settled that matter.
    """

    nurse """
    If we need something to frighten him.

    I think I found it.
    """

    """
    I reach into my coat and produce the revolver.
    """

    nurse """
    I always have this with me.

    A single woman must be able to defend herself.

    If the butler is behind all this, we confront him tonight.

    Together.
    """

    """
    The Captain stares at the revolver.

    He does not reach for it.
    """

    captain """
    You cannot be serious.

    Is that thing even loaded?
    """

    return

label nurse_day2_evening_billiard_room_confront_butler_without_bullets:

    call nurse_day2_evening_billiard_room_confront_butler_intro

    nurse """
    It is not loaded, no.

    But he does not need to know that.
    """

    captain """
    Miss Marsh, that is precisely what makes this foolish.

    If you threaten a man with an empty weapon, you had better pray he believes you.

    And if he does not — if he calls your bluff — you are entirely defenceless.

    He would be within his rights to strike back, and we would have nothing to stop him.
    """

    """
    He is right, of course.

    I put the revolver away.
    """

    return

label nurse_day2_evening_billiard_room_confront_butler:

    call nurse_day2_evening_billiard_room_confront_butler_intro

    nurse """
    It is.

    And I am entirely serious.

    Two people are dead, Captain. The staff are impostors. And the butler is the one thread that ties it all together.

    You are a military man. You have fought in wars.

    Take the gun.
    """

    """
    He does not move.

    The silence stretches between us, broken only by the crackle of the fire.

    Then I see it — something I have not seen in him before.

    Not caution. Not calculation.

    Fear.
    """

    captain """
    Miss Marsh.

    I...
    """

    """
    He stops. Starts again.
    """

    captain """
    I cannot take that gun.
    """

    nurse """
    Why not?
    """

    """
    He looks at me.

    And the mask he has worn all weekend — the upright soldier, the man of experience, the captain — slips, just slightly.
    """

    captain """
    I have held a rifle on a hunt, yes.

    I have shot at birds and game.

    But I have never once pointed a weapon at another human being.

    Not in China. Not in Zanzibar. Not anywhere.
    """

    """
    The words come slowly, as though each one costs him something.
    """

    captain """
    I was never on the front lines, Miss Marsh.

    I was behind them. Always behind them.

    Logistics. Supply routes. Dispatches.

    The battles I describe — I watched some of them from a distance.

    Others I only read about in reports.
    """

    nurse """
    Then everything you told us —
    """

    captain """
    Was a story.

    A very old story, told so many times it nearly became the truth in my mind.

    But it is not the truth.
    """

    """
    He presses his hands together and stares at the fire.
    """

    captain """
    I cannot walk into that room with a loaded revolver and threaten a man.

    I would not know how.

    And I think, if it came to it, I could not pull the trigger.

    I have never had to. And that is precisely the problem.
    """

    """
    The fire crackles.

    I pick the revolver back up and slip it into my coat.
    """

    nurse """
    Thank you for telling me the truth, Captain.
    """
    $ captain_details.description_hidden.unlock('lie')
    """
    A faint, tired smile crosses his face.

    He looks older than he did a moment ago.

    Now, I would have to confront the butler myself if I want the truth.

    But don't have that strength in me.

    I was ready when I taught the captain would help.

    But now it feels to dangerous.
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

    But I never made the connection. It is not as though we were in the same circles.

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

    And with the terrible things that happened this weekend, I will concede that something is not quite right.

    I shall be on my guard from now on, and I suggest you do the same.
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
        TimedMenuChoice('Be sympathetic', 'nurse_day2_evening_billiard_room_captain_end_good', 30, early_exit=True),
        TimedMenuChoice('Accuse him of being a fraud', 'nurse_day2_evening_billiard_room_captain_end_bad', 30, early_exit=True),
    ])

    call run_menu(nurse_day2_evening_billiard_room_zanzibar_final_menu)


label nurse_day2_evening_billiard_room_captain_end_good:

    nurse """
    You know, you don't need to lie to me.

    As a nurse in the army, I understand very well your situation: the humiliation of being given orders by incompetent young men.

    Your true value never fully recognised.

    If I could have painted a brighter picture of my time in the army, I probably would have too.
    """

    """
    He looks at me for a long moment.

    Then something gives way.
    """

    captain """
    You are right. Of course you are.

    The campaigns, yes, those were real.

    But the rank, the command, the prestige —

    Fabricated, every word.
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

    It was my only way to a better life.
    """

    """
    The fire has burned low.

    Neither of us speaks for a time.
    """

    nurse """
    I understand.

    Don't worry, I won't tell the others.
    """

    captain """
    Thank you, Miss Marsh.
    """

    $ captain_details.description_hidden.unlock('lie')

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
    """

    captain angry """
    You don't understand, if the word goes out, I'll be finished.

    My standing in London reduced to nothing.

    You can't say anything.
    """

    """
    He grabs me.

    His eyes are different, like those of a madman.
    """

    nurse """
    Captain, stop!
    """

    play sound woman_cough

    """
    The cough comes from nowhere.

    It comes the way it always comes when I have pushed too far — sudden, total, unstoppable.

    I feel instantly that it is stronger than other times.

    Blood splatters on Captain Sinha, who jumps back.
    """

    captain """
    Miss Marsh!
    """

    play sound body_fall

    """
    I slip to the floor.

    I keep hearing the Captain's voice, urgent, panicked, but the voice is getting softer.

    Until I cannot make out the words.
    """

    jump nurse_ending_billiard_room_death

    return


label nurse_day2_evening_billiard_room_manning:

    nurse """
    Captain, I have been thinking about this afternoon.

    About what happened to Doctor Baldwin.
    """

    captain """
    A dreadful accident, Miss Marsh.

    Manning was drunk and careless with a firearm. 
    
    A tragic combination.
    """

    nurse """
    You sound very certain.

    Yet, this is not the only "accident" that happened this weekend.

    Could something else be at play here?
    """

    captain """
    I don't think so.

    Sadly, this type of accident is not rare at all.

    A hunt is still a dangerous business.

    And for Thomas Moody, we all saw his injuries.

    That probably meant he was very weakened.

    His death would have happened anywhere.
    """

    nurse """
    Perhaps you are right.

    Still, I confess I am uneasy knowing Samuel Manning is just upstairs.

    A few steps from my own room.

    Are we sure he cannot get out?
    """

    captain """
    Quite sure.

    I locked the door myself, with the key the butler gave me.

    The doors in this house are solid oak. He is going nowhere.
    """

    nurse """
    That is reassuring.
    """

    if nurse_details.threads.is_unlocked('master_key'):

        """
        Especially since I am now in possession of that key.
        """

    else:

        """
        And I suppose you still have that key?
        """

        captain """
        Of course.

        It is still right here with me.
        """

        """
        He reaches into his jacket pocket.

        Then stops.

        His hand comes out empty.
        """

        captain """
        Blast.

        I had it earlier, but it is in my hunting coat.

        Upstairs, in my room.

        I changed for dinner and left it in the pocket.
        """

        nurse """
        I see.
        """

        captain """
        You shouldn't worry, I still locked my room with my regular key.

        It is safe there.
        """

        nurse """
        Good.
        """


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
