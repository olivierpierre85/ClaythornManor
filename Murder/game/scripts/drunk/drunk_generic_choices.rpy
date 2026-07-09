# Generic drunk Dialogs.
# Accessible from :
#                   - The Nurse
#                   - Broken (Saturday hunt, via the _broken variants below)

label drunk_generic:

    # Reset if previous early exit
    $ current_character.saved_variables["drunk_generic_menu"].early_exit = False

    call run_menu(current_character.saved_variables["drunk_generic_menu"])

    return


label drunk_generic_weather_friday_dinner:

    drunk """
    The weather?
    """

    drunk """
    Splendid.

    Absolutely... splendid.

    Or is it dreadful?

    No matter.
    """

    nurse """
    Of course.
    """

    """
    Well, at least he is not worried about the storm.
    """

    return


label drunk_generic_background_nurse:

    drunk """
    About myself?
    """

    nurse """
    Yes, if you don't mind.

    What is your profession?
    """

    drunk """
    Ah, well.

    I am a man of the law.

    A barrister, you see.

    Or I was.

    Doesn't... doesn't quite matter now, does it.
    """

    nurse """
    Oh, and what sort of barrister were you?
    """

    drunk """
    A defence barrister.

    Look, it's... it's complicated.

    I'd rather not bore a lady.
    """

    nurse """
    Why did you stop, Mr Manning?
    """

    drunk """
    Why did I stop.

    There were cases.

    Cases I should not have taken.

    Or should have... handled differently.

    The law is a merciless thing when you get it wrong.
    """

    nurse """
    What happened?
    """

    drunk """
    Nothing worth repeating.

    Ancient history, all of it.
    """

    """
    He trails off and stares into his glass.

    Hard to believe this person is, or at least was an attorney.

    I wonder what could have happened to him to make him like this.
    """

    $ drunk_details.description_hidden.unlock('job')

    return


label drunk_generic_heroic_act_nurse:

    nurse """
    Why were you invited here, Mr Manning?
    """

    drunk """
    Invited?

    I was... invited because I am a man of... of the people.

    Or so they seem to think.

    I've taken on cases no one else would touch.

    The poor, the... the desperate.

    Someone has to, don't they?
    """

    nurse """
    That is rather admirable of you.
    """

    drunk """
    Admirable.

    Ha.

    Yes, well.

    Don't go writing it in the papers.
    """

    """
    A brief, bitter laugh escapes him.

    Whatever good he has done, it clearly brings him little comfort.
    """

    $ drunk_details.description_hidden.unlock('heroic_act')

    return


label drunk_generic_manor:

    drunk """
    Grand old place, isn't it.

    Full of... full of history, I suppose.
    """

    return


label drunk_generic_manor_broken:

    drunk """
    This place?

    You mean the forest?

    Well it is a decent spot in the woods I suppose.

    Why do yo ask?
    """

    broken """
    No, I meant the manor.

    I think.
    """

    drunk """
    Very grand house that is,

    very impressive.
    """

    return

label drunk_generic_age_broken_intro:

    drunk """
    How old am I?

    Too old for all of this.

    Fifty-five years, if you must know.

    Fifty-five years and... and not a thing to show for it.
    """

    return


label drunk_generic_age_nurse:

    call drunk_generic_age_broken_intro

    """
    I would have guessed much older that that, but alcohol can ravage a man's body.

    He empties his glass.

    Then he waves to the footman for another one.
    """

    $ drunk_details.description_hidden.unlock('age')

    return

label drunk_generic_age_broken:

    call drunk_generic_age_broken_intro

    """
    Fifty-five years.

    Yet he looks a great deal older.

    He takes a sip from his flask.
    """

    $ drunk_details.description_hidden.unlock('age')

    return


label drunk_generic_room_friday:

    drunk """
    A room?

    They've given me a room, have they.

    Generous of them.

    I... I couldn't tell you which one.

    I haven't had the chance to see it yet.
    """

    return


label drunk_generic_room:

    drunk """
    The... the "George IV" room, I believe.

    Or some such name.

    Those kings, they all run together after a while.
    """

    $ unlock_map('bedroom_drunk')

    return


label drunk_generic_other_guests_friday_dinner:

    drunk """
    The other guests?
    """

    drunk """
    Interesting lot.

    Very... very interesting.

    I'm sure they're all perfectly fine.
    """

    """
    He waves a hand vaguely in the direction of the dining table.

    I suppose that is as much as I shall get from him.
    """

    return


