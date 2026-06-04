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

    # Explore path — the captain finished his sweep of the house. The others
    # rested in the tea room while he worked.
    $ change_room('tea_room', irisout)

    """
    After resting for a while, I believe it is time to take action.
    """

    call common_day3_afternoon_lad_psychic_captain_discussion_1

    if captain_details.threads.is_unlocked('seen_car') and captain_details.threads.is_unlocked('petrol_tin_in_shed'):

        captain """
        As it happens, we are not obliged to walk.

        The old motor car in the garage wants only petrol, and I have seen a full tin in the garden shed.

        I can have it running inside the hour.
        """

        lad """
        You can drive?
        """

        captain """
        I have driven worse, on worse roads than these.
        """

        if captain_details.endings.is_unlocked('car_ambush'):

            # Intuition — he has died on this road before, riding out with the others.
            """
            And yet.

            Something in me baulks at the picture of it.

            The four of us packed into one slow machine, crawling down a single road that anyone might be watching.

            I cannot say why, but I have the strongest sense that to leave together, in that car, is to die together.

            One man, travelling light and quiet, would stand a far better chance.

            It would be a contemptible thing to do.

            It might also be the only thing that works.
            """

            $ time_left = 1
            call run_menu( TimedMenu("captain_day3_afternoon_car_menu", [
                TimedMenuChoice("We all leave together, in the car", 'captain_day3_afternoon_car_together', early_exit=True),
                TimedMenuChoice("Tell them I will scout the road, then drive off alone{{intuition}}", 'captain_day3_afternoon_lie_alone', early_exit=True),
            ], image_left="psychic", image_right="lad"))

        else:

            """
            It is settled, then.

            We go together, and we go at once.
            """

            jump captain_day3_afternoon_car_together

    else:

        call common_day3_afternoon_lad_psychic_captain_discussion_2

        call common_day3_afternoon_lad_psychic_captain_discussion_3


        $ change_room('forest_road', dissolve)

        """
        I took only my coat and what will fit in its pockets.

        The drive gives way to a rough road, and the road to open country between the trees.
        """

        $ play_music('danger')

        """
        I keep a solid pace for an hour, then, away to my right, I notice something.

        A shape that is the wrong colour for bark.

        And from that shape, I can spot the canon of a rifle.

        I jump to the ground to hide. But the road is wide open, I am too easy a target.
        """

        play sound gun

        jump captain_ending_shot_fleeing


# ------------------------------------
#   AFTERNOON — leave together by car
#
#   The captain brings the car round to the front of the manor and the others
#   board there. On the explore path the hiding nurse emerges from the front
#   door at this moment; on the confide path she is already among them. Either
#   way all four end up aboard and the shared ambush ride follows.
# ------------------------------------
label captain_day3_afternoon_car_together:

    call change_time(13, 00)

    $ change_room('manor_garden', dissolve)

    """
    I leave the others by the front steps and go round to the garage alone.

    I fetch the tin from the shed, fill the tank, and coax the old engine into life.

    It runs rough, but it runs.

    I bring it round to the front of the manor and draw up before the steps.
    """

    if not captain_details.threads.is_unlocked('confide_in_nurse'):

        """
        As I do, a figure comes out of the front door.

        Rosalind Marsh.

        She has been somewhere in the manor all this while, and says nothing of where.
        """

        nurse """
        You were going to leave without me.
        """

        captain """
        We did not know you were alive, Miss Marsh.

        Get in. Quickly.
        """

        """
        The boy hands Miss Baxter up into the back, and Miss Marsh climbs in beside her without another word.

        I do not care for the timing of it.

        But I will not leave a living soul on that gravel.
        """

    else:

        """
        The boy hands Miss Baxter up into the back, and Miss Marsh takes her place beside her.

        The four of us, and one tired engine.
        """

    call captain_day3_car_ride_ambush


# ------------------------------------
#   AFTERNOON — the coward's lie (survive)
# ------------------------------------
label captain_day3_afternoon_lie_alone:

    captain """
    On reflection, the car will not carry all four of us over that ground.

    Let me take it ahead, scout the road to the lodge, and come back for you.

    Bar the doors until I do.
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

    I have no intention of coming back, and I think the boy half knows it.

    I fetch the tin from the shed, fill the tank, and bring the old car grinding up the drive.

    Alone.
    """

    $ change_room('manor_garden', dissolve)

    call change_time(13, 00)

    """
    I do not look back at the house.

    A man who looks back might turn the car around, and I have decided not to be that man today.

    The engine holds. The road, for me, stays empty.

    Mile after mile, and not a soul on it.
    """

    jump captain_ending_survives


# ------------------------------------
#   SHARED — the car ride that ends in ambush
#
#   Called from the afternoon "leave together" branch, once all four are aboard
#   the car at the front of the manor.
# ------------------------------------
label captain_day3_car_ride_ambush:

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
    I get out to look at the engine, because that is what a man does, and because I cannot think what else to do.

    The wood on either side is very still.

    Too still.

    I understand, in the last clear moment I am granted, that the car was never meant to carry us far.
    """

    play sound gun

    jump captain_ending_car_ambush
