# --------------------------------------------
#   Nurse
#
#   Sunday - Afternoon
#
#   12:00 -> Ending
#
#   Music: mysterious
#
#   Position
#       - House: lad, captain, psychic, doctor
#       - Attic: nurse (hiding)
#       - Dead : broken, drunk
#       -? : Host
#
#   Notes :
#       - Nurse is hiding in the butler's room with stolen silver
#       - She waits for the drive to clear before attempting to leave
#       - Captain leaves the manor to get help (heard from attic)
#       - She slips out once the drive is quiet
# --------------------------------------------
label nurse_day3_afternoon:

    call change_time(12, 00, "Afternoon", "Sunday", hide_minutes=True, chapter='sunday_afternoon')

    $ nurse_details.add_checkpoint("nurse_day3_afternoon")

    call black_screen_transition("Rosalind Marsh", chapters_names[current_chapter])

    $ change_room("butler_room", irisout)

    $ play_music('mysterious')

    """
    I sit on the edge of the narrow bed, hands folded, listening.

    The manor has been restless all morning — footsteps, doors, muffled voices I cannot quite make out.

    Then, at last, the front door.

    It opens. It closes.

    And after that, silence.

    Not the silence of people holding still, but the silence of an empty house.

    I wait a little longer, counting my breaths.

    Nothing.

    It is time.
    """

    $ change_room("entrance_hall", dissolve)

    """
    The entrance hall is deserted.

    I cross to the window and glance at the drive.

    No figures. No movement. Just the gravel and the grey sky beyond.

    Good.

    I check the weight of my bag — the candlesticks, the salver, the spoons.

    All still there.

    I should leave now, while the way is clear.

    But my stomach tightens with a familiar pang.

    I have not eaten since yesterday evening, and the walk to the nearest village will be long.

    The kitchen is just below. It would take only a few minutes.

    A foolish risk, perhaps. But I shall need my strength.
    """

    $ change_room('basement_stairs', dissolve)

    """
    I am halfway down the service stairs when I hear voices.

    Two of them, coming from the ground floor.

    My heart lurches.

    The house was supposed to be empty.
    """

    pause 1.0

    """
    I recognise the voices — Ted Harring and Amelia Baxter.

    They are heading this way.

    There is no time to retreat.

    Very well. I shall have to be convincing.
    """

    $ play_music('mysterious', 2)

    nurse """
    Hello!
    """

    pause 1.0

    nurse """
    Is there someone here?
    """

    psychic """
    Oh my God, Miss Marsh, you're here!
    """

    nurse """
    Of course I am here. Why do you look so surprised?

    I'm afraid I overslept. I don't feel quite like myself today.

    When I woke up, I went to check the dining room but found it empty.

    I wandered in the house for a while but I didn't see anyone until I met you.

    Where is everybody?
    """

    """
    The lie comes easily enough. I have had practice.
    """

    psychic """
    Oh my dear, we don't know.
    """

    """
    They tell me what has happened since this morning.

    Mr Manning — dead. The doctor — missing. Lady Claythorn — vanished.

    Captain Sinha has gone to fetch help.

    I keep my expression steady throughout.

    Not too alarmed, not too indifferent.

    Just the right measure of concern.
    """

    nurse """
    Poor Mr Manning, what a terrible fate.

    And what horror that must have been for you, my dear.

    Are you all right?
    """

    psychic """
    I am better now.

    Captain Sinha should be back with help soon, so I'll be fine if I can keep my mind occupied until then.

    Speaking of which, we were heading to the kitchen to see if we can prepare some sort of meal.
    """

    """
    Food. Precisely what I came down here for.

    And now I have company for it.
    """

    nurse """
    Right, it's a good idea. We might as well keep ourselves busy.
    """

    $ change_room('kitchen', dissolve)

    $ stop_music(2)

    """
    The kitchen is cold, the stove unlit.

    We look around for something to eat.
    """

    psychic """
    There isn't much.

    But I think we can manage a light luncheon if you're not picky.
    """

    nurse """
    I'll help you.
    """

    """
    Mr Harring offers to assist, but between Miss Baxter and myself we have it well in hand.

    He takes a seat and watches.

    While we prepare the food, I keep my composure.

    As far as they know, I simply overslept.

    All I need do is eat, wait for the right moment, and slip away.
    """

    pause 1.0

    $ change_room('dining_room', dissolve)

    """
    We carry the plates to the dining room and sit down.

    Mr Harring sets the table and then tries to leave.
    """

    psychic """
    Where are you going, Mr Harring?

    It's better if we stick together at all times.
    """

    lad """
    I understand, but there's something I need to do alone.

    We haven't had a moment apart the entire day and...
    """

    psychic """
    Say no more, I understand.

    I'm in the same situation.

    What about you, Miss Marsh?
    """

    nurse """
    Oh, I'm fine, thank you.

    You both go, I'll finish preparing the table.
    """

    psychic """
    Very well.

    Let's meet back here in a few minutes then.
    """

    lad """
    Of course.
    """

    pause 1.0

    """
    They leave.

    I am alone with the plates.

    Three places, three meals, all from the same pot.

    And yet something stops me.

    A thought — quiet, persistent, impossible to dismiss.

    If someone has been killing the guests one by one, the food is the simplest means.

    I have no proof. Only instinct, sharpened by years of watching people die.

    I look at my plate.

    Then at Mr Harring's.

    If I am wrong, no harm done.

    If I am right...

    I swap my plate with his.
    """

    pause 1.0

    """
    They return, and we eat in silence.

    The food is plain but filling.

    I watch the other two carefully, looking for any sign that something is amiss.

    Nothing. We finish our meal without incident.

    Perhaps I was being foolish after all.
    """

    pause 2.0

    """
    Mr Harring stands and offers to help with the dishes.

    But as he rises, something changes in his expression.
    """

    $ play_music('danger', fadeout_val=2)

    lad surprised """
    What's happening?

    Why am I...
    """

    """
    He cannot finish the sentence.

    His legs give way beneath him.
    """

    play sound body_fall

    """
    He collapses to the floor.

    I rush to his side. My training takes over before my mind catches up.
    """

    nurse """
    Mr Harring, can you hear me?
    """

    psychic """
    What's happened?

    How is he?
    """

    """
    I check his pulse.

    There is nothing.
    """

    nurse """
    He has no pulse.

    He's dead.
    """

    psychic """
    What?! No, that can't be.

    How is this possible?
    """

    nurse """
    I'm not sure, but I doubt it's a coincidence at this point.

    I believe he's been poisoned.
    """

    """
    Poisoned.

    From the plate I gave him.

    The plate that was meant for me.

    I was right about the food.

    And now a man is dead because of what I did.
    """

    psychic """
    No, no, no ...

    Mr Harring, why?
    """

    """
    Miss Baxter weeps.

    I barely hear her.

    I swapped the plates. I know what that means.

    If I tell the truth, they will think I am the poisoner.

    If I stay silent, I might still get out of this.

    But I cannot stay silent. Not entirely.

    Because if my plate was poisoned, then someone in this house wanted me dead.

    And there are only two people left.
    """

    pause 1.0

    nurse """
    All I know is that he wasn't the target.

    I switched my plate with his before we started eating.

    I was the one supposed to die, not him.
    """

    psychic """
    You switched plates? Why?
    """

    nurse """
    Why?!

    After all that's happened, weren't you suspecting anything?
    """

    psychic """
    ...
    """

    nurse """
    When I woke to find this place empty, I knew something was wrong.

    I heard the three of you rummaging around the house and I hid.

    I didn't trust Sushil Sinha, but once he left I felt safe enough to reveal myself.

    But I should have been more suspicious of Ted Harring.

    After all, he was the least respectable of everyone here.

    Clearly out of place in this environment.

    And I bet I can prove it.
    """

    pause 1.0

    """
    I search his pockets.

    My fingers close around cold metal.

    A revolver.
    """

    nurse """
    Look. He even had a weapon on him the whole time.

    He...
    """

    pause 1.0

    """
    I stop.

    Something is wrong.

    Not with the room. With me.

    A wave of nausea rises from my stomach, sudden and sharp.

    My vision swims.
    """

    nurse """
    I don't know what his motives were, but...
    """

    pause 1.0

    nurse """
    ...it doesn't matter now.
    """

    """
    My hands tremble.

    The revolver feels impossibly heavy.
    """

    nurse """
    Wait, something feels off.
    """

    pause 1.0

    """
    I grasp the chair for support.

    The room tilts.
    """

    $ stop_music(2)

    nurse """
    I think I'm going to faint.
    """

    """
    No.

    This is not my illness. I know what my illness feels like.

    This is something else entirely.

    The food. All of it was poisoned.

    Every plate. Every portion.

    There was never a safe choice.

    I was dead the moment I sat down.

    The swap changed nothing.
    """

    play sound body_fall

    """
    My knees hit the floor.

    The cold of the stone rises through me.

    I think of the silver in the butler's room.

    The candlesticks, the salver, the spoons.

    All for nothing.

    Everything, from the very first letter, was for nothing.
    """

    jump nurse_ending_poisoned
