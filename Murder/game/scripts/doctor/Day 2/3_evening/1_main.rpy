# --------------------------------------------
#   Doctor
#           
#   Saturday - Evening
# 
#   15h -> 23h
#
#   Music: sad
#
#   Position
#       - House: Everyone else
#       - Dead : broken, DRUNK
#
#   Notes : 
#       - Team with nurse
#       - Map 120 minutes
# --------------------------------------------
label doctor_day2_evening:

    call change_time(15,00, 'Evening', 'Saturday', chapter='saturday_evening')

    $ doctor_details.add_checkpoint("doctor_day2_evening") 
    
    call black_screen_transition("Daniel Baldwin", chapters_names[current_chapter])

    $ change_room("great_hall", irisout)

    $ play_music('sad')

    """
    I am still in shock when we reach the mansion.

    I can scarcely recall what happened in the woods.

    Samuel Manning bled to death whilst I tried to save him.

    The other group, drawn by the noise, rejoined us to witness the horrific scene.

    Once it was clear the poor man was dead, Captain Sinha took charge and had us carry Samuel Manning back to the house.

    I still can hardly believe it.

    I have killed a man.

    I cannot seem to convince myself that it was him or me.

    Yet I must not waste time dwelling on it.

    The others will have questions.

    I must think very carefully about what I am going to say to them.

    As we enter, we are greeted by Rosalind Marsh and Amelia Baxter.
    """

    psychic surprised """
    Oh my God! What happened!?

    Is that Samuel Manning? Is he injured?

    Oh no! Is he... dead?
    """

    captain """
    I'm sorry, dear, but he is.
    """

    psychic """
    But... what happened?
    """

    captain """
    It was an accident. 

    He got into a fight with Doctor Baldwin.

    And he accidentally shot himself.
    """

    psychic """
    Oh my god, what was the fight about Doctor?
    """

    $time_left = 1
    call run_menu(
        TimedMenu("doctor_day2_evening_reason", [
            TimedMenuChoice("Say he was just too drunk", 'doctor_day2_evening_reason_drunk', early_exit = True),
            TimedMenuChoice("Say nothing", 'doctor_day2_evening_reason_silence', early_exit = True),
            # TimedMenuChoice("Tell the truth {{object}}", 'doctor_day2_evening_reason_truth', early_exit = True), # Add to many complications
        ])
    )

    $ change_room("bedroom_doctor")

    call change_time(16,00)

    """
    I am back to my room, shaken with a mix of nervousness and remorse.
    """

    if doctor_details.objects.is_unlocked('book_opium'):
        
        # Don't die cause resolve to stop doing drugs

        """
        TODO
        """
        
    elif doctor_details.important_choices.is_unlocked('broken_unmasked'):
        
        # Don't die because you are too curious and too worry and want your wits about you.
        """
        TODO
        """


    else:

        """
        I don't know what to do, I feel like I don't have a choice but to get the only thing I know will calm me down.

        So I reach to my bag and grab a couple a vial of laudanum.
        """

        # TODO dead because no distractions

    jump work_in_progress


label doctor_day2_evening_reason_silence:

    """
    I try to think of something to say, yet I am at a loss for words.

    My mind feels quite empty.

    Everyone is looking at me with concern.
    """

    captain """
    There is no need to answer, Doctor.

    I am sure it was all a misunderstanding.

    It is quite obvious what happened.
    """ 

    call doctor_day2_evening_reason_drunk_silent

    return


label doctor_day2_evening_reason_drunk:

    doctor """
    I have no idea what he was angry about.

    I only wished to speak to him about his drinking, and he lost his temper with me.

    He was not making any sense, then he pointed his gun at me.

    Without thinking, I tried to jump him and wrest the weapon away, but, but...
    """

    call doctor_day2_evening_reason_drunk_silent

    return


label doctor_day2_evening_reason_drunk_silent:

    captain """
    The poor man shot himself by accident.

    I cannot say I am surprised, I think we all noticed his state of inebriation today and yesterday.

    Samuel Manning clearly had troubles he could not master.

    There is no reason to blame yourself, Doctor.
    """

    psychic """
    Of course, we are all quite certain you only wished to help that poor soul.
    """

    """
    I hear a murmur of assent from everyone.

    They will not suspect a thing.

    It is true that most people will believe a doctor without a second thought.

    I should be safe from now on.
    """

    doctor """
    Thank you, everyone.

    It has been a horrific experience.

    If you do not mind, I think I shall retire to my room now.
    """

    captain """
    Of course not, Doctor, go and rest.

    We shall have Mr Manning taken to his room for the time being.

    Will you assist me, Mr Harring?
    """

    lad """
    Of course.
    """

    return
