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
# --------------------------------------------
label host_day2_evening:

    call change_time(15, 00, 'Evening', 'Saturday', hide_minutes=True, chapter='saturday_evening')

    $ host_details.add_checkpoint("host_day2_evening")

    call black_screen_transition("Lady Claythorn", chapters_names[current_chapter])

    $ change_room('entrance_hall')

    $ play_music('sad', 2)

    """
    After the long walk home, we finally reach the manor.

    I am a wreck, and I am still not sure what to do now.
    """

    call common_day2_evening_entrance_dialog

    """
    The Captain takes charge of it all.

    Mr Harring helps him carry the doctor up the stair.

    I remain below with Miss Baxter and Miss Marsh, and I keep my hands folded.
    """

    call common_day2_evening_samuel_manning_discussion_part_1

    call common_day2_evening_samuel_manning_discussion_part_2

    # NEXT =>
    # On a major mistake and you are out (going downstairs is ok)
    if not host_details.threads.is_unlocked('stayed_with_guests') or not host_details.threads.is_unlocked('addressed_manning_first') or host_details.threads.is_unlocked('terrible_shot'):

        call host_day2_evening_captain_accusation

    else:

        call common_day2_evening_samuel_manning_discussion_part_3

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


label host_day2_evening_telephone:

    """
    The telephone stands on its table at the back of the hall, beneath the stair, and I go to it with the butler at my heel.

    He speaks low, to make sure that nobody can overhear us.
    """

    butler """
    The telephone will not work.

    It was disconnected a long time ago.
    """

    host """
    What?

    But how did you call the police this morning, then?
    """

    butler """
    I did not.

    I was hoping we could wait until tomorrow to warn them, at the end of the weekend.

    I could not risk jeopardising all that we have accomplished so far.
    """

    host """
    No, that is unacceptable!

    Two lives have been lost now.

    We have to tell everyone, right now!
    """

    butler """
    No, we will not do that.

    First, do not speak to me as though you are in charge.

    You are playing the Lady, but I am the one giving the orders.

    And you had better do as I say for now.
    """

    host """
    Are you threatening me?
    """

    butler """
    I am just warning you, that is all.

    And please keep your voice down.

    We need to pretend a little while longer.

    I will explain everything later tonight, I promise.
    """

    """
    I consider this for a moment.

    I am too shaken to think further.

    Waiting until tonight seems the wisest choice.
    """

    host """
    Fine, but you will need to explain everything to me then.
    """

    butler """
    All right.

    I will tell you everything.

    You will only have to act for a little while longer.

    Starting with a 'telephone call' to the police, now.
    """

    host """
    And what should I say?
    """

    butler """
    Pretend that they will come tomorrow.

    By then our job will be done.
    """

    host """
    Well, I do not like it, but fine.
    """

    """
    So I summon the last of my strength to make a false call to the police, just in case somebody is eavesdropping.

    It is not my greatest performance, but it should be enough to convince everyone.

    When my act is done, I set the receiver back and return to the others.
    """

    return

# --------------------------------------------
#   CAPTAIN SINHA PRESSES HER
# --------------------------------------------
label host_day2_evening_captain_accusation:

    # THIS should be a common? Or try it differently?
    call captain_day2_evening_confront_host

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
