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

    if captain_details.threads.is_unlocked('confide_in_nurse'):

        # Nurse path — the captain and Miss Marsh waited out the morning in the
        # butler's room. They come down at last, and find the others.
        $ change_room('bedrooms_hallway', irisout)

        """
        Miss Marsh and I come down from the attic at last.
        """

        $ change_room('entrance_hall', dissolve)

        """
        We are making for the kitchen when we hear voices in the hall below.

        Living voices.
        """

        lad """
        Captain Sinha!
        """

        """
        Ted Harring and Miss Baxter cross the hall towards us, plainly relieved to find us upright.
        """

        psychic """
        Thank heaven. We had begun to think we were the last souls left in the place.
        """

        lad """
        We have been over the whole house, top to bottom.

        There is a motor car in the garage, but not a drop of petrol to put in it.

        Whoever left made very sure of that.
        """

        captain """
        Then the road is all that is left to us.

        Come. We had far better talk this through together.
        """

        $ change_room('tea_room', dissolve)

    else:

        # Explore path — the captain finished his sweep of the house. The others
        # rested in the tea room while he worked.
        $ change_room('tea_room', irisout)

        """
        We rested a while in silence, 
        """

    call common_day3_afternoon_lad_psychic_captain_discussion_1

    if captain_details.threads.is_unlocked('seen_car') and captain_details.threads.is_unlocked('petrol_tin_in_shed'):

        captain """
        As it happens, we are not obliged to walk.

        There is an old motor car in the garage.

        It wants petrol, but I found a full tin in the garden shed.

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

        captain """
        There is no telephone, no motor with any fuel in it, and no help coming that I can find.

        If we are to be saved, we must save ourselves, and that means the road.

        It is a long walk, and I will go faster alone.
        """

        psychic surprised """
        Alone? You cannot mean to leave us here.
        """

        captain """
        I can move quicker than any of you, and quicker is what will fetch help before dark.

        Bar the doors, keep together, and wait for me.

        I will bring men back tonight.
        """

        """
        It is not a course I am proud of.

        But it is the only one I can see, and there is no profit in standing about discussing it.
        """

        jump captain_day3_afternoon_on_foot


# ------------------------------------
#   AFTERNOON — leave together by car
#
#   The nurse appears at the threshold and climbs in. Shared ride follows.
# ------------------------------------
label captain_day3_afternoon_car_together:

    call change_time(13, 00)

    $ change_room('manor_garden', dissolve)

    """
    I fetch the tin from the shed, fill the tank, and coax the old engine into life.

    It runs rough, but it runs.

    The boy hands Miss Baxter up into the back, and we are nearly away.
    """

    if not captain_details.threads.is_unlocked('confide_in_nurse'):

        """
        Then a figure comes out of the side door of the house.

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
        She climbs in beside Miss Baxter without another word.

        I do not care for the timing of it.

        But I will not leave a living soul on that gravel.
        """

    else:

        """
        Miss Marsh takes her place beside Miss Baxter.

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
#   AFTERNOON — leave alone on foot
# ------------------------------------
label captain_day3_afternoon_on_foot:

    call change_time(13, 00)

    $ change_room('forest_road', dissolve)

    """
    I take only my coat and what will fit in its pockets.

    The drive gives way to a rough road, and the road to open country between the trees.

    I keep a soldier's pace, or the pace I imagine a soldier keeps.

    For an hour there is nothing but my own breath and the cold.
    """

    $ play_music('danger')

    """
    Then, away to my right, the treeline.

    A branch that does not move with the wind.

    A shape that is the wrong colour for bark.

    I have read enough accounts of ambush to know one when I am standing in it.

    Too late, of course.

    A real soldier would have known an hour ago.
    """

    play sound gun

    jump captain_ending_shot_fleeing


# ------------------------------------
#   SHARED — the car ride that ends in ambush
#
#   Called from the morning nurse "leave early" branch and from the afternoon
#   "leave together" branch. Assumes four are aboard.
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
