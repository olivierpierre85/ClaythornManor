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
#       - 2_captain.rpy : broken_day2_hunt_captain  (shadow the Captain -> death)
#       - 3_drunk.rpy   : broken_day2_hunt_drunk (shadow the Drunk)
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

    The letter still lies on my bedside table.

    If I am to believe it, Captain Sinha put his name to the order that sent Tom up to the line.

    Because of that, Tom came back from the war behind a mask, and lived a small and lonely life until his wounds got the better of him.

    A thought occurs to me, one I do not like but cannot ignore.

    And a hunt is a careless sort of business.

    Accidents happen.
    """

    $ change_room('gun_room')

    """
    The butler is in the gun room, attending the rifles with his unhurried care.

    He hands me a rifle.

    It has been years since I last held a rifle, yet it settles into my hands like an old habit.

    I check the action, sight along the barrel, and find it true.

    I shall not embarrass myself today.
    """

    $ change_room('manor_garden')

    """
    The others are already gathering on the lawn.

    Two different groups are forming: Captain Sinha with Lady Claythorn and Samuel Manning with Doctor Baldwin.

    It looks like it is up to me to decide which party I will join.
    """

    if broken_details.threads.is_unlocked('talked_to_maid'):

        """
        My first instinct is to follow Captain Sinha.

        I simply cannot ignore the letter.

        Being close to him will allow me to learn more of it.

        Yet, I do not trust what is happening here this weekend.
        
        The letter, the hunt, the surprise the maid could not put a name to.

        Making me follow the captain is probably the goal of whoever organised this.

        So, which group should I join?
        """

        $ time_left = 1
        call run_menu(
            TimedMenu("broken_day2_hunt_menu_party", [
                TimedMenuChoice("Lady Claythorn and Captain Sinha", 'broken_day2_hunt_captain', early_exit=True),
                TimedMenuChoice("Join Doctor Baldwin and Samuel Manning instead", 'broken_day2_hunt_drunk', early_exit=True),
            ], image_right = "host", image_right_2 = "captain", image_left = "drunk", image_left_2 = "doctor"))

    else:

        """
        But I do not hesitate for a second.

        I do not know what I will do yet, but I need to be with Captain Sinha.        
        """

        jump broken_day2_hunt_captain
