
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


# GOOD question - if Lady Claythorn did not write the letters, then nobody in
# this room may be crossed off, and four people shut behind a door with the
# fifth is worse than six on an open road.
#
# Miss Baxter answers it by turning the suspicion on the mask: she claims she
# saw beneath it during the night and found nothing wrong with the face. That
# forces the binary choice at the end of the label:
#   - hold the lie -> broken_day3_morning_deny_mask, the argument still stands
#   - take the mask off -> broken_day3_morning_show_face, arrest and death
label broken_day3_morning_question_culprit:

    $ broken_details.saved_variables['day3_morning_good_questions'] += 1

    broken """
    I also have another theory I would like to share with you.
    """

    broken """
    Since last night we have all settled on Lady Claythorn.

    She lied to us, she emptied the house behind our backs, and she took the only motorcar.

    I would ask you to consider that she may not be the one who wrote the letters.
    """

    doctor """
    Not her?

    You were the one who proved to us she was lying, Mr Moody.
    """

    broken """
    She lied about the award and about the money, and I am certain of that.

    I am certain she came here to play a part.

    But think of what was in those letters.
    """

    broken """
    Mr Manning's named his wife, and the hospital, and the year she died.

    Mine named a paper signed in France, and the officer who put his name to it.

    Whoever wrote them had been through our lives with a pair of tweezers.
    """

    captain """
    Go on.
    """

    broken """
    Then consider last night.

    Whoever it is had a house full of sleeping people and every key in it.

    Instead the staff drove off and left us breathing, and we are still here to complain about it.

    That is not a murderer finishing her work.

    That is a hired household getting clear of it.
    """

    nurse """
    Then who is left, Mr Moody?
    """

    broken """
    That is my whole point, Miss Marsh.

    If Mr Harring was helped out of the world on Friday night, somebody stood in his room to do it.

    And nothing whatever obliges that somebody to have been sitting in the motorcar.
    """

    """
    I watch it take hold.

    Doctor Baldwin looks at Miss Marsh.

    Miss Marsh looks at Mr Manning.

    Nobody looks at anybody for very long.

    It is an ugly thing to do to a room, and I have done it deliberately.
    """

    broken """
    So I cannot name a culprit for you.

    I say only that we cannot cross a single name off, and that four of you shut behind a door with the fifth is precisely the arrangement our letter writer would choose.

    On an open road, in daylight, nobody is ever alone with anybody.
    """

    captain """
    That is a serious thing to say.

    It is also, I am sorry to admit, a reasonable one.
    """

    psychic """
    Reasonable.

    Yes, I dare say it is.

    And how very neatly it is arranged, Captain, that the one man who profits by our suspicion of one another is the man who has just planted it among us.
    """

    broken """
    I profit by nothing, Miss Baxter.

    I have put myself on the list with the rest of you.
    """

    psychic """
    Have you indeed.

    Then you will not mind my saying the thing that has sat on my chest since first light.
    """

    """
    She folds her hands in her lap and takes her time over it, and I feel the room turn like a tide.
    """

    psychic """
    I slept very badly.

    Some hour in the small of the night I woke, and the fire had burned down to ash, and every soul about me was asleep.

    You were asleep as well, Mr Moody, with your head fallen against the wing of your chair.

    And the mask had come away from your face.
    """

    """
    The room goes quiet in a manner I do not care for at all.
    """

    psychic """
    I looked at you a long while.

    I am not a squeamish woman, and I had prepared myself for something dreadful.

    But there was nothing dreadful to see.

    No burn.

    No scar.

    Nothing but a man's face, as whole as my own.
    """

    nurse """
    Miss Baxter, are you quite certain of what you saw?
    """

    psychic """
    I have spent a lifetime being told what I could not possibly have seen.

    I know the difference between a vision and a face.
    """

    doctor """
    Mr Moody.

    I have never once pressed you about the mask, and I hope you will grant me that.

    But I am a surgeon, and in three days you have not asked me for so much as an aspirin.

    That did strike me at the time.
    """

    drunk """
    A false face.

    Half of London is wearing one.

    Hers included.
    """

    """
    Nobody laughs.

    Captain Sinha has not moved at all, and that is a good deal worse than if he had.
    """

    captain """
    Mr Moody, a moment ago you told us that nobody in this room may be crossed off.

    You will understand that this includes you.

    And that it is now the only question in front of us.
    """

    """
    And there it is.

    Everything I have built these three days rests on a piece of painted tin and a woman who could not sleep.

    I can deny it. The fire was out, she was three parts asleep, and the mask covers what it covers.

    Or I can take the wretched thing off, and hand them the truth, and pray the truth is worth something in this house.
    """

    call run_menu(TimedMenu("broken_day3_morning_menu_mask", [
        TimedMenuChoice("Deny it. She was dreaming in the dark", 'broken_day3_morning_deny_mask', 0, early_exit=True),
        TimedMenuChoice("Take off the mask and show them your true face", 'broken_day3_morning_show_face', 0, early_exit=True),
    ]))

    return


