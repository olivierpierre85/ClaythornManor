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
#   Gates on the 'ambushed' ENDING (intuition), not on a thread:
#       - without it  -> no menu at all, the party splits, two men walk out
#       - with it     -> the argument menu opens. 30 minutes of patience, ten
#         minutes a question, so three may be asked. Two of them must be the
#         right ones (day3_morning_good_questions >= 2) to unlock
#         'left_together' and take the whole party out together.
#
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

    It is all right, I did not.

    Do not worry, nothing happened during the night.
    """

    broken """
    Good. I am sorry, I did not think I would fall asleep.
    """

    captain """
    It happens.

    Do not blame yourself too much for it.
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
    Very well, now that everyone is awake, I think it is time we planned our next move.
    """

    """
    People murmur in agreement.
    """

    captain """
    Good.

    What I suggest is this.

    Let us go quickly to our rooms and get ready for the long walk.

    We can meet afterwards in the entrance hall.

    The sooner we leave, the better.
    """

    psychic """
    Captain, Miss Marsh and I have been speaking quietly together these last few minutes.

    And we have come to the sorry conclusion that we shall never make it.
    """

    captain """
    Not make it, Miss Baxter?

    It is a long journey, I will admit, but not a difficult one, merely a matter of following the road.

    And we shall walk slowly, and stop as often as you need.
    """

    psychic """
    I do not doubt it is only a stroll to a man of your training, Captain.

    But my constitution is not the thing it once was, and I am not dressed for such an undertaking.
    """

    nurse """
    And I am no better.

    My health has never been strong, and a whole day on a wet road would be very taxing.
    """

    """
    Captain Sinha considers this, then turns towards me.
    """

    captain """
    Perhaps they are right, Mr Moody.

    This journey might not be fit for the ladies.

    It would be best if they stayed here.

    And even the men are not in perfect shape.
    """

    """
    He looks at Samuel Manning, and Doctor Baldwin.

    They both look sickly and exhausted.
    """

    captain """
    We would certainly go faster, just the two of us.

    We could fetch help and be back before sundown.

    What do you think?
    """

    if not broken_details.endings.is_unlocked('ambushed'):

        """
        I do not like it, but cannot think of a strong argument against his idea.
        """

        call broken_day3_morning_leave_pair

        jump broken_day3_afternoon

    # ------------------------------------
    #   INTUITION - he has walked this road before
    # ------------------------------------
    $ play_music('danger', 2)

    """
    Something in me refuses it, flatly, though I could not tell why.

    If we do not leave together, something terrible will happen.

    But how can I convince everyone of this?
    """

    $ time_left = 30

    call run_menu(TimedMenu("broken_day3_morning_menu_convince", [
        TimedMenuChoice("Ask Doctor Baldwin where he first served", 'broken_day3_morning_question_boxer', 10),
        TimedMenuChoice("Ask who carried the letters through the house", 'broken_day3_morning_question_culprit', 10),
        TimedMenuChoice("Ask the Captain whether the tree was cut", 'broken_day3_morning_question_tree', 10),
        TimedMenuChoice("Show them the bottle of rat poison", 'broken_day3_morning_question_poison', 10),
        TimedMenuChoice("Take off the mask and show them your true face", 'broken_day3_morning_show_face', 0, early_exit=True),
        TimedMenuChoice("Let it go. Leave with Captain Sinha", 'generic_cancel', 0, early_exit=True),
    ]))

    if broken_details.saved_variables['day3_morning_good_questions'] >= 2:

        call broken_day3_morning_departure_together

    else:

        if time_left <= 0:

            """
            I can see it in their faces before anybody speaks.

            Whatever I said was not convincing enough.
            """

            psychic """
            I am sorry, Mr Moody.

            Truly, I am.

            But not one word of it is reason enough to send me walking into a wood.
            """

            nurse """
            Nor me.
            """

            captain """
            Mr Moody, we cannot stand here arguing until sundown.
            """

            """
            And there it is.

            I have spent everything I had and moved not one of them an inch.

            The dread has not left me.

            It has only stopped being any use.
            """

        else:

            """
            I see in their eyes that I shall not be able to convince them.

            That leaves me only one choice.
            """

        call broken_day3_morning_leave_pair

    jump broken_day3_afternoon

# ------------------------------------
#   THE QUESTIONS
#
#   Two of the four move the room. Both weak ones are things Moody believes
#   and cannot prove this morning, and the afternoon proves him right about
#   the tree once it is far too late to matter.
# ------------------------------------
# GOOD question - the invitations were written by somebody who studied us all.
# The doctor_boxer observation only changes how Moody opens: knowing the
# answer, he asks the doctor to repeat it, otherwise he asks blind and gets
# the same one. It is deliberately not a condition on the choice, since two
# good questions must stay reachable for every player.
label broken_day3_morning_question_boxer:

    $ broken_details.saved_variables['day3_morning_good_questions'] += 1

    if broken_details.threads.is_unlocked('doctor_boxer'):

        broken """
        Doctor, on Friday evening you told me where you first served.

        Would you say it again, so that everybody hears it?
        """

    else:

        broken """
        Doctor, before the War, where did you first serve?

        Say it aloud, if you will.
        """

    doctor """
    China.

    The summer of 1900, the Boxer Rebellion.

    I was twenty-three, and the youngest surgeon in the column.
    """

    broken """
    Thank you.

    Now, the letter that brought you to this house praised you for ten years at St Margaret's.

    A charity hospital, and a worthy thing, and a thing four hundred other men in England could claim just as well.

    It did not mention China at all.
    """

    doctor """
    No.

    No, it did not.
    """

    broken """
    Nor did mine name anything a man could check.

    Nor the Captain's.

    But the letters that came afterwards, the ones pushed under our doors, were exact.

    Mr Manning's named his wife, and her hospital, and the year she died.

    Mine named the day I was sent forward, and the officer who signed the order.
    """

    """
    I let that sit with them a moment.
    """

    broken """
    Whoever brought us here praised us for things any clerk could find in a newspaper.

    And then, once we were safely inside, showed us the things nobody could.

    That is not a hostess who has run out of money and lost her nerve.

    That is somebody who has spent months among our lives, and who is not finished with them.
    """

    """
    The doctor has gone the colour of the sheet across his knees.

    Miss Marsh says nothing at all, which from her is a great deal.
    """

    nurse """
    Months.
    """

    broken """
    Months.
    """

    return


# GOOD question - nobody in this room can clear anybody else, which makes a
# shut door behind four people worse than an open road under six.
label broken_day3_morning_question_culprit:

    $ broken_details.saved_variables['day3_morning_good_questions'] += 1

    broken """
    Then let me put a plain question to the room.

    Those letters were not posted to us.

    They were carried through this house in the night and pushed under our doors.

    Can any one of you tell me who carried them?
    """

    """
    Nobody answers.

    Miss Baxter looks at the doctor.

    The doctor looks at Mr Manning.

    Mr Manning, for once, looks at nobody at all.
    """

    broken """
    No.

    Neither can I.

    And that is precisely my difficulty with leaving four of you sitting in this house.
    """

    nurse """
    You are saying that one of us wrote them.
    """

    broken """
    I am saying I cannot prove that none of us did.

    The staff had keys to this house, certainly.

    So has every person standing in this room.

    If I am wrong, we have a long dull walk and a good story for the sergeant.

    If I am right, then four of you will sit behind a shut door all afternoon, and one of you will already be on the inside of it.
    """

    """
    Nobody has an answer to that.

    Miss Marsh's hands have gone quite still in her lap, which I have not seen once all weekend.

    Even Miss Baxter has stopped shaking her head.
    """

    return


# WEAK question - he is right about the tree and cannot show them a thing.
# They walk past the saw cut in the afternoon, whichever way the morning goes.
label broken_day3_morning_question_tree:

    broken """
    Captain, the tree across the road.

    You looked at it yourself on Saturday.

    Would you swear a storm brought it down?
    """

    captain """
    I would swear I do not know.

    The crown was in the ditch and the wind had been at it all night.

    I did not examine the stump with a glass, Mr Moody.

    I will not swear to a thing I did not see.
    """

    broken """
    But if it were cut...
    """

    captain """
    If.

    I have been a soldier long enough to be careful with that word.
    """

    psychic """
    There, you hear it for yourselves.

    Mr Moody has raised us an entire cathedral upon the word if.

    A tree fell in a storm, and a poor young man died in his sleep, and upon those two sorrows we are asked to walk seven miles through a wood.
    """

    """
    Ten minutes gone, and a good deal of ground with them.

    I should have kept the tree to myself until I could stand somebody in front of the stump.
    """

    return


# WEAK question - the poison proves nothing except that Moody has been
# carrying a bottle of it about since Friday. It hands Miss Marsh a stick to
# beat him with, and sets up the arrest if he later takes off the mask.
label broken_day3_morning_question_poison:

    broken """
    There is something none of you have seen.
    """

    """
    I take the bottle from my coat and set it down on the billiard table.

    The label is plain enough, and so is the skull printed above it.
    """

    broken """
    I took this from the scullery on Friday night.

    Doctor, I believe Ted Harring was poisoned.
    """

    """
    Doctor Baldwin picks the bottle up, turns it about, and hands it back to me with something close to pity.
    """

    doctor """
    Arsenic, Mr Moody.

    Had that young man swallowed this, he would have died on his knees, and the whole floor would have heard about it for hours.

    He was quiet, and he was cold, and there was not a mark upon him.

    I examined him myself.
    """

    nurse """
    And how long have you been carrying it about, Mr Moody?
    """

    broken """
    Since Friday.

    For safe keeping.
    """

    nurse """
    Quite.
    """

    """
    Ten minutes gone, and I have put a bottle of poison in Miss Marsh's mind with my own name attached to it.

    That was not clever.
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

    You will not take my reasons.

    Take this instead.
    """

    """
    I reach up, and unfasten the mask, and set it down on the billiard table.
    """

    pause 1.0

    """
    The room goes very still.

    Miss Baxter's hand rises to her mouth.

    Miss Marsh does not move at all.

    Doctor Baldwin half stands, staring at a face that carries none of the ruin he has been imagining all weekend.
    """

    broken """
    My name is not Thomas Moody.

    Thomas Moody was my friend.

    He came home from Flanders behind that mask, and he died this spring in a rented room in Liverpool.

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
    He is not angry.

    That is the worst of it.

    He is doing arithmetic, and I have handed him the figures.
    """

    nurse """
    He talked us into that room last night.

    He told us where to sleep, and who should keep watch, and when.
    """

    psychic """
    And he has been asking questions of every one of us since Friday.

    All those little kindnesses.

    All that patient interest.
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
    You will remain here until the police come.

    That is not a punishment, sir, it is an arrest.

    I would rather have locked the door and left it at that.

    But there is a lock on the inside of it as well, and I do not know this house well enough to be certain there is not another way out.
    """

    """
    They use the cord from the curtains, and the belt from my own coat.

    The Captain does it himself, and does it well, and checks it twice, and I understand that he has done this before to men who deserved it more.
    """

    captain """
    I shall walk to the village alone.

    It is faster, and after this morning I do not think anyone else will come.

    Miss Marsh has your keys.

    She will bring you water at noon.

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

    Long enough for the light to move across the ceiling.

    Long enough to work the cord loose at one wrist, and no further.

    Then, somewhere below me, glass breaks.
    """

    play sound fire loop

    """
    There is no shouting afterwards.

    That is the thing I cannot make sense of.

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
#   THE DEPARTURE OF TWO
# ------------------------------------
label broken_day3_morning_leave_pair:

    broken """
    Very well, Captain.

    The two of us, then.

    I assume Doctor Baldwin and Mr Manning will stay here to protect the ladies.
    """

    """
    Samuel Manning is still deep in thought.

    But Doctor Baldwin gives a slight nod in agreement.

    They will not be the best bodyguards today, but that will have to do.
    """

    broken """
    The rest of you keep together, with the door shut until we come back.

    Together, mind. Nobody wanders this house alone, not for a moment, not for any reason.
    """

    nurse """
    We shall stay here for as long as needed.

    Do not worry.
    """

    captain """
    Very well.

    No need to waste any more time, then.

    Mr Moody.
    """

    broken """
    Yes, let us go.
    """

    """
    We take our coats, exit the billiard room and leave Claythorn Manor behind us.
    """

    return


