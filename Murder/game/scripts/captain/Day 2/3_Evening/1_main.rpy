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
                TimedMenuChoice("Send the butler with Manning, and challenge her", 'captain_day2_evening_confront_path', early_exit=True),
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
label captain_day2_evening_confront_path:

    call captain_day2_evening_confront_host

    return


label captain_day2_evening_confront_host:

    $ play_music('mysterious', 3, fadeout_val=4)

    """
    Miss Baxter and Miss Marsh linger uncertainly near the foot of the stair.

    Lady Claythorn draws breath to speak, no doubt to send us all to our rooms until the gong.

    I move before she can.
    """

    captain """
    Forgive me, Lady Claythorn. I am afraid I cannot, in good conscience, retire to my room as though this were merely a weekend grown tiresome.
    """

    host """
    Captain?
    """

    captain """
    Two men dead within the space of a day, beneath the same roof.

    Mr Moody in the small hours. Doctor Baldwin in the woods this afternoon.

    And now you mean to send us upstairs, to wait upon our dinner in quiet reflection.

    That, my lady, is not the conduct of a house in mourning. That is the conduct of a house carrying on a performance.
    """

    host """
    Captain, I ask only that we preserve what order we may.

    The police cannot reach us before morning. Running about in alarm will not bring back either man.
    """

    captain """
    Order has its place, my lady. And grief has another.

    You have shown us no sign of the second.
    """

    """
    The hall stills.

    Miss Marsh has turned her head. Miss Baxter watches me with an expression I cannot read at all.
    """

    psychic surprised """
    Captain... surely you cannot mean to suggest our hostess is in some way answerable for what has happened?
    """

    captain """
    I mean, Miss Baxter, that we ought not accept this evening at its face value.

    For there is a great deal about our hostess that does not sit well with me.
    """

    """
    Her smile holds, as a hostess's smile will hold through a guest's poor taste.

    But the set of her shoulders has shifted.
    """

    captain """
    Your portrait, my lady, is nowhere in the gallery upstairs.

    In a house as old as this, where every Claythorn since Cromwell hangs upon the wall, the present mistress is absent.

    And on the hunt this afternoon, you could scarcely shoulder a rifle. A gentlewoman who arranges a shooting weekend on her own grounds ought to know her piece.

    And most particular of all, your surname is not a title, as it ought to be. There is no such style as 'Lady Claythorn.'

    Any one of these, taken alone, would perhaps pass for nothing.

    Taken together, they paint a picture I cannot unsee.
    """

    host """
    Captain, you overreach yourself.

    Each of those trifles has a perfectly ordinary explanation.

    You will forgive me if, after the day we have had, I am not minded to deliver them in detail.
    """

    captain """
    Then deliver me this one, my lady, and I shall press you no further tonight.

    What is your title?
    """

    """
    A silence.

    It is the silence of a woman who was not expecting the question put quite so plainly.

    Her eye flicks towards the stair, as though to measure how long the butler has been gone.
    """

    host """
    Captain, I find your tone intolerable.

    I shall not be interrogated in my own hall.
    """

    nurse """
    Captain Sinha... perhaps this is not the hour for such a discussion.

    We are all of us shaken.
    """

    """
    Miss Marsh speaks gently, but there is something close to a warning in her eye.

    I realise at once that I have spent my ammunition.

    To press further now, before witnesses too tired and too frightened to weigh the matter, would serve only to make me appear unhinged.

    I let a beat pass, and incline my head.
    """

    captain """
    Of course, Miss Marsh. Forgive me.

    I have said what I felt I must.

    I shall say no more of it tonight.
    """

    """
    But I have said it, and before two witnesses. That cannot be taken back.

    Lady Claythorn recovers her smile.
    """

    host """
    No harm done, Captain. These are trying hours for us all.

    I trust we shall meet at dinner on better terms.
    """

    """
    A gracious answer, and perfectly delivered.

    At that moment, I hear the butler's tread upon the stair.

    He returns to the hall in the manner of a man who has heard what he was not meant to hear.

    Her eye meets his for the briefest of moments.

    A look passes between them. Brief. Unambiguous.

    Whatever I have planted in this hall tonight, I have been marked for it.
    """

    $ captain_details.saved_variables['confronted_host_publicly'] = True

    $ stop_music(2)

    return
