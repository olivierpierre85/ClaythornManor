# --------------------------------------------
#   Broken
#
#   Saturday - Evening (after the hunt)
#
#   15:00 -> 23:00
#
#   Music: chill, mysterious, sad, scary
#
#   Position
#       - House : Lady Claythorn, Captain, Doctor, Mr Manning, Miss Baxter, Miss Marsh, Broken (+ staff)
#       - Dead  : Lad (Ted Harring)
#
#   Reached only from broken_day2_hunt_drunk (drunk_letter drawn out, Mr Manning
#   talked down) - the one hunt outcome in which nobody dies. Only Ted Harring
#   is dead so far.
#
#   Structure:
#       - Return from the wood, rifles handed back, the fallen-tree news
#         (the police delayed until Sunday)
#       - Taking stock in his room (found_poison variant)
#       - A quiet dinner with one empty chair (reuses common_day2_evening_dinner_host)
#       - The gate:
#           - found_poison -> he refuses to sleep: map exploration (billiard
#             room with the Captain and Mr Manning, see 0_map_choices.rpy and
#             2_billiard_room.rpy), then the night vigil - he watches the
#             staff's motor car slip away at four in the morning, and goes on
#             to broken_day3_morning
#           - otherwise    -> he retires, and the manor burns in the night
#             (broken_ending_burned)
# --------------------------------------------
label broken_day2_evening:

    $ broken_details.add_checkpoint("broken_day2_evening")

    call change_time(15, 00, 'Evening', 'Saturday', chapter='saturday_evening')

    call black_screen_transition("Thomas Moody", chapters_names[current_chapter])

    $ change_room('manor_garden')

    $ play_music('chill', 2)

    """
    We come back across the lawn in one straggling line, and every man of us is breathing.

    By any honest measure the morning was a failure. Nothing in the bag worth the cartridges, and precious little said on the walk home.

    I count it a victory all the same.

    Mr Manning stays at my side the whole way, quiet as a church.

    Neither of us says a word about the wood, and neither of us needs to.
    """

    $ change_room('gun_room', dissolve)

    """
    The butler stands at the gun room door and takes each rifle back as we file past.

    If he is surprised to see the whole party walk home on its own legs, his face gives nothing away.

    But his eyes go from man to man as we pass, and I would swear he is counting.
    """

    $ change_room('entrance_hall', dissolve)

    """
    Miss Baxter and Miss Marsh are in the hall to meet us.
    """

    psychic """
    Well, gentlemen? How was your sport?

    No misadventures, I trust?
    """

    captain """
    None, madam.

    A quiet morning, and poor shooting.
    """

    """
    A quiet morning.

    I catch Mr Manning's eye, and he looks away.

    Between the two of us, we are the only ones who know how near the truth came to being otherwise.
    """

    $ play_music('mysterious', 2)

    """
    Before the party can scatter, the butler comes up from the back of the hall and murmurs a word to Lady Claythorn.

    Her mouth thins, and she turns to the rest of us.
    """

    host """
    I am afraid I have some tiresome news.

    The police have telephoned. A tree has come down across the road this morning, and they cannot bring a motor past it.

    They will be with us tomorrow, with men to clear the way.
    """

    captain """
    Tomorrow? And Mr Harring lying upstairs all the while?
    """

    host """
    I am sorry, Captain. They were quite firm on the point.

    There is simply nothing to be done before then.
    """

    """
    A fallen tree. It is possible. Trees do fall.

    But set beside the rest of it, the letters, the hunt, a staff hired for a single weekend, it reads less like weather and more like a bolt being drawn across a door.

    Nobody leaves, and nobody arrives.

    Whatever this house means to do with us, it now has until tomorrow to do it in.
    """

    $ change_room('bedroom_broken', dissolve)

    call change_time(17, 00)

    """
    In my room, I sit on the edge of the bed and lay the day out in order, the way I would lay out notes for a difficult piece.

    Item. A letter under my door, pointing me at the Captain.

    Item. A letter under Mr Manning's, pointing him at the doctor.

    Item. Ted Harring, dead in his bed, without a mark on him and without a cause.

    Item. A road that has closed itself behind us like a trap.

    Two loaded guns were laid out on a table this morning, and neither went off.

    I cannot think the author of all this will simply shrug and go home.
    """

    if broken_details.threads.is_unlocked('found_poison'):

        """
        And there is one item more, which nobody else has.

        I take the bottle from my coat and turn it under the lamp.

        Rat poison, uncorked, and a fair measure of it already gone. Left on a scullery shelf where any hand could reach it.

        Harring died without a mark, and the doctor could put no name to what killed him.

        I could put a name to it.

        I slip the bottle back into my coat, and it weighs more than it did.
        """

    """
    I could carry all of this down and lay it before the Captain.

    And he would ask, quite reasonably, how I come to know any of it, and who I am when the mask comes off.

    That is a door I cannot open. Not yet.

    So I keep my own counsel, and wait for the gong.
    """

    call wait_screen_transition()

    call change_time(18, 30)

    play sound dinner_gong

    $ change_room('dining_room', irisout)

    $ play_music('sad', 2)

    """
    The places have been drawn closer together tonight, so that the empty length of the table does not show.

    It shows all the same.

    Nobody sits where Harring sat, and nobody looks at it either.

    Mr Manning has been moved up the table, almost to my elbow. He has washed and shaved and put on a clean collar, and before him stands a glass of wine he does not once reach for.

    I have seen men wear that look before, in the weeks after the Armistice. Men handed back a life they had already signed away.

    The doctor eats little and notices less. He does not know he owes tonight's dinner to the man sitting three feet from him.

    And the Captain is as he always is, upright and correct, telling no stories for once.

    I watch him and wait for the old anger to rise, and find it quieter than it was.

    The order has not changed. But I have seen this morning what letters like mine are written to make men do.
    """

    """
    Lady Claythorn rises to address us.
    """

    call common_day2_evening_dinner_host

    """
    Rewards in the morning, the police to follow, and drinks in the billiard room tonight, as though good manners might still save the weekend.

    I look around the table and wonder how many of us believe a single word of it.
    """

    if broken_details.threads.is_unlocked('found_poison'):

        """
        For my own part, I drink water, and touch nothing I have not watched come out of the tap.

        The bottle in my coat has quite spoiled my taste for this house's cellar.
        """

    else:

        """
        I take a glass of the wine because my nerves ask for it, and a second because the first goes down so easily.

        It is a heavier vintage than yesterday's, and the butler keeps the glasses filled without being asked.
        """

    $ time_left = 1
    call run_menu(TimedMenu("broken_day2_evening_menu_dinner", [
        TimedMenuChoice("Speak to Mr Manning", 'broken_day2_evening_dinner_manning', early_exit=True),
        TimedMenuChoice("Keep my own counsel", 'generic_cancel', early_exit=True),
    ], image_right = "drunk"))

    call change_time(21, 00)

    """
    The dinner ends as quietly as it began.

    Lady Claythorn wishes us each a good night, and the party rises from the table without ceremony.
    """

    if broken_details.threads.is_unlocked('found_poison'):

        jump broken_day2_evening_stay_awake

    jump broken_day2_evening_retire


