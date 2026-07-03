# --------------------------------------------
#   Broken - Saturday Hunt - With the Drunk (western grove)
#
#   Reached from broken_day2_hunt (1_main.rpy) only when talked_to_maid is set
#   and the player chooses to join the Doctor and Mr Manning.
#
#   Broken notices Manning is dangerously on edge and approaches him. The Drunk
#   generic menu (drunk_generic_menu_broken, broken_config_menu.rpy) carries a
#   letter question; asking it unlocks the drunk_letter thread and reveals that
#   Manning, like Broken, was sent a letter (the Doctor killed his wife). That
#   recognition lets Broken talk him down and save both Manning and the Doctor.
#   That path continues into broken_day2_evening (Day 2/3_Evening/1_main.rpy).
#
#   TODO: the branch where Broken never draws out the letter (the Drunk shoots
#   the Doctor) is unwritten and still ends at work_in_progress.
# --------------------------------------------
label broken_day2_hunt_drunk:

    broken """
    If it is all the same to you, my lady, I should sooner go across with Doctor Baldwin and Mister Manning.
    """

    """
    Then I say lower so Samuel Manning is not hearing what I am saying.
    """

    broken """
    Mr Manning looks as though he could do with a steady man at his elbow.
    """

    """
    The Captain inclines his head, plainly relieved to see the back of me.

    If he only knew how near I had come to choosing otherwise.
    """

    butler """
    Very good. Captain Sinha shall accompany my lady, and Mr Moody will join Doctor Baldwin and Mr Manning.

    The footman and I shall divide between the parties.
    """

    call change_time(11, 45)

    $ change_room('forest')

    """
    We strike off to the west, the doctor a few paces ahead, Mr Manning weaving along at my side.

    Baldwin is grey and sweating, sunk in some private misery of his own, and pays neither of us any mind.

    Mr Manning, though, I cannot take my eyes from.

    He has not stopped at the flask since we left the lawn. His hands shake so badly he can scarcely hold it to his lips.

    And his eyes. They go to the doctor's back and stay there, again and again.

    He cleary is in some sort panic, if I want to talk to him, now is the time.

    I drop back a little, and fall into step beside him.
    """

    call drunk_generic

    if broken_details.threads.is_unlocked('drunk_letter'):

        """
        So there it is.

        The same hand that slid an old army order beneath my door slid a letter beneath his, and aimed him at the doctor as it aimed me at the Captain.

        We are not guests at all. We are loaded guns, laid out on a table for someone else to fire.

        Well. I will not go off on command, and I will be damned if I let him do it either.
        """

        broken """
        Listen to me, Mr Manning. Listen.

        Whoever wrote you that letter wrote me one of my own. They want a death of us today, and they do not greatly care whose.

        Do not give it to them.
        """

        drunk """
        But she... my Margaret...
        """

        broken """
        I know. Believe me, I do.

        But the man who has earned your bullet is not in this wood.

        He is the one who put the pen in your hand.
        """

        """
        Something in him gives way, like a sail when the wind drops.

        The fight goes out of him, and what is left is only a tired and grieving old man, swaying in the bracken.

        I take the rifle gently from his hands, and he lets me.

        I do not leave his side for the rest of the morning.

        The doctor walks out of the wood at noon, alive, and never once the wiser for how near a thing it was.

        A man who was meant to die today is breathing, and a man who was meant to kill him is not a murderer. It is not much. But after this morning, I will take it.
        """

        jump broken_day2_evening

    else:

        """
        I cannot find the words to reach him, and he will not be reached.

        He drinks, and mutters, and watches the doctor, and my unease only sharpens as the morning wears on.

        Something is going to happen in this wood. I can feel it coming, and I cannot for the life of me see how to head it off.
        """

        # TODO: If Broken never draws out the Drunk's letter, the western-grove
        # accident should still occur (the Drunk shoots the Doctor). Not written yet.

        jump work_in_progress


# --------------------------------------------
#   Drunk dialogue while shadowing the western-grove party
# --------------------------------------------
label broken_drunk_hunt_burden:

    broken """
    You have the look of a man with something heavy on his mind, Mr Manning.
    """

    drunk """
    Heavy. Ha.

    You have no notion of it, sir. No notion at all.
    """

    """
    He takes another pull from the flask, and his gaze drifts, as it always does, to the doctor's back.
    """

    drunk """
    Some debts cannot be paid in money. That is all.

    Some debts a man carries to his grave. Or sees carried to another's.
    """

    """
    He will say no more than that. Not yet.

    But the way he looks at Baldwin tells me a great deal.
    """

    return


label broken_drunk_hunt_letter:

    broken """
    Tell me something, Mr Manning, and forgive the strangeness of it.

    Did you find anything in your room last night that ought not to have been there?

    A letter, perhaps. Left where you could not fail to see it.
    """

    """
    The flask stops halfway to his mouth.

    For a moment the drink seems to go clean out of him, and he stares at me as though I had reached into his skull.
    """

    drunk """
    How... how could you possibly know that?
    """

    broken """
    Because I found one of my own.
    """

    """
    He searches my face, and whatever he finds there undoes him.

    The words come out in a rush, as though he has been holding them since the small hours.
    """

    drunk """
    They told me what he did. The doctor.

    He treated my Margaret, years ago. Held back the medicine that might have saved her, the very stuff he wanted for himself.

    He is the reason she is in the ground.

    And he walks about this house as though he had never harmed a soul in his life.
    """

    """
    His letter and mine, cut from the very same cloth.

    A grievance dug up, and sharpened, and pressed into the hand of a broken man, with a target set conveniently near.

    The same author wrote us both.
    """

    $ broken_details.threads.unlock('drunk_letter')

    return
