# --------------------------------------------
#   Broken
#
#   Sunday - Morning
#
#   8:30 -> 11:30
#
#   Music: mysterious, danger, scary
#
#   Position
#       - House : Captain, Doctor, Mr Manning, Miss Baxter, Miss Marsh, Broken
#       - Gone  : Lady Claythorn and all the staff (left in the night)
#       - Dead  : Lad (Ted Harring)
#
#   Gates on the 'ambushed' ENDING (intuition), not on a thread:
#       - without it  -> no menu at all, the party splits, two men walk out
#       - with it     -> the argument menu opens. 30 minutes of patience, ten
#         minutes a question, so three may be asked. Only one route unlocks
#         'left_together' and takes the whole party out together: reach
#         'broken_day3_morning_question_culprit', then answer Miss Baxter's
#         demand for the mask with a soldier's honour. Every other answer to
#         that demand ends with the mask off and the ending burned.
#
# --------------------------------------------
label broken_day3_morning:

    $ broken_details.add_checkpoint("broken_day3_morning")

    call change_time(8, 30, 'Morning', 'Sunday', hide_minutes = True, chapter='sunday_morning')

    call black_screen_transition("Thomas Moody", chapters_names[current_chapter])

    $ change_room('billiard_room', irisout)

    $ play_music('mysterious', 2)

    """
    Dawn has come by the time I wake, stiff in my watch chair.

    I cannot believe I fell asleep.

    I check my mask at once, and find it slightly crooked.

    I adjust it and look about the room, but nobody is watching me.

    I turn to Captain Sinha, who is sitting perfectly straight on his chair.
    """

    captain """
    Ah, Mr Moody, you are awake.

    I believe you managed a little sleep.

    I did not, but it is quite all right.

    Do not worry, nothing happened during the night.
    """

    broken """
    Good. I am sorry, I did not think I would fall asleep.
    """

    captain """
    It happens.

    Do not blame yourself too much for it.
    """

    """
    I look around the room. Everyone is awake now, all of them dishevelled.

    Doctor Baldwin is in particularly bad shape, having contracted a sort of fever.

    Samuel Manning is already back to drinking from his pocket flask.

    The ladies have managed to make themselves presentable, and Captain Sinha looks as though he had passed a perfectly ordinary night in his own bed.

    I wonder what I look like, but it hardly matters now.

    It is time for action, and Captain Sinha takes the lead.
    """

    captain """
    Very well, now that everyone is awake, I think it is time we planned our next move.
    """

    """
    People murmur in agreement.
    """

    captain """
    Good.

    What I suggest is this.

    Let us go quickly to our rooms and get ready for the long walk.

    We can meet afterwards in the entrance hall.

    The sooner we leave, the better.
    """

    psychic """
    Captain, Miss Marsh and I have been speaking quietly together these last few minutes.

    And we have come to the sorry conclusion that we shall never make it.
    """

    captain """
    Not make it, Miss Baxter?

    It is a long journey, I will admit, but not a difficult one, merely a matter of following the road.

    And we shall walk slowly, and stop as often as you need.
    """

    psychic """
    I do not doubt it is only a stroll to a man of your training, Captain.

    But my constitution is not the thing it once was, and I am not dressed for such an undertaking.
    """

    nurse """
    And I am no better.

    My health has never been strong, and a whole day on a wet road would be very taxing.
    """

    """
    Captain Sinha considers this, then turns towards me.
    """

    captain """
    Perhaps they are right, Mr Moody.

    This journey might not be fit for the ladies.

    It would be best if they stayed here.

    And even the men are not in perfect shape.
    """

    """
    He looks at Samuel Manning, and Doctor Baldwin.

    They both look sickly and exhausted.
    """

    captain """
    We would certainly go faster, just the two of us.

    We could fetch help and be back before sundown.

    What do you think?
    """

    if not broken_details.endings.is_unlocked('ambushed'):

        """
        I do not like it, but cannot think of a strong argument against his idea.
        """

        call broken_day3_morning_leave_pair

        jump broken_day3_afternoon

    # ------------------------------------
    #   INTUITION - he has walked this road before
    # ------------------------------------
    $ play_music('danger', 2)

    """
    Something in me refuses it, flatly, though I could not tell why.

    If we do not leave together, something terrible will happen.

    But how can I convince everyone of this?
    """

    $ time_left = 30

    call run_menu(TimedMenu("broken_day3_morning_menu_convince", [
        TimedMenuChoice("Show them the bottle of rat poison{{object}}", 'broken_day3_morning_question_poison', 10),
        TimedMenuChoice("Talk about the Boxer Rebellion{{observation}}", 'broken_day3_morning_question_boxer', 10, condition="broken_details.threads.is_unlocked('doctor_boxer')"),
        TimedMenuChoice("What if Lady Claythorn is not the culprit?", 'broken_day3_morning_question_culprit', 10, condition="is_choice_already_chosen('broken_day3_morning_menu_convince', 'broken_day3_morning_question_boxer')"),
        TimedMenuChoice("Let it go. Leave with Captain Sinha", 'generic_cancel', 0, early_exit=True),
    ]))

    # The room only follows him if he got as far as naming the danger inside the
    # house, and then kept his mask on by pleading a soldier's honour.
    if is_choice_already_chosen('broken_day3_morning_menu_mask', 'broken_day3_morning_mask_honour'):

        call broken_day3_morning_departure_together

    else:

        if time_left <= 0:

            """
            I can see it in their faces before anybody speaks.

            Whatever I said was not convincing enough.
            """

            psychic """
            I am sorry, Mr Moody.

            Truly, I am.

            But not one word of it is reason enough to send me walking into a wood.
            """

            nurse """
            Nor me.
            """

            captain """
            Mr Moody, we cannot stand here arguing until sundown.
            """

            """
            And there it is.

            I have spent everything I had and moved not one of them an inch.
            """

        else:

            """
            I see in their eyes that I shall not be able to convince them.

            That leaves me only one choice.
            """

        call broken_day3_morning_leave_pair

    jump broken_day3_afternoon


