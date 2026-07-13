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

    $ change_room('forest_grove')

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

    """
    Lunch is over and the footman advises us to go back to hunting.

    None of us seems particularly enthusiastic about it, but we go on anyway.
    """

    if not broken_details.threads.is_unlocked('drunk_letter'):

        # If you don't make the drunk confess about the letter, you get killed

        pause 1.0

        $ play_music('danger', 2)

        """
        This afternoon is no more successful than the morning.

        We walk for a while without encountering anything, until a small rabbit appears in front of us.
        """

        drunk """
        Oh, a rabbit!
        """

        """
        Samuel Manning raises his gun and tries to aim at the animal, but his aim is terribly off, and his rifle points towards Doctor Baldwin.
        """

        broken """
        Watch out!
        """

        """
        Instinctively, I jump towards the rifle to redirect the shot.
        """

        play sound gun

        pause 0.5

        jump broken_ending_shielded

    # Only way to survive, make the drunk confess about the letter

    """
    I do not leave Samuel Manning's side for the rest of the halt.

    I am afraid he will change his mind before the end of the hunt, but he does not.

    The doctor walks out of the wood that afternoon, alive, and without a clue about the fate he avoided.
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
    No more questions now.
    
    If I want to move things forward, I will have to be blunt and take a risk.
    """

    broken """
    Mr Manning, last night I found something in my room, left there for me to see.
    
    An old army order.

    It told me that Captain Sinha was responsible for the death of someone dear to me.
    """

    """
    The flask stops halfway to his mouth.

    For a moment the drink seems to go clean out of him, and he stares at me as though I had reached into his skull.
    """

    drunk """
    You as well.

    That is... strange...
    """

    """
    He hesitates for a second, then decides he can trust me.
    """

    drunk """
    Mine told me what he did.

    The doctor.

    He treated my Margaret, years ago. Held back the medicine that might have saved her, the very stuff he wanted for himself.

    He is the reason she is in the ground.

    He is the cause of my misery.

    But he was never condemned for it.

    I cannot let him get away so easily.

    He has to pay.
    """

    $ drunk_details.threads.unlock('wife')    

    broken """
    Listen to me, Mr Manning. Listen.

    The same person gave us those letters. They clearly meant to manipulate us.

    Do not let them.
    """

    drunk """
    But she... my Margaret...
    """

    broken """
    I know. Believe me, I do.

    I also lost someone close to me.

    But first, are we sure they are the right men?

    I have received an official order, but it could have been fabricated.

    And you, are you certain Daniel Baldwin is the same man who treated your wife years ago?
    """

    drunk """
    Yes, I think it's him.

    But it was a long time ago, my memory is not so good now.

    And doctors, they tend to all look the same.

    I can't say for sure now.
    """

    broken """
    That's right, we cannot be sure now.

    Please do not do anything hasty.

    Let us search for more information first.

    You do not want to do something you might regret later.
    """

    """
    He looks intently at me, and I can see a part of him is relieved not to have to go through with his plan.
    """

    drunk """
    Fine, I'll let him live, for now.

    But you need to prove that he is not the same doctor, otherwise...
    """

    broken """
    Understood. I'll get to the bottom of it, I assure you.
    """

    """
    He grumbles something of an agreement, and returns to his drinking.

    The conversation is over and it might have saved a man's life.
    """

    $ broken_details.threads.unlock('drunk_letter')

    return
