# --------------------------------------------
#   Drunk
#
#   Friday - Evening
#
#   18:30 -> 23:00
#
#   Music: chill at dinner, upbeat for the billiard room, scary for the letter
#
#   Position
#       - Dining Room : Everyone (he sits on Lady Claythorn's left, Miss Marsh
#         below him, the boy across the table)
#       - Billiard Room : the party, after dinner
#       - Bedroom Drunk : the letter
#
#   Notes :
#       - The dinner is a string of things half seen through the drink, and
#         one thing seen whole: the sole. Everything he half sees comes back
#         on the Saturday night, behind the locked door.
#       - The billiard room is the one thing he can do before his room. He
#         gets there before the others and carries off every bottle worth the
#         name, which is why the party finds only sherry and port on the tray
#         (raided_bar, port). The port is what his blood is made of on Sunday.
#       - The letter is on the desk. He writes the second part in both
#         branches, so that the doctor may find it that night. Then he
#         drinks (day1_drink) or he does not. Putting the bottle down is an
#         intuition, earned by dying drunk in the woods (despair).
#
#   Unlocks : drunk 'food', 'wife' - doctor 'fraud'
# --------------------------------------------
label drunk_day1_evening:

    call change_time(18, 30, 'Dinner', 'Friday', hide_minutes=True, chapter='friday_evening')

    $ drunk_details.add_checkpoint("drunk_day1_evening")

    call black_screen_transition("Samuel Manning", chapters_names[current_chapter])

    $ drunk_mode = True

    $ change_room('tea_room', irisout)

    show layer master at drunk_wobble_layer

    play sound dinner_gong

    """
    Something is hitting a gong.

    Or somebody is hitting me. Same thing, at this hour.

    The sofa. The fire. The room has filled up while I was away: a boy in a bad suit, the hat, the mask, the thin woman, the straight man still talking.

    The butler is saying dinner.

    Dinner I can do. I have never in my life missed a dinner.
    """

    $ change_room('dining_room', irisout)

    $ play_music('chill', 2)

    """
    A card with my name on it.

    They have put me next to the head of the table, on the left, with the thin woman below me and the boy in the bad suit across.

    Somebody has a sense of humour, or a very short list.

    Then a chair goes back at the top of the room, and everybody stands, so I stand.
    """

    """
    Lady Claythorn.

    Younger than the name. Handsome. A dress that cost more than my chambers.

    She looks down the table at the lot of us the way a woman looks at a hand of cards she has been dealt and means to play anyway.

    Then she speaks.
    """

    call common_day1_evening_host_welcome_speech

    """
    It is a good speech.

    It is a very good speech, and I have heard a great many, and there is something in it that I cannot put my finger on at this hour.

    The pauses. The pauses are in the wrong places.

    A woman talking about her own house does not pause where the breath goes. She pauses where the sense goes.

    This one breathes.
    """

    """
    A thousand pounds, she says, and I stop listening to the pauses.
    """

    call common_day1_evening_host_dinner_enjoy_meal

    $ drunk_details.saved_variables["day1_drinks"] += 1

    """
    Wine.

    A footman fills my glass from the left, as he should, and I pick it up by the bowl because my hand has forgotten where the stem is.

    The straight man across the table sees me do it. I see him see it.

    A man like that keeps a ledger.
    """

    call change_time(19, 00)

    """
    Then the fish comes in, and the evening stops.
    """

    call drunk_day1_dinner_sole

    """
    I put the fork down.

    Lady Claythorn is looking at me.

    She has turned to me first, as she ought, and she is looking at me the way the driver looked at the road.
    """

    drunk """
    Whoever poached that sole was in no hurry.

    The sauce has been an hour at the side of the stove. It splits if you rush it, and it has not split.
    """

    """
    It comes out whole. Every word in its place.

    It is the first whole thing I have said since Carlisle, and she hears it, and something in her face changes.

    So I let my hand go slack on the glass and I say something about the weather, and I say it badly.

    It is easier. People stop looking.
    """

    $ drunk_details.description_hidden.unlock('food')

    call drunk_day1_dinner_glimpses

    call change_time(21, 00)

    $ stop_music()

    """
    The last plate goes out.

    Lady Claythorn says something about the billiard room and drinks, and chairs go back all along the table.

    Drinks.

    In a house this size there will be a sideboard, and on it there will be everything the tray in the tea room was not.
    """

    $ time_left = 1
    call run_menu(TimedMenu("drunk_day1_evening_menu_after_dinner", [
        TimedMenuChoice('Get to the billiard room before the others do', 'drunk_day1_evening_billiard_room', early_exit=True),
        TimedMenuChoice('Go straight up to your room', 'drunk_day1_evening_go_up', early_exit=True),
    ]))

    call drunk_day1_evening_letter

    jump drunk_day2_morning


