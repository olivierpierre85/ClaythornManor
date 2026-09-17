# --------------------------------------------
#   Drunk
#
#   Saturday - The Hunt
#
#   11:00 -> 15:00
#
#   Music: upbeat for the lawn, chill for the grove, danger for the shot
#
#   Position
#       - North field   : host, captain, butler
#       - Western grove : doctor, drunk, lad, footman
#       - House         : nurse, psychic
#       - Dead          : broken (Thomas Moody)
#
#   Notes :
#       - Whisky in the flask (no watered_flask): the woods are a blur, the
#         rabbit is real, the shot is real, and the doctor's last words are
#         one thing too many. Ending despair, which is the intuition that
#         lets him put the bottle down on the Friday night.
#       - Water in the flask: the doctor is ahead of him in the bracken and
#         the rabbit is a choice. Fire (shot_doctor) and the weekend goes
#         on. Lower the rifle and the night finishes the letter's work for
#         him (spared).
#       - The death itself is the shared grove scene
#         (common_day2_hunt_accident_death), and the Captain's arrival the
#         shared north field scene (common_day2_hunt_doctor_aftermath),
#         both with his own narration.
#
#   Unlocks : doctor 'addict'
# --------------------------------------------
label drunk_day2_hunt:

    call change_time(11, 00, 'The Hunt', 'Saturday', chapter='saturday_afternoon')

    $ drunk_details.add_checkpoint("drunk_day2_hunt")

    call black_screen_transition("Samuel Manning", chapters_names[current_chapter])

    if drunk_details.threads.is_unlocked('watered_flask'):
        $ drunk_mode = False
    else:
        $ drunk_mode = True

    $ change_room('manor_garden', irisout)

    if not drunk_details.threads.is_unlocked('watered_flask'):
        show layer master at drunk_wobble_layer

    $ play_music('upbeat')

    """
    The lawn, and the lot of us on it with guns, like a bad regiment.
    """

    call common_day2_hunt_butler_groups

    if drunk_details.threads.is_unlocked('watered_flask'):

        """
        Her ladyship goes with the straight man, and the butler goes with her ladyship, and that leaves the doctor.

        I put myself beside him.

        Nobody stops me. He opens his mouth to, and cannot find the words a man uses to say he would rather not be shot at by a drunk, and closes it again.

        The boy is put with us because he is standing nearest.

        The footman leads. The good-looking one, from the car.
        """

    else:

        """
        I end up beside the doctor. I could not tell you how the sorting was done.

        The boy is with us, and the footman from the car, and we go west, and the others go somewhere else.
        """

    call change_time(11, 30)

    $ change_room('forest_grove', dissolve)

    $ play_music('chill', 2)

    if drunk_details.threads.is_unlocked('watered_flask'):

        call drunk_day2_hunt_morning_clear

    else:

        call drunk_day2_hunt_morning_drunk

    call change_time(12, 30)

    """
    We stop for luncheon with nothing to show for the morning.

    The footman lays it out on a cloth. Bread, cold meat, a pie, tea from a can.
    """

    if drunk_details.threads.is_unlocked('watered_flask'):

        """
        The pie has been made by the same hand as the sole. The pastry is short and the gravy has set properly and nobody in this clearing but me will notice.

        I eat it slowly, apart from the others, with the flask beside me where they can see it.
        """

        """
        The doctor sits by the footman.

        They talk low, heads close, and the footman's hand rests on the doctor's sleeve a moment longer than a servant's hand should.

        I have seen men look at one another like that. In chambers, once or twice, and in the dock more often than the law admits.

        It is not conspiracy. It is the other thing.

        I file it anyway. A lawyer files everything.
        """

        """
        Then the boy goes over and sits with the doctor, and the footman moves off, and they talk about nothing.

        The boy is being kind to him. The doctor does not know what to do with it.
        """

    else:

        """
        I sit apart. The pie is good, or I think it is. Everything is good by now.

        The doctor talks to the footman. The boy talks to the doctor. Nobody talks to me, and I take a pull from the flask and I do not mind it.
        """

    call common_day2_hunt_accident_footman_1

    call wait_screen_transition()

    call change_time(13, 15)

    if drunk_details.threads.is_unlocked('watered_flask'):

        call drunk_day2_hunt_afternoon_clear

    else:

        call drunk_day2_hunt_afternoon_drunk

    return


