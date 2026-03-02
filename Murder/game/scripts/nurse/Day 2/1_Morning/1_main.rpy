# --------------------------------------------
#   Nurse
#           
#   Saturday - Morning
# 
#   9:00 -> 11:00
#
#   Music: chill
#
#   Position
#       - Dining Room : Everyone else
#       - Dead : Broken
#
#   Notes :
#       - If day1_exhaustion is unlocked, nurse wakes with a cough
#       - Mirrors the doctor chapter flow; reuses common labels
# --------------------------------------------
label nurse_day2_morning:

    call change_time(9, 00, 'Morning', 'Saturday', hide_minutes = True, chapter='saturday_morning')

    $ nurse_details.add_checkpoint("nurse_day2_morning")

    call black_screen_transition("Rosalind Marsh", chapters_names[current_chapter])

    $ change_room("bedroom_nurse", irisout)

    $ play_music('chill', 3)

    if nurse_details.threads.is_unlocked('day1_exhaustion'):

        play sound woman_cough

        """
        I wake with a start — and immediately regret it.

        A fit of coughing seizes me before I am properly conscious.

        I grip the edge of the mattress and wait for it to pass.

        There is blood on the handkerchief. More than yesterday.

        I fold it away and sit quietly until the dizziness fades.

        I have been careless.

        From now on, I must be more careful about how much I push myself.
        """

    else:

        """
        I wake to a grey Scottish morning filtering through the curtains.

        A moment to take stock, then I rise.

        I slept better than I feared.
        """

    """
    I wash and dress methodically, whatever this day holds, it is best faced with one's wits about one.
    """

    call change_time(9, 30)

    $ change_room('dining_room', dissolve)

    """
    The dining room is already partially occupied.

    Captain Sinha sits alone at the far end of the table, eating in his customary silence.

    I take a seat and help myself to some toast and tea.

    Presently, Amelia Baxter and Ted Harring appear and settle nearby.

    They are engaged in some conversation.

    I do not follow it closely.

    Then Samuel Manning enters the room.

    He looks dreadful — waxy, unsteady, clutching the frame for a moment before making his way to the buffet.

    Nobody comments on it, though I notice Miss Baxter's expression harden considerably.

    He takes the seat beside me, bringing only a cup of black coffee—nothing to eat.

    While he thinks I am not looking, he gets a silver flask from his pocket and pours a generous measure into his cup.

    Well, that settles it, I am not talking to him this morning.

    Shortly after, the butler slips into the room and bends to murmur something in Lady Claythorn's ear.

    Her face changes at once.

    She rises and crosses towards the doctor.
    """

    call common_day2_morning_host_to_doctor

    """
    The room has gone quiet.

    Nobody is quite sure what has happened, but something clearly has.
    """

    call change_time(10, 0)

    $ change_room('dining_room')

    """
    After the doctor has gone upstairs with Lady Claythorn, the room settles into an uneasy hush.

    Nobody seems to know quite what to do with themselves.

    The food sits barely touched on most plates.
    """
    
    call change_time(10, 30)

    """
    It is not long before Doctor Baldwin and Lady Claythorn return.

    When they do, everyone looks up at once.
    """

    call common_day2_morning_host_death_doctor

    """
    After a while, everyone has finished eating.

    Or at any rate, has set down their cutlery and given up the pretence.
    """

    $ stop_music()

    call common_day2_morning_host_hunt

    """
    A hunt.

    I had rather forgotten about it, truth be told.

    Lady Claythorn looks at each of us in turn.
    """

    call common_day2_morning_hunt_captain_drunk

    """
    A few eyebrows are raised at this.

    Mr Manning looks in no fit state for a country walk, let alone a hunt.

    But no one says anything aloud.
    """

    call common_day2_morning_hunt_psychic

    host """
    Of course, I understand.

    And what about you, Miss Marsh?
    """

    """
    I think about it for a second.

    But a trudge across wet Scottish moorland, rifle in hand, is not what the doctor ordered.
    """

    call common_day2_morning_hunt_nurse

    call common_day2_morning_hunt_lad

    call common_day2_morning_hunt_host_to_doctor

    """
    Everyone turns towards the doctor.

    He glances around the table with a thoughtful expression.
    """

    call doctor_day2_hunt_choice

    call common_day2_morning_hunt_end

    """
    Very well, I can return to my room now.
    """

    jump nurse_day2_hunt

