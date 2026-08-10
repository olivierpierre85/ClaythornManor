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
#       - Etiquette: a hostess turns to the guest on her left first. Turning to
#         Moody first, or sitting through dinner in silence, costs a mark
#         (day1_evening_suspicious_acting), as does never joining the party.
#       - Marks are settled by the butler at the end of the night. Any mark at
#         all unlocks the suspicious_acting thread.
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
    The placement. Learn it now, because you will not have it in your hand at the table.

    Mr Manning is on your left. Mr Moody on your right.

    Do you remember the etiquette?
    """

    host """
    Of course I do.
    """

    """
    He spent hours teaching me proper dinner table manners.

    As if the whole plot depended on it.
    """

    host """
    And the speech?
    """

    butler """
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

    $ stop_music()

    play sound dinner_gong

    """
    The gong goes below.

    It is time to play my part.

    Curtain up.
    """

    call change_time(18, 30, 'Dinner', 'Friday')

    $ change_room('dining_room', irisout)

    $ play_music('chill', 2)

    """
    I come in last.

    Seven faces turn, and I take the long walk to my chair.

    I do not look at any of them until I am seated. Then I look at all of them.

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

    But only a second, because I must start talking to the guests now.

    I remember that it matters who I turn to first.
    """

    $ time_left = 90

    call run_menu(TimedMenu("host_day1_evening_menu_dinner", [
        TimedMenuChoice('Turn to Mr Manning, on your left', 'host_day1_dinner_drunk', 0, keep_alive = True, next_menu = 'drunk_generic_menu_host'),
        TimedMenuChoice('Turn to Mr Moody, on your right', 'host_day1_dinner_broken', 0, next_menu = 'host_day1_dinner_broken_menu'),
        TimedMenuChoice('Keep to yourself and see out the meal', 'generic_cancel', early_exit=True),
    ], image_left = "drunk", image_right = "broken"))

    if not host_details.saved_variables['day1_evening_dinner_first_guest']:

        $ host_details.saved_variables['day1_evening_suspicious_acting'] += 1

        """
        And so I sit through the whole of my own dinner saying nothing to the men on either side of me.

        A shy woman may do that. A nervous one may do that.

        The mistress of a house may not, because a table is hers to run, and a table that runs itself has no mistress.

        Miss Marsh looks up at me twice from the far end, and the second time she does not look away quickly.
        """

    $ stop_music()

    call change_time(21, 00)

    """
    The last plates go out, the covers come off, and I say the sentence I have been holding all evening.
    """

    host """
    There will be drinks in the billiard room for anyone who cares to sit up a while.

    Please do not feel obliged. It has been a long day for all of you.
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

        $ host_details.saved_variables['day1_evening_suspicious_acting'] += 1

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
# ------------------------------------
label host_day1_dinner_drunk:

    if not host_details.saved_variables['day1_evening_dinner_first_guest']:

        $ host_details.saved_variables['day1_evening_dinner_first_guest'] = 'drunk'

        """
        Left first. I turn to my left.
        """

    else:

        """
        I turn back to my left.
        """

    call drunk_generic

    return


# ------------------------------------
#   DINNER — MR MOODY (on her right)
#   Going to him first is a breach of the order of things, and of all the men
#   at this table he is the one who was raised below stairs and knows it.
# ------------------------------------
label host_day1_dinner_broken:

    if not host_details.saved_variables['day1_evening_dinner_first_guest']:

        $ host_details.saved_variables['day1_evening_dinner_first_guest'] = 'broken'

        $ host_details.saved_variables['day1_evening_suspicious_acting'] += 1

        """
        I turn to my right, because he has been watching me since I came in and I would rather have him where I can see him.

        I am three words into the pleasantry before I remember.

        Left first.

        He said left first, and I have gone straight past Mr Manning as though the man were furniture.

        Mr Moody's head tilts a quarter of an inch.

        That is all. A quarter of an inch, and it goes through me like cold water, because it is not the movement of a man who has noticed nothing.
        """

    else:

        """
        The plates change, and I turn to my right as I ought.
        """

    broken """
    Lady Claythorn.

    A remarkable speech, if I may say so.
    """

    host """
    You may, Mr Moody. It is a good deal easier to give away money than to earn it.
    """

    broken """
    Easier, certainly.

    Rarer, though.

    Forgive me, but I confess the whole business puzzles me a little.

    An award of this size, given quietly, out here, to seven people who have never met.

    However did it come about?
    """

    """
    And there it is, over the fish, in the pleasantest voice in the room.

    He is not making conversation. That was a question with a shape to it.
    """

    call run_menu(host_day1_dinner_broken_menu)

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

    $ host_details.saved_variables['day1_evening_suspicious_acting'] += 1

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


label host_day1_dinner_broken_deflect:

    host """
    You have a great many questions for a man who has not told me a thing about himself.

    That is hardly fair, Mr Moody. Your turn.
    """

    broken """
    There is very little to tell, I am afraid.

    I mend motor cars in Liverpool. I have done since the war.
    """

    host """
    And before the war?
    """

    broken """
    Before the war I was in service, my lady.

    Boot boy, then footman, in a house not unlike this one.
    """

    $ broken_details.description_hidden.unlock('job')

    $ broken_details.description_hidden.unlock('city')

    $ broken_details.description_hidden.unlock('background')

    """
    Well.

    That accounts for the quarter of an inch.

    He has stood at the wall through a hundred dinners exactly like this one, and there is not a thing I do at this table that he has not watched a real one do first.

    Of all the people to seat on my right.
    """

    host """
    Then you must tell me if my staff go wrong. You will see it long before I do.
    """

    broken """
    They have gone wrong twice already.

    But since you are good enough to ask, my lady, I shall say nothing about either.
    """

    """
    He says it lightly, as a joke against my footmen.

    I laugh, because it is expected, and because the alternative is to ask him which two things, and I cannot possibly ask him which two things.
    """

    return
