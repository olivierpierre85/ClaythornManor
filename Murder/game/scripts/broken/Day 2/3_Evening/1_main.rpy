# --------------------------------------------
#   Broken
#
#   Saturday - Evening (after the hunt)
#
#   15:00 -> 23:30
#
#   Music: chill, mysterious, sad, scary
#
#   Position
#       - House : Lady Claythorn, Captain, Doctor, Mr Manning, Miss Baxter, Miss Marsh, Broken (+ staff)
#       - Dead  : Lad (Ted Harring)
#
#   Structure:
#       - Return from the hunt; the police are delayed by a fallen tree
#       - Quiet dinner (only the hostess within talking distance)
#       - Gate 1, at dinner: without found_poison (the scullery bottle stayed
#         where the killer left it) the meal is poisoned and everyone
#         collapses -> broken_ending_poisoned
#       - Night map (0_map_choices.rpy): call on every bedroom, and find the
#         Captain and Mr Manning in the tea room (2_tea_room.rpy) to arrange
#         a watch -> unlocks gather_everyone
#       - Gate 2, at night: without gather_everyone the manor is set alight
#         while everyone sleeps -> broken_ending_burned; with it the watch
#         holds, Broken sees the motor car leave at four -> broken_day3_morning
# --------------------------------------------
label broken_day2_evening:

    $ broken_details.add_checkpoint("broken_day2_evening")

    call change_time(15, 00, 'Evening', 'Saturday', chapter='saturday_evening')

    call black_screen_transition("Thomas Moody", chapters_names[current_chapter])

    $ play_music('chill', 2)

    $ change_room('entrance_hall', dissolve)

    """
    We come back to the manor, exhausted and quiet.

    The butler takes our rifle back to the gun room.

    He looks distraught for some reason.

    Lady Claythorn, Miss Baxter and Miss Marsh are in the hall to meet us.
    """

    psychic """
    Welcome back, how was the hunt?
    """

    captain """
    We had a nice day out in the woods, but sadly we are coming back empty-handed.
    """

    host """
    These things happen, Captain.

    No need to worry, we didn't rely on this hunt for our dinner tonight.
    """

    captain """
    Of course, I did not want to imply we were.

    I am sure the dinner will be lovely.
    """

    broken """
    By the way, have the police arrived yet?
    """

    nurse """
    No, nobody has come yet.

    But they should arrive soon.
    """

    host """
    I am sure they will.

    In the meantime, we can all take the opportunity to go and change.

    We can gather again for dinner at the usual time.
    """

    $ change_room('bedroom_broken', dissolve)

    call change_time(17, 00)

    """
    I return to my room to change, and take the opportunity of a moment alone to think.

    I am still not sure what is happening here.

    All I know is that this whole event is a lie, but I cannot make out its ultimate goal.

    But the letters left for Thomas and Samuel Manning leave no doubt.

    We are all in danger here.

    Maybe I should stop treating this like a story, and run while I still have the time.

    I really hope the police will arrive soon, and put an end to this madness.

    The police.

    A thought occurs to me, am I really sure they will come?

    The host didn't seem surprised they were not there yet.

    But I would assume that when an unnatural death is reported, they would come at once.

    And I know that Lady Claythorn is lying and hiding something.

    She is obviously very suspicious here, I shouldn't trust whatever she said.

    So maybe I should check for myself.

    The telephone is in the entrance hall, I should try it as soon as I have the opportunity.

    I sit on my bed, and try to think of what I should do.
    """

    call change_time(18, 30)

    play sound dinner_gong

    """
    I am still deep in my thoughts when the gong rings.
    """

    $ change_room('dining_room', irisout)

    $ play_music('sad', 2)

    """
    We all take our usual seats around the dining table.

    I glance at Ted Harring's empty chair, and think it could have been worse had I not intervened with Samuel Manning.

    Lady Claythorn rises to address us.
    """

    host """
    Now that everyone is here, I want to express my deepest regret for what happened this morning.

    This isn't how I imagined our weekend.

    Nevertheless, I hope you enjoyed today's activities.

    Tomorrow, if the weather allows it, a game of croquet will be held in the garden, followed by an outdoor lunch.

    Afterwards, you'll receive your rewards, then you will be free to return home.

    For now, enjoy your dinner.

    Drinks will be available in the billiard room afterwards, as they were yesterday.
    """

    broken """
    Excuse me, Lady Claythorn, if I may, have you received any news from the police?
    """

    host """
    Right, I forgot to tell you.

    We telephoned the police station moments ago.

    I am afraid they won't be coming today.
    """

    call common_day2_evening_police_tree_explanation

    host """
    But you should not worry, I am sure everything will be sorted tomorrow morning.
    """

    """
    The police won't come, just as I feared.

    One more reason to be cautious tonight.

    The meal is served quickly after that.

    Everyone is rather quiet and I do not feel like talking either.

    But if I don't engage with our host, it could be seen as rude, or even suspicious.
    """

    call change_time(19, 30)

    $ time_left = 90

    call run_menu(TimedMenu("broken_day2_evening_menu_dinner", [
        TimedMenuChoice("Speak to Lady Claythorn", 'broken_day2_dinner_host', early_exit=True),
        TimedMenuChoice("Keep my own counsel", 'generic_cancel', early_exit=True),
    ], image_right = "host"))

    call change_time(21, 00)

    if not broken_details.threads.is_unlocked('found_poison'):

        # The bottle of rat poison stayed in the scullery, and tonight it has
        # found its way into the dinner. Everyone is poisoned; he collapses
        # among the first.
        $ stop_music()

        """
        The wine goes round a last time, and I let the footman fill my glass.

        It is Miss Marsh who falters first. Her spoon stops halfway to her lips, and her face goes the colour of the tablecloth.

        Then a heat rises in my own chest, and the room tilts.

        Across the table the Captain is on his feet, swaying, one hand knotted in the cloth.

        Somebody's glass breaks. Somebody screams. The sounds reach me from a long way off.

        My legs give before I can reach the door.

        The last thing I see is our hostess rising from her chair, and I cannot tell if she is screaming too.
        """

        jump broken_ending_poisoned

    """
    The dinner ends as quietly as it began.

    Lady Claythorn wishes us each a good night, and the party rises from the table without ceremony.

    The others drift towards the stairs and I follow them.
    """

    $ change_room('bedroom_broken', dissolve)

    call change_time(21, 15)

    $ stop_music()

    """
    I lock my door, and take a moment to think of what to do.

    I know Lady Claythorn is not to be trusted, she has probably conspired to hurt Captain Sinha, as well as Doctor Baldwin.

    And Ted Harring's death is probably not accidental either.

    Whatever is happening here, nobody is safe.

    If I don't do anything, I am afraid some of us might not survive the night.

    But leaving now is impossible, even if there were nothing wrong with the road.

    I doubt Lady Claythorn will just lend us her car.

    But what could I do?

    First, I have opened up to Samuel Manning, he is the one person I feel I could trust tonight.

    Doctor Baldwin and Captain Sinha were both intended victims, so logically, I could trust them as well.

    Logically.

    But everything is so twisted I am not sure of anything right now.
    """

    """
    Then it comes to me that thinking is not what this night needs.

    If nobody is safe alone, then nobody should be alone. It is as simple as that.

    I shall knock on every door in this house if I must, and put a watch on the night.

    Manning and the Captain first, if they are still up.

    And there is the telephone in the entrance hall to try along the way.
    """

    # Night map: call on the bedrooms (most won't answer, some hide) and find
    # the Captain and Mr Manning in the tea room. Warning the pair AND calling
    # at every occupied door unlocks gather_everyone (see 0_map_choices.rpy).
    $ play_music('mysterious', 2)

    call change_time(21, 30)

    $ time_left = 120

    call run_menu(broken_details.saved_variables["day2_evening_map_menu"])

    call change_time(23, 30)

    $ change_room('bedroom_broken', dissolve)

    $ stop_music()

    if not broken_details.threads.is_unlocked('gather_everyone'):

        # He never gathered the others: the house sleeps unguarded, and the
        # manor is set alight in the night.
        """
        The house is dark, and every man and woman in it is shut away alone behind their own door.

        I meant to do more. The night ran out before my nerve found its feet.

        I sit against the headboard, meaning to keep my eyes open until morning.

        I do not manage it.
        """

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

    # gather_everyone path: the watch holds through the night.
    """
    The watches are set.

    Captain Sinha takes the first, with Mr Manning for company, posted on the landing where every bedroom door can be seen.

    The ladies are barred in their rooms, and the doctor sleeps his heavy sleep behind his own locked door.

    Mine is the dead stretch, from two o'clock until dawn.

    I sleep in my clothes, three grey hours of half-sleep, and take my chair out to the landing when Manning taps at my door.
    """

    pause 1

    """
    Some time past four, sounds rise from below.

    Quiet feet on the gravel, a door eased shut, and then the cough of a motor car.

    From the landing window I watch its lamps slide away down the drive until the dark takes them.

    So much for the tree across the road.

    Nobody else stirs. I hold my post, and wait for the grey of morning.
    """

    jump broken_day3_morning


# ------------------------------------
#   DINNER SCENES
# ------------------------------------
label broken_day2_dinner_host:

    broken """
    You have kept a steady hand on the house today, Lady Claythorn.

    It cannot have been an easy day to preside over.
    """

    host """
    You are kind to say so, Mr Moody.
    """

    """
    I could ask her more questions, but I feel I have learned what I needed to know about her.
    """

    call host_generic

    return
