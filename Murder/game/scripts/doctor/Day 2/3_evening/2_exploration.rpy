label doctor_day2_evening_exploration:
    
    call change_time(21, 00)

    $ change_room("bedroom_doctor")

    $ play_music('mysterious', 2)

    """
    I now find myself faced with several courses of action.

    The most obvious would be to remain here in my room and wait for the morning.

    I could even move some furniture against the door to make certain no one can enter.

    Yet that, too, feels dangerous. There are other ways for someone to reach me.

    The alternative is to attempt to discover who wrote that note to Samuel Manning.

    That is the person I ought to fear.

    Everything points towards Lady Claythorn, yet I cannot be sure.

    If only I could trust at least one other person, I might ask for their assistance.

    It would be safer to investigate in company, but in whom ought I place my trust?

    It would be ideal to have someone implicitly trustworthy, like a judge.

    But everyone here appears suspicious to me.
    """

    if doctor_details.threads.is_unlocked('flirt'):

        """
        I might turn to Andrew. After the time we have spent together, I find it hard to picture him as a likely culprit.

        He is probably downstairs with the staff at present, unless he has already retired for the night.
        """

    if doctor_details.threads.is_unlocked('remember_nurse'):

        """
        By good fortune, I already know Nurse Rosalind Marsh. That acquaintance makes me more comfortable about approaching her.
        """

    if doctor_details.threads.is_unlocked('book_opium'):
        
        """
        I also have to manage symptoms of withdrawal.

        My hands tremble, and I am sweating more than is reasonable.

        They will only grow worse as the night wears on, which will not be in my favour.
        """

    """
    I feel very much at a crossroads.

    What I decide to do now may mean the difference between life and death.

    So what shall it be?
    """

    $ time_left = 90
    call run_menu(doctor_details.saved_variables["day2_evening_map_menu"])

    if doctor_details.threads.is_unlocked('trust_captain'):

        jump doctor_day3_morning_captain

    else:

        jump doctor_day3_morning_nurse

# Notable explorations
label doctor_day2_evening_bedroom_lad:

    $ change_room('bedroom_lad')

    play sound door_knock

    doctor """
    Mr Harring, are you there?
    """

    """
    For a moment there is no answer.

    Then I hear a faint voice from behind the door.
    """

    lad """
    Doctor Baldwin, is that you?
    """

    doctor """
    Yes.

    I should like a word with you, it is rather important.

    May I come in?
    """

    lad """
    Well, I don't know, doctor.

    I've already dragged a desk in front of the door.

    Might be better if we did the talking through it.
    """

    doctor """
    I am afraid it is a very sensitive matter.

    I would not care for anyone overhearing us.
    """

    lad """
    Oh.

    In that case, it is probably best if we wait until the morning.

    It will be easier to talk then.

    Good night, doctor.
    """

    doctor """
    No, it might be too late by then, I need to...
    """

    """
    I hear his footsteps recede and the faint creak of floorboards further inside the room.

    It seems Mr Harring has no intention of opening his door tonight.

    I had better try somewhere else.
    """
    
    return


label doctor_day2_evening_bedroom_broken:

    $ change_room('bedroom_broken')

    """
    Thomas Moody's room looks exactly as it did this morning.
    """

    if doctor_details.threads.is_unlocked('broken_unmasked'):

        """
        With all that has transpired since, I have scarcely given a thought to the mystery of Thomas Moody's mask.

        It is one more reason to question everything that is happening in this house.

        But there is nothing I can do about it from here.

        I should leave.
        """

    else:

        """
        The poor man's body lies just as before upon the bed.

        This morning I chose not to look beneath his mask, out of respect.

        After all that has occurred since, that restraint feels misplaced.

        I am compelled to examine him more closely.

        I step nearer to the bed and lean over him.

        At once I notice small details, such as the way the face beneath the mask does not seem as peaceful as it ought.

        Almost before I realise what I am doing, my hand reaches for the mask and I lift it away.
        """

        call doctor_day2_behind_the_mask
        

    return


