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

    # One major mistake and you are out (going downstairs is ok)
    if not host_details.threads.is_unlocked('stayed_with_guests') or not host_details.threads.is_unlocked('addressed_manning_first') or host_details.threads.is_unlocked('terrible_shot'):

        call host_day2_evening_captain_accusation

    else:

        call common_day2_evening_samuel_manning_discussion_part_3

        """
        Mr Manning rises and follows the Captain without a word of protest.
        """

        call common_day2_evening_samuel_manning_discussion_part_4

    call change_time(16, 00)


    $ change_room('bedroom_host', dissolve)

    $ play_music('mysterious', 2)

    play sound door_knock

    """
    He knocks and enters without bothering to wait for my answer.
    """

    butler """
    I know.

    I know how it looks.

    But I promise this is not as bad as it looks.
    """

    host anger """
    Not as bad as it looks?

    Two deaths now.

    And we have no means of calling the authorities.

    So they will wait in their rooms until God knows when.
    """

    butler """
    Until tomorrow, that is all.

    Our work is coming to an end now.

    All you need to do now is make it through dinner.
    """

    host """
    Right, and I suppose you still won't tell me the full story of why we are here?
    """

    butler """
    It is better you do not know.

    All you have to say is on this piece of paper, which you can read at dinner.

    That will be your final task for this weekend.
    """

    """
    I want to ask more questions, but part of me prevents me from doing so.

    If there really is something sinister that was planned, maybe it is better I do not know in advance.

    I really do not like that train of thought.

    I realise I am no longer guided by logic, but by fear.
    """

    host """
    All right, dinner then.
    """

    butler """
    Great.

    Be strong, it is almost the end.
    """

    """
    He exits abruptly and leaves me with my thoughts.

    There is nothing for me to do but get ready.
    """

    # ------------------------------------
    #   DINNER
    # ------------------------------------
    call change_time(18, 30)

    play sound dinner_gong

    """
    The gong sounds downstairs.

    Time for dinner.

    Hopefully this will be the final act of it all.
    """

    $ change_room('dining_room', irisout)

    $ play_music('sad', 3)

    """
    Three chairs stand empty.

    Doctor Baldwin. Mr Moody. Mr Manning.

    Miss Marsh is left stranded at the far end of the table with nobody in front of her and nobody at her side.
    """

    call common_day2_evening_dinner_marsh_seated

    """
    She gathers her things and comes up to me.

    I take my place at the head of it, then I rise to speak.
    """

    call common_day2_evening_dinner_host

    """
    They listen, and then fall silent.

    I have no idea whether they believe me.

    It hardly matters at this point.
    """

    """
    The plates come in.

    Miss Marsh turns to me before I have my napkin across my lap.
    """

    call common_day2_evening_dinner_host_marsh

    """
    The butler comes round with the dishes.

    He serves from the left, he holds the platter at exactly the height he ought, and he does not hurry.

    I cannot take my eyes off his hands.
    """

    if host_details.threads.is_unlocked('found_poison'):

        """
        The bottle in the scullery, standing open on the shelf.

        I pushed the thought away this morning, and it has come back to sit at my table.

        I find myself watching which plate goes to which guest, as though I should be able to tell by looking.

        Miss Marsh. Miss Baxter. Mr Harring. The Captain.

        And Mr Manning's tray, gone up the back stairs to a locked door.

        When my own plate is set in front of me I do not touch it.

        I move the food about a little, the way one does, and I wonder whether I am the only person at this table who is not eating.
        """

    else:

        """
        I eat very little.
        """

    if host_details.threads.is_unlocked('bested_captain'):

        """
        Captain Sinha does not look at me once for the whole of the meal.

        No doubt he is filled with remorse and shame after he accused me.

        He must be in as much of a hurry as I am to see the end of this weekend.
        """

    call change_time(21, 00)

    """
    The plates go out, so I say the last line on the butler's paper.

    It is about drinks laid out in the billiard room, and I hear how it sounds in that room.

    Nobody answers me.

    Chairs go back, and they leave for their rooms.

    I doubt a lot of them will come back down tonight.
    """

    # Next =>
    call change_time(21, 15)

    $ change_room('bedroom_host', dissolve)

    $ play_music('mysterious', 2)

    play sound door_knock

    butler """
    Well done for dinner.

    Now, I have just received word from our 'patron'.

    They say that things are not going as they were meant to, so they are cancelling the whole thing.

    There is no reason for either of us to remain here any longer.
    """

    host """
    You received word? How?

    How could they know what is happening?

    I thought the telephone was dead.

    Were you able to repair it?
    """

    butler """
    Never mind how, it does not matter.

    All you need to know is that our part is done.

    The car is in the garden.

    I will gather the rest of the staff, and we can leave as soon as we are ready.

    You will get your money when we reach the town.
    """

    """
    Leaving this place, finally.

    Yet, I am unsure about it.

    Leaving like robbers in the middle of the night.

    That is not how I pictured this weekend ending.
    """

    host """
    I do not know.

    Maybe it is better to wait for the morning.

    At least so we can see the road properly.

    I am not sure that leaving now is the best idea.
    """

    butler """
    Do what you want.

    If you prefer to stay here with the rest, that is your business.

    But I will leave with the others, no matter what.

    If you are not in the car by eleven, we will leave without you.
    """

    """
    He leaves without giving me more explanation.

    I am now filled with questions.

    The most pressing one is how he could have received news from the person who organised this weekend.

    Until now I thought they were still in London.

    But now I learn they are not.

    Are they hidden somewhere in this place? Or hiding in the woods?

    I do not have a good answer to that, and I probably will not have one staying here.

    I should get out of this room.
    """

    # ------------------------------------
    #   THE NIGHT
    #
    #   Ninety minutes, and two doors decide how it ends (see 0_map_choices.rpy) :
    #     - the garden, where the car is waiting, which is the ending in the woods
    #     - the billiard room, where the Captain sits up, which is the only ally
    #       she can still make
    #   The Captain is only in that room if she did not humiliate him in the tea
    #   room, so 'bested_captain' closes her happy ending for good.
    # ------------------------------------
    call change_time(21, 30)

    $ play_music('mysterious', 2)

    """
    An hour and a half, and then a car goes down that drive with me in it or without me.
    """

    $ time_left = 90

    call run_menu(host_details.saved_variables["day2_evening_map_menu"])

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
#   SHE PUTS THE SCULLERY BOTTLE TO HIM
#
#   Needs 'found_poison'. He does not deny it and he does not explain it, which
#   is what makes the car in the garage look rather different.
# --------------------------------------------
label host_day2_evening_accuse_butler:

    host """
    Before I answer you, there is something I should like to ask.

    On Friday night you told me I had no business below stairs.

    While I was down there I saw a bottle of rat poison in the scullery, standing open on the shelf and half gone.

    This house was shut up until the day before we arrived, and it will be shut up again at the end of the weekend.

    So who has been poisoning rats here, and when?
    """

    """
    He does not answer at once, and that is answer enough for me.

    A man with nothing to hide says 'what bottle' before you have finished the question.
    """

    butler """
    There are rats in a house this old, my lady.

    There is poison in every scullery in Scotland.
    """

    host """
    That is not what I asked you.
    """

    butler """
    No.

    It is not.
    """

    """
    He looks at me for a long moment, and I watch him decide how much I am worth.
    """

    butler """
    I would not think about that bottle any more tonight, if I were you.

    Nobody at that table has come to any harm, and nobody is going to.

    The car is standing in the garden, and my offer stands until it does not.
    """

    """
    Nobody at that table.

    He chose those four words with a great deal of care, and there is a man locked in a room upstairs who was not at that table.

    His tray went up the back stairs while I was watching the plates.
    """

    $ host_details.threads.unlock('accused_butler')

    return


