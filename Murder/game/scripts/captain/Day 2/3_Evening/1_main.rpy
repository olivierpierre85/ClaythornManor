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

    $ change_room("manor_garden")

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

    $ change_room('entrance_hall', irisout)

    """
    As we carry him through the entrance hall, I hear footsteps on the stair.

    Miss Baxter and Miss Marsh come to a halt at the bottom, and both their faces change at once.

    What follows is much as one might expect.

    Miss Baxter, on the brink of tears, demands to know what has happened.

    She wastes no kindness upon Mr Manning.

    Lady Claythorn calls the police, then tells us the road out is blocked by a fallen tree, and the constabulary will not reach the manor before tomorrow.

    It appears there is not much to do but wait. In the meantime, I propose moving Doctor Baldwin to his room.

    Mr Harring volunteers his help without being asked.

    So we carry the doctor up the stair and lay him upon his bed.
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
        TimedMenuChoice("Say nothing, eat in silence", 'generic_cancel', early_exit=True),
    ], image_right = "psychic"))

    call change_time(21, 00)

    """
    The dinner draws to a close in much the same hush in which it began.

    The butler sees the plates cleared with the same patient courtesy he has shown all weekend.

    Lady Claythorn rises and bids us each a measured good-night.

    Before she withdraws, she reminds us that drinks are laid out in the billiard room, as they were yesterday.

    A curious thing after the day we have had.

    The other guests rise from the table without ceremony, so I follow them upstairs.
    """

    $ change_room("bedroom_captain")

    """
    I turn the invitation for drinks over in my head.

    The billiard room is no place a careful man would go tonight.

    Two of us lie now dead, a third sits locked above stairs, and someone under this roof has had a hand in the arrangement of all of it.

    And yet.

    Whoever takes the invitation tonight will, by that very act, be telling me something.

    Either they have nothing to fear, or they wish very much to be seen as having nothing to fear.

    In either case, seeing who will be there might teach me something of value.

    And there is precious little I can learn if I keep to my room.
    """

    $ play_music('mysterious', 2)

    $ time_left = 120

    call run_menu(captain_details.saved_variables["day2_evening_map_menu"])

    call change_time(23, 00)

    $ stop_music()

    """
    I feel it's time to turn back to my room.
    """

    $ change_room("bedroom_captain", dissolve)

    """
    I close the door of my room behind me and turn the key in the lock.

    It probably will not be easy, but I should try to sleep.
    """

    if captain_details.threads.is_unlocked('confide_in_lad'):

        """
        I undress without lighting the lamp and lie down upon the bed.

        Sleep, when it comes, comes more readily than I should have thought.

        A soldier's habit, perhaps. One learns to take rest where it is offered.
        """

        call wait_screen_transition()

        call change_time(2, 30)

        """
        I do not know what wakes me.

        A breath of air, perhaps. A board easing under a careful foot.

        The room is utterly black, and yet I know, with the certainty of a man who has slept in too many rough places, that I am not alone in it.
        """

        """
        A weight settles on the edge of the bed.

        I open my mouth to speak and a hand closes over it before any sound can leave me.

        The grip is firm. Practised.

        I struggle, but the arm that holds me is younger than mine, and braced for it.
        """

        pause 0.5

        """
        There is a brief, cold pressure at my throat.

        No more than that.

        Then a great quietness, and the room seems to fall away from me by degrees.
        """

        jump captain_ending_throat_cut


    jump captain_day3_morning


# ------------------------------------
#   DINNER SCENES
# ------------------------------------
label captain_day2_dinner_psychic:

    captain """
    Miss Baxter.

    How are you holding up after today's events?
    """

    psychic """
    As well as one can, Captain, thank you for asking.

    But such a tragic event must have shaken everyone to their core.
    """

    captain """
    Of course, everyone must be processing this terrible loss.

    But for myself, I have seen enough of death to know it is a natural part of life.

    From dust to dust, from ashes to ashes, as they say.
    """

    psychic """
    Of course.
    """

    """
    She turns away from me.

    It was perhaps a touch heartless, but at least it helps me maintain my image.
    """
    
    return


# --------------------------------------------
#   Normal path - Captain escorts Manning
#   himself and pockets the butler's key
# --------------------------------------------
label captain_day2_evening_normal_escort:

    captain """
    Mister Manning, are you ready to go to your room?
    """

    drunk """
    Well - yes, of course.
    """

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
