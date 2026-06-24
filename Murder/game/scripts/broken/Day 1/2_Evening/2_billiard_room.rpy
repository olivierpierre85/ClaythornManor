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
        Well, if it is whisky you would like, we have a very good one at the bar, but it is almost empty, I am afraid.
        """

        broken """
        I will keep that in mind, thank you.
        """

        """
        The butler returns to his place in a corner of the room.
        """

        if broken_details.threads.is_unlocked('host_lies'):

            """
            Normally, a guest wouldn't go and talk with the servants.

            But since I know Lady Claythorn is hiding something, I think it might be interesting to ask a few questions to the butler.

            The potential reward is higher than the risk of attracting attention.
            """

        else:

            """
            I could put a few questions to the butler, but a guest who quizzes the servants is rather unusual.

            And I don't want to attract attention.
            """

        """
        What to do now?
        """

        $ broken_day1_evening_billiard_room_menu = TimedMenu("broken_day1_evening_billiard_room_menu", [
            TimedMenuChoice('Join the group and listen to the Captain', 'broken_day1_evening_billiard_room_story', 60),
            TimedMenuChoice('Talk to Dr Baldwin', 'broken_day1_evening_billiard_room_doctor', 0, next_menu = 'doctor_generic_menu_broken'),
            TimedMenuChoice('Speak with the butler', 'broken_day1_evening_billiard_room_butler', 0, keep_alive = True, next_menu = 'broken_butler_menu', condition = "broken_details.threads.is_unlocked('host_lies')"),
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

    I raise the flask to my lips and find it almost dry.

    If I am to sit through the rest of this, I had best charge it again.
    """

    call run_menu(TimedMenu("broken_day1_evening_billiard_room_whisky_menu", [
        TimedMenuChoice('Go to the bar to charge the flask', 'broken_day1_evening_billiard_room_refill', 0, early_exit=True),
        TimedMenuChoice('Leave it be, it would be impolite', 'broken_day1_evening_billiard_room_abstain', 0, early_exit=True),
    ]))

    call common_day1_evening_captain_billiard_room_speech_part_2

    """
    An interesting tale.

    I remember my friend Thomas telling me about that war, one of his first campaigns, where he served as a young corporal.

    His version and the captain's are similar enough.
    """

    if not broken_details.threads.is_unlocked('drink_good_whisky'):

        """
        Now that the captain has wound down, I feel I have earned a drink.

        I make my way over to the bottles.

        The whisky is gone. The bottle stands empty among the others.

        Someone else must have finished it while I sat listening.

        A pity.
        """

    return