# ------------------------------------
#   THE DEPARTURE OF TWO
# ------------------------------------
label broken_day3_morning_leave_pair:

    broken """
    Very well, Captain.

    The two of us, then.

    I assume Doctor Baldwin and Mr Manning will stay here to protect the ladies.
    """

    """
    Samuel Manning is still deep in thought.

    But Doctor Baldwin gives a slight nod in agreement.

    They will not be the best bodyguards today, but that will have to do.
    """

    broken """
    The rest of you keep together, with the door shut until we come back.

    Together, mind.

    Nobody wanders this house alone, not for a moment, not for any reason.
    """

    nurse """
    We shall stay here for as long as needed.

    Do not worry.
    """

    captain """
    Very well.

    No need to waste any more time, then.

    Mr Moody.
    """

    broken """
    Yes, let us go.
    """

    """
    We take our coats, leave the billiard room, and put Claythorn Manor behind us.
    """

    return


# ------------------------------------
#   THE DEPARTURE OF SIX
# ------------------------------------
label broken_day3_morning_departure_together:

    $ broken_details.threads.unlock('left_together')

    """
    I stop there, and let the room sit with everything I have told them.

    Nobody says anything for a while.
    """

    nurse """
    ...Very well.

    Perhaps you are right.

    It is more dangerous to stay here than to attempt the walk.

    I shall come with you.
    """

    doctor """
    So will I.
    """

    drunk """
    And me as well, then.
    """

    psychic """
    Oh, this is madness, every word of it.

    But I shall not be left the only soul in this house.

    If you are all set on going, then I shall go with you.
    """

    captain """
    Then it is settled, and we have wasted enough of the morning.

    Mr Moody, I hope you are right.
    """

    broken """
    So do I, Captain.
    """

    call change_time(11, 30)

    $ play_music('mysterious', 2)

    $ change_room('entrance_hall', dissolve)

    """
    It takes the better part of an hour to make six people fit for the journey.

    Coats and sound boots.

    Bread and cold water from the kitchen.

    It is almost noon when we step outside.

    All six of us.
    """

    return