# ------------------------------------
#   The morning, sober and pretending
# ------------------------------------
label drunk_day2_hunt_morning_clear:

    """
    The doctor walks ahead of me, grey and wet through the back of his coat, though the morning is cold.

    He wipes his face. He wipes his hands on his trousers. He wipes his face again.

    I know that sweat.

    I had it at eleven in the morning for three years, and I have watched it on clients in the cells, waiting for what they could not have.

    Whatever this man takes, he has not taken it today.
    """

    $ doctor_details.description_hidden.unlock('addict')

    """
    I stumble when the footman looks round, and I take a pull from the flask when the boy looks round, and the water goes down cold and tastes of the jug.

    Nobody looks twice.

    The boy is frightened of the gun in his own hands, and the doctor is frightened of the boy, and the footman walks in front of the three of us as if he had been told to and would rather not.

    Rabbits get up. Birds get up. Nobody fires at anything, and I am the only one who knows why I have not.
    """

    """
    Eleanor's doctor stood at the foot of the bed with his hands behind his back.

    He stood like that for four days, and on the fifth he stood like that and told me it had been the operation, and that these things happened.

    This one stands with his hands in front of him, wringing them.

    I do not know.

    I walk behind him for an hour and I do not know, and it is the not knowing that keeps the rifle pointed at the ground.
    """

    return


# ------------------------------------
#   The morning, drunk
# ------------------------------------
label drunk_day2_hunt_morning_drunk:

    """
    Trees.

    A great many trees, and all of them moving, and the ground doing what the gravel did.

    I take a pull from the flask to steady it, and it steadies, and then it does not.

    Rabbits. Somebody says there are rabbits. I have not seen one.
    """

    """
    The doctor is in front of me, a grey coat going in and out of the bracken.

    Eleanor's doctor.

    Or not. I look at the back of his neck and I try to see the man at the foot of the bed, and I get a hospital and a screen and a smell of carbolic and nothing else.

    I take another pull for the screen.
    """

    """
    The boy keeps looking back at me.

    I give him a smile. It comes out on the wrong side of my face and he looks away.
    """

    return


# ------------------------------------
#   The afternoon, sober. The doctor's back, and the choice.
# ------------------------------------
label drunk_day2_hunt_afternoon_clear:

    """
    The afternoon goes the way the morning did.

    We walk. The bracken is chest high and wet, and the doctor goes into it ahead of me and comes out of it and goes in again.

    The boy is off to my right, watching his own feet. The footman is further on.
    """

    """
    Then the doctor stops.

    He has seen something, or he has stopped to wipe his face, and he stands with his back to me in the bracken twenty paces off, and there is nothing between us but fern.

    I know that back.

    I know it because it does not matter whether I know it. That is what I have been walking behind for two hours, and I understand it now.
    """

    """
    He is not the man at the foot of the bed. He may be. It makes no difference.

    Whoever wrote that letter knows what he is. Not thinks. Knows. And whatever he is, he has done it to somebody's Eleanor, or he has done it to a ward full of people who never had anybody to write letters for them.

    A man like that does not get a jury. He gets a drunk with a rifle in a wood, and a note on a desk.

    I know that it is wrong.

    I have known that a thing was wrong and done it anyway before, and it is the one skill I still have.
    """

    """
    Something moves in the fern between us, low and quick.

    Perhaps it is a rabbit.
    """

    $ play_music('danger', 2, fadeout_val=3)

    $ time_left = 1
    call run_menu(TimedMenu("drunk_day2_hunt_menu_rabbit", [
        TimedMenuChoice('Raise the rifle and fire', 'drunk_day2_hunt_fire', early_exit=True),
        TimedMenuChoice('Lower the rifle', 'drunk_day2_hunt_lower', early_exit=True),
    ]))

    return