label doctor_day2_evening_bedroom_nurse:

    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    doctor """
    Hello?
    """

    nurse """
    Yes?

    Is that you Doctor Baldwin?
    """

    doctor """
    Yes, it is.

    Do you mind if I come in for a minute?

    I have something important to discuss.
    """

    nurse """
    I do not know, Doctor. 

    It is late, and that would be rather inappropriate.

    Also, with everything that has happened today, I would prefer to stay alone.

    I hope you understand.
    """

    if doctor_details.threads.is_unlocked('remember_nurse'):

        doctor """
        I do understand, believe me.

        Yet, as you reminded me earlier, you and I have worked side by side in far less proper circumstances than this.

        I would not trouble you now without very good reason.
        """

        """
        There is a brief pause.

        I hear the soft creak of a floorboard, as if she has stepped closer to the door.
        """

        nurse """
        Very well, what is it then?
        """

        doctor """
        It is not something I care to discuss in the hallway.

        May I come in, just for a moment?
        """

        """
        For a few seconds there is only silence, and the faint crackle of a fire from within her room.
        """

        nurse """
        All right.

        Please come in, Doctor.
        """

        play sound door_open

        $ change_room("bedroom_nurse")

        """
        I step into Miss Marsh's room.

        She has not yet undressed, but her shoulders sag with weariness, and there are dark shadows beneath her eyes.
        """

        doctor """
        Thank you.

        I shall be as brief as I can.
        """

        """
        I give her a concise account of the letter I discovered in Samuel Manning's room.
        
        Then I explain how it urged him to provoke me before the hunt, and how it led, step by step, to his death.

        As I speak, the colour drains from her face.
        """

        nurse """
        Good heavens.

        Are you saying someone lured you both into that situation on purpose?
        """

        doctor """
        That is precisely what I fear.

        Whoever wrote that letter knew far too much, and I doubt they are finished.

        I believe they may try again, with me or with someone else in this house.
        """

        nurse """
        And you came to me because we worked together before?

        Because you think you can trust me?
        """

        doctor """
        Indeed, I would rather face this night with an ally than entirely alone.
        """

        nurse """
        I cannot pretend I am not frightened.

        Every sound in this place sets my nerves on edge.

        I am thinking, to be perfectly safe maybe you could ...

        No, never mind, it's probably not a good idea.
        """

        doctor """
        What could be? In these circumstances, we shouldn't be afraid to share what we think.
        """

        nurse """
        All right then, I meant that , if we really are in danger, you should probably ... sleep here tonight.

        Not on the bed I mean, maybe on a chair.

        I know it's very unconventional, but that would make me feel better.
        """

        call run_menu( TimedMenu("broken_generic_other_guests_friday_offense", [
                TimedMenuChoice("I guess it's the safest thing to do", 'doctor_day2_evening_bedroom_nurse_sleep_yes', TIME_MAX, early_exit = True),
                TimedMenuChoice("I'd rather sleep alone", 'doctor_day2_evening_bedroom_nurse_sleep_no', 0, early_exit = True),
            ])
        )

    else:

        """
        She is right.

        I cannot simply insist upon entering the room of a woman I scarcely know at this hour.

        I should not press the matter.
        """

        doctor """
        My apologies for disturbing you.

        I shall leave you in peace, Miss Marsh.

        Good night.
        """

        nurse """
        Good night, Doctor.
        """

    return


label doctor_day2_evening_bedroom_nurse_sleep_yes:

    doctor """
    Very well.

    If you will permit it, I shall take that chair by the door.

    You may lie down and try to sleep, and I shall keep watch.
    """

    nurse """
    Thank you, Doctor.

    I confess I shall feel safer knowing you are here.

    And I am sorry if I am not good company, but I imagine I shall be asleep in a few moments.
    """

    doctor """
    No worries, please rest.
    """

    """
    I move a straight-backed chair to a position where I can see both the door and the window.

    Miss Marsh sits upon the edge of the bed, then lies down without undressing, her eyes already half closed.
    """

    nurse """
    Wake me if anything seems amiss.

    Otherwise, let us hope the night passes quietly.
    """

    doctor """
    You have my word.

    Try to rest.
    """

    """
    The fire burns low in the grate, filling the room with a dull orange glow.

    I settle into the chair, listening to the ticking of the clock and the slow deepening of Miss Marsh's breathing as she drifts into sleep.

    Pretty soon it's my turn to doze off.
    """

    # call wait_transition
    # TODO add that miss marsh makes door sound, said she wanted to be sure the door was secured?
    # doctor """
    # Were you going somewhere?
    #"""

    $ doctor_details.threads.unlock("trust_nurse")

    return
    

label doctor_day2_evening_bedroom_nurse_sleep_no:

    doctor """
    I am truly sorry but I don'think this would be right.

    I believe it would best if we sleep in our own bed tonight.

    But we can convene first thing in the morning and get ready for whatever awaits us.
    """

    nurse """
    As you wish, Doctor.

    And... thank you for telling me.

    Whatever happens, I am glad you did not keep this to yourself.
    """

    """
    I incline my head and step back into the corridor.

    Miss Marsh follows me to the threshold and closes the door softly behind me.
    """

    $ change_room("bedrooms_hallway")

    """
    The hallway feels colder than before, and the silence of the sleeping house presses in on every side.
    """

    jump doctor_day2_evening_sleep_alone


label doctor_day2_evening_sleep_alone:    

    $ change_room("bedroom_doctor", dissolve)

    """
    I reach my room alone.

    I lock my door and do what I can to secure it.
    """

    play sound door_locked

    """
    Then I drag a chair and the small chest of drawers against the door, in case Lady Claythorn or one of her accomplices decides to pay me a visit.
    """

    play sound moving_furniture

    """
    Now that everything is in place, I lie down upon the bed, fully dressed in case I need to move quickly.
    """

    call doctor_day2_evening_captain_sleep_options

    $ stop_music()

    $ change_room("black_background", dissolve)

    $ play_music('danger', 2)

    """
    I do not know how long I have slept when a faint sound rouses me.

    It is a soft scrape, close by my ear, out of place in the stillness of the room.
    """

    """
    Before I can stir, a hand clamps hard across my mouth, stifling any cry.

    The weight of a body leans over me, pinning me to the mattress.
    """

    """
    I clutch at the arm that holds me, but my limbs feel heavy and slow, still dulled by sleep.

    My heart hammers so loudly that I can scarcely hear my own thoughts.
    """

    """
    Something cold touches the bare skin of my throat.

    For one dreadful instant I understand exactly what is about to happen.
    """

    """
    Pain sears across my neck in a sudden, burning line.

    Hot wetness spills down my collar, soaking the front of my shirt.
    """

    """
    I struggle blindly, fingers clawing at the air and at the implacable hand that silences me.

    My strength ebbs almost at once, as if it were pouring away with my blood.
    """

    jump doctor_ending_throat_cut