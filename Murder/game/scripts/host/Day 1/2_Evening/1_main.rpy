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
    They have all arrived. I have heard every one of them come in without setting eyes on a single one.

    The car on the gravel, the door, the butler's voice going smoothly through the same speech again and again, and me at the top of the house being kept out of sight like a surprise.

    Which, I suppose, is what I am.

    The afternoon went on tasks. Learning which door leads where, so that I never have to ask. Learning the names of my own guests off a sheet of paper.

    And now I am dressed in eighty pounds of somebody else's clothes, looking at a woman in the glass whom I have never met.

    Not bad. Not bad at all.

    The hair is wrong for my face and exactly right for hers.
    """

    play sound door_knock

    """
    Two knocks. Always two.
    """

    butler """
    May I come in, my lady?
    """

    host """
    There is nobody in the corridor, is there.
    """

    butler """
    There is always somebody in the corridor.
    """

    """
    He comes in with a sheet of paper and that maddening calm of his, and I want to throw something at him and thank him at the same time.
    """

    butler """
    The placement. Learn it now, because you will not have it in your hand at the table.

    Mr Manning is on your left. Mr Moody on your right. The others as written.

    You will turn to your left first, then to your right when the plates change. A hostess who takes them out of order tells the whole table she was not raised to it.

    You do not eat much, you do not drink at all, and you keep the conversation moving round you rather than at you.
    """

    """
    I run my eye down the list. Seven guests, seven rooms, and beside each name a line or two in his handwriting.

    Where they come from. What they do. What each of them is supposed to have done to deserve a thousand pounds.

    Whoever put this weekend together knows a great deal about the people coming up my stairs tonight.
    """

    $ unlock_map('bedroom_lad')

    $ unlock_map('bedroom_doctor')

    $ unlock_map('bedroom_captain')

    $ unlock_map('bedroom_psychic')

    $ unlock_map('bedroom_host')

    $ unlock_map('bedroom_drunk')

    $ unlock_map('bedroom_broken')

    $ unlock_map('bedroom_nurse')

    host """
    And the speech?
    """

    butler """
    Word for word, as written.

    Do not improve it.
    """

    host """
    It could stand a little improving.
    """

    butler """
    So could most things.

    My lady. In an hour a great deal will depend on seven people believing you without being asked to.

    Say it as you would say it to a house of nine hundred who have paid to be there.
    """

    """
    Well.

    That, at least, I know how to do.
    """

    $ stop_music()

    play sound dinner_gong

    """
    The gong goes below, and every nerve I have goes with it.

    Curtain up.
    """

    call change_time(18, 30, 'Dinner', 'Friday')

    $ change_room('dining_room', irisout)

    $ play_music('chill', 2)

    """
    I come in last, because that is the only entrance worth making.

    Seven faces turn, and I take the long walk to my chair with my chin at the angle I have been practising in a cold room in Camden for a fortnight.

    Nobody stands up quickly enough, which means nobody is quite certain how grand I am. Good. Let them work it out.

    I do not look at any of them until I am seated. Then I look at all of them.

    An old soldier, very upright. A doctor with a glass already half down. A young man in a suit that is not his.

    A woman in mourning colours who has done her own hair. A masked man on my right, who has not stopped watching me since I came through the door.

    My audience.

    I let the silence sit half a beat longer than is comfortable, the way you do when a house is still coughing, and I begin.
    """

    call common_day1_evening_host_welcome_speech

    """
    I take them slowly. I give them the pause before the money, because a pause before money is worth more than the money.

    And I keep my hands still, which is the hardest part of the whole performance.

    When I sit down there is that warm shuffle round a table that means it landed.

    A few of them murmur their thanks.
    """

    call common_day1_evening_host_dinner_enjoy_meal

    """
    The first course comes in on the heels of it, and the room turns into a dinner party.

    My hands are shaking under the cloth. Nobody can see them. That is all that matters.
    """

    pause 1.0

    call change_time(19, 00)

    """
    On my left, Mr Manning has already emptied his glass and is watching the footman's progress round the table with an air of quiet mathematics.

    When the wine reaches him he does not lift the glass so much as meet it.

    He has done that a great many times, and not one person at this table is surprised by it.
    """

    $ drunk_details.description_hidden.unlock('addict')

    """
    On my right, Mr Moody sits behind a mask of painted tin, cut and coloured to stand in for the face the war took off him.

    I have seen them in the street and looked away like everybody else. It is a different thing entirely to have one turned towards you over the soup.

    I make myself hold his eye rather than the mask, which he notices, and which I meant him to notice.
    """

    $ broken_details.description_hidden.unlock('mask')

    """
    Two neighbours, then. Two hours of it.

    And a very great deal depends on which of them I turn to first.
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
