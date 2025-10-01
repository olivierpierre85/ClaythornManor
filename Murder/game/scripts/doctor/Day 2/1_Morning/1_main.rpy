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

    jump work_in_progress


label doctor_day2_morning_nurse:

    doctor """
    Good morning, Miss Marsh.
    """

    nurse """
    Good morning, Doctor.
    """

    call nurse_generic

    return