# ---------------------------------------------------------------------------
# BROKEN (Thomas Moody) variants
# Manning is questioned at the Saturday hunt lunch, flask in hand, so his
# answers cover the same ground as the nurse versions in a rougher state.
# ---------------------------------------------------------------------------

label drunk_generic_background_broken:

    broken """
    Tell me a little about yourself, Mr Manning.

    What is your profession, if you don't mind my asking?
    """

    drunk """
    My profession.

    Ha.

    You are looking at a man of the law, sir.

    A barrister.

    Or... or what remains of one.
    """

    broken """
    A barrister, no less.

    What sort of practice did you keep?
    """

    drunk """
    Defence work.

    I stood up for men the whole world had already hanged.

    Somebody... somebody had to.
    """

    broken """
    And why did you give it up?
    """

    drunk """
    Give it up.

    Is that what I did.

    There were cases, Mr Moody.

    Cases that went... that went badly.

    The law is a merciless thing when you get it wrong.

    Leave it there, will you.
    """

    """
    He takes a long pull from the flask and will not meet my eye.

    A defence barrister

    An honourable job, but I am not sure it is one worthy of an award.
    """

    $ drunk_details.description_hidden.unlock('job')

    return


label drunk_generic_heroic_act_broken:

    broken """
    And why were you invited here, Mr Manning?
    """

    drunk """
    Well, I took the cases nobody else would touch, you see.

    The poor.

    The... the desperate.

    A man of the people, the papers said.

    Somebody has to speak for them, don't they?
    """

    broken """
    That is a fine thing to be honoured for.
    """

    drunk """
    Honoured, that is a strong word to  describe it.
    """

    """
    And that is also a rather vague reason to be invited here.
   
    Now that I think of it, so was Thomas's actually.

    It was more a general reason that linked to specific event.

    Is the given reason for the award always vague?
    """

    broken """
    Mr Manning, if you do not mind, can you tell me exactly what the letter was saying?
    """

    drunk """
    Letter, what letter? What do you know of a letter?
    """

    broken """
    I mean the invitation letter.
    """

    drunk """
    Oh... Right of course, well it is like I said.

    Due to you commitment to defending the poor and the needy, you were awarded the What's it's name award.

    Nothing special about it.
    """
   
    """
    Vague reason of course, but what was the hesitation about a letter.

    He clearly had another letter in mind, just like myself.
    """

    $ drunk_details.description_hidden.unlock('heroic_act')

    return


# NOT NEED and not reviewed yet
# label drunk_generic_other_guests_friday_nurse:

#     nurse """
#     What do you make of the other guests?
#     """

#     drunk """
#     Make of them?

#     They seem... they seem decent enough.

#     Or indecent enough.

#     Hard to say which at this stage.
#     """

#     drunk """
#     There is a doctor here, isn't there.
#     """

#     """
#     Something in his voice shifts — just for a moment.

#     Then he reaches for his glass again, and the moment passes.
#     """

#     return


# label drunk_generic_other_guests_saturday_nurse:

#     nurse """
#     What is your impression of the other guests, Mr Manning?
#     """

#     drunk """
#     My impression.

#     Right.

#     Well.

#     They are all... very much here.

#     That is my impression.
#     """

#     return


# label drunk_generic_host_saturday_nurse:

#     drunk """
#     Lady Claythorn?
#     """

#     drunk """
#     Formidable woman.

#     Truly.

#     Knows how to run a house, knows how to run a room.

#     I wouldn't cross her.

#     Not on a good day, at any rate.
#     """

#     $ drunk_details.description_hidden.unlock('status')

#     return


# label drunk_generic_doctor_saturday_nurse:

#     drunk """
#     The doctor.
#     """

#     drunk """
#     Yes.

#     He's... he's a doctor, isn't he.

#     I'm sure he's very... very capable.
#     """

#     """
#     His jaw tightens, almost imperceptibly.

#     He takes a long, slow drink before continuing.
#     """

#     drunk """
#     Very capable indeed.
#     """

#     return


# label drunk_generic_captain_saturday_nurse:

#     drunk """
#     Sinha?

#     Straight as a... as a ramrod, that one.

#     Army men always are.

#     Or claim to be.

#     I respect that.

#     I do.

#     Even if they make me feel rather... rumpled by comparison.
#     """

#     return
