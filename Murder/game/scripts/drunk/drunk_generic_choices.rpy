# Generic drunk Dialogs.
# Accessible from :
#                   - The Nurse

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
    Oh, and which type of barrister were you?
    """

    drunk """
    A defence barrister.

    Look, it's... it's complicated.

    I'd rather not bore a lady.
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


label drunk_generic_age:

    drunk """
    How old am I?

    Too old for all of this.

    Fifty-five years, if you must know.

    Fifty-five years and... and not a thing to show for it.
    """

    """
    He catches himself, as if he said more than he intended.

    He empties his glass.

    Then he waves to the footman for another one.
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


label drunk_generic_room_nurse:

    drunk """
    The... the "George IV" room, I believe.

    Or some such name.

    They all run together after a while.
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

    I suppose that is as much as I shall get from him this evening.
    """

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
