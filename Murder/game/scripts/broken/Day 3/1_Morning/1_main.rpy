# --------------------------------------------
#   Broken
#
#   Sunday - Morning
#
#   8:30 -> 11:30
#
#   Music: mysterious, danger, scary
#
#   Position
#       - House : Captain, Doctor, Mr Manning, Miss Baxter, Miss Marsh, Broken
#       - Gone  : Lady Claythorn and all the staff (left in the night)
#       - Dead  : Lad (Ted Harring)
#
#   Structure:
#       - The watch ends, the Captain proposes to walk out
#       - The ladies refuse the seven miles, the doctor is feverish and
#         Mr Manning could not manage the road either. The Captain quietly
#         proposes that the two of them go alone
#         (broken_day3_morning_ladies_refuse - shared by both branches)
#       - Without the 'ambushed' ending (no intuition) there is no choice at
#         all: Moody accepts the split and the two of them set out
#         -> broken_day3_afternoon_pair -> broken_ending_ambushed
#       - With it, the departure menu (broken_day3_morning_menu_leave) opens:
#           - set out with the Captain anyway (replays the ambush)
#           - refuse to be split {{intuition}} -> broken_day3_morning_insist
#       - Insisting opens the argument menu
#         (broken_day3_morning_menu_convince). The time budget allows three
#         questions before the room stops listening, and two of the four must
#         be the right ones. Enough good questions -> left_together;
#         not enough -> the Captain and Moody go alone after all.
#         TODO the four questions are placeholders for now (see the labels
#         below). Only the Boxer Rebellion and the culprit questions count.
#       - The menu also offers the trap: showing the true face
#         (broken_day3_morning_show_face). The Captain arrests the impostor,
#         binds him to his bed and leaves alone -> broken_ending_burned
#
#   (MAYBE => the psychic will say she saw part of your face while sleeping)
#   keep for later.
# --------------------------------------------
label broken_day3_morning:

    $ broken_details.add_checkpoint("broken_day3_morning")

    call change_time(8, 30, 'Morning', 'Sunday', hide_minutes = True, chapter='sunday_morning')

    call black_screen_transition("Thomas Moody", chapters_names[current_chapter])

    $ change_room('billiard_room', irisout)

    $ play_music('mysterious', 2)

    """
    Dawn comes when I wake up, stiff in my watch chair.

    I can't believe I fell asleep.

    Captain Sinha is looking at me with a hint of reproach.
    """

    captain """
    I see you managed a little sleep, Mr Moody.

    It is alright, I did not.

    Do not worry, nothing happened during the night.
    """

    broken """
    Good. I am sorry, I did not think I would fall asleep.
    """

    captain """
    It happens. Do not blame yourself too much over it.
    """

    """
    I look around the room. Everyone is awake now, all of them dishevelled.

    Doctor Baldwin is in particularly bad shape, having contracted a sort of fever.

    Samuel Manning is already back to drinking from his pocket flask.

    The ladies have managed to make themselves presentable, and Captain Sinha looks as though he had a normal night's sleep.

    I wonder what I look like, but it hardly matters now.

    It is time for action, and Captain Sinha takes the lead.
    """

    captain """
    Alright, now that everyone is awake, I think it is time we planned our next move.
    """

    """
    People murmur in agreement.
    """

    captain """
    Good. What I suggest is this.

    Let us go quickly to our rooms and get ready for the long walk.

    We can meet afterwards in the entrance hall.

    The sooner we leave, the better.
    """

    psychic """
    Captain, Miss Marsh and I have just had a discussion.

    And we believe we shall not make it.
    """

    call broken_day3_morning_ladies_refuse

    if not broken_details.endings.is_unlocked('ambushed'):

        # No intuition yet. He has nothing to argue with, so the party splits
        # and the two of them take the road.
        call broken_day3_morning_accept_split

        call broken_day3_morning_leave_pair

        jump broken_day3_afternoon

    # ------------------------------------
    #   INTUITION - he has walked this road before
    # ------------------------------------
    $ play_music('danger', 2)

    """
    Two of us on the road, and four of us behind these walls.

    Something in me refuses it, flatly, the way a hand refuses a hot plate.

    I could not tell anyone why.

    I only know that the thought of that lane, and the bracken banks along it, fills me with a dread I have not earned.

    Ted Harring died alone in his bed.

    Samuel Manning was found alone with his letter, and I was very nearly alone in a wood with a rifle at my back.

    Everything that has happened in this house has happened to somebody who was on his own.
    """

    $ time_left = 1

    call run_menu(TimedMenu("broken_day3_morning_menu_leave", [
        TimedMenuChoice("Refuse. Nobody is to leave this house in halves.{{intuition}}", 'broken_day3_morning_insist', early_exit=True),
        TimedMenuChoice("Set out for the village with Captain Sinha", 'generic_cancel', early_exit=True),
    ], image_right = "captain"))

    if broken_details.threads.is_unlocked('left_together'):

        call broken_day3_morning_departure_together

        jump broken_day3_afternoon

    call broken_day3_morning_leave_pair

    jump broken_day3_afternoon


