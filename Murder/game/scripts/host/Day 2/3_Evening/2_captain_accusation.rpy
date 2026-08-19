label host_day2_evening_captain_accusation:

    call common_day2_evening_captain_confronts_host

    """
    The room waits for me.

    I am tired and scared.

    Nothing has happened as I imagined.

    Maybe it is time to confess and hope the Captain will understand.
    """

    $ time_left = 1
    call run_menu(
        TimedMenu("host_day2_evening_menu_accusation", [
            TimedMenuChoice("Give him the title from the library book{{observation}}", 'host_day2_evening_accusation_answer', early_exit=True, condition = "host_details.threads.is_unlocked('family_history')"),
            TimedMenuChoice("Take offence and refuse the question", 'host_day2_evening_accusation_refuse', early_exit=True),
            TimedMenuChoice("Confess the truth", 'host_day2_evening_unmasked_end', early_exit=True),
        ])
    )

    return


# --------------------------------------------
#   She read the book, so she has the answer
# --------------------------------------------
label host_day2_evening_accusation_answer:

    """
    The history book, left open on the library table for me on the first evening.

    A title was mentioned in it.

    My title.

    What was it again?
    """

    host """
    Kilbraith, Captain.

    The family name is Claythorn.

    The peerage is the Earldom of Kilbraith, and I am styled Lady Kilbraith by anybody who troubles himself over such things.

    My father had grown weary of ceremony, as a great many did after the war, and preferred that we be known by the house.

    I have kept to it since, out of habit.
    """

    captain """
    Lady Kilbraith.

    Right, that is correct.
    """

    """
    I watch him lose all his composure.

    He was certain he had caught me in a lie, and now he does not know what to do.

    I should take advantage of that.
    """

    host """
    Is that all you wanted to know, Captain?

    You mentioned other things you noticed about me.

    Would you care to share them with us?
    """

    """
    He is silent and ashamed.
    """

    if host_details.threads.is_unlocked('no_portrait'):

        host """
        Or maybe I can do it for you?

        Maybe you noticed there was no portrait of me in the whole house?

        Do you also need to know why?

        Do you plan to accuse me all evening over trivial things like that?
        """

        """
        He is clearly shocked by the ease of my answer.

        I can see all the doubts he had about me vanish in an instant.
        """


    captain """
    I am sorry, my lady.

    Then I have wronged you, and before your own guests, which is a good deal worse.

    I offer you my apology without reservation. I shall not raise the matter again.
    """

    """
    He keeps on apologising for a full minute, and I have to bear every second of it with a gracious face.

    After what feels like an eternity, we all return to our rooms to get ready for dinner.
    """

    $ host_details.threads.unlock('bested_captain')

    return


# --------------------------------------------
#   She cannot give him a title, so she takes
#   offence instead. It does not work.
#
#   The mask comes off, the butler returns with
#   a revolver, and the Captain goes for him.
#   The first shot is the one that finds her.
# --------------------------------------------
label host_day2_evening_accusation_refuse:

    host """
    I shall not be talked like that in my own house, Captain.

    Two men have died beneath this roof today.

    Everyone is in shock and upset, but that doesn't give you the right of making absurd accusations.
    """

    captain """
    I am sorry, but this not an answer.

    You might be outraged, but I doubt it cost you this much to simply name your title.
    """

    """
    He is quite right, and I do not have enough strength to keep on pretending.

    Two men dead upstairs, and I am tired of being somebody else.
    """

    jump host_day2_evening_unmasked_end


# --------------------------------------------
#   Refusal and confession arrive at the same
#   room, and the same revolver.
# --------------------------------------------
label host_day2_evening_unmasked_end:

    call common_day2_evening_host_unmasked

    """
    The Captain does not look at the revolver. He looks at the hand holding it.

    Then he moves before anybody in the room has finished breathing.
    """

    play sound gun

    """
    The revolver goes off, and something takes me in the side, very hard, as though the chair had been kicked out from under me.

    There is no pain in it at all. That is the strange part.
    """

    jump host_ending_shot_tea_room