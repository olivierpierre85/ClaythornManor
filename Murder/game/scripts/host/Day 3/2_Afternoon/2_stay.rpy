# --------------------------------------------
#   Host - Sunday afternoon, she goes in to the others
#
#   The Captain has gone for the town on foot. She crosses the hall to
#   Ted Harring and Amelia Baxter, gives them the news herself, and sits
#   down to the lunch the two of them make. Miss Marsh never comes down.
#
#   Plates (see day3_poisoning_chart.md): Miss Baxter cooked for three.
#       Mr Harring's place, a sedative
#       Miss Baxter's place, clean
#       The host's place, the poison that was meant for Miss Marsh
#   With no Captain at the door and no Miss Marsh at the table there is
#   no swap to see and nothing to read. She eats, and she dies first.
# --------------------------------------------
label host_day3_afternoon_stay:

    """
    I have lied to those two for three days, and I have left them to themselves for three nights.

    I am not going to sit behind a locked door and listen to them wait for a policeman who is never coming.

    I put the key in my pocket, and I cross the hall.
    """

    call host_day3_afternoon_tea_room_talk(False)

    host """
    Then we wait.
    """

    """
    I sit down in the chair nearest the door, which is where the Captain would have sat.

    Nobody says anything for a while.
    """

    psychic """
    None of us has eaten since dinner.

    I could see what the kitchen has, if somebody will come down with me. I do not much care to go alone.
    """

    """
    I open my mouth to say I will, and close it again.

    Lady Claythorn does not go below stairs.

    I have kept to that for three days, and the habit is stronger than I am.
    """

    lad """
    I'll come.
    """

    """
    And so they go down, the two of them, and I am left with the dead fire.
    """

    if host_details.saved_variables["day3_morning_nurse_checked"]:

        """
        Miss Marsh has not come down.

        The Captain and I opened her door this morning, and her bed had not been slept in.

        I do not know what that means, and I do not go up to find out.
        """

    else:

        """
        Miss Marsh has not come down all morning.

        Nobody has said her name, and I do not say it either.
        """

    """
    The key is in my pocket. The door is six feet away.

    I do not move.
    """

    call change_time(13, 00)

    call wait_screen_transition()

    """
    It is the boy who comes to fetch me, three quarters of an hour later.
    """

    lad """
    It's ready.

    It's not much, but Miss Baxter says it'll do.
    """

    call host_day3_afternoon_stay_lunch

    jump host_ending_poisoned


# --------------------------------------------
#   Three plates
# --------------------------------------------
label host_day3_afternoon_stay_lunch:

    $ change_room('dining_room', dissolve)

    """
    Three plates on the long table, at three of the same places as on Saturday night, and five empty chairs between them.

    The boy sets the last of them down as I come in. Miss Baxter is already in her chair.
    """

    psychic """
    It is not what you are used to, Lady Claythorn.

    I did what I could with a cold range.
    """

    host """
    It is more than I expected, Miss Baxter.

    Thank you.
    """

    """
    I take my place at the head of the table.

    One last time.
    """

    if host_details.threads.is_unlocked('found_poison'):

        """
        There is a bottle missing from a shelf in the scullery, and it has been in somebody's pocket since Friday.

        I look at the three plates. They are exactly alike.

        Whatever I am looking for, it is not on the table, and there is nothing I can do about it.
        """

    else:

        """
        I look at the three plates, because I have learnt to look at everything in this house.

        They are exactly alike, and nobody has touched any of them.

        There is nothing to see.
        """

    """
    The boy picks up his fork, and so does Miss Baxter, and so do I.

    It is plain food, and it is not bad, and I am hungrier than I knew.
    """

    call change_time(13, 30)

    pause 1.0

    """
    It starts in my hands.

    I set my fork down very carefully, as though it might break, and I put a hand flat on the table.
    """

    psychic """
    Lady Claythorn? Are you quite all right?
    """

    host """
    The food.

    It was...
    """

    $ play_music('danger', fadeout_val=2)

    """
    The boy is up. He is saying something, and he is very far away.

    Miss Baxter has not moved.

    She is looking at me across the table, and there is nothing in her face at all.
    """

    """
    Then the room goes over on its side.
    """

    play sound body_fall

    $ stop_music()

    scene black_background with dissolve

    pause 2.0

    """
    Nothing.
    """

    return
