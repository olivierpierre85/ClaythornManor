# --------------------------------------------
#   Host
#
#   Saturday - The Hunt
#
#   11:00 -> 15:00
#
#   Music: upbeat for the shoot, danger when the doctor is shot
#
#   Position
#       - House, Tea room : nurse, psychic
#       - North field     : host, captain, butler
#       - Western grove   : doctor, drunk, lad, footman
#       - Dead            : broken (Thomas Moody), then the doctor
#
#   Notes :
#       - The same morning as captain_day2_hunt_moody_dead, seen from her side.
#       - Shared beats (the pairing, the accident) must be extracted into
#         _common as they are written here.
#       - The north field stays in her own file. The missed pheasant is the
#         main timeline and happens in the captain's script too. Only the
#         rabbit afterwards is hers to decide, and it carries 'terrible_shot'.
# --------------------------------------------
label host_day2_hunt:

    call change_time(11, 00, 'The Hunt', 'Saturday', chapter='saturday_afternoon')

    $ current_character.add_checkpoint("host_day2_hunt")

    call black_screen_transition("Lady Claythorn", chapters_names[current_chapter])

    $ change_room('bedroom_host', irisout)

    $ play_music('mysterious', 1)

    """
    I am back in my room, and I try to make sense of what is happening.
    """

    if host_details.threads.is_unlocked('found_poison'):

        """
        An image suddenly pops into my mind.

        The bottle in the scullery, standing open as though somebody had just used it.

        Is it possible that it was for...

        No, I cannot start thinking that way.

        I will lose my mind.

        I push the thought aside.
        """

    else:
    
        """
        But I do not have much time, so I get ready without thinking too much about it.
        """

    """
    Soon, I am ready to join the others for the hunt.
    """

    $ change_room('gun_room', dissolve)

    """
    First I must take a weapon.
    """

    butler """
    Here is your rifle, my lady.

    I remember you said you knew how to use it.
    """

    host """
    That is true.
    """

    """
    True, but I may have exaggerated my abilities in order to get this job.

    I once went on a shoot with a fellow who was courting me.

    I hope that will be enough.

    He must sense my hesitation.
    """

    butler """
    If you are not sure...

    I will be with you to help along the way.

    All you have to do is not embarrass yourself.
    """

    host """
    Do not worry, I will be fine.
    """

    # next =>
    $ change_room('manor_garden', fadein)

    """
    Everyone is gathered outside the manor.

    TODO?
    """

    call change_time(11, 45)

    $ change_room('forest_edge')

    """
    We walk for some time through the undergrowth, and I learn that a gun is a great deal heavier than it looks.

    I once carried a rifle across a stage for three acts and thought it a burden.

    That one was hollow.

    I shift my grip and find no comfortable way to hold the thing.

    The butler walks a few paces behind us and says nothing at all, which I find I resent.
    """

    """
    A pheasant goes up out of the grass with a noise like a slammed door.

    Everything I was told in the gun room leaves me at once.

    The stock comes up late, and too high, and I fire anyway because they are both watching me.
    """

    play sound gun

    pause 1.0

    """
    The bird carries on into the trees, entirely unconcerned.

    The gun kicks back into my shoulder hard enough to bring water to my eyes.

    I laugh, because laughing is the one thing I can still do properly.
    """

    host """
    The light is most unhelpful today.
    """

    """
    Nobody answers me.

    The Captain looks at the trees where the bird went, and the butler looks at me.

    The light is perfectly fine, and all three of us know it.

    A poor line, poorly delivered. I ought to have said nothing at all.
    """

    """
    A little further on, something moves at the edge of the bracken.

    A rabbit, sitting up in the open some twenty paces off, watching us in the way that rabbits do.

    The Captain has not seen it. Nor has the butler.

    For the moment it belongs to me alone.

    I could raise the gun. It is sitting perfectly still, and surely even I cannot miss a thing that will not move.

    Or I could give it away.
    """

    $ time_left = 1
    call run_menu(
        TimedMenu("host_day2_hunt_menu_rabbit", [
            TimedMenuChoice("Raise the gun and fire", 'host_day2_hunt_rabbit_shoot', early_exit=True),
            TimedMenuChoice("Point it out to the Captain", 'host_day2_hunt_rabbit_offer', early_exit=True),
        ])
    )

    if host_details.threads.is_unlocked('terrible_shot'):

        """
        We walk on, and some minutes later a second rabbit bolts from the fern ahead of us.

        The Captain brings his gun up smartly enough.
        """

    else:

        """
        He settles himself without hurry.

        The rabbit does him the courtesy of staying exactly where it is.
        """

    play sound gun

    pause 1.0

    """
    He misses.

    The shot goes somewhere into the fern, and the rabbit goes with it.
    """

    if not host_details.threads.is_unlocked('terrible_shot'):

        """
        A creature sitting perfectly still at twenty paces, and an officer of thirty years' service cannot touch it.
        """

    host """
    Captain, that was a nice attempt.

    I am sure you will have better luck next time.
    """

    captain """
    You are too kind, my lady.

    I suppose you were right about the light.
    """

    if host_details.threads.is_unlocked('terrible_shot'):

        """
        He is being kind, and I would very much rather he were not.

        Kindness of that particular sort is what one offers a woman who has just embarrassed herself in front of the servants.
        """

    else:

        """
        The light.

        He has taken my excuse and put it straight into his own mouth, and he did not have to think about it first.

        I have spent twenty years among people pretending to be something they are not, and I know the sound of it.

        Captain Sinha cannot shoot.

        Whatever else is happening in this house, I am not the only one wearing a costume this morning.
        """

    """
    Nothing else shows itself, which is the first piece of luck I have had all morning.

    By the time the butler calls us in for luncheon, I have not been obliged to lift the gun again.
    """

    call change_time(12, 30)

    $ change_room('forest_clearing', dissolve)

    # TODO: Luncheon. The butler leaves them to look in on the other party, and she
    #       is alone with a guest who is plainly working up to a question.
    # TODO: Small talk that gives nothing away. The confrontation with the Captain
    #       belongs to the evening, at the manor.

    call change_time(13, 30)

    $ change_room('forest_edge', dissolve)

    # TODO: Two shots from the western grove, close together, and then a cry.

    $ play_music('danger', 2)

    $ change_room('forest_grove')

    # TODO: Doctor Baldwin dead in the fern. Her second body of the day, and this
    #       one was no more planned than the first.
    # TODO: She is of no use whatsoever and says so. The Captain takes charge of
    #       the stretcher, which suits her, since she has nothing to give.
    # TODO: The slow walk back through the ferns, and the thing she cannot say
    #       aloud: two dead in a house opened by a gentleman she has never met.

    jump work_in_progress