# ------------------------------------
#   The sole. The one clear thing in the evening.
# ------------------------------------
label drunk_day1_dinner_sole:

    """
    Sole.

    Poached, not boiled. There is a difference and most kitchens do not know it. This one does.

    Butter and cream and a little of the liquor the fish was cooked in, and lemon, just enough to keep the whole thing honest.

    Somebody stood at the side of a stove for the best part of an hour with a spoon and did not once walk away from it.

    I know, because my father's cook did, and I stood beside her on a stool and watched.

    I take a second mouthful, and a third, and for the length of that plate I am not drunk at all.

    I am nine years old in a kitchen in Gloucestershire, and nothing has happened yet.
    """

    return


# ------------------------------------
#   The rest of dinner. Things half seen, filed without knowing it.
#   Every one of them comes back on Saturday night.
# ------------------------------------
label drunk_day1_dinner_glimpses:

    call change_time(19, 30)

    """
    The beef comes. The shallots have been sweated and never fried, and I say nothing about them to anybody.

    The butler serves it.

    He serves from the left, at the right height, and he does not hurry, and his knuckles are the wrong shape.

    A butler carries trays. Those hands have carried something heavier, and put it down on somebody.
    """

    """
    Across the table, the hat is talking to the boy.

    She is not talking to the straight man, who is on her other side and ought to have had her first. He knows it. He is keeping his ledger.

    She looks at the boy while he answers her the way Eleanor used to look at other people's children in the park.

    Counting his fingers.
    """

    """
    The grey man in spectacles has not touched his napkin.

    He has touched his forehead, though, four times since the fish, with a handkerchief that is already damp.

    A doctor, somebody said. I know that sweat. I have seen it in the mirror at eleven in the morning.
    """

    """
    The mask does not drink the wine.

    He drinks from a flask, under the table, when he thinks the butler is not looking.

    The butler is always looking.
    """

    """
    And beside me the thin woman says the food is very good, twice, and moves it about her plate, and eats none of it.

    Nurse, somebody said. Nurses eat. I have never met one that did not.
    """

    call change_time(20, 30)

    """
    I drink the wine. All of it. The footman fills it again and I drink that too, and the room goes back to being kind.
    """

    $ drunk_details.saved_variables["day1_drinks"] += 1

    return


# ------------------------------------
#   BILLIARD ROOM. He takes everything worth the name.
#   -> raided_bar, port
# ------------------------------------
label drunk_day1_evening_billiard_room:

    $ change_room('billiard_room')

    $ play_music('upbeat')

    """
    I am the first through the door.

    I have never in my life waited for a lady to rise, and I did not start tonight.

    There it is.

    A sideboard, and on it a tray, and on the tray what I knew would be there.

    Whisky. A brandy with a good label. Gin, for some reason. Two decanters, sherry and port. And behind them, unopened, a bottle of port with dust on the shoulders.
    """

    """
    I look at the door. Nobody yet.

    A man who takes one glass is a guest. A man who takes the bottle is a drunk, and they will know that about me by breakfast anyway.

    So I take the whisky under one arm and the brandy under the other, and the gin goes in the coat, and the bottle of port goes in the other side of the coat because it is there and I am a man who takes what is there.

    I leave them the decanters.

    Sherry is for aunts, and port is for after dinner, and I have not sat down to a dinner in five years.
    """

    $ drunk_details.threads.unlock('raided_bar')
    $ drunk_details.objects.unlock('port')

    """
    The butler is in the doorway when I turn round.

    He looks at what I am carrying.

    He looks at me.

    He says nothing at all, and he steps aside to let me by.
    """

    """
    A butler says something to that.

    A butler says 'allow me, sir', and takes two of the bottles, and has them sent up, and tells her ladyship in the morning.

    This one lets me pass with the house's whisky under my arms like a man watching a dog carry off a bone he meant to give it.
    """

    $ change_room('bedrooms_hallway', dissolve)

    """
    I get up the stairs. I could not tell you how.

    A door with a king on it. George the Fourth.

    Somebody has a sense of humour.
    """

    return


# ------------------------------------
#   Straight up. Nothing taken.
# ------------------------------------
label drunk_day1_evening_go_up:

    $ change_room('bedrooms_hallway')

    $ play_music('upbeat')

    """
    No.

    I have had enough for one day, which is a sentence I say most days, and mean about one day in ten.

    The footman shows me up. A door with a king on it. George the Fourth.

    Somebody has a sense of humour.
    """

    return


