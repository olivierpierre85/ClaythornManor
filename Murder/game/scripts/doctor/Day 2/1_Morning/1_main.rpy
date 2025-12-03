# --------------------------------------------
#   Doctor
#           
#   Saturday - Morning
#   
#   08:30 -> 11:00
#
#   Music: chill
#
#   Alive: Everyone but Broken
#
#   Notes : 
#       - Generic Lad ?
# --------------------------------------------
label doctor_day2_morning:

    call change_time(8, 0, 'Morning', 'Saturday', hide_minutes=True, chapter='saturday_morning')

    $ current_character.add_checkpoint("doctor_day2_morning")

    call black_screen_transition("Daniel Baldwin", chapters_names[current_chapter])

    $ change_room("bedroom_doctor", irisout)

    $ play_music('upbeat', 3)

    """
    Awake, and alive.
    """

    if doctor_details.threads.is_unlocked('drunk_letter'):

        """
        Despite my suspicions, it seems no one tried to harm me in the night.

        It is a relief, though the weekend is far from over.

        I should prepare myself for breakfast.
        """

    else:

        """
        Strange how those two words came to mind first.

        An odd way to begin the day.

        No matter. I ought to prepare myself.
        """

    if doctor_details.threads.is_unlocked('book_opium'):

        """
        On most mornings, I would begin in the usual manner.

        But today is not most mornings.

        Today, I must be different.

        I resist the urge and wash thoroughly with cold water.

        Then I dress, ready to face the others over breakfast.
        """
    
    else: 

        """
        As always, I begin with my usual routine.
        """

        call wait_screen_transition

        """
        Much better. I feel calmer now—prepared to greet the day and those within it.
        """

    call change_time(9, 00)

    $ change_room('dining_room')

    """
    I take my seat at the breakfast table. Few have arrived so far.

    Aside from the staff, only Captain Sinha is present.

    He sits across the room and merely offers a silent nod in greeting.

    With nothing to do but eat, I quietly serve myself a plate.

    Gradually, the other guests begin to appear.

    Lady Claythorn and Rosalind Marsh enter together, deep in conversation.

    Lady Claythorn joins Captain Sinha.

    Rosalind Marsh sits beside me.

    I know it is not entirely proper to address someone across the table.

    But at present, she is the only one near enough to speak to.
    """

    $ time_left = 30 
    call run_menu(TimedMenu("doctor_day2_morning_nurse", [
        TimedMenuChoice("Talk to Rosalind Marsh", 'doctor_day2_morning_nurse', early_exit=True),
        TimedMenuChoice("Just keep to yourself", 'generic_cancel', early_exit=True),
    ], image_right = "nurse"))

    call change_time(9, 30)
    
    """
    Suddenly, our host approaches me.
    """

    call common_day2_morning_host_to_doctor

    call common_day2_breakfast_follow_doctor_lad_host

    $ change_room('dining_room')

    call change_time(10, 0)

    """
    When I reach the dining room, our host turns to me at once.
    """

    call common_day2_morning_host_death_doctor    

    """
    After a while, everyone has finished eating.
    """

    $ stop_music()

    call common_day2_morning_host_hunt

    """
    We are to go out on a hunt.

    I am not sure I feel up to it, and I do not think I am the only one.

    Everyone looks a little uncomfortable.

    Captain Sinha is the first to break the silence.
    """
        
    captain """
    I will come.

    What has happened today is tragic, but there is no point in lingering here.
    """

    drunk """
    I'll... come too. 

    Fresh air will do me well.
    """

    """
    I can see looks of disapproval at this.

    But no one dares say anything.

    Given Samuel Manning's obvious inebriety, most seem to assume he will fall asleep before the hunt even begins.
    """

    psychic """
    I am sorry, but I would rather not.

    If you do not mind, I should prefer to remain indoors.

    Please do not let me stand in your way.
    """

    nurse """
    I feel the same. 

    I should not know what to do with a gun.
    """

    host """
    Of course, I understand.
        
    I enjoy it myself, but I know that hunting is not to every lady's taste.

    I shall make sure you are comfortable staying inside.

    And how do you feel, Mister Harring?
    """

    lad """
    I'll... I'll come too, of course.
    """

    """
    He says it without much conviction.

    One can tell he is on the fence about the whole thing.
    """

    host """
    Very good. What about you, Doctor Baldwin?
    """

    """
    Everyone is looking towards me now.

    They clearly assume I shall go as well.
    """

    if doctor_details.threads.is_unlocked('remove_mask'):

        """
        Yet something troubles me.

        I cannot make sense of Thomas Moody not being truly injured.

        I do not understand it, and it makes me question everything.

        Something is not right, and a hunt is hardly the safest place to be.
        """
        
    elif doctor_details.threads.is_unlocked('book_opium'):

        """
        Yet I have not taken my 'medicine' today.

        Withdrawal could set in at any moment.

        In that case, it would be better to remain indoors and manage the symptoms.
        """

    if doctor_details.threads.is_unlocked('flirt'):

        """
        Besides, if I were to stay, I might spend a little more time with my new friend.
        """

    """
    So, which shall it be?
    """    

    $ time_left = TIME_MAX    
    call run_menu(
        TimedMenu("doctor_day2_morning_hunt", [
            TimedMenuChoice('Go on the hunt', 'doctor_day2_hunt_choice', early_exit = True),
            TimedMenuChoice('Stay here', 'doctor_day2_no_hunt_choice', early_exit = True)
        ])
    )

    host """
    Those of you who are going may change and then fetch a weapon downstairs.

    We shall meet outside in a little while.
    """

    jump doctor_day2_hunt


