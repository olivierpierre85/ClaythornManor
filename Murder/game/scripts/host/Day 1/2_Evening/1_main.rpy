# --------------------------------------------
#   Host
#
#   Friday - Evening
#
#   17:30 -> 00:30
#
#   Music: chill at dinner, upbeat for the house, mysterious for the debrief
#
#   Alive: Everyone
#
# --------------------------------------------
label host_day1_evening:

    call change_time(17, 30, 'Evening', 'Friday', hide_minutes=True, chapter='friday_evening')

    $ current_character.add_checkpoint("host_day1_evening")

    call black_screen_transition("Lady Claythorn", chapters_names[current_chapter])

    $ change_room('bedroom_host', dissolve)

    $ play_music('upbeat')

    """
    The afternoon went by fast.

    I learnt which door leads where, so that I never have to ask.

    I studied the names of the guests from a sheet of paper.

    Most of them must have arrived by now.

    I take a look in the mirror.

    And I see myself dressed in elegant clothes.

    The sort I am only accustomed to wearing onstage.

    That should help me remember that I am playing a role here.
    """

    play sound door_knock

    """
    Someone knocks on my door.
    """

    host """
    Come in!
    """

    butler """
    I come to see that everything is ready.

    Do you remember the etiquette?
    """

    host """
    Of course I do.
    """

    """
    I spent hours on a book about proper dinner table manners.

    As if the whole plot depended on it.
    """

    butler """
    Good, I also wrote the speech you are gonna give for dinner.
    
    Here it is.

    You should know it by heart by dinner.

    That would establish you without a doubt as the lady of the house.

    Do it well and they will not question who you are.

    Just pretend you are telling it to an audience in a theatre.
    """

    host """
    Very well.
    """

    """
    That, at least, I know how to do.
    """

    butler """
    One more thing. I have left a book out for you in the library.

    When you have the time, you should read the part about this place.

    That might be helpful.
    """

    """
    I nod, and he leaves without ceremony.

    So I start to memorise my lines.
    """

    call wait_screen_transition()

    play sound dinner_gong

    """
    The gong goes below.

    Curtain up.
    """

    call change_time(18, 30, 'Dinner', 'Friday')

    $ change_room('dining_room', irisout)

    $ play_music('chill', 2)

    """
    I come in last.

    Seven faces turn, and I take the long walk to my chair.

    I do not look at any of them until I reach my place.

    I let the silence sit half a beat longer than is comfortable, and I begin.
    """

    call common_day1_evening_host_welcome_speech

    """
    When I am done there is that warm shuffle round a table that means it landed.

    A few of them murmur their thanks.
    """

    call common_day1_evening_host_dinner_enjoy_meal

    """
    The first course comes in on the heels of it, and the room turns into a dinner party.

    My hands are shaking slightly under the cloth.

    But nobody can see them.

    The first act is over.

    I sit down and relax for a second.

    But I must start talking to the guests now.

    I remember that it matters who I address first.
    """

    $ time_left = 90

    call run_menu(TimedMenu("host_day1_evening_menu_dinner", [
        TimedMenuChoice('Turn to Mr Manning, on your left', 'host_day1_dinner_drunk', 20, next_menu = 'drunk_generic_menu_host'),
        TimedMenuChoice('Turn to Mr Moody, on your right', 'host_day1_dinner_broken', 90),
        TimedMenuChoice('Keep to yourself and see out the meal', 'generic_cancel', early_exit=True),
    ], image_left = "drunk", image_right = "broken"))

    $ stop_music()

    call change_time(21, 00)

    """
    The last plates go out, and it is up to me to call the end of dinner.
    """

    host """
    It looks as though everyone has finished their meal.

    I shall let you return to your rooms, then.

    Afterwards there will be drinks in the billiard room for anyone who cares to sit up a while.
    """

    """
    Chairs go back. The party moves off.

    And that is it for dinner.
    """

    $ change_room('bedroom_host', dissolve)

    """
    I go up first, because I need the door shut and regroup for a while.

    But not too long. 
    
    I am expected downstairs and not showing up would raise questions.

    But I do not need to reach the billiard room right away.

    What should I do?
    """

    $ play_music('upbeat')

    call change_time(21, 15)

    $ time_left = 90

    call run_menu(host_details.saved_variables["day1_evening_map_menu"])

    call change_time(23, 00)

    $ stop_music()

    if not host_details.threads.is_unlocked('stayed_with_guests'):

        """
        It has got rather late, so I head back to my room for the night.
        """

    $ change_room('bedroom_host', dissolve)

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
    He enters and immediately loses his air of obedience.
    """

    # TODO add picture not smiling? seriouS?

    python:
        host_debrief_fault_count = 0
        host_debrief_fault_index = 0

        if not host_details.threads.is_unlocked('addressed_manning_first'):
            host_debrief_fault_count += 1

        if host_details.threads.is_unlocked('go_downstairs'):
            host_debrief_fault_count += 1

        if not host_details.threads.is_unlocked('stayed_with_guests'):
            host_debrief_fault_count += 1

    if host_debrief_fault_count > 0:

        if host_debrief_fault_count == 1:

            butler """
            Well, the first day is gone, and better than I feared.

            There is one thing, though.
            """

            host """
            Oh? What was it?
            """

        else:
            
            butler """
            Well, the first day is gone, but I am afraid it was not without mistakes.
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
                Oh sorry, I forgot about that rule.

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

                It was making everyone uncomfortable.
                """

        if host_details.threads.is_unlocked('go_downstairs'):

            call host_day1_evening_debrief_next_fault

            butler """
            You went below stairs.
            """

            host """
            I wanted to see the house I am supposed to have grown up in.
            """

            butler """
            The mistress of a house does not go down to the servants' floor.

            She rings, and she waits, and they come up to her.
            """

            host """
            Nobody saw me.
            """

            butler """
            You cannot know that.

            There are seven people under this roof, and not one of them was where I expected them to be this evening.

            If one of them saw the lady of the house on the servants' stair, they will remember it.
            """

        if not host_details.threads.is_unlocked('stayed_with_guests'):

            call host_day1_evening_debrief_next_fault

            butler """
            You gave them drinks and did not come.

            They sat up until eleven waiting for their hostess to look in.
            """

            host """
            I needed an hour where nobody was looking at me.
            """

            butler """
            You will not get one. Not this weekend.
            """

        if host_debrief_fault_count == 1:

            butler """
            It is not fatal in itself. But it is the sort of small thing that sits badly with people, and they do not forget it.

            You should do better tomorrow.
            """

        else:

            butler """
            None of it is fatal on its own. But all put together and it might attract attention.

            You should do better tomorrow.
            """

        """
        He is right, which is the worst of it.

        I have been telling myself all evening that I got away with it, and he has stood in a corner keeping score.
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

    So I take the clothes off, and get ready for the next day.
    """

    jump host_day2_morning


# ------------------------------------
#   DEBRIEF — JOINING THE FAULTS UP
#   Called at the top of each fault block. The first one needs no lead-in,
#   because the opening line has already announced it.
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


# ------------------------------------
#   DINNER — MR MANNING (on her left)
#   The first turn of the head carries his verdict on the sole, which is the
#   whole of what she learns about him without asking a single question.
# ------------------------------------
label host_day1_dinner_drunk:


    $ host_details.threads.unlock('addressed_manning_first')

    # """
    # He has not touched his wine since the plates came in, which at this table makes him remarkable all on his own.
    # """

    # drunk """
    # The sole is poached, not boiled, and whoever made that sauce was in no hurry whatsoever.

    # Butter, cream, a little of the cooking liquor, and just enough lemon to keep the whole thing honest.

    # It has been worked at the side of the stove the best part of an hour. You cannot rush it. It splits if you do.

    # And the shallots in the beef were sweated, never fried. There is not a scorched edge anywhere on that plate.

    # host """
    # You know a great deal about a kitchen, Mr Manning.
    # """

    # """
    # And the instant I say it, he is drunk again.
    # """

    # drunk """
    # Do I.

    # My father kept a good table.

    # Very good. Very... good table.
    # """

    # $ drunk_details.description_hidden.unlock('food')

    call drunk_generic

    return


# ------------------------------------
#   DINNER — MR MOODY (on her right)
# ------------------------------------
label host_day1_dinner_broken:

    host """
    Mr Moody.
    """

    broken """
    Lady Claythorn.

    I must thank you again for your generosity.
    """

    host """
    No need, I am very happy to do it.

    But now I would like to know a little more about you.
    """

    broken """
    There is not much to tell, I am afraid.

    I spent my youth in service, boot boy and then footman, and after that I enlisted.

    Now I live quietly on my pension, in Liverpool.

    But I would far rather talk about you.
    """

    host """
    Of course, but ...
    """

    broken """
    This house is splendid, for instance.

    Has it been in your family long?
    """

    host """
    Well, yes ...
    """

    """
    He does not give me the chance to ask a single question of my own.

    And that is how it goes for the whole of dinner.

    I feel as though I am being interrogated, and I must be extremely careful not to give anything away.

    In the end, I do not manage to ask him a single question.
    """

    return
