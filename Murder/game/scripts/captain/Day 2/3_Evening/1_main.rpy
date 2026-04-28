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

        I now have a long list of things that do not sit well with our host.

        Her name that is not her title, no portrait of her in the house, her cavalier eating manners.

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
    """

    $ change_room("bedroom_doctor")

    # """
    # Mr Harring and I carry the doctor up the stair and lay him upon his bed.

    # I draw a blanket over him to the shoulders, as one would for a man asleep.

    # The boy stays beside me, drained of colour.

    # He has seen enough today to last him a long time.
    # """

    call common_day2_evening_bedroom_doctor_dialogue

    """
    I notice the blood Mr Harring has on him. Thankfully, my own jacket is untouched.

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

    After all, I represent the authority here.
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

    jump work_in_progress


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
# --------------------------------------------
label captain_day2_evening_confront_host:

    $ play_music('mysterious', 3, fadeout_val=4)

    captain """
    A moment, if you would.

    Would you be so good as to escort Mr Manning to his room and lock the door behind him?

    Use your own key. Do not let him out under any circumstance until I come for him myself.
    """

    butler """
    Of course, Captain.
    """

    """
    The butler bows, takes Manning by the elbow, and guides him up the stair without a word.

    A quarter of an hour, perhaps. Less, if he is half as careful as I take him to be.

    I shall not have a better moment than this.
    """

    captain """
    Ladies, Mr Harring.

    If I might prevail upon you to follow me into the tea room.

    There is a matter I should put to you while we are still alone in the house.
    """

    host """
    Captain, whatever can be the matter?
    """

    captain """
    Please, my lady. It will not take long.
    """

    $ change_room("tea_room", dissolve)

    """
    Miss Baxter and Miss Marsh take the small settee. Mr Harring stays standing near the window.

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
    Then let us begin with the simplest of them, my lady.

    What is your title?

    A lady cannot have forgotten the title she was raised under.

    Her father would have had it spoken in her presence a hundred times before she was ten.

    Letters would have come addressed to it. Servants would have addressed her by it.

    She would have heard it pronounced when she was presented at court.

    What is yours?
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

    Miss Marsh's hand closes upon the arm of the settee. Mr Harring has gone very still.

    Whatever air of authority she has worn this weekend leaves her by inches.
    """

    host """
    Very well, Captain.

    You are right.

    I am not Lady Claythorn.

    I do not know that there is one.

    I was hired for the part. Through a firm of solicitors in London.

    I never met the gentleman behind the arrangement.

    I was given a script of sorts, and the run of the house, and a quite extraordinary fee.

    That is the whole of what I know.
    """

    nurse """
    Hired? You mean to tell us this entire weekend has been a... a performance?
    """

    host """
    Only my part of it.

    I swear to you, what has happened to Mr Moody, and to Doctor Baldwin, I had no notion.

    None of that was in any script I was given.

    I am every bit as frightened as you are. More so, perhaps.
    """

    captain """
    Frightened of whom, madam?

    Who is here with you?
    """

    host """
    The staff. They are not staff.

    The maids, the footman, the cook. Players, all of them, hired the same way I was.

    They know less than I do, if anything at all.

    All but one.
    """

    captain """
    The butler.
    """

    host """
    Yes.

    He is not on the same arrangement as the rest of us.

    He answers to the gentleman directly.

    He gives the orders. He chooses what we are told and what we are not.

    If anyone in this house knows what is truly being done under its roof, it is he.
    """

    play sound door_knock

    """
    A measured rap upon the door of the tea room.

    Three knocks. Unhurried.

    The colour leaves Lady Claythorn's face entirely.
    """

    butler """
    My lady? Captain Sinha?

    Forgive the intrusion.

    I find myself rather curious as to why you have all withdrawn together at this hour.
    """

    """
    He has his own key, of course, and he uses it.

    He closes the door behind him with the same patient courtesy he uses to draw out a chair at dinner.

    But the courtesy is paper-thin tonight.

    His eyes go straight to the lady's face and read it in a single glance, and what he sees there does not please him.
    """

    butler """
    Madam.

    What have you told them?
    """

    host """
    Everything, I am afraid.

    Or what little I know of it.
    """

    """
    He receives this in silence.

    A man weighing, very rapidly, a number of unpleasant arithmetics.
    """

    butler """
    Then we have a difficulty.

    Captain, I shall not insult any of us with theatre.

    I am not the master of this house. I am no more the butler here than the lady is its mistress.

    My arrangement, however, is not the same as hers.

    I have rather more to lose than a pleasant fee, you understand.
    """

    captain """
    Then who do you answer to?

    And what is being done in this house?
    """

    butler """
    To the first, I do not know his name. Only his bank.

    To the second, I was not told. I was told only what to do, and what to prevent.

    The road is blocked because I had it blocked. The telephone is mute for the same reason.

    No one is coming tonight, Captain. That much I can tell you.
    """

    $ play_music('danger', 2, fadein_val=1)

    """
    He says it without relish, as a man recites a debt he cannot settle.

    His hand has not strayed from his side, but it has not quite settled either. The fingers move once, twice, against the line of his coat.

    Around me the others have gone perfectly still. Miss Baxter's hands are folded white. Miss Marsh sits forward, her chin set.

    Mr Harring's eyes have not left the butler since he stepped through the door.

    Whatever the man came in here ready to do, he has not yet decided to do it. There is still a course to be set.
    """

    $ time_left = 1
    call run_menu(
        TimedMenu("captain_day2_evening_menu_butler_offer", [
            TimedMenuChoice("Propose confining the staff until the police arrive", 'captain_day2_evening_butler_offer_confine', early_exit=True),
            TimedMenuChoice("Lunge at him before he can decide", 'captain_day2_evening_butler_offer_attack', early_exit=True),
        ])
    )


label captain_day2_evening_butler_offer_confine:

    captain """
    Then let us be practical, all of us.

    You have a great deal to lose, by your own admission, and I have no wish to see anyone lose anything further tonight.

    Here is my proposal.

    The staff, all of them, you and the lady included, will retire to their rooms and remain there until morning.

    The keys come to me.

    My fellow guests and I shall sit out the night together in this room.

    When the police arrive, as they will, the matter passes from your hands and from mine.

    You give me no cause for violence. I give you none.
    """

    """
    The butler is silent for a long moment.

    His hand drops at last from the line of his coat. His shoulders, which I had not noticed were set so high, lower a fraction.

    Whatever was about to happen here was not, I think, what he wished to happen.

    He inclines his head with something close to relief.
    """

    butler """
    A sensible compromise, Captain.

    The keys are yours.

    I shall instruct the staff myself, and present them to you in the entrance hall in five minutes.
    """

    """
    He withdraws as quietly as he came.

    Lady Claythorn lets out a breath she has plainly been holding for the last quarter of an hour, and presses her hand to her mouth.
    """

    psychic """
    Captain, that was... bravely done.
    """

    nurse """
    And cleverly, too.
    """

    captain """
    Let us not congratulate ourselves until morning.

    Until then, we sit here together. No one wanders. No one drinks anything that has not been opened in front of all of us.

    Are we agreed?
    """

    """
    A nod from each of them.

    A long night ahead, but a survivable one.

    That, at least, is what I tell myself as the butler's footsteps recede along the corridor.
    """

    pause 1.0

    """
    The hours pass slowly.

    Tea is brought in, which we ourselves pour. Sandwiches arrive on a tray, which Mr Harring inspects and Miss Marsh portions out.

    The clock on the mantelpiece marks each quarter with a small, polite chime.

    By two o'clock my eyes are heavy. The fire has burnt low. Miss Baxter sits beside me with her hands folded in her lap, perfectly composed.
    """

    pause 1.0

    """
    A weariness comes over me of a sort I have not felt in many years. Not the honest fatigue of a long day, but something heavier, and oddly sweet at the back of the tongue.

    I lift my head to speak, and find I have already half forgotten what I meant to say.

    The room recedes by a careful degree.

    Miss Baxter's voice is very gentle, though I cannot any longer make out the words.
    """

    jump captain_ending_poisoned


label captain_day2_evening_butler_offer_attack:

    """
    The man is uncertain. The lady is undone. They will not be in this state again tonight.

    If I am to act, I must act now.
    """

    """
    I draw the knife from my belt and close the distance in two strides.
    """

    pause 0.5

    play sound gun

    pause 1.0

    """
    He does not flinch. His hand is already inside his coat as I move, and what comes out of it is not what I had expected to find on a butler.

    A small revolver, dark and businesslike. The hand that holds it trembles once, and then is still.

    A flat, ugly sound in the small room.

    Something very hot opens beneath my ribs.

    The knife is no longer in my hand. I am no longer, properly, on my feet.
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
