# --------------------------------------------
#   Broken - Saturday Hunt - With the Captain (north field)
#
#   Reached from broken_day2_hunt (1_main.rpy):
#       - forced when talked_to_maid is NOT set
#       - chosen from the party menu when it is
#
#   The north-field hunt and the kill are shared with the Captain's storyline
#   (common_day2_hunt_north_field / common_day2_hunt_captain_confrontation).
#   Either outcome gets Broken killed by the butler:
#       - kill  -> broken_ending_shot
#       - spare -> broken_ending_strangled
#   The spare option requires talked_to_maid; without it the kill is forced.
# --------------------------------------------
label broken_day2_hunt_captain:

    """
    Now that the groups are set, we make our way into the woods.
    """

    call common_day2_hunt_north_field

    """
    The Captain says nothing to that. He only smiles, thin and correct.

    We settle for luncheon in a clearing among the birches. The butler lays a cloth and pours the tea with his customary care.
    """

    host """
    Captain, I have been told you are an amazing story teller.

    Isn't there a story you would like to share with us?
    """

    captain """
    There is little worth the telling, my lady.

    But if it would amuse you, I might tell you about the "War of the Golden Stool", one of my first campaigns.
    """

    host """
    What an intriguing name, please do tell.
    """

    """
    So he does, modest and precise, with the ease of a man who has told it across a hundred dinner tables.

    Lady Claythorn leans in, delighted.

    I, on the other hand, feel the anger rising as the story progresses.

    If the letter is correct, and I have started to accept it is, this man was always safe behind a desk.

    But he is playing the hero, as if he were solely responsible for England's victory.

    My thumb finds the cold of the trigger guard where the rifle rests across my knee.
    """

    if broken_details.threads.is_unlocked('talked_to_maid'):

        """
        And still the maid's words will not leave me. A surprise, prepared for the guests.

        The letter left in my room. The hunt laid on the very next morning.

        The Captain, set before me like a target on a wall.

        It is too obvious that someone is trying to use me.
        """

        $ time_left = 1
        call run_menu(
            TimedMenu("broken_day2_hunt_menu_revenge", [
                TimedMenuChoice("It doesn't matter. He is a liar and has to pay", 'broken_day2_hunt_kill', early_exit=True),
                TimedMenuChoice("Spare him", 'broken_day2_hunt_spare', early_exit=True),
            ])
        )

    else:

        """
        There is no doubt left in me now.
        """

        jump broken_day2_hunt_kill


# --------------------------------------------
#   KILL - Broken gives in to the anger and shoots the Captain
# --------------------------------------------
label broken_day2_hunt_kill:

    """
    Anger has overwhelmed me and it is too late to go back now.

    I let the talk run on a little longer, and gather myself, and wait for my opening.
    """

    call common_day2_hunt_captain_confrontation

    $ play_music('mysterious', 2)

    """
    The shot rolls away through the trees and is swallowed by them.

    Captain Sinha lies where he fell, and there is nothing of the soldier left in him now.

    I wait for the satisfaction of it.

    For something to fill the hole that has sat in my chest since they put Tom in the ground.

    It does not come.

    There is only a dead man in the bracken, and my two hands, and the quiet.

    What have I done?

    My mind races, trying to work out what to do next.

    Then, I realise I am not alone.

    The butler is standing not three paces away.

    I never heard him come.

    He looks at the Captain's body, and then kneels next to it.
    """

    butler """
    Cleanly done, Mr Moody.

    Or whatever your name is, beneath that mask.

    It hardly matters now.
    """

    """
    Then he picks up the Captain's rifle,

    and turns it against me.
    """

    """
    I bring my own rifle up.

    Too late.
    """

    play sound gun

    jump broken_ending_shot


# --------------------------------------------
#   SPARE - Broken refuses to be used; the trap springs elsewhere
#   (requires talked_to_maid)
# --------------------------------------------
label broken_day2_hunt_spare:

    """
    No, I cannot kill the man.

    Even if he is a liar, a fraud, what is happening here is too suspicious.

    I let the rage go cold in my hands.

    I let the Captain finish his story.

    Whoever drew us here wanted him dead by my hand, or more likely by Thomas's hand.

    That is the thing I must focus on.
    """

    $ play_music('danger', 2)

    play sound gun

    pause 0.5

    """
    The thought has scarcely formed when a shot cracks from the direction of the other party.

    Then, thin between the trees, a cry.

    My blood runs cold.

    Before I can move, the Captain is on his feet and away.

    I go after him but he is faster than I would have guessed, the gap between us widening with every stride.

    After a while I have to stop to catch my breath.

    Then I hear someone right behind me.

    I try to turn to see who that is.

    But before I can see, I feel a band of leather draw tight across my throat.

    I struggle to fight it off.

    But I am already out of breath, and have not enough strength left to defend myself.
    """

    jump broken_ending_strangled
