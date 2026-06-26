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
#       - Broken (the false Thomas Moody) attaches himself to the Captain's
#         party in order to get him alone, then confronts and kills him over
#         the forged transfer order.
#       - The confrontation is shared with the Captain's storyline through
#         common_day2_hunt_captain_confrontation (narration branches on text_id).
#       - In the far party, the Drunk shoots the Doctor, heard at a distance.
#       - TODO (branch): if Broken has found the Drunk's warning, he should
#         doubt the setup, spare the Captain, and join the far party to
#         prevent the Doctor's death. That finding is not written yet, so for
#         now this path is linear. See docs/next_tasks.md (Saturday - Hunt).
#       - Stops at the hunt's end (work_in_progress).
# --------------------------------------------
label broken_day2_hunt:

    $ broken_details.add_checkpoint("broken_day2_hunt")

    call change_time(11, 0, 'The Hunt', 'Saturday', chapter='saturday_afternoon')

    call black_screen_transition("Thomas Moody", chapters_names[current_chapter])

    $ change_room('bedroom_broken')

    $ play_music('upbeat', 1)

    """
    I return to my room to change into the tweeds the household has laid out for me.

    My hands are steady as I dress. Steadier than they have any right to be.

    The letter is folded in my breast pocket, where I can feel the small weight of it against my chest.

    All night I turned it over, and all night the answer came back the same.

    Captain Sinha sent Tom up to the line, and Tom did not come home.

    Whatever else is false in this house, that much I am certain of.

    And a hunt is a careless sort of business. Accidents happen. Everyone says so.
    """

    $ change_room('gun_room')

    """
    The butler is in the gun room, attending the rifles with his unhurried care.

    He hands me a piece, and the weight of it settles into my hands like an old habit.

    I check the action, sight along the barrel, and find it true.

    I have handled guns since I was a boy, in yards and back rooms no gentleman would think to look.

    Tom taught me the rest, on a fortnight's leave, laughing at how quick I took to it.

    I shall not embarrass myself today.
    """

    $ change_room('manor_garden')

    """
    The others are already gathering on the lawn.

    Doctor Baldwin stands a little apart, grey and unwell, checking his rifle as though it were a patient.

    Samuel Manning is a sorry sight, a flask in one hand and a gun in the other, swaying where he stands.

    Lady Claythorn is the last to come out, turned out head to foot in tweed she plainly does not know how to wear.

    And the Captain. Upright. Correct. A decorated officer at his ease.

    The very picture of the man whose name is at the foot of my letter.
    """

    if broken_details.threads.is_unlocked('talked_to_maid'):

        """
        The maid's words come back to me. A surprise, she said, prepared for the guests.

        A letter slipped beneath my door, and a hunt laid on the very next morning.

        It is too neat by half. I know it, somewhere beneath the anger.

        But knowing a thing and heeding it are not at all the same, and the anger is by far the louder of the two.
        """

    call common_day2_hunt_butler_groups

    captain """
    If I may, my lady. I should consider it a privilege to accompany you.
    """

    host """
    How gallant of you, Captain. The privilege, I assure you, is mine.
    """

    drunk """
    Doctor, I would be honoured to partner with you.

    You don't mind, do you?
    """

    """
    Doctor Baldwin's mouth opens and closes again. He plainly minds a great deal, yet he cannot find the words to refuse.
    """

    doctor """
    Well... no, of course not.
    """

    """
    That is the western grove settled, then. The doctor, the drunkard, and a footman to mind the pair of them.

    Which leaves the north field to our hostess, the Captain, the butler, and whoever should round them out.

    I do not mean to leave that to chance.
    """

    broken """
    Doctor Baldwin's party is already three guns strong.

    I shall round out your own, if my lady will have me.
    """

    host """
    Why, Mr Moody, of course.

    The more the merrier.
    """

    captain """
    A pleasure, Mr Moody.
    """

    broken """
    The pleasure is entirely mine, Captain.
    """

    """
    He returns my courtesy without a flicker.

    He has no notion of what I carry in my pocket, nor what I mean to make of the morning.

    Good.
    """

    butler """
    Very good. Doctor Baldwin and Mr Manning to the western grove.

    The footman will go along with them.

    My lady, Captain Sinha and Mr Moody to the north field, and I shall attend.
    """

    call change_time(11, 45)

    $ change_room('forest')

    """
    We walk some distance before the first quarry breaks cover. A pheasant, not ten yards off our line.

    I have it before the Captain's rifle is even at his shoulder.
    """

    play sound gun

    pause 1.0

    """
    The bird drops cleanly.
    """

    host """
    Bravo, Mr Moody. A splendid shot.
    """

    broken """
    You flatter me, my lady.

    One does one's best.
    """

    """
    The Captain's turn comes a few minutes on, at a rabbit sat in the grass.
    """

    play sound gun

    pause 1.0

    """
    He misses by a yard, and not for want of a steady morning.

    A decorated soldier, and he cannot put a ball into a rabbit sitting still in the open.

    I had wondered at it. Now I am sure.

    Whatever he was in the war, it was not what he tells the dinner table.
    """

    broken """
    Hard luck, Captain. Hard luck indeed.
    """

    captain """
    I misjudged the lead.
    """

    broken """
    Quite. The lead.
    """

    """
    I let a little of the mockery show. I cannot help myself.

    Lady Claythorn fares no better. Twice the barrel dips toward the earth, and once she shifts her grip as though she has forgotten where her hands belong.

    A gentlewoman who arranged a shooting weekend on her own grounds, and she handles a gun like a parasol.

    There is not an honest article in this whole party.

    Myself least of all.
    """

    $ host_details.description_hidden.unlock('hunt')

    call change_time(12, 30)

    """
    By the time the butler calls us in for luncheon, only I have any game to show for the morning.
    """

    host """
    Three birds and a pair of rabbits, Mr Moody. You are most impressive.

    I confess I had no notion we should be so splendidly provided for.
    """

    broken """
    Your ladyship is too generous.

    I was simply very lucky today, that is all.

    Otherwise, I am certain a decorated veteran like Captain Sinha would have put me quite to shame.
    """

    """
    The Captain says nothing to that. He only smiles, thin and correct.

    We settle in a clearing among the birches. The butler lays a cloth and pours the tea with his customary care.

    I keep up an easy flow of talk at Lady Claythorn's side, and watch the Captain over the rim of my cup, and wait for the butler to find some reason to leave us.
    """

    call change_time(13, 0)

    """
    In time, he does. A word about looking in upon the other party, and he is gone into the trees.

    Three of us left in the clearing, and the Captain his own master no longer.

    Now, then.
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
    Then, from the direction of the western grove, another shot. And after it, faint and thin between the trees, a cry.

    The doctor, or the drunkard, or both. It scarcely matters which.

    Whoever drew us under this roof wanted blood this morning, and every one of us has proved so very willing to spill it.

    Two men dead before the luncheon is cleared away, and the day not yet half gone.
    """

    """
    I have no time for the horror of it. The butler will have heard the shots, and our hostess is a hundred yards off and waiting.

    I compose my face behind the mask, take up my rifle, and start back toward the clearing.

    A dreadful accident, I shall tell them. The Captain wandered ahead, and the cover was thick, and I never saw him.

    God help me, I am becoming an easy liar.
    """

    # TODO: Saturday evening (saturday_evening). With the Captain dead, the Host
    # panics and leaves before dinner; the manor turns deadly. See docs/next_tasks.md.
    jump work_in_progress
