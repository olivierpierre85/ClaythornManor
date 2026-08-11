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
#   Position
#       - Bedroom : the butler's last briefing before the curtain goes up
#       - Dining Room : everyone. Manning on her left, Moody on her right
#       - The house : free roam (library, gallery, below stairs, billiard room)
#       - Bedroom : the butler's debrief
#
#   Notes :
#       - Etiquette: a hostess turns to the guest on her left first. Doing it
#         correctly unlocks the addressed_manning_first thread, which is the
#         only way that thread is ever unlocked. Turning to Moody first, or
#         sitting through dinner in silence, leaves it locked and costs her a
#         mark at the debrief, as does never joining the party.
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

    He leaves without ceremony, and I start memorize my lines.
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

    I do not look at any of them until I reach my chair.

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
        TimedMenuChoice('Turn to Mr Manning, on your left', 'host_day1_dinner_drunk', 0, keep_alive = True, next_menu = 'drunk_generic_menu_host'),
        TimedMenuChoice('Turn to Mr Moody, on your right', 'host_day1_dinner_broken', 0, keep_alive = True, next_menu = 'broken_generic_menu_host'),
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
    Chairs go back. The party moves off in twos and threes.

    And that is dinner survived.
    """

    $ change_room('bedroom_host', dissolve)

    """
    I go up first, because I need the door shut and thirty seconds of not being looked at.

    I sit on the end of the bed in eighty pounds of somebody else's clothes and let my face come off.

    Thirty seconds. That is what I allow myself.

    Then I stand up, because there is a great deal in this house I have not seen, and this is the only hour I shall have to myself.

    They are all in the billiard room, the staff are run off their feet, and nobody in the world knows where I am.
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

    if not host_details.saved_variables['day1_evening_manning_spoken']:

        $ host_details.saved_variables['day1_evening_manning_spoken'] = True

        # TODO rewrite Something about food with unlock? But may not be necessary sort out later.

        # """
        # He has not touched his wine since the plates came in, which at this table makes him remarkable all on his own.
        # """

        # drunk """
        # The sole is poached, not boiled, and whoever made that sauce was in no hurry whatsoever.

        # Butter, cream, a little of the cooking liquor, and just enough lemon to keep the whole thing honest.

        # It has been worked at the side of the stove the best part of an hour. You cannot rush it. It splits if you do.

        # And the shallots in the beef were sweated, never fried. There is not a scorched edge anywhere on that plate.

        # Whoever you have in that kitchen is a serious person, Lady Claythorn.

        # I should like to shake their hand.
        # """

        # """
        # Not one slurred word in the whole of it.

        # Not one.

        # I have spent fifteen years watching people pretend, and I know what I have just seen.

        # He was in character a moment ago, and for the length of that sauce he stepped out of it.
        # """

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

        # """
        # The hand goes back round the glass. The eyes go soft. The vowels come apart.

        # It is a decent performance. Better than decent.

        # But I have known actors sober up for a matinee and be legless again by six, and this is not that.

        # This is a man who has learnt that nobody asks a drunk anything difficult.

        # So he stays one.

        # I ought to admire it. Instead it makes me cold.

        # Because if he is playing a part at this table, then he has as much reason to hide as I have.
        # """

        # $ drunk_details.description_hidden.unlock('food')

        # $ drunk_details.description_hidden.unlock('status')

        # $ drunk_details.description_hidden.unlock('lie')

        # $ host_details.threads.unlock('manning_act')

    else:

        """
        I turn back to my Mr Moody.
        """

    call drunk_generic

    return


# ------------------------------------
#   His verdict on the sole. He is not asked for it, and it is the one thing
#   at this table that is said stone cold sober.
# ------------------------------------
label host_day1_dinner_drunk_food:



    return


# ------------------------------------
#   DINNER — MR MOODY (on her right)
#   Going to him first is a breach of the order of things, and of all the men
#   at this table he is the one who was raised below stairs and knows it.
# ------------------------------------
label host_day1_dinner_broken:

    call broken_generic

    return


label host_day1_dinner_broken_tradition:

    host """
    It is my father's doing, really.

    He began it years ago and I have simply kept it up. One does not like to let a thing lapse.

    The sum has changed, and the number of recipients. But the award itself is quite an old tradition in this house.
    """

    """
    It comes out beautifully. Warm, faintly bored, the small self-deprecating turn at the end.

    I could not have written it better, which is fortunate, because I did not write it.

    And Mr Moody says, oh, how splendid, and asks me the name of it, and I give him that too.

    Then he says nothing at all for a moment.
    """

    broken """
    How splendid. And under that same name all along?
    """

    host """
    I believe so, yes.
    """

    """
    He smiles, agrees that it is a fine thing, and turns his attention to his plate.

    And I know, with a certainty I cannot explain and cannot ignore, that I have just told a lie to the one man at this table who had already looked it up.

    An old tradition in a great house is a matter of record. Somebody writes those things down.

    He asked me a question he knew the answer to.

    That is not what a guest does. That is what a policeman does, or a journalist.
    """

    $ host_details.saved_variables['day1_evening_told_tradition'] = True


    return


label host_day1_dinner_broken_vague:

    host """
    It came about because it could, Mr Moody.

    I have the means and very little occasion out here to put them to any decent use.

    I am afraid that is the whole of the mystery.
    """

    broken """
    A pity. I had hoped for a better story than that.
    """

    host """
    So had I. One never gets one.
    """

    """
    He laughs, which is a good sign, and lets it go, which is a better one.

    Nothing offered, nothing to check, nothing to write down.

    Say less. It is the first thing you learn and the last thing you remember.
    """

    return


# Turning the question back on him is her "tell me about yourself" question by
# another road, so it runs the same scene and that choice then drops out of
# broken_generic_menu_host.
label host_day1_dinner_broken_deflect:

    host """
    You have a great many questions for a man who has not told me a thing about himself.

    That is hardly fair, Mr Moody. Your turn.
    """

    call broken_generic_background_host

    return