# --------------------------------------------
#   She fires at the rabbit herself and misses it
#   -> 'terrible_shot'
# --------------------------------------------
label host_day2_hunt_rabbit_shoot:

    """
    I raise the gun.

    I have watched men do this all morning. The cheek down, the left hand well forward, the breath let half out.

    I do every part of it, in the right order, and not one part of it helps.
    """

    play sound gun

    pause 1.0

    """
    The earth jumps a yard to the left of the animal, which is into the bracken before the sound has finished with the trees.

    Nobody says anything, and the nothing goes on rather too long.
    """

    host """
    I am quite out of practice.

    One forgets how quickly they go.
    """

    """
    It did not go anywhere. It was sitting still, and I missed it by a yard, and the Captain stood near enough to see exactly where the shot went.

    Twice now, in a quarter of an hour.

    No woman raised on this estate could have done what I have just done.
    """

    $ host_details.threads.unlock('terrible_shot')

    butler """
    A difficult light this morning, Captain, as her ladyship says.

    I have known mornings here when a man could not hit a barn door at ten paces.
    """

    """
    He is covering for me, and he is doing it far too smoothly, and that is a mistake of its own.

    The Captain says nothing whatsoever. He merely looks at the bracken where the rabbit was.
    """

    return


# --------------------------------------------
#   She gives the rabbit to her guest, which is
#   both good manners and excellent cover
# --------------------------------------------
label host_day2_hunt_rabbit_offer:

    """
    No.

    I have fired once this morning, and once was quite enough for everybody.
    """

    host """
    Captain. There, by the thorn. Do you see it?

    Take it, please. I insist.

    I have the whole season for such things, and you have come a very long way.
    """

    """
    A hostess who hands the best of the morning to her guest is doing no more than she ought.

    And a woman who does not fire cannot miss.
    """

    captain """
    You are very good, my lady.
    """

    """
    He raises the gun, and I watch him do it, because I have nothing else to do with my eyes.
    """

    return