# --------------------------------------------
#   FOUND THE POISON - he refuses to sleep and presses on
# --------------------------------------------
label broken_day2_evening_stay_awake:

    $ play_music('mysterious', 2)

    """
    The others drift towards the stairs and the billiard room, and I stand a moment in the hall with my hand on the banister.

    I am tired to the bone, and a bed has rarely argued its case so well.

    But the bottle sits in my coat like a stone.

    Harring drank in this house, and slept in this house, and did not wake.

    Whoever left that poison on a shelf has had a full day to find a new use for it, and here we all are, being wished a good night and sent up to our beds.

    No.

    Tonight I do not sleep.

    There is a man in the billiard room who has lost his taste for drink, a staff below stairs hired for one weekend only, and questions enough between them to keep me up until dawn.

    Time to go to work.
    """

    $ change_room('entrance_hall')

    call change_time(21, 30)

    $ time_left = 90

    call run_menu(broken_details.saved_variables["day2_evening_map_menu"])

    call change_time(23, 00)

    $ stop_music()

    """
    The house has gone quiet around me, room by room.

    I have seen what there is to see for one night, and the hardest part of it still lies ahead.

    Staying awake until morning.
    """

    $ change_room('bedroom_broken', dissolve)

    $ play_music('mysterious', 2)

    """
    I go up to my room at last, and I do not undress.

    I set the chair where it commands the door, stand the poison bottle on the table where I can see it, and turn the lamp down low.

    The house settles around me, board by board.

    I have sat up all night for a story before. Never for my life.
    """

    call wait_screen_transition()

    """
    Some time past four, when the dark is at its thickest, I hear it.

    Not a footstep. An engine.

    I put out the lamp and go to the window.

    Below, on the drive, the motor car rolls away from the house with its lamps unlit, the gravel crackling soft under its wheels.

    It does not hurry.

    I watch its shape sink into the black of the trees, and I cannot see who is inside.

    But no household slips away from its own guests in the dead of night, lamps out, unless the next part of the programme is one it would rather not be present for.

    Morning cannot come quickly enough.
    """

    jump broken_day3_morning