# ------------------------------------
#   THE DEPARTURE OF SIX
# ------------------------------------
label broken_day3_morning_departure_together:

    $ broken_details.threads.unlock('left_together')

    """
    I stop there, and let the room sit with it.

    Nobody says anything clever. Nobody says anything at all for a while.

    That silence is worth more than any of the words I have just spent.
    """

    nurse """
    ...Very well.

    I shall make Mr Manning something to keep him on his feet, and we shall take the miles slowly.

    I have walked further than that on worse errands.
    """

    doctor """
    I am not sure I can do it.

    But I am a good deal less sure I want to be left in this house.

    I shall walk until I cannot, and then I shall walk a little further.
    """

    psychic """
    Oh, this is madness, every word of it.
    """

    """
    She looks at the window, and at the four faces around her, and something goes out of her shoulders.
    """

    psychic """
    But I shall not be left the last soul rattling about in this house.

    If you are all set on going, then I shall go with you.
    """

    captain """
    Then it is settled, and we have wasted enough of the morning.

    Mr Moody, I hope you are right.
    """

    broken """
    So do I, Captain.
    """

    call change_time(10, 30)

    $ play_music('mysterious', 2)

    $ change_room('entrance_hall', dissolve)

    """
    It takes the better part of an hour to make six people fit for the journey.

    Coats and sound boots. Bread and cold water from the kitchen.

    At half past ten I open the front door, and we step out into the grey morning.

    All six of us.
    """

    return
