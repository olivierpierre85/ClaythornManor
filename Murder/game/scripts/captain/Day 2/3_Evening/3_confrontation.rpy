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
    We could review them all in detail, of course.

    But why not begin with the simplest of them, my lady.

    What is your title?
    """

    host """
    Well, it is Claythorn of course, the...
    """

    captain """
    That is not what I have seen. There is no 'Claythorn' title. That is meant to be your family name.

    What is your title?

    Surely you have not forgotten the title you were raised under.

    Your father would have say it aloud in your presence a hundred times.

    Letters would have come addressed to it.

    You must have heard it pronounced when you were presented at court.

    What is it?
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

    Instead, her calm composure changes to something else.

    Fear.
    """

    host """
    Very well, Captain.

    You are right.

    I believe it is time I dropped the mask.

    I am not Lady Claythorn.
    """

    captain """
    Who are you then?
    """

    host """
    An actress.

    I was hired for being here.

    I was given a script of sorts, and the run of the house, and a fee.
    """

    $ host_details.description_hidden.unlock('lie')

    nurse """
    Hired? You mean to tell us this entire weekend has been a... a performance?
    """

    host """
    Only some of it.

    But I swear to you, things have gone far beyond what was planned.

    What has happened to Mr Moody, and to Doctor Baldwin, I had no notion.

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

    Except the...
    """

    captain """
    The butler.
    """

    host """
    Yes.

    He answers to whoever is behind this directly.

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

    A man weighing, very rapidly, a number of unpleasant choices.
    """

    butler -serious """
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

    There was never any money. From what was explained to me, all of this was meant to attract you all here for the week-end.

    But I have no notion of the reasons behind it.
    """

    butler """
    Enough talking!

    Here is what is going to happen now.

    You will all go to your rooms, give me your key as I close the door behind you.

    You will have to do without supper, but I daresay it will not kill you.

    You shall be free to leave tomorrow.

    The police will come and get you.
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

    """
    He looks very sure of him, holding the gun with a firm hand.

    Whatever this man was before he was a butler, he was no stranger to a revolver.
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
    I have worn the King's uniform the better part of twenty years, and never once stood in proper combat.

    Whatever instinct a soldier is meant to acquire from being shot at, I do no have it.

    I can already see myself bleeding into the carpet if I attempt anything.
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
    He gestures with the muzzle towards the door.

    Miss Marsh rises first. Miss Baxter follows in silence.

    Lady Claythorn doesn't seem to know what to do.

    She was part of this, yet, I don't think she wills us any harm.

    The butler sense this and turns to her.
    """

    butler """
    Go warn the others.

    I will lock those up, hopefully Ted Harring is still in his room, that will make things easier.
    """

    """
    She does not protest. She has not the strength left for it.

    Whatever she is in this affair, she will not contradict him.

    I bring up the rear behind the two ladies, and feel the weight of the revolver at my back the whole length of the corridor.

    Very quickly, I am in my room.
    """

    $ change_room("bedrooms_hallway")

    butler """
    Go in captain, no need to make this more complicated that it is.
    """

    """
    I have no choice but to go in.
    """

    $ change_room("bedroom_captain", dissolve)

    play sound door_locked

    pause 0.5

    """
    The bolt slides home from the corridor side.
    """

    butler """
    Have a good night captain.

    And no need to worry, the police will come for you tomorrow, I assure you.
    """

    """
    I don't have an answer to that.

    Will the police come? I have no idea.

    I cross to the window and try the latch. Painted shut, of course. Two storeys down besides.

    For a long while I sit upon the edge of the bed and listen to the house.

    Desperate, I finally fall asleep.
    """

    call wait_screen_transition()

    call change_time(23, 10)

    """
    I do not know what wakes me.

    A scrape, perhaps. A door drawn shut along the corridor.

    Then the smell — the dry, urgent sweetness of old wood beginning to burn.

    A thin grey ribbon of smoke is already feeling its way under the door.
    """

    # play sound door_force

    """
    I throw myself at the door and find what I knew I should find. The bolt holds.

    I shoulder it twice, three times.

    The frame holds.

    Below me, somewhere, glass goes with the sound of a dropped tray.
    """

    pause 1.0

    """
    The smoke comes faster than I had thought it could.

    I sink to my knees with my coat across my mouth, and find the air no kinder there.

    Through the floorboards, very faintly, the manor begins to give voice to itself.

    A great, considered creaking, as of a vessel preparing, at last, to part with its ribs.
    """

    $ host_details.description_hidden.unlock('not_guilty')

    jump captain_ending_burned


label captain_day2_evening_butler_offer_attack:

    """
    Miss Marsh is silent. Miss Baxter looks terrorized.

    Whatever is to be done here, I must do alone.

    And I will not follow quietly a man to an unknown fate.

    Twenty years I have been an officer, but never once have I seen battle.

    A barracks officer, a parade officer.

    Other men around me went to the line.

    I never did.

    Here is my chance to see what metal I am made of.

    I lunge for his wrist.
    """

    play sound gun


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

    $ host_details.description_hidden.unlock('not_guilty')

    jump captain_ending_shot_butler