# --------------------------------------------
#   NO POISON - he retires, and the manor burns in the night
# --------------------------------------------
label broken_day2_evening_retire:

    """
    The others drift towards the stairs and the billiard room, and I stand a moment in the hall, weighing the evening.

    Something in me does not care for any of it. The road, the letters, the empty chair at dinner.

    But it is a feeling only, with nothing solid beneath it, and I have been carrying another man's face since Friday.

    I am wrung dry.

    The police come tomorrow. Whatever I mean to do about any of it, I shall do it better for a night's sleep.
    """

    $ change_room('bedroom_broken', dissolve)

    call change_time(22, 30)

    $ stop_music()

    """
    I lock my door, and take off the mask, and the face underneath it is more tired than the one on top.

    The wine has made my limbs heavy and my thoughts slow.

    Sleep takes me before I have finished deciding to allow it.
    """

    call wait_screen_transition()

    $ play_music('scary')

    play sound fire loop

    """
    Somewhere very far away, glass breaks.

    I swim up towards waking and do not reach it.

    The room is warm. The dark has a taste to it now, thick and bitter.

    Smoke.

    My body understands before my mind does, but my arms are lead, and the door is a mile away across the carpet.

    The last thing I know is the line of light beneath it. Bright, and orange, and moving.
    """

    jump broken_ending_burned


# ------------------------------------
#   DINNER SCENES
# ------------------------------------
label broken_day2_evening_dinner_manning:

    """
    I lean towards him a little, and keep my voice under the talk.
    """

    broken """
    You are not drinking, Mr Manning.
    """

    drunk """
    No.

    No, I find I have rather lost the taste for it.
    """

    """
    He turns the stem of the glass between two fingers, and looks at it the way a man looks at an old enemy.
    """

    drunk """
    Mr Moody. This morning, in the wood.

    What you kept me from...
    """

    broken """
    Was nothing at all, Mr Manning, because nothing at all took place.

    A quiet morning, and poor shooting. We shall leave it there.
    """

    """
    He nods, slowly, and something crosses his face that might, in a better week, have been a smile.
    """

    drunk """
    A quiet morning. Yes.

    Then I shall say only this, sir. If you should ever have need of me, for anything at all, you shall have me sober.
    """

    """
    I have made no friends behind this mask.

    It occurs to me, passing him the water jug, that this ruined old fellow may prove to be the first.
    """

    return
