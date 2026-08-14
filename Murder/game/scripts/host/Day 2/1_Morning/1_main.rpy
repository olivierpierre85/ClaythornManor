# --------------------------------------------
#   Host
#
#   Saturday - Morning
#
#   07:30 -> 10:30
#
#   Music: chill for the waking, mysterious upstairs, scary for the announcement,
#          upbeat for the hunt (played by the common labels)
#
#   Position
#       - Bedroom : Host
#       - Dining Room : Everyone
#       - Dead : Broken (Thomas Moody), found in his bed
# --------------------------------------------
label host_day2_morning:

    call change_time(7, 30, 'Morning', 'Saturday', hide_minutes = True, chapter='saturday_morning')

    $ current_character.add_checkpoint("host_day2_morning")

    call black_screen_transition("Lady Claythorn", chapters_names[current_chapter])

    $ change_room('bedroom_host', irisout)

    $ play_music('chill', 3)

    """
    I wake and start getting ready for breakfast.

    I realise I have the easy role in all of this.

    The rest of the staff must have been at work for a good part of the night.

    And yet they are awake sooner than I am.

    I hope they will still be all right today.
    """

    call change_time(8, 30)

    $ change_room('dining_room', dissolve)


    """
    I reach the dining room, hoping to be the first one there.

    To my surprise, Captain Sinha is already seated, enjoying a light breakfast.
    """

    captain """
    Good morning.

    I am sorry, I have already begun.

    It is a soldier's habit, I am afraid.
    """

    host """
    Do not worry, Captain.

    I will fix myself a plate and join you shortly.
    """

    """
    I take my place at the table, and the guests arrive one by one.
    """

    call change_time(9, 15)

    """
    The last one to arrive is Samuel Manning.

    That is no surprise.

    He looks as though he drank himself to sleep last night.
    """

    $ play_music('mysterious', 2)

    """
    But I do not see Thomas Moody here.

    That I did not expect.

    The butler enters the room and comes directly towards me.

    I did not even notice him come in.

    He whispers in my ear.
    """

    butler """
    I think there is something wrong with Thomas Moody.
    """

    host """
    What do you mean?
    """

    butler """
    He is still in his bed at this hour.

    That cannot be normal.
    """

    host """
    Really?

    What is wrong with him?
    """

    butler """
    I am not sure.

    We should ask Doctor Baldwin to come and look at him, just in case.
    """

    host """
    All right.
    """

    call common_day2_morning_host_to_doctor

    call common_day2_breakfast_follow_doctor_lad_host

    $ change_room('bedrooms_hallway', dissolve)

    """
    He closes the door behind us.
    """

    butler """
    I am sorry you had to see that.
    """

    host """
    What is happening?

    I do not understand.

    Is this part of the plan?
    """

    butler """
    No, of course not.

    I assure you it is an accident.

    As I am sure Doctor Baldwin will soon confirm.
    """

    host """
    An accident, yes.

    God, I hope that is what it is.

    But what should we do?

    Surely we cannot carry on.

    We must cancel everything now.
    """

    butler """
    No!

    There is no need for such a rash decision.

    We will probably lose our wages if we do that.
    """

    host """
    I do not care about the money!

    This whole enterprise was already shady enough without adding a death to it.

    I do not want to be part of it any more.
    """

    butler """
    Please wait a little.

    You may not need the money, but I do.

    And so does the rest of the staff.

    Do not be so selfish as to stop everything now.
    """

    """
    I try to regain my composure and think clearly for a second.
    """

    butler """
    Please, all I ask is that we keep to what was planned for today.

    We can decide later what needs to be done, once we have a little more information.
    """

    host """
    Yes, yes.

    But my speech...

    It will not do any more.

    I do not...
    """

    butler """
    It will still work.

    Just improvise a little.

    Please, let us keep going just for a little while longer.
    """

    host """
    Very well.

    I suppose I can manage that.
    """

    # =>>> NEXT
    # TODO add what to do next:
    # K

    # if host_details.threads.is_unlocked('found_poison'):

    #     """
    #     And I cannot stop thinking of that bottle in the scullery, standing open in a house with no rats worth the trouble.
    #     """

    # TODO: The authorities. The doctor asks for them to be sent for, the butler
    #       undertakes to see to it, and she is the only one in the room who knows
    #       what his undertakings are worth.
    # TODO: Menu candidate - press the butler about the telephone or the car now, or
    #       hold her tongue until the guests are out of the house. Needs threads.

    call change_time(10, 00)

    $ change_room('dining_room', dissolve)

    # TODO: Going back in. The whole table turns, and she has to say it out loud.

    call common_day2_morning_host_death

    call common_day2_morning_host_death_doctor

    # TODO: Sitting through the silence afterwards, counting how many of them are
    #       looking at her rather than at their plates.
    # TODO: And the thing she cannot say: a man is dead in a house that was opened for
    #       three days by a gentleman neither she nor the butler has ever met.

    call change_time(10, 15)

    $ stop_music()

    """
    What now?
    """

    call common_day2_morning_host_hunt

    """
    As expected, Miss Marsh and Miss Baxter excuse themselves.

    The men all agree to come.

    Well, I should get ready too.
    """

    jump host_day2_hunt