# ------------------------------------
#   THE REFUSAL (shared by both branches)
#
#   The ladies will not walk, the doctor has his fever and Mr Manning
#   could not manage the road. The Captain draws Moody aside and proposes
#   that the two of them go alone.
# ------------------------------------
label broken_day3_morning_ladies_refuse:

    captain """
    Not make it, Miss Baxter?

    It is seven miles of road. Long, but no worse than that.
    """

    psychic """
    Seven miles for a soldier, Captain.

    For me it might as well be seventy.

    I have not walked further than a garden in fifteen years, and I would be sitting in a ditch before the second mile.

    You would have to leave me there, and I do not think any of you would.
    """

    nurse """
    Miss Baxter is not exaggerating, and I am no better.

    My health has never been strong, and a whole day on a wet road would finish me.

    Nor could Mr Manning manage it, whatever he tells you.
    """

    drunk """
    I could try, Miss Marsh.
    """

    nurse """
    You could try, and you would fall, and then we should have to carry you.
    """

    drunk """
    ...Yes. Yes, I suppose that is the truth of it.
    """

    """
    Doctor Baldwin has said nothing at all.

    He is sitting very upright in his chair, which I have learned is what he does when he is trying not to shake.
    """

    doctor """
    I shall save you the trouble of asking.

    I am running a fever, and I have been since the small hours.

    I would be a burden on the road, and I know it.

    I shall stay, and I shall be of some use here at least, with two patients to look after.
    """

    drunk """
    And I shall stay with them.

    I am no great protection, God knows.

    But I will not have the ladies left in this house with nobody but a sick doctor.
    """

    """
    So that is the arithmetic of it.

    Four here, and however many of us take the road.

    Captain Sinha catches my eye, and moves a step or two away from the others before he speaks, low enough that only I can hear him.
    """

    captain """
    Mr Moody. A word.

    They are right, and it changes nothing. Somebody must fetch the police.

    If it is only the two of us, we shall be there by the middle of the afternoon.

    Burdened with the rest, we should still be in the wood at nightfall, and I would rather not be.
    """

    return


# ------------------------------------
#   NO INTUITION - he accepts the split
# ------------------------------------
label broken_day3_morning_accept_split:

    """
    I cannot find a single thing wrong with what he says.

    Two men move quickly. Four people stay behind a locked door with a doctor and a lawyer to watch it.

    It is sensible. It is what any reasonable person would arrange.

    And still something turns over in me when I agree to it, and I cannot for the life of me say what.
    """

    broken """
    Very well, Captain.

    The two of us, then.
    """

    return


# ------------------------------------
#   THE DEPARTURE OF TWO
#   (the split he accepted, and the argument he lost)
# ------------------------------------
label broken_day3_morning_leave_pair:

    call change_time(9, 30)

    $ change_room('entrance_hall', dissolve)

    broken """
    The rest of you keep together, in one room, with the door shut until we come back.

    Together, mind. Nobody wanders this house alone, not for a moment, not for any reason.
    """

    nurse """
    We shall be in the tea room. You will find us all exactly where you left us.
    """

    """
    We take our coats, and two walking sticks from the stand by the door.

    Mr Manning follows us out onto the step and grips my hand harder than his shaking ought to allow.
    """

    drunk """
    Come back, sir.

    I find I have grown accustomed to you.
    """

    return


# ------------------------------------
#   INSISTING - the argument
#
#   He refuses to be split, and must now give them a reason. Three
#   questions may be put to the room before they stop listening, and two
#   of the four are the right ones.
#
#   TODO all four questions are placeholders. The Boxer Rebellion and the
#   culprit questions are the good ones and increment the counter.
# ------------------------------------
label broken_day3_morning_insist:

    broken """
    No.

    Forgive me, Captain, but no. Not two of us, and not four of us.

    Six of us, together, or none of us at all.
    """

    captain """
    Mr Moody, you have heard the ladies. They cannot walk it.
    """

    broken """
    Then we go slowly, and we stop when they need to stop, and we arrive at dusk instead of at three.

    But we do not divide this house into a party on the road and a party behind a door.
    """

    psychic """
    And why not, pray?

    You say it as though you were reading it off a wall somewhere.
    """

    """
    Because I know it.

    That is not an answer I can give them.

    A man who says he simply knows is a man they will smile at and walk around.

    They will hear me out for a few minutes, no more, and every word had better be a stone in a wall.
    """

    nurse """
    Mr Moody, we are all tired and frightened, and I would rather not be frightened by guesswork.

    If you have a reason, give it to us plainly.
    """

    $ time_left = 30

    call run_menu(TimedMenu("broken_day3_morning_menu_convince", [
        TimedMenuChoice("TODO - the Boxer Rebellion", 'broken_day3_morning_question_boxer', 10),
        TimedMenuChoice("TODO - who among us is the culprit", 'broken_day3_morning_question_culprit', 10),
        TimedMenuChoice("TODO - third question, to be written", 'broken_day3_morning_question_three', 10),
        TimedMenuChoice("TODO - fourth question, to be written", 'broken_day3_morning_question_four', 10),
        TimedMenuChoice("Take off the mask and show them your true face", 'broken_day3_morning_show_face', 0, early_exit=True),
        TimedMenuChoice("Let it go. Their minds are made up.", 'generic_cancel', 0, keep_alive=True, early_exit=True),
    ], image_right = "nurse"))

    if broken_details.saved_variables['day3_morning_good_questions'] >= 2:

        call broken_day3_morning_convinced

        return

    call broken_day3_morning_not_convinced

    return


