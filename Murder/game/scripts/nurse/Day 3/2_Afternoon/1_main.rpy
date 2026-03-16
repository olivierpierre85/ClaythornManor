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
    """

    # Nurse encounters Ted and Amelia on the stairs, lies about oversleeping,
    # they prepare food together, then split up before the meal.
    call common_day3_afternoon_lad_psychic_stay

    # Nurse is now alone in the dining room with the plates.

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
    call common_day3_afternoon_lad_falls

    call common_day3_afternoon_nurse_revelation

    """
    No.

    This is not my illness.

    This is something else entirely.

    The food.

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
