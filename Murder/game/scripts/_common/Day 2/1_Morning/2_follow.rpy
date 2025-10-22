label common_day2_breakfast_follow_doctor_lad_host:

    $ change_room("bedrooms_hallway")

    if current_character.text_id == "lad":

        $ lad_details.saved_variables["day2_breakfast_follow"] = True

        """
        I leap from my seat and follow the doctor.

        We soon stop outside the Richard III Bedroom.

        They're so preoccupied, no one comments on my presence.
        """

    elif current_character.text_id == "doctor":

        """
        I followed Lady Claythorn and her butler upstairs.

        For some reason, Ted Harring came along.
        """

    elif current_character.text_id == "host":

        """
        TODO
        """

    butler """
    Here we are. Thomas Moody's room.
    """

    $ unlock_map('bedroom_broken')

    """
    We all step into the room.
    """

    $ change_room('bedroom_broken')

    butler """
    He's here in his bed. He didn't respond when I tried to wake him up.
    """

    if current_character.text_id == "lad":

        """
        The doctor walks over and takes the man's wrist.
        """

    elif current_character.text_id == "doctor":

        """
        I approach the bed.

        The body is stiff.

        I place my hand on his wrist.
        """

    elif current_character.text_id == "host":
    
        """
        TODO
        """

    $ stop_music(fadeout_length=1)

    doctor """
    No pulse.

    He's dead.
    """

    $ play_music('scary')

    host surprised """
    Dead?!!!

    How is that possible?
    """

    doctor """
    I'm not sure yet. I'll need to examine him further.

    Best if you stepped out for this.

    I'll return downstairs once I know more.
    """

    butler """
    Please, My Lady—this way.
    """

    host """
    Oh... Yes, of course...
    """

    if current_character.text_id == "host":
        return

    if current_character.text_id == "lad":

        """
        The butler escorts Lady Claythorn out.

        The doctor turns to face me.
        """

    elif current_character.text_id == "doctor":

        """
        Lady Claythorn and the butler leave, 

        leaving me alone with Ted Harring.

        Why did he come up here?
        """

    doctor """
    Mr Harring, may I ask—why are you here?
    """

    lad """
    I was just... I thought I might...
    """

    doctor """
    Never mind. Since you're here, you can help.

    Let's turn him over and check for injuries.
    """

    if current_character.text_id == "lad":

        """
        He examines the body thoroughly for some time.
        """

        call common_day2_breakfast_follow_doctor_lad_normal

    elif current_character.text_id == "doctor":

        if doctor_details.important_choices.is_unlocked('broken_offended'):

            """
            I feel somewhat uneasy. Before me lies the body of a man who was rather cross with me the last time we spoke.
            
            And now he is dead.
            
            Well, it is not the first time that has happened to me, and I daresay it will not be the last.
            
            Still, I cannot help feeling bad about it.
            """

        """
        I examine the body carefully for signs of foul play. Nothing obvious.

        Rigor mortis has set in—quite early.

        Which suggests he died shortly after going to bed.

        Not unusual, in itself.

        Normally, I'd remove the mask for closer observation...

        But it feels wrong. Perhaps best left to the coroner.
        """

        if doctor_details.objects.is_unlocked('book_mystery'):

            """
            Yet something's nagging at me.

            That book I read yesterday—how did the victim die?

            Strychnine poisoning.

            Probably coincidence, but one of the telltale signs is early rigor mortis.

            Others include: blue lips, frothing at the mouth, and a twisted expression.

            All visible—if I remove the mask.
            """

            $ time_left = 1
            call run_menu(
                TimedMenu("doctor_day2_morning_remove_mask", [
                    TimedMenuChoice("Remove the mask", 'common_day2_breakfast_follow_doctor_lad_remove_mask', early_exit = True),
                    TimedMenuChoice("Don't remove the mask, let him rest in peace", 'common_day2_breakfast_follow_doctor_lad_keep_mask', early_exit = True)
                ])
            )

        else:

            call common_day2_breakfast_follow_doctor_lad_normal

    return


label common_day2_breakfast_follow_doctor_lad_keep_mask:

    """
    I leave the mask in place.

    No sense in stirring up more trouble.

    I've got enough to go on for now.
    """

    call common_day2_breakfast_follow_doctor_lad_normal

    return


label common_day2_breakfast_follow_doctor_lad_remove_mask:

    $ doctor_details.important_choices.unlock('broken_unmasked')

    """
    I can't ignore the signs. I need to see for myself.

    But I should be alone for this.
    """

    doctor """
    Thank you for your help, Mr Harring.

    I need to examine Thomas Moody's face now.

    Would you step outside?
    """

    lad """
    Of course.
    """

    """
    Once I'm sure the room is empty, I remove the mask.

    All the symptoms are present. His face twisted in a grimace.

    There's no doubt—he was poisoned.

    And then, something strikes me.

    I should've noticed it at once.

    No disfigurement. No scars.

    His face is untouched.

    He never needed a mask.

    What does that mean?
    """

    # TODO: find appropriate music

    """
    I pause, trying to make sense of it.

    Too many questions at once.

    Thomas Moody was murdered—that much is clear.

    But he also hid behind a mask.

    Was he hiding his identity?

    I don't understand it. Not yet.

    Best to keep this to myself for now.

    Until I know who I can trust.

    I replace the mask and leave the room.
    """

    $ change_room("bedrooms_hallway")

    """
    Ted Harring is waiting in the hallway.
    """

    call common_day2_breakfast_follow_doctor_lad_normal

    return


label common_day2_breakfast_follow_doctor_lad_normal:

    lad """
    What do you think happened, Doctor?
    """

    doctor """
    I'm not certain.

    He seemed in reasonable health.

    But war injuries can be unpredictable.

    Some patients are stable for years, then... sudden failure.
    """

    lad """
    So it was natural?
    """

    doctor """
    Possibly. But I can't be sure.

    Nothing can be ruled out.

    We'll need a post-mortem to know for certain.

    First, we should contact the authorities.
    """

    if current_character.text_id == "lad":

        """
        He leaves the room.

        I trail behind, back to the dining room.
        """
    
    elif current_character.text_id == "doctor":

        """
        We both head back downstairs.
        """


    return