# --------------------------------------------
#   She takes the car
#
#   TODO ending : the wreck in the woods, as Thomas Moody sees it from the
#   other side of the story. Needs a host ending label and an entry in
#   host_config.rpy -> endings.
# --------------------------------------------
label host_day2_evening_leave_with_butler:

    $ change_room("manor_garden")

    """
    I take what will fit into one bag, and I do not look back at the room.

    The car is waiting on the gravel with its lamps already lit and nobody in it at all.

    I am the first, which I had not expected.

    I get into the back and I put the bag on my knees and I sit there in the dark.
    """

    call change_time(23, 00)

    """
    They come out to me one at a time over the next hour, and none of them says a word to me.

    The girl from the kitchen, with her carpet bag. The footman. Then the rest of them.

    Not one of them is surprised to find me sitting there, and that is the part I keep turning over.

    They were told I would be coming, and they were told before I had decided.

    The last door of the house shuts at eleven exactly, and he takes his seat and lets the brake off.
    """

    $ stop_music()

    $ play_music('danger_short')

    play sound car_driving

    # TODO expand : the drive, the trees, and the bend he takes far too fast.
    """
    We are perhaps two miles into the woods when he puts his hand out and tells me, quite gently, to hold on.
    """

    # TODO jump host_ending_car_woods once the ending is written
    jump work_in_progress


# --------------------------------------------
#   THE BILLIARD ROOM - CAPTAIN SINHA
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
