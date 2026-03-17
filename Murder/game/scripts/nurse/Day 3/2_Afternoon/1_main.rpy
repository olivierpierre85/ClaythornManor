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
    """

    $ time_left = 1
    call run_menu(
        TimedMenu("nurse_day3_afternoon_swap_plates", [
            TimedMenuChoice("Swap my plate with Mr Harring's", "nurse_day3_afternoon_swap_yes", TIME_MAX, early_exit = True),
            TimedMenuChoice("Leave the plates as they are", "nurse_day3_afternoon_swap_no", early_exit = True),
        ])
    )

    return


label nurse_day3_afternoon_swap_yes:

    $ nurse_details.important_choices.unlock('swapped_plates')

    """
    I swap my plate with his.
    """

    call nurse_day3_afternoon_meal

    pause 1.0

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

    But the poison hasn't taken me yet.

    And there is still one person in this room who isn't dying.
    """

    call common_day3_afternoon_nurse_accuses_psychic

    if nurse_details.threads.is_unlocked('take_gun') and nurse_details.threads.is_unlocked('find_bullets'):
        jump nurse_day3_afternoon_confrontation_armed
    else:
        jump nurse_day3_afternoon_confrontation_unarmed

    return


label nurse_day3_afternoon_swap_no:

    """
    No.

    I am clearly being paranoid.

    I leave the plates where they are.
    """

    call nurse_day3_afternoon_meal

    """
    I set down my fork.

    Something is wrong.

    Not with the room. With me.
    """

    $ play_music('danger', fadeout_val=2)

    """
    A wave of nausea rises from my stomach, sudden and sharp.

    My vision swims.

    I grip the edge of the table.
    """

    psychic """
    Miss Marsh? Are you quite all right?
    """

    """
    I try to answer, but my tongue feels thick and heavy.

    The room tilts.

    I know this feeling — not my illness, not the familiar ache in my chest.

    This is something else entirely.
    """

    nurse """
    The food...
    """

    psychic """
    What about the food?
    """

    nurse """
    It's been...
    """

    """
    I cannot finish the sentence.

    My legs give way beneath me.
    """

    play sound body_fall

    """
    My knees hit the floor.

    The cold of the stone rises through me.

    Through the haze, I see Mr Harring rushing to my side.

    Miss Baxter is saying something, but the words are very far away now.
    """


    jump nurse_ending_poisoned


# Shared: the meal itself, used by both swap and no-swap paths
label nurse_day3_afternoon_meal:

    pause 1.0

    """
    They return, and we eat in silence.

    The food is plain but filling.

    I watch the other two carefully, looking for any sign that something is amiss.

    Nothing. We finish our meal without incident.

    Perhaps I was being foolish after all.
    """

    return


# Armed confrontation: nurse has her own loaded gun
label nurse_day3_afternoon_confrontation_armed:

    call common_day3_afternoon_nurse_gun_confrontation

    call common_day3_afternoon_nurse_gun_fight

    """
    I am on the floor now.

    The ceiling swims above me.
    """

    jump nurse_ending_gunned_down


# Unarmed confrontation: nurse has no loaded gun
label nurse_day3_afternoon_confrontation_unarmed:

    """
    I lunge at her.

    It is a clumsy, desperate thing — more a stumble than an attack.

    But I catch her off guard and we both crash against the sideboard.
    """

    play sound broken_glass

    """
    She pushes me back and I stagger, catching myself on the table's edge.
    """

    play sound woman_cough

    """
    The cough comes.

    Not the small, manageable sort I have learnt to live with.

    This is the deep, tearing kind that brings blood with it.

    I double over, one hand pressed to my mouth, the other still gripping the table.
    """

    $ stop_music()

    """
    My body has nothing left to give.

    The poison, the illness, the exertion — it is all catching up at once.

    I slide to my knees.
    """

    play sound body_fall

    jump nurse_ending_exhausted
