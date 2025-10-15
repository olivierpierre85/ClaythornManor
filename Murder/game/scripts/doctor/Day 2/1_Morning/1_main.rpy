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

    """
    Awake, and alive.

    Strange how those two words came to mind first.

    An odd way to begin the day.

    No matter. I ought to prepare myself.
    """

    if doctor_details.objects.is_unlocked('book_opium'):

        """
        On most mornings, I would begin in the usual manner.

        But today is not most mornings.

        Today, I must be different.

        I resist the urge and wash thoroughly with cold water.

        Then I dress, ready to face the others over breakfast.
        """
    
    else: 

        """
        As always, I begin with my usual "routine".
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
    Suddenly, our host approaches and interrupts the quiet.
    """

    call common_day2_morning_host_to_doctor

    call common_day2_breakfast_follow_doctor_lad_host

    $ change_room('dining_room')

    call change_time(10, 0)

    """
    When I reach the dining room, our host directly turns towards me.
    """

    call common_day2_morning_host_death_doctor    

    """
    After a while, everyone is done eating.
    """

    $ stop_music()

    call common_day2_morning_host_hunt

    """
    Going on a hunt now.

    I am not sure I feel up for it, and I don't think I am the only one.
    
    Everyone looks a bit uncomfortable.

    Captain Sinha is the first to break the silence.
    """
    
    captain """
    I will come.

    What happened today is tragic, but there is no point in waiting here.
    """

    drunk """
    I will... come too. 

    Fresh air will do me well.
    """


    """
    I can see looks of dissaproval at this.

    But nobody dares say something.

    Looking at Samuel Manning's obvious state of inebriety, I think everyone assumes he will fall asleep before the hunt begins.
    """

    
    psychic """
    I am sorry but I would rather not come, I would rather stay inside if you don't mind.

    But don't hold back on my account.
    """

    nurse """
    I feel the same. 

    I wouldn't know what to do with a gun.
    """

    host """
    Of course, I understand.
    
    Even though I enjoy it myself, I know that hunting is not something for any ladies.

    But I'll make sure you'll be comfortable staying inside.

    And how do you feel Mister Harring?
    """

    lad """
    I'll... I'll come too of course.
    """

    """
    He said that with a clear lack of confidence.

    You can tell he is on the fence about the whole thing.
    """

    host """
    All right, what about you Doctor Baldwin?
    """

    """
    Everyone is looking towards me now.

    They clearly assume I will go as well.
    """

    if doctor_details.important_choices.is_unlocked('remove_mask'):

        """
        But there is something bothering me.

        I can't make sense of the fact that Thomas Moody wasn't really injured.

        I don't understand it and it makes me question everything.

        There is something not right, and a hunt is not the best place to stay safe.
        """
    
    elif doctor_details.important_choices.is_unlocked('book_opium'):

        """
        Yet,  I haven't had my "medicine" today.

        So the withdrawal could start anytime soon.

        In that case, it would better to stay inside and manage the symptoms
        """


    if doctor_details.important_choices.is_unlocked('flirt'):

        """
        Also, if I stayed, I could spend more time with my new friend.
        """

    """
    So, which one will it be?
    """    


    $ time_left = TIME_MAX    
    call run_menu(
        TimedMenu("doctor_day2_morning_hunt", [
            TimedMenuChoice('Go on the hunt', 'doctor_day2_hunt_choice', early_exit = True),
            TimedMenuChoice('Stay here', 'doctor_day2_no_hunt_choice', early_exit = True)
        ])
    )

    host """
    Now, those of you going can change and then fetch a weapon downstairs.

    We'll meet outside in a little while.
    """

    return


label doctor_day2_hunt_choice:

    doctor """
    I'll come too.

    You are right, we could use the distraction.
    """

    host """
    Great that settles it then. 
    """

    return


label doctor_day2_no_hunt_choice:

    doctor """
    I don't feel that well actually.

    I think it would be better if I stayed actually.
    """

    host """
    I am sorry to hear that Doctor, are you sure?

    The weather has really improve today, it might do you good.
    """

    captain """
    Yes, there is nothing like fresh air to make you feel better.

    And I don't want to sound dramatic, but it's always good to have a doctor with us, in case anything happens.
    """

    """
    They all ganged up on me.

    I don't know that I can avoid going now.

    Not without a very good reason at least.
    """

    # TODO if intuition is unlocked
    # call run_menu(
    #     TimedMenu("doctor_day2_morning_no_hunt", [
    #         TimedMenuChoice('', '', early_exit = True),
    #         TimedMenuChoice('', '', early_exit = True)
    #     ])
    # )

    call doctor_day2_hunt_choice_2

    return


label doctor_day2_no_hunt_choice_2:

    doctor """
    I am truly sorry but I don't think I should.
    """

    host """
    Well if you say so. You are the doctor after all.
    """

    return

label doctor_day2_hunt_choice_2:

    doctor """
    You might be right, the good weather should do me good.

    I'll join too.
    """

    host """
    That's great news.
    """

    return


label doctor_day2_morning_nurse:

    doctor """
    Good morning, Miss Marsh.
    """

    nurse """
    Good morning, Doctor.
    """

    call nurse_generic

    return
