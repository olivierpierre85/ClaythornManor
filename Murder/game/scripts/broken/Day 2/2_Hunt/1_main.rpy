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
#   Notes :
#       - Broken (the false Thomas Moody) joins the Captain's party in the
#         north field. The hunt hardens his conviction that Sinha is a fraud.
#       - Two of the Captain's actions stoke his anger; each is tempered by a
#         thread the player may carry into the chapter:
#           - host_lies      -> the Host is a fraud too, so the Captain's lie
#                               proves nothing of Tom (tempers the poor shooting).
#           - talked_to_maid -> the "surprise" warns of a setup (tempers the
#                               luncheon war-story).
#       - Choice gate: WITH talked_to_maid, Broken may SPARE or KILL the
#         Captain. WITHOUT it, rage wins and the kill is the only path.
#       - The north-field hunt (pairing, the shoot, the luncheon) and the kill
#         (isolation + confrontation + shot) are both shared with the Captain's
#         storyline and branch on current_character.text_id:
#           - common_day2_hunt_pairing
#           - common_day2_hunt_north_field  (holds the host_lies anger beat)
#           - common_day2_hunt_captain_confrontation
#       - In the far party, the Drunk shoots the Doctor, heard at a distance.
#       - TODO (spare branch): Broken should reach the far party to prevent the
#         Doctor's death (docs/next_tasks.md, Saturday - Hunt). Not written yet.
#       - Both branches stop at the hunt's end (work_in_progress).
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

    call common_day2_hunt_north_field

    host """
    Captain, you simply must tell us something of your soldiering.

    We have a real campaigner among us, and here I am letting him eat in silence.
    """

    captain """
    There is little worth the telling, my lady.

    But if it would amuse you, I might give you the relief of Tientsin. The heat of it, and the walls.
    """

    """
    And he is away, modest and precise, with the polished ease of a man who has told it across a hundred dinner tables.

    Lady Claythorn leans in, delighted.

    I sit very still and let it wash over me.

    This man held the safest billet in France, and came home to play the hero over the sandwiches, while Tom came home behind a mask and died by inches for the want of the very courage this fraud counterfeits so prettily.

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

    if broken_details.threads.is_unlocked('talked_to_maid'):

        """
        A surprise, the maid said. Prepared for the guests.

        I am beginning to understand what a poor part I have played in it.
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

    I compose my face behind the mask, take up my rifle, and start back the way we came.

    A dreadful accident, I shall tell them. The Captain wandered ahead, and the cover was thick, and I never saw him.

    God help me, I am becoming an easy liar.
    """

    # TODO: Saturday evening (saturday_evening). With the Captain dead, the Host
    # panics and leaves before dinner; the manor turns deadly. See docs/next_tasks.md.
    jump work_in_progress


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

    Lady Claythorn is on her feet. The Captain reaches for his rifle.

    My blood runs cold.

    The doctor. They have left him alone with that poor drunken wreck, and I have sat here playing at conscience while the next act began without me.
    """

    broken """
    Stay with her ladyship, Captain.

    I shall go.
    """

    """
    I am already moving, crashing through the bracken toward the sound, praying I am not as late as I fear.
    """

    # TODO: spare branch -> Broken reaches the far party and tries to prevent the
    # Doctor's death (docs/next_tasks.md, Saturday - Hunt). Not written yet.
    jump work_in_progress
