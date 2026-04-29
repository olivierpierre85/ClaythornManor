# --------------------------------------------
#   Captain
#
#   Saturday - Evening
#
#   15:00 -> 23:00
#
#   Music: sad
#
#   Position
#       - House: captain, lad, psychic, nurse, host, butler
#       - Dead : broken, doctor
#       - Confined : drunk (locked in his room)
#
#   Notes:
#       - Captain carries Doctor Baldwin upstairs with the lad
#       - Branches on all three host suspicions:
#           - unlocked -> choice to manoeuvre the butler out and
#             confront the hostess before everyone retires
#           - otherwise -> captain escorts Manning himself and
#             pockets the butler's master key
# --------------------------------------------

label captain_day2_evening:

    $ captain_details.add_checkpoint("captain_day2_evening")

    call change_time(15, 00, 'Evening', 'Saturday', chapter='saturday_evening')

    call black_screen_transition("Sushil Sinha", chapters_names[current_chapter])

    $ change_room('entrance_hall', irisout)

    $ play_music('sad', 2)

    """
    The walk back from the woods felt twice as long as it ought to have.

    Doctor Baldwin was a heavier man than he appeared, and the makeshift stretcher was poor work.
    """

    if (captain_details.threads.is_unlocked('captain_host_suspicion_name')
        and captain_details.threads.is_unlocked('captain_host_suspicion_portrait')
        and captain_details.threads.is_unlocked('captain_host_suspicion_shooting')):

        """
        Throughout the walk, something keeps nagging at me.

        I already had a long list of things that do not sit well with our host.

        And I have just witnessed that she is no great hunter either.

        And now, a second death.

        One death may pass as a terrible accident.

        Two deaths are more concerning.

        Especially with everything I know about her.

        But as I reach the house, I am still not sure what to do.
        """

    """
    As we carry him through the entrance hall, I hear footsteps on the stair.

    Miss Baxter and Miss Marsh come to a halt at the bottom, and both their faces change at once.

    What follows is much as one might expect.

    Miss Baxter, on the brink of tears, demands to know what has happened.

    She wastes no kindness upon Mr Manning.

    Lady Claythorn calls the police, then tells us the road out is blocked by a fallen tree, and the constabulary will not reach the manor before tomorrow.

    It appears there is not much to do but wait. In the meantime, I propose moving Doctor Baldwin to his room.

    Mr Harring volunteers his help without being asked.

    so we carry the doctor up the stair and lay him upon his bed.
    """

    $ change_room("bedroom_doctor")

    """
    I draw a blanket over him to the shoulders, as one would for a man asleep.

    The boy stays beside me, drained of colour.

    He has seen enough today to last him a long time.
    """

    call common_day2_evening_bedroom_doctor_dialogue

    """
    I point at the blood Mr Harring has on him. Thankfully, my own jacket is untouched.

    He withdraws to his room to change, and I return to the others.
    """

    $ change_room("entrance_hall")

    """
    As I come down the stairs, everyone turns to me.

    It is clear they are hoping I might give them some kind of direction.
    """

    call common_day2_evening_samuel_manning_discussion_part_2

    """
    I believe everyone assumes I should take him myself.

    After all, I represent the closest thing to a form of authority here.
    """

    if (captain_details.threads.is_unlocked('captain_host_suspicion_name')
        and captain_details.threads.is_unlocked('captain_host_suspicion_portrait')
        and captain_details.threads.is_unlocked('captain_host_suspicion_shooting')):

        """
        But instead, I take a careful look at our host.

        I have enough arguments to confront her in front of everybody.

        And it would be better to do so without the staff present.

        Right now, only the butler is with us.

        If I were to send him to lock Manning up, that would be the perfect moment to confront our hostess.

        But a public accusation, if it does not land, will put me in an incredibly awkward position.

        I need to be sure about this.
        """

        $ time_left = 1
        call run_menu(
            TimedMenu("captain_day2_evening_menu_confront", [
                TimedMenuChoice("Send the butler with Manning, and challenge her", 'captain_day2_evening_confront_host', early_exit=True),
                TimedMenuChoice("Take Manning up myself", 'captain_day2_evening_normal_escort', early_exit=True),
            ])
        )

    else:

        """
        And I have no reason to disappoint them.
        """

        call captain_day2_evening_normal_escort

    call common_day2_evening_samuel_manning_discussion_part_4

    $ change_room("bedroom_captain", dissolve)

    call change_time(17, 00)

    """
    I sit upon the edge of the bed with my hands pressed together and let the afternoon settle in my mind, piece by piece.

    Doctor Baldwin, shot under circumstances that can be explained, but that hang uneasily all the same.

    Mr Moody, dead in his bed only this morning.

    A suspicious hostess and a letter left upon my pillow last night.

    So many things to make sense of.

    I ponder for a while on what my next move should be, but cannot decide on a course.
    """

    call wait_screen_transition()

    call change_time(18, 30)

    play sound dinner_gong

    """
    The gong still rings.

    At least the order of the house is not disturbed.
    """

    $ change_room("dining_room", irisout)

    $ play_music('sad', 3)

    """
    Three chairs sit empty.

    Doctor Baldwin. Mr Moody. Mr Manning.

    I take my usual place. Miss Baxter settles on my right, quieter than I have yet seen her.

    Miss Marsh has been moved nearer to the head of the table, at our hostess's invitation.

    Mr Harring slips in a moment later, hair damp, a fresh shirt at his collar.

    Lady Claythorn rises to speak.
    """

    call common_day2_evening_dinner_host

    """
    A measured address. If she is troubled by what has happened beneath her roof today, nothing of it shows.

    A man less suspicious than I am would take her at her word and think no further of it.

    As it is, I take note of her composure, and say nothing of it aloud.
    """

    """
    The food is served shortly after, but most of us merely push it about our plates.

    Miss Marsh, in her new place at the hostess's elbow, picks at her meal without raising her eyes.

    Mr Harring keeps his head bent over his plate and answers nothing that is not put directly to him.

    Miss Baxter has scarcely touched a thing.

    She has not said a dozen words since we sat down.
    """

    $ time_left = 1
    call run_menu(TimedMenu("captain_day2_evening_menu_dinner", [
        TimedMenuChoice("Speak to Miss Baxter", 'captain_day2_dinner_psychic', early_exit=True),
        TimedMenuChoice("Say nothing, eat in silence", 'captain_day2_dinner_silence', early_exit=True),
    ], image_right = "psychic"))

    call change_time(21, 00)

    """
    The dinner draws to a close in much the same hush in which it began.

    The butler sees the plates cleared with the same patient courtesy he has shown all weekend.

    Lady Claythorn rises and bids us each a measured good-night.

    Before she withdraws, she reminds us that drinks are laid out in the billiard room, as they were yesterday.

    A curious thing after the day we have had.

    The other guests rise from the table without ceremony.

    I linger over the last of my wine and turn the invitation over in my head.

    The billiard room is no place a careful man would go tonight.

    Two of our number lie dead, a third sits locked above stairs, and someone under this roof has had a hand in the arrangement of all of it.

    A glass passed across a green baize table is no harder to spoil than one laid down at dinner.

    And yet.

    A man who fears poison in the house does not stand quietly amongst the bottles.

    A woman who fears for her life does not call upon her hostess for a brandy.

    Whoever takes the invitation tonight will, by that very act, be telling me something.

    Either they have nothing to fear, or they wish very much to be seen as having nothing to fear.

    In either case, that is information I do not now possess.

    And there is precious little I can sift from these walls if I retire and lock my door against them.

    Very well.

    The billiard room can wait a little while. There are corners of this house I have so far had no proper reason to visit — and tonight, with the butler's key in my pocket, I find I have every reason.
    """

    $ play_music('mysterious', 2)

    $ time_left = 120

    call run_menu(captain_details.saved_variables["day2_evening_map_menu"])

    call change_time(23, 00)

    $ stop_music()

    $ change_room("bedroom_captain", dissolve)

    """
    I close the door of my room behind me and turn the key in the lock.

    Whatever I have learnt tonight, I shall need a clear head to make any use of it in the morning.
    """

    jump work_in_progress


