# ------------------------------------
#   BILLIARD ROOM
# ------------------------------------
label broken_day1_evening_billiard_room:

    call broken_ascend_if_needed

    $ change_room('billiard_room')

    if not broken_details.saved_variables['day1_evening_billiard_room_visited']:

        $ broken_details.saved_variables['day1_evening_billiard_room_visited'] = True

        """
        The billiard room is warm and full.

        Most of the party have gathered here over their drinks.

        The captain holds court near the fire, with Miss Marsh and Lady Claythorn listening to him.

        Manning has found the bar, and Baldwin a chair to brood in.

        The butler has noticed my presence and comes towards me.
        """

        butler """
        Mr Moody, would you care for a drink?

        A glass of sherry, perhaps?
        """

        broken """
        Thank you, but sherry is not my drink.

        Do not trouble yourself, though, I came prepared.
        """

        """
        I show him my trusty pocket flask.

        I keep it always on me, in case the company I am in is not entertaining enough.
        """

        butler """
        Oh, I see.
        """

        """
        His face shows disapproval, but, like any good servant, he will not dare to reprimand me.
        """

        butler """
        Well, it is true that the bar is a bit limited, but if you prefer something stronger, like whisky, we have a good one set aside for special occasions.
        """

        broken """
        Well, in that case, I am interested indeed.
        """

        butler  """
        Very well, I will fetch it and put it next to the other bottles if you want to try it later.

        In the meantime, please make yourself comfortable.
        """

        broken """
        Thank you.
        """

        """
        I watch the butler leave the room.

        What to do now?
        """

        $ broken_day1_evening_billiard_room_menu = TimedMenu("broken_day1_evening_billiard_room_menu", [
            TimedMenuChoice('Join the group and listen to the Captain', 'broken_day1_evening_billiard_room_story', 60),
            TimedMenuChoice('Talk to Dr Baldwin', 'broken_day1_evening_billiard_room_doctor', 0, next_menu = 'doctor_generic_menu_broken'),
            TimedMenuChoice('Leave the room', 'generic_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ broken_day1_evening_billiard_room_menu.early_exit = False

        """
        I look in on the billiard room again.

        I keep to the wall and watch a while longer.
        """

    call run_menu(broken_day1_evening_billiard_room_menu)

    return


# ------------------------------------
#   CAPTAIN'S STORY (the Boxer Rebellion)
#   Listening empties the flask. The player then chooses whether to charge
#   it from the butler's special whisky (refill) or leave it be (abstain).
#   The whisky is poisoned: refilling and drinking it is fatal.
# ------------------------------------
label broken_day1_evening_billiard_room_story:

    """
    I take a place at the edge of the captain's little audience.

    He is well into his stride, and grateful for another pair of ears.
    """

    captain """
    Ah, Mr Moody. Come to hear an old soldier's war stories, no doubt.

    Where was I? Yes.
    """

    call common_day1_evening_captain_billiard_room_speech_part_1

    """
    It promises to be an interesting story, but if I understand the captain, it might not be a short one.

    I raise the flask to my lips and find it dry.

    If I am to sit through the rest of this, I had best charge it again.

    The good whisky the butler set aside should be waiting among the bottles by now.

    Then again, it was put by for a special occasion. To help myself to the last of another man's prize bottle would be poor manners indeed.
    """

    call run_menu(TimedMenu("broken_day1_evening_billiard_room_whisky_menu", [
        TimedMenuChoice('Charge the flask from the special whisky', 'broken_day1_evening_billiard_room_refill', 0, early_exit=True),
        TimedMenuChoice('Leave it be, it would be impolite', 'broken_day1_evening_billiard_room_abstain', 0, early_exit=True),
    ]))

    return


# ------------------------------------
#   REFILL (the fatal choice)
#   He charges his flask from the poisoned whisky, shares a glass with
#   Harring, and drinks the rest through the captain's tale.
# ------------------------------------
label broken_day1_evening_billiard_room_refill:

    """
    I drift over to the bottles. The whisky stands among the sherry and the port, just as the butler promised.

    Samuel Manning is slumped there, so drunk he does not even notice me.

    I tip the last of the bottle into my flask and slip it back inside my coat.

    As I close the flask, one of the late arrivals drifts up to the bar at my elbow.

    Ted Harring, ill at ease, with the look of someone who has never quite belonged in a room like this.

    He tries to talk with Samuel Manning.
    """

    call common_day1_evening_moody_offers_harring_flask

    """
    I settle back among the listeners and take a long, well-earned pull from the flask.

    The whisky is every bit as good as the butler promised. Smooth, with a faint bitter note at the finish that I cannot quite place.

    I let the captain carry on.
    """

    $ broken_details.threads.unlock('drink_good_whisky')

    call common_day1_evening_captain_billiard_room_speech_part_2

    """
    An interesting tale.

    I remember my friend Thomas telling me about that war, one of his first campaigns, where he served as a young corporal.

    His version and the captain's are similar enough.
    """

    return


# ------------------------------------
#   ABSTAIN (the safe choice)
#   He leaves the whisky alone, hears the rest of the tale, then goes to
#   try it afterwards out of curiosity, only to find the bottle empty.
# ------------------------------------
label broken_day1_evening_billiard_room_abstain:

    """
    No. The bottle was set aside for the occasion, and draining the last of it would be the height of bad manners.

    I leave it where it stands and settle back among the listeners, dry flask and all, to let the captain carry on.
    """

    call common_day1_evening_captain_billiard_room_speech_part_2

    """
    An interesting tale.

    I remember my friend Thomas telling me about that war, one of his first campaigns, where he served as a young corporal.

    His version and the captain's are similar enough.
    """

    """
    Now that the captain has wound down, my curiosity gets the better of me. I should rather like to know what all the fuss was about.

    I make my way over to the bottles.
    """

    """
    The good whisky is gone. The bottle stands empty among the others.

    Someone else must have finished it while I sat listening.

    A pity. I shall never know what I missed.
    """

    return


# ------------------------------------
#   DR BALDWIN
#   Generic doctor conversation. Extra journalist questions for Moody
#   are still to be written — see the TODO in doctor_generic_menu_broken
#   (broken_config_menu.rpy).
# ------------------------------------
label broken_day1_evening_billiard_room_doctor:

    """
    Baldwin sits apart from the others, a glass cradled in his hands, his eyes fixed on nothing in particular.

    The same gaze I noticed in the tea room.

    I draw up a chair beside him.
    """

    broken """
    Dr Baldwin.
    """

    doctor """
    Mr Moody. Forgive me, I was somewhere else entirely.
    """

    call doctor_generic

    return
