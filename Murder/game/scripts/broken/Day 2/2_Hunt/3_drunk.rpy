# --------------------------------------------
#   Broken - Saturday Hunt - With the Drunk (western grove)
#
#   Reached from broken_day2_hunt (1_main.rpy) only when talked_to_maid is set
#   and the player chooses to join the Doctor and Mr Manning.
#
#   At the halt, Broken must choose whom to spend the crucial minutes with:
#   Doctor Baldwin or Mr Manning (broken_day2_hunt_menu_company). Only by sitting
#   with Manning and working through the interrogation chain in the Drunk generic
#   menu (drunk_generic_menu_broken, broken_config_menu.rpy: the background
#   question reveals the invitation question, whose answer slips the word
#   "letter" and reveals the letter admission — the full chain costs the whole
#   60s budget) does Broken unlock the drunk_letter thread. Broken confides
#   that he found a letter in his own room, which unsettles Manning into
#   admitting he was sent one too (the Doctor killed his wife). That recognition
#   lets Broken talk him down and save both men, continuing into
#   broken_day2_evening (Day 2/3_Evening/1_main.rpy).
#
#   Give the doctor your attention, keep to yourself, or sit with Manning but
#   fail to draw out the letter, and Manning fires on Baldwin. Broken throws
#   himself into the shot and dies: broken_ending_shielded.
# --------------------------------------------
label broken_day2_hunt_drunk:

    broken """
    Well, if it is all the same to everybody, I will go with Doctor Baldwin and Mr Manning.
    """

    """
    The butler gives me an odd look, as if I ought to have shown a preference for our host's party.

    By way of apology, I whisper to him.
    """

    broken """
    I hope you'll forgive me, but I prefer not to leave Doctor Baldwin alone with Samuel Manning.
    """

    """
    He nods in agreement and gives me a slight smile.
    """

    call change_time(11, 45)

    $ change_room('forest')

    """
    We strike off to the west, the doctor a few paces ahead, Mr Manning weaving along at my side.

    Baldwin is grey and sweating, sunk in some private misery of his own, and pays neither of us any mind.

    Samuel Manning's hands shake so badly he can scarcely hold his weapon.

    And I am so busy observing the pair of them that I barely notice the rabbits and pheasants that come our way.

    No wonder none of us has shot anything this morning.

    We stop for lunch empty-handed.

    Doctor Baldwin settles next to the footman, and Samuel Manning sits a little apart.

    None of them seems eager for conversation.
    """

    $ time_left = 60
    call run_menu(
        TimedMenu("broken_day2_hunt_menu_company", [
            TimedMenuChoice("Talk to Doctor Baldwin", 'broken_day2_hunt_drunk_doctor', early_exit=True),
            TimedMenuChoice("Sit down beside Samuel Manning", 'broken_day2_hunt_drunk_manning', early_exit=True),
            TimedMenuChoice("Keep to yourself", 'generic_cancel', early_exit=True),
        ], image_left = "doctor", image_right = "drunk"))

    if not broken_details.threads.is_unlocked('drunk_letter'):

        # If you don't make the drunk confess about the letter, you get killed

        $ play_music('danger', 2)

        """
        It comes without a word of warning.

        Manning is on his feet, the rifle up and level, and the muzzle finds the doctor's back as though it had been waiting there all along.

        The hands that trembled all morning are suddenly, terribly steady.

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

        Manning has let the rifle fall and stands staring at his own hands, as though they are some other man's.

        A letter sent me into this wood hating Captain Sinha. Too late, I wonder what was sent to him.

        Somebody loaded that poor devil like a gun. I would stake my life on it.

        I suppose I just have.

        But the doctor is on his feet, and I am the one in the bracken, and for the length of one failing breath that seems a fair enough bargain.
        """

        jump broken_ending_shielded

    # Only way to survive, make the drunk confess about the letter

    """
    I do not leave his side for the rest of the halt.

    The doctor walks out of the wood that afternoon, alive, and never once the wiser for how near a thing it was.

    A man who was meant to die today is breathing, and a man who was meant to kill him is not a murderer. It is not much. But after this morning, I will take it.
    """

    jump broken_day2_evening

    return

# --------------------------------------------
#   Broken gives the doctor his attention and leaves Manning to stew.
#   Whatever Baldwin lets slip, it comes too late to head off the shot.
# --------------------------------------------
label broken_day2_hunt_drunk_doctor:

    """
    Samuel Manning makes me uneasy, so I approach Doctor Baldwin.

    I interrupt what looks like a hushed exchange between him and the footman.

    They break off, and act as if nothing has passed between them.
    """

    doctor """
    Ah, Mr Moody.

    Excellent day for a hunt, isn't it?

    But tell me, what is on your mind?
    """

    call doctor_generic

    return

# --------------------------------------------
#   Broken sits with Manning. Draw out the letter (drunk_letter) and he is
#   talked down; fail to, and the grove takes Broken in the doctor's place.
# --------------------------------------------
label broken_day2_hunt_drunk_manning:

    broken """
    Mr Manning, do you mind if I sit here?
    """

    drunk """
    Oh, Mr Moody, no, not at all, of course.
    """

    """
    I need to know if I can trust him, so I shouldn't waste time asking trivial questions.

    If I want to know what is happening here, I need to be careful.
    """

    call drunk_generic

    return



label broken_drunk_hunt_letter:

    """
    There is one card left to me, and no clever way to play it.

    So I lay it face up on the table.
    """

    broken """
    Mr Manning, I am going to tell you something I have told nobody else in this house.

    Last night I found something in my room. A letter.

    No signature. Left where I could not fail to find it.

    It told me of a wrong done to me by a man under this roof, and it was written to make me hate him.
    """

    """
    The flask stops halfway to his mouth.

    For a moment the drink seems to go clean out of him, and he stares at me as though I had reached into his skull.
    """

    drunk """
    A letter.

    You as well.

    That is... strange...
    """

    """
    He searches my face, and whatever he finds there undoes him.

    The words come out in a rush, as though he has been holding them since the small hours.
    """

    drunk """
    Mine told me what he did. The doctor.

    He treated my Margaret, years ago. Held back the medicine that might have saved her, the very stuff he wanted for himself.

    He is the reason she is in the ground.

    But he was never condemned for it.

    I cannot let him get away so easily. He has to pay.
    """

    $ broken_details.threads.unlock('drunk_letter')
    
    """
    So there it is.

    The same hand that left an old army order upon my pillow left a letter for him, and aimed him at the doctor as it aimed me at the Captain.

    We are not guests at all. We are loaded guns, laid out on a table for someone else to fire.

    Well. I will not go off on command, and I will be damned if I let him do it either.
    """

    broken """
    Listen to me, Mr Manning. Listen.

    The same hand wrote your letter and mine. They want a death of us today, and they do not greatly care whose.

    Do not give it to them.
    """

    drunk """
    But she... my Margaret...
    """

    broken """
    I know. Believe me, I do.

    But the man who has earned your bullet is not in this wood.

    He is the one who held the pen.
    """

    """
    Something in him gives way, like a sail when the wind drops.

    The fight goes out of him, and what is left is only a tired and grieving old man, swaying in the bracken.

    I take the rifle gently from his hands, and he lets me.
    """



    return
