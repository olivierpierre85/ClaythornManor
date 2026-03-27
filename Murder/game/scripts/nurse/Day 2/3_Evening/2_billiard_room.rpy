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

    There are a few things about this weekend that don't make sense to me.
    """

    captain """
    Oh?

    Such as?
    """

    $ nurse_day2_evening_billiard_room_captain_menu = TimedMenu(
        "nurse_day2_evening_billiard_room_captain_menu", [

        TimedMenuChoice(
            'Talk about the deaths of Thomas Moody and Daniel Baldwin',
            'nurse_day2_evening_billiard_room_manning', 10),

        TimedMenuChoice(
            "Reveal the staff other occupations{{observation}}",
            'nurse_day2_evening_billiard_room_staff', 10,
            condition="nurse_details.threads.is_unlocked('maid_actress') and nurse_details.threads.is_unlocked('footman_actor')",
            linked_choice="nurse_day2_evening_billiard_room_confront"),

        TimedMenuChoice(
            'Tell him you were at the Boxer Rebellion too{{observation}}',
            'nurse_day2_evening_billiard_room_boxer', 10,
            condition="nurse_details.threads.is_unlocked('remember_doctor')"),

        TimedMenuChoice(
            'Confront him about the "inconsistencies" in his stories{{observation}}',
            'nurse_day2_evening_billiard_room_war_stories', 10,
            condition="nurse_details.threads.is_unlocked('captain_lie_zanzibar') and nurse_details.threads.is_unlocked('remember_doctor')"),

        TimedMenuChoice(
            'Show him the loaded gun you found{{observation}} ',
            'nurse_day2_evening_billiard_room_confront', 10,
            condition="is_linked_choice_hidden('nurse_day2_evening_billiard_room_captain_menu', 'nurse_day2_evening_billiard_room_confront') and nurse_details.saved_variables['captain_boxer_discussed'] and nurse_details.threads.is_unlocked('take_gun') and nurse_details.threads.is_unlocked('find_bullets')",
            early_exit=True),

        TimedMenuChoice(
            "You don't have anything else to say to him",
            'generic_cancel', 0,
            keep_alive=True, early_exit=True),
    ])

    call run_menu(nurse_day2_evening_billiard_room_captain_menu)

    return


label nurse_day2_evening_billiard_room_suspicions:

    if nurse_details.saved_variables["captain_boxer_discussed"] and nurse_details.saved_variables["captain_staff_discussed"]:

        nurse """
        Two actors employed as servants. Three of us at the same war. 

        There are too many things wrong in this house, Captain.
        """

        """
        He pauses and ponders for a second.
        """

        captain """
        I am inclined to agree.

        Something is happening here.

        There is a great chance that this weekend is not what it appears to be.
        """

        nurse """
        That's what I believe too.
        """
        
        captain """
        But how to be sure?
        
        There is still a chance that all of this is a coincidence.

        I don't want to put Lady Claythorn in an awkward position if she has done nothing wrong.

        That would be improper.
        """

        """
        He won't mention it, but he is certainly not just worried about making a scandal.

        He is thinking about the reward as well.

        Antagonising Lady Claythorn could make her renounce giving the prize.

        That's a powerful incentive to keep people in line.

        But I cannot just do nothing.
        """

        nurse """
        There is someone else we can interrogate.
        
        The only other person on staff I have seen this weekend.
        """

        captain """
        You mean the butler?
        """

        nurse """
        Precisely.
        """

        captain """
        That's not a bad idea.

        If we could find that he too is not a career servant, that would confirm our suspicions, and we could confront Lady Claythorn about it.

        But we cannot simply march up to the man and demand an explanation.

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

        Besides, if you want to make a man talk, you would need to properly frighten him.

        And I do not have anything that would do the trick.

        At least not here with me.

        So it's better not to think of it.
        """

        nurse """
        What would you need?
        """

        captain """
        Well, I don't like talking about those things with a lady.

        But if you must know, a gun can get a confession from almost any man.

        I mean at least if it is loaded, that way you can show that you are serious about the matter.

        I have seen battle-hardened soldiers lose all confidence when a gun is shot close to them.

        But I don't have one with me here, so I don't think I can do anything.

        I am afraid we must just be on our guard tonight, and leave as soon as possible in the morning.

        Yes, now that I think of it, that's the only sensible thing to do.
        """

        """
        He turns back to his book, for him the conversation is over.

        I don't like this but I won't convince him with words only.
        """

    else:

        nurse """
        Exactly.

        That is proof that something is very wrong here.
        """

        captain """
        I wouldn't say proof, not yet.

        You will need more than that to convince me.
        """

    return

# First suspicious stuff
label nurse_day2_evening_billiard_room_staff:

    nurse """
    I believe that something strange is going on with the staff.
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

    In London, at the theatre, playing a role.

    I can't quite remember the name of the play, but I am certain that it is her.
    """

    captain """
    You think you saw a housemaid on stage.
    """

    nurse """
    I do not think it. I know it.

    And that is not all.

    The footman. I have seen him in a play as well.

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
    It is indeed hard to believe.

    In London that would perhaps be possible.

    But here, very unlikely.
    """

    $ nurse_details.saved_variables["captain_staff_discussed"] = True

    call nurse_day2_evening_billiard_room_suspicions

    return

# Second suspicious stuff
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
    """

    $ nurse_details.saved_variables["captain_boxer_discussed"] = True

    return