# ------------------------------------
#   THE LETTER
# ------------------------------------
label drunk_day1_evening_letter:

    call change_time(21, 30)

    $ change_room('bedroom_drunk', dissolve)

    """
    The room is big and cold and somebody has unpacked my bag, which will have told them everything about me that the tea room did not.

    I sit on the bed to get my boots off.

    Then I see the desk.

    There is a letter on it, and it is not mine, and it has my name on it.
    """

    $ stop_music(2)

    $ play_music('scary')

    """
    A fine hand. A woman's, or a clerk's who was taught by a woman.

    I read it standing up.
    """

    call drunk_letter_first_part

    """
    I read it again sitting down.

    Eleanor.

    Nobody in this house should know that name. Nobody in this house should know there was a hospital, or a doctor, or a bed with a screen round it, or five years since.

    But somebody knows all of it, and they know which doctor, and they have put him at the same table as me and left a note on my desk to make sure I did not miss him.

    The grey man in spectacles. The one with the damp forehead.

    Withholding of medication for his own benefit.

    I know that sweat.
    """

    $ drunk_details.description_hidden.unlock('wife')
    $ doctor_details.description_hidden.unlock('fraud')

    """
    I have stood up in a great many courtrooms, and I have never once seen a man convicted on an unsigned letter.

    I have seen a great many men hanged on less.
    """

    """
    There is a pen on the desk.

    I do not remember picking it up, and I do not remember what I meant to write, but there is ink on the page under the fine hand now, and the hand that put it there is mine.
    """

    call drunk_letter_second_part

    """
    It is not a lawyer's hand. It is the hand of a man who has been drinking since Carlisle.

    I look at it for a long time.
    """

    """
    Now.

    Here is where I am. A locked door I could lock, a bed, a letter, and a bottle.
    """

    if drunk_details.threads.is_unlocked('raided_bar'):

        """
        Four bottles, in fact. They are standing on the washstand in a row like witnesses.
        """

    else:

        """
        One bottle, in the bottom of the bag, where I always keep one, because I always keep one.
        """

    """
    I know what I do with a night like this. I have done it three hundred times.

    I drink until the letter is a piece of paper, and I wake up, and it is a piece of paper, and the man who wrote on it is somebody else.
    """

    $ time_left = 1
    call run_menu(TimedMenu("drunk_day1_evening_menu_letter", [
        TimedMenuChoice('Drink until it goes away', 'drunk_day1_evening_letter_drink', early_exit=True),
        TimedMenuChoice('Put the bottle down, and think{{intuition}}', 'drunk_day1_evening_letter_sober', early_exit=True, condition="drunk_details.endings.is_unlocked('despair')"),
    ]))

    call change_time(23, 00)

    $ stop_music()

    return


# ------------------------------------
#   He drinks. -> day1_drink
# ------------------------------------
label drunk_day1_evening_letter_drink:

    $ drunk_details.threads.unlock('day1_drink')

    $ drunk_details.saved_variables["day1_drinks"] += 1

    """
    I do what I do.

    The first one is for Eleanor. The second one is for the doctor, and I mean something by it, and by the third I could not tell you what.

    The letter is on the desk, and then it is on the floor, and then I cannot see the desk.

    The bed comes up the way the gravel did.
    """

    show layer master at drunk_wobble_layer
    $ drunk_mode = True

    scene black_background with dissolve

    pause 1.5

    return


# ------------------------------------
#   He does not. The letter did what a night's sleep never does.
# ------------------------------------
label drunk_day1_evening_letter_sober:

    """
    No.

    I put the bottle down, and I put the cork in it, and I put it on the far side of the room where I would have to get up to reach it.

    I have not done that in five years.

    It is Eleanor's name that does it. Not the doctor. Her.

    Somebody in this house has been through my life with a lamp, and they know where the bodies are, and they have picked one out and handed me the spade.

    A man who is drunk does what he is handed.

    I am not going to be handed anything tonight.
    """

    $ drunk_mode = False

    $ change_room('bedroom_drunk')

    """
    The room stops moving. It takes an hour, but it stops.

    I sit at the desk with the letter and I read it the way I used to read a brief, before the drink, when I was somebody.

    Whoever wrote the first part is educated, and a woman, and angry in a way that has had years to go cold.

    Whoever wrote the first part knows what he is. Not thinks. Knows.

    And whoever wrote it wants me to do something about him, and does not want to be seen doing it themselves.
    """

    """
    Very well.

    Tomorrow they will get a drunk. They have already had one all day, and they were pleased with him.

    A drunk is not watched. A drunk is not asked. A drunk can stand three feet from a man and look him in the face and nobody wonders why.

    And if it is him, I will know it. Eleanor's doctor had a way of standing at the foot of a bed. A man does not forget that.
    """

    """
    I lie down in my clothes, sober, in a strange house, and I sleep like a child.

    That has not happened in five years either.
    """

    scene black_background with dissolve

    pause 1.5

    return
