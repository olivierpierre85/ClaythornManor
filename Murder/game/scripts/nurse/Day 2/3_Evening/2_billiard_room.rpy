# Billiard Room - Saturday Evening
label nurse_day2_evening_billiard_room:

    $ change_room("billiard_room")

    if not nurse_details.saved_variables["day2_evening_billiard_room_visited"]:

        $ nurse_details.saved_variables["day2_evening_billiard_room_visited"] = True

        """
        A single lamp burns at the far end of the room.

        Captain Sinha is alone at the sideboard, a brandy glass in hand.

        He turns as I enter, but does not seem surprised to see me.
        """

        captain """
        Miss Marsh.

        I thought everyone had retired.
        """

        nurse """
        Not quite yet.
        """

        captain """
        Nor am I.

        Help yourself to something, if you wish.
        """

        """
        I decline with a small shake of my head.

        He carries his glass to the chairs by the fire.

        After a moment, I follow.
        """

        $ nurse_day2_evening_billiard_room_menu = TimedMenu("nurse_day2_evening_billiard_room_menu", [
            TimedMenuChoice('Ask about the staff', 'nurse_day2_evening_billiard_room_staff', 15),
            TimedMenuChoice('Ask about Zanzibar', 'nurse_day2_evening_billiard_room_zanzibar', 15),
            TimedMenuChoice('Ask about the Boxer Rebellion', 'nurse_day2_evening_billiard_room_boxer', 15),
            TimedMenuChoice('Leave', 'nurse_day2_evening_billiard_room_leave', 0, early_exit=True),
        ])

    else:

        """
        The Captain is still here.

        He glances up as I enter and raises his glass slightly.
        """

        $ nurse_day2_evening_billiard_room_menu.early_exit = False

    call run_menu(nurse_day2_evening_billiard_room_menu)

    return


label nurse_day2_evening_billiard_room_staff:

    nurse """
    I have been wondering about the staff here.

    Have you taken much notice of them, Captain?
    """

    captain """
    In what sense?
    """

    if nurse_details.threads.is_unlocked('footman_belgian'):

        nurse """
        The footman, in particular.

        # TODO placeholder — something in his bearing or speech that is not quite English.
        # The nurse should cite something specific that made her notice: an idiom, a vowel, a gesture.
        """

    if nurse_details.threads.is_unlocked('maid_actress'):

        nurse """
        And the maid.

        She is rather poised for a domestic servant.

        # TODO placeholder — the nurse notes something theatrical in her manner.
        # A quality of performance: too precise in her movements, too careful in her expressions.
        """

    if not nurse_details.threads.is_unlocked('footman_belgian') and not nurse_details.threads.is_unlocked('maid_actress'):

        nurse """
        I cannot quite say.

        # TODO placeholder — the nurse makes a vague, fishing observation.
        # She has noticed nothing specific, but there is something she cannot place.
        """

    captain """
    # TODO placeholder — captain's response.
    # Is he dismissive? Does he lower his voice? Does he share his own suspicion?
    # His manner here is a possible tell: if he is too quick to change the subject,
    # or if he glances toward the door before answering, that is worth noting.
    """

    """
    # TODO placeholder — nurse's internal reaction to what he says or doesn't say.
    """

    return


label nurse_day2_evening_billiard_room_zanzibar:

    nurse """
    You mentioned the Anglo-Zanzibar War yesterday.

    The wound on your back.
    """

    captain """
    What of it?
    """

    if nurse_details.threads.is_unlocked('captain_zanzibar'):

        nurse """
        # TODO placeholder — nurse uses what she found in the library.
        # The Anglo-Zanzibar War lasted under an hour. British firepower was overwhelming.
        # The "rather dangerous fighting" he described in the tea room does not square with that.
        # She should ask something specific: which ship, which position, which gate.
        # A question a nurse who was there in another capacity might reasonably know.
        """

        captain """
        # TODO placeholder — the captain is put on the defensive.
        # He may deflect to a general point about the chaos of war.
        # He may become slightly cold, or more precise than before — which would be its own red flag.
        """

        nurse """
        # TODO placeholder — nurse's internal conclusion.
        # His answer is not impossible, but it requires belief she is not certain she can extend.
        """

    else:

        nurse """
        # TODO placeholder — without the library research, the nurse presses more gently.
        # Something about the way he described it lodged in her mind.
        # She cannot place the exact problem, but she asks him to repeat a detail or two.
        """

        captain """
        # TODO placeholder — captain is relaxed, gives his usual version.
        # But something in the detail may be slightly different from what he said the day before.
        """

    return


label nurse_day2_evening_billiard_room_boxer:

    nurse """
    I was at the Boxer Rebellion as well, Captain.

    As a nurse.
    """

    """
    He pauses.

    I have clearly surprised him.
    """

    captain """
    Were you indeed?

    In what capacity?
    """

    nurse """
    I was attached to the field hospital at Tientsin before the column set out.

    And again in Beijing, afterwards.
    """

    captain """
    # TODO placeholder — captain responds to this.
    # He will want to establish common ground, but it is now harder to embroider his account.
    # Does he ask which regiment she was attached to? Which gate the British used?
    # Whatever he says, the nurse can test it against her own memory.
    """

    if nurse_details.threads.is_unlocked('captain_lie_rank'):

        nurse """
        # TODO placeholder — nurse is more pointed. She already noted on Friday evening
        # that Indian officers did not hold captain's rank at that time.
        # She can now press him face-to-face: she was there, she would have known.
        """

        captain """
        # TODO placeholder — captain deflects, appeals to an exceptional case,
        # or grows a degree cooler than before.
        # He does not contradict himself outright, but the answer requires more goodwill than she has.
        """

        nurse """
        # TODO placeholder — nurse's internal conclusion.
        # The lie, if it is one, is very well maintained.
        # But a well-maintained lie is still a lie.
        """

    else:

        nurse """
        # TODO placeholder — nurse plants the seed of suspicion without accusing.
        # She mentions a detail she remembers clearly, watches how he responds.
        """

        # TODO: consider unlocking captain_lie_rank here for players who missed the Day 1 billiard room.

    return


label nurse_day2_evening_billiard_room_leave:

    """
    I have nothing more to say tonight.
    """

    captain """
    Good night, Miss Marsh.
    """

    nurse """
    Good night.
    """

    return
