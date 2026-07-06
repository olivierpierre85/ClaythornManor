# --------------------------------------------
#   Broken - Saturday Hunt - With the Drunk (western grove)
#
#   Reached from broken_day2_hunt (1_main.rpy) only when talked_to_maid is set
#   and the player chooses to join the Doctor and Mr Manning.
#
#   At the halt, Broken must choose whom to spend the crucial minutes with:
#   Doctor Baldwin or Mr Manning (broken_day2_hunt_menu_company). Only by sitting
#   with Manning and putting the letter question in the Drunk generic menu
#   (drunk_generic_menu_broken, broken_config_menu.rpy) does Broken unlock the
#   drunk_letter thread and learn that Manning, like him, was sent a letter (the
#   Doctor killed his wife). That recognition lets Broken talk him down and save
#   both men, continuing into broken_day2_evening (Day 2/3_Evening/1_main.rpy).
#
#   Give the doctor your attention, keep to yourself, or sit with Manning but
#   fail to draw out the letter, and Manning fires on Baldwin. Broken throws
#   himself into the shot and dies: broken_ending_shielded.
# --------------------------------------------
label broken_day2_hunt_drunk:

    broken """
    Well, if it is the same for everybody, I will go with Doctor Baldwin and Mister Manning.
    """

    """
    The butler gives me a weird look, as if I should have shown preference in going with out host.
    
    As a way of apologizing, I whisper to her.
    """

    broken """
    I hope you'll forgive me, but I prefer not leave Doctor Baldwin alone with Samuel Manning.
    """

    """
    She nods in agreement and gives me slight smile.
    
    The Captain inclines his head, plainly relieved to see the back of me.
    """

    call change_time(11, 45)

    $ change_room('forest')

    """
    We strike off to the west, the doctor a few paces ahead, Mr Manning weaving along at my side.

    Baldwin is grey and sweating, sunk in some private misery of his own, and pays neither of us any mind.

    And Samuel Manning hands shake so badly he can scarcely hold its weapon.

    And I am so busy observing the both of them, I barely notice the rabbits and pheasants that came our way.

    No wonder none of us shot anything this morning.

    It's empty handed that we settle for lunch.

    Doctor Baldwin settle next to the footman, Samuel Manning is sitting a bit apart.

    None of them seem to want to engage in any kind of conversation.
    """

    $ time_left = 1
    call run_menu(
        TimedMenu("broken_day2_hunt_menu_company", [
            TimedMenuChoice("Draw Doctor Baldwin into talk", 'broken_day2_hunt_drunk_doctor', early_exit=True),
            TimedMenuChoice("Sit down beside Samuel Manning", 'broken_day2_hunt_drunk_manning', early_exit=True),
            TimedMenuChoice("Keep to yourself and watch them both", 'broken_day2_hunt_drunk_watch', early_exit=True),
        ], image_left = "doctor", image_right = "drunk"))


# --------------------------------------------
#   Broken gives the doctor his attention and leaves Manning to stew.
#   Whatever Baldwin lets slip, it comes too late to head off the shot.
# --------------------------------------------
label broken_day2_hunt_drunk_doctor:

    """
    Manning is the danger here, that much is plain.

    But it is Baldwin the danger is aimed at, and it is Baldwin who might yet tell me why.

    I fall in beside the doctor and try to draw him out.
    """

    call doctor_generic

    """
    Whatever I take from Baldwin, I take too slowly.

    All the while I am at his elbow, Manning is at our backs, half forgotten, the flask working and his eyes fixed on a mark he has already settled upon.

    I feel the moment turn before I see it.
    """

    jump broken_day2_hunt_drunk_grove_shot


# --------------------------------------------
#   Broken keeps his distance and trusts his eye. He reads the wood too late.
# --------------------------------------------
label broken_day2_hunt_drunk_watch:

    """
    No. I will keep my own counsel and my distance, and watch the pair of them.

    I have always trusted my eye more than my tongue, and I tell myself I will read the moment before it breaks.

    So I settle a little apart, where I can see them both, and I wait.

    It is a fine theory, right up until the instant it fails me.
    """

    jump broken_day2_hunt_drunk_grove_shot


# --------------------------------------------
#   Broken sits with Manning. Draw out the letter (drunk_letter) and he is
#   talked down; fail to, and the grove takes Broken in the doctor's place.
# --------------------------------------------
label broken_day2_hunt_drunk_manning:

    """
    Baldwin may keep his secrets a while longer.

    It is Manning who frightens me, and a frightened man is best kept talking.

    I settle myself beside him in the bracken and offer him a companionable word.
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

        jump broken_day2_hunt_drunk_grove_shot


# --------------------------------------------
#   The grove turns: Manning fires on the doctor and Broken takes the bullet
# --------------------------------------------
label broken_day2_hunt_drunk_grove_shot:

    $ play_music('danger', 2)

    """
    It comes without a word of warning.

    Manning is on his feet, the rifle up and level, and the muzzle finds the doctor's back as though it had been waiting there all along.

    Baldwin has time only to half turn, grey and uncomprehending.

    There is no thought in what I do.

    There is no time for it.

    I throw myself across the space between them.
    """

    play sound gun

    pause 0.5

    """
    The shot takes me instead.

    It is a strange thing, to feel so little at the moment it matters most.

    Only a great dull blow, and the wet earth rising to meet me, and the trees leaning in overhead.

    Baldwin is shouting something I cannot make out.

    Manning has let the rifle fall and stands staring at his own hands.

    I never learned who wrote his letter, nor who wrote mine.

    But the doctor is on his feet, and I am the one in the bracken, and for the length of one failing breath that seems a fair enough bargain.
    """

    jump broken_ending_shielded


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
