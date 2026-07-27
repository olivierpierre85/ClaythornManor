
# ------------------------------------
#   THE QUESTIONS
#
#   Good discussions points can save Moody
# ------------------------------------
label broken_day3_morning_question_boxer:

    $ broken_details.saved_variables['day3_morning_good_questions'] += 1

    broken """
    Doctor, I remember you told me you served in the Boxer Rebellion.

    Was that correct?
    """

    doctor """
    It was.

    That was my first post as a field surgeon.
    """

    """
    It is dangerous to speak as Thomas here, for I do not know the details of his part in that conflict.

    But I must, if I am to prove my point.
    """

    broken """
    Quite.

    That struck me as odd, you see, because I fought in that war as well.
    """

    doctor """
    Really? Why did you not say so before?
    """

    broken """
    I do not like to dwell on the past much.

    But now I feel this could be relevant.
    """

    captain """
    It is indeed, for I was there myself.

    I was ...
    """

    nurse """
    Good heavens!

    So was I.
    """

    """
    A pause followed that declaration.
    """

    captain """
    You were, Miss Marsh?
    """

    nurse """
    Yes, as a very young nurse.
    """

    captain """
    That is extraordinary.

    Such a coincidence...
    """

    broken """
    Captain, it is clear this is no longer a coincidence.

    Four of us served in a relatively small conflict, decades ago.

    It is very likely the reason we have been gathered here.
    """

    doctor """
    What do you mean?

    What could have happened there?
    """

    broken """
    I do not know, but if we can find out, we might begin to understand what is happening here.

    First, it is important to know whether anyone else was with us in China at that time.

    Mr Manning?
    """

    drunk """
    Yes?

    I am sorry, what is it?
    """

    broken """
    We were wondering whether you fought in China, or were there at all, during the Boxer Rebellion.
    """

    drunk """
    China? No, I have never been there.

    And certainly not during any rebellion.

    I should remember that.
    """

    psychic """
    Nor I.

    I have never so much as left this country.
    """

    broken """
    Indeed.

    And Ted Harring was obviously too young to have been there.

    As for Lady Claythorn, she was in all likelihood too young as well.

    I am not certain of her age, but...
    """

    nurse """
    She would have been too young indeed.

    I was so young myself, and Lady Claythorn is a few years younger than I am.

    She would have been a child at that time.
    """

    broken """
    I see.

    Unlikely, but not impossible.

    Sadly, we shall not hear her point of view.

    But we may still try, between ourselves, to understand what happened.

    First, do you recognise any of the others?

    For myself, I do not recognise any of you.
    """

    """
    I can only hope Thomas did not know them either.
    """

    nurse """
    Well, we never spoke of it, but I believe I worked with Doctor Baldwin.
    """

    doctor """
    We did?

    I am sorry, I am not sure I remember you.
    """

    nurse """
    Of course, I was very young, and there were a great many nurses.
    """

    doctor """
    Of course.
    """

    captain """
    Now that I think of it, I may have heard or seen your name as well.

    But I do not believe we ever spoke.
    """

    doctor """
    I am sorry, Captain.

    I do not remember.
    """

    captain """
    I am not surprised.

    There were a great many other soldiers of Indian descent.
    """

    """
    An awkward silence follows.
    """

    broken """
    Well, that is not much to go on.

    Do you remember anything of note that could have linked the four of us together?
    """

    captain """
    That is hard to say.

    It was a long time ago.

    And a great many things of importance happened.

    As they tend to, in wartime.

    But I cannot think of anything in particular.
    """

    doctor """
    Neither can I.
    """

    nurse """
    Nor can I, sorry.
    """

    broken """
    It is all right.

    I cannot think of anything myself.
    """

    """
    But Thomas could have.

    I feel a pang at my heart when I think of him.
    """

    broken """
    Well, that does not help us much for the moment, but it is a start.
    """

    return


label broken_day3_morning_question_culprit:

    $ broken_details.saved_variables['day3_morning_good_questions'] += 1

    broken """
    I also have another theory I would like to share with you.
    """

    # When everyone is suspicious of the others: AMELIA BAXTER turns the suspicion towards him, and now you have to show you face or not. then DEATH, if not, people do not believe you more
        # TimedMenuChoice("Take off the mask and show them your true face", 'broken_day3_morning_show_face', 0, early_exit=True),


    return


label broken_day3_morning_question_letters:

    $ broken_details.saved_variables['day3_morning_good_questions'] += 1

    # TODO NOTHING new is learned, we cover this before

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

    His invitation arrived after he was buried.

    I took his name, and his face, and came here in his place, because I am a journalist and an invitation to a dead man is a story.

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
    Captain, you know what was under my door.

    You read it yourself.
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
    Captain, listen to me.

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