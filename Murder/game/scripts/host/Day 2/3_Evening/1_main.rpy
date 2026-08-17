# --------------------------------------------
#   Host
#
#   Saturday - Evening
#
#   15:00 -> 23:00
#
#   Music: sad for the return, mysterious for the butler, danger for the night
#
#   Position
#       - House    : host, captain, lad, psychic, nurse, butler
#       - Confined : drunk, locked in his room
#       - Dead     : broken (Thomas Moody), doctor (Daniel Baldwin)
#
#   Notes :
#       - SKELETON. The chapter plays from end to end, but the scenes are only
#         sketched. Every '# TODO' marks writing still to be done.
#       - Shared beats live in _common/Day 2/3_Evening/1_main.rpy:
#           - common_day2_evening_entrance_dialog
#           - common_day2_evening_samuel_manning_discussion_part_1 to part_4
#           - common_day2_evening_dinner_host
#       - Captain Sinha only presses her if she has been careless. Her slips are
#         counted the same way as in host_day1_evening_debrief, and the library
#         book ('family_history') is what lets her answer him.
#       - Three ways out of the evening (see docs/next_tasks.md) :
#           - she leaves with the butler    -> the car in the woods (TODO ending)
#           - she retires alone             -> her throat cut in bed (TODO ending)
#           - she confides in the Captain   -> Sunday
# --------------------------------------------
label host_day2_evening:

    call change_time(15, 00, 'Evening', 'Saturday', hide_minutes=True, chapter='saturday_evening')

    $ host_details.add_checkpoint("host_day2_evening")

    call black_screen_transition("Lady Claythorn", chapters_names[current_chapter])

    $ change_room('manor_garden', irisout)

    $ play_music('sad', 2)

    # TODO expand : the walk up the drive behind the stretcher, and what she is
    # rehearsing to say to the two women waiting in the house.
    """
    We come up the drive in a slow procession, and nobody speaks for the whole length of it.

    I have spent the walk trying to decide what a lady does with her hands at a time like this.

    That is what I am reduced to.
    """

    $ change_room('entrance_hall')

    call common_day2_evening_entrance_dialog

    # TODO expand : the doctor carried up the stair, and her waiting below with
    # the two women while it is done.
    """
    The Captain takes charge of it all, and I am grateful to be given nothing to do.

    Mr Harring helps him carry the doctor up the stair.

    I remain below with Miss Baxter and Miss Marsh, and I keep my hands folded.
    """

    call common_day2_evening_samuel_manning_discussion_part_1

    call common_day2_evening_samuel_manning_discussion_part_2

    # ------------------------------------
    #   HER SLIPS, COUNTED
    #   The same counter as the Friday debrief. He needs the rabbit, which he
    #   watched her miss this morning, and at least one older doubt to set
    #   beside it. Give him the rabbit and he has nothing to open with.
    # ------------------------------------
    python:
        host_day2_evening_slip_count = 0

        if host_details.threads.is_unlocked('go_downstairs'):
            host_day2_evening_slip_count += 1

        if not host_details.threads.is_unlocked('addressed_manning_first'):
            host_day2_evening_slip_count += 1

        if not host_details.threads.is_unlocked('stayed_with_guests'):
            host_day2_evening_slip_count += 1

        host_day2_evening_pressed = (
            host_details.threads.is_unlocked('terrible_shot')
            and host_day2_evening_slip_count >= 1
        )

    if host_day2_evening_pressed:

        call host_day2_evening_captain_accusation

    else:

        call common_day2_evening_samuel_manning_discussion_part_3

        # TODO expand : Manning led up the stair, and her relief at not being
        # asked to decide anything at all.
        """
        Mr Manning rises and follows the Captain without a word of protest.

        Nobody asks me what I think should be done, and I am glad of it.
        """

    call common_day2_evening_samuel_manning_discussion_part_4

    call change_time(16, 00)

    call host_day2_evening_butler_recap

    # ------------------------------------
    #   DINNER
    #   TODO : the manners no longer matter to her, and that ought to show.
    #   Miss Marsh has been moved up to her elbow, so there is room for a menu
    #   here if the scene needs one.
    # ------------------------------------
    call change_time(18, 30)

    play sound dinner_gong

    """
    The gong sounds, exactly as it did last night.

    Somebody below stairs is still keeping to the order of the house, and I find that I could weep for them.
    """

    $ change_room('dining_room', irisout)

    $ play_music('sad', 3)

    # TODO expand : three empty chairs, Miss Marsh moved up beside her, and the
    # speech she has to give without a written word of it from the butler.
    """
    Three chairs stand empty.

    I take my place at the head of a table I have no right to sit at, and I rise to speak.
    """

    call common_day2_evening_dinner_host

    """
    They listen, and they thank me, and not one of them believes a word of it.

    Nor do I.
    """

    call change_time(21, 00)

    $ change_room('bedroom_host', dissolve)

    call host_day2_evening_butler_departure

    # ------------------------------------
    #   THE NIGHT
    #   TODO : replace with a proper map menu in 0_map_choices.rpy, built on the
    #   model of host_day1_evening_map_menu. The billiard room and retiring for
    #   the night are the two exits that matter.
    # ------------------------------------
    $ play_music('mysterious', 2)

    $ time_left = 60

    call run_menu(
        TimedMenu("host_day2_evening_menu_night", [
            TimedMenuChoice('Go down to the billiard room', 'host_day2_evening_billiard_room', 60, room='billiard_room'),
            TimedMenuChoice('Retire for the night', 'generic_cancel', early_exit=True, room='bedroom_host'),
        ])
    )

    call change_time(23, 00)

    $ stop_music()

    $ change_room('bedroom_host', dissolve)

    if host_details.threads.is_unlocked('trust_captain'):

        # TODO expand : she is not alone with it any more, and that is the only
        # reason she sleeps at all.
        """
        I lock my door and lie down in the dark.

        Somebody else in this house now knows what I am, and knows it from my own mouth.

        It ought to frighten me more than it does.
        """

        # TODO jump host_day3_morning once Sunday is written
        jump work_in_progress

    call host_day2_evening_alone_at_night


