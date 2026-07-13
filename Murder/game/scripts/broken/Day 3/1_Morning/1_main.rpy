# --------------------------------------------
#   Broken
#
#   Sunday - Morning
#
#   8:30 -> 11:30
#
#   Music: mysterious
#
#   Position
#       - House : Captain, Doctor, Mr Manning, Miss Baxter, Miss Marsh, Broken
#       - Gone  : Lady Claythorn and all the staff (left by motor car in the night)
#       - Dead  : Lad (Ted Harring)
#
#   Reached only from broken_day2_evening (found_poison + gather_everyone:
#   the household kept watch through the night). Broken had the small-hours
#   watch and saw the car leave at four in the morning, so the empty manor
#   is a confirmation for him, not a discovery.
#
#   Structure:
#       - The empty house: cold grates, the butler's keys left by the door,
#         the garage empty, the telephone line dead
#       - Broken proposes walking out to the police station together; the
#         others refuse - only the Captain will come
#       - The gate (broken_day3_morning_menu_leave):
#           - set out with only the Captain (always available)
#           - lay everything before them (intuition - requires the 'ambushed'
#             ending) -> the reveal, everyone agrees, unlocks left_together
#       - Both paths continue into broken_day3_afternoon
# --------------------------------------------
label broken_day3_morning:

    $ broken_details.add_checkpoint("broken_day3_morning")

    call change_time(8, 30, 'Morning', 'Sunday', hide_minutes = True, chapter='sunday_morning')

    call black_screen_transition("Thomas Moody", chapters_names[current_chapter])

    $ change_room('bedroom_broken', irisout)

    $ play_music('mysterious', 2)

    """
    Dawn comes grey and slow, and I am there to meet it, stiff in my watch chair at the head of the stairs.

    Nobody has tried a single door on my watch.

    Nobody has needed to. They simply left.

    I wash my face, fix the mask, and go down to see what the night has left us.
    """

    call change_time(8, 45)

    $ change_room('dining_room', dissolve)

    """
    The dining room is cold.

    The grates have not been laid, no breakfast has been set, and the table stands exactly as it was left last night.

    A house without servants makes a particular kind of silence, and it fills every room of this one.
    """

    $ change_room('entrance_hall', dissolve)

    """
    In the entrance hall, on the side table by the front door, someone has left the butler's ring of keys.

    Set down neatly, squared to the table's edge, like a bill presented at the end of a stay.

    We have been checked out of Claythorn Manor.
    """

    """
    The others come down one by one to find me standing over the keys.

    The Captain first, then Miss Marsh, then the doctor, grey and blinking. Mr Manning arrives combed and sober, and Miss Baxter last of all.

    It does not take long to put the picture together for them.
    """

    broken """
    The staff are gone, and Lady Claythorn with them.

    I heard a motor leave the drive some time past four this morning.

    It ran with its lamps out.
    """

    nurse """
    Gone?

    The whole household? That is absurd. Who abandons their own guests in the middle of the night?
    """

    captain """
    Somebody with a very good reason not to be here this morning.
    """

    """
    The Captain and I make a quick survey while the others stand in the hall.

    The kitchen is cold and stripped. The garage stands empty, doors ajar.

    And the telephone in the passage gives back nothing at all. Not even the exchange. The line is dead as the man upstairs.
    """

    call change_time(9, 30)

    $ change_room('tea_room', dissolve)

    """
    We gather in the tea room because nobody quite wants to sit in the dining room, with its one empty chair.

    Six of us, in a house that has been emptied around us like a stage after the interval.

    It is time somebody said it plainly, and it appears that somebody is me.
    """

    broken """
    I shall not dress it up.

    The road may be cleared by now or it may not, but I no longer believe the police are coming, today or at all.

    I believe the tree was put across that road, the same way the staff were put on that motor car.

    The village is seven miles by the road. It is not yet ten o'clock.

    I say we walk out of here, all six of us together, and bring the police back ourselves.
    """

    """
    For a moment nobody speaks.

    Then everybody does.
    """

    psychic """
    Walk? Seven miles?

    My dear Mr Moody, the authorities said they would come, and come they shall.

    We have only to remain calm and wait as we were asked. Rushing off into the woods will help nobody at all.
    """

    doctor """
    I am afraid I am with Miss Baxter.

    Half of us are in no state for such a march. I know I am not.

    Whereas these walls, whatever else may be said of them, are solid.
    """

    nurse """
    And Mr Manning could not manage seven miles of bad road, that is a plain medical fact.

    I will not send a patient out to collapse in the woods, and I will not leave one behind either.

    If he stays, I stay.
    """

    drunk """
    I could try, Miss Marsh...

    No. No, you are right, I could not.

    My spirit is willing, Mr Moody, but my legs have carried too much whisky for too many years.
    """

    """
    And that is that.

    Reasonable voices, every one, and every one of them wrong. I can feel it in my spine.

    But feeling is all I have to offer them, and feelings do not move people who are frightened and tired and clinging to the walls around them.
    """

    captain """
    I will come, Mr Moody.

    I said last night I would walk if the police did not appear, and a man is only as good as his word.

    Two of us can hold a fair pace and be back with help before dark.
    """

    """
    So there we stand.

    Four staying, two going.

    Something about the arithmetic of it worries at me, though I cannot put my finger on the why of it.
    """

    $ time_left = 1
    call run_menu(TimedMenu("broken_day3_morning_menu_leave", [
        TimedMenuChoice("Set out for the village with Captain Sinha", 'broken_day3_morning_leave_pair', early_exit=True),
        TimedMenuChoice("Lay everything before them. All of it.{{intuition}}", 'broken_day3_morning_reveal', early_exit=True, condition="broken_details.endings.is_unlocked('ambushed')"),
    ], image_right = "captain"))

    jump broken_day3_afternoon


