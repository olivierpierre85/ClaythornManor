label common_day2_breakfast_follow_doctor_lad_host:

    $ change_room("bedrooms_hallway")

    if current_character.text_id == "lad":

        $ lad_details.saved_variables["day2_breakfast_follow"]  = True

        """
        I jump from my seat and walk behind the doctor.

        Soon, we stop in front of the Richard III Bedroom.

        They're so concerned that they don't say anything about my presence.
        """

    elif current_character.text_id == "doctor":

        """
        I followed Lady Claythorn and her Butler upstairs.

        For some reason, Ted Harring followed us.
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
    We all enter the room.
    """

    $ change_room('bedroom_broken')

    butler """
    He's here in his bed. He didn't respond when I tried to wake him up.
    """

    if current_character.text_id == "lad":

        """
        The doctor approaches the bed and takes the man's wrist.
        """

    elif current_character.text_id == "doctor":

        """
        I get close to the man on the bed.
        
        His body is stiff.
        
        I put my hand on his wrist.
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

    You may want to leave for this part.

    I'll come back downstairs when I have more information.
    """

    butler """
    Please come with me, My Lady.
    """

    host """
    Oh... Yes, of course...
    """

    if current_character.text_id == "host":

        return

    if current_character.text_id == "lad":

        """
        The butler escorts the Lady out of the room.

        The doctor turns to face me.
        """

    elif current_character.text_id == "doctor":

        """
        Lady Claythorn and the butler leave the room.

        Leaving me alone with Ted Harring.

        Why did he come with us?
        """


    doctor """
    Mister Harring, can I ask why are you here?
    """

    lad """
    I was just... I thought I could...
    """

    doctor """
    Never mind. Since you're here, make yourself useful.

    Help me turn him over to check for injuries.
    """

    if current_character.text_id == "lad":

        """
        He then examines the body thoroughly for a while.
        """

        call common_day2_breakfast_follow_doctor_lad_normal

    elif current_character.text_id == "doctor":

        """
        I proceed to examine his body for sign of foul play. I don't see anything.

        The body is very stiff, rigor Mortis has set early. 
        
        Which mean he must have died right after going to bed.

        In itself that's not unusual.

        Normally I would remove the mask for more observations.

        But it feels disrespectful, I think I should let the coroner do that.
        """

        if doctor_details.objects.is_unlocked('book_mystery'):

            """
            Yet, there is something bothering me.
            
            I remember the book I read yesterday.

            How did the victim die again? 

            Strychnine poisoning.

            That is probably a coincidence, but one of the main symptom is early rigor mortis.

            The others are : blue lips, foaming at the mouth and distorted facial expression.

            All of them I could easily check if I removed his mask.
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
    I don't remove the mask.

    No need to complicate things further.

    I have enough information as it is.
    """

    call common_day2_breakfast_follow_doctor_lad_normal

    return


label common_day2_breakfast_follow_doctor_lad_remove_mask:

    $ doctor_details.important_choices.unlock('broken_unmasked')

    """
    There is enough doubts, I can't ignore the clues.

    I have to see what's behind the mask.

    But I should be alone for that.
    """

    doctor """
    Thanks for your help Mister Harring.

    I will now examine Thomas Moody's face.

    Would you mind stepping out while I do it?
    """

    lad """
    No, of course not.
    """

    """
    When I am sure he has left the room, I remove Thomas Moody' mask.

    All the symptoms are there. His face now makes a scary grimace.
    
    There can be any doubts, he has been poisoned.

    While I am processing this information, something else struck me.

    It should have been the first thing I've noticed.

    I don't see any signs of disfigurement, nor scars.

    His face is intact.

    He never needed a mask.

    What does that mean?
    """

    # TODO find good music

    """
    I take a few moments to pounder what's happening.

    That's too much too fast.

    Thomas Moody's was murdered, there is no doubt about it.

    But he was also hiding behind a mask.

    Why? Was he hiding who he was?

    I don't understand.

    There is something really weird happening here today.

    I don't know what to do, but I think it's better to keep this information to my self for the moment.

    God only knows who I can trust here, I need more time to think.

    So I quickly put the mask back on and leave the room.
    """

    $ change_room("bedrooms_hallway")

    """
    Ted Harring is waiting for me in the hallway.
    """

    call common_day2_breakfast_follow_doctor_lad_normal

    return


label common_day2_breakfast_follow_doctor_lad_normal:

    lad """
    What could have caused this, Doctor?
    """

    doctor """
    I'm not sure. 

    He seemed in good health.

    But with injuries like the ones he sustained during the war, one can never be too sure.  

    A patient can be stable for years, and then suddenly, his body can fail him.  
    """

    lad """
    So it's a natural death?
    """

    doctor """
    It's possible, but I can't confirm.

    I can't rule out anything right now.

    We'd need an autopsy for a definitive answer.

    The next step is to notify the authorities.

    I need a phone.
    """

    if current_character.text_id == "lad":

        """
        He then exits the room.

        I follow him back to the dining room.
        """

    return