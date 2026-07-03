# --------------------------------------------
#   Broken
#
#   Sunday - Afternoon
#
#   11:30 -> 16:00
#
#   Music: mysterious, danger, sad
#
#   Position
#       - Forest road : Broken and Captain Sinha (pair), or all six (together)
#       - Dead        : Lad (Ted Harring)
#
#   Branches on the left_together thread (set in broken_day3_morning):
#       - not left_together -> the two-man walk. The butler is waiting on the
#         road: the Captain is shot, then Broken -> broken_ending_ambushed
#         (intuition: do not separate, take everyone)
#       - left_together     -> the whole party walks out. Six together are too
#         many witnesses: they pass the sawn tree and reach the police station
#         by late afternoon -> broken_ending_walked_out (final ending)
#
#   The sawn-tree observation is shared between both variants
#   (broken_day3_afternoon_sawn_tree).
# --------------------------------------------
label broken_day3_afternoon:

    $ broken_details.add_checkpoint("broken_day3_afternoon")

    call change_time(11, 30, 'Afternoon', 'Sunday', chapter='sunday_afternoon')

    call black_screen_transition("Thomas Moody", chapters_names[current_chapter])

    if broken_details.threads.is_unlocked('left_together'):

        jump broken_day3_afternoon_together

    jump broken_day3_afternoon_pair


# --------------------------------------------
#   THE TWO-MAN WALK (not left_together)
# --------------------------------------------
label broken_day3_afternoon_pair:

    $ change_room('manor_exterior')

    $ play_music('mysterious', 2)

    """
    The manor watches us go with all its windows, and gives away nothing.

    The Captain sets a soldier's pace down the drive, and I fall in beside him.

    It is a relief, at first, simply to be moving. To be doing the thing instead of arguing for it.
    """

    $ change_room('forest_road', dissolve)

    """
    Past the gate, the road runs into the trees and the trees close over it.

    We walk without talking. The Captain watches the left side of the road, and I find myself watching the right, and neither of us has proposed the arrangement aloud.

    The wood is quiet.

    Not peaceful. Quiet the way the house was quiet this morning.
    """

    call change_time(12, 30)

    call broken_day3_afternoon_sawn_tree

    """
    The Captain runs his hand along the cut and looks at me, and neither of us says the obvious thing.

    We climb over the trunk and walk on.

    Perhaps a mile further, the road bends between two banks of bracken, and the Captain slows.
    """

    captain """
    Mr Moody.

    From here to the bend, there is no cover at all. If I were laying a...
    """

    $ play_music('danger', 2)

    play sound gun

    pause 0.5

    """
    He does not finish.

    The shot takes him mid-word, and he goes down into the road like a coat slipping from a hook.

    I do not think. I am running before the sound has finished rolling off the hills, for the trees, for anywhere that is not this open lane.

    The bracken drags at my legs. The second shot sounds almost leisurely.
    """

    play sound body_fall

    """
    The road comes up to meet me.

    I lie with my cheek against the wet stone, and my last thought is not of the man behind the rifle at all.

    It is of four people, sitting in a tea room, waiting for help that is now lying in the road.

    I should never have split us apart.
    """

    jump broken_ending_ambushed


# --------------------------------------------
#   ALL TOGETHER (left_together)
# --------------------------------------------
label broken_day3_afternoon_together:

    $ change_room('manor_exterior')

    $ play_music('mysterious', 2)

    """
    We go down the drive in a slow column, six abreast of nobody.

    The Captain leads. Mr Manning walks in the middle with Miss Marsh keeping his pace, the doctor and Miss Baxter behind them, and I bring up the rear, where I can count heads.

    I count them often.
    """

    $ change_room('forest_road', dissolve)

    """
    The wood takes us in, and the manor drops away behind the trees, and nobody looks back but me.

    We are slow. Painfully slow.

    Manning's breath saws at every rise, and twice the nurse calls a halt and doses him from a flask of something she mixed in the cold kitchen.

    But slow together, I keep telling myself, beats quick apart.
    """

    call change_time(13, 00)

    call broken_day3_afternoon_sawn_tree

    """
    The Captain runs his hand along the cut, and straightens, and looks not at the tree but at the woods around us.

    Nobody needs it explained.

    Miss Marsh simply gathers Mr Manning's arm, and we help one another over the trunk, all six of us, hands to elbows, one by one.

    On the far side of it, the doctor is trembling. But he walks faster.
    """

    call change_time(14, 30)

    """
    Somewhere in the third hour, in the deep of the wood, the feeling comes over me that we are observed.

    No sound. No shape among the trunks. Only the itch between the shoulder blades that a man learns to trust.

    I drop back a pace and watch the treeline, and it gives me nothing.

    But nothing comes out of it either.

    Whoever they are, they have shown me twice this weekend that they like their work done privately. One man in a bed. One man in a wood.

    Six people on an open road, arm in arm, are the least private thing in Scotland.

    I keep my eyes on the trees, and I keep us moving, and the itch follows us for a mile and then, like a cur that has run out of hedge, gives up.
    """

    call change_time(15, 30)

    $ play_music('sad', 3)

    """
    The trees thin, and give way to stone walls and pasture, and then to the first grey cottages of the village.

    Smoke from real chimneys. Washing on a line. A dog with strong opinions about strangers.

    Mr Manning stops in the middle of the lane and laughs, once, at nothing at all, and Miss Marsh does not tell him to save his breath.
    """

    $ change_room('police_station', dissolve)

    """
    The police station is a squat stone box with a blue lamp over the door, and I have never in my life been so glad of an ugly building.

    A sergeant looks up from his ledger as the six of us crowd in out of the afternoon. Muddy, spent, and every one of us alive.

    Where to even begin.

    A dead man in an upstairs bedroom. A vanished household. Two poisoned-pen letters, a bottle of rat poison, and a tree that was sawn, not fallen.

    I take off the mask, and lay the army order on his counter, and begin at the beginning.
    """

    jump broken_ending_walked_out


# --------------------------------------------
#   THE SAWN TREE (shared by both variants)
# --------------------------------------------
label broken_day3_afternoon_sawn_tree:

    """
    Two miles out, we come upon the famous tree.

    A full-grown oak, right across the road, its crown in the ditch and its roots... its roots still in the ground.

    The trunk's end is not torn. It is flat, and pale, and ridged with the even strokes of a two-man saw.

    No storm did this.

    Somebody cut this road the way you would cut a telephone line.
    """

    return