# --------------------------------------------
#   LEAVE WITH THE CAPTAIN ONLY
# --------------------------------------------
label broken_day3_morning_leave_pair:

    """
    Two, then.

    It is not the arrangement I wanted, but it is the one I have, and every hour we spend debating it is an hour given away.
    """

    broken """
    Very well.

    The Captain and I will go. The rest of you keep together, in this room, until we return with the police.

    Together, mind. Nobody wanders this house alone.
    """

    """
    Miss Marsh nods as though I had prescribed something sensible.

    Mr Manning walks us to the door and grips my hand harder than his shaking ought to allow.
    """

    drunk """
    Come back, sir.

    I find I have grown accustomed to you.
    """

    """
    We take our coats, two walking sticks from the stand, and step out into the morning.
    """

    return


# --------------------------------------------
#   INTUITION - lay everything before them
#   (requires the 'ambushed' ending)
# --------------------------------------------
label broken_day3_morning_reveal:

    """
    Something about the arithmetic will not let go of me.

    Four here, two on the road. Divided, spread thin, each half of us out of the other's sight.

    Everything that has happened in this house has happened to people who were alone. Harring alone in his bed. Manning alone with his letter. Myself, very nearly, alone in a wood.

    Whoever has arranged this weekend does their work in private, and we are about to hand them two private opportunities at a stroke.

    No.

    They will not walk seven miles on my feelings. Very well.

    Then they shall have everything else.
    """

    $ stop_music()

    broken """
    Before anyone settles into waiting, there are some things you had better see.

    All of you.
    """

    """
    I lay the army order flat on the tea table, where every one of them can read it.

    Then I set the bottle of rat poison beside it.

    And then, because half-truths have carried us to this morning and I want no part of them any longer, I reach up and unfasten the mask.
    """

    pause 1.0

    """
    The room goes very still.

    Miss Baxter's hand rises to her mouth. The doctor half stands, staring at a face that carries none of the scars he has been imagining all weekend.
    """

    broken """
    My name is not Thomas Moody.

    Thomas Moody was my friend. He came back from Flanders behind a mask, and he died this spring, quietly, in a rented room in Liverpool, of the wounds he took in another man's place.

    When this invitation came for him, I took his name and his mask and came in his stead, because I am a journalist, and because an invitation to a dead man struck me as a story.

    I was wrong. It is not a story. It is a design.
    """

    """
    I give them all of it, in order, the way I would file it.

    The order under my door, naming Captain Sinha as the man who signed Thomas away to the line.

    The letter under Mr Manning's, naming Doctor Baldwin over his wife's grave.

    Two griefs, dug out of private records, sharpened, and posted under two doors in the same house on the same night.
    """

    captain """
    May I?
    """

    """
    The Captain takes up the order and reads it through twice, and for once there is nothing correct about his face at all.
    """

    captain """
    The signature is mine.

    I signed a great many of these, and I do not remember his name among them. That is the truth, and it does not flatter me.

    Somebody knew what I had forgotten, and built a murder on it.
    """

    drunk """
    And mine was real too. Every cruel word of it.

    What this man says is no fancy. I stood in that wood yesterday with a rifle and very nearly used it.

    He talked me down. He is the only reason the doctor took dinner with us last night.
    """

    """
    Baldwin goes white to the lips, and looks at Manning, and at me, and says nothing at all.

    I tap the bottle.
    """

    broken """
    Rat poison, from the scullery shelf, uncorked and half gone, in a house where a healthy young man died in the night without a mark on him.

    A staff hired for one weekend, who fled by motor at four this morning with their lamps out.

    A telephone line that is dead, and a tree across the only road.

    Whoever built this weekend kills quietly, and privately, and one at a time.

    So we do the one thing their design cannot digest.

    We stay in one another's sight, every one of us, and we walk out of here together.
    """

    """
    The silence afterwards is a different creature from the one before.
    """

    nurse """
    ...I shall make Mr Manning a walking mixture, and we shall take the miles slowly.

    Rosalind Marsh has walked further on worse errands.
    """

    doctor """
    Yes.

    Yes, I... quite. Together is best.
    """

    """
    Miss Baxter looks from the letter to the bottle to my naked face, and something passes across her own that I am too tired to read.
    """

    psychic """
    Well.

    If we are all to walk, then let us walk.
    """

    $ broken_details.threads.unlock('left_together')

    call change_time(10, 30)

    """
    It takes the better part of an hour to make six people fit for seven miles.

    Coats, sound boots, bread and water from the cold kitchen, and every walking stick the hall stand owns.

    I put the mask back on for the road. It has one last day of work in it.

    At half past ten, I open the front door, and we step out together into the grey morning.

    All of us.
    """

    return
