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

    I am wondering how he could have received news from the person who organised this weekend.

    Until now I thought they were still in London.

    But what if they are not.

    Are they hidden somewhere in this place? Or hiding in the woods?

    I do not have a good answer to that, and I probably will not find one staying here.

    I should get out of this room.
    """

    call change_time(21, 30)

    $ play_music('mysterious', 2)

    $ time_left = 90

    call run_menu(host_details.saved_variables["day2_evening_map_menu"])

    call change_time(23, 00)

    $ stop_music()

    $ change_room('bedroom_host', dissolve)

    if host_details.threads.is_unlocked('trust_captain'):

        $ change_room("bedroom_host", fadein)

        """
        We both go to my room.

        If anyone were to see us, it would look a little scandalous, but I am beyond caring about that tonight.

        As agreed, the Captain takes a chair, and I lie down fully clothed on the bed.

        It takes a while, but in the end I feel myself growing tired.
        """

        jump host_day3_morning

    else :

        """
        I did not leave with the car.

        For whatever reason, I prefer to spend the night here.

        I lock my door, and I put a chair beneath the handle, and I lie down in my clothes.

        I was not expecting to fall asleep, but the events of the day have taken their toll, and I close my eyes.
        """

        jump host_ending_die_in_sleep


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
#   She takes the car
#
#   Ends with the wreck in the woods, the same car Thomas Moody and Captain
#   Sinha find on the Sunday afternoon of the other storylines. There is
#   nothing wrong with the engine - the butler invents the fault to put her in
#   the driver's seat, so that she is found in front and the other two behind.
# --------------------------------------------
label host_day2_evening_leave_with_butler:

    $ change_room("manor_garden")

    """
    I take what will fit into one bag, and I do not look back at the room.

    The car is waiting on the gravel with its lamps already lit and nobody in it at all.

    I am the first, which I had not expected.

    I get into the back and I put the bag on my knees and I sit there in the dark.
    """

    call wait_screen_transition()

    call change_time(23, 00)

    """
    They come out to me one at a time over the next hour, and none of them says a word to me.

    The girl from the kitchen, with her carpet bag. The footman. Then the butler takes his place in the driver's seat.
    """

    butler """
    Good, you are all here.

    No need to wait any longer then.

    They must be all in their room by now, they won't hear us leaving.
    """

    """
    I wonder why this is important, but I do not ask him.

    He has a serious face that says we should leave him alone.

    So the ride starts in complete silence.
    """

    play sound car_driving

    $ change_room('forest_road', dissolve)

    """
    We go down the drive and out through the gates, and the manor is behind the trees before I have thought to look back at it.
    """

    call change_time(23, 30)

    $ play_music('danger', 2)

    """
    The road narrows, and the trees close over us.

    Then, for no reason that I can see, we slow down.
    """

    butler """
    I do not care for the sound the engine makes.
    """

    host """
    I cannot hear anything at all.
    """

    butler """
    It is a small thing, but I am sure there is something.

    I do not want to take any chances.
    """

    """
    He brings us to a stop at the side of the road.
    """

    play sound door_open

    """
    He steps down and lifts the bonnet, and I can see nothing of him but his back.

    I turn towards the staff, and they are both asleep in the back seat.

    When I look straight ahead again, there is a gun pointing right at me.
    """

    butler """
    I am sorry.
    """

    play sound gun

    jump host_ending_shot_in_car
