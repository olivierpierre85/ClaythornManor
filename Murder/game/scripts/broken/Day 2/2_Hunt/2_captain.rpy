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
#       - kill  -> broken_ending_silenced
#       - spare -> broken_ending_overtaken
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

    Isn't there a story you would like to share with us.
    """

    captain """
    There is little worth the telling, my lady.

    But if it would amuse you, I might give you the relief of Tientsin. The heat of it, and the walls.
    """

    """
    And he is away, modest and precise, with the polished ease of a man who has told it across a hundred dinner tables.

    Lady Claythorn leans in, delighted.

    I sit very still and let it wash over me.

    This man was always safe behind a desk, but he is playing the hero over the sandwiches.
    
    While Tom came home behind a mask and died by inches for the want of the very courage this fraud counterfeits so prettily.

    My thumb finds the cold of the trigger guard where the rifle rests across my knee.
    """

    if broken_details.threads.is_unlocked('talked_to_maid'):

        """
        And still the maid's words will not leave me. A surprise, prepared for the guests.

        The letter beneath my door. The hunt laid on the very next morning. The Captain set before me like a bottle on a wall.

        Whoever arranged all this knew to a nicety what that order would do to me. They have written the scene and handed me the gun, and I am three lines from speaking my piece.

        A man who kills to another's design is no avenger. He is a tool. And I have spent a year despising the men who let themselves be used.
        """

        """
        For the first time since I read that paper, I am not certain of my own hand.
        """

        $ time_left = 1
        call run_menu(
            TimedMenu("broken_day2_hunt_menu_revenge", [
                TimedMenuChoice("Stay my hand. I'll not dance to a stranger's tune.", 'broken_day2_hunt_spare', early_exit=True),
                TimedMenuChoice("Design or not, his name is on the order. Lead him away.", 'broken_day2_hunt_kill', early_exit=True),
            ])
        )

    else:

        """
        There is no doubt left in me to stay my hand.

        Whatever game is being played beneath this roof, the name at the foot of that order is his, and Tom is in the ground.

        That has always been enough.
        """

        jump broken_day2_hunt_kill


# --------------------------------------------
#   KILL - Broken gives in to the anger and shoots the Captain
# --------------------------------------------
label broken_day2_hunt_kill:

    """
    I let the talk run on a little longer, and gather myself, and wait for my opening.
    """

    call common_day2_hunt_captain_confrontation

    $ play_music('mysterious', 2)

    """
    The shot rolls away through the trees and is swallowed by them.

    Captain Sinha lies where he fell, and there is nothing of the soldier left in him now.

    I wait for the satisfaction of it. For something to fill the hollow that has sat in my chest since they put Tom in the ground.

    It does not come.

    There is only a dead man in the bracken, and my two hands, and the quiet.
    """

    pause 1.0

    play sound gun

    pause 0.5

    """
    Then, from the direction of the other party, another shot. And after it, faint and thin between the trees, a cry.

    The doctor, or the drunkard, or both. It scarcely matters which.

    Whoever drew us under this roof wanted blood this morning, and every one of us has proved so very willing to spill it.

    Two men dead before the luncheon is cleared away, and the day not yet half gone.
    """

    """
    I have no time for the horror of it. The shot will have carried back to the clearing, and they will come looking.

    I compose my face behind the mask, take up my rifle, and turn to start back the way we came.
    """

    """
    The butler is standing not three paces away.

    I never heard him come. A big man, and yet he moves through the wood without a sound.

    He looks at the Captain's body, and then at me, with about as much feeling as a man might spare for a hare in a snare.
    """

    butler """
    Cleanly done, Mr Moody.

    Or whatever your name is, beneath that mask. It hardly signifies now.
    """

    """
    He knows. Of course he knows.

    The letter, the hunt, the Captain laid across my path. None of it was ever mine. It was theirs from the very first, and I have played my part exactly as it was written for me.
    """

    broken """
    You. You wanted this.
    """
    
    """
    I bring the rifle up.

    Too slow. I was always going to be too slow.

    He is behind me before the barrel has cleared my hip, and a thin band of leather draws tight across my throat.
    """

    jump broken_ending_silenced


# --------------------------------------------
#   SPARE - Broken refuses to be used; the trap springs elsewhere
#   (requires talked_to_maid)
# --------------------------------------------
label broken_day2_hunt_spare:

    """
    No.

    I have spent a year hating the men who did the cruel thing because a cleverer man had arranged for them to do it.

    I'll not become one more of them. Not even for Tom. Least of all for Tom.

    I let the rage go cold in my hands. I let the Captain talk. I say nothing of the letter at all.
    """

    captain """
    ... and so we held until the relief came up. A near thing, but a good one.
    """

    broken """
    A remarkable account, Captain.
    """

    """
    Whoever drew us here wanted him dead by my hand. Of that I am now certain.

    Which means the danger was never the Captain at all. The danger is whoever wrote this morning for us, and they will not have written only the one death.
    """

    $ play_music('danger', 2)

    play sound gun

    pause 0.5

    """
    The thought has scarcely formed when a shot cracks from the direction of the other party. Then a second. And after them, thin between the trees, a cry.

    My blood runs cold.

    The doctor. They have left him alone with that poor drunken wreck, and I have sat here playing at conscience while the next act began without me.
    """

    """
    Before I can move, the Captain is on his feet and away, crashing through the undergrowth toward the sound far faster than I would have given him credit for.

    Lady Claythorn does not follow. She stays beside the cloth, very still, her hands folded in her lap, watching us go.

    I go after the Captain as best I can, the bracken dragging at my legs, the gap between us widening with every stride.

    And somewhere in the green hush, between the fleeing man ahead and the seated woman behind, it comes to me that I have not once seen the butler since the shots rang out.
    """

    """
    A footfall behind me. Close. Unhurried.

    I begin to turn.
    """

    butler """
    Not that way, sir.
    """

    """
    Something hard presses itself between my shoulders, and I understand, far too late, that I was never meant to reach the other party at all.

    Ahead of me, the Captain runs on, and does not look back, and never knows.
    """

    jump broken_ending_overtaken