# ------------------------------------
#   REFILL 
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

    I let the captain carry on.
    """

    $ broken_details.threads.unlock('drink_good_whisky')

    return


# ------------------------------------
#   ABSTAIN (the safe choice)
# ------------------------------------
label broken_day1_evening_billiard_room_abstain:

    """
    No. I do not need to attract more attention to myself than needed.

    I'll have to listen to the story sober.
    """
    
    return


# ------------------------------------
#   THE BUTLER
#   Always available. Opens a small menu of questions. The butler gives
#   nothing away, and marks Moody for the asking. This is the man who later
#   cuts his throat (broken_ending_day1_throat_cut). The surprise question
#   is only offered once the maid has been questioned (talked_to_maid).
# ------------------------------------
label broken_day1_evening_billiard_room_butler:

    if not broken_details.saved_variables['day1_evening_billiard_room_butler_approached']:

        $ broken_details.saved_variables['day1_evening_billiard_room_butler_approached'] = True

        """
        The butler stands in his corner, hands folded, missing nothing.

        If I want information about this weekend, he should be the one to have it.

        I cross to him as though only in want of conversation.
        """

        butler """
        Mr Moody, what can I do for you?
        """

    else:

        $ broken_butler_menu.early_exit = False

        """
        I head back towards the butler in his corner.
        """


    
    $ broken_butler_menu = TimedMenu("broken_butler_menu", [
        TimedMenuChoice('Remark on the worn-out look of the house', 'broken_day1_evening_billiard_room_butler_house', 20),
        TimedMenuChoice('Discuss the small number of staff', 'broken_day1_evening_billiard_room_butler_staff', 15),
        TimedMenuChoice('Ask him about himself', 'broken_day1_evening_billiard_room_butler_about', 15),
        TimedMenuChoice('Ask about the surprise the maid mentioned', 'broken_day1_evening_billiard_room_butler_surprise', 20, condition = "broken_details.threads.is_unlocked('talked_to_maid')"),
        TimedMenuChoice('Leave the butler to his work', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_left = "butler")

    call run_menu(broken_butler_menu)

    return


# ------------------------------------
#   BUTLER — THE STATE OF THE HOUSE
# ------------------------------------
label broken_day1_evening_billiard_room_butler_house:

    broken """
    A fine room, this.

    Though I confess the house puzzles me.

    It has the feel of a place only lately woken from a long sleep.
    """

    """
    Something flickers behind his eyes, there and gone.
    """

    butler """
    Lady Claythorn lives rather a secluded life.

    I must admit some of the rooms had to be reopened after standing empty for a long time.

    That would explain why some of them have a rather untidy air about them.

    I do apologise for it.
    """

    """
    He answers smoothly enough, yet I have little doubt the butler is shading the truth about this house.
    """

    return


# ------------------------------------
#   BUTLER — THE SIZE OF THE STAFF
# ------------------------------------
label broken_day1_evening_billiard_room_butler_staff:

    broken """
    Tell me, how many of you are there, keeping a house of this size?

    I have seen remarkably few faces about the place.
    """

    butler """
    That is true, we are a small staff, sir.

    Smaller than a house like this would once have kept, I will own.

    Her ladyship spends most of her time alone, so she does not require a great deal of help.
    """

    broken """
    Aren't you worried it will be a rather limited staff for this weekend?
    """

    butler """
    Not at all.

    I can assure you we will manage well enough, sir.
    """

    """
    A house this size ought to swarm with servants.

    But I suppose his explanation is believable enough.
    """

    return


# ------------------------------------
#   BUTLER — THE MAN HIMSELF
# ------------------------------------
label broken_day1_evening_billiard_room_butler_about:

    broken """
    Forgive me if I am intruding, but I would like to know how long you have been a butler here.

    You seem to have a remarkable handle on things.
    """

    """
    A bit of flattery is usually a good way to get better answers.
    """

    butler """
    You are kind to say so, sir.

    I have been in the service of Lady Claythorn for a few years now.
    """

    broken """
    And what were you doing before that?
    """

    butler """
    Well, the same thing, of course.

    Just for another house, that is all.

    Sadly, it had to close, and all of the staff were let go.
    """

    broken """
    I am sorry, it is a story that is becoming too familiar these days.

    But it is good that you found another job.
    """

    butler """
    It is indeed.

    I was very lucky.
    """

    """
    A plausible and very common story.

    I will have to dig deeper if I want to learn something really useful.
    """

    return


# ------------------------------------
#   BUTLER — THE SURPRISE (talked_to_maid required)
# ------------------------------------
label broken_day1_evening_billiard_room_butler_surprise:

    broken """
    I had heard there might be some surprise laid on for us this weekend.

    A diverting one, I hope.
    """

    """
    He holds my gaze a moment longer than a servant ought.
    """

    butler """
    I assume you are referring to the prize that will be awarded at the end of this weekend.

    But it is hardly a surprise.

    Everyone has been forewarned.
    """

    broken """
    Of course, but that is not what I meant.

    I know I shouldn't have eavesdropped, but I overheard someone on your staff talking of a possible special surprise for us.
    """

    """
    Something in the look of the butler changes for a second.

    He is genuinely troubled by this.
    """

    butler """
    I am sorry, I think you might have misheard.

    There is nothing planned besides what Lady Claythorn explained at dinner.
    """

    broken """
    Oh, sorry I didn't want to intrude.
    """

    butler """
    No worries.
    """

    """
    I do not believe him.

    I have spent enough time doing interviews to know when someone is hiding something.

    Of course, if it is a surprise, obviously he might want it a secret.

    It doesn't necessarily mean it is a bad one.

    But I should keep it in mind nevertheless.
    """

    $ broken_details.threads.unlock('butler_surprise')

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
