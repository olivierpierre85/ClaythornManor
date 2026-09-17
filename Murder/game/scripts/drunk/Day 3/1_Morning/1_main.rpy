# --------------------------------------------
#   Drunk
#
#   Sunday - Morning
#
#   08:00 -> 12:00
#
#   Music: scary for the door, mysterious after
#
#   Position
#       - Bedroom Drunk : drunk, playing dead
#       - House : lad, psychic, captain (searching)
#       - Dead  : broken, doctor
#       - Gone  : butler and the staff, since the night
#
#   Notes :
#       - Only reached through played_dead. The whole morning is one held
#         breath. The door opens, the Captain looks in, and does not come
#         close. The moment he pulls the door to, Manning is a free man in a
#         house that thinks him dead.
#       - He hears the search party pass and understands the staff have gone.
#         Then he waits out the morning, because a dead man cannot be seen
#         walking, and slips down only when the house has emptied of the
#         living too.
#
#   Unlocks : drunk 'faked_death'
# --------------------------------------------
label drunk_day3_morning:

    call change_time(8, 00, 'Morning', 'Sunday', hide_minutes = True, chapter = 'sunday_morning')

    $ drunk_details.add_checkpoint("drunk_day3_morning")

    call black_screen_transition("Samuel Manning", chapters_names[current_chapter])

    $ drunk_mode = False

    scene black_background

    $ play_music('scary', 3)

    """
    Dark, behind my own eyes, and the port gone cold and stiff on my neck, and my mouth dry as a lime pit.

    I have been awake for hours. A dead man does not sleep. A dead man lies still and counts, and I have counted the whole house waking below me, and none of it coming up the stair, until now.

    Footsteps. Three sets, I think. And a key.
    """

    play sound door_knock

    captain """
    Mr Manning?
    """

    """
    I do not answer. It is not difficult. It is the easiest part.
    """

    captain """
    He may still be asleep. Stand back a little.
    """

    play sound door_open

    """
    The key turns, and the door comes open, and the light of the corridor falls across my face, and I do not move a muscle in it.

    I keep my eyes not quite shut. A hair's width, no more. Enough to see the ceiling and a piece of the wall and the shapes of them in the doorway.

    The straight man. And behind him the boy, and the hat.

    Do not come closer. Look at the throat, and the sheet, and the chair on its side, and do the sum, and do not come closer.
    """

    pause 1.0

    """
    The Captain takes two steps into the room.

    Two.

    Then he stops, the way every one of them always stops, and I hear his breath go out of him.
    """

    captain """
    Don't come in. Either of you.

    There is no need. He is dead. His throat has been cut.
    """

    lad """
    Are you certain? Shouldn't we check his—
    """

    captain """
    I have seen enough dead men, Mr Harring. I do not need to touch him to know.

    Come away. This is no sight for Miss Baxter.
    """

    """
    Bless you, Captain. Bless your decency and your weak stomach and your thirty years of not needing to touch them.

    A hand on my wrist would end me. A glass held to my lips. A finger under my jaw.

    None comes.
    """

    $ drunk_details.description_hidden.unlock('faked_death')

    """
    The boy makes a small sound. The hat does not.

    Then the straight man draws them both back into the corridor, and the door comes to, and the key turns in it again, locking a dead man safely in.

    And the footsteps go away down the stair.
    """

    $ stop_music()

    pause 1.0

    $ play_music('mysterious', 2)

    """
    I do not move for a long time after that.

    A quarter of an hour. Half of one. Long enough to be sure.

    Then I open my eyes properly, and I sit up in my own dried blood, and I am, as far as everybody living in this house believes, no longer a problem for anyone.

    It is the best position I have been in since I passed my Bar examination.
    """

    call change_time(9, 30)

    $ change_room('bedroom_drunk', dissolve)

    """
    The room in daylight.

    I get the worst of the port off my neck with the water in the jug, and I leave the rest, because a dead man who must be seen again had better stay a convincing one.

    I try the door. Locked, of course. He locked me in like a good and careful man.

    But a bedroom is not a cell. There is a window, and a drainpipe, and below it a scullery roof, and I was a boy once, in Gloucestershire, before I was anything else.

    Not yet, though.

    The house is full of the living, and the living talk, and a dead man walking the corridors would undo the whole performance.

    I lie back down on the dry side of the bed, and I wait, and I listen to Claythorn Manor going about the business of being haunted by me.
    """

    call change_time(11, 30)

    """
    By late morning the house has thinned.

    The straight man's voice, low, in the hall, and the boy's, and the hat's. Then a door, and the gravel, and one set of feet going out and not enough coming back.

    They are down to three, I think. The boy, the hat, and the thin woman, who I did not hear die and therefore did not.

    And whatever is going to happen in this house before the day is out, it is going to happen to the three of them, at the one place everything in this house has happened.

    The table.

    I get the window open.
    """

    $ stop_music()

    jump drunk_day3_afternoon
