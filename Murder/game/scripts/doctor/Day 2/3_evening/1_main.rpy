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
    Oh my God! What happened?

    Is that Samuel Manning? Is he injured?

    Oh no. Is he... dead?
    """

    captain """
    I am sorry, my dear, but he is.
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
    How terrible. What was the quarrel about, Doctor?
    """

    """
    All eyes turn to me.
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
    I am back in my room, shaken by a wretched mix of nervousness and remorse.
    """

    if doctor_details.objects.is_unlocked('book_opium'):
        
        """
        I pace the room, my hands still trembling.

        The urge to reach for my laudanum is almost overwhelming.

        Yet the words from that book I read yesterday return to me with cruel clarity.

        I have been poisoning myself for years.

        If I go on like this, I shall end as helpless as any of my poorest patients.

        With a sudden surge of resolve, I open my bag and look down at the familiar little vials.

        For a long moment I merely stare at them.

        Then I close the bag again, leaving them untouched.

        I will endure the shaking and the sleeplessness if I must.

        Better a clear mind and a fighting chance than a drugged stupor in this house.
        """

    elif doctor_details.important_choices.is_unlocked('broken_unmasked'):
        

        """
        My first impulse is to seek relief in the usual way.

        I even reach for my bag before I stop myself.

        The image of Thomas Moody without his mask appears at once in my mind.

        Then I think of the letter I found in Samuel Manning's room.

        All of this is too strange, as though I had stepped into the pages of a mystery novel.

        It is plain that someone in this house is hiding something.

        If I dull my senses now, I might miss some vital clue, or fail to react when danger comes.

        I draw my hand back from the bag and clench it into a fist.

        No, I must keep my wits about me.

        Until I know whom I may trust, I shall remain sober.
        """

    else:

        """
        I do not know what to do.

        I feel as though I have no choice but to turn to the only thing I know will calm me.
        """

        jump doctor_laudanum_death

    call wait_screen_transition()

    call change_time(18,30)

    """
    I rest for a while, until the familiar sound of the gong draws me out of my thoughts.
    """
    
    play sound dinner_gong

    """
    I suppose I am steady enough to join the others for dinner.
    """

    $ change_room("dining_room", irisout)

    """
    Every one turns to me with...
    """
    
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
