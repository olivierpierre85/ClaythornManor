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
#       - not left_together -> the two-man walk. They find Lady Claythorn and
#         her staff shot dead in her motorcar, hidden off the road, and turn
#         back. The manor is alight and the four left behind are dead in the
#         billiard room. The roof comes down on Broken
#         -> broken_ending_massacre (intuition: do not separate, take everyone)
#       - left_together     -> the whole party walks out. Six together are too
#         many witnesses: they pass the sawn tree and reach the police station
#         by late afternoon -> broken_ending_walked_out (final ending)
#
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
    We exit the manor without looking back.

    The Captain sets a soldier's pace down the drive, and I fall in beside him.

    Simply to move away from this place gives me an enormous sense of relief.
    """

    call change_time(14, 30)

    $ change_room('forest_road', dissolve)

    """
    Past the gate, the road runs into the trees and the trees close over it.

    We walk without talking.

    The Captain watches the left side of the road, and I find myself watching the right.

    Neither of us has proposed the arrangement aloud, but our military training has settled it for us.
    """

    # New more dramatic version.

    """
    For a while, we do not notice anything out of the ordinary.

    Then, on the ground, I notice wheel tracks turning towards a clearing.

    I show them to Captain Sinha.
    """

    captain """
    Well spotted, Mr Moody.

    I would not have seen those tracks on my own.

    Someone drove a car inside those woods.

    And they cannot have driven far in it.
    """

    broken """
    You think it is Lady Claythorn's motorcar?
    """

    captain """
    Probably.

    The tracks are fresh, and I do not believe much traffic comes along this road.
    """

    broken """
    Then we should check.
    """

    captain """
    I suppose we should, yes.
    """

    broken """
    They must be close, let us go.
    """

    captain """
    All right, but let me take my pistol out first.
    """

    """
    He tries to act calm, but I can see his hands shaking.

    Only now do I realise how risky this could be.
    """

    $ change_room('forest_with_car')

    """
    We do not have to walk long until we discover Lady Claythorn's car, stopped in its tracks.

    Someone has put a few branches on it to hide it from the road.
    """

    captain """
    Lady Claythorn! Are you there?
    """

    """
    No answer.
    """

    broken """
    Let us look inside.
    """

    captain """
    Humph, fine.
    """

    $ play_music('danger', 2)

    """
    The Captain puts his hand on the door and opens it.
    """

    play sound door_open

    """
    Then, for the first time, he loses his composure.
    """

    captain scared """
    Oh my God...

    Oh my God, they are dead.

    All of them.
    """

    broken """
    What?!
    """

    """
    I look inside for myself, and there they are.

    Lady Claythorn in the front seat, and her staff.

    The maid and the footman in the back.

    All three sit lifeless.

    I can see the bullet wounds in them.

    I quickly close the door.
    """

    play sound door_open

    broken scared """
    Oh no, what happened?
    """

    captain """
    I do not know.

    Someone shot them and left them here.

    But who? And why?
    """

    broken """
    Well, there was another member of the staff.

    He was probably the one driving.
    """

    captain """
    Right, right.

    The butler, where is he now?
    """

    """
    Realising what that means, he spins round.

    His gun pointing towards the woods.
    """

    captain """
    Is anyone here?!

    Show yourself!
    """

    broken """
    I think it is a bit late for that.

    He probably is long gone now.
    """

    captain """
    Right, of course.

    But gone where?
    """

    broken """
    Maybe he reached the town, or maybe...

    Maybe...
    """

    """
    A sudden realisation dawns on me.
    """

    captain """
    Yes, what?
    """

    broken """
    Maybe he went back to the manor.

    To the others.
    """

    captain """
    Oh my god.

    You could be right.

    What should we do?
    """

    """
    I know the safest thing would be to leave and reach the police.

    But we are still probably closer to the manor than the town.
    """

    broken """
    We have to go back, and quick.
    """

    """
    He hesitates for a second, not even trying to hide his fear.
    """

    captain """
    You go.

    Try to warn the others.

    And I will go towards the town.

    With the police car I might even be back before you.
    """

    """
    I highly doubt that, but I have no time to argue.
    """

    broken """
    Fine, but let us not waste any time.
    """

    $ change_room('forest_road')

    """
    We rush back to the road.
    """

    captain """
    I will go this way.

    Do not worry, I will be back to the manor as fast as possible.

    Good luck, Mr Moody.
    """

    broken """
    Goodbye, Captain.
    """

    """
    I have no opportunity to say more, as he is already on his way.

    He looks more as though he is fleeing than bravely going to fetch help.

    So I start running in the opposite direction.

    I go fast at first, but as my strength diminishes, I settle into a light jog.
    """

    $ play_music('scary', 2)

    """
    As I approach the manor, I catch a faint smell of smoke and begin to worry.
    """

    $ change_room('manor_on_fire', dissolve)

    play sound fire loop

    """
    As I feared, Claythorn Manor stands at the end of the gravel with fire in half its windows.
    """

    pause 1.0

    """
    I am frozen for a second.

    But I realise the others might still be inside.

    I feel like I do not have a choice and rush towards the entrance.
    """

    play sound door_open

    $ change_room('entrance_hall_fire', dissolve)

    """
    The hall takes the breath out of me at the door.

    The heat stands in it like a wall, and the smoke lies along the ceiling in a slow black river.

    My mask fills with it at once, so I throw it to the ground.

    I manage to shout at the top of my lungs.
    """

    broken """
    Is anyone here?

    It is Thomas Moody!
    """

    """
    No answer.

    So I make for the billiard room.

    Luckily, the door is intact.

    The flames have not reached it yet.
    """

    play sound door_open

    $ change_room('billiard_room_fire', dissolve)

    $ play_music('sad', 3)

    """
    And there they are.

    Doctor Baldwin lies nearest the door, face down, one arm still reaching for the handle.

    Samuel Manning sits propped against the little bar, almost upright, his flask fallen from his hand.

    Miss Marsh is on her side by the billiard table.

    And Miss Baxter is beyond her, blood all over her face.
    """

    broken scared """
    No.

    No, no, no.
    """

    """
    I go from one to the next on my knees, because I cannot make myself stop.

    Baldwin, then Manning, then Miss Marsh.

    Nothing.

    I try to make sense of what I see.

    The fire was not set to kill them.
    """

    play sound moving_furniture

    """
    Above me, the house makes a sound.

    I look up.

    The ceiling is bowing in the middle, slowly, almost gently.

    I know I should move, but I am paralysed by fear.
    """

    play sound thunder_full

    """
    Then the whole of Claythorn Manor comes down upon me.
    """

    stop sound fadeout 2.0

    jump broken_ending_massacre
    

# --------------------------------------------
#   ALL TOGETHER (left_together)
# --------------------------------------------
label broken_day3_afternoon_together:

    $ change_room('manor_exterior')

    $ play_music('mysterious', 2)

    """
    We go down the drive in a slow column.

    The Captain leads. Mr Manning walks in the middle with Miss Marsh keeping his pace.

    The doctor and Miss Baxter follow behind them, and I bring up the rear, where I can watch them all.

    Which I intend to do until we are safe.
    """

    $ change_room('forest_road', dissolve)

    """
    The wood takes us in, and the manor drops away behind the trees.

    Nobody looks back but me.

    We are slow. Painfully slow.

    Manning's breath saws at every rise, and twice the nurse calls a halt.
    """

    call change_time(14, 30)

    """
    Somewhere in the third hour, in the deep of the wood, the feeling comes over me that we are observed.

    I drop back a pace and watch the treeline, and it gives me nothing.

    But nothing comes out of it either.

    If there is anybody out there, they do not dare approach the whole party at once.

    I keep my eyes on the trees, and I keep us moving.
    """

    call change_time(15, 30)

    $ play_music('sad', 3)

    """
    The trees thin, and give way to stone walls and pasture, and then to the first grey cottages of the town.

    Smoke from chimneys. Washing on a line.

    Until finally, we arrive at the police station.
    """

    $ change_room('police_station', dissolve)

    """
    A sergeant looks up from his ledger as the six of us enter the small building together.

    Muddy and spent, we must make a rather strange sight.

    I approach him, finally taking off my mask.

    Then I tell our story from the beginning.
    """

    jump broken_ending_walked_out

