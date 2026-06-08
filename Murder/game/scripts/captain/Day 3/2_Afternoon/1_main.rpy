# --------------------------------------------
#   Captain
#
#   Sunday - Afternoon
#
#   12:00 -> Ending
#
#   Music: mysterious
#
#   Position
#       - House: captain, lad, psychic (+ nurse on the hide path)
#       - Dead : broken, doctor, drunk
#       - Gone : host, staff
#
#   Notes :
#       - Both morning paths (nurse "hide" / explore) converge here.
#       - Three endings:
#           * car_ambush  — leave together by motor (needs seen_car + petrol);
#                           the nurse climbs in, the car is stopped, he is shot.
#           * survives    — the coward's lie: slip away alone in the car.
#                           Gated behind the car_ambush intuition.
#           * shot_fleeing — no working car (or he chooses it): leaves alone on
#                            foot and is shot in the woods.
# --------------------------------------------

label captain_day3_afternoon:

    call change_time(12, 00, "Afternoon", "Sunday", hide_minutes=True, chapter='sunday_afternoon')

    $ captain_details.add_checkpoint("captain_day3_afternoon")

    call black_screen_transition("Sushil Sinha", chapters_names[current_chapter])

    $ play_music('mysterious')

    $ change_room('tea_room', irisout)

    """
    After resting for a while, I believe it is time to take action.
    """

    call common_day3_afternoon_lad_psychic_captain_discussion_1

    if captain_details.threads.is_unlocked('seen_car') and captain_details.threads.is_unlocked('petrol_tin_in_shed'):

        call common_day3_afternoon_lad_psychic_captain_discussion_2b

        captain """
        Luckily, we might not need to walk.

        There is an old car in the garage, probably Lady Claythorn's old vehicle.

        It was out of petrol when I checked it, but I have also seen a full tin of petrol in the garden shed.

        If the old car is in decent enough shape, I might be able to get it running.
        """

        lad """
        You can drive?
        """

        captain """
        Yes. I have driven worse, on worse roads than these.

        So I do not think it would be a problem to drive out of here.

        I will see if I can start the car and bring it in front of the entrance.

        You can wait for me there, it should not take very long.
        """

        call change_time(13, 00)

        $ change_room('manor_garden', dissolve)

        """
        I leave the others by the front steps and go round alone.

        The petrol tin still sits in the garden shed where I found it. 
        
        I pick it up.
        """

        $ change_room('garage', dissolve)

        """
        I fill the tank, set the choke, and work the crank.

        The engine baulks twice, then catches on the third pull and settles into a rough idle.

        It runs. That is all I ask of it.
        """

        $ change_room('manor_garden', dissolve)

        """
        I ease the car out of the garage and bring toward the Manor's entrance.

        The engine runs rough beneath me, but it runs.
        """

        if captain_details.endings.is_unlocked('car_ambush'):

            # Intuition — he has died on this road before, riding out with the others.
            """
            And yet.

            Something in me shivers.

            I feel an overwhelming sense of doom.

            I cannot say why, but I have the strongest sense that to leave together, in that car, is to die together.

            I assumed everyone still in the house were in the same boat as I.

            But what if they are not.

            Maybe I was too quick to disregard them as a thread.

            The safest thing now would be to leave alone.

            It would be a contemptible thing to do.

            It might also be the only way to get out of here alive.

            I can send help after I reach town.

            Maybe they will be fine just waiting a few hours there.

            But as I am thinking this, I know it is probably not true.

            If I leave now, I might not see them alive again.
            """

            $ time_left = 1
            call run_menu( TimedMenu("captain_day3_afternoon_car_menu", [
                TimedMenuChoice("We all leave together, in the car", 'captain_day3_afternoon_car_together_intro', early_exit=True),
                TimedMenuChoice("Drive off alone{{intuition}}", 'captain_day3_afternoon_lie_alone', early_exit=True),
            ], image_left="psychic", image_right="lad"))

        else:

            jump captain_day3_afternoon_car_together

    else:

        call common_day3_afternoon_lad_psychic_captain_discussion_2

        call common_day3_afternoon_lad_psychic_captain_discussion_3


        call captain_day3_leave_alone_introduction

        """
        I keep a solid pace for the better part of an hour.

        Then, somewhere behind me, I hear an engine.
        """

        play sound car_driving fadein 4 loop

        """
        A motor car, coming up the road at my back.

        For a moment I let myself hope it is help, sent on ahead of the others.

        I raise a hand and step to the verge to let it pass.

        It does not slow.

        If anything it gathers speed, and it holds straight for me.
        """

        """
        I throw myself towards the trees.

        But the road is wide open, and a man on foot is no match for a motor.

        The car corrects as I move, and the wheels come with me.
        """

        play sound body_fall

        jump captain_ending_run_over

