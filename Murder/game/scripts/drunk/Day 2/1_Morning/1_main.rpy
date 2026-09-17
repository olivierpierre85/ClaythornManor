# --------------------------------------------
#   Drunk
#
#   Saturday - Morning
#
#   07:30 -> 10:45
#
#   Music: mysterious in the room, scary for the announcement, upbeat for the hunt
#
#   Position
#       - Bedroom Drunk : drunk
#       - Dining Room : Everyone but Thomas Moody, found dead in his bed
#       - Gun Room : the men, taking their rifles
#
#   Notes :
#       - Two mornings. If he drank the night away (day1_drink) he wakes
#         with no memory of the letter, reads it as new, finds his own hand
#         on it, and fills the flask because his hands will not hold a rifle
#         without it. If he read it sober he wakes clear for the first time
#         in years and decides what goes in the flask (watered_flask).
#       - The letter is burned in both mornings, which is the burned letter
#         the boy and the doctor find in his grate.
#       - Breakfast is the shared Saturday morning: the whisper, the
#         doctor fetched, the news of Mr Moody, the hunt.
#       - The stammer in his 'I'll come too' is real in one morning and put
#         on in the other.
#
#   Unlocks : drunk 'lie'
# --------------------------------------------
label drunk_day2_morning:

    call change_time(7, 30, 'Morning', 'Saturday', hide_minutes = True, chapter='saturday_morning')

    $ drunk_details.add_checkpoint("drunk_day2_morning")

    call black_screen_transition("Samuel Manning", chapters_names[current_chapter])

    $ change_room('bedroom_drunk', irisout)

    $ play_music('mysterious', 2)

    if drunk_details.threads.is_unlocked('day1_drink'):

        call drunk_day2_morning_hungover

    else:

        call drunk_day2_morning_clear

    call change_time(9, 15)

    $ change_room('dining_room', dissolve)

    """
    Everybody is there before me. They always are.

    A buffet along the wall, and the smell of coffee and fried bread, and seven heads that turn and turn back.
    """

    if drunk_details.threads.is_unlocked('day1_drink'):

        """
        I get to the buffet. The spoon for the eggs will not stay in my hand. I pick it up twice.

        Coffee. Black. I get that to a chair without losing it, which is the morning's achievement.
        """

    else:

        """
        I go to the buffet like a man crossing a deck in weather.

        I pick up the spoon for the eggs and I let it go, and pick it up and let it go, and the second time I hear the hat say something to the boy across the room with 'dreadful' in it.

        Good.

        Coffee, black, both hands round the cup, into the nearest chair. Curtain.
        """

    """
    The mask is not here.

    Everybody else is. The straight man eating like a soldier, the grey doctor not eating, the thin woman with her tea, the hat, the boy, her ladyship at the top.

    But the mask is not here, and I notice it, and I notice the butler noticing it.
    """

    """
    Then he goes to her ladyship and bends to her ear.

    I cannot hear it. I can see it. Her face does a thing that faces do in the dock when the verdict is not the one they were promised.

    She gets up and crosses the room, and stops beside the doctor.
    """

    call common_day2_morning_host_to_doctor

    """
    The three of them go out. The boy goes after them, for no reason I can see.

    The room does what rooms do when nobody knows anything. It eats, slowly, and it does not talk.
    """

    call change_time(10, 00)

    call common_day2_morning_host_death

    if drunk_details.threads.is_unlocked('day1_drink'):

        """
        Dead.

        The mask. The one man in the house who might have understood a word I said last night, if I had said any.

        I put the coffee down before I drop it.
        """

    else:

        """
        Dead in his sleep.

        A man who drank from his own flask under the table, and would not touch the house's wine.

        I keep my hands round the cup and my face where it was.
        """

    call common_day2_morning_host_death_doctor

    if not drunk_details.threads.is_unlocked('day1_drink'):

        """
        An old wound from the war.

        Seven years old, and it picks a Friday night in a strange house to finish him.

        I have heard doctors say things like that from the witness box. Juries like them. They like a reason that asks nothing of anybody.
        """

    call change_time(10, 15)

    $ stop_music()

    """
    Then her ladyship stands up again, and it is the speech voice.
    """

    call common_day2_morning_host_hunt

    if drunk_details.threads.is_unlocked('day1_drink'):

        """
        A hunt.

        Guns, and the open air, and a flask in my pocket.

        I hear myself agreeing before I have decided to.
        """

    else:

        """
        A hunt.

        Guns.

        Somebody has just handed a drunk a rifle and pointed him at a wood with a doctor in it, and called it an activity.

        I let the stammer in before I answer. It is a good one. I have had years to work on it.
        """

    call common_day2_morning_hunt_captain_drunk

    """
    A few eyebrows go up round the table. Nobody says anything.

    Nobody ever does. That is the whole trick of it.
    """

    call common_day2_morning_hunt_psychic

    """
    The hat will not come. Her ladyship asks the thin woman.
    """

    call common_day2_morning_hunt_nurse

    call common_day2_morning_hunt_lad

    call common_day2_morning_hunt_host_to_doctor

    """
    The room turns to the doctor, and so do I, and I make sure I am the last to.
    """

    call doctor_day2_hunt_choice

    if not drunk_details.threads.is_unlocked('day1_drink'):

        """
        He is coming.

        Of course he is coming. He has been told to, in that voice, and he has not the spine to say no to it.

        Neither have I. That is the one thing he and I have in common, and by this afternoon I shall know whether there is another.
        """

    call common_day2_morning_hunt_end

    call change_time(10, 30)

    $ change_room('gun_room', dissolve)

    $ play_music('upbeat')

    """
    Sporting guns behind glass, and the butler taking them out one at a time and handing them round like hymn books.

    He comes to me last.
    """

    butler """
    Here is yours, sir.

    You have handled one of these before?
    """

    drunk """
    In my youth.
    """

    butler """
    Very good, sir.
    """

    if drunk_details.threads.is_unlocked('day1_drink'):

        """
        It is heavier than I remember. Everything is.
        """

    else:

        """
        Very good, sir.

        He has watched me drop a spoon twice this morning, and he puts a loaded rifle in my hands and says very good, sir.

        I do not think this man cares very much who gets shot today. I think he only needs somebody to be holding the gun when it happens.

        I let it hang from my hand like something I have found.
        """

    jump drunk_day2_hunt


