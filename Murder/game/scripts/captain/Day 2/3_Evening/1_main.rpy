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
    The walk back from the western grove felt twice as long as it ought to have.

    Doctor Baldwin was a heavier man than he appeared, and the makeshift stretcher was poor work.

    But that is the sort of thought one keeps firmly to oneself.

    As we carry him through the entrance hall, I hear footsteps on the stair.

    Miss Baxter and Miss Marsh come to a halt at the bottom, and both their faces change at once.
    """

    call common_day2_evening_entrance_dialog

    $ change_room("bedroom_doctor")

    """
    Mr Harring and I carry the doctor up the stair and lay him upon his bed.

    I draw a blanket over him to the shoulders, as one would for a man asleep.

    The boy stays beside me, drained of colour.

    He has seen enough today to last him a long time.
    """

    call common_day2_evening_bedroom_doctor_dialogue

    """
    I leave him to his change of clothes and start back down the stair.

    A household cannot be permitted to drift. Someone must hold it steady, and the task, by default, falls to me.
    """

    $ change_room("entrance_hall")

    call common_day2_evening_samuel_manning_discussion_part_1

    if (captain_details.threads.is_unlocked('captain_host_suspicion_name')
        and captain_details.threads.is_unlocked('captain_host_suspicion_portrait')
        and captain_details.threads.is_unlocked('captain_host_suspicion_shooting')):

        """
        The plan is laid. Manning to his room.

        Then, I have no doubt, our hostess will urge the rest of us to scatter to our own, and we shall meet again at dinner as though nothing of consequence had occurred.

        That will not do. Not with what I know.

        A name that is no title. A portrait that is not upon the wall. A hostess who cannot shoulder her own rifle.

        And now, a second death.

        One death, beneath a capable mistress, may pass as ill fortune.

        Two deaths, beneath a mistress who is not its mistress, does not.

        If I am to press her on any of this, I must do it now, before witnesses who are still shaken enough to listen.

        But I must also have the field to myself.

        The butler is her prop. Her steadiness. His keys, his discretion, his composure at her elbow.

        If I am to challenge her, I should like him well out of the room. Upstairs, seeing to Mr Manning, would do nicely.

        Or I may simply take Manning up myself, as the house has invited me to, and let this moment pass.

        A public accusation, if it does not land, will finish me just as surely as a rifle in a wood.
        """

        $ time_left = 1
        call run_menu(
            TimedMenu("captain_day2_evening_menu_confront", [
                TimedMenuChoice("Send the butler with Manning, and challenge her", 'captain_day2_evening_confront_path', early_exit=True),
                TimedMenuChoice("Take Manning up myself, as offered", 'captain_day2_evening_normal_escort', early_exit=True),
            ])
        )

    else:

        call captain_day2_evening_normal_escort

    call common_day2_evening_samuel_manning_discussion_part_3

    $ change_room("bedroom_captain", dissolve)

    call change_time(17, 00)

    """
    I sit upon the edge of the bed with my hands pressed together.

    A good officer reviews the field after the action, not during it.

    So I let the afternoon settle in my mind, piece by piece.

    Doctor Baldwin, shot under circumstances that can be explained, but that hang uneasily all the same.

    Mr Moody, dead in his bed only this morning.

    A butler with a ready set of keys. A hostess with an unruffled composure.

    And a letter left upon my pillow last night that I have still not accounted for.
    """

    call wait_screen_transition()

    call change_time(18, 30)

    play sound dinner_gong

    """
    The gong.

    As though we were the same party that sat down last night.
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

    if captain_details.saved_variables.get('confronted_host_publicly', False):

        """
        Not a glance, not a flicker, to acknowledge the exchange of an hour past.

        She might as well have taken tea with me between whiles.

        I watch her carefully and learn nothing I did not already know.

        That, in itself, is worth noting. A woman truly disturbed by a guest's accusation would not be this still.
        """

    else:

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

    call common_day2_evening_samuel_manning_discussion_part_2

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

    call captain_day2_evening_butler_escorts_manning

    call captain_day2_evening_confront_host

    return


label captain_day2_evening_butler_escorts_manning:

    captain """
    Mr Harring needed to change, he'll join us shortly.
    """

    host """
    Ah, Captain! It's good you're here.

    We've been deliberating over what action to take concerning Samuel Manning.
    """

    captain """
    I see.

    And what is your plan?
    """

    host """
    We've decided to confine him to his chamber.

    At least until the authorities can take over.
    """

    captain """
    A prudent measure, my lady.

    Though I hope you will forgive me if I stop short of playing gaoler in a house not my own.

    The task ought to fall to a member of your household.
    """

    """
    A brief silence.

    The hostess hesitates, then turns to the butler.
    """

    host """
    Of course, Captain. How thoughtless of me to have supposed otherwise.
    """

    butler """
    I shall see to it, my lady.
    """

    """
    The butler produces his keys with practised ease and moves to Samuel Manning's side.
    """

    butler """
    If you will come with me, sir. This way.
    """

    drunk """
    Yes... yes, of course.
    """

    """
    Manning rises without protest and follows the butler towards the stair.

    The two men disappear up the steps, and the hall quiets in their wake.

    That is precisely the ground I wanted.

    With the butler out of the room, our hostess has lost her closest prop.
    """

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