label captain_day3_afternoon_car_together_intro:

    """
    Despite everything in my body telling me to leave, I can not make myself abandon them to their fate.

    We will all leave together.
    """

    jump captain_day3_afternoon_car_together

    return


label captain_day3_afternoon_car_together:

    """
    I bring the car round to the front of the manor.

    Mr Harring and Miss Baxter are already outside, ready for the road.

    As I draw up before the steps, another figure comes out of the front door.

    Rosalind Marsh.

    She has been somewhere in the manor all this while.

    I step out of the car.
    """

    nurse """
    You were going to leave without me.
    """

    """
    We are all baffle by her apparition, but there is no time for long explanation.

    I want to leave as soone as possible.
    """

    captain """
    We did not know you were alive, Miss Marsh.

    But now you can come with us.

    Please, all of you, get in.
    """

    """
    The boy hands Miss Baxter up into the back, and Miss Marsh climbs in beside her without another word.

    I do not care for the timing of it.

    But I can not in good conscience leave her on that gravel.
    """

    $ change_room('forest_road', dissolve)

    """
    The gate falls behind us, and for a little while it is almost easy.

    The road unrolls between the trees. The engine settles into its work.

    I begin, against my better judgement, to believe we have managed it.
    """

    $ play_music('danger')

    """
    Then the engine coughs.

    It catches, falters, and dies, and we coast to a stop in the middle of the empty road.
    """

    captain """
    Stay in the car.

    All of you.
    """

    """
    I get out to look at the engine, because that is what a man does, and I cannot think what else to do.

    The wood on either side is very still.

    We are utterly alone.
    """

    play sound door_open

    """
    Someone gets out of the car.

    I yell while I am still looking at the engine.
    """

    captain """
    Stay inside!

    We do not know if it is safe here.
    """

    """
    I keep examining the car and check the exhaust.
    
    There is something stuck in it.

    I reach into the exhaust and pull out what is blocking it.

    A potato.

    How did it get there?
    """
    
    """
    I hear footsteps coming towards me.
    """

    captain """
    Please, go back in the car!
    """

    play sound gun

    jump captain_ending_car_ambush


# ------------------------------------
#   AFTERNOON — the coward's lie (survive)
# ------------------------------------
label captain_day3_afternoon_lie_alone:

    """
    I roll the car up to the front steps, where the three of them are waiting.

    The boy steps forward to open the door.

    I do not let him.
    """

    captain """
    The car will not carry four of us over the rough ground to the lodge.

    Loaded as we are, she will founder inside a mile, and then we have nothing at all.

    I will take her light, reach the lodge, and bring back help and a second motor.

    Bar the doors.

    Do not open for a single engine.

    Wait until you hear two.
    """

    lad """
    You will come back?
    """

    captain """
    On my honour.
    """

    """
    On my honour.

    The words come out smooth and steady, as they always have.

    I have said such things all my life and been believed.

    A supply officer who never saw a shot fired, telling boys of battles I watched from miles behind the lines.

    I learned young that a calm voice and a straight back will carry a room further than courage ever did.

    My whole life has been spent near the fighting and never once in it.

    Other men did the dying.

    I signed the papers, and told the stories afterwards.

    I am too old to become a braver man this afternoon.

    I have no intention of coming back, and I think the boy half knows it.

    He asks anyway, because he would sooner be lied to than left without a word.
    """

    $ change_room('forest_road', dissolve)

    """
    I let out the clutch and pull away, past the three of them on the steps, and do not look back at the house.

    A man who looks back might turn the car around, and I have decided not to be that man today.

    The engine holds. The road, for me, stays empty.

    Mile after mile, and not a soul on it.
    """

    jump captain_ending_survives

