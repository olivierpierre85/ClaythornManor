label host_day1_evening_debrief:
    # Mistakes counter
    python:
        host_debrief_fault_count = 0
        host_debrief_fault_index = 0

        if not host_details.threads.is_unlocked('addressed_manning_first'):
            host_debrief_fault_count += 1

        if host_details.threads.is_unlocked('go_downstairs'):
            host_debrief_fault_count += 1

        if not host_details.threads.is_unlocked('stayed_with_guests'):
            host_debrief_fault_count += 1

    $ change_room('bedroom_host', dissolve)

    $ play_music('mysterious', 2)

    play sound door_knock

    """
    Someone knocking at this hour.

    That can only be him.
    """

    butler """
    My lady?
    """

    host """
    Yes, come on in.
    """

    """
    He enters and immediately loses his air of obedience.
    """

    if host_debrief_fault_count > 0:

        if host_debrief_fault_count == 1:

            butler """
            Well, the first day is done, and better than I feared.

            There is one thing, though.
            """

            host """
            Oh? What was it?
            """

        else:

            butler """
            Well, the first day is done, but I am afraid it was not without mistakes.
            """

            host """
            Really, what happened?
            """

        if not host_details.threads.is_unlocked('addressed_manning_first'):

            call host_day1_evening_debrief_next_fault

            if is_choice_already_chosen('host_day1_evening_menu_dinner', 'host_day1_dinner_broken'):

                butler """
                You went to your right first at dinner.

                You should have gone to your left, as was plainly set out in the book of rules I gave you.
                """

                host """
                Oh, sorry, I forgot about that rule.

                But surely nobody noticed.
                """

                butler """
                Maybe, but I am not sure.

                I think some of them might be more accustomed to that sort of thing than we first thought.
                """

            else:

                butler """
                You sat through your own dinner between two guests and spoke to neither of them.

                That is not how a hostess behaves, and people have noticed.

                It made everyone uncomfortable.
                """

        if host_details.threads.is_unlocked('go_downstairs'):

            call host_day1_evening_debrief_next_fault

            butler """
            You went below stairs.

            The mistress of a house does not go down to the servants' floor.

            She rings, and she waits, and they come up to her.
            """

            host """
            Surely that cannot be so bad.

            I am sure nobody noticed.
            """

            butler """
            You cannot be certain of that.

            Even so, you might have run by chance into a guest, and that would have raised questions.

            You should not take such a risk.
            """

            host """
            Very well.
            """

        if not host_details.threads.is_unlocked('stayed_with_guests'):

            call host_day1_evening_debrief_next_fault

            butler """
            You invited them for drinks and then did not appear in the billiard room at all.

            They sat up waiting for their hostess to look in.

            No doubt questions were raised.
            """

        if host_debrief_fault_count == 1:

            butler """
            It is not fatal in itself.

            But it is the sort of small thing that sits badly with people, and they do not forget it.
            """

        else:

            butler """
            None of it is fatal on its own.

            But taken all together, it might attract attention.
            """

        butler """
        You should do better tomorrow.
        """

        """
        He is right, of course.

        I have not been careful enough.

        If I want this weekend to be a success, I should pay more attention to details.
        """

    else:

        butler """
        I shall not keep you.

        It went well. The speech was better than I expected.

        And you acted the part without a mistake.

        At least not one I could notice.
        """

        host """
        Of course, I assume you were observing me all evening.
        """

        butler """
        Yes, sorry if that is unnerving, but I need to make sure everything is going according to plan.
        """

        host """
        Of course.
        """

    butler """
    Now, if you will excuse me.

    We shall meet again tomorrow.
    """

    host """
    Of course, good night.
    """

    """
    He leaves without another word.

    I suppose he will only play the dutiful servant when we have company.

    Anyway, it has been a long day, so I take my clothes off and get into bed.

    It is not long before I fall asleep.
    """

    return


# ------------------------------------
#   DEBRIEF — JOINING THE FAULTS UP
# ------------------------------------
label host_day1_evening_debrief_next_fault:

    $ host_debrief_fault_index += 1

    if host_debrief_fault_index == 1:

        return

    if host_debrief_fault_index == 3:

        butler """
        And the last of it.
        """

    elif host_debrief_fault_count == 2:

        butler """
        And there is one other thing.
        """

    else:

        butler """
        That is not the whole of it.
        """

    return