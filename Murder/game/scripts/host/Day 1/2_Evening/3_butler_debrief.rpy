# OBSOLETE FOR NOW

label host_day1_evening_debrief:

    $ play_music('mysterious', 2)

    play sound door_knock

    """
    Someone knocking at this hour.

    That can only be him.
    """

    butler """
    My lady? May I come in.
    """

    host """
    Yes, come on in.
    """

    """
    He enters and immediately lose his air of obedience.
    """

    # TODO add picture not smiling? seriouS?

    if host_details.threads.is_unlocked('addressed_manning_first') or host_details.threads.is_unlocked('stayed_with_guests') or host_details.threads.is_unlocked('go_downstairs'):

        butler """
        Well, the first day is gone, but I am afraid it was not without mistakes.
        """

        host """
        Really, what happened?
        """

        butler """
        TODO
        """
        if not host_details.threads.is_unlocked('addressed_manning_first'):

            if is_choice_already_chosen('host_day1_evening_menu_dinner', 'host_day1_dinner_broken'):

                butler """
                You went to your right first at dinner.
                """

                host """
                One man. One turn of the head.
                """

                butler """
                To the one man at that table who has been in service.

                I know another footman when I see one. He has stood at a wall through a hundred dinners watching real ones do it correctly.

                And he knew the moment you did it. So did I, from the door.
                """

            else:

                butler """
                You sat through your own dinner between two guests and spoke to neither of them.

                A silent hostess is a frightened one, and there is no reason on earth for that woman to be frightened at her own table.
                """

        if not host_details.saved_variables['day1_evening_billiard_room_visited']:

            butler """
            And then you gave them drinks and did not come.

            They sat up until eleven waiting for their hostess to look in.
            """

            host """
            I needed an hour where nobody was looking at me.
            """

            butler """
            You will not get one. Not this weekend.
            """

        butler """
        None of it is fatal on its own. Together it is a woman who does not quite fit her own house.

        That is precisely how they begin. Not with an accusation. With a small thing that does not sit right, and then another, and then they start asking one another whether they noticed it too.

        Do better tomorrow.

        There is no understudy.
        """

        """
        He is right, which is the worst of it.

        I have been telling myself all evening that I got away with it, and he has stood in a corner counting the places where I did not.
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
    Now, if you'll excuse me.
    
    We will meet again tomorrow.
    """

    host """
    Of course, good night.
    """

    """
    He leaves without a word.
    """



    """
    He is at the door already.

    No. Not yet.

    There are things about this house I would like explained while there is nobody about to hear me ask.
    """

    $ time_left = 50

    call run_menu(TimedMenu("host_day1_evening_debrief_menu", [
        TimedMenuChoice('I am not Lady Claythorn. I am Lady Kilbraith.', 'host_day1_evening_debrief_name', 10, condition = "host_details.threads.is_unlocked('family_history')"),
        TimedMenuChoice('There is no portrait of me in this house', 'host_day1_evening_debrief_portrait', 10, condition = "host_details.threads.is_unlocked('no_portrait')"),
        TimedMenuChoice('There is an open bottle of rat poison in the scullery', 'host_day1_evening_debrief_poison', 10, condition = "host_details.threads.is_unlocked('found_poison')"),
        TimedMenuChoice('Why do I not have the key to my own attic?', 'host_day1_evening_debrief_attic', 10, condition = "host_details.saved_variables['day1_evening_attic_tried']"),
        TimedMenuChoice('Who is paying for all this?', 'host_day1_evening_debrief_employer', 10),
        TimedMenuChoice('Let him go to bed', 'generic_cancel', 0, keep_alive = True, early_exit = True),
    ], image_left = "butler"))

    $ stop_music()

    call change_time(0, 30, 'Morning', 'Saturday', hide_minutes=True)

    """
    When he has gone I sit a while with the lamp on and my hands flat on my knees, which is what I do before a first night.

    Seven people asleep along that corridor, and every one of them believes a thing about me that is not true.

    I have never had a better part.

    I have never once been frightened of one before.
    """

    jump work_in_progress