label nurse_day2_evening_billiard_room_war_stories:

    nurse """
    Captain, I have heard you talk a great deal about your campaigns.

    And there are details that trouble me.
    """

    captain """
    Really, which details?
    """

    nurse """
    Well first, I can tell you with some confidence that Indian officers did not hold the rank of captain at the time of the Boxer Rebellion.

    Not then. And it still must be very rare today.
    """

    """
    A stillness settles over him.
    """

    captain """
    You are not wrong.

    I was not officially a captain.

    I was a Subedar. The highest rank allowed for a non-white officer.

    The law at the time made quite sure that — no matter one's ability — a coloured man could never give orders to a white man.

    But explaining all that in polite company is tedious, and tends to sour the mood, which is why I omitted it.

    But the rest of my account is true.
    """

    nurse """
    Is it?

    Because I have also looked into the Anglo-Zanzibar War.

    The entire engagement lasted less than an hour. British naval artillery. No real resistance to speak of.

    The fighting you described does not quite correspond to the historical record.
    """

    """
    He does not flinch.

    If anything, he straightens slightly.
    """

    captain """
    I was there, Miss Marsh.

    And I was wounded.
    """

    nurse """
    Wounded.

    In an engagement that lasted forty-five minutes.

    With only one man lightly injured on the British side.
    """

    """
    He is quiet for a moment.

    Then he sets down his glass.
    """

    captain """
    Well my injuries were maybe so minor that they weren't reported.

    War is a messy business, not everything that happened can be recorded in history books.

    And the war was very short of course.

    I might have embellished its retelling.

    But it is just that I like to tell good stories.

    Every good storyteller does it, Miss Marsh.
    """

    """
    He smiles.

    It is true that he could just have exaggerated some facts, but I am not entirely convinced.
    """

    $ captain_details.description_hidden.unlock('embellishment')

    return


label nurse_day2_evening_billiard_room_confront:

    """
    I reach into my coat and produce the revolver.

    Captain Sinha looks at me astonished.
    """

    captain """
    Miss Marsh, how on earth do you have this with you?
    """


    nurse """
    I've learned at war that it's better to always be prepared.

    I never leave my house without it since.
    """

    """
    I hope this lie is convincing enough.
    """

    """
    It is loaded.

    Two people are dead, Captain. The staff are impostors. Three of us were at the very same war twenty-four years ago.

    Something is very wrong in this house.

    You are a military man.
    
    Take the gun, and let's confront the butler.
    """

    """
    I hold it out to him.

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

    I slip the revolver back into my coat.
    """

    $ captain_details.description_hidden.unlock('lie')

    nurse """
    Then you are a fraud.

    Every word. Every story. Every medal you claim to have earned.

    All of it, a lie.
    """

    captain """
    Miss Marsh, please —
    """

    nurse """
    And when we leave this house, I shall make sure the others know exactly what sort of man they have been dining with.
    """

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
    You don't understand. If the word goes out, I'll be finished.

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
    We've witnessed two deaths in as many days.

    Doesn't it seem strange to you?
    """

    captain """
    Not really.

    They seem pretty natural to me, Miss Marsh.

    Thomas Moody died of injuries he got during the war.

    Even if you thought he was fine, he might have been suffering in silence.

    Some people prefer to hide their distress from the people around them.
    """

    """
    Well, I can't really argue against that.
    """

    nurse """
    But for Doctor Baldwin?
    """

    captain """
    A dreadful accident, Miss Marsh.

    Manning was drunk and careless with a firearm.

    Sadly, this type of accident is not rare at all.

    A hunt is still a dangerous business.
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