# ------------------------------------
#   DINNER SCENES
# ------------------------------------
label captain_day2_dinner_psychic:

    captain """
    Miss Baxter.

    Forgive me, but I find I cannot eat in silence whilst you sit beside me untouched.
    """

    psychic """
    You are very kind, Captain.

    But I am poor company this evening. I do not believe a plate of food will mend that.
    """

    captain """
    None of us is much use tonight.

    Doctor Baldwin was a good man.

    He met an end he had done nothing to deserve.
    """

    psychic """
    He was the one soul under this roof who spoke to me as though I had a mind worth answering.

    I shall not soon find another like him.
    """

    """
    She presses a handkerchief to her cheek and turns her face a fraction from mine.

    Whatever else she may be, her grief is the only honest thing I have seen at this table tonight.
    """

    captain """
    Tomorrow the police will be here, and we shall all of us be away from this place by the afternoon.

    Until then, if there is any service I can render you, you have only to ask.
    """

    psychic """
    That is most generous of you, Captain.

    For now, I should like only to be left to my own thoughts for a little while.
    """

    captain """
    Of course.
    """

    """
    I turn back to my plate and let her be.

    There is a kindness in not pressing a woman who has just lost the one ally she had under this roof.
    """

    return


label captain_day2_dinner_silence:

    """
    I cannot think of any comfort I might offer Miss Baxter.

    So I keep my counsel and attend to my plate.
    """

    return


