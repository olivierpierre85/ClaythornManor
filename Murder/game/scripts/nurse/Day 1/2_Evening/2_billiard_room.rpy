# Billiard room
label nurse_day1_evening_billiard_room:

    $ change_room('billiard_room')

    if not nurse_details.saved_variables["day1_evening_billiard_room_visited"]:

        $ nurse_details.saved_variables["day1_evening_billiard_room_visited"] = True

        """
        A haze of pipe smoke hangs over the room.

        Captain Sinha is holding court near the fireplace.

        A small audience has gathered — the Captain's voice carries, and his stories have the weight of a man who expects to be listened to.
        """

        $ nurse_day1_evening_billiard_room_menu = TimedMenu("nurse_day1_evening_billiard_room_menu", [
            TimedMenuChoice('Listen to Captain Sinha', 'nurse_day1_evening_billiard_room_captain', 120),
            TimedMenuChoice('Go to the bar for a drink', 'nurse_day1_evening_billiard_room_bar', 10),
            TimedMenuChoice('Talk to Doctor Baldwin', 'nurse_day1_evening_billiard_room_doctor', 10),
            TimedMenuChoice('Leave the room', 'nurse_day1_evening_billiard_room_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ nurse_day1_evening_billiard_room_menu.early_exit = False

        """
        I am back in the billiard room.
        """

    call run_menu(nurse_day1_evening_billiard_room_menu)

    return


label nurse_day1_evening_billiard_room_captain:

    """
    I move a little closer to the group.

    Thomas Moody, Lady Claythorn, and Ted Harring are all listening attentively.

    Even the butler, standing quietly in the corner, seems to be following every word.
    """

    captain """
    Miss Marsh.

    I was just telling everyone here a story.

    Where was I?

    Oh, right.
    """

    call common_day1_evening_captain_billiard_room_speech_part_1

    """
    The "Boxers"?

    I remember those. That was one of my first campaigns, and perhaps the most terrible of them all.

    Was Captain Sinha there as well? How curious that would be.

    I had better listen until the end.
    """

    call common_day1_evening_captain_billiard_room_speech_part_2

    """
    Not the worst story-teller, I will grant him that.

    But there is something that troubles me about his tale.

    There was no Indian officers during that time — not at that rank.

    That may well have changed after the Great War, but I am quite certain he did not hold that rank in those days.

    And the claim that he was sent to London to command a training regiment — which would have been composed entirely of white men — is even more far-fetched.

    There is something wrong about his story.

    I should keep it in mind.
    """

    $ nurse_details.threads.unlock('captain_lie_rank')

    return


label nurse_day1_evening_billiard_room_bar:

    """
    I take a step towards the bar, then stop myself.

    No. In my condition, a drink is quite out of the question.

    That was foolish to even consider it.

    I turn away before anyone notices.
    """

    return


label nurse_day1_evening_billiard_room_doctor:

    """
    Doctor Baldwin is sitting alone in his chair, a glass of port in hand.

    I make to approach him.

    But there is something in his eyes that unsettles me.

    He is distant, tired.

    It is plain he wishes to be left alone.

    I had better not.
    """

    # TODO maybe add dialog with the doctor to help see connection with boxer rebellion?

    return


label nurse_day1_evening_billiard_room_cancel:

    """
    I don't feel like staying in this room any longer.
    """

    return