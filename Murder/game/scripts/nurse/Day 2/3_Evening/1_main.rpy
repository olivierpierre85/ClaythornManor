# --------------------------------------------
#   Nurse
#
#   Saturday - Evening
#
#   15:00 -> 23h
#
#   Music: sad
#
#   Position
#       - House: nurse, psychic, host, butler
#       - Forest: captain, doctor, drunk, lad
#       - Dead: broken
#
#   Notes :
#       - Nurse stays in the house during the hunt
#       - Witnesses the return of the hunting party
#       - Manning discussion (common text), nurse has lines in it
#       - Dinner with remaining guests
#       - Evening map, 90 minutes
# --------------------------------------------
label nurse_day2_evening:

    call change_time(15, 00, 'Evening', 'Saturday', hide_minutes=True, chapter='saturday_evening')

    $ nurse_details.add_checkpoint("nurse_day2_evening")

    call black_screen_transition("Rosalind Marsh", chapters_names[current_chapter])

    $ change_room("entrance_hall", irisout)

    $ play_music('sad')

    """
    I hear them before I see them.

    There is a commotion at the front door, a confusion of voices.

    Then the door swings wide and the hunting party files in.

    Something is wrong.

    Lady Claythorn's face is ashen.

    Two of the men are carrying someone between them.

    I step forward at once.
    """

    call common_day2_evening_entrance_dialog

    """
    The Captain takes charge with admirable promptness.

    I watch as Ted Harring helps carry the body up the stairs.

    I keep to one side.

    There is nothing more for me to do for Doctor Baldwin now.
    """

    call common_day2_evening_samuel_manning_discussion_part_1

    call common_day2_evening_samuel_manning_discussion_part_2

    """
    I watch the Captain lead Samuel Manning away.

    The man goes quietly, which surprises me.

    He seems to have only a dim sense of what has happened.
    """

    call common_day2_evening_samuel_manning_discussion_part_3

    $ change_room("bedroom_nurse")

    call change_time(16, 00)

    """
    I return to my room.

    I sit on the edge of the bed and press my fingers together.

    A man is dead.

    I have seen men die before, many of them, at far closer quarters than this.

    Yet there is something particular about a death in a house.

    It leaves a stillness in the air that does not belong there.
    """

    if nurse_details.threads.is_unlocked('captain_zanzibar'):

        """
        I think of the Captain and what I found in the library.

        His account of his wound at Zanzibar seemed improbable to me from the start.

        After today, I am no longer sure what to make of him.

        He acted with authority and presence of mind.

        But that, in itself, proves nothing.
        """

    call wait_screen_transition()

    call change_time(18, 30)

    play sound dinner_gong

    """
    The gong sounds.

    I would have preferred to stay in my room, but that is not the right course.

    It is better to be seen than to be conspicuous by my absence.
    """

    $ change_room("dining_room", irisout)

    $ play_music('sad', 3)

    """
    The dining room is noticeably quieter than it was last night.

    Three chairs sit empty.

    I take my usual place and look around the table.

    Everyone is subdued.

    Lady Claythorn stands.
    """

    call common_day2_evening_dinner_host

    """
    A measured speech.

    She holds herself well.

    I find myself wondering what she is actually feeling beneath that composed exterior.

    To my right, Amelia Baxter sits quietly.

    Across from me, Ted Harring stares at the tablecloth.
    """

    $ time_left = 90
    call run_menu(TimedMenu("nurse_day2_evening_dinner", [
        TimedMenuChoice("Speak to Mrs Baxter", 'nurse_day2_dinner_psychic'),
        TimedMenuChoice("Speak to Ted Harring", 'nurse_day2_dinner_lad'),
        TimedMenuChoice("Say nothing, eat your dinner", 'generic_cancel', early_exit=True),
    ], image_left = "psychic", image_right = "lad"))

    call change_time(21, 00)

    """
    Dinner ends.

    Very few words were exchanged.

    The butler sees the guests out of the room with quiet efficiency.

    Most of the others drift away towards their rooms.

    I do not feel ready to sleep just yet.

    The manor is quiet, but that is not the same as saying it is safe.

    Perhaps I ought to make a brief survey before I retire.
    """

    $ time_left = 90
    call run_menu(nurse_details.saved_variables["day2_evening_map_menu"])

    call change_time(22, 00)

    if time_left <= 0:

        """
        I have seen enough.

        It is time to sleep.
        """

    """
    I return to my room and lock the door behind me.

    It has been a long day.

    I need to sleep.
    """

    $ stop_music()

    jump work_in_progress


label nurse_day2_dinner_psychic:

    nurse """
    Are you quite all right, Mrs Baxter?
    """

    psychic """
    As well as one can be, I think.

    I keep seeing the poor man being carried in.

    It is not an easy image to shake.
    """

    nurse """
    It is not.

    But we must not let it overwhelm us.

    We shall leave tomorrow. The police will handle it from there.
    """

    psychic """
    Yes. You are quite right.

    Still, it is very sobering.

    One does not expect this sort of thing.
    """

    return


label nurse_day2_dinner_lad:

    nurse """
    Mr Harring.
    """

    lad """
    Miss Marsh.

    Quite a day, wasn't it.
    """

    nurse """
    Indeed.

    I hope you are not too shaken.
    """

    lad """
    Me? Oh, I'm all right. I mean...

    It's not the nicest thing, is it.

    Carrying someone back like that.
    """

    nurse """
    No.

    You did well, though.
    """

    lad """
    Suppose I did.

    Thanks, Miss Marsh.
    """

    return