# --------------------------------------------
#   Normal path - Captain escorts Manning
#   himself and pockets the butler's key
# --------------------------------------------
label captain_day2_evening_normal_escort:

    call common_day2_evening_samuel_manning_discussion_part_3

    $ change_room("bedrooms_hallway", dissolve)

    """
    Manning walks ahead of me without speaking.

    The drink is still on him, though quieter now. He moves like a man in a dream he does not care to interrupt.

    I see him into his room and draw the door closed behind him.

    The key turns in the lock with a heavy, deliberate click.
    """

    play sound door_locked

    pause 0.5

    """
    For good measure, I try the handle twice. It holds.

    He will trouble no one for the remainder of the evening.

    I weigh the key in my palm.

    It would be the natural thing to return it to the butler at once.

    And yet... I should prefer it stayed where it is.

    Tonight, under this roof, a key is not a small thing.

    I slip it quietly into my waistcoat pocket.
    """

    $ captain_details.threads.unlock('butler_key')

    $ change_room("entrance_hall", dissolve)

    """
    When I come back down, the others have remained much as I left them.

    Lady Claythorn looks towards me with the faintly anxious composure of a hostess whose weekend has slipped beyond repair.
    """

    return


# --------------------------------------------
#   Confrontation path - Captain deflects the
#   Manning task onto the butler, then presses
#   the hostess before the remaining witnesses
# Doctor, Broken => Dead
# Drunk with butler
# Lad in his room
# that leaves : Captain, psychic, nurse, host
# --------------------------------------------
label captain_day2_evening_confront_host:

    $ play_music('mysterious', 3, fadeout_val=4)

    """
    I turn to the butler.
    """

    captain """
    A moment, if you would.

    Would you be so good as to escort Mr Manning to his room and lock the door behind him?

    See to it that he is not allowed out under any circumstance.
    """

    """
    He gives a brief glance at Lady Claythorn, who nods her assent.
    """

    butler """
    Of course, Captain.
    """

    """
    The butler takes Manning by the elbow, and guides him up the stair without a word.

    That should give me a little time, but probably no more than a quarter of an hour.

    I should not waste any of it.
    """

    captain """
    Ladies, I know it is rather unusual, but I would like all of you to follow me into the tea room.

    There is a matter I should put before everyone.
    """

    host """
    Captain, whatever can be the matter?
    """

    captain """
    Please, my lady. It will not take long.
    """

    $ change_room("tea_room", dissolve)

    """
    Miss Baxter and Miss Marsh take the small settee.

    Lady Claythorn lowers herself into the wingback chair as though it were a witness box.

    I close the door behind us and place myself between it and our hostess.
    """

    captain """
    Forgive the abruptness. I have my reasons for the haste.

    Throughout this weekend I have noticed a great many things that do not sit comfortably with the role our hostess claims to hold.

    Her portrait is nowhere in the gallery.

    She either does not know, or does not follow, the proper manners at table.

    The hunt she herself arranged appears to be quite beyond her skill.

    And, worst of all, the surname she is using is not her title, as it ought to be.

    I do not believe she is Lady Claythorn.

    In truth, I do not believe there is a Lady Claythorn at all.
    """

    psychic surprised """
    Captain! What an extraordinary thing to say.
    """

    nurse """
    Surely there is some misunderstanding.
    """

    """
    Their voices come on her behalf. Their eyes do not.

    They have noticed things too. I see that now.
    """

    host """
    Captain, you have plainly taken the events of today rather harder than the rest of us.

    Each of those small oddities has a perfectly ordinary explanation.

    I would gladly walk you through them, if I thought it would settle your nerves.
    """

    captain """
    We could review them all in detail, but why not begin with the simplest of them, my lady.

    What is your title?

    A lady cannot have forgotten the title she was raised under.

    Her father would have had it spoken in her presence a hundred times before she was ten.

    Letters would have come addressed to it. Servants would have addressed her by it.

    She would have heard it pronounced when she was presented at court.

    What is yours?
    """

    host """
    Well, it is Claythorn of course, the...
    """

    captain """
    That is not what I have seen. There is no 'Claythorn' title. That is meant to be your family name.

    What is your title?
    """

    """
    She opens her mouth.

    She closes it again. Her eyes go to her hands, then to the door, then back to me.

    The room takes the silence and settles into it.
    """

    psychic """
    Lady Claythorn?
    """

    """
    There is no answer.

    Whatever air of authority she has worn this weekend leaves her by inches.
    """

    host """
    Very well, Captain.

    You are right.

    I am not Lady Claythorn.

    I do not know that there is one.
    """

    captain """
    Who are you then?
    """

    """
    An actress.
    
    I was hired for the part.

    I was given a script of sorts, and the run of the house, and a quite extraordinary fee.

    That is the whole of what I know.
    """

    nurse """
    Hired? You mean to tell us this entire weekend has been a... a performance?
    """

    host """
    Only some of it.

    I swear to you, what has happened to Mr Moody, and to Doctor Baldwin, I had no notion.

    None of that was in any script I was given.

    I am every bit as frightened as you are. More so, perhaps.
    """

    captain """
    Frightened of whom, madam?
    """

    host """
    I don't know, I don't understand most of what is happening here.

    The staff. They are not staff.

    They were hired the same way I was.

    I think they know less than I do, if anything at all.

    Except for...
    """

    captain """
    The butler.
    """

    host """
    Yes.

    He answers to the gentleman directly.

    He gives the orders. He chooses what we are told and what we are not.

    If anyone in this house knows what is truly being done under its roof, it is he.
    """

    play sound door_knock

    $ play_music('danger', 2)

    """
    A measured rap upon the door of the tea room.

    Three knocks. Unhurried.

    The colour leaves Lady Claythorn's face entirely.
    """

    butler """
    My lady? Captain Sinha?

    Forgive the intrusion.

    I find myself rather curious as to why you have all withdrawn together in here.
    """

    """
    He closes the door behind him with patient courtesy.

    His eyes go straight to Lady Claythorn's face and read it in a single glance.
    """

    butler """
    Madam.

    What is happening here?
    """

    captain """
    She told us everything, I am afraid.

    About her role in the events of this weekend.

    And about yours.
    """

    """
    He receives this in silence.

    A man weighing, very rapidly, a number of unpleasant arithmetics.
    """

    butler """
    Then we have a difficulty.

    Captain, I shall not insult any of us with theatre.

    I am no more the butler here than the lady is its mistress.
    """

    captain """
    Then to whom do you answer?

    And what is being done in this house?
    """

    butler """
    I am afraid I know no more of it than whatever Lady Claythorn might have told you.
    """

    host """
    You are lying! You have been in charge here the whole time!
    """

    butler """
    That does not mean I know more than you.

    Only that I have more to do.
    """

    captain """
    Do what?

    What were you meant to do to us?

    I think it is clear, now, that we are not here to receive any prize.

    What then?

    To make a play of us all?

    To hurt us?

    To kill us, as you killed Mr Moody and Doctor Baldwin?
    """

    butler """
    No, of course not. Nobody was supposed to get hurt!

    It was supposed to be just a— just a—
    """

    captain """
    Just what?
    """

    butler """
    I cannot say more than that.

    There is no reason for you to know.

    But I give you my word, you have nothing to fear.

    Nothing bad is going to happen.

    All you have to do is retire to your rooms and wait for the police tomorrow.

    Then you will be able to forget all about this weekend.
    """

    nurse """
    And the prize money?
    """

    butler """
    I am afraid that was another lie. I am sorry.
    """

    nurse """
    Lady Claythorn, or whatever your name truly is, is he telling the truth?
    """

    host """
    He is.

    There was never any money. From what was explained to me, all of this was meant to be a very elaborate prank.

    But I have no notion of the reasons behind it.
    """

    butler """
    Neither have I.

    Now, enough talk. You are all going to stay in your rooms.

    You will have to do without supper, but I daresay it will not kill you.

    You shall be free to leave tomorrow.
    """

    captain """
    You really expect us to follow your orders?
    """

    butler """
    I believe you will, if you value your life, Captain.
    """

    """
    He swiftly produces a revolver and points it directly at me.

    I came armed myself. But the pistol is in the pocket of my other jacket, in my bedroom.

    At present, I am defenceless.
    """

    nurse """
    But you swore you would not hurt us.
    """

    butler """
    I will not, unless I am forced to.

    This is for my own protection, I assure you.
    """

    $ time_left = 1
    call run_menu(
        TimedMenu("captain_day2_evening_menu_butler_offer", [
            TimedMenuChoice("Accepts being confined", 'captain_day2_evening_butler_offer_confine', early_exit=True),
            TimedMenuChoice("Lunge at him and grab the gun", 'captain_day2_evening_butler_offer_attack', early_exit=True),
        ])
    )