# ------------------------------------
#   He fires. -> shot_doctor, and the weekend goes on.
# ------------------------------------
label drunk_day2_hunt_fire:

    $ drunk_details.threads.unlock('shot_doctor')

    """
    I raise the rifle.

    I put the bead on the middle of the grey coat, where the liver is, because I sat through a great many medical witnesses in my time and I know where the liver is.

    And I open my mouth, and I make my voice do the thing it does.
    """

    call common_day2_hunt_accident_death

    """
    Justice.

    He says it to the boy, and the boy does not understand it, and I do.

    I stand three paces off with my hands shaking, and the shaking is not put on, and that is the one honest thing about me in this wood.

    I did not know. I still do not.

    But he did. He knew exactly what he was, and he said so, and then he drank three little bottles and stopped saying anything.
    """

    pause 2.0

    """
    The footman comes back with the others.

    By the time they reach us it is long over. Daniel Baldwin has bled out into the fern, and lies there with his shirt torn open, as still as the moss.
    """

    call change_time(13, 45)

    $ change_room('forest_edge', dissolve)

    """
    The straight man takes charge of it, the way men like him do.

    He cuts two saplings and threads his coat and the footman's between them, and his hands do the work without being told, and the boy takes the head and the footman the feet.

    I am given the bag to carry, because it is the one thing a man in my state cannot drop.

    It is heavier than it looks. There is glass in it, a great deal of glass, and it chinks with every step like a man counting money.

    Her ladyship walks ahead of me and does not look round.

    The butler walks behind me and does not say a word.
    """

    jump drunk_day2_evening


# ------------------------------------
#   He lowers the rifle. -> spared
# ------------------------------------
label drunk_day2_hunt_lower:

    """
    I lower the rifle.

    The thing in the fern goes on its way, and the doctor wipes his face and walks on, and does not know that he has been anything but a man in a wood.

    I do not know what he is.

    A man who does not know does not fire. That was the whole of the law, once, before I forgot it.
    """

    $ play_music('chill', 2)

    """
    The afternoon finishes itself.

    Nobody shoots anything. The footman calls it, and we walk back, four men and four clean rifles, and the doctor is grey and alive and does not thank me, because he does not know there is anything to thank me for.
    """

    call change_time(15, 00)

    $ change_room('entrance_hall', dissolve)

    """
    The other party is in the hall before us. Her ladyship looks at the four of us coming in, and counts, and something goes across her face and is gone.

    Four.

    She was not expecting four.
    """

    call change_time(18, 30)

    $ change_room('dining_room', dissolve)

    """
    Dinner is very good and I do not taste it.

    I sit next to her ladyship and I hold the glass by the bowl and I do not drink from it, and across the table the doctor eats nothing and sweats.

    Nobody says anything about the wood. There is nothing to say. Nothing happened in it.

    That is the whole of my trouble. I was brought here for something to happen, and it did not.
    """

    call change_time(22, 00)

    $ change_room('bedroom_drunk', dissolve)

    $ play_music('mysterious', 2)

    """
    I lock the door.

    I put a chair under the handle, because a man who has read that letter is a fool not to, and I lie down in my clothes with the rifle's weight still in my arms.

    I do not drink. I have not all day, and I do not now.

    It is the longest I have gone in five years, and I am proud of it, lying in the dark, and I fall asleep proud.
    """

    $ stop_music()

    scene black_background with dissolve

    pause 2.0

    play sound unlock

    """
    A key.

    Not mine. A key from the other side, turning slowly, the way a key turns when the hand on it has done this before.

    The chair holds for as long as a chair holds.
    """

    play sound moving_furniture

    """
    I am awake now. I am sitting up. I am reaching for a rifle that is downstairs behind glass.
    """

    jump drunk_ending_spared


# ------------------------------------
#   The afternoon, drunk. The rabbit is real. -> despair
# ------------------------------------
label drunk_day2_hunt_afternoon_drunk:

    """
    The flask is nearly gone, and so is the afternoon, and so am I.

    The doctor is a grey coat in the fern. The boy is somewhere. The footman is somewhere else.

    Then something moves, low and brown, right there, right in front of me, and I have a gun, and it is the first thing all day that has made sense.
    """

    call common_day2_hunt_accident_death

    $ stop_music(2)

    """
    Justice.

    He says it to the boy, not to me, and he closes his eyes on it, and the three little bottles roll off his chest into the moss.

    The boy is shouting for help. The footman has gone for the others. It is a big wood and it will be a long time before anybody comes.

    So it is the boy, and the doctor, and me.
    """

    """
    A rabbit.

    I have shot a man for a rabbit, and I do not know whether I meant to.

    That is the thing. That is the whole of it. I read a letter last night and I drank it away, and this morning I filled a flask, and now there is a man in the fern, and I cannot tell my own crime from my own accident.

    I could not tell them apart in court either. That is why I lost.

    Eleanor would not know me. Eleanor would not want to.
    """

    """
    The boy has his back to me. He is holding the doctor's hand, which is a kind thing, and useless.

    The rifle is very heavy, and then it is not, because I have found the one thing to do with it that I can be sure I mean.
    """

    $ play_music('sad', 2)

    play sound gun

    jump drunk_ending_despair
