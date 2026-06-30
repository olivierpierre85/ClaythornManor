# --------------------------------------------
#   Broken
#
#   Saturday - The Hunt
#
#   11:00 -> 13:30
#
#   Music: upbeat, danger, mysterious
#
#   Position
#       - House, Tea room : Miss Marsh, Miss Baxter
#       - Forest          : Lady Claythorn, Captain, Doctor, Mr Manning, Broken (+ butler, footman)
#       - Dead            : Lad (Ted Harring)
#
#   This file is the entry point: the change, the gathering, the pairing, and
#   the choice of which party to join. The two paths live in their own files:
#       - 2_captain.rpy : broken_day2_hunt_north  (shadow the Captain -> death)
#       - 3_drunk.rpy   : broken_day2_hunt_western_grove (shadow the Drunk)
#
#   Choice gate: WITHOUT talked_to_maid the path is forced (north -> kill).
#   WITH it, the player picks the party (broken_day2_hunt_menu_party); shadowing
#   the Captain still ends in Broken's death, while the grove path can save him.
#
#   The pairing is shared with the Captain's storyline:
#       - common_day2_hunt_pairing
# --------------------------------------------
label broken_day2_hunt:

    $ broken_details.add_checkpoint("broken_day2_hunt")

    call change_time(11, 0, 'The Hunt', 'Saturday', chapter='saturday_afternoon')

    call black_screen_transition("Thomas Moody", chapters_names[current_chapter])

    $ change_room('bedroom_broken')

    $ play_music('mysterious', 2)

    """
    I return to my room to change into the tweeds the household has laid out for me.

    My hands are steady as I dress. Steadier than they have any right to be.

    The letter still lies on my bedstand.

    If I am to believe it, Captain Sinha put his name to the order that sent Tom up to the line.

    Picked him up amongst other possible candidates, likely due to his background.

    Because of that, Tom came back from the war behind a mask, and lived a small and lonely life until his wounds got the better of him.

    A thought occurs to me, one I do not like but cannot ignore.

    And a hunt is a careless sort of business.

    Accidents happen.
    """

    $ change_room('gun_room')

    """
    The butler is in the gun room, attending the rifles with his unhurried care.

    He hands me a piece.

    It has been years since I last held a rifle, yet it settles into my hands like an old habit.

    I check the action, sight along the barrel, and find it true.

    I shall not embarrass myself today.
    """

    $ change_room('manor_garden')

    """
    The others are already gathering on the lawn.

    Doctor Baldwin stands a little apart, grey and unwell.

    Samuel Manning is a sorry sight, swaying where he stands.

    Lady Claythorn is the last to come out.

    And the Captain. Upright. Correct.

    A decorated officer at his ease, at least in appearance.
    """

    if broken_details.threads.is_unlocked('talked_to_maid'):

        """
        The maid's words come back to me. A surprise, she said, prepared for the guests.

        A letter slipped beneath my door, and a hunt laid on the very next morning.

        It is too neat by half. I know it, somewhere beneath the anger.

        But knowing a thing and heeding it are not at all the same, and the anger is by far the louder of the two.
        """

    call common_day2_hunt_butler_groups

    call common_day2_hunt_pairing

    if broken_details.threads.is_unlocked('talked_to_maid'):

        """
        I do not trust a line of this morning. The letter, the hunt, the surprise the maid could not put a name to.

        If the Captain has been set before me like a target, then perhaps he is not the only one who has been arranged.

        And there is the drunkard, wound tight as a watch-spring, his eyes forever sliding back to the doctor.

        I should dearly like to know what is the matter with Mr Manning.
        """

        $ time_left = 1
        call run_menu(
            TimedMenu("broken_day2_hunt_menu_party", [
                TimedMenuChoice("Make up Lady Claythorn's party, and keep the Captain close", 'broken_day2_hunt_north', early_exit=True),
                TimedMenuChoice("Join the Doctor and Mr Manning instead", 'broken_day2_hunt_western_grove', early_exit=True),
            ])
        )

    else:

        jump broken_day2_hunt_north