# ------------------------------------
#   THE NAME (family_history)
# ------------------------------------
label host_day1_evening_debrief_name:

    host """
    I read the book in the library tonight.

    The family is Claythorn. The title is Kilbraith. Earls of Kilbraith, since before Waterloo.

    Which means the woman I am playing has been introducing herself all evening by a name no peer would ever use.

    You had me learn which fork. You did not think to give me my own name.
    """

    """
    He does not apologise. I did not expect him to.
    """

    butler """
    Then you know more than you did this morning, and you had it out of a book that anybody in that house may read.
    """

    host """
    That is not an answer.
    """

    butler """
    No. Here is one.

    We were given the name to use. It was on the letters, and the letters went out before either of us was engaged.

    I could hardly send eight people an invitation from Lady Claythorn and produce a Lady Kilbraith at the door.
    """

    host """
    Then whoever wrote those letters does not know how a peerage works.
    """

    butler """
    Or did not care.
    """

    """
    He says it evenly, and something in the evenness of it is worse than if he had looked worried.
    """

    host """
    And if one of them puts it to me?
    """

    butler """
    You will say the village has called this house Claythorn since your grandfather's day, and you long ago stopped correcting people.

    Say it as though it bores you.

    You will find that the truth and a bored woman are very difficult to tell apart.
    """

    return


# ------------------------------------
#   THE PORTRAIT (no_portrait)
# ------------------------------------
label host_day1_evening_debrief_portrait:

    host """
    There is a gallery downstairs with a dozen of my ancestors in it and not one of me.

    A house like this has a portrait of its mistress. It is the whole point of a house like this.

    All it takes is one of them standing in that gallery asking which one is you.
    """

    butler """
    I know.
    """

    host """
    You know.
    """

    butler """
    There was to have been one.

    A canvas was to be hung in the gallery before the guests arrived, and it did not come.

    I have written twice about it and had no reply.
    """

    """
    That is the first time tonight that he has told me something without deciding to.

    He has been sending letters to somebody and getting nothing back.
    """

    host """
    Then I shall have to be vain about it. A portrait was begun in the spring, the man made me look like my own mother, and I sent it back.
    """

    butler """
    That will do very well.

    Be sure to be a little ashamed of it. Vanity is only believed when it is admitted.
    """

    return


# ------------------------------------
#   THE POISON (found_poison)
# ------------------------------------
label host_day1_evening_debrief_poison:

    host """
    There is a bottle of rat poison standing open on the scullery shelf.

    Above the sink. Half gone.
    """

    """
    Nothing moves in his face. Nothing ever does, which is why I am watching it so closely.
    """

    butler """
    An old house that has stood empty has rats, my lady.

    I shall have it corked and put in a cupboard.
    """

    host """
    Half of it is gone.

    This house was opened up for us this week and nobody has said one word to me about rats.
    """

    butler """
    Because nobody tells the mistress of the house about the rats.

    That is rather the point of a mistress of the house.
    """

    host """
    Do not be clever with me. Not tonight.

    Who has been using it?
    """

    butler """
    I will find out.
    """

    """
    And that is all I get.

    Not a denial. Not a laugh at a nervous woman. He does not tell me it is nothing.

    He says he will find out, which means he does not know, and I have never once seen that man not know a thing about his own house.
    """

    return


# ------------------------------------
#   THE ATTIC KEY (day1_evening_attic_tried)
# ------------------------------------
label host_day1_evening_debrief_attic:

    host """
    The attic door is locked.
    """

    butler """
    It is.
    """

    host """
    I own every room under this roof, and there is one I cannot open.

    You have the key.
    """

    butler """
    I have all the keys, my lady. That is what a butler is.

    There is nothing above but the staff rooms and a great deal of dust sheets.
    """

    host """
    Then there is no reason I should not see it.
    """

    butler """
    None whatever.

    Tomorrow, when there is light and time, and when the lady of the house has some better reason to be on the attic stair than curiosity.
    """

    """
    Tomorrow. Of course.

    He has not refused me. He has simply arranged for it not to happen tonight, which is a thing I have watched managers do to actresses my whole working life.

    I know exactly what it looks like, and I let it pass, and I am angry with myself for letting it pass.
    """

    return


# ------------------------------------
#   THE EMPLOYER
# ------------------------------------
label host_day1_evening_debrief_employer:

    host """
    Before you go.

    Who is paying for this?

    Not the wages. I know where my wages come from. The house, the staff, the seven thousand pounds we are to hand out on Sunday.
    """

    butler """
    A gentleman who prefers his name kept out of it.
    """

    host """
    You have met him.
    """

    butler """
    I have had letters from him.

    Terms, dates, the guest list, the sums. Everything one could want, in a very fine hand.
    """

    host """
    And a joke to be played on the guests before we go.
    """

    butler """
    A surprise, my lady. That was the word used.

    Which is what I was told, and it is all I was told, and I have taken the money on the strength of it exactly as you have.
    """

    """
    We look at one another for a moment across a very expensive bedroom.

    Two people who have been hired out of an empty season by a man neither of us has met, to be somebody else in a house nobody lives in, for three days.

    When you say it out loud like that it does not sound like a joke at all.
    """

    butler """
    Get some sleep, my lady.

    You have a shoot in the morning, and you cannot shoot.
    """

    return