# ------------------------------------
#   HOLDING THE LIE
#
#   The mask stays on and nothing is proved either way. The Captain hands the
#   argument back, so the question still counts, but the room will not look at
#   Moody in the same way again.
# ------------------------------------
label broken_day3_morning_deny_mask:

    """
    Thomas would have said nothing at all.

    Thomas let people look, and waited, and they always looked away first.

    So I do not hurry.
    """

    broken """
    Miss Baxter, the fire was out and you had been three parts asleep since midnight.

    What you saw was my cheek.

    The mask sits above it, it has never covered that side of my jaw, and there has never been anything the matter with it.
    """

    psychic """
    That is not what I saw.
    """

    broken """
    It is what there was to see.
    """

    """
    I keep my voice level, for a raised voice is a confession in this company.
    """

    doctor """
    It would settle the matter in ten seconds, you know.

    I should not even need to touch it.
    """

    broken """
    No, Doctor.

    I have worn this thing since Flanders, so that men might stop staring at me over their soup.

    I shall not take it off in a cold room to satisfy a lady who dreamed badly.
    """

    """
    That is the correct answer.

    It is the answer Thomas would have given, near enough word for word, and it is the answer that stops a decent Englishman where he stands.

    Doctor Baldwin, who is decent enough, sits back and studies the carpet.
    """

    nurse """
    ...Very well.
    """

    psychic """
    Very well indeed.
    """

    """
    Nobody presses me further.

    Nobody believes me either, not altogether, and that is the trouble with winning a thing on manners instead of on proof.
    """

    captain """
    Enough of it.

    Miss Baxter, whatever Mr Moody carries beneath that mask, it does not answer the point he made before you spoke.

    Somebody wrote those letters, and I cannot prove that somebody drove away last night.

    I should like an answer to that before I take any man's face into account.
    """

    """
    The Captain has handed me my argument back whole, and I do not believe I have ever been so grateful to a man in my life.

    But something has shifted in this room and it will not shift back.

    Miss Marsh has moved half a foot away from me on the couch.

    And Miss Baxter is watching the window with the calm of a woman who has said her piece and is content to let it work.
    """

    return


label broken_day3_morning_question_letters:

    $ broken_details.saved_variables['day3_morning_good_questions'] += 1

    # TODO NOTHING new is learned, we cover this before

    return


# WEAK question - the poison proves nothing except that Moody has been
# carrying a bottle of it about since Friday.
label broken_day3_morning_question_poison:

    broken """
    There is something none of you have seen.
    """

    """
    I take the bottle of rat poison from my coat and set it down on the billiard table.
    """

    broken """
    I took this from the scullery on Friday night.

    Doctor, I believe Ted Harring could have been poisoned.
    """

    """
    Doctor Baldwin picks the bottle up, turns it about, and hands it back to me with something close to pity.
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