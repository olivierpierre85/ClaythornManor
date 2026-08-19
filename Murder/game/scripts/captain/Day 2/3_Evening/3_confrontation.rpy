# --------------------------------------------
#   Confrontation path - Captain deflects the
#   Manning task onto the butler, then presses
#   the hostess before the remaining witnesses
#
#   The confrontation itself, the unmasking and
#   the gunfight are shared with the Host's own
#   timeline, in _common/Day 2/3_Evening/
#   3_captain_host_confrontation.rpy
#
# Doctor, Broken => Dead
# Drunk with butler
# Lad in his room
# that leaves : Captain, psychic, nurse, host
# --------------------------------------------
label captain_day2_evening_confront_host:

    call common_day2_evening_captain_confronts_host

    call common_day2_evening_host_unmasked

    $ time_left = 1
    call run_menu(
        TimedMenu("captain_day2_evening_menu_butler_offer", [
            TimedMenuChoice("Accepts being confined", 'captain_day2_evening_butler_offer_confine', early_exit=True),
            TimedMenuChoice("Lunge at him and grab the gun", 'captain_day2_evening_butler_offer_attack', early_exit=True),
        ])
    )


label captain_day2_evening_butler_offer_confine:

    """
    I have worn the King's uniform the better part of twenty years, and never once stood in proper combat.

    Whatever instinct a soldier is meant to acquire from being shot at, I do no have it.

    I can already see myself bleeding into the carpet if I attempt anything.
    """

    captain """
    Very well.

    Lower the weapon, sir, if you please.

    We shall do as you ask.
    """

    butler """
    A wise decision, Captain.

    No further trouble. Only quiet, until morning.
    """

    """
    He gestures with the muzzle towards the door.

    Miss Marsh rises first. Miss Baxter follows in silence.

    Lady Claythorn doesn't seem to know what to do.

    She was part of this, yet, I don't think she wills us any harm.

    The butler sense this and turns to her.
    """

    butler """
    Go warn the others.

    I will lock those up, hopefully Ted Harring is still in his room, that will make things easier.
    """

    """
    She does not protest. She has not the strength left for it.

    Whatever she is in this affair, she will not contradict him.

    I bring up the rear behind the two ladies, and feel the weight of the revolver at my back the whole length of the corridor.

    Very quickly, I am in my room.
    """

    $ change_room("bedrooms_hallway")

    butler """
    Go in captain, no need to make this more complicated that it is.
    """

    """
    I have no choice but to go in.
    """

    $ change_room("bedroom_captain", dissolve)

    play sound door_locked

    pause 0.5

    """
    The bolt slides home from the corridor side.
    """

    butler """
    Have a good night captain.

    And no need to worry, the police will come for you tomorrow, I assure you.
    """

    """
    I don't have an answer to that.

    Will the police come? I have no idea.

    I cross to the window and try the latch. Painted shut, of course. Two storeys down besides.

    For a long while I sit upon the edge of the bed and listen to the house.

    Desperate, I finally fall asleep.
    """

    call wait_screen_transition()

    call change_time(23, 10)

    """
    I do not know what wakes me.

    A scrape, perhaps. A door drawn shut along the corridor.

    Then the smell — the dry, urgent sweetness of old wood beginning to burn.

    A thin grey ribbon of smoke is already feeling its way under the door.
    """

    # play sound door_force

    """
    I throw myself at the door and find what I knew I should find. The bolt holds.

    I shoulder it twice, three times.

    The frame holds.

    Below me, somewhere, glass goes with the sound of a dropped tray.
    """

    pause 1.0

    """
    The smoke comes faster than I had thought it could.

    I sink to my knees with my coat across my mouth, and find the air no kinder there.

    Through the floorboards, very faintly, the manor begins to give voice to itself.

    A great, considered creaking, as of a vessel preparing, at last, to part with its ribs.
    """

    $ host_details.description_hidden.unlock('not_guilty')

    jump captain_ending_burned


label captain_day2_evening_butler_offer_attack:

    """
    Miss Marsh is silent. Miss Baxter looks terrified.

    Whatever is to be done here, I must do alone.

    And I will not quietly follow a man to an unknown fate.

    Twenty years I have been an officer, but never once have I seen battle.

    A barracks officer, a parade officer.

    Other men around me went to the line.

    I never did.

    Here is my chance to see what mettle I am made of.

    I lunge for his wrist.
    """

    call common_day2_evening_butler_gunfight

    """
    And then, for one whole moment, I have him.

    His arm is bent back against the edge of the table and the revolver is pointing at the ceiling, and I am the stronger of us.

    Twenty years of drill are worth something after all.
    """

    """
    Then he does something small and practised with his elbow, and the moment is finished.

    The barrel comes down between us, quite unhurried, as though he had all evening for it.
    """

    play sound gun

    """
    The second shot is fired with the muzzle against my coat.

    A flat, ugly sound, very loud in the small room.

    Something very hot opens beneath my ribs, and the floor comes up to meet me with surprising patience.

    The man has done this before, and often.

    I had read it in him a moment ago, and chosen to go for him all the same.
    """

    butler """
    Forgive me, Captain.

    You left me no choice.
    """

    """
    He sounds, of all things, sincere.

    Somewhere to my left a woman is being told to lie still.

    The room narrows to a single point of grey.
    """

    $ host_details.description_hidden.unlock('not_guilty')

    jump captain_ending_shot_butler