# ------------------------------------
#   He drank. He remembers nothing, and the letter is new.
# ------------------------------------
label drunk_day2_morning_hungover:

    show layer master at drunk_wobble_layer
    $ drunk_mode = True

    """
    Light.

    A room. Not mine. A ceiling with plaster fruit on it, and a bed I am on top of, not in, with my boots on.

    A house. A lady. A thousand pounds. It comes back in that order, and the rest does not come back at all.
    """

    if drunk_details.threads.is_unlocked('raided_bar'):

        """
        There are bottles on the washstand. Four of them, or three. One is on its side.

        I did that. I do not remember doing it, but nobody else in this house would have.
        """

    """
    There is a letter on the desk.

    I go to it, because there is nothing else in the room to go to.
    """

    call drunk_letter_first_part

    """
    Eleanor.

    Somebody in this house knows about Eleanor.

    I have to sit down, and the chair is not where I thought it was, and I sit on the floor instead.

    Then I see the rest of it, under the fine hand, in another hand.
    """

    call drunk_letter_second_part

    """
    I know that hand.

    I know it because I have signed things in it that I should not have signed, and lost things in it that I should not have lost.

    I wrote that. Last night. And I do not remember one word of deciding to.
    """

    $ drunk_details.description_hidden.unlock('wife')

    """
    There is a fire laid in the grate and I put the letter on it, both hands of it, and I hold a match under it until it goes.

    Not because I have thought about it. Because a man does not leave a thing like that on a desk for a maid to find.

    Now it is ash, and I still know what it said.
    """

    play sound fire

    """
    The flask is empty.

    My hands are doing the thing they do, and there is a whole day in front of me with people in it, and I fill the flask because that is what the flask is for.
    """

    if drunk_details.threads.is_unlocked('raided_bar'):

        """
        The whisky from the washstand. What is left of it.
        """

    else:

        """
        The bottle from the bottom of the bag. The one I always keep, because I always keep one.
        """

    """
    The hands stop.

    They always do. That is the trouble with them.
    """

    return


# ------------------------------------
#   He did not drink. First clear morning in five years.
#   -> watered_flask, or not
# ------------------------------------
label drunk_day2_morning_clear:

    $ drunk_mode = False

    """
    I wake up, and I know where I am.

    I know what day it is, and what house, and what is on the desk, and I lie still for a minute enjoying the novelty of it.

    Then I get up and I burn the letter.

    Both hands of it, the fine one and mine, in the grate with a match under them until there is nothing left to read.

    Nobody will ever be able to say that Samuel Manning was told to.
    """

    play sound fire

    """
    Now the flask.

    A drunk without a flask is a man who has stopped drinking, and people notice a man who has stopped drinking. They watch him. They wonder why.

    A drunk with a flask is furniture.
    """

    $ time_left = 1
    call run_menu(TimedMenu("drunk_day2_morning_menu_flask", [
        TimedMenuChoice('Fill it with water, and a finger of whisky for the smell', 'drunk_day2_morning_flask_water', early_exit=True),
        TimedMenuChoice('Fill it with whisky. One day will not hurt', 'drunk_day2_morning_flask_whisky', early_exit=True),
    ]))

    return


label drunk_day2_morning_flask_water:

    $ drunk_details.threads.unlock('watered_flask')

    """
    Water from the jug on the washstand, to the shoulder.
    """

    if drunk_details.threads.is_unlocked('raided_bar'):

        """
        And a finger of the house's whisky on top, for the nose.
        """

    else:

        """
        And a finger from the bottle in the bag on top, for the nose.
        """

    """
    I have done this before.

    Not often. Twice, in five years, when there was a judge who would not have me in his court with drink on me and a client who could not afford anybody else.

    I won one of them.

    Nobody could tell. That is the thing about being a known drunk: they stop looking for the difference.
    """

    $ drunk_details.description_hidden.unlock('lie')

    return


label drunk_day2_morning_flask_whisky:

    """
    Whisky.

    It has been a long night and it will be a long day, and a man cannot walk a wood on water.

    One day will not hurt. I have said that before, on other days.
    """

    if drunk_details.threads.is_unlocked('raided_bar'):

        """
        The house's whisky, from the washstand, to the shoulder.
        """

    else:

        """
        The bottle from the bag, to the shoulder.
        """

    """
    I take one now, for the stairs.

    The room goes kind.
    """

    show layer master at drunk_wobble_layer
    $ drunk_mode = True

    return