# --------------------------------------------
#   CAPTAIN SINHA PRESSES HER
#
#   Mirrors captain_day2_evening_confront_host, seen from her chair. He sends
#   the butler up with Manning so that he may put it to her without the staff
#   in the room.
#
#   TODO : move to 2_captain_accusation.rpy once the scene is written in full.
# --------------------------------------------
label host_day2_evening_captain_accusation:

    $ play_music('mysterious', 3, fadeout_val=4)

    # TODO expand : he asks the butler to take Manning up, and she understands,
    # a moment too late, exactly why he has done it.
    """
    The Captain turns to the butler and asks him, very civilly, to see Mr Manning to his room.

    The butler looks to me, and I nod, because a hostess would.

    Only when the two of them are on the stair do I understand what I have just agreed to.
    """

    # TODO expand : the tea room, the door closed, Miss Baxter and Miss Marsh
    # on the settee, and the list he has been keeping all weekend.
    $ change_room('tea_room', dissolve)

    captain """
    Forgive the abruptness, my lady.

    There is no portrait of you in the gallery.

    You do not keep the manners of this table.

    And this morning I watched you fire at a sitting rabbit at twenty paces.

    So I shall ask you a very simple thing, and I hope you will forgive me for asking it.

    What is your title?
    """

    """
    The room settles into the question and waits.
    """

    # TODO : the second choice is the interesting one. Decide what it costs her.
    $ time_left = 1
    call run_menu(
        TimedMenu("host_day2_evening_menu_accusation", [
            TimedMenuChoice("Give him the title from the library book", 'host_day2_evening_accusation_answer', early_exit=True, condition = "host_details.threads.is_unlocked('family_history')"),
            TimedMenuChoice("Take offence and refuse the question", 'host_day2_evening_accusation_refuse', early_exit=True),
        ])
    )

    return


# --------------------------------------------
#   She read the book, so she has the answer
# --------------------------------------------
label host_day2_evening_accusation_answer:

    # TODO expand : the title said plainly, as though it had never been in
    # doubt, and his apology, which is worse to sit through than the question.
    """
    I give him the name and the title exactly as the book had them, and I do not hurry over either.

    He apologises for a full minute, and I have to bear every second of it.

    Then he says nothing further, all evening.
    """

    return


# --------------------------------------------
#   She cannot answer, and has to brazen it out
#
#   TODO : this is the open question. Either the butler comes back down and
#   takes the room in hand, or she is left half undone in front of the two
#   women and must carry it into Sunday. Decide before writing the prose.
# --------------------------------------------
label host_day2_evening_accusation_refuse:

    """
    I draw myself up and tell him that I will not be questioned in my own house on the day two men have died in it.

    It is a good exit line, and I have delivered better ones to larger rooms.

    But Miss Marsh does not look away from me, and she does not look convinced.
    """

    return


# --------------------------------------------
#   THE BUTLER'S RECAP
#
#   The Friday debrief, without the manners. He wants only to know whether she
#   will hold. If she found the bottle in the scullery, she can put it to him.
#
#   TODO : move to 3_butler_recap.rpy once written in full.
# --------------------------------------------
label host_day2_evening_butler_recap:

    $ change_room('bedroom_host', dissolve)

    $ play_music('mysterious', 2)

    play sound door_knock

    """
    He knocks, as he did last night, and comes in before I have finished telling him to.
    """

    # TODO expand : no notes tonight, no speech for tomorrow. Only him asking,
    # in his flat way, whether she intends to keep going.
    butler """
    Two of them in one day.

    I know how it looks.

    But I need you at that table tonight, and I need you steady.
    """

    if host_details.threads.is_unlocked('found_poison'):

        # TODO expand : the bottle standing open on the scullery shelf, and the
        # fact that she has told nobody she was ever down there.
        """
        The bottle in the scullery is in my mouth before I have decided whether to let it out.

        If I say it, he will know I went below stairs, and he will know I have been counting.
        """

        $ time_left = 1
        call run_menu(
            TimedMenu("host_day2_evening_menu_poison", [
                TimedMenuChoice("Put the rat poison to him", 'host_day2_evening_accuse_butler', early_exit=True),
                TimedMenuChoice("Say nothing about the scullery", 'generic_cancel', early_exit=True),
            ])
        )

    return