# ------------------------------------
#   THE QUESTIONS (placeholders)
# ------------------------------------
# TODO write the question, the answer it draws out, and what it proves to
# the room. GOOD question - it counts towards convincing them.
# TODO consider gating this on the doctor_boxer observation.
label broken_day3_morning_question_boxer:

    $ broken_details.saved_variables['day3_morning_good_questions'] += 1

    """
    TODO - the Boxer Rebellion question, and what it shakes loose.
    """

    return


# TODO write the question and the answer.
# GOOD question - it counts towards convincing them.
label broken_day3_morning_question_culprit:

    $ broken_details.saved_variables['day3_morning_good_questions'] += 1

    """
    TODO - putting it to the room that one of them may be the culprit.
    """

    return


# TODO write the question and the answer.
# WEAK question - it costs him time and proves nothing.
label broken_day3_morning_question_three:

    """
    TODO - third question, a wasted one.
    """

    return


# TODO write the question and the answer.
# WEAK question - it costs him time and proves nothing.
label broken_day3_morning_question_four:

    """
    TODO - fourth question, a wasted one.
    """

    return


# ------------------------------------
#   THE ARGUMENT WON
# ------------------------------------
label broken_day3_morning_convinced:

    """
    I stop there, and let the room sit with it.

    Nobody says anything clever. Nobody says anything at all for a while.

    That silence is worth more than any of the words I have just spent.
    """

    nurse """
    ...Very well.

    I shall make Mr Manning something to keep him on his feet, and we shall take the miles slowly.

    Rosalind Marsh has walked further on worse errands.
    """

    doctor """
    I am not sure I can do it.

    But I am a good deal less sure I want to be left in this house.

    I shall walk until I cannot, and then I shall walk a little further.
    """

    psychic """
    Oh, this is madness.
    """

    """
    She looks at the window, and at the four faces around her, and something goes out of her shoulders.
    """

    psychic """
    But it is a madness with company in it, and I have had quite enough of the other sort.

    If we are all to walk, then let us walk.
    """

    captain """
    Then it is settled, and we have wasted enough of the morning.

    Mr Moody, I hope you are right.
    """

    broken """
    So do I, Captain.
    """

    $ broken_details.threads.unlock('left_together')

    return


# ------------------------------------
#   THE ARGUMENT LOST
# ------------------------------------
label broken_day3_morning_not_convinced:

    """
    I can see it in their faces before anybody speaks.

    Whatever I have given them, it has not fitted together into the one shape I needed them to see.
    """

    psychic """
    I am sorry, Mr Moody. Truly.

    But none of that is a reason to march me into a wood.
    """

    nurse """
    Nor me, and certainly not Mr Manning.

    We shall wait. It is what waiting rooms are for.
    """

    captain """
    Mr Moody, we cannot stand here arguing until noon.

    Two of us, and quickly, or nobody at all.
    """

    """
    And there it is.

    I have spent everything I had and moved not one of them an inch.

    The dread has not left me. It has only stopped being any use.
    """

    return


