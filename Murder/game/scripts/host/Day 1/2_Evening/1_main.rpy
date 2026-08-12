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

    $ time_left = 120

    call run_menu(host_details.saved_variables["day1_evening_map_menu"])

    call change_time(23, 00)

    $ stop_music()

    if not host_details.saved_variables['day1_evening_billiard_room_visited']:

        """
        Somewhere below, the last of them are going up to bed.

        I never went near the billiard room.

        A hostess who gives a party and then puts herself away for the evening is a hostess with something the matter with her.

        They will have noticed. People always notice the chair that stays empty.
        """

    $ change_room('bedroom_host', dissolve)

    """
    The house goes quiet by degrees. Doors, water in the pipes, the last of the footsteps on the landing.

    I take the clothes off, and the woman in the glass goes with them.

    One day of three.
    """

    jump host_day1_evening_debrief


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