# --------------------------------------------
#   She accuses him over the bottle
#
#   TODO : next_tasks.md has her threatening to tell the others, and him
#   killing her for it. That would be a mid-story ending and needs writing.
#   For now she only frightens him, and herself.
# --------------------------------------------
label host_day2_evening_accuse_butler:

    """
    I tell him what I saw on the scullery shelf, and I tell him what I think of it.

    For the first time since I met him, he has no answer ready.
    """

    $ host_details.threads.unlock('accused_butler')

    return


# --------------------------------------------
#   AFTER DINNER - THE MASTERMIND SENDS WORD
#
#   He has had a message. The weekend is over, and he means to drive her out
#   tonight. Going with him is the car in the woods, as in Broken's timeline.
#
#   TODO : move to 4_departure.rpy once written in full.
# --------------------------------------------
label host_day2_evening_butler_departure:

    $ play_music('mysterious', 2)

    play sound door_knock

    # TODO expand : the message, and how little he will say about who sent it.
    butler """
    I have had word.

    Matters are not going as they were meant to, so there is no reason for either of us to remain.

    Our part is done.

    The car is in the garage.

    I can have us on the road within the hour, and you need never hear of this house again.
    """

    """
    An hour ago I would have taken his arm and run for it.

    And that is precisely what troubles me now.
    """

    $ time_left = 1
    call run_menu(
        TimedMenu("host_day2_evening_menu_departure", [
            TimedMenuChoice("Go with him tonight", 'host_day2_evening_leave_with_butler', early_exit=True),
            TimedMenuChoice("Refuse, and stay in the house", 'generic_cancel', early_exit=True),
        ])
    )

    # TODO expand : her refusal, and the look he gives her before he withdraws.
    """
    I tell him I shall not leave this house tonight, and he does not argue with me.

    That, more than anything he has said, is what frightens me.
    """

    return


# --------------------------------------------
#   She takes the car
#
#   TODO ending : the wreck in the woods, as Thomas Moody sees it from the
#   other side of the story. Needs a host ending label and an entry in
#   host_config.rpy -> endings.
# --------------------------------------------
label host_day2_evening_leave_with_butler:

    $ play_music('danger', 2)

    """
    I take what will fit into one bag, and I do not look back at the room.

    The car is waiting with its lamps already lit.
    """

    # TODO expand : the drive, the trees, and the bend he takes far too fast.
    """
    We are perhaps two miles into the woods when he puts his hand out and tells me, quite gently, to hold on.
    """

    # TODO jump host_ending_car_woods once the ending is written
    jump work_in_progress


# --------------------------------------------
#   THE BILLIARD ROOM - CAPTAIN SINHA
#
#   TODO : the whole scene. She goes down meaning to sit with whoever is still
#   awake, and finds the Captain alone. Telling him the truth is the only way
#   out of the night, and it carries into Sunday.
#   next_tasks.md also floats finding him already dead, throat cut. Decide.
# --------------------------------------------
label host_day2_evening_billiard_room:

    $ change_room('billiard_room')

    # TODO expand : the room, the decanters untouched, and the Captain sitting
    # up alone with no drink in front of him at all.
    """
    The Captain is alone in the billiard room, sitting where he can see the door.

    There is a glass at his elbow that he has not touched.
    """

    # TODO expand : the confession. She tells him what she is, and why she
    # cannot be alone in this house tonight.
    host """
    Captain.

    I am going to tell you something, and I would ask you to hear all of it before you say anything at all.
    """

    $ host_details.threads.unlock('trust_captain')

    return


# --------------------------------------------
#   SHE GOES UP ALONE
#
#   TODO ending : her throat cut in her own bed, as the Captain's is in his.
#   Needs a host ending label and an entry in host_config.rpy -> endings.
# --------------------------------------------
label host_day2_evening_alone_at_night:

    $ play_music('danger_short')

    """
    I lock my door, and I put a chair beneath the handle, and I lie down in my clothes.

    Neither of those things will matter in the least, but they let me close my eyes.
    """

    call wait_screen_transition()

    # TODO expand : the weight on the edge of the bed, and how little time she
    # is given to understand it.
    """
    I wake because there is somebody sitting on the edge of my bed.

    He does not hurry, and he is not unkind about it.
    """

    # TODO jump host_ending_throat_cut once the ending is written
    jump work_in_progress