label doctor_day2_hunt_choice:

    doctor """
    I shall come as well.

    You are right. A distraction may serve us.
    """

    host """
    Excellent. That settles it, then. 
    """

    return


label doctor_day2_no_hunt_choice:

    doctor """
    I do not feel at all well.

    I think it would be wiser if I stayed.
    """

    host """
    I am sorry to hear it, Doctor. Are you quite sure?

    The weather has really improved today. It might do you good.
    """

    captain """
    Yes, there is nothing like fresh air to set a man right.

    And I do not wish to be dramatic, but it is always prudent to have a doctor with us.
    """

    """
    They are pressing me from all sides.

    I am not certain I can refuse now.

    Not without a very sound reason.
    """

    if doctor_details.threads.is_unlocked('drunk_letter'):

        """
        I do have one.

        Samuel Manning may very well use this hunt as an opportunity to harm me.

        To be alone with him, armed and far from the house, would be an unreasonable risk.

        Yet it would be difficult to refuse without exposing the contents of the letter.

        And there is a chance I could use the hunt to get an explanation out of Samuel Manning.

        I must simply remain alert at every moment.
        """


        # # TODO if intuition is unlocked
        # call run_menu(
        #     TimedMenu("doctor_day2_morning_no_hunt", [
        #         TimedMenuChoice("Pretend that you are in no condition for a hunt {{object}}", 'doctor_day2_no_hunt_choice_2', early_exit = True),
        #         TimedMenuChoice("You cannot resist the social pressure", 'doctor_day2_hunt_choice_2', early_exit = True)
        #     ])
        # )

    doctor """
    Perhaps you are right. The fine weather may do me good.

    I shall join you.
    """

    host """
    That is very good news.
    """

    return


# label doctor_day2_no_hunt_choice_2:

#     doctor """
#     I am truly sorry, but I do not think I should.

#     My condition requires a good deal of rest, I am afraid.
#     """

#     host """
#     If you say so. You are the doctor, after all.
#     """

#     jump work_in_progress



label doctor_day2_morning_nurse:

    doctor """
    Good morning, Miss Marsh.
    """

    nurse """
    Good morning, Doctor.
    """

    call nurse_generic

    return

# The rest in the common folder
label doctor_day2_breakfast_follow_doctor_lad_remove_mask:

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
    """

    call doctor_day2_behind_the_mask

    $ change_room("bedrooms_hallway")

    """
    Ted Harring is waiting in the hallway.
    """

    call common_day2_breakfast_follow_doctor_lad_normal

    return


label doctor_day2_behind_the_mask:
    
    """
    His face twisted in a horrible grimace.    

    This is not the face of someone dying peacefully in his sleep.

    It is very likely he was poisoned.

    And then, something strikes me.

    I should've noticed it at once.

    No disfigurement. No scars.

    His face is untouched.

    He never needed a mask.

    What does that mean?
    """

    $ doctor_details.threads.unlock('broken_unmasked')

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

    $ broken_details.description_hidden.unlock('lie_mask')
    
    return