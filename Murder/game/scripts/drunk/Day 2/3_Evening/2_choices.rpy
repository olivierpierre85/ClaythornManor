# --------------------------------------------
#   Drunk - Saturday night, the three ways out of the locked room
#
#   - drink    -> he cuts his own throat (throat_cut)
#   - confront -> he warns the house and one of them silences him (silenced)
#   - play dead -> he paints his throat with port and lies down (played_dead),
#                  and the story goes on to Sunday
# --------------------------------------------


# ------------------------------------
#   Accept it, and drink. -> throat_cut
# ------------------------------------
label drunk_day2_evening_drink:

    $ change_room('bedroom_drunk')

    """
    No.

    I am fifty-five years old and I have been tired for five of them, and I am not going to spend my last night on this earth outwitting a man with a broken face and a key.

    I take the whisky off the washstand.
    """

    show layer master at drunk_wobble_layer
    $ drunk_mode = True

    """
    The first one is for Eleanor.

    The second is for Daniel Baldwin, who I killed today for a woman I never met, and who may or may not have deserved it, and I shall never know, and that is the truest thing about my whole life.

    The third is for nobody. The third is just the third.
    """

    call change_time(0, 30)

    if drunk_details.threads.is_unlocked('understood'):

        """
        I know what is coming for me. I worked it out sober, in that chair, and knowing it changes nothing, because I have never once in my life used a thing I knew.

        Let them come. Let them find the door already done.

        I will not give whoever holds that key the satisfaction of a locked man waiting.
        """

    else:

        """
        Something is coming for me. I do not know its name and I am too far gone now to give it one.

        I only know I would rather meet it on my own terms than wake to it in the dark.
        """

    """
    There is a razor in my bag. There has been a razor in my bag for a year, for exactly this, on exactly the nights I did not have the courage.

    Tonight I have the whisky for courage.

    I am sorry, Eleanor. I meant to be somebody.
    """

    $ stop_music()

    $ play_music('sad', 2)

    pause 2.0

    jump drunk_ending_throat_cut


# ------------------------------------
#   Warn the house. Nobody believes a drunk. -> silenced
# ------------------------------------
label drunk_day2_evening_confront:

    $ change_room('bedroom_drunk')

    $ play_music('danger', 2)

    """
    No.

    I have spent my life sitting on what I knew, and losing for it, and drinking because I lost.

    Not tonight. Tonight I know something true, and for once in my wretched life I am going to say it out loud where it counts.
    """

    play sound door_rattling

    drunk """
    Listen to me!

    Listen! There is a killer in this house!

    The telephone is dead. Nobody is coming. The police were never called.

    Baldwin was no accident, and neither was Moody, and I am next, and after me it will be one of you!
    """

    """
    A door opens along the corridor. Then another.

    I put my mouth to the crack of my own door and I tell them all of it. The letter. The tree that fell on a night with no wind. The hostess who acts. The butler who is no butler.

    I tell it well. It is the best summing-up I have given in twenty years, and there is not a soul on a jury to hear it.
    """

    pause 1.0

    if drunk_details.observations.is_unlocked('phone_call'):

        nurse """
        The poor man has gone quite mad.

        First he shoots the doctor, and now this.
        """

    else:

        nurse """
        He is raving. He has been drinking again.
        """

    psychic """
    It is the drink talking. It always is, with him.

    Do try to sleep, Mr Manning.
    """

    """
    Of course.

    The drunk who shot the doctor this afternoon, raving behind a locked door about a killer in the house. Who would believe a word of it.

    I have spent thirty years being the man nobody believes. I built it myself, glass by glass. And now, on the one night it would save my life to be believed, the house I built holds.

    Their doors close, one by one, all the way down the corridor.

    All but one.
    """

    pause 1.0

    $ stop_music()

    """
    One set of footsteps does not go away.

    They come towards my door, unhurried, the way they always are.

    And a key goes into the lock, very gently, from the other side.
    """

    play sound door_locked

    """
    Somebody heard me after all.

    The one person in this house who knew that every word of it was true.
    """

    play sound door_open

    jump drunk_ending_silenced


# ------------------------------------
#   Play dead. -> played_dead, Sunday
# ------------------------------------
label drunk_day2_evening_play_dead:

    $ change_room('bedroom_drunk')

    $ play_music('mysterious', 2)

    """
    No.

    There is a third thing a man can do with a locked door, and it took me until fifty-five and a death sentence to think of it.

    Nobody checks a cut throat.

    I have prosecuted, and I have defended, and I have stood over more bodies than a barrister ever should, and not once, not one single time, did anybody go and put a hand to a cut throat to be sure.

    It is the one wound the living cannot bear to look at twice.

    And I have a bottle of port.
    """

    $ drunk_details.threads.unlock('played_dead')

    """
    Port makes a poor drink and a magnificent corpse.

    Dark, and thick, and it dries the colour of old blood, and I have watched enough of it spill down enough shirt fronts to know exactly how a cut throat bleeds.

    I take the razor from my bag.

    Not deep. It does not need to be deep. It needs to be red, and it needs to be still.

    A line across, high, where a hand would go if a hand had done it. Just enough of the edge to make it true to the touch, if anybody were fool enough to touch it, and nobody ever is.
    """

    play sound woman_cough

    pause 1.0

    """
    Then the port. Down the line, and over the collar, and into the pillow, and a good pool of it soaked into the sheet where the head lies.

    I make a ruin of the bed. I knock the chair over. I do it the way it would look if a man had fought and lost.

    Then I lie down in the middle of my own murder, on my back, with my head turned to the wall, and I let my mouth fall open, and I stop.
    """

    """
    I have played a great many parts in a great many courtrooms.

    The sober man. The confident man. The man who believes his own client.

    This is the finest of them, and it is the only one I have ever meant.

    I do not know how long it must last. All night. All of tomorrow, perhaps.

    A man who can lie still through his own thirst can lie still through anything.

    And I am very, very good at being thirsty.
    """

    call change_time(1, 00)

    $ stop_music()

    scene black_background with dissolve

    pause 2.0

    jump drunk_day3_morning
