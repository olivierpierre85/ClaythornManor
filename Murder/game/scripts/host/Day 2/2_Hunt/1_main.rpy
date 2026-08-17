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
#       - Shared beats live in _common/Day 2/2_Hunt:
#           - common_day2_hunt_luncheon_served
#           - common_day2_hunt_shots_heard
#           - common_day2_hunt_doctor_aftermath
#       - The lawn is hers alone. She reports the splitting of the parties in
#         her own voice rather than calling the shared labels, since none of
#         those lines are hers and she is only watching them happen.
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

    $ change_room('manor_garden', fade)

    """
    They are all waiting on the lawn.

    I take my place among them and put my smile back on.

    The butler proposes we divide into two parties, since it will be easier to spot game that way.

    Nobody thinks to disagree with him.

    Captain Sinha asks whether he might have the privilege of accompanying me, and I see no reason why not.

    Mr Manning joins Doctor Baldwin, who clearly minds but cannot find the words to say so.

    Mr Harring hovers at the edge of it all until he is put with them.

    Then the butler settles where to go in a few quiet sentences. 
    
    And we are on our way.
    """

    call change_time(11, 30)

    $ change_room('forest_edge')

    """
    We walk for some time through the undergrowth, and I remember that a gun is a great deal heavier than it looks.

    I shift my grip and find no comfortable way to hold the thing.

    A pheasant goes up out of the grass with a noise like a slammed door.

    Instinctively, I raise my rifle.
    """

    play sound gun

    """
    The shot comes up late, and too high.

    The bird flies off into the trees.

    The gun kicks back into my shoulder hard enough to bring water to my eyes.

    I am not off to a great start.
    """

    host """
    The light is most unhelpful today.
    """

    """
    Nobody answers me.

    That is a flimsy excuse.

    I ought to have said nothing at all.
    """    

    butler """
    It is true, Captain, as her ladyship says.

    I have known mornings here when a man could not hit a barn door at ten paces.
    """

    """
    He smiles at me and nods.

    But I am certain he noticed how poor my shot was.
    """

    call wait_screen_transition()

    call change_time(11, 45)

    """
    A while later, the Captain misses a shot of his own.

    I am starting to think he is not a natural hunter either.

    Or maybe he is a little rusty.
    """

    pause 1.0

    """
    Then, a little further on, I notice something behind a bush.

    A rabbit, some twenty paces off.

    The Captain has not seen it.

    Nor has the butler.

    For the moment it belongs to me alone.

    It is sitting perfectly still, and surely even I cannot miss this.

    I could fire the gun. 

    Or I could just let the Captain take the shot.
    """

    $ time_left = 1
    call run_menu(
        TimedMenu("host_day2_hunt_menu_rabbit", [
            TimedMenuChoice("Raise the gun and fire", 'host_day2_hunt_rabbit_shoot', early_exit=True),
            TimedMenuChoice("Point the rabbit out to the Captain", 'host_day2_hunt_rabbit_offer', early_exit=True),
        ])
    )


    """
    Nothing else shows itself, which is the first piece of luck I have had all morning.

    By the time the butler calls us in for luncheon, I have not been obliged to lift the gun again.
    """

    call change_time(12, 30)

    $ change_room('forest_clearing', dissolve)

    call common_day2_hunt_luncheon_served

    """
    And so I am left alone with the Captain.

    We talk of the weather, and other things of no consequence.

    I am glad I am not given the opportunity to make a mistake.

    So the luncheon goes pleasantly.
    """

    call change_time(13, 30)

    $ change_room('forest_edge', dissolve)

    call common_day2_hunt_shots_heard

    call common_day2_hunt_doctor_aftermath

    """
    The butler walks a few paces behind me on the way back, and says nothing at all.

    He was away the whole hour, and he came back to us only minutes before those shots were fired.
    """



    """
    Two deaths in one day.

    My mind goes into a race.

    And I notice my hands are shaking convulsively.
    """

    jump host_day2_evening


# --------------------------------------------
#   She fires at the rabbit herself and misses it
#   -> 'terrible_shot'
# --------------------------------------------
label host_day2_hunt_rabbit_shoot:

    """
    I raise the gun.
    """

    play sound gun

    """
    The earth jumps a yard to the left of the animal, which is into the bush before the sound has finished with the trees.

    Nobody says anything, and the silence goes on rather too long.
    """

    host """
    Too bad.

    I am quite out of practice.
    """

    butler """
    It was a nice shot, my lady, just a difficult angle.
    """

    """
    The Captain says nothing whatsoever.

    If he had doubts before, now he must be certain.

    He knows I cannot shoot.

    And he will probably understand the implications of this.

    What was I thinking, taking that shot.
    """

    $ host_details.threads.unlock('terrible_shot')

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
    Captain. Over there is a rabbit. Do you see it?

    Take it, please. I insist.

    I have the whole season for such things, and you have come a very long way.
    """

    captain """
    You are very good, my lady.
    """

    """
    He raises the gun.
    """

    play sound gun
        
    """
    He misses.

    The shot goes somewhere into the fern, and the rabbit goes with it.
    """

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

    """
    The light.

    He has taken my weak excuse and put it straight into his own mouth.

    I have spent twenty years among people pretending to be something they are not, and I know the sound of it.

    Captain Sinha cannot shoot.

    Maybe I am not the only one wearing a costume this morning.
    """

    return