# ------------------------------------
#   THE TRAP - showing the true face
#
#   An impostor under a dead man's name, in a house with a murdered man in
#   it. The Captain does the correct thing, and the correct thing kills
#   Moody.
# ------------------------------------
label broken_day3_morning_show_face:

    $ stop_music()

    """
    Words have failed, and I have one thing left that is not a word.

    They have spent three days looking at a piece of painted tin and calling it a man.

    Let them see what has been talking to them.
    """

    broken """
    Very well.

    You will not take my reasons. Take this instead.
    """

    """
    I reach up, and unfasten the mask, and set it down on the billiard table.
    """

    pause 1.0

    """
    The room goes very still.

    Miss Baxter's hand rises to her mouth. Miss Marsh does not move at all.

    Doctor Baldwin half stands, staring at a face that carries none of the ruin he has been imagining all weekend.
    """

    broken """
    My name is not Thomas Moody.

    Thomas Moody was my friend. He came home from Flanders behind that mask, and he died this spring in a rented room in Liverpool.

    His invitation arrived after he was buried. I took his name, and his face, and came here in his place, because I am a journalist and an invitation to a dead man is a story.

    Everything else I have told you this weekend is true.

    Now will you listen to me?
    """

    """
    Nobody answers.

    The doctor sits down again, slowly.

    And Captain Sinha, who has not said a word, walks around the billiard table and picks up the mask, and turns it over in his hands as though it were evidence.

    Which, I realise a good deal too late, is exactly what it is.
    """

    $ play_music('danger', 2)

    captain """
    Let us be clear about what you have just told us, sir.

    You entered this house under a false name.

    You have lied to every person in this room for three days, at every meal, with a straight face and a good deal of skill.

    And there is a young man lying dead upstairs.
    """

    broken """
    Captain, you know what was under my door. You read it yourself.
    """

    captain """
    I read a paper that you gave me.

    I have no idea now who wrote it, and neither, I think, do you.
    """

    """
    He is not angry. That is the worst of it.

    He is doing arithmetic, and I have handed him the figures.
    """

    nurse """
    He talked us into that room last night.

    He told us where to sleep, and who should keep watch, and when.
    """

    psychic """
    And he has been asking questions of every one of us since Friday.

    All those little kindnesses. All that patient interest.
    """

    broken """
    Miss Baxter, if I had wanted any of you dead, you would have died in your beds while I sat awake beside you.
    """

    captain """
    That may be so.

    But I am not able to prove it, and I am not able to disprove it either.

    So I shall do the only correct thing available to me.
    """

    call change_time(10, 00)

    $ change_room('bedroom_broken', dissolve)

    """
    There is no struggle worth the name.

    The doctor is feverish and Mr Manning is drunk, but the Captain is neither, and I am a man of forty-three who has never in his life hit anybody.

    They walk me up to my own room, which is a courtesy of a sort.
    """

    captain """
    You will remain here until the police come. That is not a punishment, sir, it is an arrest.

    I would rather have locked the door and left it at that.

    But there is a lock on the inside of it as well, and I do not know this house well enough to be certain there is not another way out.
    """

    """
    They use the cord from the curtains, and the belt from my own coat.

    The Captain does it himself, and does it well, and checks it twice, and I understand that he has done this before to men who deserved it more.
    """

    captain """
    I shall walk to the village alone. It is faster, and after this morning I do not think anyone else will come.

    Miss Marsh has your keys. She will bring you water at noon.

    If you are what you say you are, you have my apology in advance, and you shall have it properly when I return with the constables.
    """

    broken """
    Captain. Listen to me.

    Do not leave this house with four people in it and one door.
    """

    captain """
    Goodbye, Mr Moody.
    """

    """
    The door shuts.

    The key turns.

    I lie on my own bed, in my own room, tied at the wrists and the ankles with my own belt, and I listen to the front door close beneath me.

    And I have never in my life felt so entirely alone.
    """

    call wait_screen_transition()

    call change_time(11, 00)

    $ play_music('scary')

    play sound broken_glass

    """
    I do not know how long I lie there.

    Long enough for the light to move across the ceiling. Long enough to work the cord loose at one wrist, and no further.

    Then, somewhere below me, glass breaks.
    """

    play sound fire loop

    """
    There is no shouting afterwards. That is the thing I cannot make sense of.

    Glass breaks in a house with four people in it, and nobody calls out at all.

    Then I smell it.

    Smoke, coming under the door, thin and grey and perfectly patient.
    """

    """
    I pull at the cord until my wrist is wet, and it does not give.

    The room grows warm, then hot.

    I shout until there is nothing left in my throat to shout with, and the house does not answer.

    Somebody waited three days for a chance like this, and I gave it to them myself.

    I took off the only thing that was keeping me alive, and I handed them a man tied to a bed.
    """

    jump broken_ending_burned


# ------------------------------------
#   THE DEPARTURE OF SIX
# ------------------------------------
label broken_day3_morning_departure_together:

    call change_time(10, 30)

    $ play_music('mysterious', 2)

    $ change_room('entrance_hall', dissolve)

    """
    It takes the better part of an hour to make six people fit for seven miles.

    Coats and sound boots. Bread and cold water from the kitchen. Every walking stick the hall stand owns.

    Miss Marsh mixes Mr Manning something in the cold scullery that smells of nothing pleasant, and stands over him until he drinks it.

    The doctor is grey to the lips and says he is perfectly well.

    I fix the mask back on before we go out. It has one more day of work in it, and I find I would rather have it between me and the road.

    At half past ten I open the front door, and we step out into the grey morning.

    All six of us.
    """

    return