label captain_day2_evening_butler_offer_confine:

    """
    A revolver is a poor argument, but an argument all the same.

    The butler holds it as a man holds a tool he has held a great many times before.

    The wrist is locked. The trigger finger lies flat along the guard, in the manner the regulars are taught.

    Whatever this man was before he was a butler, he carried a piece in earnest. A footpad, perhaps, or worse. There is a quietness to him that I have seen, once or twice, in men who came up through a rougher apprenticeship than the army.

    There is no profit in three of us bleeding into the carpet for the sake of a point well made.
    """

    captain """
    Very well.

    Lower the weapon, sir, if you please.

    We shall do as you ask.
    """

    butler """
    A wise decision, Captain.

    No further trouble. Only quiet, until morning.
    """

    """
    He gestures with the muzzle, as polite as a steward directing his guests in to dinner, towards the door.

    Lady Claythorn rises unsteadily. Miss Marsh offers her an arm. Miss Baxter follows in silence.

    I bring up the rear, and feel the weight of the revolver at my back the whole length of the corridor.
    """

    $ change_room("bedroom_captain", dissolve)

    play sound door_locked

    pause 0.5

    """
    The bolt slides home from the corridor side.

    A small, deliberate sound, which says rather more than the butler did in any of his speeches downstairs.
    """

    pause 1.0

    """
    I cross to the window and try the latch. Painted shut, of course. Three storeys down besides.

    For a long while I sit upon the edge of the bed and listen to the house.

    The footsteps along the corridor cease, one room at a time.

    Somewhere, very faintly, a clock strikes two.
    """

    pause 1.0

    """
    I do not know what wakes me.

    A scrape, perhaps. A door drawn shut along the corridor.

    Then the smell — the dry, urgent sweetness of old wood beginning to char.

    A thin grey ribbon of smoke is already feeling its way under the door.
    """

    pause 1.0

    """
    I throw myself at the door and find what I knew I should find. The bolt holds.

    I shoulder it twice, three times. The frame answers each blow with a politeness it did not extend to the butler's key.

    Below me, somewhere, glass goes with the sound of a dropped tray.
    """

    pause 1.0

    """
    The smoke comes faster than I had thought it could.

    I sink to my knees with my coat across my mouth, and find the air no kinder there.

    Through the floorboards, very faintly, the manor begins to give voice to itself.

    A great, considered creaking, as of a vessel preparing, at last, to part with its ribs.
    """

    jump captain_ending_burned


label captain_day2_evening_butler_offer_attack:

    """
    The wrist is locked. The trigger finger lies flat along the guard.

    Whatever this man was before he was a butler, he was no stranger to a revolver.

    The nurse is silent. Miss Baxter sits as though carved from her chair.

    Whatever is to be done here, I must do alone. 
    
    And I will not stand quietly while a man marches my to an unknown fate.
    """

    # TODO add here a reflection on it might be the first he is in combat situation,  a redemption of sorts

    """
    I lunge for his wrist.
    """

    pause 0.5

    play sound gun

    pause 1.0

    """
    He fires before I have closed the half of the distance.

    A flat, ugly sound, very loud in the small room.

    Something very hot opens beneath my ribs, and the floor comes up to meet me with surprising patience.

    The shot is placed too well to be the work of any servant. The man has done this before, and often.

    I had read it in him a moment ago, and chosen to act all the same.
    """

    butler """
    Forgive me, Captain.

    You left me no choice.
    """

    """
    He sounds, of all things, sincere.

    The room narrows to a single point of grey.
    """

    jump captain_ending_shot_butler
